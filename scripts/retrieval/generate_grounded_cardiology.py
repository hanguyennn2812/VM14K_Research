#!/usr/bin/env python3
"""Create evidence-grounded Cardiology SFT candidates without opening test.

The script retrieves page-level Ministry of Health evidence with TF-IDF +
BGE-M3 reciprocal-rank fusion.  Qwen3 first drafts a cited explanation and
then performs a second strict support check.  The checker is deliberately
marked uncalibrated until the frozen 30-question retrieval gold set has been
reviewed; downstream export gates these rows by default.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

from evaluate_moh_retrieval import (
    corpus_fingerprint,
    dense_rankings,
    lexical_rankings,
    page_chunks,
    query_text,
    reciprocal_rank_fusion,
    specialty_folder,
)

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "cleaned" / "clean_final.jsonl"
SPLIT_PATH = ROOT / "splits" / "split_v1.json"
DEFAULT_OUTPUT = ROOT / "data" / "derived" / "grounded_vm14k.jsonl"
DEFAULT_REPORT = ROOT / "reports" / "training" / "grounded_cardiology_generation.json"
DEFAULT_CACHE = ROOT / "data" / "interim" / "moh_retrieval_cache"

DRAFT_SCHEMA = {
    "type": "object",
    "properties": {
        "support_label": {
            "type": "string",
            "enum": ["supported", "unsupported", "insufficient"],
        },
        "explanation": {"type": "string"},
        "claims": {
            "type": "array",
            "minItems": 1,
            "maxItems": 8,
            "items": {
                "type": "object",
                "properties": {
                    "claim": {"type": "string"},
                    "support_label": {
                        "type": "string",
                        "enum": ["supported", "unsupported", "insufficient"],
                    },
                    "cited_chunk_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "maxItems": 3,
                    },
                },
                "required": ["claim", "support_label", "cited_chunk_ids"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["support_label", "explanation", "claims"],
    "additionalProperties": False,
}

VERIFY_SCHEMA = {
    "type": "object",
    "properties": {
        "verification_label": {
            "type": "string",
            "enum": ["supported", "unsupported", "insufficient"],
        },
        "reason": {"type": "string"},
        "claim_checks": {
            "type": "array",
            "minItems": 1,
            "maxItems": 8,
            "items": {
                "type": "object",
                "properties": {
                    "claim": {"type": "string"},
                    "verification_label": {
                        "type": "string",
                        "enum": ["supported", "unsupported", "insufficient"],
                    },
                    "reason": {"type": "string"},
                    "cited_chunk_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "maxItems": 3,
                    },
                },
                "required": [
                    "claim",
                    "verification_label",
                    "reason",
                    "cited_chunk_ids",
                ],
                "additionalProperties": False,
            },
        },
    },
    "required": ["verification_label", "reason", "claim_checks"],
    "additionalProperties": False,
}


def stable_key(row: dict, seed: int) -> str:
    return hashlib.sha256(f"{seed}:{row['id']}".encode()).hexdigest()


def load_rows(
    topic: str,
    splits: set[str],
    limit: int | None,
    seed: int,
    include_ids: set[str] | None = None,
) -> list[dict]:
    if "test" in splits:
        raise ValueError("test is frozen and cannot be used to create or tune SFT data")
    split_by_id = json.loads(SPLIT_PATH.read_text(encoding="utf-8"))
    rows: list[dict] = []
    with DATA_PATH.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            if include_ids is not None and row["id"] not in include_ids:
                continue
            split = split_by_id.get(row["id"])
            if split not in splits or topic not in row.get("medical_topic", []):
                continue
            if row.get("contradiction_pending_review", False):
                continue
            if "??????" in row.get("question", ""):
                continue
            row = {**row, "split": split}
            rows.append(row)
    rows.sort(key=lambda row: stable_key(row, seed))
    return rows if limit is None else rows[:limit]


def render_options(row: dict) -> str:
    return "\n".join(
        f"{chr(65 + index)}. {option}"
        for index, option in enumerate(row["options"])
    )


def render_evidence(candidates: list[dict]) -> str:
    return "\n\n".join(
        (
            f"<evidence id=\"{item['chunk_id']}\" "
            f"source=\"{item['source_file']}\" page=\"{item['pdf_page']}\">\n"
            f"{item['text']}\n</evidence>"
        )
        for item in candidates
    )


def ollama_structured_chat(
    *,
    url: str,
    model: str,
    messages: list[dict],
    schema: dict,
    timeout_seconds: int,
) -> tuple[dict | None, str | None]:
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "think": False,
        "format": schema,
        "keep_alive": "30m",
        # 700 was too tight for the verifier: up to 8 claim_checks, each with a
        # cited_chunk_ids array *and* a free-text reason, in Vietnamese, inside a
        # single JSON object. Observed truncation mid-string on a 4-claim answer
        # (JSONDecodeError, "Unterminated string" ~2100 chars in) on 2026-08-28 —
        # normalize_verifier() then silently defaults truncated output to
        # "unsupported", which looks identical to a genuine evidence failure in
        # the report. Raised with headroom for the 8-claim ceiling.
        "options": {"temperature": 0, "seed": 42, "num_predict": 1600},
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            outer = json.load(response)
        content = outer["message"]["content"]
        parsed = json.loads(content)
        if not isinstance(parsed, dict):
            raise ValueError("structured content is not an object")
        return parsed, None
    except (
        urllib.error.HTTPError,
        urllib.error.URLError,
        TimeoutError,
        KeyError,
        TypeError,
        ValueError,
        json.JSONDecodeError,
    ) as exc:
        return None, repr(exc)


def minimum_claim_count(answer_text: str) -> int:
    """Conservative floor for visibly enumerated compound answer options."""
    return max(1, answer_text.count("+") + 1)


def normalize_draft(
    raw: dict | None, candidate_ids: set[str], minimum_claims: int
) -> dict:
    if raw is None:
        return {
            "support_label": "unsupported",
            "explanation": "",
            "cited_chunk_ids": [],
            "claims": [],
        }
    explanation = str(raw.get("explanation", "")).strip()
    claims: list[dict] = []
    raw_claims = raw.get("claims", [])
    if not isinstance(raw_claims, list):
        raw_claims = []
    for raw_claim in raw_claims[:8]:
        if not isinstance(raw_claim, dict):
            continue
        claim = str(raw_claim.get("claim", "")).strip()
        if not claim:
            continue
        claim_label = raw_claim.get("support_label")
        if claim_label not in {"supported", "unsupported", "insufficient"}:
            claim_label = "insufficient"
        cited = raw_claim.get("cited_chunk_ids", [])
        if not isinstance(cited, list):
            cited = []
        cited = list(dict.fromkeys(item for item in cited if item in candidate_ids))[:3]
        if claim_label == "supported" and not cited:
            claim_label = "insufficient"
        claims.append(
            {
                "claim": claim,
                "support_label": claim_label,
                "cited_chunk_ids": cited,
            }
        )
    claim_labels = [claim["support_label"] for claim in claims]
    if len(claims) < minimum_claims or not explanation or "unsupported" in claim_labels:
        label = "unsupported"
    elif "insufficient" in claim_labels or not claims:
        label = "insufficient"
    else:
        label = "supported"
    cited = list(
        dict.fromkeys(
            chunk_id
            for claim in claims
            for chunk_id in claim["cited_chunk_ids"]
        )
    )
    return {
        "support_label": label,
        "explanation": explanation,
        "cited_chunk_ids": cited,
        "claims": claims,
    }


def _normalize_claim_text(text: str) -> str:
    return " ".join(text.casefold().split())


def normalize_verifier(
    raw: dict | None,
    candidate_ids: set[str],
    minimum_claims: int,
    draft_claim_texts: set[str],
) -> dict:
    if raw is None:
        return {
            "verification_label": "unsupported",
            "reason": "verification call failed",
            "claim_checks": [],
        }
    checks: list[dict] = []
    raw_checks = raw.get("claim_checks", [])
    if not isinstance(raw_checks, list):
        raw_checks = []
    for raw_check in raw_checks[:8]:
        if not isinstance(raw_check, dict):
            continue
        claim = str(raw_check.get("claim", "")).strip()
        if not claim:
            continue
        label = raw_check.get("verification_label")
        if label not in {"supported", "unsupported", "insufficient"}:
            label = "insufficient"
        cited = raw_check.get("cited_chunk_ids", [])
        if not isinstance(cited, list):
            cited = []
        cited = list(dict.fromkeys(item for item in cited if item in candidate_ids))[:3]
        if label == "supported" and not cited:
            label = "insufficient"
        # The verifier is told to re-decompose the gold answer itself, but the
        # prompt also shows it all 4 options for context, and it sometimes
        # "helpfully" adds claim_checks fact-checking the *wrong* options too
        # (correctly finding them unsupported, since they're wrong). Those are
        # not claims about the gold answer and must never veto acceptance —
        # confirming a distractor is false is a good sign, not a rejection
        # reason. Observed 2026-08-28 on id db54dd9425224bb8b9ff0e034f8da9e7:
        # 4 correct claims all supported, 3 distractor claims correctly
        # unsupported, whole row wrongly rejected before this filter existed.
        in_scope = _normalize_claim_text(claim) in draft_claim_texts
        checks.append(
            {
                "claim": claim,
                "verification_label": label,
                "reason": str(raw_check.get("reason", "")).strip(),
                "cited_chunk_ids": cited,
                "in_scope": in_scope,
            }
        )
    scoped = [check for check in checks if check["in_scope"]] or checks
    labels = [check["verification_label"] for check in scoped]
    raw_label = raw.get("verification_label")
    if (
        raw_label != "supported"
        or len(scoped) < minimum_claims
        or any(label != "supported" for label in labels)
    ):
        final_label = "unsupported" if "unsupported" in labels else "insufficient"
    else:
        final_label = "supported"
    return {
        "verification_label": final_label,
        "reason": str(raw.get("reason", "")).strip(),
        "claim_checks": checks,
    }


def draft_messages(row: dict, candidates: list[dict]) -> list[dict]:
    answer_index = int(row["answer_index"])
    answer_text = row["options"][answer_index]
    system = (
        "Bạn là người gán nhãn bằng chứng y khoa nghiêm ngặt. Chỉ dùng các đoạn "
        "được cung cấp, không dùng kiến thức nhớ sẵn. Tách đáp án vàng thành từng "
        "claim nguyên tử (mỗi thuốc, liều, thủ thuật, điều kiện và thay đổi lối sống "
        "là một claim riêng). Chỉ chọn supported nếu MỌI claim được một đoạn trực "
        "tiếp chứng minh. Cùng chủ đề, danh mục viết tắt, hoặc bằng chứng gần đúng "
        "không đủ; thiếu bằng chứng cho một claim là insufficient, bằng chứng phủ "
        "định là unsupported, và mơ hồ cũng là insufficient. Giải thích "
        "ngắn bằng tiếng Việt và chỉ trích dẫn id có trong đầu vào."
    )
    user = (
        f"Câu hỏi:\n{row['question']}\n{render_options(row)}\n\n"
        f"Đáp án vàng cần kiểm tra: {row['answer']} — {answer_text}\n\n"
        f"Các đoạn ứng viên:\n{render_evidence(candidates)}\n\n"
        "Trả về đúng JSON theo schema. /no_think"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def verifier_messages(row: dict, draft: dict, cited: list[dict]) -> list[dict]:
    answer_text = row["options"][int(row["answer_index"])]
    system = (
        "Bạn là bộ kiểm định độc lập, thiên về bác bỏ. Chỉ chọn supported nếu các "
        "đoạn trích thực sự kéo theo đáp án vàng và toàn bộ giải thích, không cần "
        "kiến thức ngoài. Tự tách lại MỌI thuốc, liều, thủ thuật, điều kiện và thay "
        "đổi lối sống TRONG ĐÁP ÁN VÀNG (không phải trong các phương án khác); kiểm "
        "từng claim, kể cả claim draft có thể đã bỏ sót từ chính đáp án vàng. Các "
        "phương án khác chỉ để bạn hiểu ngữ cảnh câu hỏi — TUYỆT ĐỐI KHÔNG tạo thêm "
        "claim_checks để chấm các phương án đó; việc chúng sai không liên quan tới "
        "việc đáp án vàng có được hỗ trợ hay không. Danh mục viết tắt hoặc cùng chủ "
        "đề không phải bằng chứng. Thiếu chỉ một claim (của đáp án vàng) thì toàn bộ "
        "là insufficient; nếu bằng chứng phủ định thì là unsupported."
    )
    user = (
        f"Câu hỏi:\n{row['question']}\n{render_options(row)}\n\n"
        f"Đáp án vàng: {row['answer']} — {answer_text}\n"
        f"Giải thích cần kiểm định: {draft['explanation']}\n\n"
        f"Đoạn trích đã viện dẫn:\n{render_evidence(cited)}\n\n"
        "Trả về đúng JSON theo schema. /no_think"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def read_existing(path: Path) -> tuple[list[dict], set[str]]:
    if not path.exists():
        return [], set()
    with path.open(encoding="utf-8") as handle:
        rows = [json.loads(line) for line in handle if line.strip()]
    ids = [row["id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError(f"duplicate ids in existing output: {path}")
    return rows, set(ids)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", default="Cardiology")
    parser.add_argument("--specialty-vn", default="Tim mạch")
    parser.add_argument("--splits", nargs="+", choices=("train", "val"), default=("train", "val"))
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--ids",
        nargs="+",
        default=None,
        help="optional exact source ids for targeted smoke/review runs",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--fusion-depth", type=int, default=100)
    parser.add_argument("--chunk-words", type=int, default=180)
    parser.add_argument("--chunk-overlap", type=int, default=40)
    parser.add_argument("--embedding-model", default="bge-m3")
    parser.add_argument("--embedding-batch-size", type=int, default=32)
    parser.add_argument("--ollama-embed-url", default="http://127.0.0.1:11434/api/embed")
    parser.add_argument("--ollama-chat-url", default="http://127.0.0.1:11434/api/chat")
    parser.add_argument("--qwen-model", default="qwen3:8b")
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")
    if args.top_k < 1 or args.fusion_depth < args.top_k:
        parser.error("require 1 <= --top-k <= --fusion-depth")

    output_path = args.output if args.output.is_absolute() else ROOT / args.output
    report_path = args.report if args.report.is_absolute() else ROOT / args.report
    cache_dir = args.cache_dir if args.cache_dir.is_absolute() else ROOT / args.cache_dir
    if args.force:
        existing_rows, existing_ids = [], set()
    else:
        existing_rows, existing_ids = read_existing(output_path)

    include_ids = set(args.ids) if args.ids else None
    rows = load_rows(args.topic, set(args.splits), args.limit, args.seed, include_ids)
    if include_ids is not None:
        missing_ids = include_ids - {row["id"] for row in rows}
        if missing_ids:
            parser.error(
                "requested ids are not eligible in the selected topic/splits: "
                + ", ".join(sorted(missing_ids))
            )
    pending_rows = [row for row in rows if row["id"] not in existing_ids]
    if not pending_rows:
        print("No pending rows; existing output already covers this selection.")
        return

    folder = specialty_folder(args.specialty_vn)
    pdf_paths = sorted(folder.glob("*.pdf"), key=lambda path: path.name)
    fingerprint = corpus_fingerprint(pdf_paths, args.chunk_words, args.chunk_overlap)
    chunks = page_chunks(pdf_paths, args.chunk_words, args.chunk_overlap)
    by_chunk_id = {chunk["chunk_id"]: chunk for chunk in chunks}
    queries = [query_text(row) for row in pending_rows]
    lexical = lexical_rankings(queries, chunks, args.fusion_depth)
    dense = dense_rankings(
        queries,
        chunks,
        args.fusion_depth,
        args.embedding_model,
        None,
        args.embedding_batch_size,
        cache_dir,
        fingerprint,
        backend="ollama",
        ollama_url=args.ollama_embed_url,
        timeout_seconds=args.timeout,
    )
    hybrid = reciprocal_rank_fusion(lexical, dense, args.top_k)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    mode = "w" if args.force or not output_path.exists() else "a"
    generated: list[dict] = []
    with output_path.open(mode, encoding="utf-8") as handle:
        for number, (row, ranked) in enumerate(
            zip(pending_rows, hybrid, strict=True), start=1
        ):
            candidates = [
                {**by_chunk_id[item["chunk_id"]], "retrieval_score": item["score"]}
                for item in ranked
            ]
            candidate_ids = {item["chunk_id"] for item in candidates}
            answer_text = row["options"][int(row["answer_index"])]
            minimum_claims = minimum_claim_count(answer_text)
            raw_draft, draft_error = ollama_structured_chat(
                url=args.ollama_chat_url,
                model=args.qwen_model,
                messages=draft_messages(row, candidates),
                schema=DRAFT_SCHEMA,
                timeout_seconds=args.timeout,
            )
            draft = normalize_draft(raw_draft, candidate_ids, minimum_claims)
            cited = [
                by_chunk_id[chunk_id] for chunk_id in draft["cited_chunk_ids"]
            ]
            verifier = {
                "verification_label": "unsupported",
                "reason": "draft not supported",
                "claim_checks": [],
            }
            verify_error = None
            if draft["support_label"] == "supported":
                raw_verifier, verify_error = ollama_structured_chat(
                    url=args.ollama_chat_url,
                    model=args.qwen_model,
                    messages=verifier_messages(row, draft, cited),
                    schema=VERIFY_SCHEMA,
                    timeout_seconds=args.timeout,
                )
                draft_claim_texts = {
                    _normalize_claim_text(claim["claim"]) for claim in draft["claims"]
                }
                verifier = normalize_verifier(
                    raw_verifier, candidate_ids, minimum_claims, draft_claim_texts
                )
            verification_label = verifier.get("verification_label", "insufficient")
            accepted = (
                draft["support_label"] == "supported"
                and verification_label == "supported"
                and bool(cited)
            )
            citations = [
                {
                    "source_file": item["source_file"],
                    "source_sha256": item["source_sha256"],
                    "page_start": item["pdf_page"],
                    "page_end": item["pdf_page"],
                    "chunk_id": item["chunk_id"],
                    "passage": item["text"],
                }
                for item in cited
            ]
            result = {
                "id": row["id"],
                "split": row["split"],
                "medical_topic": row.get("medical_topic", []),
                "question": row["question"],
                "options": row["options"],
                "answer": row["answer"],
                "answer_index": row["answer_index"],
                "support_label": "supported" if accepted else "unsupported",
                "explanation": draft["explanation"] if accepted else "",
                "citations": citations if accepted else [],
                "verification_status": "uncalibrated_auto_check",
                "support_check": {
                    "draft_label": draft["support_label"],
                    "draft_claims": draft["claims"],
                    "verification_label": verification_label,
                    "verification_reason": str(verifier.get("reason", "")),
                    "verification_claims": verifier.get("claim_checks", []),
                    "minimum_claim_count": minimum_claims,
                    "draft_error": draft_error,
                    "verification_error": verify_error,
                    "model": args.qwen_model,
                    "method": "two_pass_same_model_claim_level_strict_v2",
                },
                "retrieval": {
                    "method": "rrf_tfidf_bge_m3",
                    "embedding_model": args.embedding_model,
                    "candidates": [
                        {
                            "chunk_id": item["chunk_id"],
                            "source_file": item["source_file"],
                            "source_sha256": item["source_sha256"],
                            "pdf_page": item["pdf_page"],
                            "score": item["retrieval_score"],
                            "snippet": item["text"][:500],
                        }
                        for item in candidates
                    ],
                },
            }
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")
            handle.flush()
            generated.append(result)
            print(
                f"[{number}/{len(pending_rows)}] {row['split']} {row['id']} "
                f"draft={draft['support_label']} verify={verification_label} "
                f"accepted={accepted}",
                flush=True,
            )

    all_rows = existing_rows + generated if mode == "a" else generated
    counts = collections.Counter(row["support_label"] for row in all_rows)
    # A checker call that errors (timeout, malformed/truncated JSON) is
    # normalize_verifier()'d into a plain "unsupported" row — indistinguishable
    # from a genuine evidence rejection unless someone opens support_check.*_error
    # on every row. Surface it in aggregate so a spike here is visible without that.
    checker_errors = sum(
        1
        for row in generated
        if row["support_check"]["draft_error"] or row["support_check"]["verification_error"]
    )
    try:
        output_display = str(output_path.relative_to(ROOT))
    except ValueError:
        output_display = str(output_path)
    report = {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "scope": "Cardiology train/validation only; test split never loaded",
        "output": output_display,
        "selected_rows": len(rows),
        "new_rows": len(generated),
        "total_output_rows": len(all_rows),
        "support_counts": dict(counts),
        "checker_errors_this_run": checker_errors,
        "verification_status": "uncalibrated_auto_check",
        "training_gate": (
            "Do not use as final SFT data until human verification or checker "
            "calibration passes on the frozen retrieval gold set."
        ),
        "retrieval": {
            "method": "reciprocal rank fusion of TF-IDF and BGE-M3",
            "embedding_model": args.embedding_model,
            "top_k": args.top_k,
            "fusion_depth": args.fusion_depth,
            "chunk_words": args.chunk_words,
            "chunk_overlap": args.chunk_overlap,
            "corpus_fingerprint_sha256": fingerprint,
            "pdf_files": len(pdf_paths),
            "page_chunks": len(chunks),
        },
        "support_checker": {
            "model": args.qwen_model,
            "method": "two-pass claim-level draft plus strict verification with structured JSON",
        },
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

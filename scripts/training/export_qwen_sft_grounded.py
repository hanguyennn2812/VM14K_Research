#!/usr/bin/env python3
"""Export only evidence-supported VM14K rows to grounded Qwen chat SFT.

Expected input rows are produced after retrieval, answer generation, and the
automatic support check.  Unsupported or incomplete rows are never converted
into training labels.  This replaces the answer-letter-only format for the new
grounded research direction; it does not replace the historical MCQ artifact.
"""
from __future__ import annotations

import argparse
import collections
import json
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE = ROOT / "data" / "derived" / "grounded_vm14k.jsonl"
DEFAULT_OUTPUT = ROOT / "data" / "derived" / "qwen_sft_grounded"
DEFAULT_REPORT = ROOT / "reports" / "training" / "qwen_sft_grounded_data_report.json"

SYSTEM = (
    "Bạn trả lời câu hỏi y khoa tiếng Việt chỉ dựa trên bằng chứng được cung cấp. "
    "Nêu đáp án, giải thích ngắn gọn và trích nguồn kèm số trang. "
    "Nếu bằng chứng không đủ, phải nói rõ là không đủ bằng chứng."
)


def render_options(options: list[str]) -> str:
    return "\n".join(f"{chr(65 + index)}. {option}" for index, option in enumerate(options))


def render_citations(citations: list[dict]) -> str:
    rendered: list[str] = []
    for index, citation in enumerate(citations, start=1):
        page_start = int(citation["page_start"])
        page_end = int(citation.get("page_end", page_start))
        pages = str(page_start) if page_start == page_end else f"{page_start}-{page_end}"
        rendered.append(f"[{index}] {citation['source_file']}, trang {pages}")
    return "\n".join(rendered)


def validate_supported(row: dict, allow_uncalibrated_auto_check: bool = False) -> str | None:
    if row.get("support_label") != "supported":
        return "not_supported"
    if row.get("split") not in {"train", "val", "test"}:
        return "invalid_split"
    if not row.get("explanation", "").strip():
        return "missing_explanation"
    verification_status = row.get("verification_status")
    allowed_verification = {"human_verified", "calibrated_auto_check"}
    if (
        verification_status not in allowed_verification
        and not allow_uncalibrated_auto_check
    ):
        return "evidence_not_verified"
    citations = row.get("citations", [])
    if not citations:
        return "missing_citations"
    for citation in citations:
        if not citation.get("source_file") or not citation.get("page_start"):
            return "invalid_citation"
        if not citation.get("passage", "").strip():
            return "missing_cited_passage"
    return None


def make_item(row: dict) -> dict:
    evidence = "\n\n".join(
        f"Nguồn [{index}] — {citation['source_file']}, trang {citation['page_start']}:\n"
        f"{citation['passage']}"
        for index, citation in enumerate(row["citations"], start=1)
    )
    user = (
        f"Bằng chứng:\n{evidence}\n\nCâu hỏi: {row['question']}\n"
        f"{render_options(row['options'])}\n\n/no_think"
    )
    assistant = (
        f"<think>\n\n</think>\n\nĐáp án: {row['answer']}\n"
        f"Giải thích: {row['explanation'].strip()}\n"
        f"Nguồn:\n{render_citations(row['citations'])}"
    )
    return {
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "metadata": {
            "source_id": row["id"],
            "split": row["split"],
            "support_label": row["support_label"],
            "verification_status": row.get("verification_status"),
            "citation_count": len(row["citations"]),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument(
        "--allow-uncalibrated-auto-check",
        action="store_true",
        help="exploratory pilot only; bypass human/calibrated evidence verification gate",
    )
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    source = args.source if args.source.is_absolute() else ROOT / args.source
    output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir
    report_path = args.report if args.report.is_absolute() else ROOT / args.report
    outputs = [output_dir / f"{split}.jsonl" for split in ("train", "val", "test")]
    existing = [path for path in outputs + [report_path] if path.exists()]
    if existing and not args.force:
        parser.error("outputs already exist; use --force: " + ", ".join(map(str, existing)))
    if not source.exists():
        parser.error(f"grounded source does not exist: {source}")

    accepted: dict[str, list[dict]] = {"train": [], "val": [], "test": []}
    rejected = collections.Counter()
    total = 0
    with source.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            total += 1
            row = json.loads(line)
            reason = validate_supported(row, args.allow_uncalibrated_auto_check)
            if reason:
                rejected[reason] += 1
                continue
            accepted[row["split"]].append(make_item(row))

    output_dir.mkdir(parents=True, exist_ok=True)
    for split, items in accepted.items():
        with (output_dir / f"{split}.jsonl").open("w", encoding="utf-8") as handle:
            for item in items:
                handle.write(json.dumps(item, ensure_ascii=False) + "\n")

    report = {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "source": str(source.relative_to(ROOT)),
        "purpose": "grounded answer + explanation + page-level source Qwen SFT",
        "input_rows": total,
        "accepted_per_split": {split: len(items) for split, items in accepted.items()},
        "rejected": dict(rejected),
        "safety_rule": "only support_label=supported with non-empty cited passages is exported",
        "verification_gate": (
            "human_verified or calibrated_auto_check required"
            if not args.allow_uncalibrated_auto_check
            else "BYPASSED for exploratory uncalibrated auto-check pilot"
        ),
        "augmentation": "none; evidence-bound explanations must not be detached from option text",
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

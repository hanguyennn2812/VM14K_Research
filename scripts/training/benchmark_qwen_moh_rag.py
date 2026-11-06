#!/usr/bin/env python3
"""Run the MoH-guideline RAG pilot from the original report with local Qwen.

For one clean specialty mapping (Cardiology -> Tim mạch by default), evaluate
the same frozen validation questions twice: (1) Qwen with question/options only
and (2) Qwen with the top-k TF-IDF chunks from the corresponding Ministry of
Health PDFs.  This is an evaluation pilot, not fine-tuning; test is untouched.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

import fitz
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "cleaned" / "clean_final.jsonl"
SPLIT_PATH = ROOT / "splits" / "split_v1.json"
CACHE_DIR = ROOT / "data" / "interim" / "moh_extract_cache"
REPORT_PATH = ROOT / "reports" / "training" / "qwen3_8b_moh_rag_cardiology_validation.json"
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
ANSWER_RE = re.compile(r"(?:đáp\s*án|answer)\s*[:\-]?\s*([A-G])\b", re.IGNORECASE)
LETTER_RE = re.compile(r"\b([A-G])\b", re.IGNORECASE)


def fix_mojibake(name: str) -> str:
    try:
        return name.encode("cp437").decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        return name


def specialty_folder(specialty_vn: str) -> Path:
    parent = next(p for p in (ROOT / "data").iterdir() if p.is_dir() and "khoa" in p.name.casefold())
    return next(p for p in parent.iterdir() if p.is_dir() and fix_mojibake(p.name) == specialty_vn)


def group_pdf_parts(paths: list[Path]) -> dict[str, list[Path]]:
    part_re = re.compile(r"^(?P<base>.+?)_part(?P<num>\d+)(?:\s*\(\d+\))?\.pdf$", re.IGNORECASE)
    grouped: dict[str, list[tuple[int, Path]]] = {}
    for path in paths:
        match = part_re.match(path.name)
        if match:
            grouped.setdefault(match.group("base"), []).append((int(match.group("num")), path))
        else:
            grouped.setdefault(path.stem, []).append((0, path))
    return {key: [path for _, path in sorted(values)] for key, values in grouped.items()}


def extract_documents(folder: Path) -> list[dict]:
    """Extract born-digital PDFs, cache by the specialty folder display name."""
    cache = CACHE_DIR / f"{hashlib.sha256(str(folder).encode()).hexdigest()[:12]}.jsonl"
    if cache.exists():
        with cache.open(encoding="utf-8") as fh:
            return [json.loads(line) for line in fh if line.strip()]

    documents = []
    for doc_id, parts in group_pdf_parts(sorted(folder.glob("*.pdf"))).items():
        text_parts, sources, pages = [], [], 0
        for path in parts:
            with fitz.open(path) as pdf:
                text = "\n".join(page.get_text() for page in pdf)
                pages += pdf.page_count
            text_parts.append(text)
            sources.append(path.name)
        text = "\n\n".join(text_parts)
        chars_per_page = len(re.sub(r"\s+", "", text)) / max(pages, 1)
        # Report's criterion: scans with effectively no extractable text are not
        # silently used as RAG evidence.
        if chars_per_page >= 50:
            documents.append({"doc_id": doc_id, "source_files": sources, "text": text})
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with cache.open("w", encoding="utf-8") as fh:
        for document in documents:
            fh.write(json.dumps(document, ensure_ascii=False) + "\n")
    return documents


def chunk_documents(documents: list[dict], words: int, overlap: int) -> tuple[list[str], list[str]]:
    chunks, doc_ids = [], []
    step = max(1, words - overlap)
    for document in documents:
        tokens = document["text"].split()
        for start in range(0, len(tokens), step):
            chunk = " ".join(tokens[start:start + words])
            if chunk:
                chunks.append(chunk)
                doc_ids.append(document["doc_id"])
    return chunks, doc_ids


def load_validation_rows(topic: str, limit: int, seed: int) -> list[dict]:
    split_by_id = json.loads(SPLIT_PATH.read_text(encoding="utf-8"))
    with DATA_PATH.open(encoding="utf-8") as fh:
        rows = [
            json.loads(line) for line in fh if line.strip()
            and split_by_id.get(json.loads(line)["id"]) == "val"
            and topic in json.loads(line).get("medical_topic", [])
            and not json.loads(line).get("contradiction_pending_review", False)
        ]
    random.Random(seed).shuffle(rows)
    return rows[:limit]


def build_messages(question: str, options: list[str], contexts: list[str]) -> list[dict]:
    letters = [chr(65 + i) for i in range(len(options))]
    option_text = "\n".join(f"{letter}. {option}" for letter, option in zip(letters, options))
    context_text = ""
    if contexts:
        context_text = "Tài liệu hướng dẫn Bộ Y tế tham khảo:\n" + "\n---\n".join(contexts) + "\n\n"
    return [
        {
            "role": "system",
            "content": (
                "Bạn là bác sĩ chuyên khoa làm bài trắc nghiệm y khoa tiếng Việt. "
                "Chọn một đáp án đúng nhất. Chỉ trả lời đúng định dạng `Đáp án: X`, "
                "trong đó X là một chữ cái của các lựa chọn; không giải thích."
            ),
        },
        {"role": "user", "content": f"{context_text}Câu hỏi: {question}\n{option_text}\n\nĐáp án:"},
    ]


def qwen_answer(messages: list[dict], model: str) -> tuple[str | None, str | None, str | None]:
    payload = {
        "model": model, "stream": False, "think": False,
        "options": {"temperature": 0, "seed": 42, "num_predict": 16}, "messages": messages,
    }
    request = urllib.request.Request(
        OLLAMA_URL, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            raw = json.load(response)["message"]["content"]
        match = ANSWER_RE.search(raw) or LETTER_RE.search(raw.strip())
        return (match.group(1).upper() if match else None), raw, None
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError, json.JSONDecodeError) as exc:
        return None, None, repr(exc)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--specialty-vn", default="Tim mạch")
    ap.add_argument("--topic", default="Cardiology")
    ap.add_argument("--model", default="qwen3:8b")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--top-k", type=int, default=3)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    if REPORT_PATH.exists() and not args.force:
        ap.error(f"{REPORT_PATH} exists; use --force to replace it")

    folder = specialty_folder(args.specialty_vn)
    documents = extract_documents(folder)
    chunks, doc_ids = chunk_documents(documents, words=180, overlap=40)
    if not chunks:
        raise RuntimeError(f"No born-digital text extracted from {folder}")
    vectorizer = TfidfVectorizer(max_features=20_000)
    matrix = vectorizer.fit_transform(chunks)
    rows = load_validation_rows(args.topic, args.limit, args.seed)
    if not rows:
        raise RuntimeError(f"No validation rows found for topic {args.topic}")

    results = []
    for number, row in enumerate(rows, start=1):
        similarities = cosine_similarity(vectorizer.transform([row["question"]]), matrix)[0]
        indices = np.argsort(similarities)[::-1][:args.top_k]
        contexts = [chunks[i] for i in indices if similarities[i] > 0]
        retrieved = [{"doc_id": doc_ids[i], "score": round(float(similarities[i]), 4)} for i in indices if similarities[i] > 0]
        for condition, evidence in (("baseline", []), ("rag", contexts)):
            prediction, raw, error = qwen_answer(build_messages(row["question"], row["options"], evidence), args.model)
            results.append({
                "id": row["id"], "condition": condition, "gold_answer": row["answer"],
                "predicted_answer": prediction, "correct": prediction == row["answer"],
                "raw_response": raw, "error": error,
                "retrieved_chunks": retrieved if condition == "rag" else [],
            })
        print(f"[{number}/{len(rows)}] {row['id']} gold={row['answer']} baseline={results[-2]['predicted_answer']} rag={results[-1]['predicted_answer']}", flush=True)

    summary = {}
    for condition in ("baseline", "rag"):
        subset = [r for r in results if r["condition"] == condition]
        answered = [r for r in subset if r["predicted_answer"] is not None]
        summary[condition] = {
            "n": len(subset), "accuracy": round(sum(r["correct"] for r in subset) / len(subset), 4),
            "parse_rate": round(len(answered) / len(subset), 4),
        }
    report = {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "scope": "validation-only MoH RAG pilot; frozen test split not accessed",
        "model": args.model, "specialty_vn": args.specialty_vn, "vm14k_topic": args.topic,
        "source_pdf_folder": str(folder.relative_to(ROOT)), "born_digital_documents": len(documents),
        "chunks": len(chunks), "top_k": args.top_k, "sample_size": len(rows), "seed": args.seed,
        "summary": summary, "results": results,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Summary:", summary)
    print("wrote", REPORT_PATH.relative_to(ROOT))


if __name__ == "__main__":
    main()

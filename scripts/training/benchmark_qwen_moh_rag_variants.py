#!/usr/bin/env python3
"""Validation-only ablation study of five local-Qwen MCQ answering strategies.

The study keeps the VM14K question set, frozen split, Qwen model, answer parser,
and specialty fixed.  Only the context strategy changes, making it suitable for
selecting a RAG setup before one final test evaluation.
"""
from __future__ import annotations

import argparse
import collections
import json
import random
from datetime import UTC, datetime
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from benchmark_qwen_moh_rag import (
    DATA_PATH,
    REPORT_PATH,
    ROOT,
    SPLIT_PATH,
    build_messages,
    chunk_documents,
    extract_documents,
    load_validation_rows,
    qwen_answer,
    specialty_folder,
)

OUT = ROOT / "reports" / "training" / "qwen3_8b_moh_rag_ablation_cardiology_validation.json"
SUMMARY = ROOT / "reports" / "training" / "BAO_CAO_QWEN_RAG_ABLATION.md"


def load_train_rows(topic: str) -> list[dict]:
    splits = json.loads(SPLIT_PATH.read_text(encoding="utf-8"))
    with DATA_PATH.open(encoding="utf-8") as fh:
        rows = [json.loads(line) for line in fh if line.strip()]
    return [
        row for row in rows
        if splits.get(row["id"]) == "train" and topic in row.get("medical_topic", [])
        and not row.get("contradiction_pending_review", False)
    ]


def answer_options(row: dict) -> str:
    return "\n".join(f"{chr(65 + i)}. {option}" for i, option in enumerate(row["options"]))


def nearest_examples(query: str, matrix, rows: list[dict], vectorizer, k: int = 2) -> list[str]:
    sims = cosine_similarity(vectorizer.transform([query]), matrix)[0]
    indices = np.argsort(sims)[::-1][:k]
    return [
        "Ví dụ đã gán nhãn:\n"
        f"Câu hỏi: {rows[i]['question']}\n{answer_options(rows[i])}\nĐáp án: {rows[i]['answer']}"
        for i in indices if sims[i] > 0
    ]


def top_chunks(scores: np.ndarray, chunks: list[str], doc_ids: list[str], k: int, diverse: bool) -> tuple[list[str], list[dict]]:
    chosen, evidence, used_docs = [], [], set()
    for i in np.argsort(scores)[::-1]:
        if scores[i] <= 0:
            break
        if diverse and doc_ids[i] in used_docs:
            continue
        chosen.append(chunks[i])
        evidence.append({"doc_id": doc_ids[i], "score": round(float(scores[i]), 4)})
        used_docs.add(doc_ids[i])
        if len(chosen) == k:
            break
    return chosen, evidence


def messages_with_examples(question: str, options: list[str], contexts: list[str], examples: list[str]) -> list[dict]:
    messages = build_messages(question, options, contexts)
    if examples:
        messages[1]["content"] = "\n\n".join(examples) + "\n\n" + messages[1]["content"]
    return messages


def summarize(results: list[dict]) -> dict:
    grouped = collections.defaultdict(list)
    for result in results:
        grouped[result["condition"]].append(result)
    baseline = {r["id"]: r for r in grouped["zero_shot"]}
    summary = {}
    for condition, rows in grouped.items():
        correct = sum(r["correct"] for r in rows)
        parse_rate = sum(r["predicted_answer"] is not None for r in rows) / len(rows)
        compared = collections.Counter((baseline[r["id"]]["correct"], r["correct"]) for r in rows)
        summary[condition] = {
            "n": len(rows), "accuracy": round(correct / len(rows), 4), "correct": correct,
            "parse_rate": round(parse_rate, 4),
            "versus_zero_shot_transition_counts": {
                "both_correct": compared[(True, True)], "both_wrong": compared[(False, False)],
                "zero_shot_only_correct": compared[(True, False)], "strategy_only_correct": compared[(False, True)],
            },
        }
    return summary


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--specialty-vn", default="Tim mạch")
    ap.add_argument("--topic", default="Cardiology")
    ap.add_argument("--model", default="qwen3:8b")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    if (OUT.exists() or SUMMARY.exists()) and not args.force:
        ap.error(f"outputs already exist; use --force: {OUT}, {SUMMARY}")

    folder = specialty_folder(args.specialty_vn)
    documents = extract_documents(folder)
    chunks, doc_ids = chunk_documents(documents, words=180, overlap=40)
    doc_vectorizer = TfidfVectorizer(max_features=20_000)
    doc_matrix = doc_vectorizer.fit_transform(chunks)
    train_rows = load_train_rows(args.topic)
    train_texts = [f"{row['question']}\n{answer_options(row)}" for row in train_rows]
    example_vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=20_000)
    example_matrix = example_vectorizer.fit_transform(train_texts)
    val_rows = load_validation_rows(args.topic, args.limit, args.seed)
    if not val_rows:
        raise RuntimeError("no validation rows")

    # Conditions form a compact ablation: standard RAG, document-diverse RAG,
    # supervised in-context examples, and a combined setup.
    conditions = ["zero_shot", "tfidf_top3", "diverse_doc_top3", "few_shot_2", "diverse_rag_plus_few_shot"]
    results = []
    for number, row in enumerate(val_rows, start=1):
        scores = cosine_similarity(doc_vectorizer.transform([row["question"]]), doc_matrix)[0]
        standard_chunks, standard_evidence = top_chunks(scores, chunks, doc_ids, k=3, diverse=False)
        diverse_chunks, diverse_evidence = top_chunks(scores, chunks, doc_ids, k=3, diverse=True)
        examples = nearest_examples(row["question"], example_matrix, train_rows, example_vectorizer, k=2)
        payloads = {
            "zero_shot": ([], []),
            "tfidf_top3": (standard_chunks, []),
            "diverse_doc_top3": (diverse_chunks, []),
            "few_shot_2": ([], examples),
            "diverse_rag_plus_few_shot": (diverse_chunks[:2], examples[:1]),
        }
        row_predictions = {}
        for condition in conditions:
            contexts, examples_for_prompt = payloads[condition]
            prediction, raw, error = qwen_answer(
                messages_with_examples(row["question"], row["options"], contexts, examples_for_prompt), args.model
            )
            row_predictions[condition] = prediction
            results.append({
                "id": row["id"], "condition": condition, "gold_answer": row["answer"],
                "predicted_answer": prediction, "correct": prediction == row["answer"],
                "raw_response": raw, "error": error,
                "standard_tfidf_evidence": standard_evidence,
                "diverse_tfidf_evidence": diverse_evidence,
                "few_shot_example_ids": [r["id"] for r in train_rows if any(r["question"] in text for text in examples)],
            })
        print(
            f"[{number}/{len(val_rows)}] {row['id']} gold={row['answer']} "
            + " ".join(f"{name}={row_predictions[name] or '-'}" for name in conditions), flush=True
        )

    summary = summarize(results)
    report = {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "scope": "validation-only ablation; frozen test split was not accessed",
        "model": args.model, "specialty_vn": args.specialty_vn, "vm14k_topic": args.topic,
        "sample_size": len(val_rows), "seed": args.seed, "train_examples_available": len(train_rows),
        "born_digital_documents": len(documents), "chunks": len(chunks), "conditions": conditions,
        "summary": summary, "results": results,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Qwen3 8B — ablation RAG/few-shot (validation Tim mạch)", "",
        "Cùng Qwen, cùng 20 câu validation, cùng parser. Chỉ cách cấp ngữ cảnh thay đổi.", "",
        "| Hướng | Accuracy | Đúng / n |", "|---|---:|---:|",
    ]
    for condition in conditions:
        value = summary[condition]
        lines.append(f"| {condition} | {value['accuracy']:.1%} | {value['correct']}/{value['n']} |")
    lines.extend(["", "Tập test không được truy cập trong ablation này."])
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Summary:", json.dumps(summary, ensure_ascii=False))
    print("wrote", OUT.relative_to(ROOT), "and", SUMMARY.relative_to(ROOT))


if __name__ == "__main__":
    main()

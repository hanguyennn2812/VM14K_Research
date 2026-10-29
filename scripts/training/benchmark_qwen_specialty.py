#!/usr/bin/env python3
"""Fair validation-only pilot: local Qwen versus the TF-IDF specialty baseline.

Uses Ollama's local API, never sends any dataset content to an external service,
and deliberately evaluates only the frozen validation split.  The held-out test
set remains untouched until a model/prompt is selected.
"""
from __future__ import annotations

import argparse
import json
import random
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

import joblib
import numpy as np
from sklearn.metrics import f1_score, hamming_loss
from sklearn.preprocessing import MultiLabelBinarizer

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "derived" / "specialty_clear.jsonl"
BASELINE = ROOT / "models" / "specialty_multilabel_tfidf_logreg.joblib"
OUT = ROOT / "reports" / "training" / "qwen3_8b_validation_pilot.json"
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"


def load_rows() -> list[dict]:
    with DATA.open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip() and json.loads(line)["split"] == "val"]


def sample_rows(rows: list[dict], limit: int, seed: int) -> list[dict]:
    """Cover all specialties first, then fill randomly; deterministic by seed."""
    rng = random.Random(seed)
    remaining = rows[:]
    rng.shuffle(remaining)
    chosen, covered = [], set()
    while remaining and len(chosen) < limit:
        best = max(remaining, key=lambda r: len(set(r["canonical_specialties"]) - covered))
        gain = set(best["canonical_specialties"]) - covered
        if not gain:
            break
        chosen.append(best)
        covered.update(gain)
        remaining.remove(best)
    rng.shuffle(remaining)
    chosen.extend(remaining[: max(0, limit - len(chosen))])
    return chosen


def prompt_for(row: dict, labels: list[str]) -> list[dict]:
    choices = "\n".join(f"{i + 1}. {label}" for i, label in enumerate(labels))
    options = "\n".join(f"- {option}" for option in row["options"])
    return [
        {
            "role": "system",
            "content": (
                "Bạn là bộ phân loại chuyên khoa y khoa phục vụ nghiên cứu. "
                "Chỉ chọn chuyên khoa trực tiếp phù hợp với nội dung câu hỏi và các lựa chọn; "
                "một câu có thể có nhiều chuyên khoa. Không chẩn đoán, không giải thích. "
                "Trả duy nhất JSON hợp lệ: {\"specialties\":[\"tên đúng trong danh sách\"]}."
            ),
        },
        {
            "role": "user",
            "content": f"Danh sách chuyên khoa hợp lệ:\n{choices}\n\nCâu hỏi:\n{row['question']}\n\nLựa chọn:\n{options}",
        },
    ]


def qwen_predict(row: dict, labels: list[str], model: str) -> tuple[list[str], str | None]:
    payload = {
        "model": model, "stream": False, "think": False, "format": "json",
        "options": {"temperature": 0, "seed": 42}, "messages": prompt_for(row, labels),
    }
    request = urllib.request.Request(
        OLLAMA_URL, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            content = json.load(response)["message"]["content"]
        parsed = json.loads(content)
        values = parsed.get("specialties", [])
        if not isinstance(values, list):
            raise ValueError("specialties is not a JSON list")
        invalid = [value for value in values if value not in labels]
        if invalid:
            raise ValueError(f"labels outside the allowed list: {invalid}")
        return sorted(set(values)), None
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError, json.JSONDecodeError) as exc:
        return [], str(exc)


def to_matrix(label_sets: list[list[str]], labels: list[str]) -> np.ndarray:
    return MultiLabelBinarizer(classes=labels).fit_transform(label_sets)


def metrics(gold: np.ndarray, predicted: np.ndarray) -> dict:
    return {
        "micro_f1": round(float(f1_score(gold, predicted, average="micro", zero_division=0)), 4),
        "macro_f1": round(float(f1_score(gold, predicted, average="macro", zero_division=0)), 4),
        "exact_match_accuracy": round(float((gold == predicted).all(axis=1).mean()), 4),
        "hamming_loss": round(float(hamming_loss(gold, predicted)), 4),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", default="qwen3:8b")
    ap.add_argument("--limit", type=int, default=50)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    if OUT.exists() and not args.force:
        ap.error(f"{OUT} exists; use --force to replace it")
    if not DATA.exists() or not BASELINE.exists():
        ap.error("run train_specialty_classifier.py first")

    rows = sample_rows(load_rows(), args.limit, args.seed)
    artifact = joblib.load(BASELINE)
    labels, threshold = artifact["labels"], artifact["threshold"]
    qwen_predictions, errors = [], []
    for n, row in enumerate(rows, start=1):
        prediction, error = qwen_predict(row, labels, args.model)
        qwen_predictions.append(prediction)
        if error:
            errors.append({"id": row["id"], "error": error})
        print(f"[{n}/{len(rows)}] {row['id']} -> {', '.join(prediction) or 'NO_VALID_LABEL'}", flush=True)

    gold = to_matrix([row["canonical_specialties"] for row in rows], labels)
    qwen = to_matrix(qwen_predictions, labels)
    feature_texts = [
        "Câu hỏi: " + row["question"] + "\n" + "\n".join(
            f"Lựa chọn {i + 1}: {option}" for i, option in enumerate(row["options"])
        )
        for row in rows
    ]
    baseline_probs = artifact["model"].predict_proba(artifact["vectorizer"].transform(feature_texts))
    baseline = baseline_probs >= threshold
    none = ~baseline.any(axis=1)
    baseline[none, baseline_probs[none].argmax(axis=1)] = True

    result = {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "scope": "validation pilot only; frozen test split was not accessed",
        "model": args.model, "rows": len(rows), "seed": args.seed,
        "qwen_metrics": metrics(gold, qwen),
        "tfidf_baseline_metrics_on_same_rows": metrics(gold, baseline),
        "invalid_or_failed_qwen_responses": errors,
        "examples": [
            {"id": row["id"], "question": row["question"], "gold": row["canonical_specialties"],
             "qwen_prediction": prediction}
            for row, prediction in zip(rows, qwen_predictions)
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Qwen:", result["qwen_metrics"])
    print("TF-IDF same rows:", result["tfidf_baseline_metrics_on_same_rows"])
    print("wrote", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()

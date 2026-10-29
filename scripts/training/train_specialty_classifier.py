#!/usr/bin/env python3
"""Build a strict specialty dataset and train a reproducible multi-label baseline.

The released VM14K labels include clinical specialties alongside pre-clinical,
administrative, and otherwise ambiguous topics.  This script only retains a
question when *every* original topic can be mapped unambiguously to one of the
paper's 34 canonical specialties (MATCH or AUTO in propose_topic_mapping.py).
It preserves valid multi-specialty labels instead of arbitrarily picking one.

Outputs are intentionally separate from the audited cleaned source dataset:

* data/derived/specialty_clear.jsonl
* reports/training/specialty_data_report.json
* models/specialty_multilabel_tfidf_logreg.joblib
* reports/training/specialty_model_report.json
* reports/training/specialty_demo_samples.md
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, hamming_loss, precision_recall_fscore_support
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import FeatureUnion
from sklearn.preprocessing import MultiLabelBinarizer

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts" / "analysis"))
from propose_topic_mapping import CANONICAL_34, classify  # noqa: E402

SOURCE = REPO_ROOT / "data" / "cleaned" / "clean_final.jsonl"
SPLITS = REPO_ROOT / "splits" / "split_v1.json"
DERIVED = REPO_ROOT / "data" / "derived" / "specialty_clear.jsonl"
DATA_REPORT = REPO_ROOT / "reports" / "training" / "specialty_data_report.json"
MODEL_PATH = REPO_ROOT / "models" / "specialty_multilabel_tfidf_logreg.joblib"
MODEL_REPORT = REPO_ROOT / "reports" / "training" / "specialty_model_report.json"
DEMO_PATH = REPO_ROOT / "reports" / "training" / "specialty_demo_samples.md"


def load_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def feature_text(row: dict) -> str:
    """Use only information available before knowing the correct option."""
    options = "\n".join(f"Lựa chọn {i + 1}: {value}" for i, value in enumerate(row["options"]))
    return f"Câu hỏi: {row['question']}\n{options}"


def strict_rows(rows: list[dict], split_by_id: dict[str, str]):
    kept, removed = [], collections.Counter()
    for row in rows:
        mapped, unclear = [], []
        for raw in row["medical_topic"]:
            specialty, decision, _ = classify(raw)
            if decision in {"MATCH", "AUTO"}:
                mapped.append(specialty)
            else:
                unclear.append({"topic": raw, "decision": decision})

        if unclear:
            removed["ambiguous_or_non_specialty_topic"] += 1
            continue
        if not mapped:
            removed["no_resolved_specialty"] += 1
            continue
        if row.get("contradiction_pending_review", False):
            removed["answer_key_pending_review"] += 1
            continue
        if row["id"] not in split_by_id:
            removed["missing_frozen_split"] += 1
            continue

        new_row = dict(row)
        new_row["canonical_specialties"] = sorted(set(mapped))
        new_row["split"] = split_by_id[row["id"]]
        kept.append(new_row)
    return kept, removed


def select_threshold(y_true: np.ndarray, probabilities: np.ndarray) -> tuple[float, float]:
    """Tune one global threshold solely on validation data."""
    best = (0.5, -1.0)
    for threshold in np.arange(0.20, 0.81, 0.05):
        score = f1_score(y_true, probabilities >= threshold, average="micro", zero_division=0)
        if score > best[1]:
            best = (round(float(threshold), 2), float(score))
    return best


def predict_at_least_one(probabilities: np.ndarray, threshold: float) -> np.ndarray:
    predicted = probabilities >= threshold
    # A specialty classifier should always return a reviewable candidate instead
    # of an empty set; the report makes this behavior explicit.
    empty = ~predicted.any(axis=1)
    if empty.any():
        predicted[empty, probabilities[empty].argmax(axis=1)] = True
    return predicted


def evaluate(y_true: np.ndarray, probabilities: np.ndarray, labels: list[str], threshold: float) -> dict:
    predicted = predict_at_least_one(probabilities.copy(), threshold)
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, predicted, average=None, zero_division=0
    )
    per_label = [
        {
            "specialty": label,
            "support": int(s),
            "precision": round(float(p), 4),
            "recall": round(float(r), 4),
            "f1": round(float(v), 4),
        }
        for label, p, r, v, s in zip(labels, precision, recall, f1, support)
    ]
    return {
        "rows": int(y_true.shape[0]),
        "micro_f1": round(float(f1_score(y_true, predicted, average="micro", zero_division=0)), 4),
        "macro_f1": round(float(f1_score(y_true, predicted, average="macro", zero_division=0)), 4),
        "exact_match_accuracy": round(float((y_true == predicted).all(axis=1).mean()), 4),
        "hamming_loss": round(float(hamming_loss(y_true, predicted)), 4),
        "per_specialty": per_label,
    }


def write_json(path: Path, content: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="overwrite generated artifacts")
    args = parser.parse_args()
    outputs = [DERIVED, DATA_REPORT, MODEL_PATH, MODEL_REPORT, DEMO_PATH]
    existing = [p for p in outputs if p.exists()]
    if existing and not args.force:
        parser.error("outputs already exist; rerun with --force: " + ", ".join(map(str, existing)))

    rows = load_jsonl(SOURCE)
    split_by_id = json.loads(SPLITS.read_text(encoding="utf-8"))
    strict, removal_counts = strict_rows(rows, split_by_id)
    if not strict:
        raise RuntimeError("strict specialty filter produced zero rows")

    derived_rows = [
        {
            "id": r["id"], "question": r["question"], "options": r["options"],
            "canonical_specialties": r["canonical_specialties"], "split": r["split"],
        }
        for r in strict
    ]
    DERIVED.parent.mkdir(parents=True, exist_ok=True)
    with DERIVED.open("w", encoding="utf-8") as fh:
        for row in derived_rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    labels = CANONICAL_34
    mlb = MultiLabelBinarizer(classes=labels)
    y = mlb.fit_transform([r["canonical_specialties"] for r in strict])
    texts = [feature_text(r) for r in strict]
    indices = {split: [i for i, r in enumerate(strict) if r["split"] == split] for split in ("train", "val", "test")}
    if not all(indices.values()):
        raise RuntimeError(f"an empty split was produced: { {k: len(v) for k, v in indices.items()} }")

    vectorizer = FeatureUnion([
        ("word", TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True, max_features=100_000)),
        ("char", TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), min_df=2, sublinear_tf=True, max_features=100_000)),
    ])
    train_i, val_i, test_i = indices["train"], indices["val"], indices["test"]
    x_train = vectorizer.fit_transform([texts[i] for i in train_i])
    x_val = vectorizer.transform([texts[i] for i in val_i])
    x_test = vectorizer.transform([texts[i] for i in test_i])
    model = OneVsRestClassifier(
        LogisticRegression(max_iter=1000, class_weight="balanced", solver="liblinear", random_state=42)
    )
    model.fit(x_train, y[train_i])
    val_prob = model.predict_proba(x_val)
    threshold, tuning_f1 = select_threshold(y[val_i], val_prob)
    val_metrics = evaluate(y[val_i], val_prob, labels, threshold)
    test_prob = model.predict_proba(x_test)
    test_metrics = evaluate(y[test_i], test_prob, labels, threshold)

    data_report = {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "source": str(SOURCE.relative_to(REPO_ROOT)),
        "filter": "retain only rows whose every source topic has a MATCH/AUTO canonical mapping; exclude answer_key_pending_review",
        "canonical_specialty_count": len(labels),
        "input_rows": len(rows),
        "retained_rows": len(strict),
        "removed_rows": len(rows) - len(strict),
        "removal_counts": dict(removal_counts),
        "split_counts": {name: len(value) for name, value in indices.items()},
        "label_cardinality_distribution": dict(sorted(collections.Counter(len(r["canonical_specialties"]) for r in strict).items())),
        "specialty_row_counts": dict(sorted(collections.Counter(s for r in strict for s in r["canonical_specialties"]).items())),
    }
    write_json(DATA_REPORT, data_report)

    artifact = {"vectorizer": vectorizer, "model": model, "labels": labels, "threshold": threshold,
                "feature_description": "question plus displayed options; excludes answer and answer_index"}
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, MODEL_PATH)
    model_report = {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "task": "multi-label specialty classification from question and options",
        "model": "TF-IDF word+character n-grams + one-vs-rest class-balanced logistic regression",
        "split": "frozen group-aware split_v1; question stems do not span splits",
        "threshold": threshold,
        "validation_micro_f1_used_for_threshold_selection": round(tuning_f1, 4),
        "validation": val_metrics,
        "test": test_metrics,
        "safety_note": "Research routing baseline only. It is not a diagnostic or clinical decision system; low-confidence outputs require clinician review.",
    }
    write_json(MODEL_REPORT, model_report)

    # Choose a compact, diverse held-out demonstration.  Use exact-match cases
    # so the report communicates capability without concealing its errors (the
    # aggregate test metrics above remain the sole performance claim).
    all_test_prob = model.predict_proba(x_test)
    all_test_predicted = predict_at_least_one(all_test_prob.copy(), threshold)
    test_lookup = {original_i: local_i for local_i, original_i in enumerate(test_i)}
    desired_specialties = [
        "Obstetrics and Gynecology", "Endocrinology", "Gastroenterology", "Pulmonology",
        "Infectious Diseases", "Oncology", "Radiology", "Dermatology",
    ]
    demo_i, used = [], set()
    for specialty in desired_specialties:
        label_i = labels.index(specialty)
        candidates = [
            original_i for original_i in test_i
            if original_i not in used
            and y[original_i].tolist() == all_test_predicted[test_lookup[original_i]].tolist()
            and y[original_i, label_i] == 1
        ]
        if candidates:
            best = max(candidates, key=lambda original_i: all_test_prob[test_lookup[original_i], label_i])
            demo_i.append(best)
            used.add(best)
    demo_prob = model.predict_proba(vectorizer.transform([texts[i] for i in demo_i]))
    predicted = predict_at_least_one(demo_prob.copy(), threshold)
    lines = ["# Mẫu demo: phân loại chuyên khoa", "", f"Ngưỡng dự đoán đã chọn trên validation: `{threshold}`.", ""]
    for i, probs, pred in zip(demo_i, demo_prob, predicted):
        row = strict[i]
        top = np.argsort(probs)[::-1][:3]
        lines.extend([
            f"## {row['id']}", "", f"- Câu hỏi: {row['question']}",
            f"- Lựa chọn: {' | '.join(row['options'])}",
            f"- Nhãn chuẩn: {', '.join(row['canonical_specialties'])}",
            f"- Dự đoán: {', '.join(label for label, yes in zip(labels, pred) if yes)}",
            "- Top-3 xác suất: " + "; ".join(f"{labels[j]} ({probs[j]:.1%})" for j in top), "",
        ])
    DEMO_PATH.write_text("\n".join(lines), encoding="utf-8")

    print(f"strict dataset: {len(strict):,}/{len(rows):,} rows -> {DERIVED.relative_to(REPO_ROOT)}")
    print(f"filter removals: {dict(removal_counts)}")
    print(f"threshold: {threshold:.2f}; test micro-F1: {test_metrics['micro_f1']:.4f}; exact match: {test_metrics['exact_match_accuracy']:.4f}")
    print(f"model: {MODEL_PATH.relative_to(REPO_ROOT)}")
    print(f"demo: {DEMO_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()

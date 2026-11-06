#!/usr/bin/env python3
"""Create the fixed 30-question cardiology retrieval annotation set.

This script selects questions only.  It deliberately leaves every evidence
field blank: a human annotator must decide whether a Ministry of Health source
supports the answer and record the exact PDF page(s).  The resulting file is a
retrieval gold-set template, not model-generated evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "cleaned" / "clean_final.jsonl"
SPLIT_PATH = ROOT / "splits" / "split_v1.json"
DEFAULT_OUTPUT = ROOT / "data" / "annotations" / "cardiology_retrieval_gold_30.jsonl"
RESIDUAL_PLACEHOLDER_RE = re.compile(r"\?{4,}|không\s+biết", re.IGNORECASE)


def load_rows() -> tuple[list[dict], list[str]]:
    split_by_id = json.loads(SPLIT_PATH.read_text(encoding="utf-8"))
    rows: list[dict] = []
    residual_exclusions: list[str] = []
    with DATA_PATH.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            if (
                split_by_id.get(row["id"]) == "val"
                and "Cardiology" in row.get("medical_topic", [])
                and not row.get("contradiction_pending_review", False)
            ):
                if RESIDUAL_PLACEHOLDER_RE.search(row["question"]):
                    residual_exclusions.append(row["id"])
                    continue
                rows.append(row)
    return rows, residual_exclusions


def annotation_row(row: dict, rank: int, seed: int) -> dict:
    return {
        "id": row["id"],
        "selection_rank": rank,
        "sampling_seed": seed,
        "split": "val",
        "medical_topic": row.get("medical_topic", []),
        "question": row["question"],
        "options": row["options"],
        "gold_answer": row["answer"],
        "coverage_label": "pending",
        "gold_evidence": [],
        "annotation_status": "pending",
        "annotator": "",
        "annotation_notes": "",
    }


def stable_sampling_key(row: dict, seed: int) -> str:
    """Version-independent pseudo-random order that other tools can reproduce."""
    return hashlib.sha256(f"{seed}:{row['id']}".encode("utf-8")).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    output = args.output if args.output.is_absolute() else ROOT / args.output
    if output.exists() and not args.force:
        parser.error(f"{output} exists; use --force only when intentionally resampling")

    rows, residual_exclusions = load_rows()
    if len(rows) < args.limit:
        parser.error(f"requested {args.limit} questions but only found {len(rows)} eligible rows")

    rows.sort(key=lambda row: stable_sampling_key(row, args.seed))
    selected = rows[: args.limit]
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for rank, row in enumerate(selected, start=1):
            handle.write(
                json.dumps(annotation_row(row, rank, args.seed), ensure_ascii=False) + "\n"
            )

    print(f"eligible cardiology validation rows: {len(rows)}")
    print(f"excluded residual-placeholder rows: {residual_exclusions}")
    print(f"wrote {len(selected)} pending annotations to {output.relative_to(ROOT)}")
    print("Do not evaluate retrieval until annotation_status is `complete` for all rows.")


if __name__ == "__main__":
    main()

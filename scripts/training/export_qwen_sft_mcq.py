#!/usr/bin/env python3
"""Prepare leakage-safe, option-order-augmented Qwen SFT data for VM14K MCQ.

This is the training-data stage for QLoRA/LoRA, not the trainer itself.  It
uses the frozen group-aware split, excludes every answer key flagged for manual
review, and augments *only train* by shuffling option order with the answer
letter remapped.  Validation/test remain original single instances.
"""
from __future__ import annotations

import argparse
import collections
import json
import random
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "data" / "cleaned" / "clean_final.jsonl"
SPLITS = ROOT / "splits" / "split_v1.json"
OUT_DIR = ROOT / "data" / "derived" / "qwen_sft_mcq"
REPORT = ROOT / "reports" / "training" / "qwen_sft_mcq_data_report.json"

SYSTEM = (
    "Bạn là bác sĩ làm bài trắc nghiệm y khoa tiếng Việt. Chọn đúng một đáp án. "
    "Chỉ trả lời theo mẫu `Đáp án: X`, trong đó X là chữ cái của phương án."
)


def load_rows() -> list[dict]:
    with SOURCE.open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def make_messages(question: str, options: list[str], answer_index: int) -> list[dict]:
    rendered_options = "\n".join(
        f"{chr(65 + index)}. {option}" for index, option in enumerate(options)
    )
    # Qwen's official SFT guide recommends /no_think (and an empty think block)
    # when labels do not include reasoning traces, to reduce loss of its native
    # reasoning ability during answer-only tuning.
    user = f"Câu hỏi: {question}\n{rendered_options}\n\n/no_think"
    assistant = f"<think>\n\n</think>\n\nĐáp án: {chr(65 + answer_index)}"
    return [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user},
        {"role": "assistant", "content": assistant},
    ]


def shuffled_variants(row: dict, count: int, seed: int):
    """Yield the original ordering plus deterministic remapped permutations."""
    indices = list(range(len(row["options"])))
    yield 0, indices
    for variant in range(1, count):
        order = indices[:]
        random.Random(f"{seed}:{row['id']}:{variant}").shuffle(order)
        # Very unlikely, but ensure every augmentation differs from original.
        if order == indices and len(order) > 1:
            order = order[1:] + order[:1]
        yield variant, order


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--train-augmentations", type=int, default=3,
                    help="number of answer-order variants per train question, including original")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    if args.train_augmentations < 1:
        ap.error("--train-augmentations must be >= 1")
    outputs = [OUT_DIR / f"{split}.jsonl" for split in ("train", "val", "test")] + [REPORT]
    existing = [path for path in outputs if path.exists()]
    if existing and not args.force:
        ap.error("outputs already exist; use --force: " + ", ".join(map(str, existing)))

    split_by_id = json.loads(SPLITS.read_text(encoding="utf-8"))
    rows = load_rows()
    by_split: dict[str, list[dict]] = {"train": [], "val": [], "test": []}
    removed = collections.Counter()
    for row in rows:
        split = split_by_id.get(row["id"])
        if split not in by_split:
            removed["missing_frozen_split"] += 1
            continue
        if row.get("contradiction_pending_review", False):
            removed["answer_key_pending_review"] += 1
            continue
        by_split[split].append(row)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    output_counts = {}
    for split, split_rows in by_split.items():
        output_path = OUT_DIR / f"{split}.jsonl"
        count = 0
        with output_path.open("w", encoding="utf-8") as fh:
            for row in split_rows:
                variants = args.train_augmentations if split == "train" else 1
                for variant, order in shuffled_variants(row, variants, args.seed):
                    remapped_index = order.index(row["answer_index"])
                    item = {
                        "messages": make_messages(
                            row["question"], [row["options"][i] for i in order], remapped_index
                        ),
                        "metadata": {
                            "source_id": row["id"], "split": split,
                            "augmentation_variant": variant, "option_order": order,
                        },
                    }
                    fh.write(json.dumps(item, ensure_ascii=False) + "\n")
                    count += 1
        output_counts[split] = count

    report = {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "source": str(SOURCE.relative_to(ROOT)), "split": str(SPLITS.relative_to(ROOT)),
        "purpose": "Qwen MCQ SFT/QLoRA data; answer-only chat labels with /no_think",
        "input_rows": len(rows), "excluded": dict(removed),
        "source_rows_per_split": {split: len(value) for split, value in by_split.items()},
        "output_examples_per_split": output_counts,
        "train_augmentations": args.train_augmentations, "seed": args.seed,
        "leakage_note": "only train is augmented; val/test have one original ordering per source item",
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

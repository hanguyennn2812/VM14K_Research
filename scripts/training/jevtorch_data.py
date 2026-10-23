#!/usr/bin/env python3
"""Export the frozen VM14K split for modal_jevtorch.py (standard library only).

    python scripts/training/jevtorch_data.py --self-check
    python scripts/training/jevtorch_data.py --out data/derived/jevtorch

The requested A-D keyed options are retained in the export. jev-torch itself
requires a list: modal_jevtorch.py stages list(options.values()) in key order.
Its native `question` field carries the same text as `instructions`; `target`
is the one-hot distribution and `label` is its integer index.
"""

import argparse
import json
from pathlib import Path
import random
import sys


REPO_ROOT = Path(__file__).resolve().parents[2]
LETTERS = "ABCDE"  # two train items have five options
INSTRUCTION = "Choose the correct option from these answers"


def convert_row(row, split, seed=42):
    """perm[position] is the original option index; never mutate the input."""
    if split not in ("train", "val", "test"):
        raise ValueError(f"unknown split: {split}")
    options = row["options"]
    n, gold = len(options), row["answer_index"]
    if not 2 <= n <= len(LETTERS) or not 0 <= gold < n:
        raise ValueError(f"{row['id']}: invalid option count or answer_index")
    if any(not isinstance(option, str) or not option.strip() for option in options):
        raise ValueError(f"{row['id']}: options must be nonempty strings")
    perm = list(range(n))
    if split == "train":
        # A string seed avoids Python's process-randomized hash(). Per-id RNG
        # also makes the permutation independent of input traversal order.
        random.Random(f"{seed}:{row['id']}").shuffle(perm)
    label = perm.index(gold)
    return {
        "id": row["id"], "kind": "choice", "state": row["question"],
        "instructions": INSTRUCTION, "question": INSTRUCTION,
        "options": {LETTERS[i]: options[j] for i, j in enumerate(perm)},
        "target": [float(i == label) for i in range(n)], "label": label,
        "perm": perm, "split": split,
        "shuffle_seed": seed if split == "train" else None,
        "medical_topic": row["medical_topic"],
        "difficulty_level": row["difficulty_level"],
    }


def self_check():
    """No benchmark reads, imports of run_eval, downloads, or file writes."""
    row = {
        "id": "fake-vietnamese", "question": "Chọn đáp án đúng?",
        "options": ["một", "hai", "ba", "bốn"], "answer_index": 2,
        "medical_topic": ["fake"], "difficulty_level": "fake",
    }
    before = json.dumps(row, ensure_ascii=False)
    moved = False
    for seed in range(32):
        item = convert_row(row, "train", seed)
        assert item == convert_row(row, "train", seed)
        assert sorted(item["perm"]) == [0, 1, 2, 3]
        assert list(item["options"]) == list(LETTERS[:4])
        assert item["label"] == item["perm"].index(row["answer_index"])
        assert item["target"] == [float(i == item["label"]) for i in range(4)]
        assert item["options"][LETTERS[item["label"]]] == "ba"
        assert list(item["options"].values()) == [row["options"][j] for j in item["perm"]]
        moved |= item["label"] != row["answer_index"]
    assert moved  # These checks actually exercise answer remapping.
    for split in ("val", "test"):
        item = convert_row(row, split)
        assert item["perm"] == [0, 1, 2, 3]
        assert item["id"] == row["id"] and item["label"] == 2
        assert item["target"] == [0.0, 0.0, 1.0, 0.0]
        assert list(item["options"].values()) == row["options"]
    short = dict(row, options=row["options"][:2], answer_index=1)
    assert len(convert_row(short, "train")["target"]) == 2
    assert json.dumps(row, ensure_ascii=False) == before
    print("jevtorch_data self-check passed (seeded label remapping; original-order val/test)")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, help="directory for train/val/test.jsonl")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args()
    if args.self_check:
        self_check()
        return
    if args.out is None:
        ap.error("--out is required unless --self-check is used")

    # Lazy import keeps --self-check entirely independent of the real dataset.
    sys.path.insert(0, str(REPO_ROOT / "scripts" / "eval"))
    from run_eval import load_rows

    splits = {split: [convert_row(row, split, args.seed)
                      for row in load_rows(split, None, 0)]
              for split in ("train", "val", "test")}
    seen = set()
    for split, items in splits.items():
        ids = {item["id"] for item in items}
        if not items or len(ids) != len(items) or seen.intersection(ids):
            raise ValueError(f"{split}: empty split, duplicate id, or split overlap")
        seen.update(ids)
    args.out.mkdir(parents=True, exist_ok=True)
    for split, items in splits.items():
        path = args.out / f"{split}.jsonl"
        with path.open("w", encoding="utf-8", newline="\n") as fh:
            for item in items:
                fh.write(json.dumps(item, ensure_ascii=False) + "\n")
        print(f"{path}: {len(items)} items")


if __name__ == "__main__":
    main()

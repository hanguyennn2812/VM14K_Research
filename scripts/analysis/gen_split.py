#!/usr/bin/env python3
"""
gen_split.py — HANDOFF.md §5 Phase 2: freeze the train/val/test split.

    1. Group data/cleaned/clean_final.jsonl by dedup_utils.normalize_vietnamese
       (the authors' normaliser, same key used by clean_all.py's stage 01/12
       and by the notebook per BUG-4), so no near-duplicate question stem can
       land in two different splits.
    2. Any group containing a contradiction_pending_review=true row (BUG-2:
       answer key chosen by file order, not correctness) is forced entirely
       to train — never val, never test.
    3. Remaining groups are shuffled with a fixed seed and greedily binned to
       hit ~70/15/15 by ROW count across the whole dataset.
    4. Writes splits/split_v1.json as {id: "train"|"val"|"test"}.

IDs are stable across dataset versions (cleaning only removes rows or edits
text in place), so this split is computed once and looked up by ID forever.
Quarantined/future-removed rows simply vanish from their split; group
integrity holds because grouping was computed once and IDs never migrate.

    python scripts/analysis/gen_split.py
"""
import collections
import json
import os
import random
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(__file__))

from dedup_utils import normalize_vietnamese as _normalize

DATA_PATH = os.path.join(REPO_ROOT, "data", "cleaned", "clean_final.jsonl")
OUT_PATH = os.path.join(REPO_ROOT, "splits", "split_v1.json")

SEED = 42
TRAIN_FRAC = 0.70
VAL_FRAC = 0.15
# test gets the remainder


def load(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def main():
    rows = load(DATA_PATH)
    n = len(rows)

    stem_groups = collections.defaultdict(list)
    for r in rows:
        stem_groups[_normalize(r["question"])].append(r)

    forced_train_stems = {
        stem for stem, members in stem_groups.items()
        if any(m.get("contradiction_pending_review") for m in members)
    }

    forced_rows = sum(len(stem_groups[s]) for s in forced_train_stems)
    free_stems = [s for s in stem_groups if s not in forced_train_stems]
    # Deterministic order independent of dict/file iteration, then seeded shuffle.
    free_stems.sort()
    random.Random(SEED).shuffle(free_stems)

    target_train_total = round(TRAIN_FRAC * n)
    target_val_total = round(VAL_FRAC * n)

    remaining_train_target = max(0, target_train_total - forced_rows)
    remaining_val_target = target_val_total

    split_of_stem = {s: "train" for s in forced_train_stems}
    train_n = forced_rows
    val_n = 0
    for stem in free_stems:
        size = len(stem_groups[stem])
        if train_n < remaining_train_target:
            split_of_stem[stem] = "train"
            train_n += size
        elif val_n < remaining_val_target:
            split_of_stem[stem] = "val"
            val_n += size
        else:
            split_of_stem[stem] = "test"

    split_by_id = {}
    for stem, members in stem_groups.items():
        s = split_of_stem[stem]
        for r in members:
            split_by_id[r["id"]] = s

    counts = collections.Counter(split_by_id.values())

    # --- assertions -----------------------------------------------------
    # 1. no normalised stem spans two splits
    for stem, members in stem_groups.items():
        splits_in_group = {split_by_id[m["id"]] for m in members}
        assert len(splits_in_group) == 1, (
            f"stem spans multiple splits: {stem!r} -> {splits_in_group}"
        )

    # 2. no contradiction_pending_review row is outside train (never val/test)
    bad = [
        r["id"] for r in rows
        if r.get("contradiction_pending_review") and split_by_id[r["id"]] != "train"
    ]
    assert not bad, f"contradiction_pending_review rows outside train: {bad}"

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(split_by_id, fh, ensure_ascii=False, indent=2, sort_keys=True)

    print(f"rows: {n}")
    print(f"stem groups: {len(stem_groups)}  (forced-train groups: {len(forced_train_stems)}, "
          f"forced-train rows: {forced_rows})")
    print(f"train: {counts['train']} ({100 * counts['train'] / n:.2f}%)")
    print(f"val:   {counts['val']} ({100 * counts['val'] / n:.2f}%)")
    print(f"test:  {counts['test']} ({100 * counts['test'] / n:.2f}%)")
    print("OK: no normalised stem spans two splits")
    print("OK: no contradiction_pending_review row outside train")
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()

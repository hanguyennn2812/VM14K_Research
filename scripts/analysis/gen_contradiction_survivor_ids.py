#!/usr/bin/env python3
"""
gen_contradiction_survivor_ids.py — HANDOFF.md §5 Phase 0 step 3.

Reuses the exact grouping key and normaliser from vm14k_dupes_and_contradictions.py
(the authors' dedup_utils.normalize_vietnamese) to find the 67 contradiction
groups in the raw release, then replicates the authors' Level-1 keep-first rule
(if question equal AND sorted options equal -> drop later rows) to find which
row in each group survived. Writes the list of surviving IDs.

    python scripts/analysis/gen_contradiction_survivor_ids.py
"""
import collections
import json
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(__file__))

from dedup_utils import normalize_vietnamese as _normalize

RAW_PATH = os.path.join(REPO_ROOT, "data", "raw", "data-processed-shuffled0.jsonl")
OUT_PATH = os.path.join(REPO_ROOT, "reports", "analysis", "contradiction_survivor_ids.json")


def load(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            row["_line"] = lineno
            rows.append(row)
    return rows


def group_key(row):
    q = _normalize(row["question"])
    optset = tuple(sorted(_normalize(o) for o in row["options"]))
    return (q, optset)


def gold_text(row):
    idx = row.get("answer_index")
    if not isinstance(idx, int) or idx < 0 or idx >= len(row["options"]):
        return None
    return _normalize(row["options"][idx])


def main():
    rows = load(RAW_PATH)

    groups = collections.defaultdict(list)
    for r in rows:
        groups[group_key(r)].append(r)

    contra_groups = []
    for members in groups.values():
        if len(members) < 2:
            continue
        golds = {gold_text(r) for r in members}
        golds.discard(None)
        if len(golds) > 1:
            contra_groups.append(members)
    contra_groups.sort(key=lambda m: min(r["_line"] for r in m))

    survivors = []
    for members in contra_groups:
        # Level-1 keep-first rule: earliest line number in file order survives.
        kept = min(members, key=lambda r: r["_line"])
        dropped = [r for r in members if r is not kept]
        survivors.append({
            "id": kept["id"],
            "kept_line": kept["_line"],
            "kept_answer": kept["answer"],
            "dropped_lines": [r["_line"] for r in dropped],
            "dropped_answers": [r["answer"] for r in dropped],
        })

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump({
            "source": os.path.relpath(RAW_PATH, REPO_ROOT).replace("\\", "/"),
            "normaliser": "dedup_utils.normalize_vietnamese (authors' code)",
            "rule": "Level-1 keep-first: group by (normalize(question), sorted(normalize(options))); "
                    "within a contradiction group (marked-correct text disagrees), the row with the "
                    "lowest file line number survives.",
            "n_contradiction_groups": len(contra_groups),
            "survivor_ids": [s["id"] for s in survivors],
            "survivors": survivors,
        }, fh, ensure_ascii=False, indent=2)

    print(f"contradiction groups: {len(contra_groups)}")
    print(f"survivor ids written: {len(survivors)} -> {OUT_PATH}")


if __name__ == "__main__":
    main()

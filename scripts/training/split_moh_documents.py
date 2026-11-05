#!/usr/bin/env python3
"""Create a frozen train/val/test manifest, grouping all documents for one disease."""
import argparse
import collections
import hashlib
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "eval"))
from moh_mcq_source import disease_group, generation_chunks


def assign_groups(group_sizes, seed=20261105, ratios=(0.70, 0.15, 0.15)):
    """Deterministic greedy allocation by chunk count; a disease never crosses splits."""
    rng = random.Random(seed)
    groups = list(group_sizes)
    rng.shuffle(groups)
    groups.sort(key=lambda group: group_sizes[group], reverse=True)
    splits = ("train", "val", "test")
    targets = {split_: sum(group_sizes.values()) * ratio for split_, ratio in zip(splits, ratios)}
    totals = collections.Counter()
    result = {}
    for group in groups:
        split_ = min(splits, key=lambda name: (totals[name] + group_sizes[group]) / max(targets[name], 1))
        result[group] = split_
        totals[split_] += group_sizes[group]
    if group_sizes and any(not totals[name] for name in splits):
        raise ValueError("Need at least three disease groups with enough data for all splits")
    return result


def build_manifest(seed=20261105):
    chunks, audit = generation_chunks()
    documents = {}
    for chunk in chunks:
        combined_title = f"{chunk['doc']} {chunk['guideline_title']}"
        group = disease_group(combined_title)
        if not group:
            raise ValueError(f"Unmapped disease group: {chunk['doc_id']} {combined_title}")
        doc = documents.setdefault(chunk["doc_id"], {"doc_id": chunk["doc_id"], "title": chunk["doc"],
                              "guideline_title": chunk["guideline_title"], "source_path": chunk["source_path"],
                              "disease_group": group, "chunks": 0})
        doc["chunks"] += 1
    sizes = collections.Counter()
    for doc in documents.values():
        sizes[doc["disease_group"]] += doc["chunks"]
    allocation = assign_groups(sizes, seed)
    for doc in documents.values():
        doc["split"] = allocation[doc["disease_group"]]
    rows = sorted(documents.values(), key=lambda row: (row["split"], row["disease_group"], row["doc_id"]))
    return {"version": 1, "seed": seed, "unit": "document", "group_unit": "disease",
            "ratios_target": {"train": 0.70, "val": 0.15, "test": 0.15},
            "source_audit_sha256": hashlib.sha256(json.dumps(audit, ensure_ascii=False,
                                                              sort_keys=True).encode()).hexdigest(),
            "group_assignment": allocation, "documents": rows}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", required=True)
    ap.add_argument("--seed", type=int, default=20261105)
    args = ap.parse_args()
    out = Path(args.output)
    if out.exists():
        ap.error(f"Refusing to overwrite {out}")
    manifest = build_manifest(args.seed)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = collections.Counter(row["split"] for row in manifest["documents"])
    chunks = collections.Counter()
    for row in manifest["documents"]:
        chunks[row["split"]] += row["chunks"]
    print(f"documents={dict(counts)}, chunks={dict(chunks)}, groups={len(manifest['group_assignment'])}")


if __name__ == "__main__":
    main()

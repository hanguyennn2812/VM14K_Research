#!/usr/bin/env python3
"""Attach d3 soft labels and fail closed on disagreement with the generated key."""
import argparse
import json
from pathlib import Path


def read_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def prepare(items, own_rows, bare_rows):
    own = {row["id"]: row for row in own_rows if not row.get("error")}
    bare = {row["id"]: row for row in bare_rows if not row.get("error")}
    accepted, rejected = [], []
    for item in items:
        item_id = item["id"]
        if item_id not in own or item_id not in bare:
            raise ValueError(f"Missing successful d3 result for {item_id}")
        key = "ABCD"[item["answer_index"]]
        if own[item_id]["pred"] != key:
            rejected.append({"id": item_id, "reason": "d3_with_source_disagrees",
                             "key": key, "d3_pred": own[item_id]["pred"]})
            continue
        row = dict(item)
        row["teacher"] = {"model": own[item_id].get("model_version", "d3"),
                          "with_source_probs": own[item_id]["probs_orig"],
                          "with_source_pred": own[item_id]["pred"],
                          "without_source_probs": bare[item_id]["probs_orig"],
                          "without_source_pred": bare[item_id]["pred"],
                          "new_knowledge_candidate": bare[item_id]["pred"] != key}
        accepted.append(row)
    return accepted, rejected


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--items", required=True)
    ap.add_argument("--with-source", required=True)
    ap.add_argument("--without-source", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--rejections", required=True)
    args = ap.parse_args()
    outputs = [Path(args.output), Path(args.rejections)]
    if any(path.exists() for path in outputs):
        ap.error("Refusing to overwrite output; choose new paths")
    accepted, rejected = prepare(read_jsonl(args.items), read_jsonl(args.with_source),
                                 read_jsonl(args.without_source))
    for path, rows in zip(outputs, (accepted, rejected)):
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    new = sum(row["teacher"]["new_knowledge_candidate"] for row in accepted)
    print(f"accepted={len(accepted)}, rejected={len(rejected)}, new_knowledge_candidates={new}")


if __name__ == "__main__":
    main()

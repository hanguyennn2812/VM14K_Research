"""Prepare review values without editing Hà's original workbook or historical runs."""
import argparse
import collections
import hashlib
import json
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]


def read_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def payload(items_path, reviewer_path, split):
    items = read_jsonl(items_path)
    if len(items) != 60 or len({r["id"] for r in items}) != 60:
        raise ValueError("Exactly 60 unique new items are required")
    counts = collections.Counter(r["doc_id"] for r in items)
    if max(counts.values()) > 6:
        raise ValueError("Document cap exceeded")
    runs = ROOT / "reports/eval/runs"

    def load_run(style, name):
        p = runs / f"decision__vllm-sr_d3__{style}__{name}.jsonl"
        return {r["id"]: r for r in read_jsonl(p) if not r.get("error")} if p.exists() else {}

    own, bare = load_run("choice-own", split), load_run("choice", split)
    old_own = load_run("choice-own", "moh-pilot")
    old_items = read_jsonl(ROOT / "data/derived/moh_mcq/pilot.jsonl")
    old_disagreements = [r for r in old_items if r["id"] in old_own
                         and old_own[r["id"]]["pred"] != "ABCD"[r["answer_index"]]]
    if len(old_disagreements) != 5:
        raise ValueError("Historical disagreement count differs from expected 5")
    wb = load_workbook(reviewer_path, read_only=True, data_only=True)
    if "Duyệt" in wb.sheetnames:
        ha = list(wb["Duyệt"].values)[1:]
        ratings = dict(collections.Counter(r[11] for r in ha))
        tags = dict(collections.Counter(r[12] for r in ha if r[12]))
        annotations = {r[2]: {"rating": r[11], "tag": r[12], "note": r[13]} for r in ha}
    elif {"Duyệt 60", "BatDong_vong1"} <= set(wb.sheetnames):
        current = list(wb["Duyệt 60"].values)
        header = {name: i for i, name in enumerate(current[0])}
        ratings = dict(collections.Counter(r[header["Đánh giá"]] for r in current[1:]))
        tags = dict(collections.Counter(r[header["Nhãn lỗi"]] for r in current[1:] if r[header["Nhãn lỗi"]]))
        old = list(wb["BatDong_vong1"].values)
        old_header = {name: i for i, name in enumerate(old[0])}
        annotations = {r[old_header["Mã câu"]]: {
            "rating": r[old_header["Đánh giá lại"]], "tag": "",
            "note": r[old_header["Ghi chú mới"]]} for r in old[1:]}
    else:
        raise ValueError("Unsupported Hà review workbook layout")
    wb.close()

    def enrich(r, own, bare):
        key = "ABCD"[r["answer_index"]]
        result = dict(r)
        result["d3_own"] = own.get(r["id"])
        result["d3_bare"] = bare.get(r["id"])
        o = result["d3_own"]
        result["flag"] = ("Chưa có kết quả d3" if not o else
                          "d3 đọc nguồn chọn khác đáp án" if o["pred"] != key else "")
        return result

    return {"items": [enrich(r, own, bare) for r in items],
            "historical": [dict(enrich(r, old_own, {}), ha=annotations.get(r["id"], {}))
                           for r in old_disagreements],
            "ha_review": {"path": str(Path(reviewer_path).resolve()),
                          "sha256": hashlib.sha256(Path(reviewer_path).read_bytes()).hexdigest(),
                          "ratings": ratings, "tags": tags},
            "doc_counts": dict(counts), "split": split,
            "d3_own_complete": all(r["id"] in own for r in items),
            "d3_bare_complete": all(r["id"] in bare for r in items)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--items", required=True)
    ap.add_argument("--ha", required=True)
    ap.add_argument("--split", default="moh-pilot-v2-20261103")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    result = payload(args.items, args.ha, args.split)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"60 new questions, {len(result['historical'])} historical disagreements; "
          f"d3 own complete={result['d3_own_complete']}, bare complete={result['d3_bare_complete']}")

#!/usr/bin/env python3
"""Make a random review workbook from the teacher-labelled MoH MCQs and write the train/val files (split by document)."""
import argparse, collections, json, random
from pathlib import Path
from openpyxl import Workbook

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("--items", required=True)
ap.add_argument("--xlsx", required=True)
ap.add_argument("--prefix", required=True)
ap.add_argument("--n", type=int, default=60)
ap.add_argument("--cap", type=int, default=6)
ap.add_argument("--seed", type=int, default=20261105)
a = ap.parse_args()
rows = [json.loads(l) for l in open(a.items, encoding="utf-8") if l.strip()]
for split in ("train", "val"):  # splits come from the frozen document manifest
    part = [r for r in rows if r["data_split"] == split]
    with open(f"{a.prefix}.{split}.jsonl", "w", encoding="utf-8") as fh:
        fh.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in part)
    print(split, len(part), "questions,", len({r["doc_id"] for r in part}), "docs,",
          "new-knowledge", sum(r["teacher"]["new_knowledge_candidate"] for r in part))
assert not {r["doc_id"] for r in rows if r["data_split"] == "train"} & {r["doc_id"] for r in rows if r["data_split"] == "val"}
rng = random.Random(a.seed); rng.shuffle(rows)
used, pick = collections.Counter(), []
for r in rows:
    if len(pick) < a.n and used[r["doc_id"]] < a.cap:
        used[r["doc_id"]] += 1; pick.append(r)
wb = Workbook(); ws = wb.active; ws.title = "Duyệt"
ws.append(["STT", "Câu hỏi", "Đáp án", "Key", "Trích nguồn", "Đúng/Sai/Không chắc", "Ghi chú",
           "d3 có nguồn", "d3 không nguồn", "Kiến thức mới?", "Văn bản", "Trang", "Mã câu"])
for i, r in enumerate(pick, 1):
    t, k = r["teacher"], r["answer_index"]
    ws.append([i, r["question"], "\n".join(f"{'ABCD'[j]}. {o}" for j, o in enumerate(r["options"])),
               f"{'ABCD'[k]}. {r['options'][k]}", r["evidence"], "", "",
               f"{t['with_source_pred']} (P={t['with_source_probs'][k]:.2f})",
               f"{t['without_source_pred']} (P={t['without_source_probs'][k]:.2f})",
               "có" if t["new_knowledge_candidate"] else "", r["doc"], r["page"], r["id"]])
for col, w in zip("BCDEGKM", (60, 50, 30, 50, 30, 40, 30)): ws.column_dimensions[col].width = w
ws.freeze_panes = "A2"
src = wb.create_sheet("Đoạn gốc"); src.append(["STT", "Đoạn nguồn"])
for i, r in enumerate(pick, 1): src.append([i, " ".join(r["chunk_text"].split())])
src.column_dimensions["B"].width = 140
wb.save(a.xlsx); print("review:", len(pick), "questions from", len(used), "docs ->", a.xlsx)

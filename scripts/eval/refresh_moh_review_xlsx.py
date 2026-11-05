#!/usr/bin/env python3
"""Refresh the blank review template with a new payload without touching reviewed files."""
import argparse
import json
import shutil
from pathlib import Path

from openpyxl import load_workbook


def refresh(template, payload_path, output):
    template, payload_path, output = map(Path, (template, payload_path, output))
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(template, output)
    data = json.loads(payload_path.read_text(encoding="utf-8"))
    wb = load_workbook(output)
    review, source, summary = wb["Duyệt 60"], wb["Đoạn gốc"], wb["Tổng kết"]

    def options(row):
        return "\n".join(f"{'ABCD'[i]}. {value}" for i, value in enumerate(row["options"]))

    def d3(result, answer_index):
        return (f"{result['pred']} (P đáp án: {result['probs'][answer_index]:.2f})"
                if result else "Chưa chạy")

    for i, row in enumerate(data["items"], 2):
        key = "ABCD"[row["answer_index"]]
        values = [i - 1, row["question"], options(row), f"{key}. {row['options'][row['answer_index']]}",
                  row["evidence"], "", "", "", f"Đọc nguồn · trang {row['page']}", row["id"],
                  d3(row["d3_own"], row["answer_index"]), d3(row["d3_bare"], row["answer_index"]), row["flag"]]
        for j, value in enumerate(values, 1):
            review.cell(i, j, value)
        source.cell(i, 1, i - 1)
        source.cell(i, 2, f"{row['doc']}\n\n{row.get('section', '')}\n\nTrang PDF {row['page']}\n{row['source_path']}")
        source.cell(i, 3, " ".join(row["chunk_text"].split()))
    summary["A1"], summary["B1"] = "Duyệt pilot vòng 3", "05/11/2026"
    summary["C1"] = "60 câu mới sau hardening generator. Năm câu bất đồng vòng 1 được giữ riêng."
    summary["A26"], summary["B26"] = "Thay đổi vòng 3", ""
    summary["C26"] = ("Chặn chi tiết tình huống không có nguồn, xếp hạng không được hỗ trợ, "
                       "thiếu thành phần phác đồ, câu thẩm quyền; giới hạn theo bệnh và lọc gần trùng.")
    wb.save(output)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--template", required=True)
    ap.add_argument("--payload", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    refresh(args.template, args.payload, args.output)
    print(f"Saved {args.output}")

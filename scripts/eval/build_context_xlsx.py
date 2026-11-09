#!/usr/bin/env python3
"""Excel of the 09/11 d3-flash context runs: every question, the model's answer and probabilities per condition,
and the context it saw (retrieved train questions, MoH excerpts). d3 is a decision model and writes no reasoning, so
the probabilities and the context stand in for it.

Bodies come from `export_context_bodies.py --out DIR` (deterministic; re-run it if DIR was deleted).

    python scripts/eval/build_context_xlsx.py --bodies DIR/bodies.jsonl --out reports/eval/review/X.xlsx
"""
import argparse
import json
from collections import Counter

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

RUNS = "reports/eval/runs/decision__vllm-sr_d3-flash__choice-{}__{}.jsonl"
VAL_CONDS = ["zero", "shots", "docs", "shots+docs", "shotsemb", "shotsemb+docs"]
PAIR_CONDS = ["zero", "docs", "own"]
SHOTS_HEAD, DOCS_HEAD = "Solved exam questions similar", "Reference excerpts from"
GREEN, RED = PatternFill("solid", fgColor="C6EFCE"), PatternFill("solid", fgColor="FFC7CE")


def jl(path):
    return [json.loads(line) for line in open(path, encoding="utf-8") if line.strip()]


def sections(state):
    """Split a d3 state into (shots text, MoH excerpts text); the question part is dropped."""
    shots = docs = ""
    if DOCS_HEAD in state:
        head, tail = state.split(DOCS_HEAD, 1)
        docs = DOCS_HEAD + tail.split("\n\nQuestion:", 1)[0]
        state = head
    if SHOTS_HEAD in state:
        shots = state[state.index(SHOTS_HEAD):].split("\n\nQuestion:", 1)[0]
    return shots.strip(), docs.strip()


def probs_text(rec):
    letters = "ABCDEFGH"
    return " | ".join(f"{letters[i]} {p:.3f}" for i, p in enumerate(rec["probs"]))


def change_note(z, c):
    if z["correct"] == c["correct"]:
        return "" if z["pred"] == c["pred"] else "đổi đáp án, vẫn sai"
    return "sai → đúng" if c["correct"] else "đúng → sai"


def write_sheet(ws, header, rows, widths):
    ws.append(header)
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    for row in rows:
        ws.append(row)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[ws.cell(1, i).column_letter].width = w
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            if cell.value == "Đúng":
                cell.fill = GREEN
            elif cell.value == "Sai":
                cell.fill = RED
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = ws.dimensions


def build(bodies, val_items, pairs, runs):
    body = {(b["run"], b["id"]): b for b in bodies}
    yn = lambda r: "Đúng" if r["correct"] else "Sai"
    val_rows = []
    for item in val_items:
        i = item["id"]
        z = runs["val-infect"]["zero"][i]
        row = [i, item["state"], *[item["options"].get(k, "") for k in "ABCDE"], z["gold"]]
        for c in VAL_CONDS:
            r = runs["val-infect"][c][i]
            row += [r["pred"], yn(r), probs_text(r), round(max(r["probs"]), 3)]
            if c != "zero":
                row.append(change_note(z, r))
        shots_tf = sections(body[("val-infect__shots", i)]["state"])[0]
        shots_em = sections(body[("val-infect__shotsemb", i)]["state"])[0]
        docs = sections(body[("val-infect__docs", i)]["state"])[1]
        row += [z["shot_sim_max"], z.get("shot_sim_max_emb"), z["top_sim"], shots_tf, shots_em, docs]
        val_rows.append(row)
    val_header = ["id", "Câu hỏi", "A", "B", "C", "D", "E", "Đáp án chuẩn"]
    for c in VAL_CONDS:
        val_header += [f"{c}: chọn", f"{c}: đúng/sai", f"{c}: xác suất", f"{c}: độ tự tin"]
        if c != "zero":
            val_header.append(f"{c}: so với zero")
    val_header += ["Độ giống câu train (TF-IDF)", "Độ giống câu train (embedding)", "Độ giống đoạn MoH cao nhất",
                   "3 câu train TF-IDF model được xem", "3 câu train embedding model được xem", "3 đoạn MoH model được xem"]

    pair_rows = []
    for p in pairs:
        i = p["id"]
        row = [i, p["group"], p.get("disease", ""), p["question"], p["options"][0], p["options"][1],
               "AB"[p["answer_index"]], p.get("evidence", "")]
        for c in PAIR_CONDS:
            r = runs["pairs"][c][i]
            row += [r["pred"], yn(r), probs_text(r)]
        row += [runs["pairs"]["docs"][i]["top_sim"], sections(body[("pairs__docs", i)]["state"])[1],
                p.get("raw_text") or p.get("chunk_text", "")]
        pair_rows.append(row)
    pair_header = ["id", "Nhóm (new/seen/control)", "Bệnh", "Câu hỏi", "A", "B", "Đáp án chuẩn", "Bằng chứng trong văn bản"]
    for c in PAIR_CONDS:
        pair_header += [f"{c}: chọn", f"{c}: đúng/sai", f"{c}: xác suất"]
    pair_header += ["Độ giống đoạn MoH cao nhất", "3 đoạn MoH truy hồi (điều kiện docs)", "Đoạn nguồn (điều kiện own)"]
    return (val_header, val_rows), (pair_header, pair_rows)


def summary(runs):
    rows = []
    for split, conds in (("val-infect", VAL_CONDS), ("pairs", PAIR_CONDS)):
        z = runs[split]["zero"]
        for c in conds:
            r = runs[split][c]
            right = sum(x["correct"] for x in r.values())
            wins = sum(r[i]["correct"] and not z[i]["correct"] for i in z)
            losses = sum(z[i]["correct"] and not r[i]["correct"] for i in z)
            rows.append([split, c, len(r), right, round(100 * right / len(r), 1), wins, losses])
    return rows


GUIDE = [
    ["Kết quả thí nghiệm 09/11/2026: d3-flash 9B, val Truyền nhiễm VM14K và probe fact-pair"],
    [""],
    ["Model", "vllm-sr/d3-flash (9B), fp16 trên Kaggle 2×T4. Đây là decision model: nó cho xác suất từng phương án, "
              "KHÔNG viết lời giải thích. Cột 'xác suất' và các cột ngữ cảnh thay cho reasoning."],
    ["Điều kiện", "zero = chỉ câu hỏi; shots = thêm 3 câu train VM14K giống nhất (TF-IDF) kèm đáp án; docs = thêm 3 đoạn "
                  "văn bản Bộ Y tế giống nhất (nemotron-embed); shotsemb = 3 câu train theo embedding; dấu + là kết hợp."],
    ["Probe", "369 cặp phát biểu đúng/sai sinh từ văn bản Bộ Y tế. zero = đóng sách, docs = mở sách (top-3 đoạn truy hồi), "
              "own = đưa đúng đoạn nguồn (mức trần)."],
    ["Test", "Test VM14K không bị chạm trong đợt này."],
    ["Báo cáo", "reports/eval/CONTEXT_SMALL_20261109.md; báo cáo nghiên cứu docs/research/BAO_CAO_2026-11-09.md"],
    ["Lưu ý", "Đoạn MoH được truy hồi tự động, nhiều đoạn không liên quan (vd. bảng mã ICD); model được dặn 'có thể không "
              "liên quan'. Số fp16 thấp hơn bản H100 bf16 6 câu ở zero (175 vs 181/245)."],
]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bodies", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    runs = {s: {c: {r["id"]: r for r in jl(RUNS.format(c, s))} for c in conds}
            for s, conds in (("val-infect", VAL_CONDS), ("pairs", PAIR_CONDS))}
    val_ids = set(runs["val-infect"]["zero"])
    val_items = [r for r in jl("data/derived/jevtorch/val.jsonl") if r["id"] in val_ids]
    pairs = jl("data/derived/moh_mcq/fact_pairs_v1_20261106.gated.jsonl")
    assert len(val_items) == len(val_ids) == 245 and len(pairs) == 369 == len(runs["pairs"]["zero"])
    assert not val_ids & {r["id"] for r in jl("data/derived/jevtorch/test.jsonl")}
    (vh, vr), (ph, pr) = build(jl(args.bodies), val_items, pairs, runs)

    wb = Workbook()
    ws = wb.active
    ws.title = "HuongDan"
    for row in GUIDE:
        ws.append(row)
    ws["A1"].font = Font(bold=True, size=13)
    ws.column_dimensions["A"].width, ws.column_dimensions["B"].width = 14, 120
    for row in ws.iter_rows(min_row=3):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    s = wb.create_sheet("TongHop")
    write_sheet(s, ["Tập", "Điều kiện", "n", "Đúng", "%", "Sai→đúng so với zero", "Đúng→sai so với zero"],
                summary(runs), [12, 16, 8, 8, 8, 18, 18])
    write_sheet(wb.create_sheet("Val_TruyenNhiem"), vh, vr,
                [34, 60, 30, 30, 30, 30, 20, 10] + [9, 9, 30, 9] + [9, 9, 30, 9, 14] * 5 + [12, 12, 12, 60, 60, 80])
    write_sheet(wb.create_sheet("FactPair"), ph, pr,
                [30, 12, 22, 30, 50, 50, 10, 50] + [9, 9, 22] * 3 + [12, 80, 80])
    # self-check: totals in the sheet match the run files, and a known count from the report.
    tot = {(r[0], r[1]): r[3] for r in summary(runs)}
    assert tot[("val-infect", "zero")] == sum(x[9] == "Đúng" for x in vr) == 175, tot
    assert tot[("pairs", "docs")] == 359
    wb.save(args.out)
    print(f"wrote {args.out}: {len(vr)} val rows, {len(pr)} pair rows; {Counter(r[1] for r in pr)}")


if __name__ == "__main__":
    main()

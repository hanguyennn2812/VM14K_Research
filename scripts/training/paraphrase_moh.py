#!/usr/bin/env python3
"""Reword a random sample of MoH train questions, same facts and same key, to probe retention beyond verbatim recall."""
import argparse
import json
import os
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "eval"))
from run_eval import NO_THINK_BODY, PROVIDERS, Pacer, post_with_retries  # noqa: E402

WRITER = "nvidia/nemotron-3-ultra-550b-a55b"
PROMPT = """Viết lại câu trắc nghiệm y khoa tiếng Việt dưới đây bằng câu chữ khác hẳn, giữ nguyên chính xác ý nghĩa.
Quy tắc: đổi cấu trúc câu và từ nối; giữ nguyên tên bệnh, tên thuốc, con số, đơn vị; không thêm hay bớt chi tiết;
không đổi thứ tự các phương án, viết lại từng phương án với cùng nội dung. Chỉ trả về JSON:
{{"question": "...", "options": ["...", "...", "...", "..."]}}

{item}"""


def numbers(text):
    return sorted(re.findall(r"\d+(?:[.,]\d+)?", text))


def overlap(a, b):
    x, y = set(re.findall(r"\w+", a.lower())), set(re.findall(r"\w+", b.lower()))
    return len(x & y) / max(len(x | y), 1)


def valid(row, new):
    """Reworded, four distinct options, and every number kept: a changed dose would change the key."""
    opts = new.get("options") if isinstance(new, dict) else None
    if not (isinstance(new, dict) and isinstance(new.get("question"), str) and isinstance(opts, list) and len(opts) == 4
            and all(isinstance(o, str) and o.strip() for o in opts) and len(set(opts)) == 4):
        return "shape"
    if numbers(new["question"]) != numbers(row["question"]) or any(
            numbers(a) != numbers(b) for a, b in zip(opts, row["options"])):
        return "numbers_changed"
    # A reordered option keeps its numbers, so check each new option still resembles its own original most.
    for i, opt in enumerate(opts):
        if overlap(opt, row["options"][i]) < max(overlap(opt, other) for other in row["options"]):
            return "options_reordered"
    return "too_similar" if overlap(new["question"], row["question"]) > 0.8 else None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--items", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--n", type=int, default=150)
    ap.add_argument("--seed", type=int, default=20261106)
    ap.add_argument("--rpm", type=float, default=8)
    args = ap.parse_args()
    rows = [r for r in map(json.loads, open(args.items, encoding="utf-8")) if r["data_split"] == "train"]
    random.Random(args.seed).shuffle(rows)
    url, key_env = PROVIDERS["nvidia"]
    headers, pacer = {"Authorization": f"Bearer {os.environ[key_env]}"}, Pacer(args.rpm)
    kept, fails = 0, {}
    with open(args.output, "x", encoding="utf-8") as fh:
        for row in rows:
            if kept == args.n:
                break
            item = json.dumps({"question": row["question"], "options": row["options"]}, ensure_ascii=False)
            body = {"model": WRITER, "messages": [{"role": "user", "content": PROMPT.format(item=item)}],
                    "max_tokens": 800, "temperature": 0.3, **NO_THINK_BODY["nvidia"]}
            resp, err = post_with_retries(url + "/chat/completions", body, 180, headers, pacer, 2)
            reply = ((resp or {}).get("choices") or [{}])[0].get("message", {}).get("content") or ""
            try:
                new = json.loads(reply[reply.index("{"):reply.rindex("}") + 1])
            except ValueError:
                new = None
            reason = "api_error" if err else valid(row, new)
            if reason:
                fails[reason] = fails.get(reason, 0) + 1
                continue
            fh.write(json.dumps({"id": row["id"] + "~p", "source_id": row["id"], "question": new["question"],
                                 "options": new["options"], "answer_index": row["answer_index"],
                                 "medical_topic": row["medical_topic"], "difficulty_level": "paraphrase",
                                 "new_knowledge_candidate": row["teacher"]["new_knowledge_candidate"]},
                                ensure_ascii=False) + "\n")
            fh.flush()
            kept += 1
    print(f"kept {kept}, failed {fails}")


if __name__ == "__main__":
    base = {"question": "Liều 10 mg cho lao?", "options": ["1 mg", "2 mg", "3 mg", "4 mg"]}
    good = {"question": "Với bệnh lao, cần dùng 10 mg khi nào?", "options": ["1 mg", "2 mg", "3 mg", "4 mg"]}
    assert valid(base, good) is None
    assert valid(base, {**good, "question": "Với bệnh lao, cần dùng 20 mg khi nào?"}) == "numbers_changed"
    assert valid(base, {**good, "options": ["5 mg", "2 mg", "3 mg", "4 mg"]}) == "numbers_changed"
    assert valid(base, base) == "too_similar" and valid(base, None) == "shape"
    text = {"question": "Bệnh lao có gì?", "options": ["hang lao", "dịch màng phổi", "viêm gan", "sỏi thận"]}
    swapped = {"question": "Với lao, thấy dấu hiệu nào?", "options": ["dịch màng phổi", "hang lao", "viêm gan", "sỏi thận"]}
    assert valid(text, swapped) == "options_reordered"
    main()

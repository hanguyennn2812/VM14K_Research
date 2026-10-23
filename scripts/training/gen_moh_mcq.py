#!/usr/bin/env python3
"""
gen_moh_mcq.py — pilot of CS1-style training data (arXiv 2610.27099): exam questions that an LLM writes
from Ministry of Health (MoH) guideline chunks.

Chunks come from the Infectious Diseases MoH folders, chunked as in rag_moh.py; code lists and tables are
skipped. The writer drafts up to 3 Vietnamese four-option questions per sampled chunk, each with a quote
from the chunk. Questions that refer to "the text" or have malformed options are dropped. The options are
shuffled with a seed, so the key is not tied to the writer's favourite position. Each question records
its TF-IDF similarity to the closest VM14K val/test item, so near-copies of held-out items can be removed.
The key check and the teacher probabilities come afterwards from d3 27B with the chunk in its state
(modal_decision.py --items ... --context own).

    python scripts/training/gen_moh_mcq.py --chunks 170        # about 500 questions
    python scripts/training/gen_moh_mcq.py --review            # after the two d3 runs on the pilot

Writes data/derived/moh_mcq/pilot.jsonl. --review writes reports/eval/MOH_MCQ_pilot_review.csv: every
question with d3 27B's answer with and without its chunk, flags and 60 seeded rows marked for review.
"""
import argparse
import concurrent.futures
import csv
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "eval"))
from rag_moh import SCOPES, item_text, moh_chunks  # noqa: E402
from run_eval import (LETTERS, NO_THINK_BODY, PROVIDERS, REPO_ROOT, RUNS_DIR, Pacer, load_rows,  # noqa: E402
                      post_with_retries)
from sklearn.feature_extraction.text import TfidfVectorizer  # noqa: E402

WRITER = "nvidia/nemotron-3-ultra-550b-a55b"
OUT = os.path.join(REPO_ROOT, "data", "derived", "moh_mcq", "pilot.jsonl")
REVIEW_CSV = os.path.join(REPO_ROOT, "reports", "eval", "MOH_MCQ_pilot_review.csv")
PROMPT = """You write questions for the Vietnamese medical licensing exam. Below is an excerpt from a \
Vietnamese Ministry of Health guideline.

Write up to 3 multiple-choice questions in Vietnamese that test clinical knowledge stated in the excerpt: \
diagnosis, criteria, classification, first-line treatment, doses, complications, prevention.
Rules:
- exactly 4 options, exactly one correct according to the excerpt, the other three plausible but wrong;
- each question stands alone: never mention "the excerpt", "the document", "theo văn bản", "theo hướng dẫn";
- no questions about document numbers, dates, codes, administrative procedure or operating equipment;
- if the excerpt holds no clinical knowledge (a table of contents, a list of names, a code list), return [].
Reply with JSON only: [{{"question": "...", "options": ["...", "...", "...", "..."], "answer_index": 0, \
"evidence": "a short verbatim quote from the excerpt that supports the answer"}}]

Excerpt:
{text}"""
SELF_REFERENCE = re.compile(r"đoạn trích|văn bản|tài liệu|theo hướng dẫn|excerpt", re.I)


def clinical(text):
    """False for code lists and tables: many ICD-like codes or a high share of digits."""
    codes = len(re.findall(r"\b[A-Z]\d{2}(?:\.\d+)?\b", text))
    return codes < 5 and sum(ch.isdigit() for ch in text) / max(len(text), 1) < 0.08


def parse(reply):
    """Valid questions from the writer's reply; anything malformed is dropped."""
    try:
        items = json.loads(reply[reply.index("["):reply.rindex("]") + 1])
    except ValueError:
        return []
    out = []
    for q in items if isinstance(items, list) else []:
        opts = q.get("options") if isinstance(q, dict) else None
        if (isinstance(opts, list) and len(opts) == 4 and all(isinstance(o, str) and o.strip() for o in opts)
                and len({o.strip() for o in opts}) == 4 and q.get("answer_index") in range(4)
                and isinstance(q.get("question"), str) and q["question"].strip()
                and not SELF_REFERENCE.search(q["question"] + " ".join(opts))):
            out.append({"question": q["question"].strip(), "options": [o.strip() for o in opts],
                        "answer_index": q["answer_index"], "evidence": str(q.get("evidence") or "").strip()})
    return out


def squash(s):
    return " ".join(s.lower().split())


def review():
    """Join the pilot with d3 27B's answers with and without the chunk into a CSV for human review."""
    def run(style):
        with open(os.path.join(RUNS_DIR, f"decision__vllm-sr_d3__{style}__moh-pilot.jsonl"), encoding="utf-8") as fh:
            return {r["id"]: r for r in map(json.loads, fh)}

    with open(OUT, encoding="utf-8") as fh:
        items = [json.loads(line) for line in fh]
    own, bare = run("choice-own"), run("choice")
    sample = set(random.Random(1).sample([r["id"] for r in items], min(60, len(items))))
    rows = []
    for r in items:
        o, b, key = own[r["id"]], bare[r["id"]], LETTERS[r["answer_index"]]
        flag = ("d3 đọc văn bản vẫn chọn khác đáp án" if o["pred"] != key
                else "trích dẫn không có trong đoạn" if not r["evidence_in_chunk"]
                else "d3 không cần văn bản cũng đúng" if b["pred"] == key else "")
        rows.append({"Duyệt mẫu": "x" if r["id"] in sample else "", "Mã câu": r["id"], "Văn bản nguồn": r["doc"],
                     "Câu hỏi": r["question"],
                     "Các phương án": "\n".join(f"{LETTERS[i]}. {t}" for i, t in enumerate(r["options"])),
                     "Đáp án (máy viết)": f"{key}. {r['options'][r['answer_index']]}", "Trích dẫn": r["evidence"],
                     "d3 có văn bản": f"{o['pred']} (P đáp án {o['probs'][r['answer_index']]:.2f})",
                     "d3 không văn bản": f"{b['pred']} (P đáp án {b['probs'][r['answer_index']]:.2f})",
                     "Cờ": flag, "Đánh giá (Đúng / Sai / Không rõ / Không lâm sàng)": "", "Ghi chú": "",
                     "Đoạn văn bản gốc": r["chunk_text"]})
    with open(REVIEW_CSV, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    n = len(items)
    agree = sum(own[r["id"]]["pred"] == LETTERS[r["answer_index"]] for r in items)
    known = sum(bare[r["id"]]["pred"] == LETTERS[r["answer_index"]] for r in items)
    print(f"{n} questions -> {REVIEW_CSV}\nd3 27B with the chunk agrees with the key: {agree} ({100 * agree / n:.1f}%)"
          f"\nd3 27B without the chunk: {known} ({100 * known / n:.1f}%)")
    for f in sorted({row["Cờ"] for row in rows}):
        print(f"  {f or '(no flag: key confirmed, new to d3)'}: {sum(row['Cờ'] == f for row in rows)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chunks", type=int, default=170)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--rpm", type=float, default=30)
    ap.add_argument("--review", action="store_true")
    args = ap.parse_args()
    if args.review:
        review()
        return

    chunks = moh_chunks(SCOPES["infect"][0])
    usable = [c for c in chunks if clinical(c["text"])]
    sample = random.Random(args.seed).sample(usable, min(args.chunks, len(usable)))
    print(f"{len(chunks)} chunks, {len(usable)} clinical, sampling {len(sample)}", flush=True)

    url, key_env = PROVIDERS["nvidia"]
    headers, pacer = {"Authorization": f"Bearer {os.environ[key_env]}"}, Pacer(args.rpm)

    def write(chunk):
        body = {"model": WRITER, "messages": [{"role": "user", "content": PROMPT.format(text=chunk["text"])}],
                "max_tokens": 2000, "temperature": 0.3, **NO_THINK_BODY["nvidia"]}
        resp, err = post_with_retries(url + "/chat/completions", body, 180, headers, pacer, 4)
        reply = ((resp or {}).get("choices") or [{}])[0].get("message", {}).get("content") or ""
        return chunk, parse(reply), err

    records, failed = [], 0
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for n, (chunk, qs, err) in enumerate(ex.map(write, sample), 1):
            failed += err is not None
            for k, q in enumerate(qs):
                perm = list(range(4))
                random.Random(f"{args.seed}:{chunk['id']}:{k}").shuffle(perm)
                records.append({
                    "id": f"moh-{chunk['id']}-{k}", "question": q["question"],
                    "options": [q["options"][j] for j in perm], "answer_index": perm.index(q["answer_index"]),
                    "evidence": q["evidence"], "evidence_in_chunk": bool(q["evidence"]) and
                    squash(q["evidence"]) in squash(chunk["text"]),
                    "chunk_id": chunk["id"], "doc": chunk["doc"], "chunk_text": chunk["text"],
                    "medical_topic": ["Infectious Diseases"], "difficulty_level": "generated", "writer": WRITER})
            if n % 20 == 0:
                print(f"{n}/{len(sample)} chunks, {len(records)} questions, {failed} failed calls", flush=True)

    # Near-copies of held-out VM14K items would leak the test set into training: record the closest one.
    held = load_rows("val", None, 0) + load_rows("test", None, 0)
    tvec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True).fit([item_text(r) for r in held + records])
    sim = tvec.transform([item_text(r) for r in records]) @ tvec.transform([item_text(r) for r in held]).T
    for r, row in zip(records, sim.tocsr()):
        dense = row.toarray().ravel()
        r["heldout_max_sim"], r["heldout_nearest"] = round(float(dense.max()), 4), held[int(dense.argmax())]["id"]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        for r in records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    keys = [r["answer_index"] for r in records]
    print(f"{len(records)} questions from {len(sample)} chunks ({failed} failed calls) -> {OUT}\n"
          f"key positions A-D: {[keys.count(i) for i in range(4)]}; quote found in chunk: "
          f"{sum(r['evidence_in_chunk'] for r in records)}; held-out similarity >= 0.5: "
          f"{sum(r['heldout_max_sim'] >= 0.5 for r in records)}")


if __name__ == "__main__":
    assert clinical("Sốt xuất huyết Dengue có ba giai đoạn: sốt, nguy hiểm và hồi phục.")
    assert not clinical("A00 Tả A01 Thương hàn A02 Nhiễm Salmonella A03 Lỵ trực khuẩn A04 Nhiễm khuẩn ruột")
    ok = '[{"question": "Q?", "options": ["a", "b", "c", "d"], "answer_index": 2, "evidence": "x"}]'
    assert parse("```json\n" + ok + "\n```")[0]["answer_index"] == 2
    assert parse(ok.replace('"Q?"', '"Theo văn bản, Q?"')) == [] and parse("no json") == []
    assert parse(ok.replace('"d"', '"c"')) == []  # duplicate options
    main()

#!/usr/bin/env python3
"""Fact-recall probe from MoH guidelines: pick the true statement from a pair differing in one clinical detail.

Option texts are new, so familiarity with trained answers cannot help. Pairs come from train documents, tagged
seen/new against the trained questions of that chunk, and from val documents as an untrained control. Test
documents are never read.

    python scripts/training/gen_moh_pairs.py --teacher-train TEACHER.train.jsonl --manifest SPLIT.json --output OUT.jsonl
"""
import argparse
import concurrent.futures
import json
import os
import random
import re

import gen_moh_mcq as g
from moh_mcq_source import generation_chunks

STEM = "Phát biểu nào sau đây đúng?"
PROMPT = """You write fact-checking items for Vietnamese clinicians from a Ministry of Health guideline excerpt.

Write up to 3 pairs of Vietnamese statements testing different clinical facts stated in the excerpt: diagnostic
criteria, doses, routes, durations, thresholds, age groups, contraindications, regimens.
Rules:
- "true" states a fact exactly as the excerpt supports it; "false" is the same sentence with ONE clinical detail
  changed so it contradicts the excerpt (a dose, route, duration, threshold, age group or drug);
- the changed detail must make "false" clearly wrong by the excerpt, never merely unmentioned or still acceptable;
- each statement stands alone and explicitly names the disease or condition;
- never mention the excerpt, document or guideline; no administrative, reporting or responsibility facts;
- do not add rankings or absolutes the excerpt does not use; do not infer from unclear tables;
- if the excerpt holds no such clinical fact, return [].
Reply with JSON only: [{{"true": "...", "false": "...", "disease": "short name from the excerpt",
"evidence": "a short verbatim quote from the excerpt supporting the true statement"}}]

Excerpt:
{text}"""


def words(text):
    return set(re.findall(r"\w+", g.fold(text)))


def jaccard(a, b):
    x, y = words(a), words(b)
    return len(x & y) / max(len(x | y), 1)


def parse_pairs(reply):
    try:
        rows = json.loads(reply[reply.index("["):reply.rindex("]") + 1])
    except ValueError:
        return []
    keep = ("true", "false", "disease", "evidence")
    return [{k: r[k].strip() for k in keep} for r in rows if isinstance(rows, list) and isinstance(r, dict)
            and all(isinstance(r.get(k), str) and r[k].strip() for k in keep)]


def pair_reason(pair, chunk):
    """Reuse the question filters on the true statement; the pair must differ, but only in a detail."""
    q = {"question": pair["true"], "options": ["a", "b", "c", "d"], "answer_index": 0,
         "evidence": pair["evidence"], "disease": pair["disease"]}
    reason = g.quality_reason(q, chunk["text"], chunk["raw_text"])
    if reason:
        return reason
    if g.squash(pair["true"]) == g.squash(pair["false"]):
        return "identical_pair"
    if jaccard(pair["true"], pair["false"]) < 0.5:
        return "not_one_detail"
    if g.SELF_REFERENCE.search(pair["false"]) or g.text_problem(pair["false"]):
        return "broken_false_statement"
    return None


def fact_tag(pair, trained):
    """seen when a trained question of this chunk covers the same fact, else new."""
    for row in trained:
        answer = row["question"] + " " + row["options"][row["answer_index"]]
        if g.compact(pair["evidence"]) in g.compact(row["evidence"]) or g.compact(row["evidence"]) in g.compact(
                pair["evidence"]) or len(words(pair["true"]) & words(answer)) / max(len(words(pair["true"])), 1) >= 0.6:
            return "seen"
    return "new"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--teacher-train", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--train-chunks", type=int, default=120)
    ap.add_argument("--seed", type=int, default=20261106)
    ap.add_argument("--rpm", type=float, default=8)
    ap.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()
    if os.path.exists(args.output):
        ap.error(f"Refusing to overwrite {args.output}")
    chunks, _ = generation_chunks()
    chunks = [c for c in chunks if g.clinical(c["text"])]
    selected, _ = g.select_manifest_chunks(chunks, args.manifest)  # train and val only; raises on test
    rng = random.Random(args.seed)
    train = [c for c in selected if c["data_split"] == "train"]
    rng.shuffle(train)
    sample = train[:args.train_chunks] + [c for c in selected if c["data_split"] == "val"]
    rng.shuffle(sample)
    trained = {}
    with open(args.teacher_train, encoding="utf-8") as fh:
        for row in map(json.loads, fh):
            trained.setdefault(row["chunk_id"], []).append(row)

    url, key_env = g.PROVIDERS["nvidia"]
    headers, pacer = {"Authorization": f"Bearer {os.environ[key_env]}"}, g.Pacer(args.rpm)

    def write(chunk):
        body = {"model": g.WRITER, "messages": [{"role": "user", "content": PROMPT.format(text=chunk["text"])}],
                "max_tokens": 1600, "temperature": 0.3, **g.NO_THINK_BODY["nvidia"]}
        resp, err = g.post_with_retries(url + "/chat/completions", body, 180, headers, pacer, 2)
        reply = ((resp or {}).get("choices") or [{}])[0].get("message", {}).get("content") or ""
        return chunk, reply, err

    seen, counts, kept = set(), {}, 0
    with concurrent.futures.ThreadPoolExecutor(args.workers) as ex, open(args.output, "x", encoding="utf-8") as out:
        for done, (chunk, reply, err) in enumerate(ex.map(write, sample), 1):
            pairs = parse_pairs(reply)
            if err or not pairs:
                key = "api_error" if err else "empty_reply"
                counts[key] = counts.get(key, 0) + 1
            for k, pair in enumerate(pairs[:3]):
                reason = pair_reason(pair, chunk) or ("duplicate" if g.squash(pair["true"]) in seen else None)
                if reason:
                    counts[reason] = counts.get(reason, 0) + 1
                    continue
                seen.add(g.squash(pair["true"]))
                pid = f"pair-{chunk['id']}-{k}"
                answer = random.Random(f"{args.seed}:{pid}").randrange(2)
                options = [pair["false"], pair["false"]]
                options[answer] = pair["true"]
                options[1 - answer] = pair["false"]
                group = "control" if chunk["data_split"] == "val" else fact_tag(pair, trained.get(chunk["id"], []))
                out.write(json.dumps({
                    "id": pid, "question": STEM, "options": options, "answer_index": answer, "group": group,
                    "disease": pair["disease"], "evidence": pair["evidence"], "chunk_id": chunk["id"],
                    "doc_id": chunk["doc_id"], "data_split": chunk["data_split"],
                    "disease_group": chunk["disease_group"], "chunk_text": chunk["text"], "raw_text": chunk["raw_text"],
                    "medical_topic": ["Infectious Diseases"], "difficulty_level": "generated-pair"},
                    ensure_ascii=False) + "\n")
                out.flush()
                kept += 1
            if done % 10 == 0:
                print(f"{done}/{len(sample)} chunks, {kept} pairs, rejected {counts}", flush=True)
    print(f"{kept} pairs from {len(sample)} chunks; rejected {counts}")


if __name__ == "__main__":
    good = {"true": "Bệnh lao dùng thuốc A 10 mg", "false": "Bệnh lao dùng thuốc A 20 mg", "disease": "bệnh lao",
            "evidence": "thuốc A 10 mg"}
    source = {"text": "Bệnh lao: dùng thuốc A 10 mg mỗi ngày", "raw_text": "dùng thuốc A 10 mg mỗi ngày"}
    assert pair_reason(good, source) is None
    assert pair_reason({**good, "false": good["true"]}, source) == "identical_pair"
    assert pair_reason({**good, "false": "Viêm phổi cần thở oxy kéo dài nhiều ngày liền"}, source) == "not_one_detail"
    assert pair_reason({**good, "evidence": "không có"}, source) == "evidence_not_verbatim"
    assert parse_pairs("no json") == [] and parse_pairs('[{"true": "x"}]') == []
    assert fact_tag(good, [{"question": "Q", "options": ["z"], "answer_index": 0, "evidence": "thuốc A 10 mg"}]) == "seen"
    assert fact_tag(good, [{"question": "Q", "options": ["z"], "answer_index": 0, "evidence": "khác hẳn"}]) == "new"
    main()

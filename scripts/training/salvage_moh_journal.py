#!/usr/bin/env python3
"""Re-apply today's filters to an attempts journal: no writer calls, never overwrites its input.

Candidates rejected by the old literal disease/evidence checks, verifier API errors, and replies
dropped only for a "Theo hướng dẫn" lead-in re-enter through the same filters. Salvaged records are
unverified: the mandatory d3-with-source gate (filter_moh_teacher_labels.py) still decides.
"""
import argparse
import collections
import json
import random
from pathlib import Path

import gen_moh_mcq as g
from moh_mcq_source import generation_chunks

RETRY = {"missing_disease_in_question", "disease_not_in_source", "evidence_not_verbatim", "verifier_error"}


def candidates(entry):
    """Candidates worth re-testing; a verifier_rejected or duplicate stays rejected."""
    for row in entry["rejected"]:
        if row["reason"] in RETRY:
            yield row["reason"], row["candidate"]
        elif row["reason"] == "empty_or_malformed_writer_reply":
            for q in g.parse(row["reply"]):
                yield row["reason"], q


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, help="generated JSONL with a companion .attempts.jsonl")
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--seed", type=int, default=20261105)
    args = ap.parse_args()
    if Path(args.output).exists():
        ap.error(f"Refusing to overwrite {args.output}")
    usable, _ = generation_chunks()
    chunks = {c["id"]: c for c in g.select_manifest_chunks(usable, args.manifest)[0]}
    with open(args.input, encoding="utf-8") as fh:
        previous = [json.loads(line) for line in fh if line.strip()]

    # Today's filters also tighten: previously accepted records must pass them too.
    records, outcome = [], collections.Counter()
    for r in previous:
        reason = g.quality_reason(r, chunks[r["chunk_id"]]["text"], chunks[r["chunk_id"]]["raw_text"])
        if reason:
            outcome[f"dropped_old:{reason}"] += 1
        else:
            records.append(r)

    held = g.load_rows("val", None, 0) + g.load_rows("test", None, 0)
    vec = g.TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True).fit([g.item_text(r) for r in held])
    held_vec = vec.transform([g.item_text(r) for r in held]).T
    seen = {g.squash(r["question"]) for r in records}
    by_group = collections.defaultdict(list)
    for r in records:
        by_group[r["disease_group"]].append(r)

    with open(args.input + ".attempts.jsonl", encoding="utf-8") as fh:
        entries = {e["chunk_id"]: e for e in map(json.loads, fh)}
    for chunk_id, entry in sorted(entries.items()):
        chunk = chunks[chunk_id]
        for n, (old_reason, q) in enumerate(candidates(entry)):
            reason = g.quality_reason(q, chunk["text"], chunk["raw_text"])
            if not reason:
                perm = list(range(4))
                random.Random(f"{args.seed}:{chunk_id}:r{n}").shuffle(perm)
                r = {"id": f"moh-full-{chunk_id}-r{n}", "question": q["question"],
                     "options": [q["options"][j] for j in perm], "answer_index": perm.index(q["answer_index"]),
                     "disease": q["disease"], "evidence": q["evidence"], "evidence_in_chunk": True,
                     "chunk_id": chunk_id, "doc_id": chunk["doc_id"], "doc": chunk["doc"],
                     "data_split": chunk["data_split"], "disease_group": chunk["disease_group"],
                     "section": chunk["section"], "source_path": chunk["source_path"], "page": chunk["page"],
                     "chunk_text": chunk["text"], "raw_text": chunk["raw_text"],
                     "medical_topic": ["Infectious Diseases"], "difficulty_level": "generated", "writer": g.WRITER,
                     "verifier": {"accept": None, "deferred_to": "d3_with_source", "salvaged_from": old_reason,
                                  "original_answer_index": q["answer_index"]}}
                sim = (vec.transform([g.item_text(r)]) @ held_vec).toarray().ravel()
                r["heldout_max_sim"] = round(float(sim.max()), 4)
                r["heldout_nearest"] = held[int(sim.argmax())]["id"]
                group = r["disease_group"]
                # Free-form labels vary, so compare within the frozen disease group instead of within a label.
                same = [{**p, "disease": group} for p in by_group[group]]
                reason = ("heldout_near_copy" if sim.max() >= 0.5 else
                          "duplicate_question" if g.squash(r["question"]) in seen else
                          "near_duplicate_knowledge" if g.near_duplicate({**r, "disease": group}, same) else None)
            if reason:
                outcome[f"{old_reason}->{reason}"] += 1
                continue
            outcome[f"{old_reason}->SALVAGED"] += 1
            records.append(r)
            by_group[r["disease_group"]].append(r)
            seen.add(g.squash(r["question"]))

    with open(args.output, "x", encoding="utf-8") as fh:
        for r in records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(previous)} -> {len(records)} questions")
    for key, value in sorted(outcome.items()):
        print(f"  {key}: {value}")
    print("by split:", collections.Counter(r["data_split"] for r in records))
    print("by group:", collections.Counter(r["disease_group"] for r in records).most_common())


if __name__ == "__main__":
    main()

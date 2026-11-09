#!/usr/bin/env python3
"""
export_context_bodies.py — Choice request bodies with retrieved context, for kaggle_decision.py (T1, PLAN_2026-11-09).

Builds, exactly as modal_decision.add_context does (same `Solved exam questions...` and DOCS_HEAD text, same
rag_moh retrieval over all MoH chunks and TF-IDF train neighbours), the state of each request:

  val-infect  the 245 val items of Infectious Diseases x 6 conditions declared in the plan:
              zero, shots (TF-IDF), docs, shots+docs, shotsemb (3 closest train items by nemotron-embed cosine),
              shotsemb+docs
  pairs       the 369 gated fact pairs x zero, docs (top-3 over all MoH chunks; query = question + options), own
              (the pair's own `chunk_text`, the ceiling)
  test-infect (--split test, only for T6) the 232 test items of Infectious Diseases, for --conds

Each record: run, id, state, questions (request_body), and the metadata the analysis needs (cond, gold, top_sim,
shot_sim_max for TF-IDF and embeddings, chunk ids, group). Also writes reference_zero_val.json (the H100 bf16
d3-flash predictions, for the T2 smoke check) and dataset-metadata.json. Embeddings of the 7,313 train questions
are cached in data/interim/vm14k_train_emb.npz. Query and train items are both embedded as `query`
(question-to-question similarity, symmetric).

    python scripts/eval/export_context_bodies.py --out D:/tmp/vm14k-claude2/ctx_bodies
    python scripts/eval/export_context_bodies.py --out DIR --split test --conds zero shots+docs   # T6 only
"""
import argparse
import concurrent.futures
import json
import os
import sys
import time

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rag_moh import DOCS_HEAD, K_DOCS, K_SHOTS, item_text, setup  # noqa: E402
from rag_moh import embed as rag_embed  # noqa: E402
from run_eval import LETTERS, REPO_ROOT, RUNS_DIR, SPLIT_PATH, load_rows  # noqa: E402
from run_jev import request_body  # noqa: E402

MODEL = "vllm-sr/d3-flash"
VAL_CONDS = ["zero", "shots+docs", "shots", "docs", "shotsemb", "shotsemb+docs"]  # run order: decisive first
PROBE_CONDS = ["zero", "docs", "own"]
PAIRS = os.path.join(REPO_ROOT, "data", "derived", "moh_mcq", "fact_pairs_v1_20261106.gated.jsonl")
TRAIN_EMB = os.path.join(REPO_ROOT, "data", "interim", "vm14k_train_emb.npz")
REF = os.path.join(RUNS_DIR, "decision__vllm-sr_d3-flash__choice__val.jsonl")


def embed(texts, kind, size=1):
    """rag_moh.embed one text per request, 6 in flight: on 2026-11-09 the NVIDIA embeddings endpoint answered
    HTTP 500 to most batches of 2+ texts but reliably to single texts (~1.2 s each)."""
    def one(i):
        b = texts[i:i + size]
        try:
            return rag_embed(b, kind)
        except SystemExit:
            return np.concatenate([rag_embed([t], kind) for t in b])

    with concurrent.futures.ThreadPoolExecutor(6) as ex:
        return np.concatenate(list(ex.map(one, range(0, len(texts), size))))


def train_embeddings(train):
    ids = [r["id"] for r in train]
    if os.path.exists(TRAIN_EMB):
        c = np.load(TRAIN_EMB)
        if list(c["ids"]) == ids:
            return c["emb"].astype(np.float32)
    e = embed([item_text(r) for r in train], "query")
    np.savez_compressed(TRAIN_EMB, ids=np.array(ids), emb=e.astype(np.float16))
    return e


def build_state(question, cond, train, shot_idx, chunks, doc_idx, own_text=None):
    """The request state: context blocks, then `Question: ...` (modal_decision.add_context's format)."""
    parts = []
    if "shots" in cond:  # shots and shotsemb
        parts.append("Solved exam questions similar to this one:\n\n" + "\n\n".join(
            f"Q: {train[j]['question']}\nA: {train[j]['options'][train[j]['answer_index']]}" for j in shot_idx))
    if own_text is not None:
        parts.append(f"{DOCS_HEAD}\n\n[1] {own_text}")
    elif "docs" in cond:
        parts.append(DOCS_HEAD + "\n\n" + "\n\n".join(f"[{n + 1}] {chunks[j]['text']}" for n, j in enumerate(doc_idx)))
    return "\n\n".join(parts + ["Question: " + question])


def rank(sim, k):
    """Top-k column indices per row, least similar first (the closest example sits next to the question)."""
    return np.argsort(sim, axis=1)[:, ::-1][:, :k][:, ::-1]


def make_records(rows, run_prefix, conds, train, chunks, chunk_emb, train_emb, tvec, extra=lambda r: {}):
    tf_sim = (tvec.transform([item_text(r) for r in rows]) @ tvec.transform([item_text(r) for r in train]).T).toarray()
    q_emb = embed([item_text(r) for r in rows], "query")
    em_sim, doc_sim = q_emb @ train_emb.T, q_emb @ chunk_emb.T
    shots_tf, shots_em = rank(tf_sim, K_SHOTS), rank(em_sim, K_SHOTS)
    top = np.argsort(doc_sim, axis=1)[:, ::-1][:, :K_DOCS]
    out = []
    for cond in conds:
        for k, r in enumerate(rows):
            shots = shots_em[k] if "shotsemb" in cond else shots_tf[k]
            own = r.get("chunk_text") if cond == "own" else None
            assert cond != "own" or own, f"no chunk_text for {r['id']}"
            body = request_body(r, r["options"], MODEL)
            body["state"] = build_state(r["question"], cond, train, shots, chunks, top[k], own)
            out.append({"run": f"{run_prefix}__{cond}", "id": r["id"], "cond": cond, "state": body["state"],
                        "questions": body["questions"], "model": MODEL, "gold": LETTERS[r["answer_index"]],
                        "n_options": len(r["options"]), "medical_topic": r["medical_topic"],
                        "difficulty_level": r["difficulty_level"],
                        "top_sim": round(float(doc_sim[k, top[k, 0]]), 4),
                        "shot_sim_max": round(float(tf_sim[k].max()), 4),
                        "shot_sim_max_emb": round(float(em_sim[k].max()), 4),
                        "chunks": [chunks[j]["id"] for j in top[k]] if "docs" in cond and cond != "own" else [],
                        **extra(r)})
    return out


def check(recs, n_val, n_pairs, conds, split_of, probe_conds):
    """Counts, unique ids per run, no test id in a val export, the smoke/zero state is the bare question."""
    runs = {}
    for r in recs:
        runs.setdefault(r["run"], []).append(r["id"])
    for run, ids in runs.items():
        assert len(ids) == len(set(ids)), f"duplicate ids in {run}"
    n_runs_val = sum(r.startswith("val-infect") for r in runs)
    assert len(recs) == n_val * len(conds) + (n_pairs * len(probe_conds) if probe_conds else 0), len(recs)
    assert n_runs_val == len(conds)
    for r in recs:
        if r["run"].startswith("val-infect"):
            assert split_of[r["id"]] == "val", r["id"]
        if r["cond"] == "zero":
            assert r["state"].startswith("Question: ") and "Reference excerpts" not in r["state"]
        if r["cond"].endswith("docs") or r["cond"] == "own":
            assert "Reference excerpts" in r["state"]
        if "shots" in r["cond"]:
            assert r["state"].count("\nA: ") >= K_SHOTS
    assert not any(split_of.get(i) == "test" for run, ids in runs.items() if run.startswith("val-") for i in ids)


def selfcheck_unit():
    train = [{"question": f"q{i}", "options": ["x", "y"], "answer_index": 1} for i in range(4)]
    chunks = [{"text": f"c{i}"} for i in range(3)]
    s = build_state("Q?", "shots+docs", train, [0, 1, 2], chunks, [2, 1, 0])
    assert s.index("Solved exam") < s.index("Reference excerpts") < s.index("Question: Q?")
    assert s.count("A: y") == 3 and "[3] c0" in s
    assert build_state("Q?", "zero", train, [], chunks, []) == "Question: Q?"
    assert rank(np.array([[.1, .9, .5, .7]]), 3).tolist() == [[2, 3, 1]]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--split", default="val", choices=["val", "test"])
    ap.add_argument("--conds", nargs="+", default=VAL_CONDS)
    args = ap.parse_args()
    selfcheck_unit()
    if args.split == "test":
        print("TEST EXPORT: the single scoring run of T6; use only with the frozen configuration.")
    chunks, chunk_emb, train = setup("all")
    train_emb = train_embeddings(train)
    assert train_emb.shape[0] == len(train)
    allrows = load_rows(args.split, None, 0)
    rows = [r for r in allrows if "Infectious Diseases" in r["medical_topic"]]
    # Fitted on train + the whole split, as rag_moh.Prompts does, so `shots` matches the earlier runs.
    tvec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True).fit([item_text(r) for r in train + allrows])
    recs = make_records(rows, f"{args.split}-infect", args.conds, train, chunks, chunk_emb, train_emb, tvec)
    probe = []
    if args.split == "val":
        with open(PAIRS, encoding="utf-8") as fh:
            pairs = [json.loads(line) for line in fh]
        probe = make_records(pairs, "pairs", PROBE_CONDS, train, chunks, chunk_emb, train_emb, tvec,
                             extra=lambda r: {"group": r["group"]})
    with open(SPLIT_PATH, encoding="utf-8") as fh:
        split_of = json.load(fh)
    n_pairs = len(probe) // len(PROBE_CONDS)
    check(recs + probe, len(rows), n_pairs, args.conds, split_of, PROBE_CONDS if probe else None)
    if args.split == "val":
        assert len(rows) == 245 and n_pairs == 369 and len(recs + probe) == 245 * 6 + 369 * 3
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "bodies.jsonl"), "w", encoding="utf-8") as fh:
        for r in recs + probe:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    if args.split == "val":
        with open(REF, encoding="utf-8") as fh:
            ref = {r["id"]: r["pred"] for r in map(json.loads, fh)}
        with open(os.path.join(args.out, "reference_zero_val.json"), "w", encoding="utf-8") as fh:
            json.dump({r["id"]: ref[r["id"]] for r in rows}, fh)
    with open(os.path.join(args.out, "dataset-metadata.json"), "w", encoding="utf-8") as fh:
        json.dump({"title": "vm14k ctx bodies", "id": "trcnguynontrung/vm14k-ctx-bodies", "licenses": [{"name": "other"}]},
                  fh)
    print(f"wrote {len(recs + probe)} bodies ({len(recs)} {args.split}-infect, {len(probe)} pairs) to {args.out}; self-check ok")


if __name__ == "__main__":
    main()

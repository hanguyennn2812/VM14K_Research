#!/usr/bin/env python3
"""
rag_moh.py — do Ministry of Health (MoH) guideline excerpts help on VM14K?

Two scopes, both fixed before any result:
  infect  the infectious-disease folders (Truyền nhiễm, HIV, STDs, Ký sinh trùng, Nhiễm khuẩn học -
          Vi sinh) and the items labelled Infectious Diseases: the pilot
  all     every MoH folder and every item, whatever its topic label: the main run, scored on the whole split
Chunks the scope's MoH PDFs, retrieves the chunks closest to each question (cosine of NVIDIA
nemotron-3.5-embed-8b embeddings, question + options as the query; chunk embeddings cached in
data/interim/), and builds up to four prompts per item:

  zero        the paper's Fig. 6 prompt
  docs        the same, preceded by the top-K MoH excerpts
  shots       the 3 most similar train questions with their keys as earlier chat turns, chosen exactly
              as kaggle_27b.py does, so `shots` reproduces its fewshot3-tfidf prompts
  shots+docs  both

Two ways to score them: an OpenAI-compatible API (default), or --export DIR, which writes the prompts
for kaggle_27b_rag.py (Qwen3.5-27B NF4 on Kaggle, letter-logit scored). Each record keeps `top_sim`,
the best chunk's similarity, so a gate ("add excerpts only when the best one scores at least t") is
evaluated offline: gated = the docs answer if top_sim >= t, else the answer without docs. t is picked
on val (best accuracy, smallest t on a tie) and applied to test unchanged. --report writes
reports/eval/RAG_MOH.md.

    python scripts/eval/rag_moh.py --export <dir>                       # prompts for the Kaggle job
    python scripts/eval/rag_moh.py --scope all --export <dir>
    python scripts/eval/rag_moh.py --split val --cond zero docs         # via the NVIDIA API
    python scripts/eval/rag_moh.py --report --prefix hf-logit__Qwen_Qwen3.5-27B-bnb4
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
import sys
import threading
from pathlib import Path

import numpy as np
import pymupdf
from sklearn.feature_extraction.text import TfidfVectorizer

HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "analysis"))
from compare_runs import mcnemar_exact  # noqa: E402
from moh_corpus_audit import fix_mojibake  # noqa: E402
from run_eval import (LETTERS, NO_THINK_BODY, PROVIDERS, REPO_ROOT, RUNS_DIR, FATAL_HTTP, Pacer,  # noqa: E402
                      build_prompt, done_records, load_rows, parse_letter, permute, post_with_retries)
from summarize_eval import load_run  # noqa: E402

SCOPES = {  # name -> (MoH folders, None = all; VM14K topic of the items, None = all)
    "infect": (["Truyền nhiễm", "HIV", "STDs", "Ký sinh trùng", "Nhiễm khuẩn học - Vi sinh"], "Infectious Diseases"),
    "all": (None, None),
}
CHUNK_WORDS, CHUNK_STEP, MIN_CHARS = 200, 150, 50  # MIN_CHARS: the corpus audit's scanned-page floor
K_DOCS, K_SHOTS = 3, 3
DOCS_HEAD = "Reference excerpts from Vietnamese Ministry of Health guidelines (they may not be relevant):"
TAG = {"zero": "paper", "docs": "moh-k3", "shots": "fewshot3-tfidf", "shots+docs": "fewshot3-tfidf+moh-k3"}
# Kaggle run order: the comparison that decides the gate first, so a cut-off run still answers it.
# The test `zero` and `shots` runs already exist for the whole split (kaggle_27b.py).
EXPORT = {"infect": [("val", "shots"), ("val", "shots+docs"), ("test", "shots+docs"), ("val", "docs"),
                     ("test", "docs"), ("val", "zero")],
          "all": [("val", "shots"), ("val", "shots+docs"), ("test", "shots+docs")]}
EMB_MODEL = "nvidia/nemotron-3.5-embed-8b"
EMB_CACHE = os.path.join(REPO_ROOT, "data", "interim", "moh_{scope}_emb.npz")
OUT_MD = os.path.join(RUNS_DIR, "..", "RAG_MOH_{scope}.md")
GATES = [0.0, 0.35, 0.4, 0.45, 0.5, 0.55]  # val best-chunk similarity: median 0.385, 90th percentile 0.53


def item_text(r):
    return r["question"] + " " + " ".join(r["options"])


def moh_chunks(folders):
    """200-word windows over every readable page of the chosen folders, byte-identical files once."""
    root = next(p for p in Path(REPO_ROOT, "data").iterdir() if fix_mojibake(p.name) == "Chuyên khoa")
    seen, chunks = set(), []
    for folder in (d for d in sorted(root.iterdir())
                   if d.is_dir() and (folders is None or fix_mojibake(d.name) in folders)):
        for pdf in sorted(folder.rglob("*.pdf")):
            digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
            if digest in seen:
                continue
            seen.add(digest)
            with pymupdf.open(pdf) as doc:
                pages = [page.get_text() for page in doc]
            if sum(len("".join(p.split())) for p in pages) / max(len(pages), 1) < MIN_CHARS:
                continue  # scanned document: the audit's document-level floor
            words = " ".join(p for p in pages if len("".join(p.split())) >= MIN_CHARS).split()
            for s in range(0, max(len(words) - CHUNK_WORDS, 0) + 1, CHUNK_STEP):
                chunks.append({"id": f"{digest[:10]}:w{s}", "doc": fix_mojibake(pdf.stem)[:80],
                               "text": " ".join(words[s:s + CHUNK_WORDS])})
    return chunks


def embed(texts, kind):
    """Unit-normalised embeddings, 32 texts per request, 6 requests in flight."""
    headers = {"Authorization": f"Bearer {os.environ['NVIDIA_API_KEY']}"}

    def batch(b):
        resp, err = post_with_retries(PROVIDERS["nvidia"][0] + "/embeddings",
                                      {"input": b, "model": EMB_MODEL, "encoding_format": "float",
                                       "input_type": kind, "truncate": "END"}, 300, headers, Pacer(0), 5)
        if resp is None:
            sys.exit(f"embedding failed: {err}")
        return [d["embedding"] for d in resp["data"]]

    with concurrent.futures.ThreadPoolExecutor(6) as ex:
        e = np.array([v for vs in ex.map(batch, [texts[i:i + 32] for i in range(0, len(texts), 32)]) for v in vs],
                     dtype=np.float32)
    return e / np.linalg.norm(e, axis=1, keepdims=True)


def chunk_embeddings(chunks, scope):
    ids, path = [c["id"] for c in chunks], EMB_CACHE.format(scope=scope)
    if os.path.exists(path):
        cache = np.load(path)
        if list(cache["ids"]) == ids:
            return cache["emb"].astype(np.float32)
    e = embed([c["text"] for c in chunks], "passage")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    np.savez_compressed(path, ids=np.array(ids), emb=e.astype(np.float16))
    return e


def scope_rows(split, scope):
    topic = SCOPES[scope][1]
    return [r for r in load_rows(split, None, 0) if topic is None or topic in r["medical_topic"]]


class Prompts:
    """The scope's items in one split, with their top MoH chunks and train examples."""

    def __init__(self, split, scope, chunks, chunk_emb, train):
        rows = load_rows(split, None, 0)
        # Fitted on train + the whole split, as kaggle_27b.py does, so the examples match its run.
        tvec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True).fit([item_text(r) for r in train + rows])
        self.rows = scope_rows(split, scope)
        shot_sim = tvec.transform([item_text(r) for r in self.rows]) @ tvec.transform([item_text(r) for r in train]).T
        self.shots = [row.toarray().ravel().argsort()[::-1][:K_SHOTS][::-1] for row in shot_sim.tocsr()]
        doc_sim = embed([item_text(r) for r in self.rows], "query") @ chunk_emb.T
        self.top = doc_sim.argsort(axis=1)[:, ::-1][:, :K_DOCS]
        self.top_sim = np.take_along_axis(doc_sim, self.top[:, :1], axis=1).ravel()
        self.split, self.scope, self.chunks, self.train = split, scope, chunks, train

    def build(self, k, cond):
        """(chat messages, top chunk indices) for item k under cond."""
        r, top = self.rows[k], self.top[k]
        msgs = []
        if "shots" in cond:
            for j in self.shots[k]:  # least similar first, so the closest example sits next to the question
                ex = self.train[j]
                options, gold, _ = permute(ex, "fewshot")
                msgs += [{"role": "user", "content": build_prompt("paper", ex["question"], options)},
                         {"role": "assistant", "content": LETTERS[gold]}]
        prompt = build_prompt("paper", r["question"], r["options"])
        if "docs" in cond:
            prompt = DOCS_HEAD + "\n\n" + "\n\n".join(f"[{n + 1}] {self.chunks[j]['text']}"
                                                       for n, j in enumerate(top)) + "\n\n" + prompt
        return msgs + [{"role": "user", "content": prompt}], top

    def record(self, k, cond, top, **scored):
        r = self.rows[k]
        return {"id": r["id"], "prompt_style": TAG[cond], "think": "off", "shuffle_seed": None,
                "split": f"{self.split}-{self.scope}", "medical_topic": r["medical_topic"],
                "difficulty_level": r["difficulty_level"], "n_options": len(r["options"]),
                "perm": list(range(len(r["options"]))), "gold": LETTERS[r["answer_index"]],
                "top_sim": round(float(self.top_sim[k]), 4),
                "chunks": [self.chunks[j]["id"] for j in top] if "docs" in cond else [], **scored}


def setup(scope):
    chunks = moh_chunks(SCOPES[scope][0])
    emb = chunk_embeddings(chunks, scope)
    print(f"{len(chunks)} chunks from {len({c['id'].split(':')[0] for c in chunks})} documents", flush=True)
    return chunks, emb, load_rows("train", None, 0)


def export(args):
    chunks, emb, train = setup(args.scope)
    plan = EXPORT[args.scope]
    prompts = {s: Prompts(s, args.scope, chunks, emb, train) for s in dict(plan)}
    os.makedirs(args.export, exist_ok=True)
    path = os.path.join(args.export, "prompts.jsonl")
    with open(path, "w", encoding="utf-8") as fh:
        for split, cond in plan:
            p = prompts[split]
            for k in range(len(p.rows)):
                msgs, top = p.build(k, cond)
                fh.write(json.dumps({"run": f"{TAG[cond]}__{split}-{args.scope}", "messages": msgs,
                                     **p.record(k, cond, top)}, ensure_ascii=False) + "\n")
    print(f"wrote {sum(len(prompts[s].rows) for s, _ in plan)} prompts to {path}")


def ask(cfg, messages):
    body = {"model": cfg["model"], "messages": messages, "max_tokens": 32, "temperature": 0.0,
            **NO_THINK_BODY.get(cfg["provider"], {})}
    resp, err = post_with_retries(cfg["base_url"] + "/chat/completions", body, 120,
                                  {"Authorization": f"Bearer {cfg['api_key']}"}, cfg["pacer"], 5)
    if resp is None:
        return "", err
    return ((resp.get("choices") or [{}])[0].get("message") or {}).get("content") or "", None


def run(args):
    chunks, emb, train = setup(args.scope)
    p = Prompts(args.split, args.scope, chunks, emb, train)
    base_url, key_env = PROVIDERS[args.provider]
    cfg = {"model": args.model, "provider": args.provider, "base_url": base_url,
           "api_key": os.environ.get(key_env), "pacer": Pacer(args.rpm)}
    if not cfg["api_key"]:
        sys.exit(f"set {key_env} first")
    stop = threading.Event()

    def work(k, cond):
        if stop.is_set():
            return None
        msgs, top = p.build(k, cond)
        raw, err = ask(cfg, msgs)
        if err and any(err.startswith(f) for f in FATAL_HTTP):
            stop.set()
        pred = parse_letter(raw, len(p.rows[k]["options"]))
        return p.record(k, cond, top, provider=args.provider, model=args.model, pred=pred,
                        correct=pred == LETTERS[p.rows[k]["answer_index"]], raw=raw, error=err)

    for cond in args.cond:
        path = os.path.join(RUNS_DIR, f"{args.provider}__{args.model.replace('/', '_')}__{TAG[cond]}__"
                                      f"{args.split}-{args.scope}.jsonl")
        done = done_records(path)
        todo = [k for k, r in enumerate(p.rows) if r["id"] not in done]
        print(f"{cond}: {len(todo)} to do -> {os.path.relpath(path, REPO_ROOT)}", flush=True)
        with open(path, "a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(args.workers) as ex:
            futures = [ex.submit(work, k, cond) for k in todo]
            for n, fut in enumerate(concurrent.futures.as_completed(futures), 1):
                rec = fut.result()
                if rec:
                    fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    fh.flush()
                if n % 50 == 0:
                    print(f"  {cond}: {n}/{len(todo)}", flush=True)
        if stop.is_set():
            sys.exit("stopped on a fatal HTTP error; rerun to resume")


def acc(run, ids):
    return 100 * sum(run[i]["correct"] for i in ids) / len(ids)


def gated(with_docs, without, t, ids):
    return {i: with_docs[i] if with_docs[i]["top_sim"] >= t else without[i] for i in ids}


def paired(label, a, b, ids):
    a_only = sum(a[i]["correct"] and not b[i]["correct"] for i in ids)
    b_only = sum(b[i]["correct"] and not a[i]["correct"] for i in ids)
    p = mcnemar_exact(a_only, b_only)
    return (f"| {label} | {len(ids)} | {acc(a, ids):.1f} | {acc(b, ids):.1f} | {acc(b, ids) - acc(a, ids):+.1f} | "
            f"{a_only} | {b_only} | {p:.2g}{' *' if p < 0.05 else ''} |")


def report(args):
    def load_split(split):
        ids = [r["id"] for r in scope_rows(split, args.scope)]
        runs = {}
        for cond, tag in TAG.items():  # a scope run, else the full-split run restricted to the scope
            for path in (os.path.join(RUNS_DIR, f"{args.prefix}__{tag}__{split}-{args.scope}.jsonl"),
                         os.path.join(RUNS_DIR, f"{args.prefix}__{tag}__{split}.jsonl")):
                if os.path.exists(path):
                    run = {r["id"]: r for r in load_run(path)}
                    if all(i in run for i in ids):
                        runs[cond] = run
                        break
        return ids, runs

    folders, topic = SCOPES[args.scope]
    lines = [f"# VM14K: MoH guideline excerpts, scope `{args.scope}`", "",
             f"Generated by `scripts/eval/rag_moh.py --report --scope {args.scope} --prefix {args.prefix}`. "
             f"MoH folders: {', '.join(folders) if folders else 'all'}; items: {topic or 'all'}; "
             f"{CHUNK_WORDS}-word chunks, top {K_DOCS} by {EMB_MODEL} cosine. `gated t` adds "
             "the excerpts only when the best chunk's similarity is at least t; t is picked on val (best accuracy, "
             "smallest t on a tie) and applied to test unchanged. McNemar exact.", ""]
    chosen = {}
    for split in ("val", "test"):
        ids, runs = load_split(split)
        if not runs:
            continue
        lines += [f"## {split} ({len(ids)} items)", "", "| condition | accuracy | unparsed |", "|---|---:|---:|"]
        lines += [f"| {c} | {acc(run, ids):.1f} | {sum(run[i]['pred'] is None for i in ids)} |"
                  for c, run in runs.items()]
        rows = [paired(f"{a} → {b}", runs[a], runs[b], ids)
                for a, b in (("zero", "docs"), ("zero", "shots"), ("shots", "shots+docs"), ("zero", "shots+docs"))
                if a in runs and b in runs]
        for a, b in (("zero", "docs"), ("shots", "shots+docs")):
            if a in runs and b in runs:
                if split == "val":
                    chosen[b] = max(GATES, key=lambda t: (acc(gated(runs[b], runs[a], t, ids), ids), -t))
                if b in chosen:
                    g = gated(runs[b], runs[a], chosen[b], ids)
                    rows.append(paired(f"{a} → {b} gated {chosen[b]}", runs[a], g, ids))
        lines += ["", "| comparison (A → B) | n | A % | B % | B − A | only A right | only B right | p |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|"] + rows
        for a, b in (("zero", "docs"), ("shots", "shots+docs")):
            if a in runs and b in runs:
                lines += ["", f"Gate on `{b}` (else `{a}`)", "", "| t | items with excerpts | accuracy |",
                          "|---:|---:|---:|"]
                lines += [f"| {t} | {100 * sum(runs[b][i]['top_sim'] >= t for i in ids) / len(ids):.0f}% | "
                          f"{acc(gated(runs[b], runs[a], t, ids), ids):.1f} |" for t in GATES]
        lines.append("")
    with open(OUT_MD.format(scope=args.scope.upper()), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default="google/gemma-4-31b-it")
    ap.add_argument("--provider", default="nvidia", choices=sorted(PROVIDERS))
    ap.add_argument("--scope", default="infect", choices=list(SCOPES))
    ap.add_argument("--split", default="val", choices=["val", "test"])
    ap.add_argument("--cond", nargs="+", default=["zero", "docs"], choices=list(TAG))
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--rpm", type=float, default=40)
    ap.add_argument("--export", metavar="DIR", help="write the prompts for kaggle_27b_rag.py and stop")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--prefix", default="hf-logit__Qwen_Qwen3.5-27B-bnb4", help="run-file prefix for --report")
    args = ap.parse_args()
    if args.report:
        report(args)
    elif args.export:
        export(args)
    else:
        run(args)


if __name__ == "__main__":
    main()

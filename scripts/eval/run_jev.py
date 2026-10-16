#!/usr/bin/env python3
"""
run_jev.py — score TypeSafe's Jev (a "System One" model) on the VM14K split.

Each question becomes one Choice question (docs.typesafe.ai/primitives/choice):
the state is the question text, the instruction is the paper's Fig. 6 line,
and the criteria map the option letters to the option texts. Jev returns a
probability per letter, so nothing is parsed; the probabilities are kept for
calibration and for fusion/routing with other runs (analyze_jev.py).

--shuffle-seed N presents the options in a seeded order, as run_eval.py does,
to test position bias. Letters in the record are as presented, `perm[i]` is the
original index of the option shown at position i, and `probs_orig` holds the
probabilities in the original option order.

Records follow run_eval.py's format (reports/eval/runs/<run>.jsonl); a rerun
resumes where it stopped. Key: TYPESAFE_API_KEY (console.typesafe.ai/keys).

    python scripts/eval/run_jev.py --dry-run             # print one request, send nothing
    python scripts/eval/run_jev.py --limit 20            # smoke test
    python scripts/eval/run_jev.py                       # E2: full test split
    python scripts/eval/run_jev.py --shuffle-seed 1      # E5: shuffled options
"""
import argparse
import concurrent.futures
import json
import os
import sys
import threading
import time

sys.path.insert(0, os.path.dirname(__file__))
from run_eval import LETTERS, RUNS_DIR, Pacer, done_records, load_rows, permute, post_with_retries  # noqa: E402

URL = "https://api.typesafe.ai/v1/systemone"
INSTRUCTION = "Choose the correct option from these answers"
FATAL = ("HTTP 401", "HTTP 403", "HTTP 404")


def request_body(row, options, model):
    return {
        "state": row["question"],
        "model": model,
        "questions": {"answer": {"type": "choice", "instructions": INSTRUCTION,
                                 "criteria": {LETTERS[i]: opt for i, opt in enumerate(options)}}},
    }


def to_record(row, gold, perm, resp, err, args, latency):
    """One run_eval-style record from a Jev response (or an error)."""
    n = len(perm)
    rec = {
        "id": row["id"], "provider": "typesafe", "model": args.model, "prompt_style": "paper-choice",
        "think": False, "shuffle_seed": args.shuffle_seed, "split": args.split,
        "medical_topic": row["medical_topic"], "difficulty_level": row["difficulty_level"],
        "n_options": n, "perm": perm, "gold": LETTERS[gold], "pred": None, "correct": False,
        "probs": None, "probs_orig": None, "confidence": None, "model_version": None, "usage": None,
        "latency_s": round(latency, 3), "error": err,
    }
    if err is None:
        ans = (resp.get("answers") or {}).get("answer") or {}
        raw = ans.get("probabilities") or {}
        probs = [float(raw.get(LETTERS[i], 0.0)) for i in range(n)]
        if not sum(probs):
            rec["error"] = "no probabilities in response: " + json.dumps(resp, ensure_ascii=False)[:300]
            return rec
        choice = ans.get("choice")
        pred = choice if choice in LETTERS[:n] else LETTERS[probs.index(max(probs))]
        orig = [0.0] * n
        for i, p in enumerate(probs):
            orig[perm[i]] = p
        rec.update(pred=pred, correct=pred == LETTERS[gold], probs=[round(p, 5) for p in probs],
                   probs_orig=[round(p, 5) for p in orig], confidence=ans.get("confidence"),
                   model_version=resp.get("model"), usage=resp.get("usage"))
    return rec


def run_name(args):
    name = f"typesafe__{args.model}__choice__{args.split}"
    if args.shuffle_seed is not None:
        name += f"__shuf{args.shuffle_seed}"
    return name + (f"__n{args.limit}" if args.limit else "")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default="jev-latest")
    ap.add_argument("--split", default="test", choices=["train", "val", "test"])
    ap.add_argument("--limit", type=int, help="seeded subsample of the split")
    ap.add_argument("--shuffle-seed", type=int, help="present options in a seeded order (position-bias test)")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--rpm", type=float, default=300, help="request starts per minute, across workers")
    ap.add_argument("--timeout", type=float, default=60)
    ap.add_argument("--retries", type=int, default=4)
    ap.add_argument("--dry-run", action="store_true", help="print the first request body and exit")
    args = ap.parse_args()

    rows = load_rows(args.split, args.limit, 0)
    if args.dry_run:
        options, _, _ = permute(rows[0], args.shuffle_seed)
        print(json.dumps(request_body(rows[0], options, args.model), ensure_ascii=False, indent=2))
        return
    key = os.environ.get("TYPESAFE_API_KEY")
    if not key:
        sys.exit("TYPESAFE_API_KEY is not set (get a key at https://console.typesafe.ai/keys)")

    path = os.path.join(RUNS_DIR, run_name(args) + ".jsonl")
    done = done_records(path)
    todo = [r for r in rows if r["id"] not in done]
    print(f"model={args.model} split={args.split} rows={len(rows)} done={len(done)} todo={len(todo)} -> {path}", flush=True)
    headers = {"Authorization": f"Bearer {key}"}
    pacer, lock, stop = Pacer(args.rpm), threading.Lock(), threading.Event()

    def work(row):
        if stop.is_set():
            return None
        options, gold, perm = permute(row, args.shuffle_seed)
        t0 = time.time()
        resp, err = post_with_retries(URL, request_body(row, options, args.model), args.timeout, headers,
                                      pacer, args.retries)
        if err and err.startswith(FATAL):
            stop.set()
        return to_record(row, gold, perm, resp, err, args, time.time() - t0)

    os.makedirs(RUNS_DIR, exist_ok=True)
    n_ok = n_err = 0
    with open(path, "a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(args.workers) as ex:
        for rec in ex.map(work, todo):
            if rec is None:
                continue
            with lock:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                fh.flush()
            n_ok += rec["error"] is None
            n_err += rec["error"] is not None
            if rec["error"] and n_err <= 3:
                print("error:", rec["error"][:300], flush=True)
            if (n_ok + n_err) % 100 == 0:
                print(f"  {n_ok + n_err}/{len(todo)}", flush=True)
    recs = list(done_records(path).values())
    if recs:
        acc = sum(r["correct"] for r in recs) / len(recs)
        tokens = sum((r.get("usage") or {}).get("input_tokens", 0) for r in recs)
        print(f"{path}\nn={len(recs)} acc={100 * acc:.1f} errors_this_run={n_err} input_tokens={tokens}")
    if stop.is_set():
        sys.exit("stopped on an auth/model error (401/403/404): check TYPESAFE_API_KEY and --model")


if __name__ == "__main__":
    main()

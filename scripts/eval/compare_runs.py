#!/usr/bin/env python3
"""
compare_runs.py — paired comparison of two eval runs on the questions both answered.

Two runs on the same questions are paired data: a model that is 3 points better
overall may win on 40 questions and lose on 28, and only those discordant
questions carry information. McNemar's exact test on them is far more
sensitive than comparing two independent confidence intervals, and it is the
right test for "did the change (Vietnamese pre-training, RAG, fine-tuning)
help on this topic?".

    python scripts/eval/compare_runs.py reports/eval/runs/A.jsonl reports/eval/runs/B.jsonl
    python scripts/eval/compare_runs.py A.jsonl B.jsonl --topic Pulmonology --min-n 20
"""
import argparse
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from summarize_eval import CANONICAL_34, load_run  # noqa: E402


def mcnemar_exact(b, c):
    """Two-sided exact McNemar p-value from the discordant counts b and c."""
    n = b + c
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, i) for i in range(min(b, c) + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def paired(a, b):
    """(n, acc_a, acc_b, a_only, b_only, p) over ids answered by both."""
    ids = a.keys() & b.keys()
    a_only = sum(1 for i in ids if a[i]["correct"] and not b[i]["correct"])
    b_only = sum(1 for i in ids if b[i]["correct"] and not a[i]["correct"])
    n = len(ids)
    acc_a = sum(a[i]["correct"] for i in ids) / n if n else 0.0
    acc_b = sum(b[i]["correct"] for i in ids) / n if n else 0.0
    return n, acc_a, acc_b, a_only, b_only, mcnemar_exact(a_only, b_only)


def row(label, stats):
    n, acc_a, acc_b, a_only, b_only, p = stats
    star = "*" if p < 0.05 else " "
    return (f"{label:36s} {n:5d}  {100 * acc_a:5.1f}  {100 * acc_b:5.1f}  "
            f"{100 * (acc_b - acc_a):+5.1f}  {a_only:4d} {b_only:4d}  {p:.3g}{star}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_a")
    ap.add_argument("run_b")
    ap.add_argument("--topic", action="append", help="only these topics (repeatable)")
    ap.add_argument("--min-n", type=int, default=30, help="per-topic rows need this many shared questions")
    args = ap.parse_args()

    a = {r["id"]: r for r in load_run(args.run_a)}
    b = {r["id"]: r for r in load_run(args.run_b)}
    print(f"A = {os.path.basename(args.run_a)}\nB = {os.path.basename(args.run_b)}\n")
    print(f"{'':36s} {'n':>5s}  {'A%':>5s}  {'B%':>5s}  {'B-A':>5s}  {'A>B':>4s} {'B>A':>4s}  p (McNemar exact)")
    print(row("overall", paired(a, b)))

    topics = args.topic or sorted(CANONICAL_34)
    lines = []
    for t in topics:
        at = {i: r for i, r in a.items() if t in r["medical_topic"]}
        bt = {i: r for i, r in b.items() if t in r["medical_topic"]}
        stats = paired(at, bt)
        if stats[0] >= (1 if args.topic else args.min_n):
            lines.append((stats[2] - stats[1], row(t, stats)))
    if lines:
        print()
        for _, line in sorted(lines, reverse=True):
            print(line)
    print("\n* p < 0.05. A>B / B>A: questions only that run got right.")


if __name__ == "__main__":
    main()

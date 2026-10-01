#!/usr/bin/env python3
"""
raw_vs_clean.py — what a model scores on the raw VM14K release vs the cleaned split.

The paper scored models on the raw 12,488-row release. Cleaning keeps 10,567
rows byte-identical, edits 61 and removes 1,860 (dedup and quarantine), so a
model's raw score differs from its clean score only through those rows.
Re-running all 12,488 rows is unnecessary: an identical prompt under greedy
decoding gives the identical answer. Scoring just the 1,860 removed rows plus
the edited test rows is enough to rebuild the raw-release number, and it
says *which* removed rows move it.

    python scripts/eval/raw_vs_clean.py ids
        writes reports/eval/raw/fates.json and raw_delta_ids.txt
    python scripts/eval/run_eval.py --model qwen3.5:9b \\
        --data data/raw/data-processed-shuffled0.jsonl \\
        --ids reports/eval/raw/raw_delta_ids.txt --tag raw0-delta
    python scripts/eval/raw_vs_clean.py report \\
        --pair reports/eval/runs/qwen3.5_9b__paper__test.jsonl \\
               reports/eval/runs/qwen3.5_9b__paper__ids-raw0-delta.jsonl
        writes reports/eval/RAW_VS_CLEAN.md

Raw-release accuracy is estimated as
    (kept rows x accuracy on the test split with raw text
     + sum over removed categories of category accuracy x category size) / 12,488.
The kept-row term assumes the test split is representative of all kept rows
(it is a random stem-grouped split); the removed term is a census, not a
sample, once the delta run is complete.
"""
import argparse
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts", "analysis"))
from dedup_utils import normalize_vietnamese as norm  # noqa: E402
from summarize_eval import load_run, wilson  # noqa: E402

RAW_PATH = os.path.join(REPO_ROOT, "data", "raw", "data-processed-shuffled0.jsonl")
BASE_PATH = os.path.join(REPO_ROOT, "data", "baseline", "clean.jsonl")
CLEAN_PATH = os.path.join(REPO_ROOT, "data", "cleaned", "clean_final.jsonl")
QUAR_PATH = os.path.join(REPO_ROOT, "data", "quarantine", "quarantine_all.jsonl")
SPLIT_PATH = os.path.join(REPO_ROOT, "splits", "split_v1.json")
OUT_DIR = os.path.join(REPO_ROOT, "reports", "eval", "raw")
OUT_MD = os.path.join(REPO_ROOT, "reports", "eval", "RAW_VS_CLEAN.md")

QUAR_LABEL = {
    "stage02": "quarantined: blank question / <2 options",
    "stage03": "quarantined: duplicate option text",
    "stage06": "quarantined: refers to missing image/audio",
    "stage07": "quarantined: placeholder options",
    "stage10": "quarantined: corrupted option markers",
    "stage13": "quarantined: other defective options",
}
REMOVED_ORDER = [
    "dedup: duplicate, same answer",
    "dedup: duplicate, CONTRADICTING answer",
    "dedup: near-duplicate (fuzzy)",
    "dedup: cleaning stages 12/14",
] + list(QUAR_LABEL.values())

# Paper Table 3 pass@1 on the raw release, for models the paper also ran.
PAPER_RAW = {"llama3.1:8b": ("Llama-3.1-8B-Instruct", 48.73)}


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def compute_fates():
    raw = _load(RAW_PATH)
    base = {r["id"] for r in _load(BASE_PATH)}
    clean = {r["id"]: r for r in _load(CLEAN_PATH)}
    quar = {q["id"]: q for q in _load(QUAR_PATH)}

    def key(r):
        return norm(r["question"]), tuple(sorted(norm(o) for o in r["options"]))

    def answer(r):
        return norm(r["options"][r["answer_index"]])

    survivors = collections.defaultdict(list)
    for r in raw:
        if r["id"] in base:
            survivors[key(r)].append(r)

    fates = {}
    for r in raw:
        i = r["id"]
        if i in clean:
            c = clean[i]
            same = (c["question"], c["options"], c["answer_index"]) == (r["question"], r["options"], r["answer_index"])
            fates[i] = "kept: identical" if same else "kept: text edited"
        elif i in quar:
            fates[i] = QUAR_LABEL[quar[i]["source_stage"].split("_", 1)[0]]
        elif i in base:
            fates[i] = "dedup: cleaning stages 12/14"
        else:
            s = survivors.get(key(r))
            if not s:
                fates[i] = "dedup: near-duplicate (fuzzy)"
            elif any(answer(x) != answer(r) for x in s):
                fates[i] = "dedup: duplicate, CONTRADICTING answer"
            else:
                fates[i] = "dedup: duplicate, same answer"
    return fates


def cmd_ids(_args):
    fates = compute_fates()
    with open(SPLIT_PATH, encoding="utf-8") as fh:
        split_of = json.load(fh)
    delta = sorted(i for i, f in fates.items()
                   if not f.startswith("kept") or (f == "kept: text edited" and split_of.get(i) == "test"))
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "fates.json"), "w", encoding="utf-8") as fh:
        json.dump(fates, fh, ensure_ascii=False, indent=0, sort_keys=True)
    with open(os.path.join(OUT_DIR, "raw_delta_ids.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(delta) + "\n")
    for fate, n in sorted(collections.Counter(fates.values()).items()):
        print(f"{n:6d}  {fate}")
    print(f"\n{len(delta)} ids to score -> {os.path.relpath(OUT_DIR, REPO_ROOT)}/raw_delta_ids.txt")


def cell(k, n):
    if not n:
        return "–"
    lo, hi = wilson(k, n)
    return f"{100 * k / n:.1f} [{100 * lo:.0f}–{100 * hi:.0f}]"


def cmd_report(args):
    with open(os.path.join(OUT_DIR, "fates.json"), encoding="utf-8") as fh:
        fates = json.load(fh)
    population = collections.Counter(fates.values())
    n_kept = population["kept: identical"] + population["kept: text edited"]
    n_raw = len(fates)

    lines = ["# Raw release vs cleaned split", "",
             "Generated by `scripts/eval/raw_vs_clean.py report`. The raw release has "
             f"{n_raw:,} rows; cleaning keeps {n_kept:,} ({population['kept: text edited']} of them "
             f"with edited text) and removes {n_raw - n_kept:,}. Each model was scored on every "
             "removed row and on the test rows whose text cleaning edited, all with the raw "
             "release's own text (`data-processed-shuffled0.jsonl`). Accuracy in %, Wilson 95% "
             "interval in brackets.", "",
             "**Raw-release estimate** = (kept rows × test-split accuracy on raw text + Σ removed "
             "category accuracy × category size) / all raw rows. Its uncertainty is dominated by "
             "the test-split term (about ±0.2 points for the difference column).", ""]

    summary, per_cat = [], {}
    for clean_path, raw_path in args.pair:
        clean_recs = {r["id"]: r for r in load_run(clean_path)}
        raw_recs = {r["id"]: r for r in load_run(raw_path)}
        model = next(iter(clean_recs.values()))["model"]
        k_clean = sum(r["correct"] for r in clean_recs.values())
        n_clean = len(clean_recs)
        # test split with raw text: swap in raw-text answers for rows cleaning edited
        test_raw = {i: raw_recs.get(i, r) if fates.get(i) == "kept: text edited" else r
                    for i, r in clean_recs.items()}
        acc_test_raw = sum(r["correct"] for r in test_raw.values()) / len(test_raw)
        cats = collections.defaultdict(lambda: [0, 0])
        for i, r in raw_recs.items():
            f = fates.get(i, "")
            if not f.startswith("kept"):
                cats[f][0] += r["correct"]
                cats[f][1] += 1
        scored = sum(n for _, n in cats.values())
        expected = n_raw - n_kept
        removed_correct = sum(k / n * population[f] for f, (k, n) in cats.items() if n)
        est_raw = (n_kept * acc_test_raw + removed_correct) / n_raw
        acc_removed = sum(k for k, _ in cats.values()) / scored if scored else float("nan")
        paper = PAPER_RAW.get(model)
        summary.append([f"`{model}`", cell(k_clean, n_clean),
                        f"{100 * acc_removed:.1f}" + ("" if scored >= expected else f" (n={scored}/{expected})"),
                        f"**{100 * est_raw:.1f}**", f"{100 * (est_raw - k_clean / n_clean):+.1f}",
                        f"{paper[0]} {paper[1]:.2f}" if paper else "–"])
        per_cat[model] = cats

    header = ["model", "clean test split", "removed rows", "raw-release estimate", "raw − clean", "paper (raw)"]
    lines += ["## Headline", "", "| " + " | ".join(header) + " |", "|---" + "|---:" * (len(header) - 1) + "|"]
    lines += ["| " + " | ".join(row) + " |" for row in summary]
    lines += ["", "## Accuracy on each kind of removed row", "",
              "Compare each row with the model's clean test-split accuracy above. Rows whose "
              "accuracy sits near random (~27%) were unanswerable as released.", ""]
    models = list(per_cat)
    lines += ["| removed because | rows | " + " | ".join(f"`{m}`" for m in models) + " |",
              "|---|---:" + "|---:" * len(models) + "|"]
    for f in REMOVED_ORDER:
        if population[f]:
            lines.append(f"| {f} | {population[f]} | " +
                         " | ".join(cell(*per_cat[m].get(f, [0, 0])) for m in models) + " |")
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("ids", help="classify raw rows and write the delta id list")
    rp = sub.add_parser("report", help="raw-release estimate per model")
    rp.add_argument("--pair", nargs=2, action="append", required=True, metavar=("CLEAN_RUN", "RAW_DELTA_RUN"))
    args = ap.parse_args()
    {"ids": cmd_ids, "report": cmd_report}[args.cmd](args)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
summarize_eval.py — per-model and per-topic accuracy from run_ollama_eval.py output.

Reads every reports/eval/runs/*.jsonl (smoke runs named *__n<k>.jsonl are
skipped unless --include-smoke) and writes:

    reports/eval/SUMMARY.md      overall, paper top-10 topics, all topics, difficulty
    reports/eval/per_topic.csv   long format: run, topic, n, correct, acc, 95% CI

Topics are multi-label, as in the release: a question tagged
["Urology", "Nephrology"] counts once toward each. Topic strings are the raw
127 release labels; the 127 -> 34 canonical mapping is still pending review
(reports/analysis/topic_mapping_review.xlsx), so the tables mark which labels
are in the paper's 34-category list and which are not.

Paper numbers (arXiv 2506.01305 Tables 3-4) are pass@1 on the uncleaned
12,488-row release, not on our cleaned test split. They are a reference
point, not a same-questions comparison.

    python scripts/eval/summarize_eval.py
"""
import argparse
import collections
import csv
import glob
import json
import math
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUNS_DIR = os.path.join(REPO_ROOT, "reports", "eval", "runs")
OUT_MD = os.path.join(REPO_ROOT, "reports", "eval", "SUMMARY.md")
OUT_CSV = os.path.join(REPO_ROOT, "reports", "eval", "per_topic.csv")

# Paper Table 5.
CANONICAL_34 = {
    "Allergy and Immunology", "Anesthesiology", "Cardiology", "Dermatology", "Endocrinology",
    "Gastroenterology", "Geriatrics", "Hematology", "Infectious Diseases", "Internal Medicine",
    "Nephrology", "Neurology", "Nuclear Medicine", "Obstetrics and Gynecology", "Oncology",
    "Ophthalmology", "Orthopedics", "Otolaryngology", "Palliative Medicine", "Pathology",
    "Pediatrics", "Physical Medicine and Rehabilitation", "Psychiatry", "Pulmonology", "Radiology",
    "Rheumatology", "Sports Medicine", "Surgery", "Urology", "General Medicine", "Eastern Medicine",
    "Public Health", "Preventive Healthcare", "Emergency Medicine",
}

# Paper Table 3, overall pass@1.
PAPER_OVERALL_PASS1 = {
    "GPT-4o": 72.74, "o3-mini": 71.42, "Claude 3.5 Sonnet": 71.46, "Gemini 2.0 Flash": 75.67,
    "DeepSeek-R1": 78.17, "Qwen3-32B": 72.47, "Qwen3-30B-A3B": 71.32, "Llama 4 Maverick": 71.76,
    "Phi-4": 51.15, "Gemma3-27B-Instruct": 63.38, "Gemma3-12B-Instruct": 58.05,
    "Llama-3.1-8B-Instruct": 48.73, "Llama-3-70B-UltraMedical": 54.96, "Meditron3-70B": 42.27,
    "HuatuoGPT-o1-8B": 54.52, "Llama-3.1-8B-UltraMedical": 41.86, "Meditron3-8B": 23.05,
}

# Paper Table 4, pass@1 by the 10 most frequent topics.
PAPER_TOPIC_MODELS = ["GPT-4o", "o3-mini", "Llama 4 Maverick", "Claude 3.5 Sonnet",
                      "Qwen3-32B", "Gemini 2.0 Flash", "DeepSeek-R1"]
PAPER_TOPIC_PASS1 = {
    "Gastroenterology":          [72.07, 73.19, 73.31, 72.43, 74.02, 77.01, 81.47],
    "Obstetrics and Gynecology": [74.61, 69.80, 72.29, 74.12, 71.55, 77.18, 79.71],
    "Pulmonology":               [70.87, 70.82, 68.12, 68.66, 70.23, 74.00, 77.35],
    "Infectious Diseases":       [73.23, 72.24, 71.74, 71.63, 71.74, 76.20, 77.79],
    "Endocrinology":             [76.92, 76.79, 76.34, 75.63, 78.01, 78.27, 81.24],
    "Oncology":                  [75.86, 75.74, 76.58, 75.15, 77.41, 79.67, 82.64],
    "Pathology":                 [71.23, 67.61, 69.16, 70.97, 73.03, 74.19, 78.19],
    "Pediatrics":                [67.74, 67.48, 64.52, 68.65, 67.23, 68.39, 73.16],
    "Radiology":                 [70.81, 72.05, 69.57, 69.25, 70.19, 74.84, 77.48],
    "Surgery":                   [68.77, 66.83, 68.77, 68.61, 68.77, 71.36, 75.89],
}
PAPER_REF_COLS = ["Qwen3-32B", "DeepSeek-R1"]

DIFFICULTY_ORDER = ["Easy", "Medium", "Challenging", "Hard"]


def wilson(k, n, z=1.96):
    if n == 0:
        return 0.0, 0.0
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


def split_sizes():
    """Scorable rows per split (pending-review rows are never scored), for spotting partial runs."""
    with open(os.path.join(REPO_ROOT, "splits", "split_v1.json"), encoding="utf-8") as fh:
        split_of = json.load(fh)
    sizes = collections.Counter()
    with open(os.path.join(REPO_ROOT, "data", "cleaned", "clean_final.jsonl"), encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                r = json.loads(line)
                if not r.get("contradiction_pending_review"):
                    sizes[split_of.get(r["id"])] += 1
                    sizes["all"] += 1
    return sizes


def load_run(path):
    """Last error-free record per id (a resumed run may retry an id)."""
    latest = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue  # half-written last line of a run still in progress
                if rec.get("error") is None:
                    latest[rec["id"]] = rec
    return list(latest.values())


class Tally:
    __slots__ = ("n", "k")

    def __init__(self):
        self.n = 0
        self.k = 0

    def add(self, ok):
        self.n += 1
        self.k += bool(ok)

    @property
    def acc(self):
        return self.k / self.n if self.n else 0.0

    def cell(self, ci=True):
        if not self.n:
            return "–"
        if not ci:
            return f"{100 * self.acc:.1f}"
        lo, hi = wilson(self.k, self.n)
        return f"{100 * self.acc:.1f} [{100 * lo:.0f}–{100 * hi:.0f}]"


def summarize(recs):
    s = {
        "overall": Tally(), "always_a": Tally(), "pred_a": Tally(), "random": 0.0, "unparsed": 0,
        "topic": collections.defaultdict(Tally), "difficulty": collections.defaultdict(Tally),
    }
    for r in recs:
        s["overall"].add(r["correct"])
        s["always_a"].add(r["gold"] == "A")
        s["pred_a"].add(r["pred"] == "A")
        s["random"] += 1 / r["n_options"]
        s["unparsed"] += r["pred"] is None
        s["difficulty"][r["difficulty_level"]].add(r["correct"])
        for t in set(r["medical_topic"]):
            s["topic"][t].add(r["correct"])
    s["random"] /= max(len(recs), 1)
    return s


def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" if i == 0 else "---:" for i in range(len(header))) + "|"]
    out += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", nargs="*", help="explicit run files (default: all in reports/eval/runs)")
    ap.add_argument("--include-smoke", action="store_true")
    ap.add_argument("--min-n", type=int, default=15, help="hide topics with fewer scored questions")
    ap.add_argument("--common", action="store_true",
                    help="score every run only on the question ids all runs share "
                         "(e.g. full runs next to a --limit 400 screen)")
    ap.add_argument("--out-md", default=OUT_MD)
    ap.add_argument("--out-csv", default=OUT_CSV)
    args = ap.parse_args()

    paths = args.runs or sorted(glob.glob(os.path.join(RUNS_DIR, "*.jsonl")))
    if not args.include_smoke:
        paths = [p for p in paths if "__n" not in os.path.basename(p)]
    sizes = split_sizes()
    loaded = {os.path.basename(p)[:-len(".jsonl")]: load_run(p) for p in paths}
    loaded = {name: recs for name, recs in loaded.items() if recs}
    if args.common and loaded:
        shared = set.intersection(*({r["id"] for r in recs} for recs in loaded.values()))
        loaded = {name: [r for r in recs if r["id"] in shared] for name, recs in loaded.items()}
    runs = {}
    for name, recs in loaded.items():
        expected = sizes.get(recs[0].get("split"))
        if not args.common and expected and len(recs) < expected and "__n" not in name:
            name += f" (partial {len(recs)}/{expected})"
        runs[name] = summarize(recs)
    if not runs:
        raise SystemExit("no run files found")
    names = list(runs)

    lines = ["# VM14K zero-shot evaluation — summary", "",
             "Generated by `scripts/eval/summarize_eval.py`. Accuracy is pass@1 in %, "
             "with the Wilson 95% interval in brackets. Topics are multi-label, so topic "
             "counts sum to more than the number of questions.", ""]
    if args.common:
        lines += [f"**Restricted to the {next(iter(runs.values()))['overall'].n} question ids every "
                  "listed run answered (`--common`)**, so all columns score the same questions.", ""]
    lines += [
             "Paper columns are pass@1 from arXiv 2506.01305 on the uncleaned 12,488-row "
             "release, not on these questions: a reference point, not a matched comparison.", ""]

    lines += ["## Overall", ""]
    rows = []
    for name, s in runs.items():
        rows.append([f"`{name}`", s["overall"].n, s["overall"].cell(), s["unparsed"],
                     f"{100 * s['always_a'].acc:.1f}", f"{100 * s['random']:.1f}",
                     f"{100 * s['pred_a'].acc:.1f}"])
    lines += [md_table(["run", "n", "accuracy", "unparsed", "always-A", "random", "model picks A"], rows), "",
              "`always-A` and `random` are the two floors for the same questions; `model picks A` "
              "above the gold A-rate (the always-A column) means the model leans on the "
              "position bias the release already carries.", ""]
    lines += ["Paper reference, overall pass@1: " + ", ".join(
        f"{m} {v:.2f}" for m, v in PAPER_OVERALL_PASS1.items()) + ".", ""]

    lines += ["## Paper's top-10 topics (Table 4)", ""]
    header = ["topic", "n"] + [f"`{n}`" for n in names] + [f"paper {m}" for m in PAPER_REF_COLS] + ["paper range (7 models)"]
    rows = []
    for topic, vals in PAPER_TOPIC_PASS1.items():
        n = max(runs[name]["topic"][topic].n for name in names)
        ref = [f"{vals[PAPER_TOPIC_MODELS.index(m)]:.1f}" for m in PAPER_REF_COLS]
        rows.append([topic, n] + [runs[name]["topic"][topic].cell() for name in names] + ref
                    + [f"{min(vals):.1f}–{max(vals):.1f}"])
    lines += [md_table(header, rows), ""]

    all_topics = collections.Counter()
    for s in runs.values():
        for t, tal in s["topic"].items():
            all_topics[t] = max(all_topics[t], tal.n)

    for title, keep in (("## All topics in the paper's 34-category list", lambda t: t in CANONICAL_34),
                        ("## Topic labels outside the paper's 34 categories", lambda t: t not in CANONICAL_34)):
        shown = [t for t, n in all_topics.most_common() if keep(t) and n >= args.min_n]
        hidden = sum(1 for t, n in all_topics.items() if keep(t) and n < args.min_n)
        lines += [title, "", f"Labels with n ≥ {args.min_n}; {hidden} smaller labels hidden.", ""]
        rows = [[t, all_topics[t]] + [runs[name]["topic"][t].cell() for name in names] for t in shown]
        lines += [md_table(["topic", "n"] + [f"`{n}`" for n in names], rows), ""]

    lines += ["## Weakest topics per run", "",
              "Canonical topics with n ≥ 30, lowest accuracy first. `below` marks topics whose "
              "95% upper bound is under the run's overall accuracy — the candidates for a "
              "targeted improvement.", ""]
    for name, s in runs.items():
        overall = s["overall"].acc
        cand = [(t, tal) for t, tal in s["topic"].items() if t in CANONICAL_34 and tal.n >= 30]
        cand.sort(key=lambda x: x[1].acc)
        rows = [[t, tal.n, tal.cell(), "below" if wilson(tal.k, tal.n)[1] < overall else ""] for t, tal in cand[:6]]
        lines += [f"`{name}` (overall {100 * overall:.1f})", "", md_table(["topic", "n", "accuracy", ""], rows), ""]

    lines += ["## By difficulty", ""]
    rows = [[d, max(runs[n]["difficulty"][d].n for n in names)] + [runs[n]["difficulty"][d].cell() for n in names]
            for d in DIFFICULTY_ORDER]
    lines += [md_table(["difficulty", "n"] + [f"`{n}`" for n in names], rows), ""]

    os.makedirs(os.path.dirname(args.out_md), exist_ok=True)
    with open(args.out_md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    with open(args.out_csv, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["run", "topic", "in_paper_34", "n", "correct", "acc", "ci_lo", "ci_hi"])
        for name, s in runs.items():
            for t, tal in sorted(s["topic"].items(), key=lambda x: -x[1].n):
                lo, hi = wilson(tal.k, tal.n)
                w.writerow([name, t, t in CANONICAL_34, tal.n, tal.k, f"{tal.acc:.4f}", f"{lo:.4f}", f"{hi:.4f}"])
    print(f"wrote {os.path.relpath(args.out_md, REPO_ROOT)} and {os.path.relpath(args.out_csv, REPO_ROOT)} ({len(runs)} runs)")


if __name__ == "__main__":
    main()

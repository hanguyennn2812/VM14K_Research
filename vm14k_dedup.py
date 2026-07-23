#!/usr/bin/env python3
"""
vm14k_dedup.py — reproduce VM14K's OWN deduplication pipeline on the released data
and emit a cleaned dataset.

WHAT THIS IS
    A faithful re-implementation of the authors' Deduplication/deduplication.py,
    adapted to read the released JSONL (their code only reads a CSV with
    optionA..optionG columns) and to write a cleaned JSONL back out.

    The DEDUP LOGIC is theirs, parameter-for-parameter:
        - normaliser : dedup_utils.normalize_vietnamese  (imported, not copied)
        - vectoriser : TfidfVectorizer(min_df=5, max_df=0.8, ngram (1,1)) on QUESTIONS
        - blocking   : 2000-row row-blocks against the full corpus
        - epsilon1   : 1e-8   -> "exact" duplicate candidates
        - epsilon2   : 0.1    -> "near" duplicate candidates
        - Level 1    : drop j if norm-question equal AND sorted norm-option-set equal
        - Level 2    : drop j if fuzz(rm_cau(qi), rm_cau(qj)) >= 90 AND same option set
        - Level 3    : drop rows whose medicalTopic cell == "Other(No Category)"

DELIBERATE DIVERGENCES FROM THEIR SCRIPT  (all logged at runtime)
    1. Input is JSONL with an `options` array; theirs is CSV optionA..optionG.
       We transpose options[0..6] -> optionA..G, padding missing slots with "".
       (Their published code cannot read the published data without this.)
    2. Their code raises `ValueError: np.nan is an invalid document` on this data,
       because some questions normalise to "" (pandas reads them back as NaN).
       We coerce normalised questions to "" instead of NaN. Nothing else changes.
    3. We keep a stable back-reference to each original JSON row so the cleaned
       output is the ORIGINAL records (untouched), not the normalised CSV view.

WHAT "CLEAN" MEANS / KNOWN LIMITS  (these are properties of THEIR algorithm)
    - Candidates are nominated by QUESTION similarity only; options are a guard,
      not a key. Two copies of one question with DIFFERENT option sets are never
      merged (by design).
    - min_df=5 makes very short questions zero-vectors; they are never nominated,
      so a few exact duplicates survive (e.g. the "U brenner" pair). This script
      therefore reports a `residual_exact_duplicates` count so you can SEE what
      their pipeline leaves behind. It does NOT silently fix it.

USAGE
    python vm14k_dedup.py                              # defaults, no output file
    python vm14k_dedup.py data-processed-shuffled0.jsonl
    python vm14k_dedup.py data.jsonl --dedup-utils repo/Deduplication/dedup_utils.py
    python vm14k_dedup.py data.jsonl --out clean.jsonl --report report.json
"""

import argparse
import collections
import importlib.util
import json
import os
import sys

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from thefuzz import fuzz


# --------------------------------------------------------------------------- #
# Locate the authors' normaliser. We import THEIR module so "same question" is
# defined by their rules. No silent fallback: if it's missing we stop, because a
# different normaliser would produce different numbers and quietly invalidate the
# whole point.
# --------------------------------------------------------------------------- #
def load_authors_normaliser(explicit_path):
    candidates = []
    if explicit_path:
        candidates.append(explicit_path)
    candidates += [
        "dedup_utils.py",
        "repo/Deduplication/dedup_utils.py",
        os.path.join(os.path.dirname(__file__), "dedup_utils.py"),
    ]
    for path in candidates:
        if path and os.path.exists(path):
            spec = importlib.util.spec_from_file_location("dedup_utils", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod.normalize_vietnamese, mod.rm_cau, os.path.abspath(path)
    sys.exit(
        "ERROR: could not find the authors' dedup_utils.py.\n"
        "Pass it with --dedup-utils PATH (it lives in the repo's Deduplication/ dir).\n"
        "Refusing to run with a substitute normaliser, since that would change the numbers."
    )


def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            r["_line"] = lineno
            rows.append(r)
    return rows


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("data", nargs="?", default="data-processed-shuffled0.jsonl",
                    help="released JSONL (the original / shuffled0 file)")
    ap.add_argument("--dedup-utils", default=None,
                    help="path to the authors' dedup_utils.py")
    ap.add_argument("--out", default=None,
                    help="write cleaned JSONL here (original records, dupes removed)")
    ap.add_argument("--report", default=None,
                    help="write a JSON stats report here")
    args = ap.parse_args()

    if not os.path.exists(args.data):
        sys.exit(f"ERROR: cannot find {args.data!r}")

    normalize_vietnamese, rm_cau, norm_path = load_authors_normaliser(args.dedup_utils)

    rows = load_jsonl(args.data)
    n0 = len(rows)

    # ---- audit-side metrics (independent of their pipeline) ---------------- #
    def nq(r):
        return normalize_vietnamese(r["question"])

    def noptset(r):
        return tuple(sorted(normalize_vietnamese(str(o)) for o in r["options"]))

    def gold_text(r):
        i = r.get("answer_index")
        if not isinstance(i, int) or i < 0 or i >= len(r["options"]):
            return None
        return normalize_vietnamese(str(r["options"][i]))

    def audit(records):
        g = collections.defaultdict(list)
        for r in records:
            g[(nq(r), noptset(r))].append(r)
        dup = {k: v for k, v in g.items() if len(v) > 1}
        redundant = sum(len(v) - 1 for v in dup.values())
        contra = sum(1 for v in dup.values()
                     if len({gold_text(r) for r in v} - {None}) > 1)
        return dict(rows=len(records), unique_keys=len(g),
                    dup_groups=len(dup), redundant=redundant, contra_groups=contra)

    before = audit(rows)

    # ---- build the authors' expected frame (divergence #1) ----------------- #
    recs = []
    for r in rows:
        p = (list(r["options"]) + [""] * 7)[:7]
        recs.append({
            "question": r["question"],
            "optionA": p[0], "optionB": p[1], "optionC": p[2], "optionD": p[3],
            "optionE": p[4], "optionF": p[5], "optionG": p[6],
            "medicalTopic": ", ".join(r["medical_topic"])
                            if isinstance(r.get("medical_topic"), list)
                            else str(r.get("medical_topic", "")),
            "_row": r,
        })
    df = pd.DataFrame(recs).reset_index(drop=True)

    # ======================= THEIR PIPELINE (verbatim) ====================== #
    df["q"] = df["question"].apply(normalize_vietnamese)
    for c, s in [("oa", "optionA"), ("ob", "optionB"), ("oc", "optionC"),
                 ("od", "optionD"), ("oe", "optionE"), ("of", "optionF"),
                 ("og", "optionG")]:
        df[c] = df[s].apply(normalize_vietnamese)

    df["q"] = df["q"].fillna("").astype(str)   # divergence #2 (NaN guard)

    vectorizer = TfidfVectorizer(analyzer="word", lowercase=True, stop_words=None,
                                 ngram_range=(1, 1), min_df=5, max_df=0.8)
    X = vectorizer.fit_transform(df["q"])
    zero_vec = int((X.getnnz(axis=1) == 0).sum())

    epsilon1, epsilon2 = 1e-8, 0.1
    dup_pairs, near_pairs = [], []
    for i in range(X.shape[0] // 2000 + 1):
        s = i * 2000
        dist = 1 - X[s:s + 2000, :].dot(X.T).toarray()
        t = np.argwhere(dist < epsilon1)
        dup_pairs.append(t + [[s, 0]] * len(t))
        t2 = np.argwhere((dist < epsilon2) & (dist >= epsilon1))
        near_pairs.append(t2 + [[s, 0]] * len(t2))

    dup_pairs = np.concatenate(dup_pairs, axis=0)
    dup_pairs = dup_pairs[dup_pairs[:, 0] != dup_pairs[:, 1]]
    dup_pairs = np.unique(dup_pairs, axis=0)
    dup_pairs = dup_pairs[dup_pairs[:, 0] < dup_pairs[:, 1]]

    near_pairs = np.concatenate(near_pairs, axis=0)
    near_pairs = near_pairs[near_pairs[:, 0] != near_pairs[:, 1]]

    val = df[["q", "oa", "ob", "oc", "od", "oe", "of", "og"]].fillna("").values

    # Level 1 — exact
    removed = set()
    for i, j in dup_pairs:
        if i in removed or j in removed:
            continue
        if val[i, 0] == val[j, 0] and sorted(val[i, 1:]) == sorted(val[j, 1:]):
            removed.add(j)
    after_l1 = audit([r["_row"] for k, r in df.iterrows() if k not in removed])

    # Level 2 — near-dup
    removed_fuzz = set()
    for i, j in near_pairs:
        if i in removed or j in removed or i in removed_fuzz or j in removed_fuzz:
            continue
        if fuzz.ratio(rm_cau(val[i, 0]), rm_cau(val[j, 0])) >= 90 \
           and sorted(val[i, 1:]) == sorted(val[j, 1:]):
            removed_fuzz.add(j)
    keep_l2 = ~(df.index.isin(removed) | df.index.isin(removed_fuzz))

    # Level 3 — off-topic filter (their whole-cell string equality, as written)
    keep_l3 = keep_l2 & (df["medicalTopic"] != "Other(No Category)")
    # ======================================================================= #

    clean_rows = [df.iloc[k]["_row"] for k in range(len(df)) if keep_l3.iloc[k]]
    after = audit(clean_rows)

    # ---- report ------------------------------------------------------------ #
    line = "=" * 72
    print(line)
    print("VM14K — faithful reproduction of the authors' dedup pipeline")
    print(line)
    print(f"input        : {args.data}")
    print(f"normaliser   : {norm_path}")
    print(f"rows in      : {n0}")
    print(f"zero-vector questions (min_df=5, never nominated): {zero_vec}")
    print("-" * 72)
    hdr = f"{'stage':<22}{'rows':>8}{'dup grps':>10}{'redundant':>11}{'contra grps':>13}"
    print(hdr)
    print(f"{'released (before)':<22}{before['rows']:>8}{before['dup_groups']:>10}"
          f"{before['redundant']:>11}{before['contra_groups']:>13}")
    print(f"{'after Level 1 (exact)':<22}{after_l1['rows']:>8}{after_l1['dup_groups']:>10}"
          f"{after_l1['redundant']:>11}{after_l1['contra_groups']:>13}")
    print(f"{'after Levels 1-3':<22}{after['rows']:>8}{after['dup_groups']:>10}"
          f"{after['redundant']:>11}{after['contra_groups']:>13}")
    print("-" * 72)
    print(f"rows removed             : {n0 - after['rows']}")
    print(f"redundant copies removed : {before['redundant'] - after['redundant']} "
          f"of {before['redundant']}")
    print(f"contradiction groups     : {before['contra_groups']} -> {after['contra_groups']}")
    print(f"residual_exact_duplicates: {after['redundant']}  "
          f"(what their pipeline LEAVES; blame min_df=5 zero-vectors)")
    print(line)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            for r in clean_rows:
                r = {k: v for k, v in r.items() if k != "_line"}
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"wrote cleaned dataset: {args.out}  ({len(clean_rows)} rows)")

    if args.report:
        json.dump({"input": args.data, "normaliser": norm_path,
                   "rows_in": n0, "zero_vector_questions": zero_vec,
                   "before": before, "after_level1": after_l1, "after_all": after,
                   "rows_removed": n0 - after["rows"],
                   "residual_exact_duplicates": after["redundant"]},
                  open(args.report, "w"), indent=2)
        print(f"wrote report: {args.report}")


if __name__ == "__main__":
    main()

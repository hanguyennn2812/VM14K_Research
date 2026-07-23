#!/usr/bin/env python3
"""
VM14K — duplicates and self-contradictions, reproducibly.

One script, one grouping key, two results:

    Step 1  Load data-processed-shuffled0.jsonl (keep 1-indexed line numbers).
    Step 2  Normalise with the authors' own dedup_utils.normalize_vietnamese
            (strips diacritics, lowercases, removes punctuation, collapses space).
    Step 3  Group every row by:
                key = ( normalise(question), sorted normalise(each option) )
            The option set is sorted so option ORDER does not matter, so a
            shuffled copy collapses onto its original.

    Step 4a DUPLICATES     = every group of size >= 2.
    Step 4b CONTRADICTIONS = those groups where the normalised text of the
            marked-correct option is not the same across all rows.

Because the key already forces identical option sets, every contradiction is a
real one -- "different options => different answers" cannot sneak in.

--------------------------------------------------------------------------------
REQUIREMENTS
    - data-processed-shuffled0.jsonl        (the ORIGINAL / unshuffled file)
    - dedup_utils.py                        (from the repo's Deduplication/ dir)
      Put both next to this script, OR pass paths on the command line.

USAGE
    python vm14k_dupes_and_contradictions.py
    python vm14k_dupes_and_contradictions.py path/to/data-processed-shuffled0.jsonl
    python vm14k_dupes_and_contradictions.py data.jsonl --write   # also dump .md lists

EXPECTED OUTPUT (on the 12,488-row release)
    rows                 : 12488
    duplicate groups     : 1125   rows 2450   (19.62%)
    contradiction groups : 67     rows 152    (floor >= 0.537%)
--------------------------------------------------------------------------------
"""

import argparse
import collections
import json
import os
import sys

# ---- Step 2: the authors' own normaliser -------------------------------------
# We import their function rather than reimplementing it, so "same question" is
# defined by THEIR rules, not ours. If dedup_utils.py can't be found, we fall
# back to an inline copy of the same logic and say so loudly.
try:
    from dedup_utils import normalize_vietnamese as _normalize
    _NORM_SOURCE = "dedup_utils.normalize_vietnamese (authors' code)"
except Exception:  # pragma: no cover
    import re
    import unicodedata

    def _normalize(text):
        text = unicodedata.normalize("NFD", text)
        text = "".join(c for c in text if unicodedata.category(c) != "Mn")
        text = text.replace("đ", "d").replace("Đ", "D")
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        return re.sub(r"\s+", " ", text).strip()

    _NORM_SOURCE = "INLINE FALLBACK (dedup_utils.py not found — numbers may differ!)"


# ---- Step 1: load -------------------------------------------------------------
def load(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            row["_line"] = lineno
            rows.append(row)
    return rows


# ---- Step 3: the grouping key -------------------------------------------------
def group_key(row):
    """Normalised question + order-insensitive normalised option set."""
    q = _normalize(row["question"])
    optset = tuple(sorted(_normalize(o) for o in row["options"]))
    return (q, optset)


def gold_text(row):
    """Normalised text of the marked-correct option, or None if index is bad."""
    idx = row.get("answer_index")
    if not isinstance(idx, int) or idx < 0 or idx >= len(row["options"]):
        return None
    return _normalize(row["options"][idx])


# ---- md writers (optional) ----------------------------------------------------
def write_md(path, title, subtitle, groups, source_file):
    n_rows = sum(len(g) for g in groups)
    with open(path, "w", encoding="utf-8") as out:
        out.write(f"# {title}\n\n{subtitle}\n\n")
        out.write(f"Normalisation: {_NORM_SOURCE}\n")
        out.write(f"Line numbers refer to {source_file}.\n\n")
        out.write(f"Groups: {len(groups)}   Rows: {n_rows}\n\n")
        for gi, members in enumerate(groups, start=1):
            members = sorted(members, key=lambda r: r["_line"])
            topics = members[0].get("medical_topic", [])
            out.write(f"### Group {gi} — topic: {', '.join(topics)}\n")
            out.write(f"Q: {members[0]['question']}\n")
            out.write(f"Options (shared set): {members[0]['options']}\n")
            for r in members:
                ai = r.get("answer_index")
                ans = r["options"][ai] if isinstance(ai, int) and ai < len(r["options"]) else "<OOB>"
                out.write(
                    f"  line {r['_line']:>6} | {r['difficulty_level']:<11} | "
                    f"id {r['id']} | {r['answer']} -> {ans}\n"
                )
            out.write("\n")


# ---- main ---------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("data", nargs="?", default="data-processed-shuffled0.jsonl",
                    help="path to data-processed-shuffled0.jsonl (the ORIGINAL file)")
    ap.add_argument("--write", action="store_true",
                    help="also write duplicates.md and contradictions.md next to the data")
    args = ap.parse_args()

    if not os.path.exists(args.data):
        sys.exit(f"ERROR: cannot find {args.data!r}. Pass the path as the first argument.")

    rows = load(args.data)

    # Step 3: group
    groups = collections.defaultdict(list)
    for r in rows:
        groups[group_key(r)].append(r)

    # Step 4a: duplicates = groups of size >= 2
    dup_groups = [members for members in groups.values() if len(members) >= 2]
    dup_groups.sort(key=lambda m: min(r["_line"] for r in m))
    dup_rows = sum(len(g) for g in dup_groups)

    # Step 4b: contradictions = dup groups whose marked-correct text disagrees
    contra_groups = []
    for members in dup_groups:
        golds = {gold_text(r) for r in members}
        golds.discard(None)
        if len(golds) > 1:
            contra_groups.append(members)
    contra_groups.sort(key=lambda m: min(r["_line"] for r in m))
    contra_rows = sum(len(g) for g in contra_groups)

    size_dist = dict(sorted(collections.Counter(len(g) for g in dup_groups).items()))

    n = len(rows)
    print("=" * 68)
    print("VM14K — duplicates and self-contradictions")
    print("=" * 68)
    print(f"source file          : {args.data}")
    print(f"normaliser           : {_NORM_SOURCE}")
    print(f"rows                 : {n}")
    print("-" * 68)
    print(f"DUPLICATE groups     : {len(dup_groups):>6}   "
          f"rows {dup_rows:>6}   ({100 * dup_rows / n:.2f}% of rows)")
    print(f"  group-size dist    : {size_dist}")
    print("-" * 68)
    print(f"CONTRADICTION groups : {len(contra_groups):>6}   "
          f"rows {contra_rows:>6}   "
          f"(label-error floor >= {100 * len(contra_groups) / n:.3f}%)")
    print("  (subset of the duplicate groups above, where the marked-correct")
    print("   answer text disagrees across otherwise-identical copies)")
    print("=" * 68)

    if args.write:
        base = os.path.dirname(os.path.abspath(args.data))
        dpath = os.path.join(base, "duplicates.md")
        cpath = os.path.join(base, "contradictions.md")
        write_md(dpath, "VM14K: duplicate questions",
                 "Same normalised question AND same normalised option set (any order).",
                 dup_groups, args.data)
        write_md(cpath, "VM14K: self-contradictory answer keys",
                 "Same normalised question AND same normalised option set, "
                 "but a different option is marked correct.",
                 contra_groups, args.data)
        print(f"wrote {dpath}")
        print(f"wrote {cpath}")


if __name__ == "__main__":
    main()

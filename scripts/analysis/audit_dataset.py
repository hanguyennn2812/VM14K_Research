#!/usr/bin/env python3
"""
audit_dataset.py — one script, every distribution the supervisors asked for.

Covers action items 4-7 (option-set counts, A/B/C/D distribution, difficulty
distribution, bias flags) plus the invariant checks and the regression checks
that catch pipeline-ordering bugs.

Run on ANY version of the dataset. Emits a JSON report and a markdown table
block you can paste straight into the weekly report.

    python audit_dataset.py data/cleaned/clean_final.jsonl
    python audit_dataset.py data/baseline/clean.jsonl --json reports/audit_baseline.json
    python audit_dataset.py a.jsonl --compare b.jsonl     # side-by-side

NOTE ON REGEXES: LETTER_REF_RE and ALL_NONE_RE are HEURISTIC. Their counts are
TENTATIVE until a human reads the matches. Use --dump-matches to write them out
for manual audit. Do not publish these counts unaudited.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
import unicodedata
from pathlib import Path

# --------------------------------------------------------------------------
# Normalisers
# --------------------------------------------------------------------------

def remove_accents(text: str) -> str:
    text = unicodedata.normalize("NFD", str(text))
    text = re.sub("[\u0300-\u036f]", "", text)
    return text.replace("đ", "d").replace("Đ", "D")


def aggressive(text: str) -> str:
    """The authors' normalize_vietnamese. Strips punctuation AND diacritics."""
    text = remove_accents(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def conservative(text: str) -> str:
    """NFC + collapse whitespace + casefold. Punctuation PRESERVED."""
    text = unicodedata.normalize("NFC", str(text)).strip()
    return re.sub(r"\s+", " ", text).casefold()


# --------------------------------------------------------------------------
# Heuristic detectors — TENTATIVE, require manual audit
# --------------------------------------------------------------------------

# Options that NAME OTHER OPTIONS BY LETTER. These are the shuffle-breaking
# ones: if the option order changes, the letters point at different content.
LETTER_REF_RE = re.compile(
    r"(?:^|\b)(?:c[aâ]u\s*)?[ABCDabcd]\s*(?:,|v[àa]|and|&|\+)\s*(?:c[aâ]u\s*)?[ABCDabcd]\b"
    r"|\bc[aả]\s+[ABCDabcd]\s+v[àa]\s+[ABCDabcd]\b",
    re.IGNORECASE,
)

# "All of the above" / "none of the above". These do NOT name letters, so
# shuffling does NOT break them. Counted SEPARATELY and never folded into the
# shuffle-corruption number.
ALL_NONE_RE = re.compile(
    r"t[aấ]t c[aả].{0,15}(đ[uú]ng|sai)|kh[oô]ng c[oó].{0,15}(đ[uú]ng|n[aà]o)",
    re.IGNORECASE,
)


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{n}: {exc}") from exc
    return rows


def full_key(row: dict) -> tuple:
    return (
        aggressive(row["question"]),
        tuple(sorted(aggressive(o) for o in row["options"])),
    )


def gold_text(row: dict) -> str | None:
    i = row.get("answer_index")
    if not isinstance(i, int) or not 0 <= i < len(row["options"]):
        return None
    return aggressive(row["options"][i])


def audit(rows: list[dict], label: str) -> dict:
    n = len(rows)
    out: dict = {"label": label, "rows": n}

    # --- item 4: option-set count distribution -----------------------------
    out["option_count_dist"] = dict(
        sorted(collections.Counter(len(r["options"]) for r in rows).items())
    )

    # --- item 5: A/B/C/D distribution + positional bias --------------------
    letters = collections.Counter(r["answer"] for r in rows)
    out["answer_letter_dist"] = {
        k: {"n": v, "pct": round(100 * v / n, 2)} for k, v in sorted(letters.items())
    }
    four = [r for r in rows if len(r["options"]) == 4]
    if four:
        f = collections.Counter(r["answer"] for r in four)
        out["answer_letter_dist_4option_only"] = {
            k: {"n": v, "pct": round(100 * v / len(four), 2)} for k, v in sorted(f.items())
        }
    two = [r for r in rows if len(r["options"]) == 2]
    if two:
        a = sum(1 for r in two if r["answer_index"] == 0)
        out["two_option_first_position_rate"] = round(100 * a / len(two), 2)
    # expected accuracy of a no-skill "always first option" strategy
    out["always_A_accuracy"] = round(
        100 * sum(1 for r in rows if r["answer_index"] == 0) / n, 2
    )
    # expected accuracy of uniform random, respecting each item's option count
    out["random_expected_accuracy"] = round(
        100 * sum(1 / len(r["options"]) for r in rows) / n, 2
    )

    # --- item 6: difficulty distribution -----------------------------------
    diff = collections.Counter(r["difficulty_level"] for r in rows)
    out["difficulty_dist"] = {
        k: {"n": v, "pct": round(100 * v / n, 2)} for k, v in diff.most_common()
    }

    # --- topics ------------------------------------------------------------
    topics = collections.Counter(t for r in rows for t in r.get("medical_topic", []))
    out["distinct_topics"] = len(topics)
    out["topics_top15"] = dict(topics.most_common(15))

    # --- invariants --------------------------------------------------------
    out["invariants"] = {
        "ids_unique": len({r["id"] for r in rows}) == n,
        "answer_index_in_range": all(
            0 <= r["answer_index"] < len(r["options"]) for r in rows
        ),
        "answer_letter_matches_index": all(
            r["answer"] == chr(65 + r["answer_index"]) for r in rows
        ),
        "min_two_options": all(len(r["options"]) >= 2 for r in rows),
        "question_non_blank": all(str(r["question"]).strip() for r in rows),
        "text_is_nfc": all(
            unicodedata.is_normalized("NFC", r["question"])
            and all(unicodedata.is_normalized("NFC", str(o)) for o in r["options"])
            for r in rows
        ),
    }

    # --- duplicate / contradiction regression ------------------------------
    groups = collections.defaultdict(list)
    for r in rows:
        groups[full_key(r)].append(r)
    dup = {k: v for k, v in groups.items() if len(v) > 1}
    out["full_key_dup_groups"] = len(dup)
    out["full_key_dup_rows"] = sum(len(v) for v in dup.values())
    out["contradiction_groups"] = sum(
        1 for v in dup.values() if len({gold_text(x) for x in v} - {None}) > 1
    )

    stems = collections.defaultdict(list)
    for r in rows:
        stems[aggressive(r["question"])].append(r)
    rep = {k: v for k, v in stems.items() if len(v) > 1}
    out["repeated_stem_groups"] = len(rep)
    out["repeated_stem_rows"] = sum(len(v) for v in rep.values())

    # --- item 7: bias flags (TENTATIVE — regex heuristics) -----------------
    lref, allnone = [], []
    for r in rows:
        if any(LETTER_REF_RE.search(str(o)) for o in r["options"]):
            lref.append(r)
        if any(ALL_NONE_RE.search(str(o)) for o in r["options"]):
            allnone.append(r)
    out["TENTATIVE_letter_referential_rows"] = len(lref)
    out["TENTATIVE_all_none_of_above_rows"] = len(allnone)
    out["_tentative_note"] = (
        "letter_referential and all_none counts are REGEX HEURISTICS and are "
        "NOT publication-ready. Run with --dump-matches and hand-audit before "
        "quoting. Only letter-referential items are shuffle-breaking; "
        "all/none-of-the-above are NOT."
    )
    return out, lref, allnone


def markdown_block(a: dict) -> str:
    L = [f"### `{a['label']}` — {a['rows']:,} rows", ""]
    L.append("| option count | rows |")
    L.append("|---:|---:|")
    for k, v in a["option_count_dist"].items():
        L.append(f"| {k} | {v:,} |")
    L.append("")
    L.append("| answer | rows | % |")
    L.append("|---|---:|---:|")
    for k, v in a["answer_letter_dist"].items():
        L.append(f"| {k} | {v['n']:,} | {v['pct']} |")
    L.append("")
    L.append(f"- always-first-option accuracy: **{a['always_A_accuracy']}%**")
    L.append(f"- uniform-random expected accuracy: **{a['random_expected_accuracy']}%**")
    L.append("")
    L.append("| difficulty | rows | % |")
    L.append("|---|---:|---:|")
    for k, v in a["difficulty_dist"].items():
        L.append(f"| {k} | {v['n']:,} | {v['pct']} |")
    L.append("")
    L.append(f"- distinct topic strings: **{a['distinct_topics']}** (canonical target: 34)")
    L.append(f"- full-key duplicate groups: **{a['full_key_dup_groups']}**")
    L.append(f"- contradiction groups: **{a['contradiction_groups']}**")
    L.append(f"- repeated question stems: **{a['repeated_stem_groups']}** groups / "
             f"{a['repeated_stem_rows']} rows")
    L.append(f"- letter-referential (TENTATIVE): **{a['TENTATIVE_letter_referential_rows']}**")
    L.append(f"- all/none-of-above (TENTATIVE, not shuffle-breaking): "
             f"**{a['TENTATIVE_all_none_of_above_rows']}**")
    L.append("")
    failed = [k for k, v in a["invariants"].items() if not v]
    L.append(f"- invariants: {'ALL PASS' if not failed else 'FAILED: ' + ', '.join(failed)}")
    return "\n".join(L)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("data", type=Path)
    p.add_argument("--compare", type=Path, default=None)
    p.add_argument("--json", type=Path, default=None)
    p.add_argument("--markdown", type=Path, default=None)
    p.add_argument("--dump-matches", type=Path, default=None,
                   help="write regex matches to this dir for manual audit")
    args = p.parse_args()

    reports = []
    for path in filter(None, [args.data, args.compare]):
        rows = load_jsonl(path)
        rep, lref, allnone = audit(rows, path.name)
        reports.append(rep)
        print(markdown_block(rep))
        print()
        if args.dump_matches:
            args.dump_matches.mkdir(parents=True, exist_ok=True)
            for name, subset in [("letter_referential", lref), ("all_none", allnone)]:
                out = args.dump_matches / f"{path.stem}.{name}.jsonl"
                with out.open("w", encoding="utf-8") as fh:
                    for r in subset:
                        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
                print(f"wrote {len(subset)} rows -> {out}", file=sys.stderr)

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(reports, ensure_ascii=False, indent=2),
                             encoding="utf-8")
        print(f"wrote {args.json}", file=sys.stderr)
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text("\n\n".join(markdown_block(r) for r in reports),
                                 encoding="utf-8")
        print(f"wrote {args.markdown}", file=sys.stderr)


if __name__ == "__main__":
    main()

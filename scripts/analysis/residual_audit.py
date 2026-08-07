#!/usr/bin/env python3
"""
residual_audit.py — read-only top-to-bottom scan of clean_final.jsonl for
anything the 12 cleaning stages didn't catch.

Does NOT modify any file. Reads data/cleaned/clean_final.jsonl and prints/
writes findings only. Run with --markdown to emit reports/analysis/RESIDUAL_ISSUES.md.

Checks (see HANDOFF.md request):
  1. Option-text integrity (empty/whitespace/bare-label options, leftover
     extraction markers, embedded mid-text markers, byte-identical options
     within a row)
  2. Question-text integrity (blank, mid-sentence truncation heuristic,
     image/figure/table references)
  3. Answer validity (index range, letter/index match, answer pointing at a
     defective option)
  4. Duplicate/contradiction regression (full-key dup groups, same-question
     different-option-set groups and whether any disagree on the answer)
  5. Field hygiene (medical_topic type/emptiness, unexpected top-level keys,
     difficulty_level outside the known four)
  6. Encoding (NFC, control characters, doubled spaces)

    python scripts/analysis/residual_audit.py
    python scripts/analysis/residual_audit.py --markdown reports/analysis/RESIDUAL_ISSUES.md
"""
from __future__ import annotations

import collections
import json
import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = REPO_ROOT / "data" / "cleaned" / "clean_final.jsonl"
OUT_PATH = REPO_ROOT / "reports" / "analysis" / "RESIDUAL_ISSUES.md"

KNOWN_DIFFICULTIES = {"Easy", "Medium", "Challenging", "Hard"}
CANONICAL_KEYS = {
    "id", "difficulty_level", "medical_topic", "question", "options",
    "option_map", "answer", "answer_index", "contradiction_pending_review",
}


# --------------------------------------------------------------------------
# Normalisers (same rules as audit_dataset.py / clean_all.py)
# --------------------------------------------------------------------------

def remove_accents(text: str) -> str:
    text = unicodedata.normalize("NFD", str(text))
    text = re.sub("[̀-ͯ]", "", text)
    return text.replace("đ", "d").replace("Đ", "D")


def aggressive(text: str) -> str:
    text = remove_accents(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def conservative(text: str) -> str:
    text = unicodedata.normalize("NFC", str(text)).strip()
    return re.sub(r"\s+", " ", text).casefold()


# --------------------------------------------------------------------------
# Heuristic detectors (TENTATIVE — need human audit before publishing counts)
# --------------------------------------------------------------------------

BARE_LABEL_RE = re.compile(r"^[A-Ga-g][.\):]?$")
LEFTOVER_MARKER_RE = re.compile(r"\boption[A-G]\b|\bINVALID[_ ]OPTION\b", re.IGNORECASE)
# A letter-marker ("B." / "C)") appearing after some other content, not at the
# very start of the option -- the stage-10 "concatenated options" signature.
EMBEDDED_MARKER_RE = re.compile(
    r"[a-zà-ỹ0-9\.,\)][ \t]+[A-D][.\)][ \t]+\S", re.IGNORECASE
)

# Dangling conjunctions/prepositions a Vietnamese question shouldn't end on —
# a cheap truncation smell. "..."/"…" endings are excluded (documented as
# legitimate fill-in-the-blank format in CLEANING.md).
DANGLING_END_RE = re.compile(
    r"\b(và|hoặc|là|của|với|trong|cho|để|khi|mà|nhưng|thì|hay|do|bởi|nên|"
    r"sẽ|đã|đang|được|có|không|sau|trước|theo|từ|bằng|như|các|những|một)\s*$",
    re.IGNORECASE,
)

IMAGE_REF_RE = re.compile(
    r"\b(?<!điển )(hình|ảnh|sơ đồ|biểu đồ|bảng)\s+(dưới|trên|sau|bên)\b"
    r"|\btheo\s+(hình|ảnh|sơ đồ|biểu đồ|bảng)\b(?!\s*thức)"
    r"|\b(quan sát|nhìn(?:\s+vào)?|xem)\s+(hình|ảnh)\b"
    r"|\bđây là gì\b"
    r"|\bdựa vào\s+(hình|ảnh|bảng|sơ đồ|biểu đồ)\b",
    re.IGNORECASE,
)
# NOTE (hand-audited): even after excluding "điển hình" (typical) and "theo
# ... hình thức" (in the manner of) as unambiguous false positives, "hình ảnh
# sau/trên" is still genuinely ambiguous — it means both "the image below" AND
# "imaging [technique/appearance] follow[ing]/on [X-ray]" depending on
# grammar. Left flagged; disambiguation requires a human read, documented in
# RESIDUAL_ISSUES.md rather than forced into the regex.

CONTROL_CHAR_RE = re.compile(
    r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f​‌‍‎‏﻿]"
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
    opts = row.get("options") or []
    if not isinstance(i, int) or not 0 <= i < len(opts):
        return None
    return aggressive(opts[i])


def is_defective_option(text: str) -> str | None:
    """Returns a short reason string if the option text is structurally
    defective (empty/whitespace/bare-label), else None."""
    if text == "":
        return "empty"
    if not text.strip():
        return "whitespace_only"
    if BARE_LABEL_RE.match(text.strip()):
        return "bare_label"
    return None


class Finding:
    def __init__(self, key, title, tracked_as=None):
        self.key = key
        self.title = title
        self.tracked_as = tracked_as  # None -> new; else pointer into HANDOFF.md
        self.row_ids = set()  # count = distinct ROWS affected, not raw hits
        self.examples = []  # list of (id, detail)

    def add(self, row_id, detail=""):
        is_new_row = row_id not in self.row_ids
        self.row_ids.add(row_id)
        if is_new_row and len(self.examples) < 3:
            self.examples.append((row_id, detail))

    @property
    def count(self):
        return len(self.row_ids)


def main() -> None:
    rows = load_jsonl(DATA_PATH)
    n = len(rows)

    findings: dict[str, Finding] = {}

    def F(key, title, tracked_as=None) -> Finding:
        if key not in findings:
            findings[key] = Finding(key, title, tracked_as)
        return findings[key]

    # ---- 1. Option-text integrity -----------------------------------------
    f_opt_empty = F("opt_empty", "Options that are empty strings")
    f_opt_ws = F("opt_whitespace", "Options that are whitespace-only")
    f_opt_bare = F("opt_bare_label", 'Options that are a bare label only (e.g. "A.", "C)")')
    f_opt_leftover = F("opt_leftover_marker", 'Options containing leftover markers ("optionD", "INVALID_OPTION")')
    f_opt_embedded = F("opt_embedded_marker", "Options with an embedded mid-text option marker (concatenation signature)")
    f_opt_dup_within_row = F("opt_dup_within_row", "Options byte-identical within a row (conservative compare) — stage-03 defect, must be 0")

    for r in rows:
        opts = r.get("options") or []
        seen_conservative = []
        for i, opt in enumerate(opts):
            s = str(opt)
            reason = is_defective_option(s)
            if reason == "empty":
                f_opt_empty.add(r["id"], f"options[{i}]='{s}'")
            elif reason == "whitespace_only":
                f_opt_ws.add(r["id"], f"options[{i}]={s!r}")
            elif reason == "bare_label":
                f_opt_bare.add(r["id"], f"options[{i}]='{s}'")
            if LEFTOVER_MARKER_RE.search(s):
                f_opt_leftover.add(r["id"], f"options[{i}]='{s[:60]}'")
            if EMBEDDED_MARKER_RE.search(s):
                f_opt_embedded.add(r["id"], f"options[{i}]='{s[:80]}'")
            seen_conservative.append(conservative(s))
        if len(seen_conservative) != len(set(seen_conservative)):
            f_opt_dup_within_row.add(r["id"], f"n_options={len(opts)}")

    # ---- 2. Question-text integrity ---------------------------------------
    f_q_blank = F("q_blank", "Blank/whitespace-only questions — must be 0 (final_invariants guards this)")
    f_q_truncated = F("q_truncated_tentative", "TENTATIVE: question ends on a dangling word (possible mid-sentence truncation)")
    f_q_image_ref = F("q_image_ref", "Questions referencing an unseen image/figure/table")

    for r in rows:
        q = str(r.get("question", ""))
        if not q.strip():
            f_q_blank.add(r["id"])
            continue
        q_stripped = q.strip()
        # exclude legitimate "..."/"…" fill-in-the-blank endings (documented, not a bug)
        if not q_stripped.endswith(("...", "…")) and DANGLING_END_RE.search(q_stripped):
            f_q_truncated.add(r["id"], f'"...{q_stripped[-40:]}"')
        if IMAGE_REF_RE.search(q):
            f_q_image_ref.add(r["id"], f'"{q[:70]}"')

    # ---- 3. Answer validity -------------------------------------------------
    f_ans_range = F("ans_out_of_range", "answer_index out of range — must be 0 (final_invariants guards this)")
    f_ans_letter = F("ans_letter_mismatch", "answer letter does not match answer_index — must be 0 (final_invariants guards this)")
    f_ans_defective = F("ans_points_at_defective", "answer_index points at an empty/whitespace/bare-label option")

    for r in rows:
        opts = r.get("options") or []
        idx = r.get("answer_index")
        if not isinstance(idx, int) or not (0 <= idx < len(opts)):
            f_ans_range.add(r["id"], f"answer_index={idx}, n_options={len(opts)}")
            continue
        if r.get("answer") != chr(65 + idx):
            f_ans_letter.add(r["id"], f"answer={r.get('answer')!r}, answer_index={idx}")
        reason = is_defective_option(str(opts[idx]))
        if reason:
            f_ans_defective.add(r["id"], f"answer_index={idx} is {reason}")

    # ---- 4. Duplicate / contradiction regression ---------------------------
    f_full_dup = F("full_key_dup", "Full-key duplicate groups (question+options) — must be 0", tracked_as="BUG-1, fixed by stage12")

    groups_full = collections.defaultdict(list)
    for r in rows:
        groups_full[full_key(r)].append(r)
    full_dup_groups = {k: v for k, v in groups_full.items() if len(v) > 1}
    for k, v in full_dup_groups.items():
        f_full_dup.add(v[0]["id"], f"group of {len(v)}: {[x['id'] for x in v]}")

    f_stem_family = F(
        "stem_diff_options",
        "Same-question, different-option-set groups (the family the authors' Level-1 dedup structurally cannot catch)",
        tracked_as="repeated question stems, already tracked in HANDOFF.md §2 (225 groups/517 rows pre-BUG-1-fix)",
    )
    f_stem_contradiction = F(
        "stem_family_answer_disagreement",
        "Of those same-stem groups, how many disagree on the answer's own text (content-level contradiction beyond exact-key BUG-2)",
    )
    f_stem_spacing_near_dup = F(
        "stem_family_spacing_only",
        "Of those same-stem groups, how many 'disagree' only due to whitespace formatting (4mm vs 4 mm) — residual near-duplicates BUG-1's exact-key rule can't catch",
    )

    groups_stem = collections.defaultdict(list)
    for r in rows:
        groups_stem[aggressive(r["question"])].append(r)
    stem_groups = {k: v for k, v in groups_stem.items() if len(v) > 1}
    for k, v in stem_groups.items():
        option_sets = {tuple(sorted(aggressive(o) for o in r["options"])) for r in v}
        if len(option_sets) > 1:
            f_stem_family.add(v[0]["id"], f"group of {len(v)}, {len(option_sets)} distinct option-sets: {[x['id'] for x in v]}")
            golds = {gold_text(r) for r in v} - {None}
            if len(golds) > 1:
                golds_nospace = {g.replace(" ", "") for g in golds}
                if len(golds_nospace) > 1:
                    f_stem_contradiction.add(v[0]["id"], f"answers disagree: {golds}")
                else:
                    f_stem_spacing_near_dup.add(v[0]["id"], f"answers differ only by whitespace: {golds}")

    # ---- 5. Field hygiene ----------------------------------------------------
    f_topic_empty = F("topic_empty", "medical_topic is an empty list")
    f_topic_type = F("topic_type", "medical_topic is not a list, or contains non-string entries")
    f_extra_keys = F("unexpected_keys", "Rows with a key set different from the canonical schema")
    f_diff_unknown = F("difficulty_unknown", "difficulty_level outside the known four (Easy/Medium/Challenging/Hard)")

    for r in rows:
        topic = r.get("medical_topic")
        if not isinstance(topic, list):
            f_topic_type.add(r["id"], f"type={type(topic).__name__}")
        else:
            if len(topic) == 0:
                f_topic_empty.add(r["id"])
            if any(not isinstance(t, str) for t in topic):
                f_topic_type.add(r["id"], f"non-string entries: {[t for t in topic if not isinstance(t, str)]}")
        keys = set(r.keys())
        if keys != CANONICAL_KEYS:
            f_extra_keys.add(r["id"], f"extra={keys - CANONICAL_KEYS}, missing={CANONICAL_KEYS - keys}")
        if r.get("difficulty_level") not in KNOWN_DIFFICULTIES:
            f_diff_unknown.add(r["id"], f"difficulty_level={r.get('difficulty_level')!r}")

    # ---- 6. Encoding -----------------------------------------------------
    f_not_nfc = F("not_nfc", "Text not NFC-normalised — must be 0 (final_invariants guards this)")
    f_control_chars = F("control_chars", "Stray control/zero-width characters in question or options")
    f_double_space = F("double_space", 'Internal doubled spaces ("  ") in question or options', tracked_as="1 known instance (a4c0e0be...) documented in CLEANING.md as intentional, not a bug")

    for r in rows:
        texts = [str(r.get("question", ""))] + [str(o) for o in (r.get("options") or [])]
        if any(not unicodedata.is_normalized("NFC", t) for t in texts):
            f_not_nfc.add(r["id"])
        for t in texts:
            if CONTROL_CHAR_RE.search(t):
                f_control_chars.add(r["id"], f"chars={[hex(ord(c)) for c in CONTROL_CHAR_RE.findall(t)]}")
                break
        for t in texts:
            if "  " in t:
                f_double_space.add(r["id"], f'"...{t[max(0, t.find("  ")-15):t.find("  ")+17]}..."')
                break

    return rows, findings, full_dup_groups, stem_groups


def render_markdown(rows: list[dict], findings: dict[str, Finding]) -> str:
    n = len(rows)
    L = []
    L.append("# RESIDUAL_ISSUES.md — read-only re-audit of `clean_final.jsonl`")
    L.append("")
    L.append(f"Scanned **{n:,}** rows in `data/cleaned/clean_final.jsonl`. "
             "Nothing in this document was modified — this is a scan, not a fix. "
             "Counts marked TENTATIVE are regex heuristics and require a human read "
             "before being quoted, same convention as `HANDOFF.md` §0.")
    L.append("")
    L.append("| # | Finding | Count | Status | Example IDs |")
    L.append("|---|---|---:|---|---|")

    order = [
        "opt_empty", "opt_whitespace", "opt_bare_label", "opt_leftover_marker",
        "opt_embedded_marker", "opt_dup_within_row",
        "q_blank", "q_truncated_tentative", "q_image_ref",
        "ans_out_of_range", "ans_letter_mismatch", "ans_points_at_defective",
        "full_key_dup", "stem_diff_options", "stem_family_answer_disagreement", "stem_family_spacing_only",
        "topic_empty", "topic_type", "unexpected_keys", "difficulty_unknown",
        "not_nfc", "control_chars", "double_space",
    ]

    for i, key in enumerate(order, 1):
        f = findings[key]
        status = "already tracked: " + f.tracked_as if f.tracked_as else ("**NEW**" if f.count else "clean")
        examples = ", ".join(x[0] for x in f.examples) if f.examples else "—"
        L.append(f"| {i} | {f.title} | {f.count:,} | {status} | {examples} |")

    L.append("")
    L.append("---")
    L.append("")
    L.append("## Detail per finding")
    L.append("")
    for i, key in enumerate(order, 1):
        f = findings[key]
        L.append(f"### {i}. {f.title}")
        L.append("")
        L.append(f"**Count:** {f.count:,}")
        if f.tracked_as:
            L.append(f"**Status:** already tracked — {f.tracked_as}")
        else:
            L.append(f"**Status:** {'NEW finding this audit' if f.count else 'checked, clean (0)'}")
        if f.examples:
            L.append("")
            L.append("**Examples:**")
            for row_id, detail in f.examples:
                L.append(f"- `{row_id}` — {detail}")
        L.append("")

    return "\n".join(L)


if __name__ == "__main__":
    rows, findings, full_dup_groups, stem_groups = main()
    md = render_markdown(rows, findings)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(md, encoding="utf-8")
    print(f"wrote {OUT_PATH}", file=sys.stderr)
    total_new = sum(1 for f in findings.values() if f.count and not f.tracked_as)
    print(f"{total_new} finding categories have a nonzero, NOT-already-tracked count", file=sys.stderr)

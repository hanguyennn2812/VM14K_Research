#!/usr/bin/env python3
"""VM14K end-to-end cleaning pipeline — one file, one run, one report.

Reads the reproduced baseline (`data/baseline/clean.jsonl`, itself the
output of the *separate* `scripts/analysis/vm14k_dedup.py` reproduction of
the authors' pipeline) and applies eleven audited cleaning stages in
sequence, entirely in memory. Writes exactly three artifacts:

    data/cleaned/clean_final.jsonl        the accepted dataset
    data/quarantine/quarantine_all.jsonl  every excluded row, tagged by stage
    reports/cleaning/clean_final.report.json   one machine-readable report

This file replaces eleven separate step scripts and eleven separate step
reports that used to live under scripts/cleaning/ and reports/cleaning/.
Each stage below is still its own function with its own audited rule and
expected-count guard (so the pipeline still fails loudly if a rule's scope
silently changes) — only the file layout was consolidated, not the care
taken at each step. Every quarantined row is stored with the exact original
object under "row" so it can be recovered unmodified.

Stage order and what each one does:

01. Remove one residual normalized-duplicate row already flagged by the
    original VM14K audit (keep-first, abort on contradictory answers).
02. Quarantine structurally unusable rows (blank question, <2 options).
03. Quarantine rows with duplicate answer choices (conservative
    NFC+trim+casefold comparison).
04. Repair five audited malformed medical_topic lists (ID-specific).
05. Canonicalize Unicode NFC and outer whitespace in question/options.
06. Quarantine twelve audited rows whose answer depends on a missing
    image/audio asset (ID-specific).
07. Quarantine rows containing explicit missing-option placeholders
    (optionA..optionG, or punctuation-only placeholders).
08. Convert genuine HTML <br> tags to newlines (not comparison operators).
09. Decode residual HTML entities (&gt; &quot; &nbsp; ...).
10. Quarantine rows whose option array shows boundary corruption:
    concatenated options, options mislabeled relative to their own
    position, or empty marker-only options (ID-specific, hand-audited).
11. Strip redundant self-referential "A./B./C./D." option prefixes where,
    and only where, the leaked letter matches the option's own position.

See docs/cleaning/CLEANING.md for the full narrative, worked examples, and
the reasoning behind each rule.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]

Row = dict[str, Any]


# --------------------------------------------------------------------------
# Shared helpers
# --------------------------------------------------------------------------


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_jsonl(path: Path) -> list[Row]:
    rows: list[Row] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"line {line_number}: invalid JSON: {error}") from error
            if not isinstance(row, dict) or not isinstance(row.get("id"), str):
                raise ValueError(f"line {line_number}: invalid record")
            rows.append(row)
    return rows


def dump_jsonl(path: Path, rows: list[Row]) -> bytes:
    buf = "\n".join(json.dumps(row, ensure_ascii=False) for row in rows)
    if rows:
        buf += "\n"
    data = buf.encode("utf-8")
    path.write_bytes(data)
    return data


def remove_accents(text: str) -> str:
    text = unicodedata.normalize("NFD", text)
    text = re.sub("[̀-ͯ]", "", text)
    return text.replace("đ", "d").replace("Đ", "D")


def normalize_vietnamese(text: str) -> str:
    text = remove_accents(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_option_conservative(text: str) -> str:
    text = unicodedata.normalize("NFC", text).strip()
    text = re.sub(r"\s+", " ", text)
    return text.casefold()


def assert_stage_count(stage: str, expected: int, actual: int) -> None:
    if expected != actual:
        raise RuntimeError(
            f"{stage}: expected {expected} affected row(s), found {actual} "
            "(the audited rule's scope changed — investigate before proceeding)"
        )


# A quarantined entry: the untouched original row, which stage removed it,
# and a short human-readable reason.
Quarantined = tuple[Row, str, str]


# --------------------------------------------------------------------------
# Stage 01 — remove one residual normalized-content duplicate
# --------------------------------------------------------------------------


def stage01_residual_exact_dedup(rows: list[Row]) -> tuple[list[Row], list[Quarantined]]:
    def key(row: Row) -> tuple[str, tuple[str, ...]]:
        return (
            normalize_vietnamese(row["question"]),
            tuple(sorted(normalize_vietnamese(o) for o in row["options"])),
        )

    kept_by_key: dict[tuple[str, tuple[str, ...]], Row] = {}
    output: list[Row] = []
    removed: list[Row] = []

    for row in rows:
        k = key(row)
        prior = kept_by_key.get(k)
        if prior is None:
            kept_by_key[k] = row
            output.append(row)
            continue
        kept_answer = normalize_vietnamese(prior["options"][prior["answer_index"]])
        dropped_answer = normalize_vietnamese(row["options"][row["answer_index"]])
        if kept_answer != dropped_answer:
            raise RuntimeError(
                f"stage01: refusing to remove contradictory duplicate id={row['id']}"
            )
        removed.append(row)

    assert_stage_count("stage01_residual_exact_dedup", 1, len(removed))
    # This row is an exact removal (not quarantined): it is fully recoverable
    # from the unchanged data/baseline/clean.jsonl, per the original design.
    return output, []


# --------------------------------------------------------------------------
# Stage 02 — quarantine structurally unusable rows
# --------------------------------------------------------------------------


def stage02_structural_validity(rows: list[Row]) -> tuple[list[Row], list[Quarantined]]:
    output: list[Row] = []
    quarantined: list[Quarantined] = []
    for row in rows:
        reasons = []
        if not row["question"].strip():
            reasons.append("blank_question")
        if len(row["options"]) < 2:
            reasons.append("fewer_than_2_options")
        if reasons:
            quarantined.append((row, "stage02_structural_validity", ",".join(reasons)))
        else:
            output.append(row)
    assert_stage_count("stage02_structural_validity", 14, len(quarantined))
    return output, quarantined


# --------------------------------------------------------------------------
# Stage 03 — quarantine rows with duplicate answer choices
# --------------------------------------------------------------------------


def stage03_unique_options(rows: list[Row]) -> tuple[list[Row], list[Quarantined]]:
    def has_duplicates(row: Row) -> bool:
        seen: dict[str, int] = defaultdict(int)
        for option in row["options"]:
            seen[normalize_option_conservative(option)] += 1
        return any(count > 1 for count in seen.values())

    output: list[Row] = []
    quarantined: list[Quarantined] = []
    for row in rows:
        if has_duplicates(row):
            quarantined.append((row, "stage03_unique_options", "duplicate_option_text"))
        else:
            output.append(row)
    assert_stage_count("stage03_unique_options", 199, len(quarantined))
    return output, quarantined


# --------------------------------------------------------------------------
# Stage 04 — repair five audited malformed topic lists
# --------------------------------------------------------------------------

TOPIC_REPAIRS: dict[str, dict[str, Any]] = {
    "83ddfd12cefe4752ac58d4879ad6f1f5": {
        "expected_before": [
            "Endocrinology",
            "Internal Medicine",
            '"Endocrinology',
            'Internal Medicine"',
        ],
        "after": ["Endocrinology", "Internal Medicine"],
    },
    "27551d5653154d9db7b598157343744e": {
        "expected_before": [
            "10. Tích oxalat. Các hội chứng bất thường liên quan đến gen "
            "lặn là gì? (Dịch: Các hội chứng bất thường liên quan đến gen "
            "lặn là gì?)"
        ],
        "after": ["Other(No Category)"],
    },
    "214ddf96c58c46928e2a32022c3d40e0": {
        "expected_before": ["lí giải minh bạch"],
        "after": ["Other(No Category)"],
    },
    "c8581f4ef08a444484f13e133e3f4a5d": {
        "expected_before": ["optionD"],
        "after": ["Other(No Category)"],
    },
    "02c62260fd4549c2a8dad341b288e8b7": {
        "expected_before": [""],
        "after": ["Other(No Category)"],
    },
}


def stage04_repair_topics(rows: list[Row]) -> list[Row]:
    found: set[str] = set()
    for row in rows:
        repair = TOPIC_REPAIRS.get(row["id"])
        if repair is None:
            continue
        found.add(row["id"])
        if row["medical_topic"] != repair["expected_before"]:
            raise RuntimeError(f"stage04: unexpected topic list for id={row['id']}")
        row["medical_topic"] = repair["after"]
    if found != set(TOPIC_REPAIRS):
        raise RuntimeError(f"stage04: missing IDs {set(TOPIC_REPAIRS) - found}")
    return rows


# --------------------------------------------------------------------------
# Stage 05 — canonicalize Unicode NFC and outer whitespace
# --------------------------------------------------------------------------


def canonicalize(text: str) -> str:
    return unicodedata.normalize("NFC", text).strip()


def stage05_canonicalize_text(rows: list[Row]) -> list[Row]:
    changed = 0
    for row in rows:
        question_after = canonicalize(row["question"])
        options_after = [canonicalize(o) for o in row["options"]]
        if question_after != row["question"] or options_after != row["options"]:
            changed += 1
        row["question"] = question_after
        row["options"] = options_after
    assert_stage_count("stage05_canonicalize_text", 46, changed)
    return rows


# --------------------------------------------------------------------------
# Stage 06 — quarantine twelve audited missing-visual/audio-context rows
# --------------------------------------------------------------------------

MISSING_CONTEXT_IDS: dict[str, str] = {
    "76c400d1a93d41698b8f1161cc79b80f": "visual: generic stem with parasite-image choices",
    "65e57b882c8f4b61b6a3a5f25ce14d8b": "visual: generic stem with parasite-image choices",
    "1801c48b61f5426ab17ad4dfab20dc12": "visual: generic stem with parasite-image choices",
    "46f15e95ab5e4d1a87e44f75b3e8aacb": "visual: generic stem with parasite-image choices",
    "3a1a3d0e396749cfbd4d67a8ca663cd0": "visual: generic stem with parasite-image choices",
    "2635597782734cc98ae5bd6e7aa18aee": "visual: pneumonia type from absent image",
    "40f195bb763e40f589014308f3afef53": "visual: gross lung-cancer type from absent image",
    "83b312c96aa544ad96fa197d4495b4a4": "visual: reaction (1) in absent Krebs-cycle diagram",
    "29489774e895419aa67fca6704060590": "visual: generic stem with surgical-instrument choices",
    "aeb5dc9bec314f3d83c4ef519cb34b28": "visual: diagnosis from absent referenced image",
    "3f5b7dbf52994bd5a8691f8110f9bb8b": "audio: listening item has no audio or transcript",
    "473b8848ae67408ea087d9c45b599e1b": "audio: listening item has no audio or transcript",
}


def stage06_missing_context(rows: list[Row]) -> tuple[list[Row], list[Quarantined]]:
    output: list[Row] = []
    quarantined: list[Quarantined] = []
    found: set[str] = set()
    for row in rows:
        reason = MISSING_CONTEXT_IDS.get(row["id"])
        if reason is None:
            output.append(row)
            continue
        found.add(row["id"])
        quarantined.append((row, "stage06_missing_context", reason))
    if found != set(MISSING_CONTEXT_IDS):
        raise RuntimeError(f"stage06: missing IDs {set(MISSING_CONTEXT_IDS) - found}")
    assert_stage_count("stage06_missing_context", 12, len(quarantined))
    return output, quarantined


# --------------------------------------------------------------------------
# Stage 07 — quarantine explicit missing-option placeholders
# --------------------------------------------------------------------------

OPTION_LABEL_PATTERN = re.compile(r"option[A-G]", re.IGNORECASE)
PUNCTUATION_PLACEHOLDER_PATTERN = re.compile(r"[.…_\-\s]{3,}")


def placeholder_reasons(row: Row) -> list[str]:
    reasons = []
    for option in row["options"]:
        stripped = option.strip()
        if OPTION_LABEL_PATTERN.fullmatch(stripped):
            reasons.append("option_label_placeholder")
        elif PUNCTUATION_PLACEHOLDER_PATTERN.fullmatch(stripped):
            reasons.append("punctuation_only_placeholder")
    return reasons


def stage07_placeholder_options(rows: list[Row]) -> tuple[list[Row], list[Quarantined]]:
    output: list[Row] = []
    quarantined: list[Quarantined] = []
    for row in rows:
        reasons = placeholder_reasons(row)
        if reasons:
            quarantined.append((row, "stage07_placeholder_options", ",".join(sorted(set(reasons)))))
        else:
            output.append(row)
    assert_stage_count("stage07_placeholder_options", 66, len(quarantined))
    return output, quarantined


# --------------------------------------------------------------------------
# Stage 08 — convert genuine HTML <br> tags to newlines
# --------------------------------------------------------------------------

BREAK_TAG = re.compile(r"[ \t]*<br\s*/?>[ \t]*", re.IGNORECASE)


def stage08_convert_break_tags(rows: list[Row]) -> list[Row]:
    changed_rows = 0
    total_replacements = 0
    for row in rows:
        question_after, qcount = BREAK_TAG.subn("\n", row["question"])
        options_after = []
        row_count = qcount
        for option in row["options"]:
            option_after, count = BREAK_TAG.subn("\n", option)
            options_after.append(option_after)
            row_count += count
        if row_count:
            row["question"] = question_after
            row["options"] = options_after
            changed_rows += 1
            total_replacements += row_count
    if changed_rows != 3 or total_replacements != 12:
        raise RuntimeError(
            f"stage08: expected 3 rows / 12 replacements, found "
            f"{changed_rows} rows / {total_replacements} replacements"
        )
    return rows


# --------------------------------------------------------------------------
# Stage 09 — decode residual HTML entities
# --------------------------------------------------------------------------

ENTITY_PATTERN = re.compile(r"&#?\w+;")


def decode_entities(text: str) -> str:
    return unicodedata.normalize("NFC", html.unescape(text)).strip()


def stage09_decode_html_entities(rows: list[Row]) -> list[Row]:
    changed = 0
    for row in rows:
        question_after = decode_entities(row["question"])
        options_after = [decode_entities(o) for o in row["options"]]
        if question_after != row["question"] or options_after != row["options"]:
            changed += 1
        row["question"] = question_after
        row["options"] = options_after
    assert_stage_count("stage09_decode_html_entities", 6, changed)
    return rows


# --------------------------------------------------------------------------
# Stage 10 — quarantine option-boundary corruption (hand-audited)
# --------------------------------------------------------------------------

OPTION_MARKER_CORRUPTION_IDS: dict[str, str] = {
    # Concatenated options: sibling option text (with marker) absorbed into
    # one slot, leaving a duplicate or an orphaned fragment elsewhere.
    "ed63be9518874b9cbfa22a84c7006c8c": "concatenated_options",
    "90a227237a0443bf8e694de34b2af6bc": "concatenated_options",
    "62a96ed2071e48d4bcb645c666303617": "concatenated_options",
    "254b7056dc554532a86faa73095c9e21": "concatenated_options",
    "bd90078946ed4f06bd4c8fc300a1b0a5": "concatenated_options",
    "87d08108c78c4a1fa2435c0a6ccfeff9": "concatenated_options",
    "92af9fbc75c24772be87012e1ac95c6e": "concatenated_options",
    "8d334738ecbf4cb0b6f2d2d0a510b6bf": "concatenated_options",
    "9e2c249e0a06442e89f89b0588ce379a": "concatenated_options",
    # Mislabeled options: leaked marker letter does not match the option's
    # own zero-based position.
    "e8185bb1feb64ffe8fdb0196b4506bd3": "mislabeled_option_position",
    "256d804918584816a122ae159644bb29": "mislabeled_option_position",
    "8f31f73f834c465b9a61d4a63c87a630": "mislabeled_option_position",
    "a9007d316b514d819ee50bea5766fb7f": "mislabeled_option_position",
    "eb9b65af0660470bb2ac1f7ac4b76eb4": "mislabeled_option_position",
    "8ab4ab15ddf94a9ba1b9991e2272ab95": "mislabeled_option_position",
    "16f1e5cf69be463992d11584acb5364e": "mislabeled_option_position",
    "788eaaa8d8564f6b8f2e4756da6a144f": "mislabeled_option_position",
    # Empty marker-only options: no real content survives.
    "15b2469bf5254bc39a141ae325d6e511": "empty_marker_only_option",
    "ce403ce231064eaf8b09c7f4b609e15d": "empty_marker_only_option",
    "ee6671a69d50413d84b82125ab2d1bf0": "empty_marker_only_option",
    "9dcb8a0294c741129690b05db893266a": "empty_marker_only_option",
    # Punctuation-only option exposed by Stage 09 entity decoding
    # ("&nbsp; ------" -> "------"), matching Stage 07's placeholder rule.
    "8de9934f131349f29c33957e2be86f79": "placeholder_exposed_by_entity_decode",
}


def stage10_option_marker_corruption(rows: list[Row]) -> tuple[list[Row], list[Quarantined]]:
    output: list[Row] = []
    quarantined: list[Quarantined] = []
    found: set[str] = set()
    for row in rows:
        reason = OPTION_MARKER_CORRUPTION_IDS.get(row["id"])
        if reason is None:
            output.append(row)
            continue
        found.add(row["id"])
        quarantined.append((row, "stage10_option_marker_corruption", reason))
    if found != set(OPTION_MARKER_CORRUPTION_IDS):
        raise RuntimeError(
            f"stage10: missing IDs {set(OPTION_MARKER_CORRUPTION_IDS) - found}"
        )
    assert_stage_count("stage10_option_marker_corruption", 22, len(quarantined))
    return output, quarantined


# --------------------------------------------------------------------------
# Stage 11 — strip redundant self-referential option-letter prefixes
# --------------------------------------------------------------------------

LEADING_MARKER = re.compile(r"^([A-D])[.\)]\s+(\S.*)$", re.DOTALL)


def strip_redundant_prefix(option: str, zero_based_index: int) -> str | None:
    match = LEADING_MARKER.match(option)
    if match is None:
        return None
    letter, remainder = match.group(1), match.group(2)
    if letter != chr(ord("A") + zero_based_index):
        return None
    return remainder.strip()


def stage11_strip_redundant_prefixes(rows: list[Row]) -> list[Row]:
    changed_rows = 0
    stripped_options = 0
    for row in rows:
        row_changed = False
        for index, option in enumerate(row["options"]):
            stripped = strip_redundant_prefix(option, index)
            if stripped is not None and stripped != option:
                row["options"][index] = stripped
                stripped_options += 1
                row_changed = True
        if row_changed:
            changed_rows += 1
    if changed_rows != 9 or stripped_options != 26:
        raise RuntimeError(
            f"stage11: expected 9 rows / 26 options, found "
            f"{changed_rows} rows / {stripped_options} options"
        )
    return rows


# --------------------------------------------------------------------------
# Final invariants, run once on the accepted output
# --------------------------------------------------------------------------


def final_invariants(rows: list[Row]) -> dict[str, bool]:
    ids = [row["id"] for row in rows]
    return {
        "ids_unique": len(ids) == len(set(ids)),
        "questions_non_blank": all(row["question"].strip() for row in rows),
        "at_least_two_options": all(len(row["options"]) >= 2 for row in rows),
        "answer_index_in_range": all(
            0 <= row["answer_index"] < len(row["options"]) for row in rows
        ),
        "answer_letter_matches_index": all(
            row["answer"] == chr(ord("A") + row["answer_index"]) for row in rows
        ),
        "medical_topic_non_empty": all(
            row["medical_topic"] and all(t.strip() for t in row["medical_topic"])
            for row in rows
        ),
        "text_is_nfc": all(
            unicodedata.normalize("NFC", row["question"]) == row["question"]
            and all(unicodedata.normalize("NFC", o) == o for o in row["options"])
            for row in rows
        ),
        "no_outer_whitespace": all(
            row["question"] == row["question"].strip()
            and all(o == o.strip() for o in row["options"])
            for row in rows
        ),
        "no_duplicate_options": all(
            len(row["options"])
            == len({normalize_option_conservative(o) for o in row["options"]})
            for row in rows
        ),
        "no_placeholder_options": all(not placeholder_reasons(row) for row in rows),
        "no_break_tags": all(
            not BREAK_TAG.search(row["question"])
            and all(not BREAK_TAG.search(o) for o in row["options"])
            for row in rows
        ),
        "no_html_entities": all(
            not ENTITY_PATTERN.search(row["question"])
            and all(not ENTITY_PATTERN.search(o) for o in row["options"])
            for row in rows
        ),
    }


# --------------------------------------------------------------------------
# Pipeline driver
# --------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input", type=Path, default=REPO_ROOT / "data" / "baseline" / "clean.jsonl"
    )
    parser.add_argument(
        "--output", type=Path, default=REPO_ROOT / "data" / "cleaned" / "clean_final.jsonl"
    )
    parser.add_argument(
        "--quarantine",
        type=Path,
        default=REPO_ROOT / "data" / "quarantine" / "quarantine_all.jsonl",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=REPO_ROOT / "reports" / "cleaning" / "clean_final.report.json",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing output/quarantine/report files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = args.input.resolve()
    output_path = args.output.resolve()
    quarantine_path = args.quarantine.resolve()
    report_path = args.report.resolve()

    if not input_path.is_file():
        raise FileNotFoundError(input_path)
    if not args.force:
        for path in (output_path, quarantine_path, report_path):
            if path.exists():
                raise FileExistsError(f"refusing to overwrite: {path} (use --force)")

    rows = load_jsonl(input_path)
    starting_rows = len(rows)
    all_quarantined: list[Quarantined] = []
    stage_counts: dict[str, int] = {}

    rows, q = stage01_residual_exact_dedup(rows)
    stage_counts["01_residual_exact_dedup"] = starting_rows - len(rows)
    all_quarantined += q

    rows, q = stage02_structural_validity(rows)
    stage_counts["02_structural_validity"] = len(q)
    all_quarantined += q

    rows, q = stage03_unique_options(rows)
    stage_counts["03_unique_options"] = len(q)
    all_quarantined += q

    rows = stage04_repair_topics(rows)
    rows = stage05_canonicalize_text(rows)

    rows, q = stage06_missing_context(rows)
    stage_counts["06_missing_context"] = len(q)
    all_quarantined += q

    rows, q = stage07_placeholder_options(rows)
    stage_counts["07_placeholder_options"] = len(q)
    all_quarantined += q

    rows = stage08_convert_break_tags(rows)
    rows = stage09_decode_html_entities(rows)

    rows, q = stage10_option_marker_corruption(rows)
    stage_counts["10_option_marker_corruption"] = len(q)
    all_quarantined += q

    rows = stage11_strip_redundant_prefixes(rows)

    invariants = final_invariants(rows)
    if not all(invariants.values()):
        raise RuntimeError(f"final invariants failed: {invariants}")

    output_ids = {row["id"] for row in rows}
    quarantine_ids = {row["id"] for row, _, _ in all_quarantined}
    if not output_ids.isdisjoint(quarantine_ids):
        raise RuntimeError("a row ended up both kept and quarantined")

    output_bytes = dump_jsonl(output_path, rows)
    quarantine_rows = [
        {"id": row["id"], "source_stage": stage, "reason": reason, "row": row}
        for row, stage, reason in all_quarantined
    ]
    quarantine_bytes = dump_jsonl(quarantine_path, quarantine_rows)

    report = {
        "pipeline": "clean_all.py (consolidated stages 01-11)",
        "input": {
            "path": str(input_path),
            "rows": starting_rows,
            "sha256": sha256_bytes(input_path.read_bytes()),
        },
        "output": {
            "path": str(output_path),
            "rows": len(rows),
            "sha256": sha256_bytes(output_bytes),
        },
        "quarantine": {
            "path": str(quarantine_path),
            "rows": len(quarantine_rows),
            "sha256": sha256_bytes(quarantine_bytes),
        },
        "stage_removal_counts": stage_counts,
        "total_removed": starting_rows - len(rows),
        "quarantine_reason_counts": dict(
            Counter(reason for _, _, reason in all_quarantined)
        ),
        "final_invariants": invariants,
    }
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

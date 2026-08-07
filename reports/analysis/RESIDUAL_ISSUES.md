# RESIDUAL_ISSUES.md

Re-audit of `clean_final.jsonl` after the 12-stage pipeline, plus the fixes it triggered.
Scanner: [`scripts/analysis/residual_audit.py`](../../scripts/analysis/residual_audit.py).

## Fixed — stages 13 and 14 added, pipeline re-run

**10,640 → 10,628 rows.** Quarantine 313 → 316. All invariants pass.

### Stage 13 — quarantined 3 rows with destroyed option content

| ID | Defect |
|---|---|
| `0c80985c40434291a0a80b94a6e5dada` | options are bare letters `['A','C','D','E']`; the hepatitis-type answer text is gone and `answer_index` points into it |
| `75bf0cf82ff443cba4b4ed9bf7356432` | `options[3] == "INVALID_OPTION"` — stage 07 only fullmatches `option[A-G]`, so this literal slipped through |
| `6cc1b7f508274cccad8f39fb7e75d9c4` | `options[3] == "Không answer"`, a corrupted fragment; row also carried a stray U+200E |

New invariant `no_invalid_option_literal` guards the second class. Deliberately **not** a
general "no single-letter option" rule — legitimate rows have single-letter options (vitamin
names `["K","D","E","A"]`, thresholds defined in the question text), so the ID list is explicit,
same pattern as stages 06 and 10.

### Stage 14 — removed 9 whitespace-only duplicate rows

Stages 01/12 use the authors' normaliser, which collapses whitespace runs but doesn't remove
them, so `sỏi 4mm` and `sỏi 4 mm` stayed distinct keys. Re-running the dedup rule with internal
whitespace stripped found 9 groups, **zero with conflicting answers**, so keep-first is safe.
Guarded by new invariant `whitespace_free_dup_groups_zero`.

## Open — needs a doctor, not confirmed as a defect

**139 groups.** Same normalised question stem, **different option sets**, different answer text
marked correct.

This is not BUG-2. BUG-2's groups have *identical* option sets, so a differing answer is
unambiguously a contradiction. Here the options differ too, which means each group is either a
real inconsistent key or simply two different questions that normalise to the same stem — and
the stem is often generic enough that the latter is plausible. Example: 4 rows share a
gonorrhea-treatment vignette with 4 different regimens marked correct; that could be 4
conflicting keys, or 4 distinct vignettes each with its own valid answer.

**Text alone cannot distinguish these.** No action until someone reads them. If confirmed, reuse
the BUG-2 machinery (ID list → `contradiction_pending_review` → Phase 4 Excel).

## Clean

Empty/whitespace options · duplicate options within a row · blank questions · `answer_index`
range · answer letter vs index · full-key duplicate groups · whitespace-free duplicate groups ·
`INVALID_OPTION` literals · control/zero-width characters · `medical_topic` type and emptiness ·
top-level key set · `difficulty_level` values · NFC.

## False positives — do not spend audit time here

- **328 "truncated question" candidates** (end on `là`, `do`, `trong`…): 15/15 sampled are
  normal fill-in-the-blank stems the options complete. Real truncation isn't regex-detectable.
- **10 "image reference" candidates**: all answerable from text. `hình ảnh` also means *imaging*
  (the modality), and the ones saying "hình ảnh sau" have full text descriptions as options —
  e.g. `09ea286b…` describes the histology in the question itself. Nothing to quarantine.
- **5 "embedded option marker" candidates**: vitamin names, species abbreviations
  (`A. duodenale`), parenthetical group labels. 2 are already in the 248-row letter-referential
  set.
- **4 remaining "bare label option" candidates**: vitamin-name options, a question defining
  A/B/C as its own thresholds, and a grammar exercise. Match exceptions `CLEANING.md` already
  documents.

## Known blind spot

`"Không answer"` was found by chance, not by any of the six systematic checks — it isn't empty,
isn't a bare label, and contains no marker. Garbled extraction fragments of that shape are
undetectable by these regexes. Read the 0-counts above as "no *detectable* instances", not
"none".

# Remaining review backlog

The following findings remain in `data/cleaned/clean_final.jsonl`. They
are not auto-cleaned because a simple rule risks deleting valid questions or
changing medical meaning.

> Resolved: residual HTML entities and option-boundary corruption
> (concatenated, mislabeled, or empty-marker options). See
> `docs/cleaning/CLEANING.md` (stages 09-11) for rules and worked examples.

## 1. Repeated normalized question stems

- 227 normalized-question groups.
- 521 rows involved.
- A naive keep-one policy would remove 294 rows.

Many are generic stems such as `Chọn câu đúng`, or intentionally reuse a stem
with different option sets. Question text alone is therefore not a valid dedup
key. Review should compare the full semantic proposition and all options.

## 2. Aggressive-normalizer option collisions

- 42 rows.

These rows have distinct options under the conservative Step 03 rule but collide
under `dedup_utils.normalize_vietnamese`, which removes punctuation and
diacritics. Examples include:

- `<5 tuổi` versus `>5 tuổi`.
- Positive versus negative notation such as `(+)` and `(-)`.
- Mathematical operators and formula punctuation.

They must not be deduplicated using the aggressive normalizer. A domain-aware
review can identify genuine typos separately.

## 3. Very short questions

- 12 questions have seven or fewer characters.

The group mixes valid abbreviations (`TLC là`, `FRC là`, `IC=?`) with suspicious
or context-poor strings such as `xxcfd`, `đen`, and `cạnh?`. Length alone is not
enough to delete a row. The suspicious subset should be manually adjudicated.

## 4. Potential answer leakage

- 39 rows have normalized correct-answer text of at least ten characters
  contained in the question.

Some are genuine leakage or answer-only conversions; others are valid fill-in,
case descriptions, or proposition-evaluation formats. Review should decide the
intended task format before removal or rewriting.

## 5. Internal line breaks

- 84 questions contain internal newlines after Step 08.
- 30 rows contain at least one option with an internal newline.

Many newlines encode numbered statements and should be preserved. Some reflect
PDF/OCR line wrapping. A future formatter should distinguish structural breaks
from soft wraps rather than flattening them globally.

## 6. Topic taxonomy consolidation

The dataset still contains rare and overlapping labels such as:

- `Infectious Diseases` and `Infection Diseases`.
- `Periodontology` and `Periodontics`.
- `Cell Biology` and `Cellular Biology`.
- `Preventive Healthcare` and `Preventive Medicine`.

Consolidation requires an agreed canonical taxonomy and mapping policy. Step 04
only repaired indisputably malformed values.

## 7. Medical and answer-key correctness

Structural validation cannot establish that a marked answer is medically
correct, current, or unambiguous. This requires:

- Source-backed medical review.
- Special attention to questions involving outdated guidelines or thresholds.
- Review of near-duplicate questions that state different answer keys.
- A documented adjudication process and evidence source.

## Recommended next action

Create a manual-review queue rather than another automatic filter. Suggested
priority:

1. Suspicious very short/gibberish stems.
2. Potential answer leakage.
3. Near-duplicate or semantically overlapping questions.
4. Medical answer-key verification.
5. Canonical topic taxonomy mapping.

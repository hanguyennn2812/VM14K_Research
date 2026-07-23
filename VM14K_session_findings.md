Repo state: `Venera-AI/VM14K-Megarepo` @ `2c15604` (HEAD at time of clone).
First commit: `611a5d3 "Initial commit (fresh start)"`.
Data file: `data-processed-shuffled0.jsonl`, 12,488 rows.
Authors' normalizer: `Deduplication/dedup_utils.normalize_vietnamese`.

---

## 1. Figure 5 was plotted from the 12,488-row release, not from 14,000

**Status: VERIFIED.**

The paper says 14,000 throughout, but its own difficulty-distribution figure (Fig. 5) reports
Medium 56.80% / Easy 32.93% / Challenging 9.55% / Hard 0.72%. The released 12,488-row file gives:

| level | count | % of 12,488 | Fig. 5 |
|---|---|---|---|
| Medium | 7,093 | 56.80 | 56.80 |
| Easy | 4,112 | 32.93 | 32.93 |
| Challenging | 1,193 | 9.55 | 9.55 |
| Hard | 90 | 0.72 | 0.72 |

All four match to two decimals. The paper's only distributional figure describes the 12,488 file.

---

## 2. The published dedup code, run on the released data

| stage | rows | redundant copies | contradiction groups | contra rows |
|---|---|---|---|---|
| **BEFORE (released)** | 12,488 | **1,325** | **67** | 152 |
| after Level 1 (exact) | 11,164 | 1 | **0** | 0 |
| after Level 2 (near-dup) | 10,956 | 1 | 0 | 0 |
| after Level 3 (off-topic) | 10,956 | 1 | 0 | 0 |

**Level 1 alone** — plain exact match after normalization — removes 1,324/1,325 redundant copies and
eliminates all 67 contradictions. The clustering/Levenshtein machinery is not needed. The released
artifact is therefore not the output of the published pipeline.

**Caveats to state in any writeup:**
- Their code expects CSV columns `optionA..optionG`; the release is JSONL with an `options` array.
  A transpose is required — *the published code cannot read the published data as-is.*
- Their code raises `ValueError: np.nan is an invalid document` on the release (see item 3).

---

## 3. The dedup code misses very short questions (min_df=5)

`TfidfVectorizer(min_df=5, max_df=0.8)`:

- **Blind spot:** 11 rows have questions that are zero-vectors under `min_df=5` (every token below the
  document-frequency floor). They can never be nominated as duplicate candidates. **The one duplicate
  group that survives item 2's dedup is exactly such a case** — "U brenner" (Brenner tumour),
  lines 3857 & 3883: identical question, identical options, identical answer, both zero-vectors.

This confirms (with a named example) the earlier `min_df=5` mechanism. Very short questions are
structurally invisible to this dedup.

---

## 4. Repo provenance (three strata)

(From `git log` on the clone.)

| stratum | dates | contents | relation to paper |
|---|---|---|---|
| pipeline code | 22 May – 3 Jun 2025 | `DataCleaning/`, `Deduplication/`, `Evaluation/`, `Inference/` | the paper's code; unmodified since |
| docs suite | 4 Jul 2025 | `docs/*.md` | authored by `cursoragent`, branch `cursor/write-documentation-from-content-0f99`, ~3 weeks post-arXiv; auto-generated |
| Eval-vLLM | Nov 2025 | `Eval-vLLM/` incl. `Data/VM14K.jsonl` | additive; different contributor; ~5 months post-arXiv; not the harness behind Tables 2–3 |
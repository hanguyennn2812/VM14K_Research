# VM14K Revisited: An Audit of a Vietnamese Medical QA Benchmark

*Working draft v2, 2026-10-03. Revised after Codex's fact-check and reviewer pass (`CODEX_REVIEW_3.md`).
Placeholders are written `[TBD: …]`. Every number in this draft has a row in the claims ledger (Appendix A) that
names the file or command producing it. Change a number there first, then here.
Realistic venue as framed now: a workshop. Findings becomes realistic once the clinician review, the rescoring
and the flagging baselines (§9) are done.*

---

## Abstract

VM14K was introduced as the first Vietnamese medical multiple-choice benchmark (arXiv 2506.01305). We audit its
public release and code.

(i) The public snapshot has 12,488 rows rather than the 14,000 reported. It is inconsistent with the output of the
published deduplication method: our adapted implementation of that method removes 1,324 of the 1,325 redundant
copies, and under the authors' normalization it collapses all 67 groups of duplicates that carry conflicting keys,
without deciding which key is correct.

(ii) Difficulty labels are inconsistent across normalized duplicate groups (19.8% of groups). Mean accuracy across
seven LLM configurations is 60.4%, 58.5% and 59.1% on Easy, Medium and Challenging test items, so the labels show
weak evidence of discrimination for these models.

(iii) The paper describes the key as "the correct answer according to GPT-4o", and the release has no item-level
verification provenance. On 238 of the 1,658 evaluated test questions (14.4%), DeepSeek-v4.1-flash and Gemma-4-31B
select the same non-key option.

We specify a clinician review protocol before annotation. It has a random stratum for estimating prevalence and
model-guided strata for finding errors efficiently [TBD: results]. We provide a structurally cleaned split, a map
from every removed row to its removal reason, and evaluations of seven models. Clinical validation of the keys is
pending.

---

## 1 Introduction

- Local-language benchmarks provide evidence about medical QA performance outside English, and, as audits of
  English benchmarks show (§2), their validity needs independent assessment.
- The VM14K paper reports 34 specialties, four difficulty levels, and evaluations of 17 models (L21).
- **Contributions.**
  1. An audit of the public release that uses the authors' normalizer and an explicitly adapted implementation of
     their deduplication algorithm (§3–4).
  2. A structurally cleaned split. Quarantined records are preserved, every removed raw row is mapped to a removal
     reason, and every stage checks its audited row count (§5).
  3. A re-evaluation of seven models with explicit baselines (§6).
  4. A prospectively specified clinician review that combines model-guided flags with a simple random sample, so
     that the prevalence of key errors can be estimated rather than only illustrated (§7).

## 2 Related work

- **Label errors in evaluation sets.** Northcutt, Athalye & Mueller (2021) find pervasive label errors in the
  test sets they examine. *Are We Done with MMLU?* (Gema et al., NAACL 2025) estimates that 6.49% of MMLU questions
  contain errors, and 57% of the Virology questions it analysed. Platinum benchmarks (Vendrow et al., 2025) revise
  examples from fifteen benchmarks to minimize label errors and ambiguity. Nahum et al. use LLM ensembles to flag
  likely label errors for expert review [cite the EMNLP 2025 version]. We combine model-guided review with a simple
  random sample for prevalence estimation.
- **What medical MCQ benchmarks measure.** Construct validity of MCQ medical QA [Kim & Yoon, BioNLP 2025, verify];
  expert-written explanations (MedExpQA, Alonso et al., 2024).
- **Non-English medical QA.** HEAD-QA (Spanish, ACL 2019), CMB (Chinese, 2023), and IgakuQA (Japanese; Kasai et
  al., 2023), where models sometimes select choices prohibited in Japanese practice. WorldMedQA-V adds multilingual
  and multimodal evaluation with native and translated versions. AfriMed-QA is an English-language benchmark grounded
  in African clinical contexts. VietMed-MCQ (2026) is specific to Vietnamese **Traditional** Medicine.
- **Option order and multiple-choice robustness.** LLMs are not robust multiple-choice selectors (Zheng et al.,
  ICLR 2024). We separate model position bias from a different problem: permutations that change what an item
  means (§4.2).
- **Deduplication and split hygiene.** Lee et al. (ACL 2022). Our split groups by exact normalized stem only, which
  is not semantic leakage prevention.
- **Difficulty.** Easy2Hard-Bench derives numerical difficulty from human and model performance (IRT/Glicko-2).
  We only test whether VM14K's assigned labels are consistent and whether they separate accuracy.
- **Documentation.** Data Statements (Bender & Friedman, TACL 2018) for the provenance of the cleaned release.

[TBD: verify every reference (authors, venue, year, numbers) against the source before submission.]

## 3 What VM14K reports and what its public snapshot contains

| Paper reports | Audited public snapshot | Ledger |
|---|---|---|
| 14,000 questions | 12,488 rows; three files with the same IDs in the same order, differing only in option order | L1, L2 |
| Sample public 4k / full public 10k / private 2k | The snapshot exposes neither the sample/full partition nor identifiers for a private set | L2 |
| Questions sampled from a deduplicated pool | 1,125 normalized duplicate groups covering 2,450 rows (19.62%) | L3 |
| Expert involvement in verification | Key described as "according to GPT-4o"; no item-level record of source, LLM, or expert answers | L4 |
| Difficulty distribution (Fig. 5) | Fig. 5 percentages match the 12,488-row file to two decimals | L5 |

## 4 Audit findings

### 4.1 Duplicates and conflicting keys
- Grouping by normalized question plus normalized option multiset, with the authors' `normalize_vietnamese`, gives
  **1,125 groups covering 2,450 rows (19.62%)**. In **67 groups (152 rows)**, copies carry different keys.
  "Duplicate" here means equality after normalization, which strips diacritics and punctuation. It does not
  guarantee identical medical meaning. [TBD: manually validate the 67 contradiction groups; an earlier sample of 25
  found 9 genuine key conflicts and several other defects, L18.]
- Our adapted implementation of the three-level published dedup returns **10,956 rows (−1,532)**. Level 1 applies
  normalized equality checks to TF-IDF-nominated candidate pairs. It already removes **1,324 of the 1,325 redundant
  copies** and collapses all 67 conflicting-key groups. The released artifact is therefore inconsistent with the
  output of this pipeline.
- Two properties of the method matter for any reuse. Questions with no retained TF-IDF features (`min_df=5`) are
  never nominated; the one surviving redundant pair is such a case. And the dedup key ignores the answer, so when a
  conflicting group is collapsed, the copy that survives is whichever comes first in the file.

### 4.2 Question formats, extraction defects, and answer-position imbalance
- **1,240 two-option items** (~10% of the raw rows), many presented as true/false, are scored in the same aggregate
  as four-option items.
- The raw release has **15 one-option rows**. Cleaning quarantines further structural and extraction defects:
  placeholder options, merged options, and items that refer to missing images (§5, L11).
- **At least 80 released rows** contain options that refer to other options by position (e.g. "Cả A và B"), and
  these can change meaning when options are shuffled. The paper's ensemble shuffles options; its effect on the
  ensemble scores has not been quantified (§9, experiment 3).
- **Position of the key.** In the raw release the key is option A in **31.35%** of rows, against **27.62%**
  expected under uniform placement. That is 28.7% against 25% for four-option rows and 53.8% against 50% for
  two-option rows. After cleaning it is 30.29% against 27.48%.

### 4.3 Difficulty labels
- **Consistency.** **223 of 1,125** normalized duplicate groups (19.82%) carry more than one difficulty label.
  Agreement over the 1,567 within-group pairs is **82.58%**, and generalized Fleiss κ (groups weighted equally) is
  **0.647**. The release has no labeller provenance, so we cannot attribute this to one LLM contradicting itself.
- **Discrimination.** On the 1,658 evaluated test items, mean accuracy across seven LLM configurations is
  **60.4 / 58.5 / 59.1%** for Easy / Medium / Challenging. Easy minus Challenging is **1.30 pp, 95% CI
  [−4.06, 6.62]**. With model fixed effects and question-clustered SEs, the Easy-vs-Challenging odds ratio is
  **1.058 [0.834, 1.341]**, and Spearman ρ between the ordinal label and per-question accuracy is **−0.027**. We do
  not find clear evidence that the labels separate accuracy for these seven configurations. The CI does not rule out
  a modest effect, and no equivalence test was run. Hard has 13 test items and is not interpreted. Difficulty for
  LLMs is not difficulty for clinicians.

### 4.4 Answer-key provenance
- Table 1 of the paper defines `correctOption` as "the correct answer according to GPT-4o". The paper also
  describes verification against three sources (source answer, foundation LLMs, experts), starting with easy
  questions on which the source and the models disagree. The release records neither which source each key came
  from nor which items an expert checked.

### 4.5 Evaluation reporting
- The paper's "ensemble" is one model run three times with independently shuffled options and a majority vote.
- The reference column of Table 3 is mixed. Across all 17 rows it equals Table 2 pass@3 for 12 models and pass@1 for
  4 (o3-mini, Qwen3-32B, Qwen3-30B-A3B, HuatuoGPT-o1-8B). For Gemini 2.0 Flash it matches neither (77.29 against a
  pass@3 of 77.92). The Δ printed for Llama 4 Maverick (−1.33) does not equal ensemble minus reference
  (72.46 − 73.13 = −0.67). The parenthesized Δ values are therefore not comparable across rows.

## 5 A structurally cleaned split

- Our adapted dedup implementation returns 10,956 rows, matching the stored reproduction report. Fourteen stages
  then give **10,628 rows**. **316 rows are quarantined** with their stage and reason, and the other removed raw
  rows are mapped to their reasons in `reports/eval/raw/fates.json`. Each stage checks its audited affected-row
  count and aborts if the count differs (L22).
- Two issues in our own pipeline are documented (L23). Text repairs created new duplicates, which a later dedup stage now
  removes. Collapsing conflicting groups left survivors whose key was never checked; these 62 rows are flagged
  `contradiction_pending_review` and kept out of the test split, but their keys are still unverified.
- Frozen split, grouped by normalized stem so that identical normalized stems never cross splits; we checked that
  no such group spans two splits. Usable rows: train / val / test = 7,313 / 1,595 / 1,658. The split manifest lists
  1,662 test IDs; four were later removed as duplicates by cleaning stages 12/14.
- "Cleaned" means structurally cleaned only. It does not mean the keys are medically validated.

## 6 Re-evaluation

- **Protocol.** The paper's prompt (Fig. 6), temperature-zero decoding, thinking disabled where the model supports
  a switch (model-specific settings are recorded in the run metadata), pass@1 on the 1,658 test items. Baselines:
  always-A 29.8%, uniform random 27.6%.
- **Results** (pass@1 on 1,658 items, Wilson 95% CI; L12):

  | Model | Correct | pass@1 | 95% CI |
  |---|---:|---:|---|
  | Gemma-4-31B | 1,188 | 71.7 | [69.4, 73.8] |
  | DeepSeek-v4.1-flash | 1,183 | 71.4 | [69.1, 73.5] |
  | Qwen3.5-9B | 1,044 | 63.0 | [60.6, 65.3] |
  | Gemma-4-12B | 993 | 59.9 | [57.5, 62.2] |
  | Qwen3-8B | 904 | 54.5 | [52.1, 56.9] |
  | MedGemma-4B | 778 | 46.9 | [44.5, 49.3] |
  | Llama-3.1-8B | 775 | 46.7 | [44.4, 49.1] |

  The paper reports 48.73 for Llama-3.1-8B. Different questions
  and configurations mean this is not a paired replication. [TBD: add Gemma3-12B (paper 58.05) and Phi-4 (paper
  51.15).]
- **Raw versus clean.** We combine scores on the removed rows with a test-based estimate for the retained rows.
  The estimated raw-minus-clean difference is −0.1 pp for Llama-3.1-8B and +0.2 pp for Qwen3.5-9B, and their order
  is unchanged. On the 70 removed rows from conflicting-key groups, the two models score 32.9% and 28.6%, against a
  uniform-random baseline of 25.4% for that subset. When copies carry different keys, no single answer can be right
  for all of them. [TBD: CI of the raw−clean difference.]
- **Per specialty:** exploratory only, pending comparisons that account for dependence and correct for
  multiplicity.

## 7 Clinician review of the answer key

- **Model flags.** On 238 / 1,658 evaluated test questions (14.4%), DeepSeek-v4.1-flash and Gemma-4-31B select the
  same non-key option. Nemotron-3-Ultra answered 210 of these and matches them on 140. All seven fully run models
  miss the key on 125 questions.
- **Model explanations.** Nemotron-3-Ultra was asked to explain in Vietnamese with thinking on (320 questions: the
  268 flagged plus 52 random-sample questions). On 90 of the 140 triple-agreement items it keeps the consensus
  answer. It abstains on four items, citing missing imagery or context, or the absence of a correct option. These
  are the model's own reasons, not confirmed defects.
- **Protocol** (specified before annotation in `reports/eval/review_sample/HUONG_DAN.md`; [TBD: freeze version and
  sample size, e.g. by a dated commit, before review starts]). Current pilot design:
  - 60 random items, plus disjoint priority strata (3 / 85 / 15 / 15), for 178 items in total.
  - 36 items double-reviewed.
  - A blind round 1 (question and options only), then a reveal round 2.
  - Endpoints: E1 (confirmed key error, with s/n…(s+u)/n sensitivity bounds), E2 (defect that affects
    answerability), E3 (union), plus an adjudication procedure.
  - Analysis code: `scripts/eval/analyze_review.py`.
- **Results:** [TBD]. Candidate example, pending clinician review and a demographic reference: an item on
  replacement-level fertility whose key is "GRR = 1", where standard demographic definitions use NRR = 1.

## 8 Discussion and limitations

- In the raw-versus-clean comparison, the two models assessed keep their order. For the seven configurations
  tested, difficulty labels show weak discrimination.
- Erroneous keys may distort measured accuracy, and not necessarily downward, since a model can match a wrong key.
  We will quantify the effect by rescoring fixed predictions after adjudication (§9).
- Clinician-review prevalence estimates concern only the 1,658 evaluated test questions. Structural audit rates use
  the raw or clean population stated alongside each one.
- Model flags may reflect correlated training data or shared errors; their agreement is not independent clinical
  validation.
- Reasoning traces are the models' self-reports and are used only as reviewing aids.

## 9 Analyses that would most strengthen the paper (planned)

1. **Rescore fixed predictions after key adjudication.** Paired score differences, CIs, rank uncertainty, and which
   error types drive the change.
2. **Flagging baselines** measured by yield per reviewer-hour against the random stratum:
   - a single model disagreeing with the key;
   - the strong pair agreeing on a non-key option (current);
   - the 7-model vote;
   - structural heuristics.
3. **Shuffle experiment on position-referential items:** original order, naive shuffle, and a shuffle that
   preserves the references. This is a method-level result that transfers to other benchmarks.
4. **Decomposition on the same predictions:** raw → dedup → format filtering → text repairs → adjudicated keys.
5. **Detector validation:** precision of normalized-equality "duplicates", checked on a designed sample.

---

## Appendix A — Claims ledger

Status: **R** = re-run in this session (2026-10-02/03) and confirmed independently by Codex where noted;
**F** = read from a repo report and not re-run; **P** = from the paper (arXiv 2506.01305 HTML v1); **T** = pending.

| # | Claim | Value | Evidence | Status |
|---|---|---|---|---|
| L1 | Raw rows | 12,488 | `scripts/analysis/vm14k_dupes_and_contradictions.py` | R (Codex ✓) |
| L2 | Three raw files: same IDs and order, options shuffled; no sample/full/private partition exposed | — | `docs/research/VM14K_audit_notes.pdf` §1.1; Codex re-checked the three JSONL files | R |
| L3 | Normalized duplicate groups / rows | 1,125 / 2,450 (19.62%) | `vm14k_dupes_and_contradictions.py` | R (Codex ✓) |
| L3b | Conflicting-key groups / rows | 67 / 152 | same | R (Codex ✓) |
| L3c | Adapted dedup | −1,532 → 10,956; Level 1 −1,324/1,325 (→ 11,164); 67 → 0; 1 residual | `scripts/analysis/vm14k_dedup.py --out <tmp> --report <tmp>` | R (Codex ✓) |
| L4 | Key "according to GPT-4o"; verification starts with easy source/LLM disagreements | — | Paper Table 1, §3.2 | P (Codex ✓) |
| L5 | Fig. 5 percentages = raw label shares | 56.80/32.93/9.55/0.72 (7,093/4,112/1,193/90) | `scripts/analysis/difficulty_labels.py`; Fig. 5 values in `VM14K_session_findings.md` | R (Codex ✓) |
| L6 | Two-option rows | raw 1,240; clean 1,025; test 173 | inline count | R (Codex ✓) |
| L6b | One-option rows (raw) | 15 | inline count of `data/raw/data-processed-shuffled0.jsonl` | R |
| L7 | Key = A | raw 3,915/12,488 = 31.35% vs 27.62%; 4-opt 28.7% vs 25%; 2-opt 53.8%; clean 30.29% vs 27.48%; test 29.79% vs 27.64% | inline count | R (Codex ✓) |
| L7b | `TONG_QUAN_VM14K_CHO_THAY.md` §1.2b, uncommitted in the main checkout, gives "28.7% → 31.02% → 30.33%" | mixes the 4-option rate with all-row rates; current clean = 30.29% | this ledger, L7 | fix in that file |
| L8 | Position-referential options | ≥80 rows | `docs/research/VM14K_manual_verify.pdf` §6 (no ID list) | F — [TBD: regenerate with a command] |
| L9 | Difficulty consistency | 223/1,125 = 19.82%; 1,294/1,567 = 82.58%; κ 0.647 | `scripts/analysis/difficulty_labels.py` → `reports/analysis/DIFFICULTY_LABELS.md` | R (Codex ✓) |
| L10 | Difficulty discrimination | 2,301/3,808, 3,831/6,545, 687/1,162; Δ 1.30 [−4.06, 6.62]; OR 1.058 [0.834, 1.341]; ρ −0.0269 | same | R (Codex ✓) |
| L11 | Clean split | 10,628 rows; 316 quarantined; 62 pending; usable 7,313/1,595/1,658; manifest 7,382/1,596/1,662 | `data/cleaned/clean_final.jsonl`, `data/quarantine/quarantine_all.jsonl`, `splits/split_v1.json` (Codex counted) | R |
| L11b | Four test IDs removed after the split was frozen | 1,662 → 1,658: `26a6a66f…`, `2eaa5ad4…`, `56effd0a…`, `ebc900a6…` | `reports/eval/raw/fates.json` ("dedup: cleaning stages 12/14"); stages added in commit `5a8d12f` (2026-08-07), split frozen in `4a96690` (2026-07-31) | R |
| L11c | No normalized-stem group spans two splits | 0 | Codex check | R |
| L12 | Accuracies | 1,183 / 1,188 / 1,044 / 993 / 904 / 778 / 775 of 1,658 | `reports/eval/runs/*__paper__test.jsonl`, last error-free record per id | R (Codex ✓) |
| L12b | Paper reference scores | Llama-3.1-8B 48.73; Gemma3-12B 58.05; Phi-4 51.15 | Paper Table 2 | P |
| L13 | Raw−clean estimate | −0.1 / +0.2 pp (two models) | `reports/eval/RAW_VS_CLEAN.md` | F |
| L13b | Conflicting-key removed rows | 70 rows; Llama 32.9%, Qwen3.5 28.6%; uniform-random baseline 25.4% | `RAW_VS_CLEAN.md`; baseline = mean 1/n_options over the 70 rows with fate "dedup: duplicate, CONTRADICTING answer" | F / R (baseline) |
| L14 | Model flags | 238; 140/210; 125; overlap 95; union 268 | `scripts/eval/build_review_workbook.py` | R (Codex ✓) |
| L15 | Explanations | 320 IDs (268 flagged + 52 random-sample); 90/140 keep; 4 abstain; 108/237 change within the flagged union (115/276 over all IDs with both records) | `reports/eval/reasoning/nvidia__nvidia_nemotron-3-ultra-550b-a55b__explain__review_ids__think-on.jsonl` | R (Codex ✓) |
| L16 | Ensemble = one model × 3 shuffled runs + vote | — | Paper §4 | P (Codex ✓) |
| L16b | Table 3 reference column | 12 = pass@3; 4 = pass@1 (o3-mini, Qwen3-32B, Qwen3-30B-A3B, HuatuoGPT-o1-8B); Gemini 77.29 ≠ pass@3 77.92; Llama 4 Δ printed −1.33, computed −0.67 | Paper Tables 2–3, all 17 rows | P (Codex ✓, Claude ✓ for Gemini, Llama 4, Huatuo). Note: Table 3 names "Llama-3-8B-Instruct" for the model Table 2 calls Llama-3.1-8B-Instruct |
| L17 | Review protocol (pilot) | 60 random; strata 3/85/15/15; 178 total; 36 double | `reports/eval/review_sample/sample_manifest.csv`, `HUONG_DAN.md` | R |
| L18 | Earlier manual check of 25 conflicting groups | 9 genuine key conflicts | `docs/research/VM14K_manual_verify.pdf` | F |
| L19 | Review results | — | `scripts/eval/analyze_review.py` | T |
| L21 | VM14K paper scope | 34 specialties; 4 difficulty levels; 17 models | Paper abstract, §3, Tables 2–3 | P |
| L22 | Stage count guards | `assert_stage_count(...)` per stage | `scripts/cleaning/clean_all.py`; `docs/cleaning/CLEANING.md` | F |
| L23 | Pipeline issues found and handled | BUG-1 (post-repair duplicates, now stage 12); BUG-2 (unadjudicated survivors → 62 flagged) | `docs/cleaning/CLEANING.md` §BUG-1, §BUG-2 | F |
| L20 | Related-work numbers (MMLU-Redux 6.49% / 57% analysed Virology; Platinum 15 benchmarks) | — | Gema et al. 2025; Vendrow et al. 2025 | P — [TBD: verify every citation] |

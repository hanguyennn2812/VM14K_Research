# VM14K: Vietnamese Medical Decision Models

**Research date: 2026-10-23. Read-only review; no files modified.**

## 1. Recommendation

**Start with Decision-1.0 Sol-2B and a matched Qwen3.5-2B with your own candidate head. Add Eos-0.8B as the efficiency experiment; retain Nox-4B as a capacity control.** These checkpoints provide the relevant size comparisons, but their Vietnamese medical performance remains unverified. [Sol](https://huggingface.co/vllm-sr/Decision-1.0-Sol-2B), [Qwen-2B](https://huggingface.co/Qwen/Qwen3.5-2B), [Eos](https://huggingface.co/vllm-sr/Decision-1.0-Eos-0.8B), [Nox](https://huggingface.co/vllm-sr/Decision-1.0-Nox-4B).

The strongest research question is:

> **Does decision-specific pretraining improve Vietnamese medical accuracy, calibration, and selective prediction beyond ordinary LoRA and temperature scaling—and does guideline supervision add knowledge beyond exam-format adaptation?**

Your existing one-pass letter-logit models are essential baselines. They already achieve approximately 2% ECE after LoRA, so returning probabilities without generating text is insufficient as the contribution. [Project fine-tuning results](F:/VM14K_Research/reports/eval/FINETUNE.md).

### Model comparison

Input limits below include the question and candidate descriptions, unless stated otherwise.

| Model / exact Hugging Face repository | Licence | Backbone and option scoring | Input length | Vietnamese evidence; proposed role |
|---|---|---|---|---|
| [Decision-1.0-Eos-0.8B](https://huggingface.co/vllm-sr/Decision-1.0-Eos-0.8B) | Apache-2.0 | Qwen3.5-0.8B text backbone; shared candidate head | 16,384 | Multilingual positioning; no verified Vietnamese medical results. **Efficiency candidate.** |
| [Decision-1.0-Sol-2B](https://huggingface.co/vllm-sr/Decision-1.0-Sol-2B) | Apache-2.0 | Qwen3.5-2B text backbone; shared candidate head | 16,384 | No verified Vietnamese medical results. **Primary decision checkpoint.** |
| [Decision-1.0-Nox-4B](https://huggingface.co/vllm-sr/Decision-1.0-Nox-4B) | Apache-2.0 | Qwen3.5-4B text backbone; shared candidate head | 16,384 | No verified Vietnamese medical results. **Capacity control.** |
| [Decision-1.0-Lux-9B](https://huggingface.co/vllm-sr/Decision-1.0-Lux-9B) | Apache-2.0 | Qwen3.5-9B text backbone; shared candidate head | 16,384 | No verified Vietnamese medical results. **Larger comparator**, lower training priority. |
| [Decision-1.0-Kai-0.6B](https://huggingface.co/vllm-sr/Decision-1.0-Kai-0.6B) | Apache contributions, retained upstream terms¹ | Vela/mmBERT-derived encoder; separate Choice/Noul/Score paths with candidate readouts | 1,024 | Multilingual ancestry; no verified Vietnamese medical results. **Optional encoder baseline.** |
| [Decision-1.0-Lex-0.6B](https://huggingface.co/vllm-sr/Decision-1.0-Lex-0.6B) | Same qualification¹ | Kai architecture, specialized for English operational workflows | 1,024 | English specialization provides no established medical advantage. **Lowest priority.** |
| [Cloudflare/clef-flash](https://huggingface.co/Cloudflare/clef-flash) | Apache-2.0 | Qwen3.5-9B with joint schema-routing head; per-question softmax | Advertised 64K; released Python API defaults to 16,384² | No Vietnamese medical validation verified. **Strong external decision baseline.** |
| [autotrust/JEV-9B](https://huggingface.co/autotrust/JEV-9B) | Apache-2.0 | Frozen Qwen3.5-9B text backbone, rank-16 LoRA, 24-slot head; Choice activates up to 16 answer slots | Backbone configuration: 262,144; serving example: 4,096³ | Already measured locally: 62.7%, ECE 3.1%. **Reuse as baseline.** |
| **CS1-4B** — no public HF weights verified | Release licence **unverified** | Full fine-tune of **Decision 2.0 Nox-4B**, retaining its candidate head | Document ≤15,356 tokens; question segment ≤1,024; packed training unit ≤20,480 | English clinical-record evidence; Vietnamese transfer unverified. **Do not depend on availability.** [Paper](https://arxiv.org/html/2610.27099v1) |
| Plain [Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B), [2B](https://huggingface.co/Qwen/Qwen3.5-2B), [4B](https://huggingface.co/Qwen/Qwen3.5-4B) + own head | Apache-2.0 | Use text backbone; implement candidate scoring explicitly | Native backbone context: 262,144; use 1–2K initially | Publisher reports multilingual benchmarks; your VM14K runs provide direct evidence for 2B. **Mandatory matched controls.** |
| Plain **Qwen3.8 small models** | **Unverified** | Official 0.8B/2B/4B checkpoints were not verified | **Unverified** | Do not build the plan around third-party names. The official collection lists larger Qwen3.8 releases. [Official collection](https://huggingface.co/Qwen/collections) |

¹ Kai/Lex are **not an unconditional Apache-only stack**: retained MIT components and Gemma-origin tokenizer terms apply. [Licensing status](https://huggingface.co/vllm-sr/Decision-1.0-Kai-0.6B/blob/main/LICENSING_STATUS.md).

² Distinguish Cloudflare’s advertised context from the code’s default admission limit and the backbone’s positional capacity. [Announcement](https://blog.cloudflare.com/clef-decision-models/), [released API code](https://huggingface.co/Cloudflare/clef-flash/blob/main/joint_schema_model.py).

³ The configuration ceiling is **not demonstrated long-context decision quality**. [JEV configuration](https://huggingface.co/autotrust/JEV-9B/blob/main/config.json), [serving instructions](https://huggingface.co/autotrust/JEV-9B). Local accuracy comes from [JEV.md](F:/VM14K_Research/reports/eval/JEV.md).

**CS1 availability:** the paper explicitly says weights and training/inference code will be released after institutional approval, with a credentialed release anticipated. I found no verified public checkpoint. Its clinical results therefore motivate the methodology, not an immediately usable base. [CS1 paper](https://arxiv.org/html/2610.27099v1).

### What “candidate head” means

- **Decision decoders:** candidate-endpoint states and the final query state enter a shared scoring head; all options for one question are scored in one backbone pass. This differs from reading A/B/C/D logits. [Sol architecture](https://huggingface.co/vllm-sr/Decision-1.0-Sol-2B).
- **Clef-flash:** jointly routes state evidence to schema fields and options. Cloudflare trained the routing head and rank-256 LoRA using label-smoothed CE plus Brier loss. [Architecture and training](https://blog.cloudflare.com/clef-decision-models/).
- **JEV-9B:** reads the final prompt state into fixed answer slots initialized from answer-token rows. It is an independent student, distinct from proprietary TypeSafe Jev. [Model card](https://huggingface.co/autotrust/JEV-9B).
- **Proposed Qwen control:** use a shared scalar scorer over contextualized candidate representations, normalize across valid options, and shuffle option order during training. This is a proposed implementation, not a released Qwen capability.

### Training tooling: the practical limitation

| Family | Verified tooling status |
|---|---|
| Eos/Sol/Nox/Lux | Transformers inference is released; **a current end-to-end training CLI was not verified**. Integrating LoRA, differentiable head outputs, and loss requires work. [Release tree](https://huggingface.co/vllm-sr/Decision-1.0-Sol-2B/tree/main) |
| Kai/Lex | Historical fine-tuning tools exist at a pinned revision; they should not be assumed compatible with current artifacts without checking. [Historical training documentation](https://huggingface.co/vllm-sr/Decision-1.0-Kai-0.6B/blob/52c81702356711b43b1a68e4aca8c98c84230155/FINETUNING.md) |
| Clef-flash | Weights and differentiable model code are public; **complete local training/RLCD scripts were not verified**. Cloudflare advertises managed fine-tuning. [Files](https://huggingface.co/Cloudflare/clef-flash/tree/main), [announcement](https://blog.cloudflare.com/clef-decision-models/) |
| JEV-9B | Recipe published; independent Apache-2.0 [jev-torch](https://github.com/smha1012/jev-torch) provides training code and reports an H100 reproduction. Its QLoRA path is explicitly not yet validated. |
| Plain Qwen | Public LoRA/QLoRA tooling exists; a candidate head and its loss still need integration. Reuse the team’s working trainer where possible. [ms-swift documentation](https://github.com/modelscope/ms-swift/blob/main/docs/source_en/BestPractices/Qwen3_8-Best-Practice.md) |

**Important hardware issue:** the current Decision decoder loader specifies BF16 on GPU. T4 execution needs a verified FP16-compatible path; memory fit alone does not establish compatibility. Use H100 for the initial reference run. [Decision runtime requirements](https://huggingface.co/vllm-sr/Decision-1.0-Sol-2B), [FlashAttention hardware support](https://github.com/Dao-AILab/flash-attention).

### VRAM planning

**Engineering estimates, not measured training requirements.** Assume text only, 1–2K tokens, microbatch 1, checkpointing, low-rank adapters, and FP32 head/loss. Actual peaks may differ substantially.

| Models | LoRA planning envelope | QLoRA planning envelope | Practical placement |
|---|---:|---:|---|
| Eos / plain 0.8B | 4–8 GB | 3–6 GB | One T4 after compatibility checks |
| Sol / plain 2B | 7–12 GB | 5–10 GB | One T4; H100 for reference |
| Nox / plain 4B | 12–22 GB | 8–15 GB | QLoRA on one T4; otherwise H100/sharding |
| Lux / JEV / plain 9B | 23–36 GB | 12–22 GB | H100 preferred; T4 requires sharding or careful QLoRA |
| Clef-flash | 30–50 GB with rank-256 adapters | 18–30 GB | H100 preferred |
| Kai/Lex | Roughly 8–16 GB for active Choice-path tuning | Not established | T4 potentially feasible; measure first |
| CS1-4B | No released training implementation to profile | Not established | Theoretical 4B envelope only |

Two T4s are **two 16-GB devices**, not a transparent 32-GB pool. Ordinary data parallelism replicates weights. The team has already demonstrated 9B FP16 LoRA with explicit two-GPU splitting, which is better evidence than generic estimates. [Existing training configuration](F:/VM14K_Research/reports/eval/FINETUNE.md).

## 2. Build data to distinguish knowledge from habits

### Preserve the benchmark

Use the frozen **7,313 train items**, retaining original keys and provenance. Shuffle options with correct label remapping; mask absent options. Keep validation and test out of training, generation prompts, demonstrations, and retrieval-example banks.

Do not silently correct disputed keys. Report the original benchmark and a separately adjudicated sensitivity analysis. The “undisputed” subset is model-selected and cannot serve as an unbiased replacement test. [Project voting analysis](F:/VM14K_Research/reports/eval/VOTE.md).

### Resolve the corpus discrepancy first

The checked-in audit reports **100 usable documents and 6,972 eligible pages**, using PyMuPDF 1.28.2 and a 50-character page floor, rather than 104 usable documents. It also identifies incomplete document parts and zero usable emergency-medicine coverage. Reconcile this before freezing generation inputs. [Corpus audit](F:/VM14K_Research/reports/analysis/moh_corpus_audit.md), [corpus specification](F:/VM14K_Research/data/MoH_corpus_spec.md).

### Grounded synthetic MCQ pipeline

| Stage | Proposed procedure |
|---|---|
| Split first | Group by **parent document, disease/topic, and guideline version** before chunking. Keep duplicate files and multipart documents together. |
| Generator | Start with the existing **Qwen3.5-27B 4-bit pipeline**. Supply only an approved guideline section; request Vietnamese questions, 2–4 options, one correct answer, and evidence for every option. [Checkpoint](https://huggingface.co/Qwen/Qwen3.5-27B), [existing pipeline results](F:/VM14K_Research/reports/eval/QWEN27B.md). |
| Provenance | Store document ID, official URL, decision number/date, page/section, evidence span, generator revision, prompt, and filter outcomes. |
| Automatic filters | Require unique options, exactly one supported answer, plausible distractors, explicit population/time qualifiers, and intact doses/units. Reject questions requiring missing pages or unsupported textbook conventions. |
| Independent verification | Have another available strong model solve the item **without seeing the proposed key**, then check its evidence. Agreement is a filter, not clinical ground truth. |
| Human audit | Clinicians review a stratified pilot of approximately 200 items, emphasizing numbers, contraindications, ambiguity, and Vietnamese terminology. Target ≥95% acceptable before scaling; otherwise revise generation. |
| Scale | Begin with 1,000 accepted items; expand to 5,000 only if quality and measured generation cost justify it. Cap domination by infectious-disease documents. |

Keep rationales and evidence in the dataset for audit; the decision model’s target remains an option distribution.

### Leakage controls

- Never ask generators to repair or imitate the 125 failed test questions.
- Deduplicate synthetic questions against all benchmark partitions using normalized text, lexical similarity, and semantic review.
- Have a separate overlap audit return exclusion IDs; do not expose held-out items to the generator or use overlap findings to improve prompts.
- Split synthetic validation/test by source document and disease cluster, **not by generated question**.
- Flag residual pretraining contamination as unknown.

Train and evaluate **two distinct tasks**:

1. **Closed-book:** no guideline passage at inference—tests retained knowledge.
2. **Evidence-conditioned:** retrieved guideline passage supplied—tests application of evidence.

A gain only in the second supports evidence use, not knowledge internalization.

### Copyright

Maintain the team’s exclusion of copyrighted textbooks. Public availability of a guideline does not establish that every annex, figure, or incorporated work is freely redistributable.

Vietnam’s Article 15 excludes specified official documents from copyright; the 2025 amendment also introduced a conditional AI-training provision, effective April 2026. **Neither establishes blanket clearance for this corpus or public dataset redistribution.** Record the legal basis per document and distinguish training access from redistribution rights. [Article 15](https://vbpl.vn/uybandantoc/Pages/vbpq-toanvan.aspx?ItemID=16748), [Copyright Office explanation of the amendment](https://cov.gov.vn/tin-tuc/gioi-thieu-luat-sua-doi-bo-sung-mot-so-dieu-cua-luat-so-huu-tri-tue-nam-2025-noi-dung-quyen-tac-gia-quyen-lien-quan-168841.html).

The inspected VM14K dataset card did not establish an explicit redistribution licence; verify this separately before releasing derived question text. [Dataset card](https://huggingface.co/datasets/AnonymouseV/VM14K).

## 3. Evaluation that could support publication

### Required comparisons

| Axis | Comparisons |
|---|---|
| Architecture | Plain Qwen letter logits versus own candidate head versus Decision checkpoint, at matched backbone size |
| Adaptation | Untuned; VM14K-only; synthetic-only; VM14K + synthetic |
| Calibration | Raw versus validation-fitted temperature scaling; CE versus CE + Brier as a limited ablation |
| Evidence | Closed-book versus identical retrieved evidence across models |
| Scale | 0.8B and 2B primary; 4B capacity control; 9B external references |
| Generation | Same-backbone direct answer generation; larger existing generative runs; reasoning generation separately |
| Cheap alternatives | Letter-prior correction, temperature scaling, and the existing LoRA baseline |

Use both CE and Brier rather than assuming label smoothing is necessary. Select loss weights on development data. Temperature scaling is a required inexpensive comparator. [Calibration reference](https://arxiv.org/abs/1706.04599).

### Metrics and protocol

| Area | Report |
|---|---|
| Correctness | Accuracy, paired bootstrap confidence intervals, McNemar comparison; three seeds for final training comparisons |
| Probabilities | NLL, multiclass Brier **\(\frac1N\sum_i\sum_k(p_{ik}-y_{ik})^2\)**, reliability plots, 15-bin ECE plus equal-frequency sensitivity analysis |
| Variable option count | Separate 2/3/4-option results and calibration; include uniform-probability Brier references |
| Abstention | Risk–coverage curve, AURC, coverage at predefined error targets; thresholds selected on calibration data |
| Escalation | Accuracy/cost frontier against random routing and the larger model alone; include all escalation costs |
| Robustness | Option permutations, paraphrases, negation, numerical changes, irrelevant evidence, and missing evidence |
| Efficiency | Same GPU, precision, input budget, batch 1 and throughput batches; p50/p95 latency, peak VRAM, questions/sec, cost/1,000 questions |
| Specialty | Counts and intervals for all 34 labels; macro-specialty result alongside overall accuracy; multiplicity correction for exploratory claims |

Measure generation, one-pass letter scoring, and candidate scoring separately. **Do not claim a large speedup by comparing a decision head only with long reasoning generation.** Selective prediction should measure error against retained coverage, not merely confidence concentration. [Selective-classification reference](https://arxiv.org/abs/1705.08500).

Split the 1,595 validation items into fixed **development and calibration subsets**. Do not tune temperature, abstention thresholds, or stopping rules on test results.

### Held-out-topic experiment

Preselect two sufficiently represented disease clusters from train/validation metadata:

- Remove every related VM14K training item, including multilabel overlaps.
- Remove corresponding synthetic questions and guideline sections.
- Evaluate a **new clinician-authored test** on those clusters.
- Then introduce only their guideline-derived training data and measure the incremental change.

This separates general format transfer from topic-specific learning. Include clinician-checked paraphrases and numerical counterfactuals to test whether improvements survive changed wording.

The existing VM14K test remains useful, but repeated inspection means it is no longer a pristine prospective evaluation. A fresh, independently keyed document/topic holdout is the most valuable addition.

## 4. Main failure risks

| Risk | Consequence and response |
|---|---|
| Guidelines do not cover textbook conventions | Better guideline reasoning may barely move VM14K accuracy. Report performance by answerability/source category; do not target training at known test failures. |
| Fine-tuning mostly teaches habits | Repeat the topic holdout and compare against prior correction, option shuffling, and temperature scaling. Existing evidence supports this hypothesis but does not prove knowledge learning is impossible. |
| Small-model knowledge ceiling | A calibrated 2B model may remain substantially less accurate. Assess selective utility; use Nox-4B to test capacity. |
| Synthetic errors and teacher bias | Require evidence, independent solving, clinician audits, and human-keyed final evaluation. |
| Calibration fails under shift | Report held-out-topic calibration and fixed-threshold coverage; low in-distribution ECE is insufficient. |
| Head offers no measurable advantage | A negative result is useful if matched controls show that simple letter scoring achieves the same frontier. |
| Tooling consumes the project | Time-box Decision training integration to one day; retain the working plain-Qwen trainer as fallback. |

Existing results set a demanding standard: 9B LoRA already reaches **66.8% with approximately 2% ECE**, while the retrieved 27B baseline reaches **72.7%**. These are local reference results, not directly comparable with the paper’s uncleaned-release scores. [Fine-tuning](F:/VM14K_Research/reports/eval/FINETUNE.md), [retrieval](F:/VM14K_Research/reports/eval/QWEN27B.md).

## 5. Concrete two-week plan

| Dates | Ordered experiment / work | Decision produced |
|---|---|---|
| **Oct 23–25** | **Experiment 1: untuned screening.** Evaluate Eos, Sol, Nox, Kai/Lex, and matched Qwen readouts on development data; add Lux/Clef-flash as resources permit. Reuse JEV results. Start reference execution on H100; measure input failures, calibration, latency, and memory. | Select 0.8B/2B candidates by measured accuracy–cost tradeoff. Establish whether T4 execution is viable. |
| **Oct 26–28** | **Experiment 2: isolate decision pretraining/head value.** Fine-tune Sol-2B and plain Qwen3.5-2B candidate-head/letter-logit controls on VM14K only, with matched examples and training budgets. Fit temperatures separately. | Determine whether the decision checkpoint adds value beyond ordinary adaptation. |
| **Oct 29–Nov 2** | **Experiment 3: grounded-data pilot.** Audit 1,000 accepted synthetic items, then compare VM-only with VM + synthetic on the selected model. Evaluate both closed-book and evidence-conditioned; add a matched VM-only replay control. | Determine whether gains reflect new knowledge, evidence use, or simply more optimization. |
| **Nov 3–5** | Repeat decisive comparisons across three seeds; complete held-out-topic and fresh clinician-keyed evaluation, permutations, risk–coverage curves, and final cost measurements. | Produce a reproducible result with uncertainty and an explicit failure analysis. |

Reserve Kaggle’s weekly allocation for short-context training and screening; use H100 for reference compatibility and selected larger runs. Measure throughput before committing to synthetic-data scale, and keep AWS outside the critical path until its GPU is identified.

**Deliverable:** a small, reproducible Vietnamese medical decision model plus a controlled study of whether decision pretraining and guideline supervision improve the accuracy–calibration–cost frontier. A publishable outcome depends on that evidence, not on attaching a new head alone.
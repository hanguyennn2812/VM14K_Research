# VM14K Research

Reproducible analysis, cleaning, and Ministry-of-Health-grounded evaluation of
the released VM14K medical question dataset.

## Repository layout

```text
VM14K_Research/
├── data/
│   ├── raw/          Original released JSONL files
│   ├── baseline/     Output of the reproduced authors' dedup pipeline
│   ├── cleaned/       clean_final.jsonl — the accepted dataset
│   ├── annotations/  Fixed human-annotation sets for retrieval evaluation
│   └── quarantine/   quarantine_all.jsonl — every excluded row, tagged by stage
├── reports/
│   ├── analysis/     Duplicate, contradiction, and baseline dedup reports
│   └── cleaning/     clean_final.report.json — one machine-readable report
├── docs/
│   ├── research/     Research findings and supporting PDFs
│   └── cleaning/     CLEANING.md (pipeline + evidence) and the review backlog
├── scripts/
│   ├── analysis/     Original-pipeline reproduction and audit scripts
│   ├── retrieval/    Page-aware MoH retrieval and gold-set tooling
│   └── cleaning/     clean_all.py — the entire cleaning pipeline, one file
└── README.md
```

## Current accepted dataset

- Dataset: `data/cleaned/clean_final.jsonl`
- Rows: 10,628 total; 10,566 usable after excluding 62 pending answer-key reviews
- Full pipeline explanation, worked examples, and rollback: `docs/cleaning/CLEANING.md`
- Deferred manual-review items: `docs/cleaning/REMAINING_REVIEW_BACKLOG.md`

## Current grounded-research direction

The active protocol is `docs/research/OPENEVIDENCE_GROUNDED_PROTOCOL.md`. It
supersedes answer-only fine-tuning as the immediate priority:

1. freeze and reconcile the MoH corpus;
2. finish page-level evidence annotation for the fixed 30-question cardiology set;
3. compare TF-IDF, BGE-M3, and their reciprocal-rank fusion using Recall/MRR;
4. only after retrieval passes the predeclared gate, generate answer + explanation
   + source and validate the automatic support checker.

Create/reproduce the pending annotation template:

```powershell
python scripts/retrieval/export_cardiology_gold_template.py
python scripts/retrieval/prepare_cardiology_gold_candidates.py
```

The second command writes a separate search-aid file with candidate PDF pages;
it never changes pending labels or treats retriever output as human gold.

After all annotations are marked complete, run retrieval evaluation:

```powershell
ollama pull bge-m3
python scripts/retrieval/evaluate_moh_retrieval.py --force
```

The evaluator uses local Ollama embeddings by default and caches the page-level
corpus vectors by model + corpus SHA-256. A SentenceTransformers backend remains
available for GPU/cloud reproduction.

After the retrieval gate passes, generate two-pass auto-checked Cardiology
grounding candidates (train/validation only; test is rejected by code):

```powershell
python scripts/retrieval/generate_grounded_cardiology.py
```

The generated rows are explicitly marked `uncalibrated_auto_check`. The checker
decomposes compound answers into atomic claims and requires page evidence for
every drug, dose, procedure, condition, and lifestyle instruction. The normal
SFT exporter refuses them until a human verifies them or the support checker is
calibrated. For a clearly labelled exploratory pilot only, the gate can be
bypassed:

```powershell
python scripts/training/export_qwen_sft_grounded.py `
  --allow-uncalibrated-auto-check
```

Qwen3-8B QLoRA requires a CUDA machine; the local environment has CPU-only
PyTorch. On Colab/Kaggle/A10/L4/A100, install a CUDA PyTorch build, then:

```bash
python -m pip install -r requirements-gpu.txt
python scripts/training/train_qwen_grounded_qlora.py
```

The trainer uses 4-bit NF4 double quantization, all-linear LoRA, assistant-only
loss, validation-loss checkpoint selection, and refuses silent truncation or
train/validation ID overlap.

## Analysis workflow

Use Python 3.11+ and install the analysis dependencies:

```powershell
python -m pip install -r requirements.txt
```

Inspect duplicate and contradiction groups:

```powershell
python scripts/analysis/vm14k_dupes_and_contradictions.py
```

Regenerate the human-readable analysis reports:

```powershell
python scripts/analysis/vm14k_dupes_and_contradictions.py --write
```

Reproduce the authors' deduplication pipeline:

```powershell
python scripts/analysis/vm14k_dedup.py `
  --out data/baseline/clean.jsonl `
  --report reports/analysis/report.json
```

The existing baseline and reports are immutable artifacts. To reproduce without
overwriting them, pass temporary output/report paths.

## Cleaning workflow

One script runs the whole pipeline end to end:

```powershell
python scripts/cleaning/clean_all.py
```

It reads `data/baseline/clean.jsonl`, applies eleven audited stages in
memory, and writes exactly three files: `data/cleaned/clean_final.jsonl`,
`data/quarantine/quarantine_all.jsonl`, and
`reports/cleaning/clean_final.report.json`. Each stage has an
expected-count guard and aborts the run if its audited scope changes. Pass
`--force` to overwrite existing output files.

See `docs/cleaning/CLEANING.md` for what each stage does, why, and worked
before/after examples.

## Model evaluation workflow

Zero-shot evaluation on the frozen split, using the paper's Fig. 6 prompt and
pass@1 so results sit next to the paper's Tables 3-4. Works with Ollama
(local, or cloud models after `ollama signin`) and with OpenAI-compatible APIs
(`nvidia`, `groq`, `cerebras`, `gemini`, `openrouter`, `deepseek`; the key is
read from `<PROVIDER>_API_KEY`):

```powershell
python scripts/eval/run_eval.py --model qwen3:8b --limit 20   # smoke test
python scripts/eval/run_eval.py --model qwen3:8b              # full test split
$env:NVIDIA_API_KEY = "nvapi-..."
python scripts/eval/run_eval.py --provider nvidia --model deepseek-ai/deepseek-v3.2 --rpm 35 --workers 4
python scripts/eval/summarize_eval.py                         # reports/eval/SUMMARY.md
```

Per-question predictions land in `reports/eval/runs/<run>.jsonl`. A killed
run, or one stopped by a rate limit or daily quota (HTTP 429), resumes where it
stopped when the same command is rerun. `summarize_eval.py` writes overall,
per-topic (paper top-10 and all topics, with 95% intervals) and per-difficulty
tables, plus `reports/eval/per_topic.csv`. Options: `--prompt vi` for a
Vietnamese instruction, `--think on` for reasoning models (the run warns if
replies hit the token limit before giving a letter), `--extra-body` for
provider-specific switches such as `'{"reasoning_effort": "low"}'`,
`--shuffle-seed N` to permute options, `--temperature/--top-p/--top-k` for
models that break under greedy decoding (report it when used).

Compare two runs question-by-question (McNemar exact test, overall and per
topic) — the test to use for "did this change help on topic X?":

```powershell
python scripts/eval/compare_runs.py reports/eval/runs/A.jsonl reports/eval/runs/B.jsonl --topic Pulmonology
python scripts/eval/summarize_eval.py --include-smoke --common --runs ... --out-md reports/eval/SCREEN400.md
```

`--common` scores every listed run only on the ids they all answered, so full
runs can sit next to `--limit 400` screens.

Raw release vs cleaned split (the paper scored the raw 12,488 rows). Cleaning
keeps 10,567 rows byte-identical, so only the 1,860 removed rows and the
edited test rows need scoring with the raw text; a determinism check (40/40
identical answers on re-run) backs that shortcut:

```powershell
python scripts/eval/raw_vs_clean.py ids        # fates.json + raw_delta_ids.txt
python scripts/eval/run_eval.py --model llama3.1:8b --data data/raw/data-processed-shuffled0.jsonl `
  --ids reports/eval/raw/raw_delta_ids.txt --tag raw0-delta
python scripts/eval/raw_vs_clean.py report --pair <clean test run> <raw0-delta run>   # RAW_VS_CLEAN.md
```

## Important notes

- `data/raw/` and `data/baseline/` are preserved inputs; `clean_all.py` never
  writes to them.
- Every quarantined row is preserved unmodified inside `quarantine_all.jsonl`
  (under the `"row"` key), tagged with the stage and reason that excluded it.
- Structural cleaning does not establish medical correctness — see the
  review backlog.
- The analysis scripts intentionally use the authors' aggressive normalizer so
  their published logic and counts remain reproducible.
- `vm14k_dedup.py` uses `thefuzz` when available; otherwise it applies
  TheFuzz-compatible integer rounding to the installed RapidFuzz backend. Both
  routes reproduce the documented 10,956-row baseline.

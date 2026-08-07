# VM14K Research

Reproducible analysis and cleaning of the released VM14K medical question
dataset.

## Repository layout

```text
VM14K_Research/
├── data/
│   ├── raw/          Original released JSONL files
│   ├── baseline/     Output of the reproduced authors' dedup pipeline
│   ├── cleaned/       clean_final.jsonl — the accepted dataset
│   └── quarantine/   quarantine_all.jsonl — every excluded row, tagged by stage
├── reports/
│   ├── analysis/     Duplicate, contradiction, and baseline dedup reports
│   └── cleaning/     clean_final.report.json — one machine-readable report
├── docs/
│   ├── research/     Research findings and supporting PDFs
│   └── cleaning/     CLEANING.md (pipeline + evidence) and the review backlog
├── scripts/
│   ├── analysis/     Original-pipeline reproduction and audit scripts
│   └── cleaning/     clean_all.py — the entire cleaning pipeline, one file
└── README.md
```

## Current accepted dataset

- Dataset: `data/cleaned/clean_final.jsonl`
- Rows: 10,642
- Full pipeline explanation, worked examples, and rollback: `docs/cleaning/CLEANING.md`
- Deferred manual-review items: `docs/cleaning/REMAINING_REVIEW_BACKLOG.md`

## Analysis workflow

Install the analysis dependencies:

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

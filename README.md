# VM14K_Research

This repository contains a reproducible analysis of the VM14K dataset release. It includes the released data, scripts for duplicate and contradiction analysis, a cleaned output, and the written findings that summarize what the scripts reveal.

## File Guide

| File | What it is for |
| --- | --- |
| `data-processed-shuffled0.jsonl` | Main source dataset used by the analysis scripts. This is the original JSONL release with one record per line. |
| `data-processed-shuffled1.jsonl` | Alternate shuffled copy of the dataset, kept for comparison and traceability. |
| `data-processed-shuffled2.jsonl` | Another shuffled copy of the dataset, kept for comparison and traceability. |
| `dedup_utils.py` | Normalization helpers used by the original code. The scripts rely on these rules so their counts match the authors' logic. |
| `vm14k_dupes_and_contradictions.py` | Reproducibly groups rows into duplicate and self-contradictory question sets, and can write `duplicates.md` and `contradictions.md`. |
| `vm14k_dedup.py` | Reproduces the authors' deduplication pipeline on the released JSONL data and can write a cleaned dataset plus a JSON report. |
| `duplicates.md` | Human-readable duplicate-question report generated from the dataset. |
| `contradictions.md` | Human-readable contradiction report showing groups where the marked answer changes across duplicate rows. |
| `clean.jsonl` | Cleaned dataset output after running the deduplication pipeline. |
| `report.json` | Machine-readable summary of the deduplication run and its counts. |
| `VM14K_session_findings.md` | Written research notes and conclusions from the analysis work in this repository. |
| `VM14K_audit_notes.pdf` | Supporting audit notes for the dataset investigation. |
| `VM14K_manual_verify.pdf` | Manual verification notes and evidence for the findings. |

## Common Workflow

1. Run `python vm14k_dupes_and_contradictions.py` to inspect duplicate and contradiction groups.
2. Run `python vm14k_dupes_and_contradictions.py --write` to regenerate `duplicates.md` and `contradictions.md`.
3. Run `python vm14k_dedup.py --out clean.jsonl --report report.json` to reproduce the cleaned output and summary report.

## Notes

The scripts are written to match the authors' normalization and deduplication behavior as closely as possible. That is important here because small changes in normalization can change the counts.


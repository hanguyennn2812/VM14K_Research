# MoH Guideline Corpus — Ingestion Specification (v1)

**Status:** draft, pre-freeze
**Scope:** Ministry of Health (BYT/SYT) clinical guideline PDFs, one zip, 26 specialty folders.
**Purpose:** turn the raw PDF dump into a frozen, auditable text corpus for training use, with every token traceable to a source document and every exclusion logged with a reason. Same discipline as the VM14K frozen artifact.

This is a spec, not results. Numbers below are provisional and marked as such; they get replaced by exact values at manifest-freeze time.

---

## 1. Source inventory (provisional)

| Item | Value | Confidence |
|---|---|---|
| PDF files on disk | 112 | measured (`find -iname '*.pdf' \| wc -l` — reconfirm) |
| Files claimed by index PDF | 109 (+`.DS_Store`, +`.tex`) | from `van_ban_theo_chuyen_khoa.pdf` |
| Specialty folders | 26 | measured |
| Extractable non-whitespace chars (all files) | 10,098,274 | measured (one run, crashed after) |
| Rough token estimate | ~2.8M (chars ÷ 5 × ~1.4) | go/no-go only, NOT for freeze |

**OPEN — denominator reconciliation.** 112 on disk vs 109 in the index. Must be resolved before freeze: diff the on-disk filename list against the index PDF's list to identify the 3+ extra/missing. Do not freeze a corpus whose file count you can't explain — same rule as the 12,488 VM14K row count.

---

## 2. Extractability split

Files fall into two classes by extractable char count (from `extract_report.tsv`):

- **Born-digital** — high char count (the mass runs 100k–900k chars). Text extracts cleanly via `pdftotext`. **In scope for v1.**
- **Scanned / no text layer** — 0 to low-hundreds of chars despite tens/hundreds of pages. **Out of scope for v1** (see §4).

Nearly all extractable *content* lives in the born-digital class, even though scanned files are a non-trivial share of the *file count*. The corpus is viable without OCR.

Confirmed 0-char (scanned) examples: `636` first-aid, `3594` nutrition, `2674` HIV testing, `3792` cervical cancer. Full per-file classification lives in `extract_report.tsv`.

---

## 3. Known data issues to handle before use

### 3.1 Content duplicate — FACT
One byte-identical pair (md5 `664c9e95…`):
- `Da liễu/…4416…benh_Da_lieu.pdf`
- `Truyền nhiễm/…4416…benh_Da_lieu.pdf`

Content is dermatology guidance, correctly homed in `Da liễu`, misfiled a second time into `Truyền nhiễm`. **Action:** keep the `Da liễu` copy, drop the `Truyền nhiễm` copy, record the drop. No other md5 collisions in the set — single dedup, not a pattern.

Dedup rule: **content hash, not filename or path.** A folder-walk corpus builder would otherwise train on this twice and, if QA pairs are ever derived, produce cross-specialty label conflicts on identical content.

### 3.2 Multi-part documents — FACT
Four source documents are split across `part01`/`part02` files; none exceeds 2 parts, no gaps evident from filenames:
- `2834` HIV new-infection testing
- `2557` fundus photography / diabetic retinopathy
- `2558` diabetic retinopathy diagnosis & management
- `2201` Marburg haemorrhagic fever

**Action:** map each part → parent document; concatenate parts in sorted order; treat the concatenated result as one corpus unit. Do not tokenize parts independently (splits a guideline mid-section).

### 3.3 Mangled short-names — OPEN
Several files carry Windows 8.3 short-names (`QU25D4~1.PDF`, `QU30C0~1.PDF`, `QU54DF~1.PDF`). The underlying files are intact; only the display name is mangled. **Action:** resolve each to its real title (open + read header, or match by md5/size against the index) before it goes in the manifest. Don't freeze a manifest with unresolved names.

### 3.4 Cross-filing — NOTE
The `4416` case shows a document can be filed under more than one specialty folder. The manifest must allow a document to carry **multiple specialty tags** rather than assuming folder = single label. Deduplicate the *content*; preserve *all* folder memberships as tags.

---

## 4. Scanned files — exclusion policy

**Decision: exclude scanned files from v1. Do not OCR for v1.**

Rationale: OCR of Vietnamese medical text — dosages, drug names, tables — introduces silent numeric/character corruption. Feeding that into training unverified repeats the exact failure this project exists to catch in VM14K. A wrong digit in a dosage is worse than an absent document.

Rules:
1. Any file below a char-per-page floor (proposed: **< 50 chars/page**, tune after eyeballing the middle of `extract_report.tsv`) is tagged `scanned_dropped` with the measured value.
2. Every drop is logged with reason — nothing silently disappears (same rule as VM14K's `quarantine_all.jsonl`).
3. **Coverage check:** if excluding scanned files leaves any specialty with **zero** usable documents, flag that specialty to the supervisor as a coverage gap. Do not paper over it with bad OCR.
4. OCR is a possible **v2** sub-project with its own verification step, out of scope here.

---

## 5. Corpus manifest — the deliverable

One row **per source document** (not per file). Format: JSONL + a TSV summary.

Per-document fields:

| Field | Meaning |
|---|---|
| `doc_id` | stable id (e.g. decision number `2557`, or hash prefix if ambiguous) |
| `title` | resolved human title (short-names expanded) |
| `parent_files[]` | the one-or-more PDF files composing this doc (parts) |
| `specialty_tags[]` | all folders it appears under (≥1) |
| `pages` | total page count across parts |
| `chars` | extractable non-whitespace char count |
| `class` | `born_digital` \| `scanned_dropped` |
| `content_md5` | hash for dedup / provenance |
| `drop_reason` | populated iff excluded |
| `notes` | short-name resolution, misfiling, etc. |

Plus a **per-specialty coverage summary**: doc count, born-digital count, dropped count, total usable chars — so a coverage gap is visible at a glance.

**Freeze criteria** (all must hold before the corpus is declared v1):
- File denominator reconciled (§1 OPEN closed).
- All short-names resolved (§3.3 closed).
- Content dedup applied, drop logged (§3.1).
- Parts concatenated per parent (§3.2).
- Every file classified `born_digital` or `scanned_dropped` with a reason.
- Exact word/token count recomputed on the final born-digital set (replaces the ÷5 estimate).
- Manifest stamped with build date + a hash of the manifest itself.

---

## 6. Intended use — decide before generating anything

Two distinct jobs, different formats, **not yet chosen** — flag to supervisor:

- **(A) Continued pretraining / domain adaptation** on raw guideline text. Uses the corpus as-is. Lower verification burden (no new labels created).
- **(B) Supervised finetune on QA/MCQ pairs** derived from the guidelines. Requires an LLM to generate questions from guideline text → **creates a second unverified dataset** needing the same doctor verification as VM14K. Do not start (B) quietly.

Pin this decision before any generation. If (B), it inherits the full VM14K verification pipeline, not a shortcut.

---

## 7. Provenance & integration

When MoH text is eventually mixed into training:
- Every training row stamped with `doc_id` + `content_md5` + corpus manifest hash.
- Dataset version (VM14K clean version + MoH corpus version) is a **config parameter, never hardcoded** — so a "VM14K only" vs "VM14K + MoH" ablation is clean and no data shifts silently between runs.
- MoH corpus freeze is independent of the VM14K prof-side blockers; it can be finalised now.

---

## 8. Open items (carry list)

| # | Item | Blocks |
|---|---|---|
| 1 | Reconcile 112-on-disk vs 109-in-index | freeze |
| 2 | Resolve 8.3 short-names to real titles | freeze |
| 3 | Set char/page floor for scanned cutoff | classification |
| 4 | Confirm any specialty left at zero usable docs | supervisor flag |
| 5 | Choose intended use (A) vs (B) | all downstream generation |
| 6 | Exact token count on final born-digital set | freeze |

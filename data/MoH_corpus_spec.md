# MoH Guideline Corpus — Ingestion Specification (v1)

**Status:** draft, pre-freeze — §1/§3.2/§3.3 resolved 2026-08-28; §3.5 (new) and
item 5 (intended use) still open, see §8.
**Scope:** Ministry of Health (BYT/SYT) clinical guideline PDFs, one zip, 27
specialty folders. `Trạm y tế` is now **in scope** as the 27th specialty (decision
below); the author's `.tex` index only ever covered 26.
**Purpose:** turn the raw PDF dump into a frozen, auditable text corpus for training use, with every token traceable to a source document and every exclusion logged with a reason. Same discipline as the VM14K frozen artifact.

This is a spec, not results. Numbers below are provisional and marked as such; they get replaced by exact values at manifest-freeze time.

---

## 1. Source inventory (re-audited 2026-08-28; still pre-freeze)

| Item | Value | Confidence |
|---|---|---|
| PDF files under `data/Chuyên khoa` | 111 = 110 source PDFs + 1 root index PDF | measured in current Git tree |
| Source entries claimed by `.tex` index | 109 | parsed from `van_ban_theo_chuyen_khoa.tex` |
| Specialty folders on disk | 27 | measured; 26 indexed sections + unindexed `Trạm y tế` |
| Extractable non-whitespace chars (all files) | 10,098,274 | measured (one run, crashed after) |
| Rough token estimate | ~2.8M (chars ÷ 5 × ~1.4) | go/no-go only, NOT for freeze |

**RESOLVED 2026-08-28.** The multiset difference was exactly:

- present on disk but absent from the index, both under `Trạm y tế`:
  `HD chan doan tram y te xa 20121220.pdf` and
  `VNM_D1_QD so 2919_QD-BYT huong dan kham chua benh tram y te xa.pdf`;
- present in the index but absent from disk:
  `Quyet_dinh_so_3902_QD_BYT_ngay_25_12_2024_...methadone...pdf`.

Therefore `109 - 1 missing + 2 unindexed = 110` source PDFs on disk, plus the root
index PDF gives 111 total. The older provisional count of 112 described a different
snapshot.

**Decision (applied, override if you disagree):** `Trạm y tế` is **in scope** as a
27th specialty. The author's `.tex` index is a bibliography of what one person typed
up, not a scope definition — a folder of genuine, on-disk BYT/SYT guideline PDFs is
evidence of intent to include it, and excluding real content because an index entry
is missing would be the same mistake as trusting the index over the disk anywhere
else in this project. File 3902 (methadone) cannot be restored — it does not exist
anywhere in this working tree, and fetching a substitute from an external portal
risks pulling a different revision than whatever the original author cited — so it
is logged as `indexed_missing` in the manifest (§5) rather than silently dropped or
faked. This has near-zero effect on the active Cardiology work either way: no VM14K
topic in the 34-topic taxonomy maps to `Trạm y tế`, so `specialty_folder()` lookups
for retrieval never touch it; the only real effect is corpus-size reporting.

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

### 3.2 Multi-part documents — CORRECTED 2026-08-28

The "four documents, none exceeds 2 parts, no gaps" claim above was **wrong** —
it was written from filenames alone, without opening the files. Re-audited by
actually reading first/last page text of every `_partNN` file
(`data/interim/moh_corpus_survey.jsonl`, first/last-page snippets):

**18 groups carry a `_partNN` suffix, not 4.** Most turn out to be misleading, not
broken — a `partNN`-suffixed file is very often a **complete, self-contained
document** (own `BỘ Y TẾ` decree header through a references/appendix ending);
the "missing" `part01` was usually just the short one-page decree cover, not
substantive content. Classification after opening every group:

- **17 groups: complete as a single file**, safe to use as one corpus unit despite
  the misleading suffix (its sibling part was never substantive, or the file
  already has both parts and is genuinely a 2-part concat) — includes `2834`
  (HIV, parts 1+2), `2557` (parts 1+2), `2201` (parts 1+2), and 14 more that are
  single `partNN` files starting with a decree header and ending in a references/
  appendix section. Treat `_partNN` in the filename as a naming artifact for
  these, not a signal to go find a missing sibling.
- **1 real gap: `2558`** (Nhãn khoa, diabetic retinopathy diagnosis & management).
  `part01` (25p) is genuinely truncated mid-sentence, mid-image-caption, on its
  last page. `part02`–`part05` do not exist anywhere in the tree. `part06` (20p)
  exists but its extractable text is **only** a repeated clerk watermark stamp
  (`syt_binhdinh_vt_...`), no substantive content — it does not fill the gap.
  **This document is incomplete on disk; flag `content_incomplete` in the
  manifest, do not present it as the full guideline.**

**Action:** for the 17 complete groups, treat the single file as the whole corpus
unit (no concatenation needed — there is nothing to concatenate). For `2558`,
either mark it `content_incomplete` and keep the 25 usable pages with that flag,
or exclude it entirely — pick one before freeze (leaning exclude: 25 pages of an
unknown-length document is a coverage risk, not a usable partial).

### 3.3 Mangled short-names — RESOLVED 2026-08-28

Three files carry Windows 8.3 short-names (`QU25D4~1.PDF`, `QU30C0~1.PDF`,
`QU54DF~1.PDF`). The author's own `.tex` index also only ever recorded the
mangled name (checked directly — no better source there), so the only way to
recover the real title was to open each file and read its own header, exactly as
this section already proposed:

| File | Specialty | Pages | Real title (from the PDF itself) |
|---|---|---:|---|
| `QU25D4~1.PDF` | HIV:AIDS | 26 | *Quy trình kỹ thuật tư vấn về dự phòng lây nhiễm HIV cho người nhiễm HIV và người phơi nhiễm... tại cơ sở y tế* (QĐ-BYT, 2024) — title itself has dropped glyphs on extraction, see §3.5 |
| `QU30C0~1.PDF` | Ung bướu | 33 | *Tài liệu bổ sung hướng dẫn hoạt động dự phòng, sàng lọc, phát hiện sớm và quản lý ung thư vú, ung thư cổ tử cung tại cộng đồng thuộc Đề án 818 đến năm 2030* (kèm QĐ-BYT, 3/2021) |
| `QU54DF~1.PDF` | Ung bướu | 12 | *Phòng chống ung thư vú, ung thư cổ tử cung* — tài liệu tuyên truyền nội bộ Đề án 818 (`dean818k.vn`) |

### 3.5 Garbled-but-not-empty extraction — NEW, OPEN

Two files are more dangerous than the scanned/0-char case §2 already excludes,
because they **do** produce a non-trivial character count and would slip past a
naive char-per-page floor while containing wrong text, not absent text — exactly
the "silent numeric/character corruption" risk §4 already warns about:

- `Truyền nhiễm/Quyet_dinh_so_1856_..._part01.pdf` — extracted text is garbled
  Latin-lookalike glyphs (`"BQYTE CONG HOA xA HOI cmr NGHIA VIET NAM"`), a
  font/ToUnicode mapping failure, not real Vietnamese text.
- `Thận học/Cong_van_so_5544_..._part02.pdf` — 3 pages, similarly garbled
  (`"BÒ Y TẾ CON(J HOÀ..."`, `"...á.h giá ,h,'„ „ă„g thậ„..."`).

Two more files pass the char-count floor trivially because they extract to
**almost nothing but a clerk watermark** (no real corruption risk since there is
effectively no text to be wrong, but also no usable content):
`Nhi khoa/..._2341_..._part02.pdf` and `Truyền nhiễm/Cong_van_so_3874_..._part02.pdf`.

**Action (not yet decided — do not freeze past this):** exclude all four from v1
by default (`garbled_extraction` / `watermark_only` drop reasons, distinct from
`scanned_dropped`), and re-attempt `1856`/`5544` with a different extractor
(`pdfplumber`, or `pymupdf` with `flags=fitz.TEXTFLAGS_TEXT` / a font-remap pass)
only as a deliberate follow-up, verified before it re-enters the corpus.

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

**Coverage check result (run 2026-08-28 against `moh_corpus_survey.jsonl`, floor
tentatively at <50 chars/page — this floor itself is still unvalidated per §8
item 3, so treat this as directional, not final):** `Cấp cứu - Sơ cứu`
(Emergency/First-aid) drops to **zero usable documents** — its one PDF (`636`,
already flagged scanned in §1's original note) fails the floor and there is no
second document to fall back on. If VM14K has emergency-medicine questions,
retrieval grounding for that specialty is structurally impossible under the
current corpus, not a retrieval-quality problem to tune away. Four more
specialties lose one document each but keep usable coverage: `Dinh dưỡng` (2/3),
`HIV` (4/5), `Nhi khoa` (5/6), `Ung bướu` (6/7, before the §3.5 garbled-file
decision is even applied — could drop further).

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

| # | Item | Status |
|---|---|---|
| 1 | Decide scope for 2 unindexed `Trạm y tế` files; restore or log missing file 3902 | **Resolved 2026-08-28** — in scope, 3902 logged `indexed_missing` (§1). Default applied, not a supervisor sign-off; flag if you want it reopened. |
| 2 | Resolve 8.3 short-names to real titles | **Resolved 2026-08-28** (§3.3) |
| 2b | *(new)* Multi-part re-audit — spec's "4 docs, no gaps" claim was wrong | **Resolved 2026-08-28** (§3.2): 18 groups, 1 real gap (`2558`), 17 non-issues |
| 2c | *(new)* Garbled-but-non-empty extraction on 4 files | **Open** (§3.5) — needs an exclude-vs-reextract decision before freeze |
| 3 | Set char/page floor for scanned cutoff | Proposed `<50 chars/page` still unvalidated against the full `moh_corpus_survey.jsonl` distribution — do that pass before relying on it |
| 4 | Confirm any specialty left at zero usable docs | Not yet checked against the final exclusion list (depends on 2c) |
| 5 | Choose intended use (A) vs (B) | **Still open — this is yours to decide**, not a default I should pick. (B) silently creates a second unverified dataset needing full doctor verification; picking it quietly would violate this project's own rule in §6. |
| 6 | Exact token count on final born-digital set | Blocked on 2c + 3 (both change which files count) |

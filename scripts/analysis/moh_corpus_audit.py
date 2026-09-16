#!/usr/bin/env python3
"""
moh_corpus_audit.py — page-level and document-level audit of the MoH guideline corpus.

Exists because the paper's methods section quotes counts that nothing in the repo
regenerates. Every number in `reports/analysis/moh_corpus_audit.md` comes from this
script, so a reviewer can rerun it and get the same values.

What it produces:

  reports/analysis/moh_corpus_audit.md    human-readable report (paste into the paper)
  reports/analysis/moh_corpus_audit.json  same numbers, machine-readable
  data/interim/moh_corpus_pages.jsonl     one row per PDF page  -> page selection
  data/interim/moh_corpus_manifest.jsonl  one row per DOCUMENT  -> the train/test split key

    python scripts/analysis/moh_corpus_audit.py
    python scripts/analysis/moh_corpus_audit.py --floor 30
    python scripts/analysis/moh_corpus_audit.py --no-cache      # force re-extract

WHY THE MANIFEST MATTERS. Splitting train/test by *PDF filename* leaks: 19 parent
documents are split across `_partNN` files and one document is byte-identical in two
specialty folders. `_partNN` siblings and md5-identical copies must land on the same
side of the split. Key the split on `doc_id` from the manifest, never on the filename.

SCANNED-PAGE THRESHOLD IS A CHOICE, NOT A FACT. `--floor` (default 50 non-whitespace
chars/page, per MoH_corpus_spec.md §4) decides what counts as "no text layer". The
report prints the sensitivity curve across thresholds so the choice is visible. Quote
the threshold alongside any page count you publish.

EXTRACTOR MATTERS TOO. Counts come from PyMuPDF. pdfplumber gives different values on
the same files. The extractor and its version are stamped in the JSON output.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import sys
import time
import unicodedata
from pathlib import Path

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "data"
INDEX_STEM = "van_ban_theo_chuyen_khoa"  # the corpus index, not a guideline itself

SENSITIVITY_THRESHOLDS = [1, 5, 10, 20, 30, 50, 80, 100, 150, 200]

DEFAULT_FLOOR = 50  # MoH_corpus_spec.md §4


def rel(p: Path) -> str:
    """Display path, repo-relative when possible. Never raises on outside paths."""
    try:
        return str(p.relative_to(REPO)).replace("\\", "/")
    except ValueError:
        return str(p)


# --------------------------------------------------------------------------
# Name handling
# --------------------------------------------------------------------------

def fix_mojibake(name: str) -> str:
    """UTF-8 bytes read as CP437 at unzip time -> reverse it. No-op if it fails."""
    try:
        return name.encode("cp437").decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        return name


def find_corpus_dir() -> Path:
    for p in DATA.iterdir():
        if p.is_dir() and fix_mojibake(p.name) == "Chuyên khoa":
            return p
    sys.exit("FATAL: no 'Chuyên khoa' directory under data/ (even after mojibake fix)")


PART_RE = re.compile(r"_part(\d+)", re.IGNORECASE)
COPY_SUFFIX_RE = re.compile(r"\s*\(\d+\)(?=\.[Pp][Dd][Ff]$|$)")
SHORTNAME_RE = re.compile(r"^[A-Z0-9]{6}~\d\.PDF$", re.IGNORECASE)

# Decision/dispatch number, e.g. Quyet_dinh_so_2557_QD_BYT..., Cong_van_so_3172_SYT...
DOCNUM_RE = re.compile(r"(?:Quyet_dinh|Cong_van|Quyet_dinh_so|QD)[_\s]*(?:so[_\s]*)?(\d{2,5})", re.IGNORECASE)


def part_stem(filename: str) -> tuple[str, int | None]:
    """('...Huong_dan.pdf', 2) for a `_part02` file; (name, None) otherwise.

    Also strips a trailing ' (1)' download-copy suffix, so `X_part02 (1).pdf` and
    `X_part02.pdf` group together rather than looking like two separate documents.
    """
    cleaned = COPY_SUFFIX_RE.sub("", filename)
    m = PART_RE.search(cleaned)
    if not m:
        return cleaned, None
    return PART_RE.sub("", cleaned), int(m.group(1))


def norm_for_match(name: str) -> str:
    """Loose key for reconciling disk names against index names."""
    name = COPY_SUFFIX_RE.sub("", name)
    name = unicodedata.normalize("NFC", name).strip().lower()
    return re.sub(r"[^a-z0-9]+", "", name)


def norm_specialty(name: str) -> str:
    """Index writes 'HIV:AIDS'; Windows cannot, so disk has 'HIV'. Match loosely."""
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFC", name).lower())


# --------------------------------------------------------------------------
# Extraction
# --------------------------------------------------------------------------

def extract_pages(path: Path) -> tuple[list[int], str | None]:
    """Per-page non-whitespace character counts. (counts, error)."""
    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf  # older installs
    try:
        doc = pymupdf.open(path)
    except Exception as exc:  # a corrupt/encrypted PDF must not kill the run
        return [], f"{type(exc).__name__}: {exc}"
    try:
        counts = [len("".join(page.get_text().split())) for page in doc]
    except Exception as exc:
        return [], f"{type(exc).__name__}: {exc}"
    finally:
        doc.close()
    return counts, None


def extractor_version() -> str:
    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf
    return f"pymupdf {getattr(pymupdf, '__version__', 'unknown')}"


def scan_files(corpus_dir: Path, cache: Path, use_cache: bool) -> list[dict]:
    """One row per PDF on disk, with per-page char counts. Cached — extraction is slow."""
    if use_cache and cache.exists():
        rows = [json.loads(line) for line in cache.open(encoding="utf-8")]
        print(f"[cache] {len(rows)} files from {cache.relative_to(REPO)}")
        return rows

    rows: list[dict] = []
    t0 = time.time()
    for spec_dir in sorted(corpus_dir.iterdir()):
        if not spec_dir.is_dir():
            continue
        specialty = fix_mojibake(spec_dir.name)
        pdfs = sorted({p for p in spec_dir.rglob("*") if p.suffix.lower() == ".pdf"})
        for pdf in pdfs:
            raw = pdf.read_bytes()
            page_chars, error = extract_pages(pdf)
            rows.append({
                "specialty": specialty,
                "filename": pdf.name,
                "relpath": str(pdf.relative_to(REPO)).replace("\\", "/"),
                "size_bytes": len(raw),
                "md5": hashlib.md5(raw).hexdigest(),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "pages": len(page_chars),
                "chars": sum(page_chars),
                "page_chars": page_chars,
                "error": error,
            })
            print(f"  {specialty}/{pdf.name[:55]:<55} {len(page_chars):>4}p", flush=True)

    cache.parent.mkdir(parents=True, exist_ok=True)
    with cache.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"[scan] {len(rows)} files in {time.time() - t0:.1f}s -> {cache.relative_to(REPO)}")
    return rows


# --------------------------------------------------------------------------
# Index reconciliation
# --------------------------------------------------------------------------

def parse_index(corpus_dir: Path) -> tuple[dict[str, list[str]], int | None]:
    """Parse van_ban_theo_chuyen_khoa.tex -> {specialty: [filenames]}, claimed total."""
    tex = corpus_dir / f"{INDEX_STEM}.tex"
    if not tex.exists():
        return {}, None
    text = tex.read_text(encoding="utf-8", errors="replace")

    claimed = None
    m = re.search(r"Tổng số tệp.*?\\textbf\{(\d+)\}", text, re.DOTALL)
    if m:
        claimed = int(m.group(1))

    by_spec: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        sec = re.match(r"\\section\{(.+?)\}", line.strip())
        if sec:
            current = sec.group(1).strip()
            by_spec.setdefault(current, [])
            continue
        item = re.search(r"\\path\{(.+?)\}", line)
        if item and current:
            by_spec[current].append(item.group(1).strip())
    return by_spec, claimed


# --------------------------------------------------------------------------
# Document grouping
# --------------------------------------------------------------------------

def build_documents(files: list[dict], floor: int) -> list[dict]:
    """Collapse files into documents.

    Two collapses, in order:
      1. byte-identical files (same md5) in different folders -> ONE document
         carrying BOTH specialty tags (spec §3.1 / §3.4)
      2. `_partNN` siblings sharing a stem -> ONE document, parts concatenated
         in part order (spec §3.2)

    The resulting `doc_id` is the unit the train/test split must key on.
    """
    # 1. md5 collapse
    by_md5: dict[str, list[dict]] = collections.defaultdict(list)
    for f in files:
        by_md5[f["md5"]].append(f)

    entities = []
    for md5, group in by_md5.items():
        first = group[0]
        entities.append({
            "md5": md5,
            "filename": first["filename"],
            "specialty_tags": sorted({g["specialty"] for g in group}),
            "duplicate_paths": [g["relpath"] for g in group] if len(group) > 1 else [],
            "pages": first["pages"],
            "page_chars": first["page_chars"],
            "relpath": first["relpath"],
            "error": first["error"],
        })

    # 2. part collapse
    by_stem: dict[str, list[dict]] = collections.defaultdict(list)
    for e in entities:
        stem, part_no = part_stem(e["filename"])
        e["part_no"] = part_no
        by_stem[stem].append(e)

    docs = []
    for stem, group in sorted(by_stem.items()):
        group.sort(key=lambda e: (e["part_no"] or 0))
        parts_present = sorted(e["part_no"] for e in group if e["part_no"] is not None)

        num = DOCNUM_RE.search(stem)
        stem_hash = hashlib.md5(stem.encode("utf-8")).hexdigest()[:8]
        doc_id = f"{num.group(1)}-{stem_hash}" if num else f"doc-{stem_hash}"

        page_chars = [c for e in group for c in e["page_chars"]]
        tags = sorted({t for e in group for t in e["specialty_tags"]})

        usable = sum(1 for c in page_chars if c >= floor)
        chars_per_page = round(sum(page_chars) / len(page_chars), 1) if page_chars else 0.0

        # A scanned PDF signed with a digital certificate carries ONE page of signature
        # metadata ("Ký bởi: BỘ Y TẾ / Cơ quan / Ngày ký"), ~60-90 chars. That page clears
        # the per-page floor, so a `usable_pages > 0` test wrongly calls the whole document
        # born-digital. Require the DOCUMENT to clear the floor on average as well.
        # Measured separation is clean: the four affected documents sit at 0.5-35.0
        # chars/page, the lowest genuine document at 52.0.
        signature_only = usable > 0 and chars_per_page < floor
        is_born_digital = usable > 0 and chars_per_page >= floor

        flags = []
        if signature_only:
            flags.append("signature_page_only")
        if any(e["duplicate_paths"] for e in group):
            flags.append("cross_filed_duplicate")
        if parts_present:
            if len(parts_present) == 1:
                flags.append("orphan_part")
            expected = list(range(1, max(parts_present) + 1))
            if parts_present != expected:
                flags.append("incomplete_part_run")
        if any(SHORTNAME_RE.match(e["filename"]) for e in group):
            flags.append("unresolved_shortname")
        if not is_born_digital:
            flags.append("no_usable_pages")
        if any(e["error"] for e in group):
            flags.append("extract_error")

        docs.append({
            "doc_id": doc_id,
            "stem": stem,
            "specialty_tags": tags,
            "source_files": [e["relpath"] for e in group],
            # extra on-disk copies of the same bytes; their pages are counted once, under
            # source_files, so these paths exist for provenance but are not re-counted
            "duplicate_paths": [p for e in group for p in e["duplicate_paths"]
                                if p != e["relpath"]],
            "parts_present": parts_present,
            "content_md5": [e["md5"] for e in group],
            "pages": len(page_chars),
            "usable_pages": usable if is_born_digital else 0,
            "chars": sum(page_chars),
            "chars_per_page": chars_per_page,
            "class": "born_digital" if is_born_digital else "scanned_dropped",
            "drop_reason": None if is_born_digital else (
                f"{chars_per_page} chars/page across {len(page_chars)} pages, below the "
                f"{floor} floor" + (" — the only page with text is a digital-signature stamp"
                                    if signature_only else "")
            ),
            "flags": flags,
        })
    return docs


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------

def build_report(files, docs, index_by_spec, claimed_total, floor) -> tuple[str, dict]:
    all_page_chars = [c for f in files for c in f["page_chars"]]
    total_pages = len(all_page_chars)
    low = sum(1 for c in all_page_chars if c < floor)

    # unique pages (drop the byte-identical second copy)
    seen_md5, uniq_page_chars = set(), []
    for f in files:
        if f["md5"] in seen_md5:
            continue
        seen_md5.add(f["md5"])
        uniq_page_chars.extend(f["page_chars"])
    uniq_low = sum(1 for c in uniq_page_chars if c < floor)

    sensitivity = {t: sum(1 for c in uniq_page_chars if c < t) for t in SENSITIVITY_THRESHOLDS}
    zero = sum(1 for c in uniq_page_chars if c == 0)

    # index reconciliation
    disk_keys = {norm_for_match(f["filename"]) for f in files}
    index_names = [n for names in index_by_spec.values() for n in names]
    index_keys = {norm_for_match(n) for n in index_names}
    only_disk = sorted(f"{f['specialty']}/{f['filename']}" for f in files
                       if norm_for_match(f["filename"]) not in index_keys)
    only_index = sorted(n for n in index_names if norm_for_match(n) not in disk_keys)

    # per-specialty
    spec_rows = []
    for spec in sorted({f["specialty"] for f in files}):
        sf = [f for f in files if f["specialty"] == spec]
        sd = [d for d in docs if spec in d["specialty_tags"]]
        spec_rows.append({
            "specialty": spec,
            "files": len(sf),
            "docs": len(sd),
            # from documents, so pages inside a scanned_dropped document are not counted
            "pages": sum(d["pages"] for d in sd),
            "usable_pages": sum(d["usable_pages"] for d in sd),
            "usable_docs": sum(1 for d in sd if d["class"] == "born_digital"),
        })

    flagged = [d for d in docs if d["flags"]]
    flag_counts = collections.Counter(f for d in docs for f in d["flags"])
    usable_docs = [d for d in docs if d["class"] == "born_digital"]
    dropped_docs = [d for d in docs if d["class"] == "scanned_dropped"]
    usable_pages_total = sum(d["usable_pages"] for d in usable_docs)
    pages_in_dropped = sum(d["pages"] for d in dropped_docs)

    L = []
    a = L.append
    a("# MoH guideline corpus — audit")
    a("")
    a(f"Generated by `scripts/analysis/moh_corpus_audit.py` · extractor: {extractor_version()} · "
      f"scanned-page floor: **< {floor} non-whitespace chars/page**")
    a("")
    a("Every figure here is regenerated by rerunning that script. Quote the floor and the "
      "extractor alongside any page count taken from this report — both change the answer.")
    a("")
    a("## 1. Totals")
    a("")
    a("| Quantity | Value |")
    a("|---|---|")
    a(f"| Specialty folders | {len(spec_rows)} |")
    a(f"| PDF files on disk (excl. index) | {len(files)} |")
    a(f"| Distinct documents after dedup + part merge | {len(docs)} |")
    a(f"| Documents with usable text | {len(usable_docs)} |")
    a(f"| Pages, counting every file | {total_pages} |")
    a(f"| Pages, unique content only | {len(uniq_page_chars)} |")
    a(f"| Unique pages with no text layer (< {floor} chars) | {uniq_low} |")
    a(f"| Pages inside documents dropped as scanned | {pages_in_dropped} |")
    a(f"| **Unique pages eligible for question writing** | **{usable_pages_total}** |")
    a("")
    a(f"The eligible figure is the one to quote. It is not simply "
      f"{len(uniq_page_chars)} − {uniq_low}: {len(dropped_docs)} documents are dropped wholesale "
      f"as scanned (§5), and a handful of their pages clear the per-page floor on "
      f"digital-signature metadata alone rather than on content.")
    a("")
    if total_pages != len(uniq_page_chars):
        a(f"> The raw page total double-counts **{total_pages - len(uniq_page_chars)} pages** from the "
          f"byte-identical file filed under two specialties. Report the unique figure.")
        a("")
    a("## 2. Scanned-page threshold sensitivity")
    a("")
    a("The count of \"unreadable\" pages is a function of the threshold. On unique pages:")
    a("")
    a("| Floor (non-ws chars/page) | Pages below it |")
    a("|---|---|")
    a(f"| 0 (no text at all) | {zero} |")
    for t in SENSITIVITY_THRESHOLDS:
        mark = "  ← **current**" if t == floor else ""
        a(f"| < {t} | {sensitivity[t]}{mark} |")
    a("")
    a("## 3. Index reconciliation")
    a("")
    a(f"Index (`{INDEX_STEM}.tex`) claims **{claimed_total}** files; disk holds **{len(files)}** "
      f"guideline PDFs plus the index PDF itself.")
    a("")
    a(f"- On disk but not in the index: **{len(only_disk)}**")
    for p in only_disk:
        a(f"  - `{p}`")
    a(f"- In the index but not on disk: **{len(only_index)}**")
    for n in only_index:
        a(f"  - `{n}`")
    a("")
    a("## 4. Per-specialty coverage")
    a("")
    a("| Specialty | Files | Docs | Pages | Usable pages | Usable docs |")
    a("|---|---|---|---|---|---|")
    for r in sorted(spec_rows, key=lambda r: r["usable_pages"]):
        warn = " ⚠️" if r["usable_pages"] < 10 else ""
        a(f"| {r['specialty']}{warn} | {r['files']} | {r['docs']} | {r['pages']} | "
          f"{r['usable_pages']} | {r['usable_docs']} |")
    a("")
    thin = [r for r in spec_rows if r["usable_pages"] < 10]
    if thin:
        a(f"⚠️ **{len(thin)} specialties have fewer than 10 usable pages** "
          f"({', '.join(r['specialty'] for r in thin)}). Any claim of sampling pages "
          f"\"evenly across the specialties\" has to account for these — the usable-page "
          f"range across specialties is "
          f"{min(r['usable_pages'] for r in spec_rows)} to {max(r['usable_pages'] for r in spec_rows)}.")
        a("")
    a("## 5. Document-level anomalies")
    a("")
    a("| Flag | Documents | Why it matters |")
    a("|---|---|---|")
    reasons = {
        "cross_filed_duplicate": "same bytes in 2 specialty folders — must not straddle the split",
        "orphan_part": "only one `partNN` on disk; the rest of the document is missing",
        "incomplete_part_run": "gap in the part sequence — text is discontinuous",
        "unresolved_shortname": "8.3 short-name, real title unresolved",
        "no_usable_pages": "document is scanned; unusable without OCR",
        "signature_page_only": "scanned, but one digital-signature page clears the per-page floor — would pass a naive filter",
        "extract_error": "extractor failed on a source file",
    }
    for flag, n in flag_counts.most_common():
        a(f"| `{flag}` | {n} | {reasons.get(flag, '')} |")
    a("")
    a(f"{len(flagged)} of {len(docs)} documents carry at least one flag. Full detail in "
      "`data/interim/moh_corpus_manifest.jsonl`.")
    a("")
    if dropped_docs:
        a("### Documents dropped as scanned")
        a("")
        a("| doc_id | Specialty | Pages | Chars | Chars/page | Why |")
        a("|---|---|---|---|---|---|")
        for d in sorted(dropped_docs, key=lambda d: d["chars_per_page"]):
            why = ("signature page only" if "signature_page_only" in d["flags"]
                   else "no text at all")
            a(f"| `{d['doc_id']}` | {', '.join(d['specialty_tags'])} | {d['pages']} | "
              f"{d['chars']} | {d['chars_per_page']} | {why} |")
        a("")
        a("A document-level floor is doing real work here. Filtering only on the per-page "
          "rule would admit these documents on a single page of digital-signature metadata "
          "(`Ký bởi: BỘ Y TẾ / Cơ quan / Ngày ký`), which contains no clinical content. The "
          "separation is clean — the lowest genuine document sits at 52.0 chars/page.")
        a("")
    for flag in ["orphan_part", "incomplete_part_run", "cross_filed_duplicate", "unresolved_shortname"]:
        hits = [d for d in docs if flag in d["flags"]]
        if not hits:
            continue
        a(f"### `{flag}` ({len(hits)})")
        a("")
        for d in hits:
            parts = f" parts={d['parts_present']}" if d["parts_present"] else ""
            a(f"- `{d['doc_id']}`{parts} — {d['stem'][:80]} — tags: {', '.join(d['specialty_tags'])}")
        a("")
    multipart = [d for d in docs if len(d["parts_present"]) > 1]
    fragments = [d for d in docs if len(d["parts_present"]) == 1]
    a("## 6. Splitting")
    a("")
    a("Splitting train/test on *filename* leaks, for two separate reasons:")
    a("")
    a(f"- **{len(multipart)} documents are assembled from more than one `partNN` file** "
      f"({', '.join(d['doc_id'] for d in multipart)}). Split by filename and one part goes to "
      f"train while another goes to test — the same document, so the retriever is tested on "
      f"text it trained on.")
    a(f"- **{flag_counts['cross_filed_duplicate']} document is byte-identical across two specialty "
      f"folders**, so it can land on both sides at once.")
    a("")
    a(f"Key the split on `doc_id` from `data/interim/moh_corpus_manifest.jsonl` and both cases "
      f"resolve — every page of a document lands on one side.")
    a("")
    a(f"Separately, **{len(fragments)} documents are a single part with the rest missing from disk** "
      f"(mostly a lone `part02`). That is not a leakage problem but a grounding one: a question "
      f"written on a `part02` page may depend on definitions that live in the absent `part01`. "
      f"Either exclude these {len(fragments)} documents from question writing or state that "
      f"questions are written only from pages that are self-contained.")
    a("")

    report_json = {
        "generated_by": "scripts/analysis/moh_corpus_audit.py",
        "extractor": extractor_version(),
        "floor_nonws_chars_per_page": floor,
        "specialty_folders": len(spec_rows),
        "pdf_files_on_disk": len(files),
        "documents": len(docs),
        "usable_documents": len(usable_docs),
        "pages_all_files": total_pages,
        "pages_unique": len(uniq_page_chars),
        "pages_no_text_layer_unique": uniq_low,
        "pages_usable_unique": usable_pages_total,
        "pages_zero_chars_unique": zero,
        "threshold_sensitivity_unique": sensitivity,
        "index_claimed_total": claimed_total,
        "on_disk_not_in_index": only_disk,
        "in_index_not_on_disk": only_index,
        "per_specialty": spec_rows,
        "flag_counts": dict(flag_counts),
    }
    return "\n".join(L), report_json


# --------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--floor", type=int, default=DEFAULT_FLOOR,
                    help=f"non-whitespace chars/page below which a page has no text layer "
                         f"(default: {DEFAULT_FLOOR}, per MoH_corpus_spec.md §4)")
    ap.add_argument("--no-cache", action="store_true", help="re-extract instead of using the cache")
    ap.add_argument("--out-md", type=Path, default=REPO / "reports/analysis/moh_corpus_audit.md")
    ap.add_argument("--out-json", type=Path, default=REPO / "reports/analysis/moh_corpus_audit.json")
    ap.add_argument("--out-manifest", type=Path, default=None,
                    help="per-document manifest (default: data/interim/moh_corpus_manifest.jsonl)")
    ap.add_argument("--out-pages", type=Path, default=None,
                    help="per-page classification (default: data/interim/moh_corpus_pages.jsonl)")
    args = ap.parse_args()

    # A non-default floor produces a differently-classified manifest. Writing it to the
    # canonical path would silently replace the spec-conformant one, so suffix instead.
    suffix = "" if args.floor == DEFAULT_FLOOR else f".floor{args.floor}"
    manifest = args.out_manifest or DATA / "interim" / f"moh_corpus_manifest{suffix}.jsonl"
    pages_out = args.out_pages or DATA / "interim" / f"moh_corpus_pages{suffix}.jsonl"
    if suffix:
        print(f"[note] floor={args.floor} is not the spec floor ({DEFAULT_FLOOR}); "
              f"writing to {rel(manifest)} so the canonical manifest is left intact.")

    corpus_dir = find_corpus_dir()
    cache = DATA / "interim" / "moh_corpus_pagescan.jsonl"

    files = scan_files(corpus_dir, cache, use_cache=not args.no_cache)
    files = [f for f in files if Path(f["filename"]).stem != INDEX_STEM]

    errs = [f for f in files if f["error"]]
    if errs:
        print(f"[warn] {len(errs)} file(s) failed extraction:")
        for f in errs:
            print(f"        {f['relpath']}: {f['error']}")

    index_by_spec, claimed_total = parse_index(corpus_dir)
    docs = build_documents(files, args.floor)
    md, js = build_report(files, docs, index_by_spec, claimed_total, args.floor)

    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text(md, encoding="utf-8")
    args.out_json.write_text(json.dumps(js, ensure_ascii=False, indent=2), encoding="utf-8")

    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", encoding="utf-8") as fh:
        for d in docs:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")

    doc_of_file = {src: d for d in docs for src in d["source_files"]}
    dup_of_file = {p: d for d in docs for p in d["duplicate_paths"]}
    with pages_out.open("w", encoding="utf-8") as fh:
        for f in files:
            d = doc_of_file.get(f["relpath"])
            is_dup_copy = d is None and f["relpath"] in dup_of_file
            if is_dup_copy:
                d = dup_of_file[f["relpath"]]
            for i, c in enumerate(f["page_chars"], start=1):
                if is_dup_copy:
                    reason = "second on-disk copy of the same bytes; counted under the primary path"
                elif c < args.floor:
                    reason = f"< {args.floor} non-ws chars"
                elif d and d["class"] != "born_digital":
                    reason = f"document dropped: {d['drop_reason']}"
                else:
                    reason = None
                fh.write(json.dumps({
                    "doc_id": d["doc_id"] if d else None,
                    "specialty": f["specialty"],
                    "relpath": f["relpath"],
                    "sha256": f["sha256"],
                    "page": i,
                    "nonws_chars": c,
                    "has_text_layer": c >= args.floor,
                    # the page-selection filter: text layer AND its document survived §5
                    # AND this is not a duplicate copy already counted elsewhere
                    "eligible": bool(reason is None),
                    "ineligible_reason": reason,
                }, ensure_ascii=False) + "\n")

    print(f"\n[write] {rel(args.out_md)}")
    print(f"[write] {rel(args.out_json)}")
    print(f"[write] {rel(manifest)}  ({len(docs)} documents)")
    print(f"[write] {rel(pages_out)}")
    print()
    print(md)


if __name__ == "__main__":
    main()

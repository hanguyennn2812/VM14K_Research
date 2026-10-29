#!/usr/bin/env python3
"""Survey every PDF under data/Chuyên khoa/: hash, page count, extractable chars.

Read-only audit step feeding the corpus manifest freeze described in
data/MoH_corpus_spec.md. Does not resolve parts, dedupe, or classify — it only
measures. Output is regenerable, so it is written under data/interim/ (gitignored).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "interim" / "moh_corpus_survey.jsonl"


def fix_mojibake(name: str) -> str:
    """Recover UTF-8 names decoded through the legacy Windows CP437 path."""
    try:
        return name.encode("cp437").decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        return name


def specialty_parent() -> Path:
    candidates = [p for p in (ROOT / "data").iterdir() if p.is_dir()]
    parents = [p for p in candidates if "khoa" in fix_mojibake(p.name).casefold()]
    if len(parents) != 1:
        raise RuntimeError(f"expected one specialty parent, found {len(parents)}: {parents}")
    return parents[0]


def survey() -> list[dict]:
    parent = specialty_parent()
    records: list[dict] = []
    for folder in sorted(parent.iterdir(), key=lambda p: fix_mojibake(p.name)):
        if not folder.is_dir():
            continue
        specialty = fix_mojibake(folder.name)
        pdfs = sorted(set(folder.rglob("*.pdf")) | set(folder.rglob("*.PDF")))
        for pdf in pdfs:
            if not pdf.is_file():
                continue
            raw = pdf.read_bytes()
            md5 = hashlib.md5(raw).hexdigest()
            sha256 = hashlib.sha256(raw).hexdigest()
            try:
                doc = fitz.open(stream=raw, filetype="pdf")
                pages = doc.page_count
                chars = sum(len(page.get_text().strip()) for page in doc)
                first_page = doc[0].get_text()[:200] if pages else ""
                last_page = doc[-1].get_text()[-200:] if pages else ""
                doc.close()
                error = None
            except Exception as exc:  # noqa: BLE001 - record and move on
                pages, chars, first_page, last_page = 0, 0, "", ""
                error = repr(exc)
            records.append(
                {
                    "specialty": specialty,
                    "filename": fix_mojibake(pdf.name),
                    "raw_name_on_disk": pdf.name,
                    "size_bytes": len(raw),
                    "md5": md5,
                    "sha256": sha256,
                    "pages": pages,
                    "chars": chars,
                    "chars_per_page": round(chars / pages, 1) if pages else 0.0,
                    "first_page_snippet": first_page,
                    "last_page_snippet": last_page,
                    "error": error,
                }
            )
    return records


def main() -> None:
    records = survey()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"wrote {len(records)} records to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

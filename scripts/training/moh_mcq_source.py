"""Conservative, provenance-preserving sources for MCQ generation (not RAG retrieval).

Keep page/section boundaries and reject table pages rather than flattening their cells.
No OCR corrections or disease names are invented here. Normalisation is Unicode NFC only.
"""
import collections
import hashlib
import re
import unicodedata
from pathlib import Path

import pymupdf

from rag_moh import SCOPES
from moh_corpus_audit import fix_mojibake
from run_eval import REPO_ROOT


def fold(text):
    text = unicodedata.normalize("NFD", text.lower().replace("đ", "d"))
    return " ".join("".join(c for c in text if not unicodedata.combining(c)).split())


def accent_ratio(text):
    letters = [c for c in unicodedata.normalize("NFC", text) if c.isalpha()]
    return sum(c.lower() == "đ" or any(unicodedata.combining(x) for x in
               unicodedata.normalize("NFD", c)) for c in letters) / max(len(letters), 1)


def text_problem(text):
    # Greek symbols, units and Latin scientific names are legitimate. Other scripts are not.
    for c in unicodedata.normalize("NFKC", text):
        if c.isalpha() and not any(n in unicodedata.name(c, "") for n in ("LATIN", "GREEK")):
            return "foreign_script"
    if "\ufffd" in text:
        return "replacement_character"
    if accent_ratio(text) < 0.06:
        return "low_vietnamese_accents"
    if len(re.findall(r"[A-Za-zÀ-ỹ][~?][A-Za-zÀ-ỹ]|[A-Za-z][046][A-Za-z]", text)) >= 3:
        return "broken_ocr"
    return None


def document_problem(title, text):
    title = fold(title.replace("_", " "))
    if "giam sat" in title:
        return "surveillance_document"
    if "xet nghiem moi hiv" in title and "su dung so lieu" in title:
        return "incidence_surveillance_document"
    if "danh muc" in title or "cong van" in title:
        return "administrative_document"
    # A stray glyph should quarantine its page, not an otherwise readable 474-page guideline.
    return "low_vietnamese_accents" if accent_ratio(text) < 0.06 else None


def page_lines(page):
    out = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            spans = line["spans"]
            text = unicodedata.normalize("NFC", "".join(s["text"] for s in spans)).strip()
            if not text or text.isdigit() or "syt_binhdinh" in text.lower():
                continue
            out.append({"text": text, "size": max(s["size"] for s in spans),
                        "bold": any("bold" in s["font"].lower() for s in spans),
                        "bbox": line["bbox"]})
    return out


def table_page(page, lines):
    # Detect bordered tables and borderless columns. Dropping the whole page is conservative.
    if len(page.get_drawings()) >= 6 and page.find_tables().tables:
        return True
    by_y = collections.defaultdict(list)
    for line in lines:
        by_y[round(line["bbox"][1] / 4)].append(line)
    return sum(len(row) >= 3 for row in by_y.values()) >= 3


def section_title(line):
    t = line["text"]
    return (line["bold"] and line["size"] >= 15 and t.isupper()
            and len(t.split()) >= 2 and not re.match(r"^[\dIVX]+[.)]", t)
            and not any(s in fold(t) for s in ("huong dan", "chan doan", "bo y te", "quyet dinh",
                                               "cong hoa", "doc lap", "dieu tri", "muc luc")))


def cover_title(pdf, fallback):
    """Copy clinical cover headings, with accents, instead of relying on ASCII filenames."""
    for page in list(pdf)[:3]:
        lines = page_lines(page)
        headings = [l["text"] for l in lines if l["bold"] and l["size"] >= 14
                    and l["text"].isupper() and len(l["text"].split()) >= 2
                    and not re.match(r"^[\dIVX]+[.)]", l["text"])]
        text = " ".join(headings)
        if any(term in fold(text) for term in ("chan doan", "dieu tri", "phong benh", "du phong")):
            return text
    return fallback


def generation_chunks(folders=None):
    """Return (chunks, audit). IDs include PDF hash, 1-based page and page-local segment."""
    folders = SCOPES["infect"][0] if folders is None else folders
    root = next(p for p in Path(REPO_ROOT, "data").iterdir() if fix_mojibake(p.name) == "Chuyên khoa")
    chunks, audit, seen = [], {"documents": [], "rejected_pages": collections.Counter()}, set()
    for folder in sorted(root.iterdir()):
        if not folder.is_dir() or fix_mojibake(folder.name) not in folders:
            continue
        for path in sorted(folder.rglob("*.pdf")):
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest in seen:
                continue
            seen.add(digest)
            title = fix_mojibake(path.stem).replace("_", " ")
            info = {"doc_id": digest[:10], "source_path": path.relative_to(REPO_ROOT).as_posix(),
                    "title": title, "chunks": 0}
            with pymupdf.open(path) as pdf:
                raw = "\n".join(p.get_text() for p in pdf)
                problem = document_problem(title, raw)
                if problem:
                    info["rejected"] = problem
                    audit["documents"].append(info)
                    continue
                guideline = cover_title(pdf, title)
                heading = ""
                disease_heading = ""
                for page_no, page in enumerate(pdf, 1):
                    lines = page_lines(page)
                    # Update a disease/chapter heading even on a rejected page, for continuation pages.
                    titles = [l["text"] for l in lines if section_title(l)]
                    # Large multi-disease textbooks need their disease chapter carried forward.
                    if titles and len(pdf) > 200:
                        disease_heading = " ".join(titles)
                    section_lines = [l["text"] for l in lines if l["bold"] and len(l["text"]) < 160
                                     and re.match(r"^\d+(?:\.\d+)*[.)]\s*\D", l["text"])]
                    if section_lines:
                        heading = section_lines[-1]
                    body = "\n".join(l["text"] for l in lines)
                    reason = ("administrative_section" if any(s in fold(heading) for s in
                              ("trach nhiem", "to chuc thuc hien", "phan cap", "bao cao", "bieu mau")) else
                              "contents_or_references" if re.search(r"mục lục|tài liệu tham khảo|\.{5}", body, re.I)
                              else text_problem(body))
                    if not reason and table_page(page, lines):
                        reason = "table_page"
                    if not reason and (len(body.split()) < 65 or not re.search(
                            r"chẩn đoán|triệu chứng|điều trị|lâm sàng|liều|biến chứng|dự phòng|phòng bệnh", body, re.I)):
                        reason = "no_clinical_prose"
                    if reason:
                        audit["rejected_pages"][reason] += 1
                        continue
                    # A page cannot straddle diseases in this pilot. Retain line breaks and complete lines.
                    if len(titles) > 2:
                        audit["rejected_pages"]["multiple_headings"] += 1
                        continue
                    segments, current = [], []
                    for line in lines:
                        if sum(len(l.split()) for l in current) >= 360:
                            segments.append("\n".join(current))
                            current = []
                        current.append(line["text"])
                    if current:
                        if segments and len(" ".join(current).split()) < 65:
                            segments[-1] += "\n" + "\n".join(current)
                        else:
                            segments.append("\n".join(current))
                    for k, segment in enumerate(segments):
                        section = " / ".join(s for s in (disease_heading, heading) if s)
                        context = (f"Văn bản: {title}\nTiêu đề hướng dẫn: {guideline}\n"
                                   f"Mục/bệnh: {section or guideline}\nTrang PDF: {page_no}\n\n{segment}")
                        chunks.append({"id": f"{digest[:10]}:p{page_no}:s{k}", "doc_id": digest[:10],
                                       "doc": title, "guideline_title": guideline, "section": section, "page": page_no,
                                       "source_path": info["source_path"], "raw_text": segment, "text": context})
                        info["chunks"] += 1
            audit["documents"].append(info)
    audit["rejected_pages"] = dict(audit["rejected_pages"])
    audit["chunks"] = len(chunks)
    return chunks, audit


def balanced_sample(chunks, count, seed):
    import random
    rng, groups = random.Random(seed), collections.defaultdict(list)
    for chunk in chunks:
        groups[chunk["doc_id"]].append(chunk)
    docs = sorted(groups)
    rng.shuffle(docs)
    for rows in groups.values():
        rng.shuffle(rows)
    sample = []
    while len(sample) < count and any(groups.values()):
        for doc in docs:
            if groups[doc] and len(sample) < count:
                sample.append(groups[doc].pop())
    return sample

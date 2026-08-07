#!/usr/bin/env python3
"""
propose_topic_mapping.py — build a topic-canonicalisation PROPOSAL for human review.

Reads data/cleaned/clean_final.jsonl, collects every distinct `medical_topic`
string with its row frequency, and proposes a target among the paper's 34
canonical specialties (VM14K arXiv 2506.01305, Table 5 / Appendix A).

Writes reports/analysis/topic_mapping_proposed.csv. Applies NOTHING — the
dataset is never opened for writing. Every AUTO/AMBIGUOUS/JUNK call below is a
proposal that a human must sign off on before any mapping is applied, per
HANDOFF.md §6 ("Write the mapping table by hand, then apply it programmatically").

    python scripts/analysis/propose_topic_mapping.py
"""
from __future__ import annotations

import collections
import csv
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from dedup_utils import normalize_vietnamese

DATA_PATH = REPO_ROOT / "data" / "cleaned" / "clean_final.jsonl"
OUT_PATH = REPO_ROOT / "reports" / "analysis" / "topic_mapping_proposed.csv"


# --------------------------------------------------------------------------
# The paper's 34 canonical specialties — Table 5 / Appendix A, verbatim.
# --------------------------------------------------------------------------

CANONICAL_34 = [
    "Allergy and Immunology",
    "Anesthesiology",
    "Cardiology",
    "Dermatology",
    "Endocrinology",
    "Gastroenterology",
    "Geriatrics",
    "Hematology",
    "Infectious Diseases",
    "Internal Medicine",
    "Nephrology",
    "Neurology",
    "Nuclear Medicine",
    "Obstetrics and Gynecology",
    "Oncology",
    "Ophthalmology",
    "Orthopedics",
    "Otolaryngology",
    "Palliative Medicine",
    "Pathology",
    "Pediatrics",
    "Physical Medicine and Rehabilitation",
    "Psychiatry",
    "Pulmonology",
    "Radiology",
    "Rheumatology",
    "Sports Medicine",
    "Surgery",
    "Urology",
    "General Medicine",
    "Eastern Medicine",
    "Public Health",
    "Preventive Healthcare",
    "Emergency Medicine",
]
assert len(CANONICAL_34) == 34, f"expected 34 canonical names, got {len(CANONICAL_34)}"

# Normalised canonical name -> original canonical name. normalize_vietnamese is
# the authors' normaliser (strips punctuation + diacritics, lowercases), so it
# absorbs case/spacing/punctuation differences for the closeness comparison.
# The ORIGINAL raw string is always what gets written to the CSV.
CANON_BY_NORM = {normalize_vietnamese(c): c for c in CANONICAL_34}


# --------------------------------------------------------------------------
# AUTO — close variants: typo, wording, standard synonym, or an established
# subspecialty that unambiguously rolls up into exactly one canonical name.
# --------------------------------------------------------------------------

AUTO_MAP: dict[str, tuple[str, str]] = {
    "Infection Diseases": ("Infectious Diseases", "typo; cited verbatim in HANDOFF.md §6"),
    "Preventive Medicine": ("Preventive Healthcare", "wording variant of the same concept"),
    "Accident and Emergency": ("Emergency Medicine", "standard UK/Commonwealth synonym"),
    "Family Medicine": ("General Medicine", "standard synonym for primary/general care"),
    "Immunology": ("Allergy and Immunology", "canonical name already contains this term"),
    "Hepatology": ("Gastroenterology", "established subspecialty of GI"),
    "Neonatology": ("Pediatrics", "established subspecialty of paediatrics"),
    "Interventional Cardiology": ("Cardiology", "established subspecialty of cardiology"),
    "Vascular Surgery": ("Surgery", "established surgical subspecialty"),
}


# --------------------------------------------------------------------------
# JUNK — not a medical specialty at all: placeholders, agencies, process words,
# administrative/meta topics. Nothing to map onto the clinical taxonomy.
# --------------------------------------------------------------------------

JUNK_NOTES: dict[str, str] = {
    "Other(No Category)": "explicit no-category placeholder",
    "FDA": "regulatory agency, not a specialty",
    "Classification": "process word, not a specialty",
    "Diagnosis": "process word, not a specialty",
    "Diagnostic Testing": "process word, not a specialty",
    "Diagnostic Medicine": "process word, not a specialty",
    "Physical Examination": "clinical procedure, not a specialty",
    "Etiology": "concept word, not a specialty",
    "Research": "activity, not a specialty",
    "Clinical Research": "activity, not a specialty",
    "Risk Assessment": "activity, not a specialty",
    "Patient Safety": "quality-improvement domain, not a specialty",
    "Communication Skills": "training topic, not a specialty",
    "History of Medicine": "academic subject, not a specialty",
    "Medical Ethics": "academic subject, not a specialty",
    "Demographics": "academic subject, not a specialty",
    "Sociology": "academic subject, not a specialty",
    "Health Economics": "health-systems domain, not a clinical specialty",
    "Health Management": "health-systems domain, not a clinical specialty",
    "Health Administration": "health-systems domain, not a clinical specialty",
    "Health Policy": "health-systems domain, not a clinical specialty",
    "Health System": "health-systems domain, not a clinical specialty",
    "Pharmaceutical": "adjective fragment, not a specialty name",
}


# --------------------------------------------------------------------------
# AMBIGUOUS — a real medical/scientific domain, but NOT clearly one of the 34.
# Second element is a best-guess nearest canonical, or "" where forcing one
# would destroy information. A human must decide; see the summary printout.
# --------------------------------------------------------------------------

AMBIGUOUS_GUESS: dict[str, tuple[str, str]] = {
    # --- basic / preclinical sciences: high volume, no clinical home in the 34
    "Pharmacology": ("", "preclinical science; no canonical target — taxonomy gap"),
    "Toxicology": ("", "preclinical science; no canonical target — taxonomy gap"),
    "Medical Toxicology": ("", "merge with Toxicology first; no canonical target"),
    "Anatomy": ("", "preclinical science; no canonical target — taxonomy gap"),
    "Physiology": ("", "preclinical science; no canonical target — taxonomy gap"),
    "Biochemistry": ("", "preclinical science; no canonical target — taxonomy gap"),
    "Embryology": ("", "preclinical science; no canonical target — taxonomy gap"),
    "Histology": ("Pathology", "microscopic anatomy; closest clinical home is Pathology"),
    "Cell Biology": ("", "merge with Cellular Biology; no canonical target"),
    "Cellular Biology": ("", "merge with Cell Biology (HANDOFF.md §6 cites this pair)"),
    "Molecular Biology": ("", "preclinical science; no canonical target"),
    "Genetics": ("", "preclinical science; no canonical target — taxonomy gap"),
    "Genetic": ("", "fragment of Genetics; merge first, then decide"),
    "Medical Genetics": ("", "merge with Genetics; no canonical target"),
    "Genetic Disorders": ("", "merge with Genetics; no canonical target"),
    "Genetic Engineering": ("", "merge with Genetics; no canonical target"),
    "Teratology": ("", "developmental toxicology; no canonical target"),
    "Chemistry": ("", "not a medical subject at all — candidate for JUNK instead"),
    "Analytical Chemistry": ("", "not a medical subject — candidate for JUNK instead"),
    "Industrial Chemistry": ("", "not a medical subject — candidate for JUNK instead"),
    "Physics": ("", "not a medical subject — candidate for JUNK instead"),
    "Botany": ("", "not a medical subject; may relate to Eastern Medicine herbs"),
    "Entomology": ("", "may relate to Parasitology/vector-borne disease"),
    # --- microbiology family
    "Microbiology": ("", "preclinical science; overlaps Infectious Diseases"),
    "Medical Microbiology": ("", "merge with Microbiology first"),
    "Virology": ("", "merge with Microbiology, or roll into Infectious Diseases"),
    "Parasitology": ("", "preclinical science; overlaps Infectious Diseases"),
    "Infection Control": ("Public Health", "practice domain spanning ID and Public Health"),
    "Epidemiology": ("Public Health", "core Public Health discipline"),
    # --- dentistry family: entirely absent from the 34
    "Dentistry": ("", "dentistry has NO canonical target in the 34 — taxonomy gap"),
    "General Dentistry": ("", "merge with Dentistry; no canonical target"),
    "Periodontology": ("", "merge with Periodontics; no canonical target"),
    "Periodontics": ("", "merge with Periodontology; no canonical target"),
    "Endodontics": ("", "dental subspecialty; no canonical target"),
    "Prosthodontics": ("", "dental subspecialty; no canonical target"),
    "Oral and Maxillofacial Surgery": ("Surgery", "surgical, but dental-adjacent — judgement call"),
    # --- clinical domains that plausibly roll up, but not unambiguously
    "Neurosurgery": ("Surgery", "could equally roll into Neurology — judgement call"),
    "Transplant": ("Surgery", "fragment; likely transplant surgery"),
    "Critical Care": ("", "merge with Intensive Care*; no canonical target"),
    "Intensive Care": ("", "HANDOFF.md §6 cites this vs Intensive Care Medicine as a judgement call"),
    "Intensive Care Medicine": ("", "HANDOFF.md §6 cites this vs Intensive Care as a judgement call"),
    "Pain Management": ("Anesthesiology", "could equally be Palliative Medicine — judgement call"),
    "Pain Medicine": ("Anesthesiology", "merge with Pain Management first"),
    "Vascular Medicine": ("Cardiology", "could equally be Internal Medicine"),
    "Hypertension": ("Cardiology", "a condition, not a specialty; Cardiology is nearest"),
    "Electrocardiography": ("Cardiology", "an investigation, not a specialty"),
    "Transfusion Medicine": ("Hematology", "commonly sits under Haematology"),
    "Audiology": ("Otolaryngology", "allied-health field adjacent to ENT"),
    "Speech-Language Pathology": ("Physical Medicine and Rehabilitation", "allied-health rehab field"),
    "Reproductive Medicine": ("Obstetrics and Gynecology", "OB/GYN subspecialty"),
    "Family Planning": ("Obstetrics and Gynecology", "could equally be Public Health"),
    "Forensic Medicine": ("Pathology", "forensic pathology is nearest, but scope is wider"),
    "Laboratory Medicine": ("Pathology", "lab medicine commonly sits under Pathology"),
    "Occupational Medicine": ("Public Health", "merge with Occupational Health first"),
    "Occupational Health": ("Public Health", "merge with Occupational Medicine first"),
    "Environmental Health": ("Public Health", "Public Health subdomain"),
    "Addiction Medicine": ("Psychiatry", "commonly sits under Psychiatry"),
    "Nutrition": ("", "spans Internal Medicine, Public Health, Endocrinology"),
    "Nursing": ("", "a profession, not one of the 34 physician specialties"),
    "Veterinary Medicine": ("", "NOT human medicine — 66 rows; likely mis-scoped content"),
    "Pharmacognosy": ("Eastern Medicine", "medicinal-plant science; overlaps herbal medicine"),
}


def load_topic_frequencies(path: Path) -> collections.Counter:
    """Distinct raw topic string -> number of ROWS it appears in."""
    counts: collections.Counter = collections.Counter()
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            topics = row.get("medical_topic") or []
            # set(): a string repeated inside one row still counts as one row
            for topic in set(topics):
                counts[topic] += 1
    return counts


def classify(raw: str) -> tuple[str, str, str]:
    """Return (proposed_canonical, decision_tag, note) for a raw topic string."""
    if not str(raw).strip():
        return ("", "JUNK", "empty string")

    norm = normalize_vietnamese(raw)

    # 1. exact canonical match (after the authors' normaliser)
    if norm in CANON_BY_NORM:
        canon = CANON_BY_NORM[norm]
        if raw == canon:
            return (canon, "MATCH", "exact match to canonical name")
        return (canon, "AUTO", "differs from canonical only by case/spacing/punctuation")

    # 2. hand-curated close variant
    if raw in AUTO_MAP:
        target, note = AUTO_MAP[raw]
        return (target, "AUTO", note)

    # 3. hand-curated junk
    if raw in JUNK_NOTES:
        return ("", "JUNK", JUNK_NOTES[raw])

    # 4. hand-curated ambiguous
    if raw in AMBIGUOUS_GUESS:
        guess, note = AMBIGUOUS_GUESS[raw]
        return (guess, "AMBIGUOUS", note)

    # 5. anything not triaged by hand — surfaced loudly rather than guessed at
    return ("", "AMBIGUOUS", "NOT HAND-TRIAGED — review required")


def main() -> None:
    counts = load_topic_frequencies(DATA_PATH)

    records = []
    for raw, freq in counts.items():
        proposed, tag, note = classify(raw)
        records.append(
            {
                "raw_string": raw,
                "frequency": freq,
                "proposed_canonical": proposed,
                "decision_tag": tag,
                "note": note,
            }
        )

    # Sort by decision_tag, then frequency descending, so high-volume
    # AMBIGUOUS/JUNK surface at the top of their blocks.
    tag_order = {"AMBIGUOUS": 0, "JUNK": 1, "AUTO": 2, "MATCH": 3}
    records.sort(key=lambda r: (tag_order[r["decision_tag"]], -r["frequency"], r["raw_string"]))

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["raw_string", "frequency", "proposed_canonical", "decision_tag", "note"],
        )
        writer.writeheader()
        writer.writerows(records)

    # ---- summary ----------------------------------------------------------
    print(f"distinct raw topic strings : {len(records)}")
    print(f"canonical specialties      : {len(CANONICAL_34)}")
    print()
    print(f"{'tag':<11} {'strings':>8} {'rows touched':>14}")
    print("-" * 35)
    for tag in ("MATCH", "AUTO", "AMBIGUOUS", "JUNK"):
        subset = [r for r in records if r["decision_tag"] == tag]
        print(f"{tag:<11} {len(subset):>8} {sum(r['frequency'] for r in subset):>14,}")
    print("-" * 35)
    print(f"{'TOTAL':<11} {len(records):>8} {sum(r['frequency'] for r in records):>14,}")
    print()
    print("NOTE: 'rows touched' double-counts rows carrying several topics.")
    print(f"wrote {OUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()

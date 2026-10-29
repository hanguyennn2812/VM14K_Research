#!/usr/bin/env python3
"""Attach search candidates to the frozen Cardiology annotation template.

This is an annotation aid, not an evaluator and not a source of gold labels.
It writes a separate file, leaves every coverage/status field unchanged, and
requires the annotator to open the cited PDF page before completing a row.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from evaluate_moh_retrieval import (
    corpus_fingerprint,
    dense_rankings,
    lexical_rankings,
    page_chunks,
    query_text,
    reciprocal_rank_fusion,
    specialty_folder,
)

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GOLD = ROOT / "data" / "annotations" / "cardiology_retrieval_gold_30.jsonl"
DEFAULT_OUTPUT = (
    ROOT / "data" / "annotations" / "cardiology_retrieval_gold_30_candidates.jsonl"
)
DEFAULT_CACHE = ROOT / "data" / "interim" / "moh_retrieval_cache"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--specialty-vn", default="Tim mạch")
    parser.add_argument("--embedding-model", default="bge-m3")
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--fusion-depth", type=int, default=100)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--chunk-words", type=int, default=180)
    parser.add_argument("--chunk-overlap", type=int, default=40)
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434/api/embed")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    gold_path = args.gold if args.gold.is_absolute() else ROOT / args.gold
    output_path = args.output if args.output.is_absolute() else ROOT / args.output
    cache_dir = args.cache_dir if args.cache_dir.is_absolute() else ROOT / args.cache_dir
    if output_path.exists() and not args.force:
        parser.error(f"{output_path} exists; use --force to replace it")

    with gold_path.open(encoding="utf-8") as handle:
        rows = [json.loads(line) for line in handle if line.strip()]
    folder = specialty_folder(args.specialty_vn)
    pdf_paths = sorted(folder.glob("*.pdf"), key=lambda path: path.name)
    fingerprint = corpus_fingerprint(pdf_paths, args.chunk_words, args.chunk_overlap)
    chunks = page_chunks(pdf_paths, args.chunk_words, args.chunk_overlap)
    chunk_by_id = {chunk["chunk_id"]: chunk for chunk in chunks}
    queries = [query_text(row) for row in rows]
    lexical = lexical_rankings(queries, chunks, args.fusion_depth)
    dense = dense_rankings(
        queries,
        chunks,
        args.fusion_depth,
        args.embedding_model,
        None,
        args.batch_size,
        cache_dir,
        fingerprint,
        backend="ollama",
        ollama_url=args.ollama_url,
    )
    hybrid = reciprocal_rank_fusion(lexical, dense, args.top_k)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for row, ranked in zip(rows, hybrid, strict=True):
            candidates = []
            for item in ranked:
                chunk = chunk_by_id[item["chunk_id"]]
                candidates.append(
                    {
                        "chunk_id": chunk["chunk_id"],
                        "source_file": chunk["source_file"],
                        "source_sha256": chunk["source_sha256"],
                        "pdf_page": chunk["pdf_page"],
                        "score": item["score"],
                        "passage": chunk["text"],
                    }
                )
            assisted = {
                **row,
                "retrieval_candidates": candidates,
                "candidate_warning": (
                    "Search aid only. Open the PDF page and verify manually; do not "
                    "copy a candidate into gold_evidence solely because it ranked highly."
                ),
            }
            handle.write(json.dumps(assisted, ensure_ascii=False) + "\n")
    print(f"wrote {len(rows)} annotation-aid rows to {output_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Evaluate lexical and embedding retrieval on page-level MoH evidence.

The evaluator refuses to score a pending gold set.  It reports guideline
coverage separately from retrieval quality and computes retrieval metrics only
for questions annotated as covered.  Exact source-file and PDF-page provenance
is retained in every retrieved hit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import time
from datetime import UTC, datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import numpy as np
import pymupdf
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GOLD = ROOT / "data" / "annotations" / "cardiology_retrieval_gold_30.jsonl"
DEFAULT_REPORT = ROOT / "reports" / "retrieval" / "cardiology_retrieval_eval.json"
DEFAULT_CACHE = ROOT / "data" / "interim" / "moh_retrieval_cache"


def fix_mojibake(name: str) -> str:
    """Recover UTF-8 names decoded through the legacy Windows CP437 path."""
    try:
        return name.encode("cp437").decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        return name


def specialty_folder(specialty_vn: str) -> Path:
    candidates = [path for path in (ROOT / "data").iterdir() if path.is_dir()]
    parents = [path for path in candidates if "khoa" in fix_mojibake(path.name).casefold()]
    if len(parents) != 1:
        raise RuntimeError(f"expected one specialty parent, found {len(parents)}: {parents}")
    matches = [
        path
        for path in parents[0].iterdir()
        if path.is_dir() and fix_mojibake(path.name) == specialty_vn
    ]
    if len(matches) != 1:
        raise RuntimeError(f"expected one specialty folder for {specialty_vn!r}, found {matches}")
    return matches[0]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def corpus_fingerprint(paths: list[Path], words: int, overlap: int) -> str:
    digest = hashlib.sha256(f"page-chunks-v1:{words}:{overlap}".encode())
    for path in paths:
        digest.update(path.name.encode("utf-8"))
        digest.update(file_sha256(path).encode())
    return digest.hexdigest()


def page_chunks(paths: list[Path], words: int, overlap: int) -> list[dict]:
    if words < 1 or overlap < 0 or overlap >= words:
        raise ValueError("require words >= 1 and 0 <= overlap < words")
    step = words - overlap
    chunks: list[dict] = []
    for path in paths:
        source_sha256 = file_sha256(path)
        with pymupdf.open(path) as document:
            for page_index, page in enumerate(document, start=1):
                text = re.sub(r"\s+", " ", page.get_text()).strip()
                tokens = text.split()
                if not tokens:
                    continue
                for start in range(0, len(tokens), step):
                    chunk_tokens = tokens[start : start + words]
                    if not chunk_tokens:
                        continue
                    chunks.append(
                        {
                            "chunk_id": f"{source_sha256[:12]}:p{page_index}:w{start}",
                            "source_file": path.name,
                            "source_sha256": source_sha256,
                            "pdf_page": page_index,
                            "word_start": start,
                            "text": " ".join(chunk_tokens),
                        }
                    )
    return chunks


def load_gold(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        rows = [json.loads(line) for line in handle if line.strip()]
    if not rows:
        raise ValueError(f"gold set is empty: {path}")
    incomplete = [row["id"] for row in rows if row.get("annotation_status") != "complete"]
    if incomplete:
        preview = ", ".join(incomplete[:5])
        raise ValueError(
            f"gold set has {len(incomplete)} pending rows ({preview}); finish annotation first"
        )
    allowed = {"covered", "not_covered", "uncertain"}
    invalid = [row["id"] for row in rows if row.get("coverage_label") not in allowed]
    if invalid:
        raise ValueError(f"invalid coverage_label for {invalid[:5]}")
    for row in rows:
        if row["coverage_label"] == "covered" and not row.get("gold_evidence"):
            raise ValueError(f"covered row {row['id']} has no gold_evidence")
    return rows


def query_text(row: dict) -> str:
    options = " ".join(
        f"{chr(65 + index)}. {option}" for index, option in enumerate(row["options"])
    )
    return f"{row['question']} {options}"


def lexical_rankings(queries: list[str], chunks: list[dict], top_k: int) -> list[list[dict]]:
    vectorizer = TfidfVectorizer(max_features=20_000)
    matrix = vectorizer.fit_transform(chunk["text"] for chunk in chunks)
    query_matrix = vectorizer.transform(queries)
    scores = query_matrix @ matrix.T
    rankings: list[list[dict]] = []
    for row_index in range(len(queries)):
        dense_scores = scores.getrow(row_index).toarray().ravel()
        indices = np.argsort(dense_scores)[::-1][:top_k]
        rankings.append([hit(chunks[index], dense_scores[index]) for index in indices])
    return rankings


def dense_rankings(
    queries: list[str],
    chunks: list[dict],
    top_k: int,
    model_name: str,
    device: str | None,
    batch_size: int,
    cache_dir: Path,
    fingerprint: str,
    backend: str = "ollama",
    ollama_url: str = "http://127.0.0.1:11434/api/embed",
    timeout_seconds: int = 300,
) -> list[list[dict]]:
    cache_key = hashlib.sha256(
        f"{backend}:{model_name}:{fingerprint}".encode()
    ).hexdigest()[:20]
    cache_path = cache_dir / f"dense_{cache_key}.npz"
    if cache_path.exists():
        with np.load(cache_path, allow_pickle=False) as cached:
            embeddings = cached["embeddings"]
        if embeddings.shape[0] != len(chunks):
            raise RuntimeError(f"stale embedding cache: {cache_path}")
    else:
        embeddings = encode_texts(
            [chunk["text"] for chunk in chunks],
            backend=backend,
            model_name=model_name,
            device=device,
            batch_size=batch_size,
            ollama_url=ollama_url,
            timeout_seconds=timeout_seconds,
            show_progress=True,
        )
        cache_dir.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(cache_path, embeddings=embeddings)

    query_embeddings = encode_texts(
        queries,
        backend=backend,
        model_name=model_name,
        device=device,
        batch_size=batch_size,
        ollama_url=ollama_url,
        timeout_seconds=timeout_seconds,
        show_progress=False,
    )
    rankings: list[list[dict]] = []
    for query_embedding in query_embeddings:
        scores = embeddings @ query_embedding
        indices = np.argsort(scores)[::-1][:top_k]
        rankings.append([hit(chunks[index], scores[index]) for index in indices])
    return rankings


def encode_texts(
    texts: list[str],
    *,
    backend: str,
    model_name: str,
    device: str | None,
    batch_size: int,
    ollama_url: str,
    timeout_seconds: int,
    show_progress: bool,
) -> np.ndarray:
    """Encode text with either a local Ollama server or SentenceTransformers."""
    if not texts:
        return np.empty((0, 0), dtype=np.float32)
    if backend == "sentence-transformers":
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:
            raise RuntimeError(
                "the sentence-transformers backend requires sentence-transformers"
            ) from exc
        model = SentenceTransformer(model_name, device=device)
        vectors = model.encode(
            texts,
            batch_size=batch_size,
            normalize_embeddings=True,
            show_progress_bar=show_progress,
            convert_to_numpy=True,
        )
        return np.asarray(vectors, dtype=np.float32)
    if backend != "ollama":
        raise ValueError(f"unsupported embedding backend: {backend}")

    vectors: list[list[float]] = []
    started = time.monotonic()
    for start in range(0, len(texts), batch_size):
        batch = texts[start : start + batch_size]
        payload = json.dumps({"model": model_name, "input": batch}).encode("utf-8")
        request = Request(
            ollama_url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=timeout_seconds) as response:
                result = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError) as exc:
            raise RuntimeError(
                f"Ollama embedding failed at {ollama_url}; ensure `ollama serve` "
                f"is running and `{model_name}` is installed"
            ) from exc
        batch_vectors = result.get("embeddings")
        if not isinstance(batch_vectors, list) or len(batch_vectors) != len(batch):
            raise RuntimeError("Ollama returned an invalid embeddings payload")
        vectors.extend(batch_vectors)
        if show_progress:
            done = min(start + batch_size, len(texts))
            elapsed = max(time.monotonic() - started, 1e-9)
            print(f"embedded {done}/{len(texts)} texts ({done / elapsed:.1f}/s)")

    array = np.asarray(vectors, dtype=np.float32)
    norms = np.linalg.norm(array, axis=1, keepdims=True)
    if np.any(norms == 0):
        raise RuntimeError("embedding backend returned a zero vector")
    return array / norms


def reciprocal_rank_fusion(
    first: list[list[dict]],
    second: list[list[dict]],
    top_k: int,
    rank_constant: int = 60,
) -> list[list[dict]]:
    """Fuse two rankings without tuning incompatible raw score scales."""
    if len(first) != len(second):
        raise ValueError("ranking sets must contain the same number of queries")
    fused_rankings: list[list[dict]] = []
    for first_hits, second_hits in zip(first, second, strict=True):
        by_id: dict[str, dict] = {}
        fused_scores: dict[str, float] = {}
        for ranked_hits in (first_hits, second_hits):
            for rank, item in enumerate(ranked_hits, start=1):
                chunk_id = item["chunk_id"]
                by_id.setdefault(chunk_id, item)
                fused_scores[chunk_id] = fused_scores.get(chunk_id, 0.0) + 1.0 / (
                    rank_constant + rank
                )
        ordered = sorted(fused_scores, key=fused_scores.get, reverse=True)[:top_k]
        fused_rankings.append(
            [
                {
                    **by_id[chunk_id],
                    "score": round(fused_scores[chunk_id], 8),
                }
                for chunk_id in ordered
            ]
        )
    return fused_rankings


def hit(chunk: dict, score: float) -> dict:
    return {
        "chunk_id": chunk["chunk_id"],
        "source_file": chunk["source_file"],
        "source_sha256": chunk["source_sha256"],
        "pdf_page": chunk["pdf_page"],
        "score": round(float(score), 6),
        "snippet": chunk["text"][:500],
    }


def is_relevant(retrieved: dict, evidence: list[dict]) -> bool:
    for item in evidence:
        page_start = int(item["page_start"])
        page_end = int(item.get("page_end", page_start))
        if (
            Path(retrieved["source_file"]).name == Path(item["source_file"]).name
            and page_start <= int(retrieved["pdf_page"]) <= page_end
        ):
            return True
    return False


def wilson_interval(successes: int, total: int, z: float = 1.96) -> list[float] | None:
    if total == 0:
        return None
    proportion = successes / total
    denominator = 1 + z * z / total
    centre = proportion + z * z / (2 * total)
    margin = z * math.sqrt(
        proportion * (1 - proportion) / total + z * z / (4 * total * total)
    )
    return [round((centre - margin) / denominator, 4), round((centre + margin) / denominator, 4)]


def score_method(gold: list[dict], rankings: list[list[dict]], cutoffs: list[int]) -> dict:
    covered_indices = [index for index, row in enumerate(gold) if row["coverage_label"] == "covered"]
    metrics: dict[str, object] = {"n_covered": len(covered_indices)}
    per_question: list[dict] = []
    reciprocal_ranks: list[float] = []
    for index in covered_indices:
        row = gold[index]
        ranked = rankings[index]
        first_rank = next(
            (rank for rank, item in enumerate(ranked, start=1) if is_relevant(item, row["gold_evidence"])),
            None,
        )
        reciprocal_ranks.append(0.0 if first_rank is None else 1.0 / first_rank)
        per_question.append(
            {"id": row["id"], "first_relevant_rank": first_rank, "top_hits": ranked}
        )
    for cutoff in cutoffs:
        successes = sum(
            item["first_relevant_rank"] is not None and item["first_relevant_rank"] <= cutoff
            for item in per_question
        )
        metrics[f"recall_at_{cutoff}"] = round(successes / len(covered_indices), 4) if covered_indices else None
        metrics[f"recall_at_{cutoff}_95ci"] = wilson_interval(successes, len(covered_indices))
    metrics[f"mrr_at_{max(cutoffs)}"] = (
        round(sum(reciprocal_ranks) / len(reciprocal_ranks), 4) if reciprocal_ranks else None
    )
    metrics["per_question"] = per_question
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--specialty-vn", default="Tim mạch")
    parser.add_argument(
        "--methods",
        nargs="+",
        choices=("tfidf", "dense", "hybrid"),
        default=("tfidf", "dense", "hybrid"),
    )
    parser.add_argument("--embedding-backend", choices=("ollama", "sentence-transformers"), default="ollama")
    parser.add_argument("--embedding-model", default="bge-m3")
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434/api/embed")
    parser.add_argument("--embedding-timeout", type=int, default=300)
    parser.add_argument("--device", default=None)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--chunk-words", type=int, default=180)
    parser.add_argument("--chunk-overlap", type=int, default=40)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--fusion-depth", type=int, default=100)
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    gold_path = args.gold if args.gold.is_absolute() else ROOT / args.gold
    report_path = args.report if args.report.is_absolute() else ROOT / args.report
    cache_dir = args.cache_dir if args.cache_dir.is_absolute() else ROOT / args.cache_dir
    if report_path.exists() and not args.force:
        parser.error(f"{report_path} exists; use --force to replace it")
    if args.top_k < 10:
        parser.error("--top-k must be at least 10 so Recall@10 and MRR@10 are defined")
    if args.fusion_depth < args.top_k:
        parser.error("--fusion-depth must be at least --top-k")

    gold = load_gold(gold_path)
    folder = specialty_folder(args.specialty_vn)
    pdf_paths = sorted(folder.glob("*.pdf"), key=lambda path: path.name)
    if not pdf_paths:
        raise RuntimeError(f"no PDFs found in {folder}")
    fingerprint = corpus_fingerprint(pdf_paths, args.chunk_words, args.chunk_overlap)
    chunks = page_chunks(pdf_paths, args.chunk_words, args.chunk_overlap)
    if not chunks:
        raise RuntimeError(f"no extractable page chunks found in {folder}")

    queries = [query_text(row) for row in gold]
    rankings: dict[str, list[list[dict]]] = {}
    needs_tfidf = "tfidf" in args.methods or "hybrid" in args.methods
    needs_dense = "dense" in args.methods or "hybrid" in args.methods
    tfidf_rankings = (
        lexical_rankings(queries, chunks, args.fusion_depth) if needs_tfidf else None
    )
    dense_results = None
    if needs_dense:
        dense_results = dense_rankings(
            queries,
            chunks,
            args.fusion_depth,
            args.embedding_model,
            args.device,
            args.batch_size,
            cache_dir,
            fingerprint,
            backend=args.embedding_backend,
            ollama_url=args.ollama_url,
            timeout_seconds=args.embedding_timeout,
        )
    if "tfidf" in args.methods and tfidf_rankings is not None:
        rankings["tfidf"] = [hits[: args.top_k] for hits in tfidf_rankings]
    if "dense" in args.methods and dense_results is not None:
        rankings["dense"] = [hits[: args.top_k] for hits in dense_results]
    if "hybrid" in args.methods and tfidf_rankings is not None and dense_results is not None:
        rankings["hybrid"] = reciprocal_rank_fusion(
            tfidf_rankings, dense_results, args.top_k
        )

    coverage_counts = {
        label: sum(row["coverage_label"] == label for row in gold)
        for label in ("covered", "not_covered", "uncertain")
    }
    cutoffs = [1, 3, 5, 10]
    report = {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "scope": "validation-only retrieval evaluation; no VM14K test rows accessed",
        "gold_path": str(gold_path.relative_to(ROOT)),
        "gold_questions": len(gold),
        "coverage": {
            "counts": coverage_counts,
            "covered_fraction": round(coverage_counts["covered"] / len(gold), 4),
        },
        "corpus": {
            "specialty_vn": args.specialty_vn,
            "folder": str(folder.relative_to(ROOT)),
            "pdf_files": len(pdf_paths),
            "page_chunks": len(chunks),
            "fingerprint_sha256": fingerprint,
            "chunk_words": args.chunk_words,
            "chunk_overlap": args.chunk_overlap,
        },
        "query_definition": "question plus all answer options; gold answer is not added",
        "embedding_backend": args.embedding_backend if needs_dense else None,
        "embedding_model": args.embedding_model if needs_dense else None,
        "methods": {
            method: score_method(gold, method_rankings, cutoffs)
            for method, method_rankings in rankings.items()
        },
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    console_methods = {
        method: {key: value for key, value in metrics.items() if key != "per_question"}
        for method, metrics in report["methods"].items()
    }
    print(
        json.dumps(
            {"coverage": report["coverage"], "methods": console_methods},
            ensure_ascii=False,
            indent=2,
        )
    )
    print(f"wrote {report_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

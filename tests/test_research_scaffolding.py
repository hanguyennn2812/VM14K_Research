from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ResearchScaffoldingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # PyMuPDF is exercised in the real retrieval run.  These unit tests only
        # cover gold-set gating and scoring, so a module stub avoids requiring the
        # heavyweight PDF dependency in a minimal test environment.
        sys.modules.setdefault("pymupdf", types.ModuleType("pymupdf"))
        cls.gold_export = load_module(
            "gold_export", "scripts/retrieval/export_cardiology_gold_template.py"
        )
        cls.retrieval = load_module(
            "retrieval_eval", "scripts/retrieval/evaluate_moh_retrieval.py"
        )
        sys.modules["evaluate_moh_retrieval"] = cls.retrieval
        cls.generator = load_module(
            "grounded_generator", "scripts/retrieval/generate_grounded_cardiology.py"
        )
        cls.grounded = load_module(
            "grounded_export", "scripts/training/export_qwen_sft_grounded.py"
        )
        cls.trainer = load_module(
            "grounded_trainer", "scripts/training/train_qwen_grounded_qlora.py"
        )

    def test_gold_selection_is_fixed_and_excludes_residual_placeholder(self) -> None:
        rows, exclusions = self.gold_export.load_rows()
        rows.sort(key=lambda row: self.gold_export.stable_sampling_key(row, 42))
        selected = rows[:30]
        self.assertEqual(len(rows), 40)
        self.assertEqual(exclusions, ["7385849c6bb44b54a55f37349115b504"])
        self.assertEqual(len({row["id"] for row in selected}), 30)
        self.assertNotIn(exclusions[0], {row["id"] for row in selected})

    def test_retrieval_refuses_pending_gold(self) -> None:
        path = ROOT / "data/annotations/cardiology_retrieval_gold_30.jsonl"
        with self.assertRaisesRegex(ValueError, "pending rows"):
            self.retrieval.load_gold(path)

    def test_retrieval_metrics_use_exact_file_and_page(self) -> None:
        gold = [
            {
                "id": "q1",
                "coverage_label": "covered",
                "gold_evidence": [
                    {"source_file": "guideline-a.pdf", "page_start": 3, "page_end": 4}
                ],
            },
            {
                "id": "q2",
                "coverage_label": "covered",
                "gold_evidence": [
                    {"source_file": "guideline-b.pdf", "page_start": 7, "page_end": 7}
                ],
            },
            {"id": "q3", "coverage_label": "not_covered", "gold_evidence": []},
        ]
        rankings = [
            [
                {"source_file": "guideline-a.pdf", "pdf_page": 3},
                {"source_file": "other.pdf", "pdf_page": 1},
            ],
            [
                {"source_file": "guideline-b.pdf", "pdf_page": 6},
                {"source_file": "guideline-b.pdf", "pdf_page": 7},
            ],
            [{"source_file": "anything.pdf", "pdf_page": 1}],
        ]
        scored = self.retrieval.score_method(gold, rankings, [1, 3, 5, 10])
        self.assertEqual(scored["n_covered"], 2)
        self.assertEqual(scored["recall_at_1"], 0.5)
        self.assertEqual(scored["recall_at_3"], 1.0)
        self.assertEqual(scored["mrr_at_10"], 0.75)
        self.assertEqual(len(scored["per_question"]), 2)

    def test_grounded_export_rejects_missing_evidence(self) -> None:
        base = {
            "id": "q1",
            "split": "train",
            "question": "Q?",
            "options": ["a", "b"],
            "answer": "A",
            "explanation": "Vì bằng chứng nêu như vậy.",
            "support_label": "supported",
            "verification_status": "human_verified",
            "citations": [],
        }
        self.assertEqual(self.grounded.validate_supported(base), "missing_citations")
        base["citations"] = [
            {
                "source_file": "guideline.pdf",
                "page_start": 2,
                "page_end": 2,
                "passage": "Bằng chứng.",
            }
        ]
        self.assertIsNone(self.grounded.validate_supported(base))
        item = self.grounded.make_item(base)
        answer = item["messages"][-1]["content"]
        self.assertIn("Đáp án: A", answer)
        self.assertIn("guideline.pdf, trang 2", answer)
        self.assertTrue(answer.startswith("<think>\n\n</think>"))
        self.assertTrue(item["messages"][-2]["content"].endswith("/no_think"))

    def test_uncalibrated_auto_check_is_gated_by_default(self) -> None:
        row = {
            "id": "q-auto",
            "split": "train",
            "question": "Q?",
            "options": ["a", "b"],
            "answer": "A",
            "explanation": "Evidence-bound explanation.",
            "support_label": "supported",
            "verification_status": "uncalibrated_auto_check",
            "citations": [
                {
                    "source_file": "guideline.pdf",
                    "page_start": 2,
                    "page_end": 2,
                    "passage": "Evidence.",
                }
            ],
        }
        self.assertEqual(self.grounded.validate_supported(row), "evidence_not_verified")
        self.assertIsNone(self.grounded.validate_supported(row, True))

    def test_reciprocal_rank_fusion_rewards_agreement(self) -> None:
        first = [[
            {"chunk_id": "shared", "score": 0.9},
            {"chunk_id": "lexical", "score": 0.8},
        ]]
        second = [[
            {"chunk_id": "dense", "score": 0.95},
            {"chunk_id": "shared", "score": 0.7},
        ]]
        fused = self.retrieval.reciprocal_rank_fusion(first, second, top_k=3)
        self.assertEqual(fused[0][0]["chunk_id"], "shared")
        self.assertEqual(
            {item["chunk_id"] for item in fused[0]},
            {"shared", "lexical", "dense"},
        )

    def test_trainer_refuses_uncalibrated_evidence(self) -> None:
        row = {
            "messages": [
                {"role": "system", "content": "system"},
                {"role": "user", "content": "question"},
                {"role": "assistant", "content": "answer"},
            ],
            "metadata": {
                "source_id": "q1",
                "split": "train",
                "support_label": "supported",
                "verification_status": "uncalibrated_auto_check",
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "train.jsonl"
            path.write_text(json.dumps(row) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unverified evidence"):
                self.trainer.load_jsonl(path, "train", False)
            accepted = self.trainer.load_jsonl(path, "train", True)
        self.assertEqual(len(accepted), 1)

    def test_compound_answers_require_every_atomic_claim(self) -> None:
        answer = "Aspirin + Statin + Metformin + amputation + no smoking"
        self.assertEqual(self.generator.minimum_claim_count(answer), 5)
        raw = {
            "support_label": "supported",
            "explanation": "Partial explanation.",
            "claims": [
                {
                    "claim": f"claim {index}",
                    "support_label": "supported",
                    "cited_chunk_ids": ["c1"],
                }
                for index in range(3)
            ],
        }
        normalized = self.generator.normalize_draft(raw, {"c1"}, 5)
        self.assertEqual(normalized["support_label"], "unsupported")


if __name__ == "__main__":
    unittest.main()

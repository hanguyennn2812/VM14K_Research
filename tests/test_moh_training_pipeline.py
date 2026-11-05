import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "training"))
from filter_moh_teacher_labels import prepare
from split_moh_documents import assign_groups


def test_teacher_disagreement_is_rejected_and_soft_labels_are_kept():
    items = [{"id": "ok", "answer_index": 0}, {"id": "bad", "answer_index": 1}]
    own = [{"id": "ok", "pred": "A", "probs_orig": [.7, .1, .1, .1], "error": None},
           {"id": "bad", "pred": "C", "probs_orig": [.1, .1, .7, .1], "error": None}]
    bare = [{"id": "ok", "pred": "B", "probs_orig": [.2, .6, .1, .1], "error": None},
            {"id": "bad", "pred": "B", "probs_orig": [.1, .7, .1, .1], "error": None}]
    accepted, rejected = prepare(items, own, bare)
    assert [row["id"] for row in accepted] == ["ok"]
    assert accepted[0]["teacher"]["with_source_probs"] == [.7, .1, .1, .1]
    assert accepted[0]["teacher"]["new_knowledge_candidate"] is True
    assert rejected == [{"id": "bad", "reason": "d3_with_source_disagrees", "key": "B", "d3_pred": "C"}]


def test_disease_groups_never_cross_document_splits():
    sizes = {"tb": 20, "mpox": 10, "dengue": 8, "hiv": 6, "measles": 5}
    assignment = assign_groups(sizes, seed=7)
    assert set(assignment) == set(sizes)
    assert len(set(assignment.values())) == 3
    assert assignment == assign_groups(sizes, seed=7)

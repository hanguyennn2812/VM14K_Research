import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts", "eval"))

from compare_runs import mcnemar_exact  # noqa: E402
from collect_reasoning import final_letter  # noqa: E402
from run_eval import build_prompt, done_records, parse_letter, permute, repair_partial_tail  # noqa: E402
from summarize_eval import is_subsample  # noqa: E402


def test_parse_single_letter():
    assert parse_letter("B", 4) == "B"
    assert parse_letter(" C.\n", 4) == "C"
    assert parse_letter("**D**", 4) == "D"


def test_parse_answer_phrases():
    assert parse_letter("Đáp án: C", 4) == "C"
    assert parse_letter("Đáp án đúng là B vì ...", 4) == "B"
    assert parse_letter("The answer is (A).", 4) == "A"


def test_parse_ignores_reasoning_block():
    assert parse_letter("<think>maybe A, but D fits</think>\nB", 4) == "B"
    # an unfinished reasoning block (hit num_predict) yields no answer
    assert parse_letter("<think>A or C", 4) is None


def test_parse_rejects_out_of_range_and_words():
    assert parse_letter("D", 2) is None           # 2-option question has only A/B
    assert parse_letter("Vitamin Đ thiếu", 4) is None
    assert parse_letter("", 4) is None


def test_permute_identity_without_seed():
    row = {"id": "x", "options": ["a", "b", "c", "d"], "answer_index": 2}
    options, gold, perm = permute(row, None)
    assert options == row["options"] and gold == 2 and perm == [0, 1, 2, 3]


def test_permute_tracks_gold_and_is_deterministic():
    row = {"id": "abc", "options": ["a", "b", "c", "d"], "answer_index": 1}
    options, gold, perm = permute(row, 7)
    assert options[gold] == "b"
    assert sorted(perm) == [0, 1, 2, 3]
    assert permute(row, 7) == (options, gold, perm)


def test_prompt_matches_paper_template():
    p = build_prompt("paper", "Q?", ["x", "y"])
    assert p == "Q?\nChoose the correct option from these answers:\nA. x\nB. y\nOnly response with 1 character\nExample: A"


def test_mcnemar_exact():
    assert mcnemar_exact(0, 0) == 1.0
    assert mcnemar_exact(0, 6) == 2 / 64          # all 6 discordant pairs one way
    assert mcnemar_exact(5, 5) == 1.0
    assert abs(mcnemar_exact(10, 20) - 0.0987) < 1e-3


def test_is_subsample_only_matches_limit_suffix():
    assert is_subsample("qwen3_8b__paper__test__n20")
    assert is_subsample("x__paper__test__think-on__n400")
    assert not is_subsample("nvidia__nvidia_nemotron-3-ultra-550b-a55b__paper__test")
    assert not is_subsample("qwen3_8b__paper__test")


def test_resume_drops_partial_tail_and_keeps_later_records(tmp_path):
    log = tmp_path / "run.jsonl"
    log.write_bytes(b'{"id": "old", "error": null}\n{"id": "cut", "err')
    repair_partial_tail(str(log))
    with open(log, "a", encoding="utf-8") as fh:  # what a resumed run does next
        fh.write('{"id": "retried", "error": null}\n')
    assert sorted(done_records(str(log))) == ["old", "retried"]
    assert (tmp_path / "run.jsonl.partial").read_bytes() == b'{"id": "cut", "err\n'


def test_resume_survives_tail_cut_inside_utf8_character(tmp_path):
    log = tmp_path / "run.jsonl"
    log.write_bytes('{"id": "old", "error": null}\n{"id": "cut", "q": "Tiế'.encode("utf-8")[:-1])
    repair_partial_tail(str(log))
    assert sorted(done_records(str(log))) == ["old"]


def test_resume_refuses_corruption_in_the_middle(tmp_path):
    log = tmp_path / "run.jsonl"
    log.write_bytes(b'{"id": "a", "error": null}\nnot json\n{"id": "b", "error": null}\n')
    repair_partial_tail(str(log))  # ends in a newline: nothing to cut
    with pytest.raises(SystemExit):
        done_records(str(log))


def test_final_letter_takes_last_answer_line_and_abstentions():
    assert final_letter("Xét A sai, B sai.\n\nĐáp án: C", 4) == "C"
    assert final_letter("**Đáp án:** B", 4) == "B"
    assert final_letter("Đáp án: B\nĐáp án: G", 4) is None
    assert final_letter("Đáp án: B\nĐáp án: không có phương án đúng", 4) is None
    assert final_letter("Không chọn A hay B.", 4) is None
    assert final_letter("Lập luận...\n**C.**", 4) == "C"


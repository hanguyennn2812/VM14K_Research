"""Regression checks for the failure modes in Hà's 60-question pilot review."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "training"))
import gen_moh_mcq as g
from moh_mcq_source import balanced_sample, disease_group, document_problem, text_problem


def question(**changes):
    q = dict(question="Trong bệnh lao, thuốc nào được dùng?", options=["Streptomycin", "A", "B", "C"],
             answer_index=0, evidence="dùng Streptomycin", disease="bệnh lao")
    return dict(q, **changes)


SOURCE = "Bệnh lao màng não nên dùng Streptomycin (thay cho E) trong giai đoạn tấn công."


def test_parse_rejects_boolean_index_and_missing_quote():
    assert g.parse(json.dumps([question(answer_index=True)])) == []
    assert g.quality_reason(question(evidence="không có trong nguồn"), SOURCE) == "evidence_not_verbatim"


def test_no_document_wording_or_unsupported_absolutes():
    assert g.quality_reason(question(question="Thuốc nào KHÔNG được liệt kê để điều trị bệnh lao?"), SOURCE)
    assert g.quality_reason(question(question="Trong bệnh lao, thuốc nào bị chống chỉ định tuyệt đối?"), SOURCE)


def test_disease_must_be_grounded_and_in_stem():
    assert g.quality_reason(question(question="Thuốc nào được dùng?"), SOURCE) == "missing_disease_in_question"
    assert g.quality_reason(question(disease="bệnh phong"), SOURCE) == "disease_not_in_source"
    assert g.quality_reason(question(), SOURCE) is None


def test_disease_abbreviations_need_expansion_in_question():
    q = question(question="Trong SXHD, thuốc nào được dùng?", disease="SXHD")
    assert g.quality_reason(q, SOURCE + " SXHD") == "undefined_disease_abbreviation"
    q["question"] = "Trong sốt xuất huyết Dengue (SXHD), thuốc nào được dùng?"
    assert g.quality_reason(q, SOURCE + " SXHD") is None


def test_semantic_leak_examples_have_lexical_flags():
    q = question(question="Bệnh nhân lao đa kháng được phân loại là 'Thất bại công thức I' khi nào?",
                 options=["Đã từng điều trị công thức I và bị thất bại", "a", "b", "c"])
    assert g.answer_leak(q)
    q = question(question="Bệnh nhân lao đa kháng thuộc nhóm 'Điều trị lại sau bỏ trị' có đặc điểm gì?",
                 options=["Đã từng điều trị lao, được kết luận bỏ trị, nay chẩn đoán là lao đa kháng", "a", "b", "c"])
    assert g.answer_leak(q)


def test_administrative_sources_and_font_noise():
    assert document_problem("Huong_dan_giam_sat_va_phong_chong_benh_sot_ret", SOURCE) == "surveillance_document"
    assert text_problem("The same specimens can be used to carry out incidence estimation.")
    assert text_problem("Nguai la v~t chu giun luan tru6ng")
    assert text_problem(SOURCE) is None
    assert text_problem(SOURCE + " 횡") == "foreign_script"
    assert text_problem(SOURCE + " 5 µg/kg/phút, 𝑚, ℽ") is None
    assert document_problem("Hướng dẫn chẩn đoán bệnh lao", SOURCE + " 횡") is None
    assert document_problem("Huong dan xet nghiem moi HIV va su dung so lieu", SOURCE) == "incidence_surveillance_document"
    q = question(question="Đối với trẻ nhiễm HIV, cơ sở y tế thực hiện biện pháp nào?", disease="HIV")
    assert g.quality_reason(q, SOURCE + " HIV") == "administrative_question"
    assert document_problem("Huong dan chan doan va dieu tri cac benh Da lieu", SOURCE) == "outside_infectious_diseases"
    assert document_problem("Huong dan phuc hoi chuc nang sau mac COVID 19", SOURCE) == "outside_infectious_diseases"
    assert document_problem("QU25D4~1", "QUY TRÌNH kỹ thuật dịch vụ tư vấn HIV") == "administrative_document"


def test_three_remaining_pilot_v2_failures_are_rejected():
    mpox = question(
        question="Một bệnh nhân mpox 30 tuổi, suy giảm miễn dịch ổn định, có tổn thương da lan rộng nên điều trị ở đâu?",
        options=["Tại nhà", "Bệnh viện huyện", "Bệnh viện tỉnh", "Theo dõi"], disease="mpox",
        evidence="Bệnh viện quận/huyện: điều trị ca bệnh có nguy cơ tiến triển nặng")
    assert g.quality_reason(mpox, "mpox. Bệnh viện quận/huyện: điều trị ca bệnh có nguy cơ tiến triển nặng") == "invented_scenario_detail"
    regimen = question(
        question="Điều trị đồng nhiễm Chlamydia trong bệnh lậu được thực hiện như thế nào?",
        options=["Azithromycin 1g", "A", "B", "C"], disease="bệnh lậu",
        evidence="Kết hợp azithromycin 1g uống liều duy nhất để điều trị đồng nhiễm Chlamydia.")
    src = "bệnh lậu. Kết hợp azithromycin 1g uống liều duy nhất để điều trị đồng nhiễm Chlamydia."
    assert g.quality_reason(regimen, src) == "adjunct_presented_as_complete_regimen"
    authority = question(question="Trong bệnh lao, ai có thẩm quyền quyết định chẩn đoán?")
    assert g.quality_reason(authority, SOURCE) == "administrative_question"


def test_unsupported_rankings_and_near_duplicate_knowledge():
    q = question(question="Trong bệnh lao, thuốc hàng đầu là thuốc nào?")
    assert g.quality_reason(q, SOURCE) == "unsupported_ranking"
    a = question(question="Trong bệnh lao, thuốc nào được dùng điều trị?", options=["Streptomycin", "A", "B", "C"])
    b = question(question="Thuốc nào dùng cho bệnh lao?", options=["Streptomycin", "D", "E", "F"])
    assert g.near_duplicate(b, [a])
    assert disease_group("Huong dan dieu tri benh dau mua khi o nguoi") == "mpox"
    assert disease_group("Huong dan phong benh Mpox") == "mpox"


def test_balanced_sampling_is_seeded_and_round_robins_documents():
    chunks = [{"doc_id": d, "id": f"{d}{n}"} for d, count in [("a", 30), ("b", 3), ("c", 3)] for n in range(count)]
    sample = balanced_sample(chunks, 6, 7)
    assert sample == balanced_sample(chunks, 6, 7)
    assert [sum(c["doc_id"] == d for c in sample) for d in "abc"] == [2, 2, 2]


def test_verifier_fails_closed_on_bad_responses():
    assert not g.verified("not json")
    assert not g.verified('{"accept": true}')
    assert not g.verified('{"accept": true, "correct_indices": [0,1], "reason": "multiple"}', 0)
    assert not g.verified('{"accept": true, "correct_indices": [1], "reason": "wrong key"}', 0)
    assert g.verified('{"accept": true, "correct_indices": [0], "reason": "source supports only 0"}', 0)

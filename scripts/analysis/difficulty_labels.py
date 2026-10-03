#!/usr/bin/env python3
"""Audit difficulty labels; writes only reports/analysis/DIFFICULTY_LABELS.md.

Run from any directory: python scripts/analysis/difficulty_labels.py
Requires numpy, pandas, scipy, statsmodels, pypdf. No network or model calls.
"""
from __future__ import annotations

import sys

# Import the existing grouping implementation without creating other files.
sys.dont_write_bytecode = True

import collections
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import pandas as pd

from dedup_utils import normalize_vietnamese
from vm14k_dupes_and_contradictions import group_key, _normalize

ROOT = Path(__file__).resolve().parents[2]
LEVELS = ["Easy", "Medium", "Challenging", "Hard"]
MODELS = [
    ("DeepSeek-v4.1-flash", "nvidia__deepseek-ai_deepseek-v4.1-flash__paper__test"),
    ("Gemma-4-31B", "nvidia__google_gemma-4-31b-it__paper__test"),
    ("Gemma-4-12B", "gemma4_12b__paper__test"),
    ("Qwen3.5-9B", "qwen3.5_9b__paper__test"),
    ("Qwen3-8B", "qwen3_8b__paper__test"),
    ("Llama-3.1-8B", "llama3.1_8b__paper__test"),
    ("MedGemma-4B", "medgemma_4b__paper__test"),
]
SEED = 20261003
BOOTSTRAPS = 5000
CI_QUANTILES = (0.025, 0.975)


def read_jsonl(path):
    with path.open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def wilson(k, n):
    z = 1.959963984540054
    p = k / n
    center = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return center - half, center + half


def interval(values):
    return np.quantile(values, CI_QUANTILES)


def pct_ci(value, ci):
    return f"{100 * value:.1f}% [{100 * ci[0]:.1f}; {100 * ci[1]:.1f}]"


def reliability(raw):
    require(_normalize is normalize_vietnamese, "Existing grouping must use authors' normalizer; no fallback")
    groups = collections.defaultdict(list)
    for row in raw:
        require(row["difficulty_level"] in LEVELS, "Unknown raw difficulty label")
        groups[group_key(row)].append(row)
    duplicates = [g for g in groups.values() if len(g) >= 2]
    counts = np.array([[sum(r["difficulty_level"] == level for r in g)
                        for level in LEVELS] for g in duplicates], dtype=int)
    sizes = counts.sum(axis=1)
    pairs = np.zeros((4, 4), dtype=int)
    for g in duplicates:
        for a, b in itertools.combinations(g, 2):
            i, j = sorted((LEVELS.index(a["difficulty_level"]), LEVELS.index(b["difficulty_level"])))
            pairs[i, j] += 1
    n_pairs = int(pairs.sum())
    agreement = np.trace(pairs) / n_pairs
    # Generalized Fleiss: sample item uniformly, then two distinct copies.
    # Equal item weights for both observed agreement and category marginals.
    per_group = (counts * (counts - 1)).sum(axis=1) / (sizes * (sizes - 1))
    marginals = (counts / sizes[:, None]).mean(axis=0)
    chance = np.square(marginals).sum()
    fleiss = (per_group.mean() - chance) / (1 - chance)
    # All pairs equally weighted: endpoint category marginals use n_i - 1.
    endpoint_marginals = (counts * (sizes - 1)[:, None]).sum(axis=0) / (2 * n_pairs)
    pair_chance = np.square(endpoint_marginals).sum()
    pair_kappa = (agreement - pair_chance) / (1 - pair_chance)
    # Standard, fixed-number-of-ratings Fleiss on the size-2 subset.
    two = counts[sizes == 2]
    two_p = (two * (two - 1)).sum(axis=1).mean() / 2
    two_chance = np.square(two.sum(axis=0) / two.sum()).sum()
    two_kappa = (two_p - two_chance) / (1 - two_chance)
    bad = (counts > 0).sum(axis=1) > 1
    require(n_pairs == sum(len(g) * (len(g) - 1) // 2 for g in duplicates), "Pair denominator mismatch")
    return dict(groups=len(duplicates), rows=int(sizes.sum()), bad=int(bad.sum()),
                bad_rows=int(sizes[bad].sum()), sizes=dict(sorted(collections.Counter(sizes.tolist()).items())),
                pairs=pairs, n_pairs=n_pairs, agreement=agreement, fleiss=fleiss,
                group_agreement=per_group.mean(), chance=chance, pair_chance=pair_chance,
                pair_kappa=pair_kappa, two_n=len(two), two_kappa=two_kappa)


def load_test():
    clean_path = ROOT / "data/cleaned/clean_final.jsonl"
    split_path = ROOT / "splits/split_v1.json"
    split = json.loads(split_path.read_text(encoding="utf-8"))
    clean = read_jsonl(clean_path)
    require(len({r["id"] for r in clean}) == len(clean), "Duplicate clean IDs")
    by_id = {r["id"]: r for r in clean}
    all_test = {qid for qid, s in split.items() if s == "test"}
    missing = all_test - by_id.keys()
    fates_path = ROOT / "reports/eval/raw/fates.json"
    fates = json.loads(fates_path.read_text(encoding="utf-8"))
    missing_fates = {}
    for qid in sorted(missing):
        fate = fates.get(qid)
        require(isinstance(fate, str) and bool(fate.strip()),
                f"Missing test ID {qid} has no recorded fate in {fates_path}")
        missing_fates[qid] = fate
    pending = {qid for qid in all_test & by_id.keys() if by_id[qid].get("contradiction_pending_review")}
    test_ids = all_test - missing - pending
    require(len(test_ids) == 1658, "Expected frozen scored test of 1658 questions")
    require(len({group_key(by_id[qid]) for qid in test_ids}) == len(test_ids), "Test contains duplicate item groups")
    records, paths = [], [clean_path, split_path, fates_path]
    parse_failures = 0
    for label, stem in MODELS:
        path = ROOT / "reports/eval/runs" / f"{stem}.jsonl"
        paths.append(path)
        latest = {}
        for rec in read_jsonl(path):
            if rec.get("error") is None:
                latest[rec["id"]] = rec
        require(set(latest) == test_ids, f"{label}: run IDs differ from eligible frozen test")
        for qid in sorted(test_ids):
            rec, row = latest[qid], by_id[qid]
            require(rec["perm"] == list(range(len(row["options"]))), f"{label}: shuffled options")
            require(rec["n_options"] == len(row["options"]), f"{label}: option count mismatch")
            require(rec["gold"] == row["answer"], f"{label}: gold mismatch")
            require(rec["difficulty_level"] == row["difficulty_level"], f"{label}: label mismatch")
            require(rec["split"] == "test" and rec["prompt_style"] == "paper"
                    and rec["think"] in (False, "off", None),
                    f"{label}: unexpected configuration")
            correct = int(rec.get("pred") == row["answer"])
            require(bool(rec["correct"]) == bool(correct), f"{label}: correctness mismatch")
            parse_failures += rec.get("pred") is None
            records.append(dict(id=qid, model=label, level=row["difficulty_level"], correct=correct))
    frame = pd.DataFrame(records)
    require(set(frame.level) == set(LEVELS), "Unknown or missing test labels")
    return frame, len(all_test), missing_fates, len(pending), parse_failures, paths


def main():
    import scipy
    from scipy.stats import spearmanr
    import statsmodels
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    import pypdf
    from pypdf import PdfReader

    raw_path = ROOT / "data/raw/data-processed-shuffled0.jsonl"
    raw = read_jsonl(raw_path)
    require(len(raw) == 12488, "Expected 12488 raw rows")
    rel = reliability(raw)
    pdf_path = ROOT / "docs/research/VM14K_audit_notes.pdf"
    pdf_hits = []
    import re
    for page_no, page in enumerate(PdfReader(pdf_path).pages, 1):
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        for match in re.finditer(r"19[.,]8\s*%", text):
            pdf_hits.append((page_no, text[max(0, match.start() - 110):match.end() + 30].strip()))
    frame, all_test_n, missing, pending_n, unparsed, paths = load_test()
    questions = frame.groupby("id", sort=True).agg(level=("level", "first"), correctness=("correct", "mean"))
    questions["ordinal"] = questions.level.map({label: i for i, label in enumerate(LEVELS)})
    rng = np.random.default_rng(SEED)
    boot_means = {}
    for level in LEVELS:
        values = questions.loc[questions.level == level, "correctness"].to_numpy()
        boot_means[level] = values[rng.integers(len(values), size=(BOOTSTRAPS, len(values)))].mean(axis=1)

    fit = smf.glm("correct ~ C(level, Treatment(reference='Easy')) + C(model)",
                  data=frame, family=sm.families.Binomial()).fit(
                      cov_type="cluster", cov_kwds={"groups": frame.id, "use_correction": True})
    term = "C(level, Treatment(reference='Easy'))[T.Challenging]"
    # Report Easy relative to Challenging (inverse of treatment coefficient).
    beta = -float(fit.params[term])
    or_ci = np.exp(-fit.conf_int().loc[term].to_numpy()[::-1])
    level_terms = [i for i, name in enumerate(fit.params.index) if name.startswith("C(level")]
    restriction = np.eye(len(fit.params))[level_terms]
    omnibus = fit.wald_test(restriction, scalar=True)
    coef_rows = []
    for level in LEVELS[1:]:
        name = f"C(level, Treatment(reference='Easy'))[T.{level}]"
        ci = np.exp(fit.conf_int().loc[name].to_numpy())
        coef_rows.append(f"| {level} / Easy | {np.exp(fit.params[name]):.3f} [{ci[0]:.3f}; {ci[1]:.3f}] | {fit.pvalues[name]:.4f} |")

    rho_rows = []
    rho_results = []
    for name, subset in [("Đủ bốn mức", questions), ("Bỏ Hard (độ nhạy)", questions[questions.level != "Hard"])]:
        x = subset.ordinal.to_numpy()
        # Use mean correctness directly; higher ordinal difficulty should correlate negatively.
        y = subset.correctness.to_numpy()
        rho, p = spearmanr(x, y)
        boot_rho = []
        for _ in range(BOOTSTRAPS):
            idx = rng.integers(len(x), size=len(x))
            boot_rho.append(spearmanr(x[idx], y[idx]).statistic)
        ci = interval(boot_rho)
        rho_rows.append(f"| {name} | {len(x)} | {rho:.4f} [{ci[0]:.4f}; {ci[1]:.4f}] | {p:.4f} |")
        rho_results.append((rho, ci, p))

    level_accuracy = frame.groupby("level").correct.mean()
    level_counts = questions.level.value_counts()
    model_n = len(MODELS)
    ci_percent = 100 * (CI_QUANTILES[1] - CI_QUANTILES[0])
    table = []
    for level in LEVELS:
        subset = frame[frame.level == level]
        k, n = int(subset.correct.sum()), len(subset)
        table.append(f"| {level} | {int(level_counts[level])} | {k}/{n} | {pct_ci(k/n, wilson(k,n))} | {pct_ci(k/n, interval(boot_means[level]))} |")
    model_table = []
    for model, _ in MODELS:
        cells = []
        for level in LEVELS:
            subset = frame[(frame.model == model) & (frame.level == level)]
            k, n = int(subset.correct.sum()), len(subset)
            cells.append(pct_ci(k/n, wilson(k,n)))
        model_table.append(f"| {model} | " + " | ".join(cells) + " |")
    confusion = []
    for i, level in enumerate(LEVELS):
        cells = [str(rel["pairs"][i, j]) if j >= i else "—" for j in range(4)]
        confusion.append(f"| {level} | " + " | ".join(cells) + " |")
    diff = questions[questions.level == "Easy"].correctness.mean() - questions[questions.level == "Challenging"].correctness.mean()
    diff_ci = interval(boot_means["Easy"] - boot_means["Challenging"])
    mismatches = rel["n_pairs"] - int(np.trace(rel["pairs"]))
    ch_hard = rel["pairs"][2, 3]
    hard_pairs = int(rel["pairs"][:, 3].sum())
    snapshot = hashlib.sha256()
    for path in [raw_path, pdf_path] + paths:
        snapshot.update(path.relative_to(ROOT).as_posix().encode())
        snapshot.update(hashlib.sha256(path.read_bytes()).digest())
    pdf_note = (f"pypdf tìm thấy **19,8% ở trang {pdf_hits[0][0]}**; câu văn nói nhãn bất đồng trên các item giống nhau, không ghi mẫu số."
                if pdf_hits else "pypdf không tìm thấy chuỗi 19,8% trong PDF hiện tại.")
    missing_note = "; ".join(f"`{qid}` → `{fate}`" for qid, fate in missing.items()) or "không có"
    dedup_n = sum(fate == "dedup: cleaning stages 12/14" for fate in missing.values())
    if dedup_n:
        missing_note += (f". Theo `reports/eval/raw/fates.json`, {dedup_n} ID này bị loại như bản trùng ở "
                         "cleaning stage 12/14 (dedup sau chuẩn hóa và bỏ khác biệt khoảng trắng), hai stage "
                         "được thêm sau khi split đóng băng; bản được giữ của mỗi cặp vẫn nằm trong dữ liệu sạch")
    level_acc = questions.groupby("level").correctness.mean()

    def vi_count(value):
        return f"{value:,}".replace(",", ".")

    def vi_pct(value, digits=1):
        return f"{100 * value:.{digits}f}%".replace(".", ",")

    report = f"""# VM14K — kiểm tra nhãn độ khó

Sinh bằng `python scripts/analysis/difficulty_labels.py`. Chỉ đọc dữ liệu và log sẵn có; không gọi model.
Phụ thuộc: numpy {np.__version__}, pandas {pd.__version__}; **scipy {scipy.__version__}, statsmodels {statsmodels.__version__}, pypdf {pypdf.__version__}** (đều khai báo trong `requirements.txt`).
Fingerprint SHA-256 của manifest đường dẫn + nội dung đầu vào: `{snapshot.hexdigest()}`. Bootstrap {BOOTSTRAPS:,} lần, seed {SEED}; mọi CI dưới đây là 95%.

## 1. Độ nhất quán trong bản phát hành thô

Đọc `data/raw/data-processed-shuffled0.jsonl` (**{len(raw):,} dòng**). Import trực tiếp `group_key` từ `vm14k_dupes_and_contradictions.py`, kiểm tra nó dùng đúng `dedup_utils.normalize_vietnamese`: khóa là câu hỏi chuẩn hóa + tuple phương án chuẩn hóa đã sắp xếp (giữ số lần phương án xuất hiện, bỏ qua thứ tự). Không gom theo ID hay khóa đáp án.

- **{rel['groups']:,} nhóm có ≥2 bản sao**, chứa **{rel['rows']:,}/{len(raw):,} dòng = {100*rel['rows']/len(raw):.2f}%**. Phân bố kích thước (số bản sao: số nhóm): {rel['sizes']}.
- **{rel['bad']}/{rel['groups']:,} nhóm = {100*rel['bad']/rel['groups']:.2f}%** có >1 nhãn. Các nhóm này chứa {rel['bad_rows']}/{rel['rows']:,} dòng bản sao = {100*rel['bad_rows']/rel['rows']:.2f}% (hoặc {rel['bad_rows']}/{len(raw):,} dòng toàn bộ = {100*rel['bad_rows']/len(raw):.2f}%). Đây là dòng *thuộc nhóm bất nhất*, không phải số nhãn được chứng minh sai.
- Lấy mọi cặp không thứ tự trong từng nhóm: mẫu số **Σ nᵢ(nᵢ−1)/2 = {rel['n_pairs']:,} cặp**. Đồng ý **{int(np.trace(rel['pairs'])):,}/{rel['n_pairs']:,} = {100*rel['agreement']:.2f}%**; bất đồng **{mismatches}/{rel['n_pairs']:,} = {100*(1-rel['agreement']):.2f}%**. Nhóm lớn đóng góp nhiều cặp hơn.

Ma trận cặp không thứ tự, mỗi cặp chỉ đếm một lần (đường chéo: đồng ý; tam giác trên: bất đồng, không biểu thị hướng đổi nhãn):

| Nhãn | Easy | Medium | Challenging | Hard |
|---|---:|---:|---:|---:|
{chr(10).join(confusion)}

Challenging↔Hard: **{ch_hard}/{rel['n_pairs']:,} cặp**; **{ch_hard}/{mismatches} cặp bất đồng**; **{ch_hard}/{hard_pairs} cặp có ít nhất một bản sao Hard**.

Không có hai người/lần gán nhãn định danh cố định, nên Cohen kappa theo “bản sao thứ nhất/thứ hai” là tùy tiện. Báo kappa không trọng số:

- **Fleiss tổng quát, nhóm có trọng số bằng nhau: κ = {rel['fleiss']:.4f}** trên {rel['groups']:,} nhóm/{rel['rows']:,} nhãn. P̄ = trung bình tỷ lệ cặp đồng ý trong từng nhóm = {rel['group_agreement']:.6f}; pⱼ = trung bình nᵢⱼ/nᵢ trên nhóm; Pₑ=Σpⱼ²={rel['chance']:.6f}; κ=(P̄−Pₑ)/(1−Pₑ). Công thức nêu rõ vì số bản sao thay đổi, không dùng Fleiss chuẩn cố định số người chấm cho toàn bộ nhóm.
- **Kappa theo mọi cặp, cặp có trọng số bằng nhau: κ = {rel['pair_kappa']:.4f}** trên {rel['n_pairs']:,} cặp. pⱼ = Σᵢ(nᵢ−1)nᵢⱼ / (2×{rel['n_pairs']:,}) là phân bố nhãn ở hai đầu cặp; Pₑ={rel['pair_chance']:.6f}. Đây là phiên bản theo cặp của phép hiệu chỉnh ngẫu nhiên, không phải Cohen với hai người chấm độc lập.
- Kiểm tra bằng **Fleiss chuẩn chỉ trên {rel['two_n']} nhóm đúng hai bản sao** ({2*rel['two_n']} nhãn): **κ = {rel['two_kappa']:.4f}**.

**Đối chiếu audit notes:** {pdf_note} Tái hiện **{rel['bad']}/{rel['groups']:,} = {100*rel['bad']/rel['groups']:.2f}% → 19,8%**. Với định nghĩa gom nhóm này, mẫu số phải là **nhóm bản sao**, không phải dòng hoặc cặp; PDF không đủ thông tin để xác nhận mã tính gốc. Không gọi đây là lỗi 19,8% của toàn bộ nhãn. Nhãn khác nhau chứng minh thiếu nhất quán của artifact; thiếu provenance nên không chứng minh cùng một LLM đã tự mâu thuẫn ở các lần gán nhãn. Chuẩn hóa cũng có thể gộp biến thể ký hiệu/dấu câu có ý nghĩa y khoa.

## 2. Nhãn có phân biệt câu khó với bảy LLM không?

Nguồn: `data/cleaned/clean_final.jsonl`, `splits/split_v1.json`, bảy file `reports/eval/runs/*__paper__test.jsonl` được liệt kê cố định trong script (đúng bảy model ở bảng dưới). Split có **{all_test_n:,} ID test** nhưng **{len(missing)} ID vắng khỏi dữ liệu sạch hiện tại**; loại thêm **{pending_n} câu `contradiction_pending_review`** theo harness; còn **{len(questions):,} câu**, mỗi câu có đủ **7 model**, tổng **{len(frame):,} lượt trả lời**. Nemotron chạy dở không được dùng. ID vắng: {missing_note}.
Giữ record cuối có `error is None` theo thứ tự file cho mỗi ID; kiểm tra tập ID, nhãn, gold, cấu hình paper, thứ tự phương án và `correct`. Metadata thinking là `off` (hai run NVIDIA), `False` (Gemma-12B và hai Qwen), `null` (Llama/MedGemma); không coi `null` là bằng chứng độc lập rằng đã tắt thinking. Tự chấm `pred == answer` của dữ liệu sạch; **{unparsed} lượt không parse được tính sai**. Không có hai ID test trùng khóa nhóm nói trên.

| Mức | Số câu | Đúng / lượt trả lời | Accuracy, Wilson CI danh nghĩa | Accuracy, CI bootstrap theo câu |
|---|---:|---:|---|---|
{chr(10).join(table)}

Wilson gộp dùng mẫu số 7×số câu nhưng giả định độc lập lượt trả lời, **không điều chỉnh tương quan bảy model trên cùng câu**; dùng CI bootstrap theo câu để diễn giải accuracy gộp. Bootstrap lấy lại nguyên vector bảy kết quả, phân tầng theo nhãn với số câu mỗi mức giữ nguyên; model là bảy hệ thống cố định, không lấy mẫu lại model.

Accuracy từng model và Wilson CI (%); mẫu số **mỗi ô** lần lượt Easy=544, Medium=935, Challenging=166, Hard=13 câu:

| Model | Easy | Medium | Challenging | Hard |
|---|---|---|---|---|
{chr(10).join(model_table)}

**Logistic có hiệu ứng cố định theo model:** `correct ~ C(level) + C(model)`, Easy làm chuẩn; GLM nhị thức, sandwich SE gom cụm theo **{len(questions):,} câu**, trên **{len(frame):,} lượt trả lời**, có hiệu chỉnh mẫu hữu hạn. Mô hình chỉ điều chỉnh khác biệt baseline giữa model, không điều chỉnh chuyên khoa/định dạng và không ước lượng quan hệ nhân quả.

| So sánh | Odds ratio [CI gom cụm] | p Wald hai phía |
|---|---|---:|
{chr(10).join(coef_rows)}

So sánh chính **Easy / Challenging: OR={np.exp(beta):.3f} [{or_ci[0]:.3f}; {or_ci[1]:.3f}], p={fit.pvalues[term]:.4f}**. Chênh accuracy thực nghiệm Easy−Challenging = **{100*diff:.2f} điểm phần trăm**, CI bootstrap theo câu **[{100*diff_ci[0]:.2f}; {100*diff_ci[1]:.2f}]**. Kiểm định chung ba hệ số nhãn: χ²(3)={float(omnibus.statistic):.3f}, p={float(omnibus.pvalue):.4f}. Không bác bỏ ở mức 0,05 không chứng minh tương đương hay hoàn toàn không có tác dụng.

**Spearman:** ordinal Easy=0, Medium=1, Challenging=2, Hard=3; đối chiếu với **mean(correctness của 7 model) trên từng câu**, nên rho âm là hướng mong đợi. Nếu biểu diễn độ khó thực nghiệm bằng tỷ lệ sai (1−mean correctness), rho và hai cận CI đổi dấu/đảo thứ tự, p giữ nguyên. Dùng rank trung bình khi hòa; p hai phía xấp xỉ của scipy; CI percentile bootstrap theo câu, lấy lại cả nhãn và vector kết quả.

| Tập | Mẫu số câu | rho [CI] | p |
|---|---:|---|---:|
{chr(10).join(rho_rows)}

**Hard chỉ có 13 câu**: 91 lượt không phải 91 câu độc lập. Báo riêng, không gộp với Challenging; CI rộng và SE gom cụm của hệ số Hard dựa trên rất ít câu ở mức này, nên không kết luận thứ hạng Hard hay lấy nó làm bằng chứng chính. Các mức còn lại không cho thấy xu hướng accuracy giảm rõ theo độ khó. Kết quả chỉ nói về khóa hiện có, tập test đã làm sạch và bảy LLM/cấu hình này; “khó với các LLM này” ≠ “khó với bác sĩ”. Lỗi khóa, chuyên khoa, số phương án, kiến thức huấn luyện có thể ảnh hưởng; chưa có correctness của bác sĩ để kiểm định độ khó lâm sàng.

## Kết luận cho bài viết

Các câu có thể dùng:

1. “Trong bản phát hành {vi_count(len(raw))} dòng, {rel['bad']}/{vi_count(rel['groups'])} nhóm câu hỏi và bộ phương án giống nhau sau chuẩn hóa ({vi_pct(rel['bad'] / rel['groups'], 2)}) có nhãn độ khó không nhất quán; độ đồng ý trên {rel['n_pairs']:,} cặp bản sao là {100*rel['agreement']:.2f}% và Fleiss tổng quát với trọng số bằng nhau theo nhóm là {rel['fleiss']:.3f}.”
2. “Trên {vi_count(len(questions))} câu test được chấm bởi bảy LLM cố định, accuracy trung bình ở Easy, Medium và Challenging lần lượt là {vi_pct(level_acc['Easy'])}, {vi_pct(level_acc['Medium'])} và {vi_pct(level_acc['Challenging'])}; chênh Easy−Challenging là {100*diff:.2f} điểm phần trăm (CI {ci_percent:.0f}% [{100*diff_ci[0]:.2f}; {100*diff_ci[1]:.2f}]).”
3. “Sau khi điều chỉnh hiệu ứng cố định theo model và gom cụm theo câu hỏi, OR đúng của Easy so với Challenging là {np.exp(beta):.3f} (CI {ci_percent:.0f}% [{or_ci[0]:.3f}; {or_ci[1]:.3f}]); tương quan Spearman giữa nhãn thứ bậc và mean correctness của bảy LLM trên từng câu là {rho_results[0][0]:.4f}.”
4. “Các kết quả này cho thấy nhãn thiếu nhất quán giữa bản sao và bằng chứng phân biệt độ khó đối với các LLM được khảo sát còn yếu; chúng không xác nhận hay phủ định độ khó đối với bác sĩ. Mức Hard (13 câu) chưa đủ để kết luận riêng chắc chắn.”
"""
    destination = ROOT / "reports/analysis/DIFFICULTY_LABELS.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(report, encoding="utf-8")
    print(f"Wrote {destination}")
    print(f"Duplicate groups: {rel['bad']}/{rel['groups']} inconsistent; agreement {rel['agreement']:.6f}; Fleiss {rel['fleiss']:.6f}")
    print(f"Easy/Challenging OR {np.exp(beta):.6f}, CI {or_ci}; Spearman {rho_results[0][0]:.6f}")


if __name__ == "__main__":
    main()

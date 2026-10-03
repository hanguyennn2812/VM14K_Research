# VM14K — kiểm tra nhãn độ khó

Sinh bằng `python scripts/analysis/difficulty_labels.py`. Chỉ đọc dữ liệu và log sẵn có; không gọi model.
Phụ thuộc: numpy 2.3.2, pandas 2.3.3; **scipy 1.17.1, statsmodels 0.15.0, pypdf 6.10.1** (đều khai báo trong `requirements.txt`).
Fingerprint SHA-256 của manifest đường dẫn + nội dung đầu vào: `a351c79c6cc8771f4903f33c7c853dd7840fd57b355d3838c61d05f2b718884a`. Bootstrap 5,000 lần, seed 20261003; mọi CI dưới đây là 95%.

## 1. Độ nhất quán trong bản phát hành thô

Đọc `data/raw/data-processed-shuffled0.jsonl` (**12,488 dòng**). Import trực tiếp `group_key` từ `vm14k_dupes_and_contradictions.py`, kiểm tra nó dùng đúng `dedup_utils.normalize_vietnamese`: khóa là câu hỏi chuẩn hóa + tuple phương án chuẩn hóa đã sắp xếp (giữ số lần phương án xuất hiện, bỏ qua thứ tự). Không gom theo ID hay khóa đáp án.

- **1,125 nhóm có ≥2 bản sao**, chứa **2,450/12,488 dòng = 19.62%**. Phân bố kích thước (số bản sao: số nhóm): {2: 959, 3: 138, 4: 24, 5: 2, 6: 2}.
- **223/1,125 nhóm = 19.82%** có >1 nhãn. Các nhóm này chứa 495/2,450 dòng bản sao = 20.20% (hoặc 495/12,488 dòng toàn bộ = 3.96%). Đây là dòng *thuộc nhóm bất nhất*, không phải số nhãn được chứng minh sai.
- Lấy mọi cặp không thứ tự trong từng nhóm: mẫu số **Σ nᵢ(nᵢ−1)/2 = 1,567 cặp**. Đồng ý **1,294/1,567 = 82.58%**; bất đồng **273/1,567 = 17.42%**. Nhóm lớn đóng góp nhiều cặp hơn.

Ma trận cặp không thứ tự, mỗi cặp chỉ đếm một lần (đường chéo: đồng ý; tam giác trên: bất đồng, không biểu thị hướng đổi nhãn):

| Nhãn | Easy | Medium | Challenging | Hard |
|---|---:|---:|---:|---:|
| Easy | 302 | 179 | 2 | 0 |
| Medium | — | 886 | 80 | 4 |
| Challenging | — | — | 104 | 8 |
| Hard | — | — | — | 2 |

Challenging↔Hard: **8/1,567 cặp**; **8/273 cặp bất đồng**; **8/14 cặp có ít nhất một bản sao Hard**.

Không có hai người/lần gán nhãn định danh cố định, nên Cohen kappa theo “bản sao thứ nhất/thứ hai” là tùy tiện. Báo kappa không trọng số:

- **Fleiss tổng quát, nhóm có trọng số bằng nhau: κ = 0.6471** trên 1,125 nhóm/2,450 nhãn. P̄ = trung bình tỷ lệ cặp đồng ý trong từng nhóm = 0.814163; pⱼ = trung bình nᵢⱼ/nᵢ trên nhóm; Pₑ=Σpⱼ²=0.473437; κ=(P̄−Pₑ)/(1−Pₑ). Công thức nêu rõ vì số bản sao thay đổi, không dùng Fleiss chuẩn cố định số người chấm cho toàn bộ nhóm.
- **Kappa theo mọi cặp, cặp có trọng số bằng nhau: κ = 0.6561** trên 1,567 cặp. pⱼ = Σᵢ(nᵢ−1)nᵢⱼ / (2×1,567) là phân bố nhãn ở hai đầu cặp; Pₑ=0.493436. Đây là phiên bản theo cặp của phép hiệu chỉnh ngẫu nhiên, không phải Cohen với hai người chấm độc lập.
- Kiểm tra bằng **Fleiss chuẩn chỉ trên 959 nhóm đúng hai bản sao** (1918 nhãn): **κ = 0.6365**.

**Đối chiếu audit notes:** pypdf tìm thấy **19,8% ở trang 8**; câu văn nói nhãn bất đồng trên các item giống nhau, không ghi mẫu số. Tái hiện **223/1,125 = 19.82% → 19,8%**. Với định nghĩa gom nhóm này, mẫu số phải là **nhóm bản sao**, không phải dòng hoặc cặp; PDF không đủ thông tin để xác nhận mã tính gốc. Không gọi đây là lỗi 19,8% của toàn bộ nhãn. Nhãn khác nhau chứng minh thiếu nhất quán của artifact; thiếu provenance nên không chứng minh cùng một LLM đã tự mâu thuẫn ở các lần gán nhãn. Chuẩn hóa cũng có thể gộp biến thể ký hiệu/dấu câu có ý nghĩa y khoa.

## 2. Nhãn có phân biệt câu khó với bảy LLM không?

Nguồn: `data/cleaned/clean_final.jsonl`, `splits/split_v1.json`, bảy file `reports/eval/runs/*__paper__test.jsonl` được liệt kê cố định trong script (đúng bảy model ở bảng dưới). Split có **1,662 ID test** nhưng **4 ID vắng khỏi dữ liệu sạch hiện tại**; loại thêm **0 câu `contradiction_pending_review`** theo harness; còn **1,658 câu**, mỗi câu có đủ **7 model**, tổng **11,606 lượt trả lời**. Nemotron chạy dở không được dùng. ID vắng: `26a6a66f0ca34282aaf411d3cd26185f` → `dedup: cleaning stages 12/14`; `2eaa5ad48c054a84abb28bccdfdf66cd` → `dedup: cleaning stages 12/14`; `56effd0a6f2a40ebb815b47625543738` → `dedup: cleaning stages 12/14`; `ebc900a646584ccfa8a4d21c3914eb4c` → `dedup: cleaning stages 12/14`. Theo `reports/eval/raw/fates.json`, 4 ID này bị loại như bản trùng ở cleaning stage 12/14 (dedup sau chuẩn hóa và bỏ khác biệt khoảng trắng), hai stage được thêm sau khi split đóng băng; bản được giữ của mỗi cặp vẫn nằm trong dữ liệu sạch.
Giữ record cuối có `error is None` theo thứ tự file cho mỗi ID; kiểm tra tập ID, nhãn, gold, cấu hình paper, thứ tự phương án và `correct`. Metadata thinking là `off` (hai run NVIDIA), `False` (Gemma-12B và hai Qwen), `null` (Llama/MedGemma); không coi `null` là bằng chứng độc lập rằng đã tắt thinking. Tự chấm `pred == answer` của dữ liệu sạch; **26 lượt không parse được tính sai**. Không có hai ID test trùng khóa nhóm nói trên.

| Mức | Số câu | Đúng / lượt trả lời | Accuracy, Wilson CI danh nghĩa | Accuracy, CI bootstrap theo câu |
|---|---:|---:|---|---|
| Easy | 544 | 2301/3808 | 60.4% [58.9; 62.0] | 60.4% [57.8; 63.0] |
| Medium | 935 | 3831/6545 | 58.5% [57.3; 59.7] | 58.5% [56.5; 60.6] |
| Challenging | 166 | 687/1162 | 59.1% [56.3; 61.9] | 59.1% [54.3; 63.9] |
| Hard | 13 | 46/91 | 50.5% [40.5; 60.6] | 50.5% [36.3; 64.8] |

Wilson gộp dùng mẫu số 7×số câu nhưng giả định độc lập lượt trả lời, **không điều chỉnh tương quan bảy model trên cùng câu**; dùng CI bootstrap theo câu để diễn giải accuracy gộp. Bootstrap lấy lại nguyên vector bảy kết quả, phân tầng theo nhãn với số câu mỗi mức giữ nguyên; model là bảy hệ thống cố định, không lấy mẫu lại model.

Accuracy từng model và Wilson CI (%); mẫu số **mỗi ô** lần lượt Easy=544, Medium=935, Challenging=166, Hard=13 câu:

| Model | Easy | Medium | Challenging | Hard |
|---|---|---|---|---|
| DeepSeek-v4.1-flash | 72.8% [68.9; 76.4] | 70.4% [67.4; 73.2] | 72.3% [65.0; 78.5] | 69.2% [42.4; 87.3] |
| Gemma-4-31B | 72.1% [68.1; 75.7] | 72.0% [69.0; 74.8] | 69.3% [61.9; 75.8] | 61.5% [35.5; 82.3] |
| Gemma-4-12B | 60.7% [56.5; 64.7] | 59.3% [56.1; 62.4] | 61.4% [53.9; 68.5] | 53.8% [29.1; 76.8] |
| Qwen3.5-9B | 62.3% [58.2; 66.3] | 63.9% [60.7; 66.9] | 60.8% [53.3; 67.9] | 53.8% [29.1; 76.8] |
| Qwen3-8B | 56.2% [52.1; 60.4] | 53.4% [50.2; 56.5] | 54.2% [46.6; 61.6] | 69.2% [42.4; 87.3] |
| Llama-3.1-8B | 48.0% [43.8; 52.2] | 45.8% [42.6; 49.0] | 50.0% [42.5; 57.5] | 23.1% [8.2; 50.3] |
| MedGemma-4B | 50.9% [46.7; 55.1] | 45.1% [42.0; 48.3] | 45.8% [38.4; 53.4] | 23.1% [8.2; 50.3] |

**Logistic có hiệu ứng cố định theo model:** `correct ~ C(level) + C(model)`, Easy làm chuẩn; GLM nhị thức, sandwich SE gom cụm theo **1,658 câu**, trên **11,606 lượt trả lời**, có hiệu chỉnh mẫu hữu hạn. Mô hình chỉ điều chỉnh khác biệt baseline giữa model, không điều chỉnh chuyên khoa/định dạng và không ước lượng quan hệ nhân quả.

| So sánh | Odds ratio [CI gom cụm] | p Wald hai phía |
|---|---|---:|
| Medium / Easy | 0.922 [0.798; 1.064] | 0.2650 |
| Challenging / Easy | 0.945 [0.746; 1.198] | 0.6417 |
| Hard / Easy | 0.659 [0.356; 1.218] | 0.1830 |

So sánh chính **Easy / Challenging: OR=1.058 [0.834; 1.341], p=0.6417**. Chênh accuracy thực nghiệm Easy−Challenging = **1.30 điểm phần trăm**, CI bootstrap theo câu **[-4.06; 6.62]**. Kiểm định chung ba hệ số nhãn: χ²(3)=2.633, p=0.4518. Không bác bỏ ở mức 0,05 không chứng minh tương đương hay hoàn toàn không có tác dụng.

**Spearman:** ordinal Easy=0, Medium=1, Challenging=2, Hard=3; đối chiếu với **mean(correctness của 7 model) trên từng câu**, nên rho âm là hướng mong đợi. Nếu biểu diễn độ khó thực nghiệm bằng tỷ lệ sai (1−mean correctness), rho và hai cận CI đổi dấu/đảo thứ tự, p giữ nguyên. Dùng rank trung bình khi hòa; p hai phía xấp xỉ của scipy; CI percentile bootstrap theo câu, lấy lại cả nhãn và vector kết quả.

| Tập | Mẫu số câu | rho [CI] | p |
|---|---:|---|---:|
| Đủ bốn mức | 1658 | -0.0269 [-0.0745; 0.0220] | 0.2733 |
| Bỏ Hard (độ nhạy) | 1645 | -0.0225 [-0.0709; 0.0261] | 0.3615 |

**Hard chỉ có 13 câu**: 91 lượt không phải 91 câu độc lập. Báo riêng, không gộp với Challenging; CI rộng và SE gom cụm của hệ số Hard dựa trên rất ít câu ở mức này, nên không kết luận thứ hạng Hard hay lấy nó làm bằng chứng chính. Các mức còn lại không cho thấy xu hướng accuracy giảm rõ theo độ khó. Kết quả chỉ nói về khóa hiện có, tập test đã làm sạch và bảy LLM/cấu hình này; “khó với các LLM này” ≠ “khó với bác sĩ”. Lỗi khóa, chuyên khoa, số phương án, kiến thức huấn luyện có thể ảnh hưởng; chưa có correctness của bác sĩ để kiểm định độ khó lâm sàng.

## Kết luận cho bài viết

Các câu có thể dùng:

1. “Trong bản phát hành 12.488 dòng, 223/1.125 nhóm câu hỏi và bộ phương án giống nhau sau chuẩn hóa (19,82%) có nhãn độ khó không nhất quán; độ đồng ý trên 1,567 cặp bản sao là 82.58% và Fleiss tổng quát với trọng số bằng nhau theo nhóm là 0.647.”
2. “Trên 1.658 câu test được chấm bởi bảy LLM cố định, accuracy trung bình ở Easy, Medium và Challenging lần lượt là 60,4%, 58,5% và 59,1%; chênh Easy−Challenging là 1.30 điểm phần trăm (CI 95% [-4.06; 6.62]).”
3. “Sau khi điều chỉnh hiệu ứng cố định theo model và gom cụm theo câu hỏi, OR đúng của Easy so với Challenging là 1.058 (CI 95% [0.834; 1.341]); tương quan Spearman giữa nhãn thứ bậc và mean correctness của bảy LLM trên từng câu là -0.0269.”
4. “Các kết quả này cho thấy nhãn thiếu nhất quán giữa bản sao và bằng chứng phân biệt độ khó đối với các LLM được khảo sát còn yếu; chúng không xác nhận hay phủ định độ khó đối với bác sĩ. Mức Hard (13 câu) chưa đủ để kết luận riêng chắc chắn.”

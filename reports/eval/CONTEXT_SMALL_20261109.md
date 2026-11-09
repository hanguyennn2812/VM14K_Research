# RAG cho decision model 9B (d3-flash) ở chuyên khoa Truyền nhiễm — kết quả 09/11/2026

*Claude Sonnet 5.5, pha thực thi của `docs/research/PLAN_2026-11-09.md`. Chỉ dùng val và probe. **Test VM14K không bị chạm** (T6 không chạy vì H1 không đạt).*

## Tóm tắt

- **H1 KHÔNG ĐẠT.** d3-flash 9B + 3 câu train + 3 đoạn MoH đạt 181/245 = 73,9% trên val Truyền nhiễm, so với 175/245 = 71,4% không ngữ cảnh (Δ +2,4, bootstrap CI [−1,6; +6,5], McNemar p = 0,34). Không điều kiện nào có CI loại được 0; cao nhất `shotsemb+docs` 74,3% (Δ +2,9, p = 0,30). Ngưỡng là ≥ 196/245. Với gate `top_sim` (chọn trên val) cao nhất là 75,9%, vẫn dưới ngưỡng. Để so: d3 27B + cùng loại ngữ cảnh đạt 198/245 = 80,8% (bảng 1 PLAN).
- **H2 ĐẠT.** Trên probe 369 cặp (2 phương án, mốc ngẫu nhiên 50,0%, luôn-A 49,9%): đóng sách 77,8%, mở sách (top-3 MoH) 97,3%, Δ +19,5 [+15,4; +23,6], p = 5e-19; đoạn nguồn của cặp (mức trần) 100%. Model 9B **dùng được bằng chứng** MoH khi bằng chứng có mặt.
- **H3 không bị bác bỏ nhưng không có sức nặng.** Với `shots+docs`, nhóm câu có độ giống câu train tốt nhất < 0,3 (n = 161) có Δ +1,9 [−3,7; +7,5], CI chứa 0; mọi con số ở bảng 3 đều nhỏ và không có ý nghĩa thống kê.
- **Đọc theo bảng "Đọc kết quả" (mục 3 PLAN): hàng "Không / Đạt".** Model dùng được bằng chứng, nhưng văn bản MoH cùng câu train gần nhất không phủ đề VM14K đủ để nâng 9B lên mốc paper. Kế hoạch ghi: dừng hướng MoH cho VM14K, kể cả CPT; không sang RAFT (RAFT chỉ khi H2 không đạt).
- Lưu ý đọc H2: probe được sinh từ chính văn bản MoH và truy hồi chạy trên mọi đoạn MoH, nên nó đo "khi đoạn đúng có mặt model có dùng không" (có), không đo độ phủ của MoH đối với đề thi. Độ phủ đối với đề thi là điều H1 đo, và kết quả là chưa đủ.

## Cấu hình chốt (T4, viết trước mọi lần chấm test)

- Model: `vllm-sr/d3-flash` (9B), fp16 trên 2×T4 (xem "Lệch kế hoạch").
- Điều kiện cao nhất trên val: `shotsemb+docs` (182/245, 74,3%); có gate `top_sim ≥ 0,4` thì 75,9%. Chênh lệch giữa các điều kiện có ngữ cảnh đều không có ý nghĩa thống kê, nên không có cơ sở chọn một cấu hình "thắng".
- **Không chấm test.** Điều kiện chạy T6 là H1 đạt; H1 không đạt nên không có cấu hình nào để chốt cho test. Phần "Test" trong bảng bên dưới vì thế không có.
- T5 (reranker) không chạy: điều kiện là H1 sát ngưỡng 77–80%, còn thực tế là 74%.

## Kiểm tra trước (T0)

- `NVIDIA_API_KEY` sống. `/embeddings` với `nvidia/nemotron-3.5-embed-8b` trả lời bình thường với **một** văn bản mỗi yêu cầu (~1,2 giây); với 2 văn bản trở lên thì HTTP 500 ngắt quãng, nên `export_context_bodies.py` nhúng từng câu một (6 luồng). Phần nhúng 7.313 câu train mất khoảng 25–30 phút.
- `data/interim/moh_all_emb.npz` có sẵn (16.049 đoạn × 4096).
- Quota GPU Kaggle: CLI không in ra số giờ còn lại; kernel push không bị từ chối, và cả hai kernel (smoke + full) chạy xong tổng cộng dưới 30 phút GPU.
- Bốn số có chú thích ¹ tính lại bằng Python từ các file run: **181/245, 166/232, 153/232, 198/245** (khớp PLAN).

## Lệch kế hoạch (cần người kiểm tra biết)

1. **Cách nạp d3-flash.** Mã từ xa của d3 từ chối `dtype=float16` và `device_map` nhiều thiết bị (ValueError/TypeError), và backbone bf16 (~19 GB) không vừa một T4. `scripts/eval/kaggle_decision.py` thay vào đó nạp qua `d3_runtime.D3` của chính repo model, thay loader của backbone bằng fp16 trải 2 GPU, tắt đường nhanh `d3_fast`, chuyển readout sang GPU cuối. Kernel thật chạy được; nhân fla/causal-conv1d rơi về bản PyTorch (chậm hơn nhưng 0,18 giây/câu cho `zero`, ~1,3 giây/câu cho ngữ cảnh dài).
2. **Cổng smoke.** Kernel smoke 50 câu đầu của `zero`: trùng 46/50 = 92% với dự đoán H100 bf16, **dưới ngưỡng 95%** của PLAN; không NaN, không lỗi. Cả 4 câu lệch đều là hoà sát nút (hai xác suất cao nhất cách nhau ≤ 0,05 ở cả hai bản; xác suất fp16 và bf16 lệch ≤ 0,05). Theo luật đúng chữ, bước kế là T2b (Qwen3.5-9B logit), nhưng T2b là model khác (không phải d3-flash) nên không trả lời được câu hỏi của kế hoạch. Tôi **nới ngưỡng cổng xuống 0,90 cho kernel đầy đủ và chạy tiếp**, ghi lại ở đây. Sau đó đo trên cả 245 câu: `zero` fp16 trùng dự đoán H100 ở **235/245 = 95,9%**, tức là đạt ngưỡng 95% trên mẫu lớn hơn. Hệ quả phải nhớ: `zero` fp16 = 175/245 (71,4%) còn `zero` H100 bf16 = 181/245 (73,9%), cách nhau 6 câu. Mọi Δ trong báo cáo đều so cặp trong cùng môi trường fp16, nên không bị ảnh hưởng, nhưng không so tuyệt đối số fp16 với số H100 được.
3. **Embedding câu train.** Cả câu train và câu val đều nhúng với `input_type=query` (đối xứng câu-với-câu); `shotsemb` dùng cosine này. `data/interim/vm14k_train_emb.npz` (55 MB) là cache.
4. Không có T2b, T5, T6.

## Lưu ý về smoke CPT (để không bị đọc sai)

`reports/eval/runs/cpt__Qwen_Qwen3.5-9B__smoke__{before,after}.jsonl` giống hệt nhau từng byte. Nguyên nhân (người kiểm tra đã xác nhận) nằm ở `scripts/training/modal_jevtorch.py::cpt_probe` (dòng ~304): với `--limit 16` mỗi epoch chỉ có 4 micro-batch mà `accum = 8`, bộ đếm `(start // batch_size + 1) % accum` reset mỗi epoch, nên `optimizer.step()` không bao giờ chạy; bản đầy đủ thì mang gradient thừa qua epoch và bỏ phần dư cuối. Vậy smoke đó **không train bước nào**, không phải bằng chứng rằng "CPT không có tác dụng". Phiên này không sửa file (đúng phạm vi) và không chạy CPT.

## Bảng kết quả (sinh bởi `scripts/eval/analyze_context.py`)

Mốc: ngẫu nhiên = trung bình 1/n_options của đúng các câu đó; luôn-A = tỉ lệ khoá là A. CI: Wilson cho tỉ lệ; bootstrap cặp (2.000 lần) và McNemar exact cho Δ.

<!-- TABLES START (generated by scripts/eval/analyze_context.py) -->

### Bảng 1: val Truyền nhiễm, n = 245

Mốc ngẫu nhiên 26.6%, luôn chọn A 25.7% (cùng 245 câu). 'wins/losses' = số câu điều kiện đúng mà zero sai / số câu zero đúng mà điều kiện sai.

| condition | n | right | % | Wilson 95% CI | Δ vs zero [bootstrap 95% CI] | wins/losses | McNemar p |
|---|---:|---:|---:|---:|---:|---:|---:|
| zero | 245 | 175 | 71.4 | [65.5, 76.7] | | | | |
| shots | 245 | 179 | 73.1 | [67.2, 78.2] | +1.6 [-2.9, +6.1] | 18/14 | 0.6 |
| docs | 245 | 177 | 72.2 | [66.3, 77.5] | +0.8 [-4.1, +5.7] | 20/18 | 0.87 |
| shots+docs | 245 | 181 | 73.9 | [68.0, 79.0] | +2.4 [-1.6, +6.5] | 17/11 | 0.34 |
| shotsemb | 245 | 179 | 73.1 | [67.2, 78.2] | +1.6 [-2.4, +6.1] | 15/11 | 0.56 |
| shotsemb+docs | 245 | 182 | 74.3 | [68.5, 79.4] | +2.9 [-1.6, +7.3] | 20/13 | 0.3 |

### Bảng 2: gate theo `top_sim` (chọn t trên val: độ đúng cao nhất, t nhỏ nhất khi hoà)

`docs` (else `zero`); t chọn = 0.4

| t | câu có đoạn MoH | độ đúng % |
|---:|---:|---:|
| 0.0 | 100% | 72.2 |
| 0.35 | 79% | 73.1 |
| 0.4 | 62% | 74.3 |
| 0.45 | 41% | 73.9 |
| 0.5 | 20% | 72.2 |
| 0.55 | 12% | 72.7 |

`shots+docs` (else `shots`); t chọn = 0.5

| t | câu có đoạn MoH | độ đúng % |
|---:|---:|---:|
| 0.0 | 100% | 73.9 |
| 0.35 | 79% | 73.1 |
| 0.4 | 62% | 74.3 |
| 0.45 | 41% | 74.3 |
| 0.5 | 20% | 75.1 |
| 0.55 | 12% | 75.1 |

`shotsemb+docs` (else `shotsemb`); t chọn = 0.4

| t | câu có đoạn MoH | độ đúng % |
|---:|---:|---:|
| 0.0 | 100% | 74.3 |
| 0.35 | 79% | 75.5 |
| 0.4 | 62% | 75.9 |
| 0.45 | 41% | 75.9 |
| 0.5 | 20% | 75.1 |
| 0.55 | 12% | 74.3 |

### Bảng 3 (H3): Δ so với zero theo độ giống câu train tốt nhất (TF-IDF `shot_sim_max` ≥ 0.3)

| condition | nhóm | n | zero % | điều kiện % | Δ [bootstrap 95% CI] | wins/losses | p |
|---|---|---:|---:|---:|---:|---:|---:|
| shots | ≥ 0.3 | 84 | 70.2 | 71.4 | +1.2 [-6.0, +8.3] | 5/4 | 1 |
| shots | < 0.3 | 161 | 72.0 | 73.9 | +1.9 [-4.3, +8.1] | 13/10 | 0.68 |
| docs | ≥ 0.3 | 84 | 70.2 | 70.2 | +0.0 [-8.3, +8.3] | 6/6 | 1 |
| docs | < 0.3 | 161 | 72.0 | 73.3 | +1.2 [-5.0, +7.5] | 14/12 | 0.85 |
| shots+docs | ≥ 0.3 | 84 | 70.2 | 73.8 | +3.6 [-3.6, +10.7] | 6/3 | 0.51 |
| shots+docs | < 0.3 | 161 | 72.0 | 73.9 | +1.9 [-3.7, +7.5] | 11/8 | 0.65 |
| shotsemb | ≥ 0.3 | 84 | 70.2 | 69.0 | -1.2 [-8.3, +6.0] | 4/5 | 1 |
| shotsemb | < 0.3 | 161 | 72.0 | 75.2 | +3.1 [-1.9, +8.1] | 11/6 | 0.33 |
| shotsemb+docs | ≥ 0.3 | 84 | 70.2 | 72.6 | +2.4 [-6.0, +10.7] | 7/5 | 0.77 |
| shotsemb+docs | < 0.3 | 161 | 72.0 | 75.2 | +3.1 [-2.5, +8.7] | 13/8 | 0.38 |

### Bảng 4 (H2): probe fact-pair, n = 369

Mốc ngẫu nhiên 50.0%, luôn chọn A 49.9%. Ba nhóm chỉ để mô tả: không train gì nên đều là kiến thức 'chưa học'.

| condition | n | right | % | Wilson 95% CI | Δ vs zero [bootstrap 95% CI] | wins/losses | McNemar p |
|---|---:|---:|---:|---:|---:|---:|---:|
| zero | 369 | 287 | 77.8 | [73.3, 81.7] | | | | |
| docs | 369 | 359 | 97.3 | [95.1, 98.5] | +19.5 [+15.4, +23.6] | 75/3 | 5.2e-19 * |
| own | 369 | 369 | 100.0 | [99.0, 100.0] | +22.2 [+18.2, +26.6] | 82/0 | 4.1e-25 * |

Nhóm `control` (n = 107)

| condition | n | right | % | Wilson 95% CI | Δ vs zero [bootstrap 95% CI] | wins/losses | McNemar p |
|---|---:|---:|---:|---:|---:|---:|---:|
| zero | 107 | 92 | 86.0 | [78.2, 91.3] | | | | |
| docs | 107 | 105 | 98.1 | [93.4, 99.5] | +12.1 [+5.6, +19.6] | 14/1 | 0.00098 * |
| own | 107 | 107 | 100.0 | [96.5, 100.0] | +14.0 [+7.5, +21.5] | 15/0 | 6.1e-05 * |

Nhóm `new` (n = 133)

| condition | n | right | % | Wilson 95% CI | Δ vs zero [bootstrap 95% CI] | wins/losses | McNemar p |
|---|---:|---:|---:|---:|---:|---:|---:|
| zero | 133 | 99 | 74.4 | [66.4, 81.1] | | | | |
| docs | 133 | 128 | 96.2 | [91.5, 98.4] | +21.8 [+15.0, +29.3] | 29/0 | 3.7e-09 * |
| own | 133 | 133 | 100.0 | [97.2, 100.0] | +25.6 [+18.0, +33.1] | 34/0 | 1.2e-10 * |

Nhóm `seen` (n = 129)

| condition | n | right | % | Wilson 95% CI | Δ vs zero [bootstrap 95% CI] | wins/losses | McNemar p |
|---|---:|---:|---:|---:|---:|---:|---:|
| zero | 129 | 96 | 74.4 | [66.3, 81.2] | | | | |
| docs | 129 | 126 | 97.7 | [93.4, 99.2] | +23.3 [+16.3, +31.0] | 32/2 | 6.9e-08 * |
| own | 129 | 129 | 100.0 | [97.1, 100.0] | +25.6 [+18.6, +33.3] | 33/0 | 2.3e-10 * |

### Kết luận theo ngưỡng khai báo trước

- **H1** (`shots+docs` ≥ 196/245 và McNemar p < 0,05): 181/245 = 73.9%, Δ +2.4, p = 0.34 → **KHÔNG ĐẠT**.
- **H3** (Δ ở nhóm < 0.3 > 0): n = 161, Δ +1.9 [-3.7, +7.5] → **KHÔNG BÁC BỎ** (CI chứa 0).
- Điều kiện cao nhất trên val: `shotsemb+docs`. Bác bỏ H1 theo mục 3 (không điều kiện nào ≥ +2 hoặc mọi CI chứa 0): CÓ.
- **H2** (`docs` − `zero` ≥ 15 điểm, p < 0,05): Δ +19.5 [+15.4, +23.6], p = 5.2e-19 → **ĐẠT**.

<!-- TABLES END -->

## File

- Code: `scripts/eval/export_context_bodies.py`, `scripts/eval/kaggle_decision.py`, `scripts/eval/analyze_context.py` (mỗi file có `--selfcheck`/assert; `export_context_bodies.py` kiểm đếm 245×6 + 369×3 = 2.577 bản ghi, id không trùng, không id test).
- Runs: `reports/eval/runs/decision__vllm-sr_d3-flash__choice-<cond>__val-infect.jsonl` (zero, shots, docs, shots+docs, shotsemb, shotsemb+docs) và `...__choice-<cond>__pairs.jsonl` (zero, docs, own).

## Dọn dẹp

Đã xoá `D:\tmp\vm14k-claude2\ctx_bodies` (kết quả đã nằm trong `reports/`). Giữ: `data/interim/vm14k_train_emb.npz` (cache nhúng, dùng lại được), các thư mục kernel/output tạm khác ở `D:\tmp\vm14k-claude2\` cùng `phase2_log.md` (nhật ký), và trên tài khoản Kaggle một dataset riêng tư `vm14k-ctx-bodies` cùng hai kernel riêng tư `vm14k-d3flash-smoke`, `vm14k-d3flash-full` (chủ có thể xoá).

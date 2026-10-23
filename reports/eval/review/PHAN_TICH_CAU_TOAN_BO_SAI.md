# Phân tích các câu mà cả 7 model đều sai

Sinh bởi `scripts/eval/build_allwrong_file.py`; cùng nội dung với sheet `TomTat_PhanTich` của `VM14K_125_cau_7_model_deu_sai.xlsx`.

**125/1658 câu test (7.5%)** bị cả 7 model chọn sai. Mọi nhãn và nhóm gợi ý là tự động, chỉ để định hướng việc duyệt; kết luận cần ý kiến chuyên môn.

## Các model đã có lời giải thích (reasoning) cho các câu này

| Model | Chạy ở đâu | Có phần suy nghĩ (thinking)? | Số câu có giải thích | Trạng thái |
|---|---|---|---|---|
| Nemotron-3-Ultra | NVIDIA (API) | Có | 125/125 | Đủ |
| gpt-oss-20b | NVIDIA (API) | Có | 54/125 | Đang chạy |
| DeepSeek-v4.1-flash | NVIDIA (API) | Có | 0/125 | Chưa lấy được — NVIDIA đang quá tải, sẽ thử lại |
| Gemma-4-31B | NVIDIA (API) | Có | 0/125 | Chưa lấy được — NVIDIA đang quá tải, sẽ thử lại |
| Qwen3.5-9B | Máy local (Ollama, CPU) | Không — chỉ có phần giải thích | 5/125 | Đang chạy |
| MedGemma-4B | Máy local (Ollama, CPU) | Không — chỉ có phần giải thích | 0/125 | Đang chờ (các model local chạy lần lượt) |
| Llama-3.1-8B | Máy local (Ollama, CPU) | Không — chỉ có phần giải thích | 0/125 | Đang chờ (các model local chạy lần lượt) |
| Qwen3-8B | Máy local (Ollama, CPU) | Không — chỉ có phần giải thích | 0/125 | Đang chờ (các model local chạy lần lượt) |
| Gemma-4-12B | Máy local (Ollama, CPU) | Không — chỉ có phần giải thích | 0/125 | Đang chờ (các model local chạy lần lượt) |

*Cập nhật lúc 22:59 03/10/2026. Bảng tự cập nhật mỗi lần tạo lại file.*

## Mức hội tụ: số model (trong 7) cùng chọn một đáp án sai

| Số model | Số câu | Tỉ lệ |
|---|---|---|
| 7 | 32 | 25.6% |
| 6 | 26 | 20.8% |
| 5 | 23 | 18.4% |
| 4 | 31 | 24.8% |
| 3 | 13 | 10.4% |

*Hội tụ cao = nhiều model cùng một đáp án khác khoá → đáng nghi khoá sai; phân tán = câu khó/mơ hồ. Với 4 phương án (3 đáp án sai), mức thấp nhất có thể là 3/7.*

## Nemotron-3-Ultra khi được yêu cầu lập luận (thinking bật, giải thích tiếng Việt)

| Kết quả | Số câu | Tỉ lệ |
|---|---|---|
| Giữ đáp án sai của đa số | 66 | 52.8% |
| Chọn đúng khoá khi lập luận | 29 | 23.2% |
| Chọn một đáp án sai khác | 26 | 20.8% |
| Từ chối chọn | 4 | 3.2% |

*Lần trả lời nhanh của Nemotron không được tính vào 7 model (chạy chưa đủ tập test).*

## Nhóm gợi ý (tự động)

| Nhóm | Số câu | Tỉ lệ |
|---|---|---|
| Nghi đáp án chuẩn sai: ≥5/7 model cùng chọn một đáp án khác, Nemotron giữ đáp án đó khi lập luận | 47 | 37.6% |
| Nghi câu hỏi lỗi: Nemotron từ chối chọn (thiếu hình / thiếu dữ kiện / không có đáp án đúng) | 4 | 3.2% |
| ≥5/7 model cùng chọn một đáp án khác khoá (Nemotron không giữ khi lập luận) | 14 | 11.2% |
| 4/7 model cùng chọn một đáp án khác khoá | 23 | 18.4% |
| Model chọn phân tán (đáp án sai phổ biến nhất chỉ 3/7): câu khó hoặc mơ hồ | 8 | 6.4% |
| Nemotron chọn đúng khoá khi được yêu cầu lập luận: lỗi có thể do trả lời nhanh | 29 | 23.2% |

## Từng model khi được yêu cầu giải thích rồi chốt đáp án

| Model | Số câu có giải thích | Chọn đúng khoá | Giữ đáp án sai của đa số | Chọn một đáp án sai khác | Từ chối chọn |
|---|---|---|---|---|---|
| Nemotron-3-Ultra | 125 | 29 (23.2%) | 66 (52.8%) | 26 (20.8%) | 4 (3.2%) |
| gpt-oss-20b | 54 | 6 (11.1%) | 34 (63.0%) | 10 (18.5%) | 4 (7.4%) |
| Qwen3.5-9B | 5 | 1 (20.0%) | 4 (80.0%) | 0 (0.0%) | 0 (0.0%) |

*Nemotron và gpt-oss-20b bật thinking (qua NVIDIA). Các model local chạy trên CPU với thinking tắt nên chỉ có phần giải thích; model nào chưa chạy xong thì số câu ít hơn 125.*

## Nguồn Nemotron viện dẫn trong lời giải thích

| Loại nguồn | Số câu | …trong đó Nemotron giữ đáp án sai của đa số |
|---|---|---|
| Không nêu nguồn cụ thể | 49 (39.2%) | 26 |
| Nhắc nguồn / bối cảnh VN | 43 (34.4%) | 27 |
| Cả VN và quốc tế | 31 (24.8%) | 12 |
| Chỉ nguồn quốc tế | 2 (1.6%) | 1 |

*Dò từ khoá đơn giản (Bộ Y tế, phác đồ, Việt Nam… / WHO, AHA, Harrison…). Câu model giữ đáp án sai trong khi viện dẫn nguồn quốc tế là ứng viên cho nhóm 'đúng theo thực hành VN', cần chuyên gia xác nhận.*

## Các giả thuyết đã kiểm tra (không cần chuyên gia)

| Giả thuyết | Kết quả | Kết luận |
|---|---|---|
| Đáp án chuẩn bị lệch một vị trí (ví dụ đúng là B nhưng khoá ghi A) | Đáp án đa số nằm cạnh khoá: 53/113 = 46.9%; mọi câu trả lời sai khác: 53.1%; nếu ngẫu nhiên: 48.5% | Không có dấu hiệu lệch vị trí |
| Model bị hút về phương án dài nhất | Đáp án đa số là phương án dài nhất: 33/85 = 39%; khoá là phương án dài nhất: 21/85 = 25% | Tín hiệu yếu, chưa đủ để kết luận |
| Câu y hệt (cùng chữ, cùng phương án) xuất hiện ở chỗ khác trong bản gốc với khoá khác | 0/125 câu | Không có: các bản trùng có khoá mâu thuẫn đã được xử lý khi làm sạch. Các câu 'gần giống' tìm thấy đều khác số liệu hoặc khác thuốc, nên là câu khác nhau |

## Đặc điểm câu: nhóm 7 model đều sai so với toàn bộ tập test

| Đặc điểm | Trong 125 câu sai | Trong 1658 câu test | Hệ số (lift) | p (Fisher) |
|---|---|---|---|---|
| Hỏi đếm số lượng (bao nhiêu / mấy) | 10 (8.0%) | 64 (3.9%) | 2.07 | 0.025 |
| Có hai phương án gần giống nhau | 25 (20.0%) | 207 (12.5%) | 1.60 | 0.011 |
| Phương án là số liệu / ngưỡng | 26 (20.8%) | 244 (14.7%) | 1.41 | 0.049 |
| Hỏi phủ định / loại trừ | 20 (16.0%) | 210 (12.7%) | 1.26 | 0.262 |
| Nhắc tới hình / bảng / ảnh | 13 (10.4%) | 137 (8.3%) | 1.26 | 0.396 |
| Phương án tham chiếu phương án khác (Cả A và B…) | 9 (7.2%) | 104 (6.3%) | 1.15 | 0.700 |
| Liên quan quy định / chương trình y tế VN | 2 (1.6%) | 24 (1.4%) | 1.11 | 0.701 |
| Câu hỏi rất ngắn (< 30 ký tự) | 8 (6.4%) | 136 (8.2%) | 0.78 | 0.610 |
| Câu đúng / sai (2 phương án) | 4 (3.2%) | 173 (10.4%) | 0.31 | 0.003 |

*Lift > 1: đặc điểm xuất hiện nhiều hơn bình thường trong nhóm toàn bộ sai. Phân tích khám phá: nhiều phép so sánh, quy tắc gán nhãn đơn giản, chưa hiệu chỉnh p — chỉ dùng để gợi hướng.*

## Theo nhãn độ khó

| Nhóm | Trong 125 câu sai | Trong 1658 câu test | Tỉ lệ sai toàn bộ |
|---|---|---|---|
| Challenging | 14 (11.2%) | 166 (10.0%) | 8.4% |
| Easy | 40 (32.0%) | 544 (32.8%) | 7.4% |
| Hard | 1 (0.8%) | 13 (0.8%) | 7.7% |
| Medium | 70 (56.0%) | 935 (56.4%) | 7.5% |

## Theo số phương án

| Nhóm | Trong 125 câu sai | Trong 1658 câu test | Tỉ lệ sai toàn bộ |
|---|---|---|---|
| 2 | 4 (3.2%) | 173 (10.4%) | 2.3% |
| 3 | 0 (0.0%) | 6 (0.4%) | 0.0% |
| 4 | 121 (96.8%) | 1479 (89.2%) | 8.2% |

## Theo chuyên khoa (chuyên khoa có ≥15 câu test)

| Chuyên khoa | Số câu cả 7 model sai | Số câu test | Tỉ lệ |
|---|---|---|---|
| Dentistry | 5 | 15 | 33.3% |
| Physiology | 4 | 22 | 18.2% |
| General Medicine | 11 | 69 | 15.9% |
| Palliative Medicine | 2 | 15 | 13.3% |
| Hematology | 7 | 53 | 13.2% |
| Physical Medicine and Rehabilitation | 3 | 23 | 13.0% |
| Psychiatry | 3 | 23 | 13.0% |
| Toxicology | 6 | 49 | 12.2% |
| Emergency Medicine | 3 | 30 | 10.0% |
| Dermatology | 4 | 40 | 10.0% |
| Geriatrics | 2 | 20 | 10.0% |
| Pediatrics | 11 | 113 | 9.7% |
| Pulmonology | 20 | 228 | 8.8% |
| Public Health | 4 | 46 | 8.7% |
| Nephrology | 5 | 64 | 7.8% |
| Pathology | 9 | 116 | 7.8% |
| Cardiology | 3 | 39 | 7.7% |
| Orthopedics | 2 | 28 | 7.1% |
| Infectious Diseases | 16 | 232 | 6.9% |
| Oncology | 8 | 118 | 6.8% |
| Endocrinology | 13 | 198 | 6.6% |
| Internal Medicine | 4 | 61 | 6.6% |
| Neurology | 4 | 63 | 6.3% |
| Preventive Healthcare | 3 | 49 | 6.1% |
| Allergy and Immunology | 2 | 33 | 6.1% |
| Gastroenterology | 20 | 340 | 5.9% |
| Radiology | 5 | 85 | 5.9% |
| Obstetrics and Gynecology | 18 | 319 | 5.6% |
| Genetics | 1 | 19 | 5.3% |
| Surgery | 4 | 78 | 5.1% |
| Pharmacology | 4 | 80 | 5.0% |
| Rheumatology | 1 | 20 | 5.0% |
| Ophthalmology | 1 | 22 | 4.5% |
| Urology | 3 | 76 | 3.9% |
| Eastern Medicine | 1 | 32 | 3.1% |
| Anesthesiology | 0 | 15 | 0.0% |
| Parasitology | 0 | 17 | 0.0% |
| Otolaryngology | 0 | 36 | 0.0% |
| Cell Biology | 0 | 16 | 0.0% |
| Anatomy | 0 | 22 | 0.0% |

*Tỉ lệ chung: 7.5%. Một câu có thể thuộc nhiều chuyên khoa. Cỡ mẫu từng chuyên khoa nhỏ.*

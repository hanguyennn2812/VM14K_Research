# Báo cáo nhanh — mô hình phân loại chuyên khoa VM14K

## Mục tiêu

Tự động gán một hoặc nhiều chuyên khoa cho câu hỏi trắc nghiệm y khoa. Đây là
mô hình định tuyến câu hỏi phục vụ nghiên cứu, không dùng để chẩn đoán hay ra
quyết định lâm sàng.

## Chuẩn bị dữ liệu

- Nguồn đã làm sạch cấu trúc: 10.628 câu hỏi.
- Giữ lại 8.397 câu mà mọi nhãn gốc đều map rõ ràng về một trong 34 chuyên
  khoa chuẩn của VM14K.
- Loại 2.180 câu mang nhãn mơ hồ/ngoài taxonomy (ví dụ Pharmacology,
  Toxicology, Dentistry, Other(No Category)) và 51 câu có cờ mâu thuẫn đáp án.
- Câu đa-chuyên-khoa được giữ nguyên dưới dạng đa-nhãn, không bị ép vào một
  nhãn duy nhất.

## Thiết lập thử nghiệm

- Chia dữ liệu cố định theo nhóm stem câu hỏi: train 5.798, validation 1.277,
  test 1.322. Một stem không xuất hiện ở hai tập khác nhau.
- Đầu vào: câu hỏi và các phương án lựa chọn; không đưa đáp án đúng hoặc vị trí
  đáp án vào mô hình.
- Baseline: TF-IDF word/character n-gram + One-vs-Rest Logistic Regression.
- Ngưỡng đa-nhãn được chọn trên validation, sau đó đánh giá một lần trên test.

## Kết quả trên test hold-out

| Chỉ số | Giá trị |
|---|---:|
| Micro-F1 | 75,8% |
| Macro-F1 | 67,9% |
| Exact-match accuracy | 43,3% |
| Hamming loss | 2,71% |

Micro-F1 là chỉ số chính cho bài toán đa-nhãn. Exact-match khắt khe hơn: một
câu chỉ được tính đúng khi toàn bộ tập chuyên khoa dự đoán khớp hoàn toàn nhãn
chuẩn.

## Tài liệu kèm theo

- `specialty_demo_samples.md`: 8 ví dụ hold-out đa dạng, dự đoán đúng toàn bộ
  nhãn.
- `specialty_model_report.json`: đầy đủ chỉ số theo từng chuyên khoa.
- `specialty_data_report.json`: quy tắc lọc, số lượng và phân bố nhãn.

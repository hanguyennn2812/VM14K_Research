# Pilot MoH vòng 2 — 03/11/2026

Đã tạo đủ **60 câu để duyệt**, từ **17 văn bản**, tối đa **6 câu/văn bản**. Chưa sinh toàn bộ data,
chưa train, commit/push hoặc triển khai thay đổi. Hai job d3 trên Modal là các lượt đánh giá thử nghiệm.

File duyệt: `outputs/moh_pilot_v2_20261103/MOH_MCQ_pilot_v2_review.xlsx`.
Chấm cột F của tab **Duyệt 60**, dùng cột G–H để ghi lỗi. Tab **Đoạn gốc** giữ đủ đoạn nguồn và số trang.
Tab **BatDong_vong1** giữ nguyên năm câu cũ mà d3 đọc nguồn vẫn chọn khác, để chấm riêng.
Chúng không nằm trong mẫu số 60 của vòng mới. **Tổng kết** chỉ báo đạt khi chấm đủ 60 và có ít nhất
54 câu Đúng; vẫn cần người dùng duyệt trước khi chuyển sang sinh data.

## Nguyên nhân và thay đổi

File Hà gửi có 47 Đúng, 1 Sai, 6 Không rõ và 6 Không lâm sàng (78,3% Đúng).
Chín câu có nhãn thiếu tên bệnh. Generator cũ cắt cửa sổ 200 từ xuyên mục/trang, làm mất tiêu đề
và cấu trúc bảng. Bộ lọc chỉ đếm mã ICD và tỷ lệ chữ số, còn prompt không đủ ngăn câu hành chính.

- Tách nguồn sinh MCQ khỏi bộ chunk dùng cho RAG, giữ tiêu đề hướng dẫn, chương bệnh, mục, trang PDF,
  đường dẫn và phần thân. Sửa việc kéo tiêu đề xét nghiệm cũ sang mục điều trị.
- Loại văn bản giám sát, hướng dẫn thu thập số liệu nhiễm mới HIV, văn bản hành chính và mục trách nhiệm/
  biểu mẫu. Loại nguồn ít chữ có dấu, OCR hỏng, ký tự khác hệ chữ và trang có bảng. Giữ nguyên PDF gốc.
- Bắt buộc tên bệnh có trong nguồn và câu hỏi; giải nghĩa SXHD/ĐTĐ/SLE nếu dùng trong câu hỏi.
  Trích dẫn phải khớp phần thân sau chuẩn hóa Unicode và khoảng trắng.
- Loại câu hỏi câu chữ tài liệu, tự lộ đáp án, từ khẳng định mạnh hơn nguồn và bản gần trùng val/test
  (TF-IDF >= 0,5). Xáo phương án có seed, lấy mẫu luân phiên văn bản và áp trần 6 câu/PDF.
- Thêm lượt kiểm cả bốn lựa chọn bằng cùng model viết câu, trong request riêng. Đây là tự kiểm bằng
  model, không phải xác nhận y khoa độc lập. Lượt rà cuối bắt thêm bốn câu từ nguồn hành chính/thu thập
  số liệu; đã loại bằng quy tắc chung và sinh bù, rồi chạy lại cả hai lượt d3 trên bộ cuối.
- Có journal giữ ứng viên bị loại, checkpoint và `--resume`; khi resume, câu cũ cũng phải qua bộ lọc
  hiện tại. Mặc định chỉ sinh pilot 60 câu.

## Kết quả kiểm tra

- `python -X utf8 -m pytest tests -q`: **46 passed**.
- Bộ cuối: 60 ID khác nhau, 17 văn bản, trần 6/PDF, 60/60 trích dẫn khớp nguồn, không câu nào có
  độ tương đồng held-out >= 0,5. Vị trí đáp án A/B/C/D: 17/16/14/13.
- d3 có nguồn: **60/60** đồng ý đáp án; không nguồn: **49/60 (81,7%)**. Mỗi lượt 60 bản ghi, 0 lỗi.
  Không dùng hai kết quả này để thay tỷ lệ duyệt của người.
- Workbook: thử 53/60, 54/60, chấm 59 câu và chưa chấm; khôi phục toàn bộ đánh giá về trống.
  Đã kiểm hình render của cả bốn tab và đọc lại XLSX để đối chiếu câu/nguồn/ID, năm câu cũ, danh sách
  chọn, bộ lọc, cố định hàng tiêu đề, 60 liên kết nội bộ và trạng thái lưu sẵn “Chưa xong”.
- File Hà giữ nguyên SHA256:
  `849bbe094c3a73a97b09c820738d49177513c4085f23a21a7ceed282cf857c56`.
- JSONL cuối: `data/derived/moh_mcq/pilot_v2_20261103.jsonl`, SHA256
  `54f286be375fd0bb3f09015fa614fd3682c1dfac7901a9e09762a60cecb00af3`.
  Audit và journal ở hai file cùng tên với hậu tố `.source_audit.json` và `.attempts.jsonl`.

## Giới hạn và ảnh hưởng

Chưa sửa OCR hay tái dựng bảng: bỏ trang có bảng làm giảm độ phủ. Tỷ lệ chữ có dấu và kiểm tra chồng
từ là heuristic, không bảo đảm phát hiện mọi lỗi. Chưa đo riêng tác động của viết tắt lên d3.
Chưa kiểm tương tác bằng ứng dụng Excel; đã kiểm công thức bằng engine artifact-tool và cấu trúc file
bằng trình đọc XLSX độc lập. Hàm HYPERLINK của engine không tính được nên dùng liên kết nội bộ OOXML
thay thế, giữ nhãn hiển thị bình thường.

Runtime artifact-tool trên Windows xuất file/render thành công nhưng tiến trình bị lỗi native
`-1073740791` sau khi Node báo exit 0. File đã lưu được kiểm lại độc lập và không có lỗi ZIP/công thức
hay mất dữ liệu. Đây là giới hạn của bước xuất trên máy hiện tại; không ghi nhận builder exit 0.

Thay đổi chỉ ở pipeline nghiên cứu và artifact pilot. Bộ RAG, PDF gốc, dữ liệu chuẩn và kết quả vòng 1
được giữ nguyên. Không có thay đổi production. Duyệt >=54/60 rồi người dùng xác nhận mới đi tiếp.

## Lệnh chạy lại

```powershell
python -X utf8 scripts/training/gen_moh_mcq.py --seed 20261103 --chunks 170 --target 60 --max-per-doc 6 --output data/derived/moh_mcq/pilot_v2_new.jsonl
python -X utf8 -m modal run scripts/eval/modal_decision.py --models vllm-sr/d3 --items data/derived/moh_mcq/pilot_v2_20261103.jsonl --split moh-pilot-v2-20261103 --context own
python -X utf8 -m modal run scripts/eval/modal_decision.py --models vllm-sr/d3 --items data/derived/moh_mcq/pilot_v2_20261103.jsonl --split moh-pilot-v2-20261103
python -X utf8 scripts/eval/prepare_moh_review.py --items data/derived/moh_mcq/pilot_v2_20261103.jsonl --ha d:/Dowloads/MOH_MCQ_pilot_review_Ha.xlsx --output outputs/moh_pilot_v2_20261103/review_payload.json
node scripts/eval/build_moh_review.mjs outputs/moh_pilot_v2_20261103/review_payload.json outputs/moh_pilot_v2_20261103/MOH_MCQ_pilot_v2_review.xlsx
```

Builder dùng `@oai/artifact-tool` từ runtime cung cấp, được nối vào `OUTPUT_DIR/node_modules`.
Lệnh cuối ghi đè artifact duyệt; không chạy lại trên file đã có đánh giá của người dùng.

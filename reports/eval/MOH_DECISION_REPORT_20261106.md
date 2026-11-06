# Báo cáo decision model và văn bản Bộ Y tế

06/11/2026 · TrucNguyen2211

## Kết luận

Chưa có bằng chứng văn bản Bộ Y tế giúp model làm đề VM14K tốt hơn: trên VM14K test, VM14K + MoH ×4 đạt 52,4%, baseline đạt 52,8% (p=0,72).

Model vẫn nhớ được nội dung đã train: câu viết lại tăng 22,3 điểm. Vì vậy kết quả này không có nghĩa là model không học được gì. Phần học được chưa chuyển thành điểm trên đề thi, một phần vì chỉ 65/1.658 câu test nêu đúng bệnh đã train.

Báo cáo được chốt dựa trên hai đợt duyệt pilot (47/60 và 57/60 câu Đúng). Bộ 533 câu và bộ test văn bản không được người chấm trực tiếp.

## Trạng thái kế hoạch

Cả sáu bước đã chạy và được chốt, nhưng có hai phần làm khác kế hoạch: bộ test văn bản dừng ở 29/54 chunk và không duyệt toàn bộ, còn mẫu từ bộ 533 câu không được chấm.

| Bước | Trạng thái | Còn thiếu |
| --- | --- | --- |
| 1. Commit pilot, sửa generator | Xong | Không |
| 2. Chia văn bản theo bệnh | Xong | Không |
| 3. Sinh toàn bộ, nhãn mềm d3 | Xong | Chốt theo hai đợt duyệt pilot; không chấm mẫu 60 câu mới |
| 4. Bộ test từ văn bản test | Dừng ở 29/54 chunk, 39 câu | 25 chunk chưa sinh; không được người duyệt |
| 5. Train các nhánh, chọn trên val | Xong | Nhánh không train chỉ có số trên 797 câu dev |
| 6. Đánh giá một lần | Xong | Bộ test văn bản chỉ có 39 câu |

VM14K test đã chấm trước khi người duyệt dữ liệu, theo yêu cầu chạy hết kế hoạch. Nếu sau này sửa dữ liệu rồi train lại, kết quả test lần sau không còn sạch.

## Dữ liệu

Bộ train cuối có 533 câu từ 10 văn bản: 438 train, 95 val, trong đó 107 câu d3 không nguồn trả lời sai (ứng viên kiến thức mới).

| Bước | Số câu |
| --- | --- |
| Sinh từ 318 chunk, qua bộ lọc ban đầu | 333 |
| Sau khi sửa rule, cứu từ journal | 538 |
| Qua d3 có nguồn | 533 |

Rule cũ loại oan nhiều câu vì bắt nhãn bệnh phải khớp từng chữ với câu hỏi. Có 208 câu được cứu, còn 205 câu sau gate d3. Các câu này không qua verifier, và d3 có nguồn đồng ý tới 99,1% nên khó bắt câu sai.

Dữ liệu lệch bệnh: lao, COVID-19 và sốt xuất huyết chiếm 407/538 câu (76%). Hai đợt duyệt đã làm là trên pilot: vòng 1 đạt 47/60, pilot v2 đạt 57/60. Chỉ 1 câu của pilot v2 còn trong bộ 533. Mẫu 60 câu từ bộ 533 chưa chấm; tạo lại được bằng `scripts/training/review_and_split_moh.py`.

## Kết quả trên VM14K val

Cấu hình được chọn là VM14K + MoH ×4 (55,3%), nhưng mức hơn baseline 54,4% chưa chắc là thật. Chỉ train MoH kém rõ rệt. Model học sinh là Qwen3.5-2B + jev-torch LoRA, 1 epoch, loss KL.

| Nhánh train | Số dòng train | Tất cả, n=1.595 (%) | Truyền nhiễm, n=245 (%) | Nêu bệnh đã train, n=65 (%) | MoH val, n=95 (%) |
| --- | --- | --- | --- | --- | --- |
| Chỉ VM14K (baseline) | 7.313 | 54,4 | 58,8 | 46,2 | 60,0 |
| VM14K + MoH ×1 | 7.751 | 54,2 | 58,8 | 55,4 | 58,9 |
| VM14K + MoH ×4 (được chọn) | 9.065 | 55,3 | 60,4 | 49,2 | 63,2 |
| Chỉ MoH ×1 | 438 | 48,0 | 47,8 | 36,9 | 60,0 |
| Chỉ MoH ×4 | 1.752 | 48,5 | 49,0 | 44,6 | 62,1 |

So sánh chính (mức tăng ở Truyền nhiễm trừ mức tăng ở chuyên khoa khác) là +0,1 điểm với ×1 [−4,9; +5,1] và +0,8 điểm với ×4 [−3,9; +5,3], đều chứa 0.

Mức +9,2 ở nhóm bệnh đã train với ×1 không lặp lại khi tăng liều (còn +3,1 với ×4), nên nhiều khả năng là nhiễu. Nhánh không train chỉ có số liệu 32,1% trên 797 câu dev (step 0); không chấm riêng trên toàn bộ val.

## Kiểm tra độ nhớ

Model có nhớ nội dung đã train, kể cả khi câu được viết lại: với MoH ×4, câu viết lại tăng 22,3 điểm so với nhánh chỉ train VM14K (khoảng tin cậy 95%: 13,6 đến 32,0).

| Độ chính xác (%) | Số câu | Chỉ VM14K | MoH ×1 | MoH ×4 |
| --- | --- | --- | --- | --- |
| Câu train gốc, toàn bộ | 438 | 53,9 | 63,5 | 79,5 |
| Câu train gốc, cùng mẫu với câu viết lại | 103 | 46,6 | 58,3 | 75,7 |
| Câu viết lại | 103 | 47,6 | 56,3 | 69,9 |

Kết quả này chưa chứng minh model học được kiến thức. Câu viết lại vẫn giữ cùng các phương án, chỉ đổi câu chữ, nên model có thể chỉ quen mặt đáp án đúng. Lượt viết lại dừng ở 105/150 câu do session bị ngắt; mẫu vẫn ngẫu nhiên vì là phần đầu của danh sách đã xáo. Hai câu bị đổi thứ tự phương án làm sai key đã bị loại, còn 103 câu.

## Đánh giá trên test

VM14K test không cho thấy cải thiện: toàn bộ giảm 0,4 điểm, và so sánh chính là +3,0 điểm [−2,5; +8,6], chứa 0. Cấu hình đã chốt trên val trước khi chấm.

| VM14K test | Số câu | Baseline (%) | MoH ×4 (%) | Tăng (điểm) | Thắng/thua |
| --- | --- | --- | --- | --- | --- |
| Tất cả | 1.658 | 52,8 | 52,4 | −0,4 | 132/139 |
| Truyền nhiễm | 232 | 54,7 | 56,9 | +2,2 | 21/16 |
| Chuyên khoa khác | 1.426 | 52,5 | 51,6 | −0,8 | 111/123 |
| Nêu bệnh đã train | 65 | 55,4 | 50,8 | −4,6 | 5/8 |
| Không nêu bệnh đã train | 1.593 | 52,7 | 52,4 | −0,3 | 127/131 |

So sánh phụ (bệnh đã train trừ phần còn lại) là −4,4 điểm [−15,0; +6,3]. Hiệu chỉnh xác suất tương đương: ECE baseline 0,027, MoH ×4 0,023.

Bộ test văn bản không cho thấy khác biệt: cả hai đều đạt 76,9% trên 39 câu (thắng/thua 1/1), khoảng tin cậy [−7,7; +7,7]. Bộ này dừng ở 29/54 chunk, qua d3 có nguồn 39/39, không được người duyệt và quá nhỏ để kết luận. Các bệnh trong bộ này (lậu, viêm gan C, sởi, mpox) không được train, nên nó chỉ đo khả năng khái quát, không đo kiến thức vừa học.

## Kiểm tra độc lập và hạn chế

Codex kiểm tra ở chế độ chỉ đọc và tìm ra hai lỗi thật, đã sửa; cả hai không làm thay đổi kết luận. Đây là so khớp với đoạn nguồn, không phải xác nhận y khoa độc lập.

| Phát hiện của Codex | Xử lý |
| --- | --- |
| So khớp evidence bỏ cả dấu > và < | Đã sửa. 2/533 câu không còn khớp, không câu nào đảo ngưỡng; không train lại |
| Câu viết lại đổi thứ tự phương án, sai key (1/30 câu mẫu) | Đã thêm kiểm tra; tìm thêm 1 câu, loại cả 2, còn 103 câu |
| Câu được cứu: 28/30 key khớp nguồn, 1 sai rõ, 1 chưa xác định được | Chưa sửa; cần người duyệt |
| Bộ lọc trùng dùng câu hỏi VM14K val và test, không dùng đáp án | Giữ nguyên, đúng kế hoạch bước 3 |
| Xác suất MoH val lưu theo thứ tự đã xáo | Chưa sửa; không ảnh hưởng độ chính xác |

Hạn chế còn lại:

- Việc chọn checkpoint và hiệu chỉnh dùng VM14K val, nên số trên val hơi lạc quan.
- Chỉ khoảng 65 câu mỗi bộ nêu bệnh đã train, không đủ để phát hiện hiệu ứng nhỏ.
- Mỗi nhánh chỉ chạy một seed. Model là bản 2B nhỏ, 1 epoch.

## Bước tiếp theo

Nếu làm tiếp, việc đáng làm nhất là bước 3 dưới đây; hai bước đầu chỉ cần khi muốn công bố kết quả.

1. Duyệt 60 câu mẫu từ bộ 533, ngưỡng 90%.
2. Sinh nốt 25 chunk của bộ test văn bản (có thể resume), rồi duyệt toàn bộ và đóng băng.
3. Phân biệt kiến thức với quen mặt đáp án: hỏi lại cùng sự kiện với các phương án sai mới.
4. Chỉ khi bước 3 cho tín hiệu thật mới thử model lớn hơn (4B, 9B) hoặc thêm văn bản.

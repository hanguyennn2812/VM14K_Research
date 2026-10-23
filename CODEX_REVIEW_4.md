Quy ước **hợp lý cho κ và E2**: cờ trống chỉ thành “Không” khi đã điền tình trạng; nếu chưa điền thì là thiếu. κ dùng quy tắc này, giữ cảnh báo mà không loại dòng; validation kiểm tra dropdown ở cả hai vòng. E2 dùng tình trạng cuối và trạng thái khóa, đúng protocol. Tầng ngẫu nhiên đã đứng đầu.

Còn hai điểm cần sửa:

- `scripts/eval/build_review_sample.py:131`: hướng dẫn workbook nói vô điều kiện “cờ trống = KHÔNG”, thiếu điều kiện đã chọn tình trạng như HUONG_DAN §3.
- `scripts/eval/analyze_review.py:263` và `:282–290`: bất đồng **chỉ về tình trạng** không vào danh sách phân xử; E2 có thể bị giữ là thiếu, và quyết định phân xử nhập riêng cho câu đó cũng bị bỏ qua.

Kết quả chạy, không sửa worktree:

- Python 3.13, pytest tắt plugin ngoài/cache và dùng capture trong bộ nhớ: **22 passed, 15 errors**. Cả 15 lỗi do sandbox không cho tạo thư mục tạm; chưa xác nhận được 37/37.
- Files thật, chặn hai hàm ghi đầu ra: **178 câu, 0 ô duyệt được điền, 0 vấn đề, 0 bất đồng**; endpoint đều thiếu, κ không xác định.
- CLI `--simulate` bị chặn khi tạo thư mục tạm. Chạy cùng `simulate()`/`analyze()` với I/O trong bộ nhớ cho **251 vấn đề, 12 bất đồng**; đây không thay thế kiểm thử ghi workbook thật.

DRAFT v2 sửa trung thành phần lớn các lỗi diễn giải, mẫu số và ngoại lệ Gemini/Δ Llama 4. Những điểm còn thiếu:

- `docs/paper/DRAFT.md:1,38`: tiêu đề vẫn khẳng định “First”; Introduction vẫn giữ “much of the evidence” chưa có nguồn.
- `:40,223`: ledger chưa bổ sung nguồn riêng cho **34 specialties / 4 levels / 17 models**.
- `:58,69,73`: citation related work vẫn còn placeholder; Easy2Hard thiếu tác giả/năm.
- `:140–146`: count guards và hai vấn đề pipeline chưa có ledger/code location như đã yêu cầu.
- `:149,240`: lịch sử split có số **1.662→1.658**, nhưng chưa liệt kê bốn ID và fate tương ứng.
- `:154–166`: ledger protocol/configuration, bảng CI đủ bảy model, CI raw−clean và random baseline cho 70 câu vẫn chưa hoàn tất.
- `:249`: đã sửa cơ cấu đủ 17 dòng, nhưng bỏ sót chú thích tên Llama ở Table 3 thiếu “.1”.
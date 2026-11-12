# Bằng chứng chuẩn và distillation có nguồn — 11/11/2026

Owner yêu cầu Codex và Claude2 thử tiếp các hướng bổ sung kiến thức và train bằng lời giải có nguồn. Model trả lời ≤9B; chỉ NVIDIA Build/Kaggle/local miễn phí, không Modal, không release hay git commit/push.

## Protocol trước GPU

- Mẫu phát triển cố định, seed 20261115: **32 câu uniform** từ dev-tune cũ và **16 câu đang sai** ngoài nhóm uniform. Báo riêng hai tầng, không gộp 48 câu thành điểm đại diện quần thể. Đây là pilot chẩn đoán, không phải phép xác nhận 83–85%.
- Bank ví dụ mới loại toàn bộ pseudo-hold cũ, cả 48 câu đánh giá và láng giềng cosine ≥0,9: 593 id bị loại, còn 6.720 câu. Kiểm mọi shot không thuộc tập bị loại. Lọc cả chunk kho mở mang cờ liên quan các câu bị loại. Sự tách biệt từ lượt này không xoá lịch sử đã dùng pseudo-hold trước đây.
- Claude2 chọn ≤2 đoạn cho mỗi câu từ file chỉ có question/options/nguồn, không có gold/prediction. Đã khoá 48 annotations. JSON đếm được 9 sufficient, 25 partial, 14 absent; không dùng số đếm nhẩm của agent. Không coi đây là bác sĩ duyệt.
- Codex xác minh nguồn mới do Claude2 tìm bằng trang gốc, không ép nguồn mới khớp khoá cũ. Câu thiếu dữ kiện/phác đồ khác thời kỳ giữ cờ ambiguous/conflict. Không sửa gold benchmark.
- D3-flash 9B fp16: so `safe_shots`, `safe_retrieved`, `oracle_curated`, `oracle_augmented`, cùng bank/câu/thứ tự. Oracle không có đoạn thì fallback truy hồi; công bố coverage và phân tầng. Thước đo: số đúng/n, Wilson 95%, Δ bootstrap cặp, thắng/thua, McNemar; luôn-A và random. Oracle là điều kiện được trợ giúp chọn nguồn, không phải cấu hình triển khai.
- Train pilot: Qwen3.5-9B gốc, hai LoRA cùng câu/nguồn/thứ tự/siêu tham số: đối chứng chỉ đáp án và bản học lời giải dẫn nguồn rồi đáp án. Dữ liệu từ MCQ MoH đã duyệt nguồn/được d3 đối chiếu trước đó, loại gần trùng với 48 câu (TF-IDF <0,6); không dùng các đoạn oracle để tạo câu train. Teacher mới phải có quote tồn tại trong nguồn; bỏ mẫu thiếu hỗ trợ/khóa nghi vấn. Không train trên OpenStax mới hay nguồn web có quyền chưa rõ.
- Dự kiến tối đa64 câu train có lời giải, tối thiểu16 cho smoke/pilot; một epoch, LoRA r16, lr1e-4, batch1/accum8, max sequence1024, seed42. Đây là thử cơ chế trên bộ nhỏ, kết quả âm không loại được hướng ở quy mô lớn hơn. Phải chứng minh optimizer thực sự bước và trọng số adapter đổi.
- Đánh giá student sinh câu trả lời trên cùng48 câu với prompt RAG và ngân sách256 token không-thinking/greedy, trước và sau từng LoRA. Lấy dòng đáp án cuối; câu rỗng/cắt không có kết luận tính sai. Báo answer-rate và cờ truncation để tách tuân thủ định dạng khỏi kiến thức. Không so trực tiếp tuyệt đối với D3 khác readout/prompt.
- Không lưới siêu tham số, không chọn theo test/hold. Tối đa4 giờ GPU mới cho pilot; nếu tốc độ/OOM vượt dự toán thì ghi blocker, không âm thầm đổi backbone hoặc dùng tiền.

## Phân công và trạng thái

Codex: bank, kiểm nguồn/teacher, code, self-check, GPU, phân tích và dọn. Claude2: chọn nguồn che gold, tìm nguồn mới, rồi tạo lời giải train khi API không ổn định.

NVIDIA gặp lỗi đầu ra chữ rác/JSON hỏng ở Nemotron, Gemma trả404, DeepSeek timeout trong probe. Mẫu lỗi không vào train. Đã thử sampling theo model card chính thức; chưa coi teacher API là đáng tin chỉ vì HTTP200. Claude2 đã trả lời giải từ64 câu MoH cố định, sau kiểm lọc còn52 câu có nguồn.

## Kết quả

Đã xong pha D3; bảng ở cuối. Pha student 9B đã tải model trên Kaggle nhưng dừng ở assertion `training EOS is not a generation stop token` trong đánh giá baseline. File baseline rỗng, chưa chạy optimizer và chưa có adapter đã học. Cần sửa calibration token kết thúc theo generation config rồi chạy lại để có kết quả trước/sau train. Trạng thái được đối chiếu log khi tổng hợp ngày12/11.

### Dữ liệu và review chéo trước train

Claude2 trả đủ64 annotations train, nhận62, loại2. Codex kiểm62 quote đều nguyên văn4–25 từ, loại thêm câu yếu/hành chính và bỏ những câu giải thích chỉ suy từ việc nguồn không nhắc đến: còn **52 câu** (A15/B13/C13/D11). Cosine tối đa với48 câu đánh giá là0,194 (<0,6). Dữ liệu này tập trung6 văn bản MoH, không phải giáo trình bao phủ toàn bộ chuyên khoa; chưa được bác sĩ duyệt.

Claude2 review code phát hiện lối tắt: quote bị chèn/lặp ở đầu nguồn train. Đã sửa dùng nguyên văn passage, cắt cửa sổ token quanh quote với vị trí biến thiên; vị trí nguồn đúng cũng được xáo giữa hai đoạn. Hai adapter dùng cùng cửa sổ và câu, chỉ khác target. Đã kiểm tokenizer Qwen3.5-9B thật cho52 câu ×2 thứ tự và48 câu đánh giá; không mất quote, target dài nhất152 token (ngân sách256). Cộng guard EOS, số optimizer step thực và trọng số LoRA phải đổi để tránh lặp lỗi smoke CPT cũ.

### Các case nguồn cần chuyên gia xem, không sửa gold

- `ce3e25dd6a08404ebcf3c91b034acc1f`: khóa B, mọi điều kiện D3 chọn D. [CDC DPDx](https://www.cdc.gov/dpdx/malaria/index.html) mô tả palps bằng vòi, vảy cánh đen trắng, trứng rời có phao và bụng chếch lên khi nghỉ; phù hợp D, trái chi tiết hút máu ban ngày/nghỉ song song trong B. Đánh dấu **nghi khóa sai có bằng chứng**, chưa phải bác sĩ phân xử.
- `a18d01a1b6d141e7811aae07f9b4718f`: nguồn [CDC CAUTI III.E](https://www.cdc.gov/infection-control/hcp/cauti/summary-of-recommendations.html) không khuyến cáo lịch thay túi cố định; đề chỉ cho2/5/7/10 ngày. Model đổi B→C và trùng khóa C khi thêm nguồn, nhưng nguồn không hỗ trợ C. Điểm tăng này không chứng minh hiểu bằng chứng tốt hơn.
- `de054813576146d282e277806a3f45fd`: nguồn [Adelaide](https://mycology.adelaide.edu.au/fungal-descriptions-and-antifungal-susceptibility/dermatophytes/epidermophyton) phân biệt màu mặt khuẩn lạc và sắc tố mặt trái; đề không nói rõ mặt nào. Giữ cờ partial/ambiguous, không tự chọn lại gold.

Chi tiết prediction đã đóng băng trong `GROUNDED_SOURCE_CASES_2026-11-11.json`. Không loại các câu này khỏi điểm chính sau khi thấy kết quả.

## Dọn dẹp

Đang giữ `D:/tmp/vm14k-grounded/` để chạy. Kết quả lâu dài vào `docs/research/` và prediction vào `reports/eval/runs/`. Cuối lượt xoá đúng tài nguyên mới do lượt này tạo; không xoá artifact cũ của Claude2.

## Kết quả D3 9B: nguồn chọn che gold

### uniform, n=32

Random 29.9%, luôn A 37.5%.

| condition | n | right | % | Wilson 95% CI | Δ vs safe_retrieved [bootstrap 95% CI] | wins/losses | McNemar p |
|---|---:|---:|---:|---:|---:|---:|---:|
| safe_shots | 32 | 25 | 78.1 | [61.2, 89.0] | +6.2 [+0.0, +15.6] | 2/0 | 0.5 |
| safe_retrieved | 32 | 23 | 71.9 | [54.6, 84.4] | +0.0 [+0.0, +0.0] | 0/0 | 1 |
| oracle_curated | 32 | 23 | 71.9 | [54.6, 84.4] | +0.0 [+0.0, +0.0] | 0/0 | 1 |
| oracle_augmented | 32 | 24 | 75.0 | [57.9, 86.7] | +3.1 [+0.0, +9.4] | 1/0 | 1 |

### hard, n=16

Random 31.2%, luôn A 31.2%.

| condition | n | right | % | Wilson 95% CI | Δ vs safe_retrieved [bootstrap 95% CI] | wins/losses | McNemar p |
|---|---:|---:|---:|---:|---:|---:|---:|
| safe_shots | 16 | 3 | 18.8 | [6.6, 43.0] | +6.2 [-12.5, +31.2] | 2/1 | 1 |
| safe_retrieved | 16 | 2 | 12.5 | [3.5, 36.0] | +0.0 [+0.0, +0.0] | 0/0 | 1 |
| oracle_curated | 16 | 3 | 18.8 | [6.6, 43.0] | +6.2 [+0.0, +18.8] | 1/0 | 1 |
| oracle_augmented | 16 | 2 | 12.5 | [3.5, 36.0] | +0.0 [-18.8, +18.8] | 1/1 | 1 |

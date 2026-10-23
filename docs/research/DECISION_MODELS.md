# Decision model cho câu hỏi y khoa tiếng Việt: chọn model nền nào

*Ghi chú nghiên cứu, 23/10/2026. Claude và Codex nghiên cứu độc lập rồi đối chiếu; bản gốc của Codex ở
[DECISION_MODELS_CODEX.md](DECISION_MODELS_CODEX.md). Bối cảnh: buổi họp 23/10, thầy Thành đề xuất hướng
"open decision model" nhỏ (0,6B–2B): đo trên VM14K, tinh chỉnh bằng tài liệu Bộ Y tế, đo lại.*

## 1. Kết luận

- **Đo trước, chưa huấn luyện.** Chạy các decision model mở có sẵn trên 1.658 câu test, so với các run
  nhóm đã có. Chưa ai công bố số của decision model trên y khoa tiếng Việt, nên riêng bảng này đã là một
  kết quả.
- **Ứng viên chính: họ Decision 3.0 (d3) của vLLM Semantic Router**, ra 10/10/2026, Apache-2.0, đủ cỡ
  0,6B–27B trên nền Qwen3.5/Qwen3.8. Bản 2B (d3-nano) mạnh hơn hẳn đời trước cùng cỡ.
- **Vướng chính là huấn luyện:** d3, Decision 1.0 và Clef đều chỉ công bố code chạy, không có code huấn
  luyện. Có hai đường:
  1. Tự viết vòng huấn luyện LoRA quanh phần đầu chấm điểm của d3-nano. Giới hạn 1 ngày công.
  2. Dùng [jev-torch](https://github.com/smha1012/jev-torch) (code Apache-2.0, đã chạy thật trên
     2×H100) để huấn luyện từ Qwen3.5-0,8B/2B/4B.
- **Đối chứng bắt buộc:** cách đã có của nhóm (LoRA + xác suất chữ cái A/B/C/D, `sft_mcq_lora.py`). Bản
  này đã đạt sai số hiệu chỉnh khoảng 2%, nên "trả về xác suất thay vì viết chữ" tự nó chưa đủ là đóng
  góp. Đóng góp phải đến từ một trong ba thứ:
  - decision model đúng hơn hoặc rẻ hơn ở cùng cỡ;
  - không bị thiên lệch vị trí phương án;
  - tài liệu Bộ Y tế thêm được kiến thức.

## 2. Decision model khác cách nhóm đang làm ở đâu

| | Cách nhóm đang làm | Decision model (d3, Clef, Jev) |
|---|---|---|
| Chấm điểm | Xác suất của token chữ cái A/B/C/D ở bước kế tiếp | Một "đầu chấm điểm" đọc biểu diễn của **nội dung từng phương án** và của câu hỏi, cho một điểm mỗi phương án |
| Thứ tự phương án | Nhạy với thứ tự: model gốc nghiêng về A | Theo thiết kế không phụ thuộc chữ cái. JEV-9B giữ cùng đáp án ở 84,5% câu khi đảo phương án ([JEV.md](../../reports/eval/JEV.md)) |
| Số phương án | Cố định theo chữ cái | 2–255 lựa chọn, nhãn đặt lúc chạy |
| Huấn luyện | Cross-entropy trên chữ cái đúng | Cross-entropy (thường có làm mượt nhãn) + Brier cho hiệu chỉnh (Clef); KL theo model thầy (jev-torch) |

VM14K có thiên lệch vị trí đã đo được: khoá là A ở 29,8% câu test. Vì vậy câu "decision model có hết
thiên lệch vị trí không" là một câu hỏi đo được ngay.

## 3. Các ứng viên

| Model | Cỡ, nền | Giấy phép | Code huấn luyện | Ghi chú |
|---|---|---|---|---|
| [d3-edge](https://huggingface.co/vllm-sr/d3-edge) / [d3-lite](https://huggingface.co/vllm-sr/d3-lite) | 0,6B / 0,8B, Qwen3.5-0.8B | Apache-2.0 | Không | Nhỏ nhất, dùng cho đo hiệu quả |
| [d3-nano](https://huggingface.co/vllm-sr/d3-nano) | 2B, Qwen3.5-2B | Apache-2.0 | Không | **Ứng viên chính.** Jev Decision Index 38,9, so với Decision 2.0 cùng cỡ 27,1 (model card) |
| [d3-mini](https://huggingface.co/vllm-sr/d3-mini) | 4B, Qwen3.5-4B | Apache-2.0 | Không | Kiểm tra tăng cỡ; khoảng 35 nghìn lượt tải |
| [d3-flash](https://huggingface.co/vllm-sr/d3-flash) | 9B, Qwen3.5-9B | Apache-2.0 | Không | Mốc so sánh lớn |
| [Decision-1.0 Eos/Sol/Nox/Lux](https://vllm-sr.ai/blog/decision-models/) | 0,8B/2B/4B/9B, Qwen3.5 | Apache-2.0 | Không | Đời cũ hơn d3; Sol-2B đạt 66,3% trên bộ 54 tác vụ của nhà phát hành |
| [Cloudflare/clef-flash](https://huggingface.co/Cloudflare/clef-flash) | 9B, Qwen3.5-9B | Apache-2.0 | Không (có code model khả vi) | MMLU 91,8% theo Cloudflare, ngang Jev |
| [autotrust/JEV-9B](https://huggingface.co/autotrust/JEV-9B) | 9B, Qwen3.5-9B | Apache-2.0 | Có, qua jev-torch | **Nhóm đã đo:** 62,7%, ECE 3,1% |
| [CS1-4B](https://arxiv.org/abs/2610.27099) | 4B, tinh chỉnh toàn bộ từ Decision 2.0 Nox-4B | Chưa công bố trọng số | Không | Decision model lâm sàng đầu tiên, huấn luyện trên 12,4 triệu câu hỏi–đáp. Chỉ dùng làm tham khảo phương pháp |
| Qwen3.5-0,8B/2B/4B + đầu chấm điểm tự làm | — | Apache-2.0 | jev-torch, hoặc code của nhóm | Đối chứng cùng nền |

Chưa model nào có số đo trên y khoa tiếng Việt. Đây là chỗ nhóm điền vào.

Về phần cứng (theo Codex, là ước tính chứ chưa đo):
- Loader của các decision model đặt sẵn BF16, mà card T4 không hỗ trợ BF16. Nên chạy lần đầu trên H100
  (Modal), rồi mới thử đường FP16 cho Kaggle.
- LoRA cho bản 2B cần khoảng 7–12 GB; bản 9B nên dùng H100.

## 4. Dữ liệu huấn luyện

1. **Phần train của VM14K, 7.313 câu.** Đảo thứ tự phương án mỗi câu, vì đã biết không đảo thì model học
   cách đoán "A".
2. **Câu hỏi tổng hợp từ tài liệu Bộ Y tế.** Lần thử tháng 8 đã có sẵn đường làm, trên nhánh
   `moh-specialty-llm-pilot`. Quy trình đề xuất:
   - Chia theo văn bản và bệnh **trước khi** cắt đoạn.
   - Model sinh câu hỏi chỉ được xem đúng một đoạn tài liệu, và phải trích bằng chứng cho từng phương án.
   - Lọc tự động.
   - Một model khác giải câu hỏi mà không được xem khoá.
   - Bác sĩ duyệt thử 200 câu trước khi mở rộng.
   - Bắt đầu với 1.000 câu.
3. **Chống rò đề thi:** không cho model sinh câu hỏi xem câu val/test hay 125 câu sai; lọc trùng với mọi
   phần của VM14K.
4. **Hai kiểu đánh giá tách riêng:**
   - Đóng sách: không đưa tài liệu lúc trả lời, đo kiến thức đã học được.
   - Có tài liệu: đưa đoạn tài liệu vào, đo khả năng dùng bằng chứng.
5. **Bản quyền:**
   - Không dùng giáo trình, như thầy Nhật đã lưu ý.
   - Điều 15 Luật Sở hữu trí tuệ loại văn bản hành chính khỏi đối tượng bảo hộ, nhưng không tự động cho
     phép phát hành lại mọi phụ lục.
   - Cần ghi lại cơ sở pháp lý cho từng văn bản (theo Codex).
   - Kho hiện có **100 văn bản dùng được**, theo [audit](../../reports/analysis/moh_corpus_audit.md);
     con số 104 trước đây đếm riêng từng phần của văn bản nhiều phần.

## 5. Đánh giá để có đóng góp

- **So sánh cùng cỡ nền:**
  1. Xác suất chữ cái (cách cũ).
  2. Đầu chấm điểm tự làm.
  3. Decision model có sẵn.
- **So sánh cách tinh chỉnh:**
  1. Không tinh chỉnh.
  2. Chỉ VM14K.
  3. Chỉ dữ liệu tổng hợp.
  4. VM14K + dữ liệu tổng hợp.
- **Chỉ số:**
  - Độ đúng, kèm kiểm định McNemar trên từng câu và chạy 3 seed.
  - NLL, Brier, ECE, biểu đồ độ tin cậy.
  - Đường đánh đổi giữa tỉ lệ câu chịu trả lời và sai số (chỉ trả lời khi đủ chắc).
  - Độ trễ, bộ nhớ, chi phí cho mỗi 1.000 câu trên cùng một GPU.
- **Mốc so sánh rẻ phải có:** sửa thiên lệch chữ cái (đã có, +4,5 điểm cho 2B) và hiệu chỉnh nhiệt độ.
- **Độ bền:** đảo thứ tự phương án, đổi cách diễn đạt.
- **Phân nhóm:**
  - Theo chuyên khoa, có hiệu chỉnh khi so nhiều chuyên khoa.
  - Theo loại câu: câu phác đồ hay câu giáo trình.
  - Theo 41 câu "thiếu thuật ngữ Việt Nam".
- **Tách nhóm chuyên khoa khỏi dữ liệu huấn luyện** (như thí nghiệm bỏ Sản phụ khoa), rồi chỉ thêm tài
  liệu của nhóm đó, để đo xem tài liệu có thêm kiến thức không.
- Chia tập val thành hai phần cố định: một để chỉnh tham số, một để hiệu chỉnh xác suất. Không chỉnh gì
  trên test.

## 6. Rủi ro

| Rủi ro | Cách đối phó |
|---|---|
| Tinh chỉnh chỉ dạy cách làm đề (nhóm đã thấy điều này) | Thí nghiệm tách nhóm chuyên khoa; so với sửa thiên lệch chữ cái và hiệu chỉnh nhiệt độ |
| Tài liệu Bộ Y tế thiên về điều trị, đề thi lấy từ giáo trình (thầy Nhật) | Báo cáo riêng câu phác đồ và câu giáo trình; không nhắm vào các câu test đã biết là sai |
| Model 2B có trần kiến thức thấp | Giá trị nằm ở chi phí và khả năng biết khi nào chuyển cho người; dùng d3-mini 4B để kiểm tra |
| Đầu chấm điểm không hơn cách xác suất chữ cái | Vẫn là kết quả âm có ích, nếu đối chứng làm đúng cách |
| Viết code huấn luyện ngốn hết thời gian | Giới hạn 1 ngày; nếu không xong thì quay về jev-torch hoặc code LoRA của nhóm |

## 7. Kế hoạch hai tuần

| Thời gian | Việc | Kết quả cần có |
|---|---|---|
| 24–26/10 | **Đo không tinh chỉnh:** d3-edge, d3-lite, d3-nano, d3-mini, d3-flash, Clef-flash trên val và test, đúng định dạng câu hỏi chọn đáp án như `run_jev.py`. Chạy trên Modal H100, ước tính dưới 5 USD | Bảng độ đúng, ECE, độ trễ; chọn model 0,6–2B tốt nhất |
| 27–29/10 | **Xem đầu chấm điểm có giá trị không:** tinh chỉnh d3-nano (hoặc Qwen3.5-2B qua jev-torch) và bản LoRA chữ cái cùng nền, cùng dữ liệu VM14K, cùng số bước | Decision model có hơn cách cũ ở cùng cỡ không |
| 29/10–2/11 | **Thử dữ liệu Bộ Y tế:** 1.000 câu tổng hợp (bắt đầu từ Truyền nhiễm), bác sĩ duyệt mẫu; so VM14K so với VM14K + tổng hợp, đóng sách và có tài liệu | Tài liệu thêm kiến thức, giúp dùng bằng chứng, hay không gì cả |
| 3–5/11 | Chạy 3 seed, tách nhóm chuyên khoa, đảo phương án, đường đánh đổi trả lời/sai số, đo chi phí | Kết quả có khoảng tin cậy, đủ để viết |

GPU: Modal (khoảng 30 USD/tháng) cho lần chạy chuẩn đầu tiên; Kaggle cho các lần chạy ngắn; GPU AWS của
trường khi thầy Quang bật máy.

## 8. Claude và Codex khác nhau ở đâu

- Codex đề xuất Decision **1.0** Sol-2B làm ứng viên chính, vì blog thầy gửi chỉ nói tới bản 1.0. Khi
  kiểm tra Hugging Face, Claude thấy đã có **Decision 3.0 (d3)**, ra 10/10, và CS1 thì tinh chỉnh từ bản
  2.0. Ghi chú này chọn d3, giữ Decision 1.0 làm đối chứng phụ.
- Codex tìm ra **jev-torch** có code huấn luyện, và chỉ ra con số "104 văn bản" của Claude là đếm sai.
- Codex đề xuất bác sĩ soạn hẳn một bộ test mới cho các nhóm chuyên khoa bị tách ra. Bộ test đó giá trị
  nhất nhưng tốn công nhất; để làm mục tiêu sau, không nằm trên đường chính.
- Hai bên thống nhất: đóng góp phải đến từ so sánh có đối chứng với cách LoRA chữ cái sẵn có, không phải
  từ việc gắn thêm một đầu chấm điểm.

## Nguồn

- Cloudflare, "Clef decision models", blog, 2026. https://blog.cloudflare.com/clef-decision-models/
- vLLM Semantic Router, "Decision 1.0", blog, 2026. https://vllm-sr.ai/blog/decision-models/
- vLLM Semantic Router, Decision 3.0 (d3) model cards, Hugging Face, 10/2026. https://huggingface.co/vllm-sr/d3-nano
- TypeSafe AI, "Introducing System One models and Jev", 2026. https://typesafe.ai/blog/introducing-system-one-models-and-jev
- A. Zhang et al., "A general-purpose System One decision model for clinical records", arXiv:2610.27099, 2026.
- smha1012, jev-torch (Apache-2.0), GitHub. https://github.com/smha1012/jev-torch
- C. Guo et al., "On Calibration of Modern Neural Networks", ICML 2017. https://arxiv.org/abs/1706.04599
- Y. Geifman, R. El-Yaniv, "Selective Classification for Deep Neural Networks", NeurIPS 2017. https://arxiv.org/abs/1705.08500

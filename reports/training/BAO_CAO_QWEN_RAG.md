# Pilot Qwen3 8B + RAG hướng dẫn Bộ Y tế

## Thiết kế

Pilot tái hiện thiết kế trong `MoH_LLM_Specialty_Pilot.ipynb`, nhưng thay LLM API
bằng `qwen3:8b` chạy local qua Ollama.

- Chuyên khoa: **Tim mạch** → VM14K topic `Cardiology`.
- Nguồn RAG: 6 PDF Bộ Y tế có text trích xuất được, chia thành 1.351 chunk.
- Dữ liệu: 20 câu random, seed 42, chỉ từ frozen **validation** split; không truy
  cập test set.
- Mỗi câu được Qwen trả lời hai lần: `baseline` (câu hỏi + lựa chọn) và `rag`
  (thêm top-3 chunk TF-IDF từ guideline). Output bị ép về `Đáp án: A/B/C/D/...`.

## Kết quả

| Điều kiện | Accuracy | Parse rate |
|---|---:|---:|
| Qwen zero-shot | 60,0% (12/20) | 100% |
| Qwen + RAG | 60,0% (12/20) | 100% |

RAG không làm tăng accuracy ở pilot này: 11 câu đúng ở cả hai điều kiện, 7 câu sai ở
cả hai, RAG sửa đúng 1 câu nhưng cũng làm sai 1 câu khác. Vì `n=20`, đây chỉ là kết
quả định hướng, chưa phải kết luận về năng lực của Qwen hay chất lượng guideline.

## Diễn giải và bước tiếp theo

Qwen local tuân thủ định dạng tốt; điểm nghẽn hiện là retrieval TF-IDF: top-3 chunk
thường đến từ cùng một PDF và có thể không bao phủ kiến thức cần cho câu hỏi. Bước nên
làm tiếp là lấy đa dạng tối đa một chunk mỗi tài liệu, mở rộng toàn bộ 41 câu validation
Tim mạch, cố định prompt/retriever bằng validation, rồi mới chạy một lần trên test.

Không được diễn giải pilot này như một hệ thống chẩn đoán hoặc tư vấn lâm sàng.

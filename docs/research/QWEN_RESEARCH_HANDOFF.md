# VM14K × Qwen — Research Handoff

> **Cập nhật 2026-08-28:** hướng answer-only/QLoRA bên dưới được giữ như baseline
> lịch sử, nhưng không còn là ưu tiên nghiên cứu. Protocol hiện hành là
> `docs/research/OPENEVIDENCE_GROUNDED_PROTOCOL.md`: freeze corpus, tạo gold set
> retrieval, kiểm tra embedding search, rồi mới sinh answer + explanation + source.
> Không chạy full generation hoặc fine-tuning từ export answer-only trước khi qua
> retrieval gate.

## Mục tiêu

Đánh giá Qwen3 8B local cho VM14K: phân loại chuyên khoa, trả lời trắc nghiệm, và RAG từ hướng dẫn Bộ Y tế. Đây là benchmark nghiên cứu, không phải hệ thống chẩn đoán hoặc tư vấn lâm sàng.

## Dữ liệu và kiểm soát chất lượng

- Nguồn: `data/cleaned/clean_final.jsonl`, 10.628 câu đã qua pipeline làm sạch.
- Loại 62 câu `contradiction_pending_review=true` khỏi toàn bộ SFT.
- Dùng frozen split `splits/split_v1.json`, nhóm theo stem để tránh leakage.
- Bài toán specialty routing giữ 8.397 câu map rõ về 34 chuyên khoa chuẩn; câu đa-chuyên-khoa được giữ dưới dạng đa-nhãn.

## Kết quả đã có

### Phân loại chuyên khoa

TF-IDF word/character n-gram + One-vs-Rest Logistic Regression:

| Test metric | Giá trị |
|---|---:|
| Micro-F1 | 75,8% |
| Macro-F1 | 67,9% |
| Exact match | 43,3% |

Artifact: `models/specialty_multilabel_tfidf_logreg.joblib`. Chi tiết: `reports/training/specialty_model_report.json`.

### Qwen3 8B: phân loại chuyên khoa zero-shot

Pilot 50 câu validation: micro-F1 48,6%, thấp hơn baseline TF-IDF 72,8% trên cùng tập mẫu. Qwen thường chọn một nhãn chính trong khi nhãn VM14K là đa-nhãn. Chi tiết: `reports/training/qwen3_8b_validation_pilot.json`.

### Qwen3 8B: MCQ Tim mạch, zero-shot vs RAG Bộ Y tế

20 câu validation, 6 PDF born-digital, 1.351 TF-IDF chunk, top-3 context:

| Điều kiện | Accuracy |
|---|---:|
| Zero-shot | 60% (12/20) |
| RAG top-3 | 60% (12/20) |

RAG sửa đúng một câu và làm sai một câu khác. Chi tiết: `reports/training/qwen3_8b_moh_rag_cardiology_validation.json`.

### Ablation 5 hướng Qwen MCQ

| Hướng | Accuracy (20 validation) |
|---|---:|
| zero-shot | 60% |
| TF-IDF RAG top-3 | 60% |
| RAG đa dạng 3 PDF | 50% |
| few-shot, 2 ví dụ train | 60% |
| RAG đa dạng + few-shot | 45% |

Hiện chưa có bằng chứng context/RAG làm Qwen3 8B tốt hơn zero-shot. Không dùng test để chọn cấu hình. Chi tiết: `reports/training/BAO_CAO_QWEN_RAG_ABLATION.md`.

## Bộ dữ liệu QLoRA/SFT đã sẵn sàng

`scripts/training/export_qwen_sft_mcq.py` xuất dữ liệu chat Qwen:

- `data/derived/qwen_sft_mcq/train.jsonl`: 21.939 mẫu = 7.313 câu train × 3 thứ tự phương án.
- `data/derived/qwen_sft_mcq/val.jsonl`: 1.595 câu, không augmentation.
- `data/derived/qwen_sft_mcq/test.jsonl`: 1.658 câu, không augmentation.

Mỗi train augmentation hoán đổi phương án theo seed cố định và remap đáp án, để model không học bias vị trí A/B/C/D. Mẫu dùng Qwen chat messages, `/no_think`, và output chỉ gồm đáp án chuẩn.

Tái tạo:

```powershell
python scripts/training/export_qwen_sft_mcq.py --force
```

## Đề xuất thí nghiệm tiếp theo

1. Qwen3 8B zero-shot với 3 lần shuffle phương án và majority vote.
2. QLoRA/SFT Qwen3 8B với train data trên; giữ validation để chọn cấu hình.
3. Ablation QLoRA: rank 8 vs 16, learning rate `5e-5` vs `1e-4`, 1–3 epochs.
4. Chạy test đúng một lần cho cấu hình tốt nhất trên validation.
5. Chỉ thử RAG-SFT khi retriever dùng embedding/reranker và có kiểm tra evidence coverage.

Không làm DPO/RLHF trước khi có tập preference/negative answer đã được bác sĩ xác minh. QLoRA không chạy từ GGUF/Ollama; cần Qwen weights gốc và CUDA GPU.

## Lệnh tái lập các benchmark hiện có

```powershell
python scripts/training/train_specialty_classifier.py --force
python scripts/training/benchmark_qwen_specialty.py --limit 50 --force
python scripts/training/benchmark_qwen_moh_rag.py --limit 20 --force
python scripts/training/benchmark_qwen_moh_rag_variants.py --limit 20 --force
```

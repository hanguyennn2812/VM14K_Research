# Qwen3 8B — ablation RAG/few-shot (validation Tim mạch)

Cùng Qwen, cùng 20 câu validation, cùng parser. Chỉ cách cấp ngữ cảnh thay đổi.

| Hướng | Accuracy | Đúng / n |
|---|---:|---:|
| zero_shot | 60.0% | 12/20 |
| tfidf_top3 | 60.0% | 12/20 |
| diverse_doc_top3 | 50.0% | 10/20 |
| few_shot_2 | 60.0% | 12/20 |
| diverse_rag_plus_few_shot | 45.0% | 9/20 |

Tập test không được truy cập trong ablation này.

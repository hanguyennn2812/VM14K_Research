# Brief cho Claude2: VM14K, bước tiếp theo (2026-11-09)

Repo: `F:\VM14K_Research`, nhánh `eval-zero-shot-baselines`. Đọc file này trước, rồi mới đọc repo.

## Mục tiêu (không đổi)

Tìm cách làm **một model nhỏ** (≤ 9B, lý tưởng 2–4B, chạy được trên laptop hoặc 1 GPU miễn phí) trả lời
**1–2 chuyên khoa của VM14K** (arXiv 2506.01305) tốt hơn mức paper báo cáo, và giải thích được vì sao.
Chuyên khoa đề xuất: **Truyền nhiễm (Infectious Diseases)**: 232 câu test, 245 câu val, kho MoH lớn nhất
(18 văn bản, 1.196 trang). Mốc paper: DeepSeek-R1 77,8 trên chuyên khoa này. Các Thầy muốn một đóng góp rõ
ràng và kết thúc giai đoạn thử nghiệm sớm.

## Đã biết (đừng đo lại)

Nguồn: memory ở `C:\Users\PC\.claude\projects\f--VM14K-Research\memory\`, `reports/eval/*.md`
(DECISION.md, FINETUNE.md, QWEN27B.md, VOTE.md, MOH_DECISION_REPORT_20261106.md), `docs/research/`.

- Test 1.658 câu, đã đóng băng. Luôn báo kèm mốc ngẫu nhiên và luôn-chọn-A (~30% đáp án là A).
- LoRA trên MCQ dạy thói quen (bỏ bias chữ A), không dạy kiến thức. 2B +9,2 (một nửa là letter prior), 9B +2,4.
- Decision model: d3-nano (2B) 52,9; jev-torch 2B train trên VM14K 53,0; d3-flash (9B) 67,9; d3 27B 74,4;
  d3 27B + 3 câu train TF-IDF + 3 chunk MoH 76,2 (Truyền nhiễm 80,6 vs paper 77,8, p 0,17).
- Qwen3.5-27B + 3 câu train retrieve: 72,7. Gain retrieval chỉ có ở câu có câu train giống (sim ≥ 0,3).
- Thử nghiệm MoH (06/11): 533 câu MCQ sinh từ văn bản MoH bởi Nemotron, nhãn mềm d3, train 2B jev-torch:
  VM14K test 52,4 vs 52,8 (p 0,72). Nhớ câu viết lại +22,3 nhưng có thể chỉ quen mặt đáp án.
  **VM14K test đã "tiêu" cho dữ liệu này**: chọn mọi thứ trên val, chỉ chấm test một lần ở cuối.
- **Chưa báo cáo, có trong working tree:** probe fact-pair (`scripts/training/gen_moh_pairs.py`,
  `scripts/eval/analyze_pairs.py`, `data/derived/moh_mcq/fact_pairs_v1_20261106.gated.jsonl`, 369 cặp,
  runs `reports/eval/runs/jevtorch__Qwen_Qwen3.5-2B__pairs__{vm14k,moh,x4}.jsonl`). Kết quả x4: new facts
  +4,5, control +2,8, **new − control +1,7 [−12,0; +15,9]**; seen facts −7,0. Tức là train MCQ chưa truyền
  kiến thức. Đã bắt đầu hướng CPT (continual pre-training, arXiv 2605.01077): `scripts/training/gen_moh_docs.py`,
  `cpt_docs_v1_merged_20261106.jsonl` (171 văn bản viết lại/wiki), smoke 9B 32 câu
  (`reports/eval/runs/cpt__Qwen_Qwen3.5-9B__smoke__{before,after}.jsonl`), phần sửa chưa commit trong
  `scripts/training/modal_jevtorch.py`.
- Kết luận chung đến nay: kiến thức bị giới hạn bởi backbone; muốn model nhỏ giỏi một chuyên khoa thì phải
  (a) đưa kiến thức vào lúc suy luận (RAG) hoặc (b) nạp được kiến thức vào trọng số (CPT, distillation) và
  chứng minh được bằng probe kiến thức chứ không phải bằng MCQ quen mặt.

## Tài nguyên

- **NVIDIA Build** (NVIDIA_API_KEY trong env user, ~40 RPM, miễn phí): nemotron-3-ultra-550b-a55b,
  nemotron-3.5-lightning-30b-a3b ổn định; DeepSeek/Gemma hay timeout. Probe trước khi xếp hàng.
- **Kaggle** (miễn phí, 2× T4 16 GB, không bf16): `.venv\Scripts\kaggle.exe kernels push -p <dir>
  --accelerator NvidiaTeslaT4`. Cần `pip uninstall -y torchao` trước peft. Mẫu: `scripts/eval/kaggle_27b_rag.py`,
  `scripts/training/kaggle_heldout.py`.
- **Local**: Intel Arc 140T qua torch XPU (`.venv-xpu`, `HF_HOME=F:/hf_cache`): eval 2B logit 1.658 câu ~2,5 phút,
  LoRA 2B 1 epoch ~70 phút, cần gradient checkpointing. Ollama CPU-only. Ổ C: và D: gần đầy, model để ở F:.
- **Modal: KHÔNG dùng** trong đợt này (tốn tiền, owner chỉ cho NVIDIA/Kaggle/local).

## Luật làm việc

- Không `git commit`, không `git push`, không merge, không xoá file người khác. Không gửi gì cho các Thầy.
- Chọn cấu hình trên **val**. Chỉ chạm test khi kế hoạch đã ghi rõ là lần chấm cuối, và ghi lại điều đó.
- Mọi kết quả: n, %, CI 95% (bootstrap hoặc McNemar), mốc ngẫu nhiên và luôn-chọn-A.
- File tạm để ở `D:\tmp\vm14k-claude2\`. Kết quả lâu dài để ở chỗ ghi trong từng pha.
- Ghi file tiếng Việt bằng Python `encoding="utf-8"` hoặc Write/Edit, không pipe PowerShell.
- Nếu bị chặn (API chết, Kaggle hết quota, OOM), ghi rõ lý do vào file kết quả rồi dừng, không bịa số.

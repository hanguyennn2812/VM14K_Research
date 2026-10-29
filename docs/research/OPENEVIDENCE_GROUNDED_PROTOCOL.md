# VM14K × tài liệu Bộ Y tế — protocol nghiên cứu grounded QA

**Ngày chốt protocol:** 2026-08-28  
**Phạm vi:** nghiên cứu benchmark; không phải hệ thống chẩn đoán hoặc tư vấn lâm sàng.  
**Trạng thái:** phase 0–1; retriever và trainer đã được triển khai/smoke-test,
nhưng chưa được phép chạy full generation hoặc fine-tuning chính thức trước gate.

## 1. Câu hỏi nghiên cứu

Không tối ưu thêm một con số accuracy đơn lẻ. Mục tiêu chính là đo:

> Bao nhiêu câu VM14K có thể được trả lời bằng một đoạn bằng chứng truy nguyên được
> từ tài liệu y khoa chính thức của Việt Nam, và tỷ lệ đó thay đổi thế nào theo
> chuyên khoa?

Câu hỏi phụ:

1. Embedding retrieval có tìm đúng trang hỗ trợ tốt hơn TF-IDF không?
2. Với cùng một model, cung cấp đúng bằng chứng có thay đổi accuracy so với
   zero-shot không?
3. Câu trả lời sinh ra có thực sự được đoạn trích hỗ trợ không?
4. Automatic support check có đủ tin cậy khi đối chiếu với một mẫu bác sĩ chấm không?

Đóng góp kỳ vọng không phải là “mô hình nhỏ đánh bại frontier model”, mà là một
đánh giá có provenance ở bối cảnh tiếng Việt: answer + explanation + source page,
kèm coverage theo chuyên khoa.

## 2. Trạng thái repo đã xác nhận

- Dataset clean có **10.628** dòng, trong đó **62** dòng còn
  `contradiction_pending_review=true`; còn **10.566** dòng dùng được. Vì vậy con số
  10.640 trong note không phải denominator hiện tại của repo.
- Có 262 câu Cardiology dùng được: train 182, validation 41, test 39.
- Pilot hiện tại dùng 20/41 câu validation Cardiology, 6 PDF, 1.351 chunk:
  zero-shot 60% và TF-IDF RAG 60%.
- Tree hiện có 111 PDF dưới `data/Chuyên khoa`: 110 source PDF trong 27 thư mục và
  một PDF index ở root. File `.tex` index liệt kê 109 source entries trong 26
  sections. Multiset diff giải thích chênh lệch hiện tại: index thiếu hai file trong
  thư mục `Trạm y tế`, còn file `Quyet_dinh_so_3902...methadone...pdf` có trong
  index nhưng không có trên disk. `data/MoH_corpus_spec.md` vẫn ghi provisional
  112 PDF / 26 thư mục từ snapshot cũ. Chưa có manifest frozen hoặc extract report;
  phải quyết định policy cho ba file này trước khi báo cáo coverage toàn corpus.
- Retriever cũ ghép text theo tài liệu rồi chunk theo từ, không giữ page provenance.
  Cách đó không đủ để xuất citation kiểm chứng được.
- Export SFT cũ dạy output chỉ một chữ cái và `/no_think`. Artifact này được giữ
  như baseline lịch sử, nhưng không dùng cho hướng grounded QA mới.

## 3. Cập nhật literature sau note OpenEvidence

Ba kết quả không nên bị gộp thành một kết luận đơn giản:

1. OpenEvidence công bố 100% ngày 2025-08-15 qua press release, đồng thời phát hành
   giải thích theo từng câu. Đây là product claim, không phải peer-reviewed study.
2. Bài độc lập trên *Nature Medicine* (2026-06-12) cho thấy frontier LLM hơn
   OpenEvidence và UpToDate Expert AI trên MedQA, HealthBench và 100 real clinical
   queries. Kết quả này ủng hộ việc không suy ra chất lượng thực tế từ một practice
   set công khai.
3. Hai preprint mới hơn làm kết luận tổng quát bớt chắc chắn:
   - Real-POCQi (2026-06-27) dùng 620 câu hỏi từ chính OpenEvidence và 149 bác sĩ
     chấm theo chuyên khoa; OpenEvidence được đánh giá cao nhất. Tuy nhiên chính
     paper ghi OE thực hiện data collection/survey và query distribution có thể có
     routing bias.
   - VITA (2026-08-12) cho thấy RAG theo corpus/quốc gia có thể ngang hoặc hơn
     frontier LLM trên HealthBench, nhưng kiến trúc/corpus là proprietary; ở
     sensitivity 500 câu với judge trung lập, VITA và GPT-5.5 chỉ đạt parity về
     mean score. Một số tác giả có liên hệ trực tiếp với VITA/funder.

Kết luận dùng cho VM14K: không đặt giả thuyết “RAG luôn tăng accuracy”. Giả thuyết
có thể kiểm nghiệm là **corpus đúng bối cảnh + retrieval đúng trang làm tăng
grounding/coverage**, còn accuracy là outcome phụ và có thể tăng, giữ nguyên hoặc giảm.

Nguồn chính:

- OpenEvidence press release: https://www.prnewswire.com/news-releases/openevidence-creates-the-first-ai-in-history-to-score-a-perfect-100-on-the-united-states-medical-licensing-examination-usmle-302531156.html
- Vishwanath et al., *Nature Medicine* 2026: https://doi.org/10.1038/s41591-026-04431-5
- Feng et al., Real-POCQi: https://arxiv.org/abs/2606.28960
- Reddy et al., VITA: https://arxiv.org/abs/2608.12138
- BGE-M3: https://arxiv.org/abs/2402.03216

## 4. Outcomes và unit of analysis

### 4.1 Retrieval outcomes — primary gate

Trên gold set 30 câu validation Cardiology:

- `coverage`: tỷ lệ câu có ít nhất một trang BYT thực sự hỗ trợ đáp án;
- Recall@1, @3, @5 và @10 trên các câu `covered`;
- MRR@10;
- Wilson 95% CI cho từng recall;
- error analysis theo: no-document coverage, synonym/acronym, table/numeric,
  cross-page, scan/no text layer, và wrong-specialty routing.

TF-IDF và BGE-M3 dùng cùng page chunks, cùng query và cùng gold annotations.
Query chỉ gồm question + toàn bộ options; không thêm gold answer.

Eligibility loại 62 câu pending contradiction và một Cardiology validation row
`7385849c6bb44b54a55f37349115b504` còn marker nguồn
`??????KHÔNG BIẾT???????`. Exclusion này là residual data-quality rule được áp
trước retrieval; không tính nó thành `not_covered` hay retrieval failure.

**Go/no-go đã định trước:** chưa chạy generation toàn bộ nếu dense Recall@5 dưới
0,80 hoặc không hơn TF-IDF ít nhất 0,10 tuyệt đối. Với n=30, CI và error analysis
phải được báo cáo; threshold là engineering gate, không phải statistical claim.

### 4.2 Generation outcomes

Chỉ sau khi qua retrieval gate, chạy trên validation:

- cùng model, cùng decoding, hai điều kiện: closed-book và retrieved-evidence;
- answer accuracy với bootstrap 95% CI;
- paired McNemar test cho chênh lệch đúng/sai;
- parse rate;
- citation correctness: cited page có nằm trong gold evidence không;
- citation completeness: các claim chính trong explanation có được passage hỗ trợ;
- abstention correctness khi evidence không đủ.

Test split giữ untouched cho tới khi toàn bộ prompt, retriever, threshold và support
checker đã freeze trên validation.

### 4.3 Support checker

Input checker gồm question, selected answer, explanation và cited passage. Output
bắt buộc là JSON với `supported | unsupported | insufficient` và claim-level reasons.

Không dùng agreement của checker với chính model sinh câu trả lời như validation.
Mẫu 200 câu được bác sĩ spot-check phải được lấy stratified theo chuyên khoa và theo
ba nhãn checker. Báo cáo confusion matrix, macro-F1, sensitivity cho
`unsupported/insufficient`, và Cohen's kappa. Threshold triển khai được chốt trước
khi đọc test.

Implementation v2 còn tách đáp án ghép thành các claim nguyên tử: từng thuốc,
liều, thủ thuật, điều kiện và thay đổi lối sống đều phải có citation trực tiếp.
Smoke test v1 từng nhận sai một đáp án ghép vì guideline hỗ trợ aspirin/statin/cắt
cụt/bỏ thuốc lá nhưng không chỉ định trực tiếp metformin; checker còn viện dẫn nhầm
trang danh mục viết tắt. Gate mặc định đã chặn row này, và v2 hiện gán claim
metformin là thiếu bằng chứng rồi loại toàn row. Kết quả này là lý do thực nghiệm
để không coi same-model self-check là human gold.

## 5. Gold set 30 câu Cardiology

Tạo template cố định:

```powershell
python scripts/retrieval/export_cardiology_gold_template.py
python scripts/retrieval/prepare_cardiology_gold_candidates.py
```

File `*_candidates.jsonl` chỉ là search aid giúp mở nhanh đúng PDF/trang. Nó không
ghi đè template, không tự đổi `annotation_status`, và không được coi top hit là
gold nếu annotator chưa mở trang nguồn để xác nhận.

Mỗi câu phải được gán một trong ba coverage labels:

- `covered`: có trang BYT hỗ trợ đáp án;
- `not_covered`: đã tìm hết 6 tài liệu Cardiology nhưng không có bằng chứng phù hợp;
- `uncertain`: chưa thể kết luận, ví dụ scan/table lỗi hoặc cần chuyên gia.

Với `covered`, `gold_evidence` phải chứa tên file đúng tuyệt đối, `page_start`,
`page_end`, và có thể nhiều passage thay thế. Không được dùng output của retriever
đang đánh giá để âm thầm quyết định gold; annotator có thể search tài liệu, nhưng
phải kiểm tra trang nguồn trực tiếp. `annotation_status=complete` chỉ khi đã điền
xong coverage và evidence.

## 6. Chạy retrieval evaluation

Môi trường cần Python 3.11+, các package trong `requirements.txt`, Ollama đang chạy,
và model embedding local `bge-m3`. Backend SentenceTransformers vẫn được giữ để
tái lập trên GPU/cloud.

```powershell
ollama pull bge-m3
python scripts/retrieval/evaluate_moh_retrieval.py --force
```

Output chính:

```text
reports/retrieval/cardiology_retrieval_eval.json
```

Script từ chối chạy nếu gold set còn `pending`, giữ citation ở cấp file + PDF page,
và cache embedding trong `data/interim/` (đã gitignore).

## 7. Format grounded SFT mới

Không sửa hoặc tái sử dụng output answer-only cũ. Sau khi generation và support
check hoàn tất, tạo `data/derived/grounded_vm14k.jsonl` với ít nhất:

```json
{
  "id": "...",
  "split": "train",
  "question": "...",
  "options": ["..."],
  "answer": "B",
  "explanation": "...",
  "citations": [
    {
      "source_file": "...pdf",
      "page_start": 12,
      "page_end": 12,
      "passage": "đoạn trích thực tế"
    }
  ],
  "support_label": "supported"
}
```

Candidate generator dùng hybrid reciprocal-rank fusion (TF-IDF + BGE-M3), sau đó
Qwen3:8B tạo explanation có trích dẫn và tự kiểm định lại bằng prompt nghiêm ngặt:

```powershell
python scripts/retrieval/generate_grounded_cardiology.py
```

Vì hai lượt vẫn dùng cùng một model, output được đánh dấu
`verification_status=uncalibrated_auto_check`, không phải human gold. Sau khi
human verification hoặc calibration đạt gate, mới export:

```powershell
python scripts/training/export_qwen_sft_grounded.py
```

Exporter chỉ nhận `supported`, yêu cầu passage/citation không rỗng, không shuffle
options để tránh tách explanation khỏi nội dung đáp án, và sinh assistant output gồm
đáp án + giải thích + nguồn/trang. Mặc định exporter còn yêu cầu
`human_verified | calibrated_auto_check`; bypass chỉ dành cho exploratory pilot và
phải dùng flag có tên rõ ràng `--allow-uncalibrated-auto-check`.

QLoRA chạy trên CUDA bằng:

```bash
python -m pip install -r requirements-gpu.txt
python scripts/training/train_qwen_grounded_qlora.py
```

Trainer dùng Qwen3-8B, NF4 + double quant, all-linear LoRA rank 16, assistant-only
loss, và chọn checkpoint có validation loss thấp nhất. Nó abort nếu thiếu CUDA,
train/validation trùng source ID, evidence chưa verify (trừ exploratory opt-in),
hoặc bất kỳ sequence nào sẽ bị truncate. Test không được load ở bước này.

## 8. Thứ tự thực thi đã sửa

1. Quyết định đưa `Trạm y tế` vào scope hay không và khôi phục/ghi nhận file 3902
   đang thiếu; sau đó build và freeze manifest có hash.
2. Tạo và hoàn thành gold set 30 câu validation Cardiology.
3. So sánh TF-IDF với BGE-M3 trên Recall/MRR; làm error analysis.
4. Chỉ khi qua gate: freeze retriever và chạy generation trên validation.
5. Xây support checker, rồi bác sĩ spot-check 200 câu để hiệu chuẩn.
6. Freeze pipeline; chạy full clean set để báo coverage theo specialty.
7. Tạo grounded SFT export; fine-tune là thí nghiệm sau cùng, không phải điều kiện
   để có kết quả nghiên cứu chính.
8. Chỉ chạy test đúng một lần cho cấu hình cuối.

## 9. Những điều không được claim

- Không gọi practice questions là kỳ thi thật.
- Không gọi citation “đúng” chỉ vì model in ra tên tài liệu.
- Không suy từ 20 hoặc 30 câu Cardiology sang 34 chuyên khoa.
- Không gộp `not_covered` với retrieval failure.
- Không dùng automatic checker chưa được bác sĩ hiệu chuẩn như ground truth.
- Không công bố full-set accuracy nếu test đã được dùng để chọn prompt/retriever.

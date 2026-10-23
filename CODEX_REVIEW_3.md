## 1. Claims ledger: đối chiếu từng dòng R/F và các dòng P

**Kết luận:** các số đếm chính khớp. Vấn đề lớn nằm ở cách diễn giải, nguồn dẫn chưa đầy đủ và ngoại lệ Gemini trong L16b.

Tôi chỉ đọc repo. Các lệnh Python dùng `-B`; không chạy các hàm tạo workbook hay pipeline ghi dữ liệu. Dedup được chạy không có `--out/--report`. Với difficulty, tôi chạy mã tính toán sau khi bỏ khối ghi report trong bộ nhớ. Không sửa file trong worktree.

**MATCH dưới đây xác nhận số liệu, không mặc nhiên xác nhận kết luận đi kèm.**

| Ledger | Kết quả | Giá trị tôi đối chiếu và nguồn |
|---|---|---|
| L1 — R | **MATCH** | Chạy `vm14k_dupes_and_contradictions.py`: **12.488 dòng**. |
| L2 — F | **MATCH, có giới hạn phạm vi** | PDF §1.1 mô tả một pool phát hành ba lần. Tôi kiểm tra trực tiếp: cả ba JSONL có **12.488 dòng**, cùng ID/thứ tự; stem, bộ options và nội dung đáp án được giữ. Điều này xác nhận cấu trúc các file công khai được kiểm tra, không chứng minh private set chưa từng tồn tại. |
| L3 — R | **MATCH** | **1.125 nhóm**, **2.450 dòng**, **19,62%**. Chạy lại script được dẫn. |
| L3b — R | **MATCH** | **67 nhóm**, **152 dòng**, theo khóa chuẩn hóa và nội dung option được đánh dấu đúng. |
| L3c — R | **MATCH** | Chạy lại: **12.488 → 10.956**, loại **1.532**; sau Level 1 còn **11.164**, tức loại **1.324/1.325** bản dư; contradiction groups **67 → 0**; còn **1** bản dư. Đây là script tái triển khai có các điều chỉnh input/NaN được ghi trong mã. |
| L5 — R | **MATCH về số** | Đếm raw: Medium **7.093**, Easy **4.112**, Challenging **1.193**, Hard **90** → **56,80/32,93/9,55/0,72%**. Khớp các giá trị Figure 5 được ghi trong `VM14K_session_findings.md`. Sự trùng tỷ lệ không chứng minh chắc chắn figure được tạo từ chính file này. |
| L6 — R | **MATCH** | Two-option: raw **1.240**, clean **1.025**, test **173**. Tôi đếm trực tiếp JSONL. |
| L7 — R | **MATCH** | Raw A: **3.915/12.488 = 31,3501%**, random **27,6228%**; four-option **3.185/11.111 = 28,6653%**; two-option **667/1.240 = 53,7903%**. Clean A **3.219/10.628 = 30,2879%**, random **27,4799%**. Test A **494/1.658 = 29,7949%**, random **27,6387%**. |
| L8 — F | **MATCH với tài liệu được dẫn** | `VM14K_manual_verify.pdf` §6 ghi **“at least 80 questions”**. PDF không cung cấp danh sách đủ 80 ID hoặc lệnh tái tạo; đây vẫn là xác nhận từ report, chưa phải số được tôi tái kiểm độc lập. |
| L9 — R | **MATCH** | Tính lại: **223/1.125 = 19,82%**; **1.294/1.567 = 82,5782%**; generalized Fleiss κ **0,647075**. |
| L10 — R | **MATCH** | Report và tính lại khớp: Easy **2.301/3.808 = 60,4254%**; Medium **3.831/6.545 = 58,5332%**; Challenging **687/1.162 = 59,1222%**. Report: Δ **1,30 pp**, CI **[−4,06; 6,62]**. Chạy lại: OR **1,057961**, CI **[0,834464; 1,341318]**, Spearman **−0,026921**. |
| L11 — F | **MATCH số; MISMATCH đường dẫn nguồn** | JSONL và split cho **10.628**, quarantine **316**, pending **62**, usable train/val/test **7.313/1.595/1.658**. Nhưng **`reports/training/qwen_sft_mcq_data_report.json` không tồn tại** trong worktree. Thay nguồn bằng các artifact hiện có. Manifest chưa lọc có **7.382/1.596/1.662** ID. |
| L12 — F/R | **MATCH** | Đếm record cuối không lỗi: DeepSeek **1.183/1.658 = 71,3510%**; Gemma-31B **1.188 = 71,6526%**; Qwen3.5 **1.044 = 62,9674%**; Gemma-12B **993 = 59,8914%**; Qwen3 **904 = 54,5235%**; MedGemma **778 = 46,9240%**; Llama **775 = 46,7431%**. Các số làm tròn trong §6 khớp. Wilson của Llama **[44,4; 49,1]%** khớp. |
| L13 — F | **MATCH với report** | `RAW_VS_CLEAN.md`: raw−clean **−0,1 pp** cho Llama, **+0,2 pp** cho Qwen3.5. Đây là **ước lượng có trọng số**, không phải đánh giá toàn bộ 12.488 dòng cho mọi model. |
| L14 — R | **MATCH** | Tính độc lập từ logs: pair disagreement **238**; Nemotron có record **210**, cùng chọn **140**; all-seven-wrong **125**; giao **95**; hợp **268**. |
| L15 — R | **MATCH khi ghi rõ tập so sánh** | Log có **320** ID giải thích không lỗi; giữ đáp án trên **90/140** triple-agreement items; **4** abstentions. **108/237** đổi đáp án đúng **trong hợp hai tập flagged, có cả quick/explanation record**. Trên toàn bộ giao hai logs hiện có, kết quả là **115/276**; không dùng hai mẫu số thay thế nhau. |

L7b không mang trạng thái R/F và không có nguồn cụ thể; nhận xét về việc trộn tỷ lệ four-option với tỷ lệ all-row phù hợp với số tôi đếm, nhưng nên dẫn chính xác file/phiên bản cần sửa.

Với dòng P:

- **L4: MATCH** với mô tả `correctOption` ở Table 1. Mô tả schema không chứng minh mọi khóa cuối cùng đều do GPT-4o quyết định.
- **L16: MATCH**: §4 mô tả cùng một model chạy ba lần, shuffle options rồi vote.
- **L16b: MISMATCH một phần**. Bảng dưới đối chiếu đủ 17 dòng, theo [VM14K HTML v1, Tables 2–3](https://arxiv.org/html/2506.01305v1).

| Model | Table 2 pass@1 | Table 2 pass@3 | Table 3 reference | Đối chiếu |
|---|---:|---:|---:|---|
| GPT-4o | 72,74 | 80,40 | 80,40 | pass@3 |
| o3-mini | 71,42 | — | 71,42 | pass@1 |
| Claude 3.5 Sonnet | 71,46 | 75,62 | 75,62 | pass@3 |
| Gemini 2.0 Flash | 75,67 | **77,92** | **77,29** | **Không khớp cả hai** |
| DeepSeek-R1 | 78,17 | 83,02 | 83,02 | pass@3 |
| Qwen3-32B | 72,47 | — | 72,47 | pass@1 |
| Qwen3-30B-A3B | 71,32 | — | 71,32 | pass@1 |
| Llama 4 Maverick | 71,76 | 73,13 | 73,13 | pass@3 |
| Phi-4 | 51,15 | 69,18 | 69,18 | pass@3 |
| Gemma3-27B | 63,38 | 64,45 | 64,45 | pass@3 |
| Gemma3-12B | 58,05 | 60,03 | 60,03 | pass@3 |
| Llama-3.1-8B | 48,73 | 60,88 | 60,88 | pass@3; tên Table 3 thiếu “.1” |
| Llama-3-70B-UltraMedical | 54,96 | 67,34 | 67,34 | pass@3 |
| Meditron3-70B | 42,27 | 59,55 | 59,55 | pass@3 |
| HuatuoGPT-o1-8B | 54,52 | — | 54,52 | pass@1 |
| Llama-3.1-8B-UltraMedical | 41,86 | 48,01 | 48,01 | pass@3 |
| Meditron3-8B | 23,05 | 30,04 | 30,04 | pass@3 |

**Kết luận đủ 17 dòng:** 12 reference khớp pass@3, bốn khớp pass@1, một không khớp. Vì vậy “mixed pass@3/pass@1” đúng về cấu trúc bảng, nhưng không mô tả chính xác mọi dòng.

Thêm lỗi số học: Llama 4 có ensemble **72,46**, reference **73,13**, nên Δ phải là **−0,67**, không phải **−1,33**. Gemini cần xác minh reference trước khi sửa Δ. Các chi tiết này đều hiện trong [hai bảng gốc](https://arxiv.org/html/2506.01305v1).

## 2. Các câu thiếu ledger hoặc vượt quá bằng chứng

Tôi liệt kê cả những câu có thể đúng nhưng chưa được ledger hỗ trợ. Các phát biểu related work được xử lý tiếp ở mục 4.

| Vị trí và câu trích | Vấn đề | Nên viết thay |
|---|---|---|
| Abstract: **“VM14K … is the first public Vietnamese medical multiple-choice benchmark.”** | Ledger chưa kiểm tra ưu tiên lịch sử; paper gốc tự nhận “first” chưa đủ cho xác nhận độc lập. | **“VM14K was introduced as the first Vietnamese medical multiple-choice benchmark.”** Hoặc bổ sung khảo sát chứng minh “first public”. |
| Abstract: **“It was never passed through the authors' own published deduplication pipeline”** | **“never”** khẳng định lịch sử xử lý không quan sát được. Duplicates có thể được đưa lại sau một bước dedup. | **“The released artifact is inconsistent with the output of our adapted implementation of the published deduplication pipeline.”** |
| Abstract: **“… removes … all 67 groups of identical questions with contradictory answer keys.”** | “Identical” ở đây là **sau chuẩn hóa**. Xóa các bản sao làm mất mâu thuẫn quan sát được nhưng không sửa đúng khóa của survivor. | **“… collapses all 67 groups with conflicting keys under the authors’ normalization, without adjudicating which key is correct.”** |
| Abstract: **“The difficulty labels are unreliable and do not discriminate.”** | Bất nhất giữa copies không chứng minh toàn bộ nhãn sai; kiểm định không có ý nghĩa không chứng minh không có discrimination. | **“Difficulty labels are inconsistent across normalized duplicate groups and show weak evidence of discrimination for the seven evaluated LLM configurations.”** |
| Abstract: **“… seven LLMs score 59–60% on Easy, Medium and Challenging alike.”** | Số là **mean across models**, không phải mỗi model đều đạt mức đó. “Alike” hàm ý tương đương chưa kiểm định. | **“Mean accuracy across seven LLMs is 60.4%, 58.5%, and 59.1% on Easy, Medium, and Challenging test items, respectively.”** |
| Abstract: **“On 14% of test questions, two frontier models choose the same option and that option is not the key.”** | Phải ghi test đã đánh giá; “frontier” không có tiêu chí trong evidence. | **“On 238/1,658 evaluated test questions (14.4%), DeepSeek-v4.1-flash and Gemma-4-31B select the same non-key option.”** |
| Abstract: **“A clinician review with a pre-registered sampling design finds [TBD…]”** | Review chưa có kết quả; “pre-registered” chưa có registration có dấu thời gian, phiên bản cố định. | Hiện tại: **“We specify a clinician review protocol before annotation; review results are pending.”** Chỉ dùng “pre-registered” khi có bằng chứng đăng ký. |
| Abstract: **“We release a cleaned, deduplicated split with a full audit trail and re-evaluate [N] models.”** | `[N]` chưa hoàn tất; “cleaned” dễ bị hiểu là medically validated. “Full” cần nói rõ trail bao gồm gì. | **“We provide a structurally cleaned split, a removal-reason map and repair logs, and evaluate seven models; clinical validation remains pending.”** |
| Abstract: **“Model rankings are robust to cleaning (overall scores move by ≤0.2 points)”** | L13 chỉ có hai model; raw score là estimate. Không kiểm tra ranking của bảy model hoặc ranking paper gốc. | **“For two models, estimated raw-minus-clean score changes are −0.1 and +0.2 percentage points; their relative order is unchanged.”** |
| §1: **“Benchmarks outside English carry most of the evidence … yet they are audited far less often than MMLU or MedQA.”** | Hai so sánh “most” và “far less often” không có nguồn hay định nghĩa corpus. | **“Local-language benchmarks provide evidence about medical QA performance, but their validity requires independent assessment.”** |
| §1: **“VM14K is the reference point for Vietnamese medical QA: 34 specialties, four difficulty levels, and 17 models evaluated in the paper.”** | “The reference point” chưa có bằng chứng sử dụng. **34/4/17** thiếu ledger riêng. | **“The VM14K paper reports 34 specialties, four difficulty levels, and evaluations of 17 models.”** Thêm ledger dẫn paper; phân biệt ontology công bố với topic strings thực tế. |
| §1: **“A reproducible audit … run with the authors' own code”** | Dedup là tái triển khai thích nghi, không chạy nguyên trạng script gốc. | **“… using the authors’ normalizer and an explicitly adapted implementation of their deduplication algorithm.”** |
| §1: **“… every removed row kept and labelled with the reason”** | Quarantine chỉ chứa 316 dòng; các dòng dedup dùng raw file và fate map. | **“… preserving quarantined records and mapping all removed raw rows to removal reasons.”** Dẫn thêm `fates.json`, không chỉ quarantine. |
| §3: **“No such sets exist in the release”** | Chấp nhận được nếu giới hạn rõ snapshot công khai; private set không phải vật bắt buộc có trong public download. | **“The audited public snapshot does not expose the advertised sample/full partition or identifiers for the private evaluation set.”** |
| §3: **“All questions verified by experts”** | Là paraphrase mạnh hơn việc paper báo một quy trình/khối lượng verification. Cần quote đúng phát biểu gốc và ledger riêng. | **“The paper reports expert involvement in verification; the release does not provide item-level verification provenance.”** |
| §3: **“Fig. 5 matches the 12,488-row file to two decimals”** | Câu này phù hợp số liệu. Nhưng L5 **“Fig. 5 = 12,488-row file”** khẳng định nguồn tạo figure mạnh hơn bằng chứng. | Giữ **“matches … to two decimals”**; bỏ kết luận chắc chắn về file đã dùng để vẽ. |
| §4.1: **“Level 1, a plain exact match”** | Có TF-IDF candidate nomination trước khi so equality; không phải quét exact-match thuần trên mọi cặp. | **“Level 1 applies normalized equality checks to TF-IDF-nominated candidate pairs.”** |
| §4.1: **“The TF-IDF step (`min_df=5`) cannot see very short questions”** | Không phải mọi câu ngắn đều zero-vector. | **“Questions with no retained TF-IDF features are never nominated; the surviving duplicate pair is such a case.”** |
| §4.2 heading: **“Format defects that inflate or distort scores”** | Tác động tăng/giảm điểm chưa được cô lập. Binary MCQ không tự nó là defect. | **“Question formats, extraction defects, and answer-position imbalance.”** |
| §4.2: **“1,240 two-option (true/false) items”** | Count chứng minh two-option; chưa có ledger phân loại tất cả là true/false hợp lệ. | **“1,240 two-option items, many presented as true/false questions.”** Nếu muốn “all”, cần taxonomy/count tương ứng. |
| §4.2: **“15 one-option items, placeholder options … and options merged during extraction”** | **15** và các loại defect thiếu ledger; sources khác nhau theo raw/baseline/clean. | **“The raw release contains 15 one-option rows; subsequent cleaning quarantines distinct structural and extraction defects.”** Thêm ledger raw count và từng stage; không đồng nhất 15 raw với 12 baseline `<2 options`. |
| §4.2: **“Options … break when the options are shuffled. This affects at least 80 items and the paper's shuffle-based ensemble.”** | Không phải mọi permutation đều đổi referents; chưa đo bao nhiêu shuffled instances thực sự đổi nghĩa. | **“At least 80 released rows contain position-referential options that can change meaning under shuffling; the impact on ensemble scores has not been quantified.”** |
| §4.3: **“This shows the labels do not separate items for these LLMs.”** | CI còn cho phép hiệu ứng dương đáng kể về thực dụng; chưa có equivalence test. | **“We do not find clear evidence that the labels separate accuracy for these seven LLM configurations on this test set.”** Giữ câu phân biệt clinicians. |
| §4.4: **“… a three-source verification … that started with the easiest disagreements.”** | Paper mô tả **ưu tiên** annotate, không cung cấp execution log chứng minh lịch sử thực tế. | **“The paper describes prioritizing easy questions on which source and model answers disagree.”** Bổ sung phần này vào L4. |
| §4.5: **“So the Δ in parentheses compares different things across rows.”** | Kết luận phù hợp, nhưng còn một reference không khớp và một Δ sai số học. | **“The reference mixes pass@1 and pass@3; Gemini is inconsistent across tables, and the Llama 4 delta is arithmetically incorrect.”** |
| §5: **“The authors' dedup reproduces exactly (10,956 rows).”** | Cùng count không chứng minh reproduction nguyên trạng hay đúng output lịch sử. | **“Our adapted implementation returns 10,956 rows, matching the stored reproduction report.”** |
| §5: **“Each stage has an expected-count guard and stops if its scope changes.”** | Có bằng chứng trong cleaning docs/code nhưng chưa có ledger. Guard kiểm tra count, không phát hiện mọi thay đổi scope cùng count. | **“Each stage checks its audited affected-row count and aborts on count mismatches.”** Thêm ledger/code location. |
| §5: **“Two bugs in our own pipeline were found and fixed, both documented.”** | “Two” thiếu ledger riêng. BUG-2 được giảm rủi ro bằng flag, chưa chữa khóa. | **“We documented post-repair duplicates and unresolved contradiction survivors; additional deduplication removes the former, while the latter remain flagged pending review.”** |
| §5: **“… so that no near-duplicate crosses splits”** | Group theo normalized stem chỉ bảo đảm equality theo khóa đó, không fuzzy/semantic near-duplicates. | **“… so that identical normalized stems do not cross splits.”** Tôi kiểm tra hiện tại: **0 normalized-stem groups** vượt split. |
| §5: **“Four test IDs were later removed as duplicates by stages 12/14.”** | Khớp report nhưng thiếu ledger riêng cho lịch sử split. | Giữ câu; thêm ledger manifest **1.662 → 1.658**, bốn ID và fate tương ứng. |
| §6: **“The paper's Fig. 6 prompt, zero-shot, greedy decoding, thinking off”** | L12 chỉ dẫn accuracy; chưa ledger protocol. Logs Llama/MedGemma có `think: null`, không phải bằng chứng độc lập đã tắt thinking. | **“We use the paper’s prompt with temperature-zero decoding and disable thinking where supported; model-specific configurations are documented.”** Dẫn harness và run metadata. |
| §6: **“… with always-A … and random … floors.”** | Đây là baselines, không phải lower bounds; model có thể thấp hơn. | **“… with always-A (29.8%) and uniform-random (27.6%) baselines.”** |
| §6: **“Results (pass@1, Wilson 95% CI): …”** | Chỉ Llama được trình bày CI trong câu, các model khác thiếu. | Đưa thành bảng đủ numerator/denominator và CI cho bảy model. |
| §6: **“… different questions and different configurations mean this is not a paired replication.”** | Hợp lý, nên giữ. Các số paper **48,73/58,05/51,15** chưa có ledger riêng. | Giữ câu; thêm ledger cho reference scores, version/model names và khác biệt cấu hình. |
| §6: **“Scoring every removed row … moves the overall estimate …”** | Cần nói rõ phần kept được ngoại suy từ test accuracy. | **“Combining removed-row scores with a test-based estimate for retained rows gives estimated raw-minus-clean differences of …”** Kèm CI của chênh lệch và giả định sampling. |
| §6: **“… score 29–33%, close to the random floor: these items cannot be answered as released.”** | Điểm gần random không chứng minh unanswerability. Hai model được chấm trên **70 removed contradiction rows**, không toàn bộ 152 contradiction rows. | **“On 70 removed rows from contradiction groups, the two models score 28.6% and 32.9%. Conflicting keys prevent a single content-consistent answer from satisfying all copies.”** Bổ sung ledger; tính random baseline riêng cho subset này. |
| §6: **“The paper's ‘weakest topics’ are not significantly below each model's overall score in our runs.”** | Chưa có paired test/multiplicity analysis. `SUMMARY.md` chỉ dùng CI upper bound so với overall, và còn có các topic được đánh dấu `below`. | **“Specialty differences remain exploratory pending dependence-aware comparisons and multiplicity correction.”** Không biến CI overlap thành kiểm định. |
| §7: **“… Vietnamese explanation, 320 questions”** | **320** thiếu trong L15. Các câu giải thích được mở rộng ngoài flagged union. | Giữ số, thêm L15 mô tả **320 unique error-free IDs** và cách hình thành tập. |
| §7: **“… refuses to answer 4 items (missing image, no correct option, missing context).”** | Đây là lý do model tự báo, chưa phải clinician-confirmed defects. | **“… abstains on four items, citing missing imagery/context or the absence of a correct option.”** |
| §7: **“Sampling design (pre-registered in … HUONG_DAN.md)”** | File local có kế hoạch trước review, nhưng chưa chứng minh registration/version bất biến; cỡ random còn chưa chốt. | **“A prospective review protocol is specified in …; the final sample size and protocol version must be frozen before annotation.”** |
| §7: **“A simple random stratum of [60 \| TBD] … Four disjoint priority strata … 36 double-reviewed questions … A blind round 1 … Endpoints E1 …”** | Các thông số và endpoint chưa có ledger. Nếu tăng random sample, manifest/36 có thể đổi. | Với artifact hiện tại: **60 random**, **178 tổng**, **36 double-review**; gọi là thiết kế pilot và thêm ledger cho manifest/protocol. |
| §7: **“… the ‘replacement-level fertility’ item, whose key is GRR = 1 where demographic convention gives NRR = 1”** | Không có ledger nguồn chuyên môn; log giải thích của model không đủ làm gold. | **“… a candidate key disagreement concerning replacement-level fertility, pending clinician review and a demographic reference.”** |
| §8: **“Scores on VM14K are robust in ranking but not interpretable by difficulty level.”** | Cả hai vế khái quát quá phạm vi. | **“The relative order of the two models assessed in the raw-versus-clean analysis is unchanged; difficulty labels show weak discrimination for the seven tested configurations.”** |
| §8: **“Scores near the top have a ceiling set by the share of erroneous keys”** | Không có ceiling chung đơn giản bằng `1−error rate`: model có thể khớp khóa sai, và lỗi có thể phụ thuộc model. | **“Erroneous keys may distort measured accuracy; we will quantify their effect by rescoring fixed predictions after adjudication.”** |
| §8: **“The review covers a sample; every rate is restricted to the 1,658 evaluated test questions.”** | “Every rate” mâu thuẫn duplicate/difficulty-consistency rates trên raw release. | **“Clinician-review prevalence estimates concern only the 1,658 evaluated test questions; structural audit rates use their explicitly stated raw or clean populations.”** |
| §8: **“Model flags share training data and errors”** | Có thể có shared data/error, nhưng training overlap của các model chưa được xác minh. | **“Model flags may reflect correlated training data or errors; agreement is not independent clinical validation.”** |

Một điểm cần sửa xuyên suốt: **“same item” phải phân biệt equality sau chuẩn hóa với cùng nghĩa y khoa.** Normalizer bỏ dấu và ký hiệu; số count khớp không đủ bảo đảm mọi collision là duplicate hợp lệ. Nên kiểm tra thủ công toàn bộ 67 contradiction groups hoặc ít nhất báo độ chính xác của detector trên mẫu được chọn có thiết kế.

## 3. Ba phản đối mạnh nhất của một reviewer ACL và cách tăng điểm

**Phản đối 1 — Đóng góp hiện tại chủ yếu là sửa một artifact, chưa có kết quả trung tâm đủ mạnh.**

Duplicates, provenance thiếu và lỗi extraction hữu ích, nhưng chưa cho thấy chúng thay đổi kết luận khoa học nào. Kết quả raw-vs-clean chỉ đổi khoảng 0,1–0,2 pp ở hai model; clinician review vẫn TBD. Reviewer có thể hỏi: *sau audit, điều gì về đánh giá medical LLM thay đổi?*

**Cách tăng điểm mạnh nhất:** hoàn tất adjudication và **rescore cùng predictions trước/sau sửa key**. Báo paired score differences, CI, rank uncertainty và loại lỗi tạo tác động. Nếu aggregate score ổn định nhưng một phân tích specialty/difficulty sai lệch, đó vẫn là kết quả tốt khi chứng minh rõ.

**Phản đối 2 — Các phát biểu validity mạnh hơn thiết kế thống kê.**

Random sample hiện tại 60 câu chỉ là pilot; inference chỉ tới test đã được làm sạch và loại pending contradictions. Không phát hiện difficulty effect không chứng minh equivalence. Đồng thuận model có thể chỉ tìm lỗi mà cùng một họ model dễ phát hiện. Sự khác biệt trước/sau reveal không tách được tác động explanation, key, votes và suy nghĩ lại.

**Cách tăng điểm:** tăng random stratum trước khi review, theo mục tiêu precision; đóng băng protocol/manifest; tăng review độc lập có adjudication theo chuyên khoa. So sánh yield của flags với random, kèm chi phí reviewer. Không báo recall nếu chưa review đủ phần không flagged.

Baseline flagging nên gồm:

- một model không đồng ý key;
- hai model cùng chọn một non-key answer;
- vote của bảy model;
- heuristic structural defects.

Như vậy paper trả lời được *chiến lược nào dùng thời gian bác sĩ hiệu quả*, thay vì chỉ thu thập ví dụ.

**Phản đối 3 — Re-evaluation chưa cô lập được nguyên nhân và chưa tạo phương pháp khái quát.**

Đổi model generation, provider/configuration, subset, cleaning và key cùng lúc làm comparison với paper gốc khó diễn giải. Exact normalized-stem grouping cũng chưa chứng minh không có semantic leakage. Count guards chứng minh pipeline khớp các trường hợp đã audit, chưa chứng minh cleaning tổng quát.

**Cách tăng điểm:** dùng thiết kế trên cùng items/predictions, phân rã:

1. raw → dedup;
2. loại format defects;
3. text repairs;
4. adjudicated keys.

Thêm thí nghiệm shuffle trên position-referential items: giữ nguyên thứ tự, shuffle không sửa references, và shuffle có bảo toàn references. Đây là một kết quả phương pháp có thể chuyển sang benchmark khác. Một benchmark thứ hai hoặc validation ngoài tập VM14K sẽ tăng sức thuyết phục hơn việc chỉ thêm nhiều model mới.

**Venue:** với framing và bằng chứng hiện tại, **workshop thực tế hơn; Findings khả thi hơn sau khi hoàn tất review và analysis**. Main conference vẫn có thể phù hợp cho resource/audit paper, không bắt buộc có model mới. Nhưng “audit + clinician key review” chỉ đủ khi quy mô, độ tin cậy và kết quả sau sửa đủ mạnh để tạo hiểu biết vượt khỏi một bản phát hành lỗi.

Tôi sẽ ưu tiên **analysis sau adjudication**, rồi **baseline cho hiệu quả flagging**, rồi **framing**. Đổi tiêu đề hoặc tăng số model không thay thế được hai phần đầu.

## 4. Related work: thiếu gì và citation nào cần sửa

Các câu ở §2 đều chưa có ledger riêng, dù draft tuyên bố “every number” đã được liệt kê.

| Câu trích trong §2 | Đối chiếu và sửa |
|---|---|
| **“Studies of test sets in general find pervasive label errors (Northcutt et al., 2021).”** | Hướng đúng nhưng “in general” quá rộng. Viết rằng nghiên cứu phát hiện lỗi nhãn trong các test sets được khảo sát, không mọi test set. Phân biệt paper *Pervasive Label Errors…* với paper *Confident Learning*, vì tác giả khác. [Northcutt, Athalye & Mueller](https://arxiv.org/abs/2103.14749). |
| **“MMLU-Redux (Gema et al., NAACL 2025) estimates that 6.49% … with 57% in Virology.”** | **Venue/year/numbers khớp.** Nhưng 57% là các câu Virology **được phân tích**, không kiểm tra toàn bộ Virology. Tên paper là *Are We Done with MMLU?*. Thêm ledger và nêu sampling scope. [NAACL 2025](https://aclanthology.org/2025.naacl-long.262/). |
| **“Platinum benchmarks (Vendrow et al.) re-curate 15 benchmarks to remove label noise.”** | **15 khớp**, thiếu năm; mục tiêu còn gồm ambiguity, không bảo đảm noise-free. Viết “revise examples from fifteen benchmarks to minimize label errors and ambiguity.” Dùng phiên bản/title cụ thể. [Vendrow et al., 2025](https://arxiv.org/abs/2502.03461). |
| **“Nahum et al. (2024) use LLM ensembles to flag label errors for expert review.”** | **2024 đúng nếu dẫn preprint**. Có bản hội nghị **EMNLP 2025**; nên dùng citation hội nghị hoặc ghi rõ version. [EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1360/). |
| **“We adopt their flag-then-review idea, but add a random stratum so that the error rate can be estimated.”** | Mô tả thiết kế được hỗ trợ bởi protocol; **không đủ chứng minh novelty** của random stratum. Viết “We combine model-guided review with a simple random sample for prevalence estimation.” |
| **“IgakuQA (Kasai et al., 2023) shows that LLMs pick options that are prohibited in Japanese practice.”** | **Khớp**, nhưng nên viết “sometimes select prohibited choices” và nêu các model được khảo sát. [Kasai et al., 2023](https://arxiv.org/abs/2303.18027). |
| **“AfriMed-QA and WorldMedQA-V document regional gaps in knowledge.”** | Quá gộp. **AfriMed-QA là benchmark tiếng Anh trong bối cảnh châu Phi**, không phải ví dụ non-English. WorldMedQA-V còn có modality/image effects và native/translated evaluation; không quy mọi gap thành “knowledge”. Tách hai vai trò. [AfriMed-QA](https://arxiv.org/abs/2411.15640), [WorldMedQA-V](https://arxiv.org/abs/2410.12722). |
| **“VietMed-MCQ (2026) builds Vietnamese MCQs with retrieval-augmented generation and reports that general-purpose models beat Vietnamese-centric ones.”** | **Năm và RAG khớp**, nhưng bỏ sót scope quan trọng: **Vietnamese Traditional Medicine**, không medical QA nói chung. Kết quả liên quan các general models có strong Chinese priors trong tập model khảo sát. [VietMed-MCQ](https://arxiv.org/abs/2601.03792). |
| **“Easy2Hard-Bench and recent probing work compare labelled difficulty with difficulty measured on models.”** | “Recent probing work” không định danh được. Easy2Hard-Bench xây numerical difficulty từ human/model performance bằng IRT/Glicko-2; câu hiện tại làm mờ đóng góp thực tế. Dẫn tác giả/năm và mô tả đúng, hoặc bỏ phần probing cho tới khi có citation. [Easy2Hard-Bench](https://arxiv.org/abs/2409.18433). |

Các bổ sung quan trọng nhất:

- **Construct validity của medical QA:** *Questioning Our Questions* đặt trực tiếp câu hỏi MCQ benchmark có phản ánh clinical capability không. Đây là related work sát framing hơn chỉ liệt kê dataset. Dùng để giới hạn kết luận của VM14K ở exam-style QA. [Kim & Yoon, BioNLP 2025](https://aclanthology.org/2025.bionlp-1.24/).
- **Option-position robustness:** *Large Language Models Are Not Robust Multiple Choice Selectors* là nền trực tiếp cho position/shuffle analysis. Phân biệt bias của model với việc permutation phá nghĩa của item; phần thứ hai có thể là đóng góp riêng của paper này. [Zheng et al.](https://arxiv.org/abs/2309.03882).
- **Dedup và train–test overlap:** Lee et al. giúp đặt split hygiene vào nghiên cứu đã có, đồng thời tránh gọi exact-stem grouping là semantic leakage prevention. [ACL 2022](https://aclanthology.org/2022.acl-long.577/).
- **Expert-grounded multilingual QA:** MedExpQA có gold explanations do bác sĩ viết, rất sát review/evidence protocol của bài. [Alonso et al., 2024](https://arxiv.org/abs/2404.05590).
- **Nguồn non-English lâu đời:** HEAD-QA và CMB cần có nếu §2 muốn đại diện lĩnh vực, thay vì chỉ Nhật/châu Phi/Vietnam. [HEAD-QA, ACL 2019](https://aclanthology.org/P19-1092/), [CMB](https://arxiv.org/abs/2308.08833).
- **Provenance và phạm vi suy rộng:** Data Statements hỗ trợ yêu cầu ghi nguồn, annotators, population và giới hạn sử dụng của cleaned release. [Bender & Friedman, TACL 2018](https://aclanthology.org/Q18-1041/).

## 5. Danh sách sửa theo ưu tiên

1. **Sửa ngay các khẳng định quá mức:** “never”, “do not discriminate”, “ranking robust”, “cannot be answered”, “no near-duplicate”, và ceiling từ erroneous keys. Giới hạn kết luận theo raw release, cleaned test và từng tập model.
2. **Hoàn tất clinician review trước khi viết kết quả:** chốt random sample đủ precision, đóng băng protocol/version, review độc lập và adjudication có nguồn. Chưa có kết quả thì abstract không được viết “finds”.
3. **Rescore predictions cố định sau sửa key**, với paired CI và rank uncertainty. Đây là phần có khả năng tăng điểm nhiều nhất.
4. **Sửa L16b đủ 17 dòng:** thêm ngoại lệ Gemini, Huatuo pass@1, lỗi Δ Llama 4 và tên model Llama ở Table 3.
5. **Hoàn thiện ledger:** sửa đường dẫn L11; thêm protocol, raw one-option count, 320 explanation IDs, subset 70 contradiction rows, split history và toàn bộ số/citation §2.
6. **Kiểm tra detector và cleaning:** validation các collision sau normalization; danh sách ID/lệnh cho ≥80 position-reference rows; tách structural cleaning khỏi clinical validation.
7. **Thêm baseline flagging và thí nghiệm shuffle có bảo toàn nghĩa**, rồi viết lại framing quanh kết quả đã chứng minh. Nếu hiệu ứng vẫn nhỏ và chỉ một dataset, đặt mục tiêu Findings/workshop với claim vừa đủ.
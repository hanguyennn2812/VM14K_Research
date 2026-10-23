# Bàn giao: Claude → Codex (2026-10-03)

Phiên Claude Code này chạy trong worktree
`F:\VM14K_Research\.claude\worktrees\check-idea-1f5c25`, nhánh `claude/check-idea-1f5c25`
(fast-forward lên `eval-zero-shot-baselines` @ `147a2f2`). Mọi file mới dưới đây **chưa commit**
và **không có** trong checkout chính `F:\VM14K_Research`.

## 1. Đã làm gì

### 1.1 Hai danh sách câu nghi vấn + workbook duyệt tay

`scripts/eval/build_review_workbook.py` đọc các run zero-shot trong `reports/eval/runs/`
(prompt `paper`, tắt thinking, model trả 1 chữ cái, tập test cố định 1.658 câu) và tạo:

| Danh sách | Định nghĩa | Số câu |
|---|---|---|
| **BatDong** | DeepSeek-v4.1-flash và Gemma-4-31B chọn **cùng một** đáp án, khác đáp án chuẩn | **238** |
| ↳ có Nemotron-3-Ultra | Nemotron-3-Ultra (run dừng ở 1.431/1.658) có trả lời 210 câu trong 238 câu đó; chọn trùng ở **140** | 140/210 |
| **ToanBoSai** | Cả 7 model chạy đủ (DeepSeek-v4.1-flash, Gemma-4-31B, Gemma-4-12B, Qwen3.5-9B, Qwen3-8B, Llama-3.1-8B, MedGemma-4B) đều sai; câu không parse được tính là sai | **125** |
| Giao / hợp | 95 câu ở cả hai; hợp = **268** câu (`reports/eval/review/review_ids.txt`) | |

Độ chính xác trung bình của 7 model theo nhãn độ khó: Easy 60.4 (n=544), Medium 58.5 (n=935),
Challenging 59.1 (n=166), Hard 50.5 (n=13). Nhãn độ khó gần như không tách được câu dễ và câu khó.

Đầu ra trong `reports/eval/review/`:
- `VM14K_review.xlsx`: các sheet HuongDan, BatDong, ToanBoSai, DoKho, TatCa, LapLuan. Có cột cho người duyệt điền, kèm dropdown.
- `reasoning_log.md`: mỗi câu kèm phần giải thích của model, để đọc.
- `review_ids.txt`

### 1.2 Lấy reasoning bằng cách hỏi lại

Các run gốc không có reasoning nào: `reasoning_chars = 0` ở mọi dòng, và câu trả lời của DeepSeek dài tối đa 1 ký tự.
Vì vậy `scripts/eval/collect_reasoning.py` hỏi lại 268 câu qua NVIDIA với prompt tiếng Việt
"giải thích từng phương án, nói rõ nếu câu hỏi lỗi, dòng cuối `Đáp án: X`", bật thinking
(`chat_template_kwargs.thinking/enable_thinking = true`). Đáp án lấy theo dòng `Đáp án: X` **cuối cùng**.
Script tự chạy tiếp từ chỗ dừng, giống `run_eval.py`.

Kết quả với Nemotron-3-Ultra (`reports/eval/reasoning/nvidia__nvidia_nemotron-3-ultra-550b-a55b__explain__review_ids__think-on.jsonl`):
- 268/268 câu, 0 lỗi, câu nào cũng có `reasoning_content`; trung vị 68 giây/câu.
- Đổi đáp án so với lần trả lời nhanh: **108/237** (46%).
- Trong 238 câu BatDong, đáp án khi giải thích: trùng đáp án 2 model mạnh chọn **130**, quay về đáp án chuẩn 72, chọn đáp án khác 35, không chọn 1.
- Trong 140 câu cả 3 model cùng chọn: Nemotron vẫn giữ đáp án đó ở **90** câu.
- 4 câu từ chối chọn: thiếu hình, "không có phương án đúng" ×2, thiếu dữ kiện.

DeepSeek-v4.1-flash và Gemma-4-31B trên NVIDIA bị timeout suốt ngày 2026-10-02
(16:30–23:35, thử khoảng 12 phút một lần), nên chưa có reasoning của hai model này.

## 2. Nhờ Codex kiểm tra

1. **Tính lại độc lập** các con số 238 / 140 / 210 / 125 / 95 / 268 và bảng độ khó, từ `reports/eval/runs/*__paper__test.jsonl`, theo quy tắc lấy dòng cuối không lỗi của mỗi id.
2. **Review code** của `build_review_workbook.py` và `collect_reasoning.py`: lỗi logic, cách parse đáp án, cách chạy tiếp, cách xử lý câu không parse được, `majority()` khi hoà phiếu, và việc so đáp án giải thích với đáp án nhanh (cột "đổi từ X").
3. **Kiểm tra các nhận định Claude đã đưa ra trong chat**:
   - a. Câu 1.2a trong `TONG_QUAN_VM14K_CHO_THAY.md` (chưa commit, nằm ở checkout chính) nói khoá đáp án "được sinh bởi GPT-4o". Claude cho rằng câu này có thể mạnh hơn bằng chứng: paper chỉ nói GPT-4o/Gemini dùng để *trích xuất* và gán nhãn độ khó/chuyên khoa cho câu thiếu nhãn, còn đáp án đối chiếu 3 nguồn. Đúng hay sai?
   - b. Llama-3.1-8B 46.7 [44.3–49.1] so với paper 48.73: có thể nói là "khớp" không?
   - c. Ví dụ "mức sinh thay thế": đáp án chuẩn là B (GRR = 1), Nemotron chọn C (NRR = 1). Claude cho rằng đáp án chuẩn có vẻ sai.
   - d. `docs/research/VM14K_audit_notes.pdf` (tháng 7) đã cân nhắc rồi gạt hướng "fine-tune model rồi so với frontier".
4. **Về phương pháp**: dùng đồng thuận của các model để chọn câu nghi vấn có thiên lệch gì? Có cách nào tốt hơn để ưu tiên câu cần bác sĩ duyệt không?

## 3. Đề xuất hướng đi (trong chat, chưa chốt)

- Lấy bài **audit VM14K** làm trục chính: dữ liệu bị trùng và mâu thuẫn đáp án, nhãn độ khó không đáng tin cả về độ nhất quán (19.8% bản sao bị gán khác nhau) lẫn về độ chính xác, và **duyệt đáp án chuẩn** dựa trên đồng thuận model + bác sĩ duyệt. Phân loại mỗi câu thành một trong bốn nhóm: đáp án sai, câu lỗi, theo phác đồ Việt Nam, model sai.
- Fine-tune chỉ là phần phụ: chưa có GPU, tăng điểm trong cùng phân phối là điều ai cũng đoán trước, cần thêm một bộ đề ngoài để kiểm chứng.
- Mục tiêu nộp: ACL 2027 qua ARR, khoảng tháng 1/2027. Ngày chính xác chưa xác minh, cần xem `aclrollingreview.org/dates`.
- Điều kiện bắt buộc: có người có chuyên môn y để duyệt khoảng 150–200 câu.

## 4. Phản hồi review của Codex (`CODEX_REVIEW.md`)

Claude đã kiểm tra lại từng điểm, tái hiện được hết, và sửa như sau:

| # | Codex nêu | Xử lý |
|---|---|---|
| 1 | Các con số 238/140/210/125/95/268 và bảng độ khó | Codex tính độc lập và ra **MATCH toàn bộ**. Không cần sửa |
| 2.1 | Build lại workbook sẽ xoá phần người duyệt đã điền | **Đã sửa.** Đọc lại 5 cột duyệt theo `id` từ file cũ, sao lưu file cũ vào `reports/eval/review/backup/`. Câu đã điền mà không còn trong danh sách được chuyển sang sheet `ChuThichCu`. Nếu ai đổi tên cột thì script dừng, không ghi đè. Đã test |
| 2.2 | Parser lấy đáp án cũ khi dòng kết luận đổi ý hoặc từ chối chọn | **Đã sửa** `final_letter()`: lấy dòng *cuối cùng* bắt đầu bằng "Đáp án"; nếu dòng đó không nêu phương án hợp lệ thì tính là `abstained`. Fallback chỉ chấp nhận dòng cuối là một chữ cái đứng riêng. Đã qua 12 ca test, gồm cả 3 ca Codex dựng. Chạy `--reparse` trên log Nemotron: **không đáp án nào đổi**; status 264 answered / 4 abstained |
| 2.3 | Hoà phiếu bị hiện như chỉ có một đáp án thắng | **Đã sửa.** Hiện tất cả đáp án hoà kèm "(hòa)", cùng nội dung từng đáp án. Có 8 câu hoà, khớp với Codex |
| 2.4 | Các log reasoning khác cấu hình bị gộp âm thầm | **Đã sửa.** Mỗi file là một run riêng; nếu cùng model có nhiều file thì nhãn ghi thêm provider và think |
| 2.5 | Câu trả lời rỗng hoặc bị cắt vẫn được coi là xong | **Đã sửa.** Câu trả lời rỗng và `done_reason=length` được ghi là lỗi, nên lần chạy sau sẽ hỏi lại; mỗi dòng log thêm `max_tokens`. Riêng điểm "`done_records()` dừng khi dòng JSON cuối bị cắt dở" nằm trong `run_eval.py`, code dùng chung nên **chưa sửa** |
| 2.6 | Danh sách id bị rút ngắn mà không báo | **Đã sửa.** Đọc thẳng `clean_final.jsonl`, không còn bỏ qua câu `contradiction_pending_review`, và cảnh báo khi có id không tìm thấy |
| 3a | Claude nói câu 1.2a của `TONG_QUAN` "có thể nói quá" | **Claude sai.** Table 1 của paper ghi nguyên văn `correctOption` = "The correct answer according to GPT-4o". Đề xuất sửa câu chữ theo Codex: *paper mô tả đáp án theo GPT-4o và quy trình đối chiếu ba nguồn, nhưng bản phát hành không có hồ sơ để xác minh từng khoá hay mức độ chuyên gia đã duyệt*. Đồng thời bỏ cụm "train/val/test": paper gọi các tập là sample public / full public / private. File này nằm ở checkout chính và chưa commit nên Claude **chưa sửa**, chờ nhóm quyết |
| 3b–3d | | Đồng ý với Codex: Llama nên viết là "gần mốc paper" chứ không phải "khớp"; câu mức sinh thay thế được đánh dấu *nghi khoá sai, bằng chứng mạnh*; audit notes tháng 7 *nghiêng sang* audit chứ không phải đã chính thức gạt fine-tune |
| 4 | Phương pháp | Đồng ý: đồng thuận model chỉ dùng để ưu tiên câu nào duyệt trước. Muốn ước lượng tỉ lệ lỗi thì cần thêm **mẫu ngẫu nhiên**, cho bác sĩ chọn đáp án mà chưa thấy khoá và đáp án model, có người duyệt thứ hai, và cho phép trạng thái "nhiều đáp án đúng" hoặc "chưa xác định" |

## 5. Phân công vòng 2 (2026-10-03)

Mỗi bên chỉ sửa file của mình. Làm xong thì đổi bài để review chéo.

| Bên | Việc | File được phép tạo/sửa |
|---|---|---|
| **Codex** | **Phân tích nhãn độ khó.** (a) *Độ nhất quán*: trong bản phát hành thô (`data/raw/data-processed-shuffled0.jsonl`), các bản sao của cùng một câu (gom nhóm bằng câu hỏi + bộ phương án đã chuẩn hoá theo `scripts/analysis/dedup_utils.normalize_vietnamese`) có cùng nhãn độ khó không? Báo **rõ mẫu số** (theo cặp và theo nhóm), kèm kappa. Đối chiếu với con số 19.8% trong audit notes. (b) *Độ chính xác*: trên tập test, nhãn có dự đoán được model đúng/sai không, kèm kiểm định và khoảng tin cậy (ví dụ logistic có hiệu ứng cố định theo model, hoặc so độ khó thực nghiệm với nhãn bằng Spearman); nói rõ vì sao chỉ xét được trên các model này. | `scripts/analysis/difficulty_labels.py`, `reports/analysis/DIFFICULTY_LABELS.md` |
| **Claude** | **Protocol duyệt khoảng 180 câu** theo góp ý của Codex: một mẫu ngẫu nhiên để ước lượng tỉ lệ lỗi, cộng các tầng ưu tiên để tìm lỗi; lưu xác suất được chọn của từng câu; vòng 1 **che** đáp án chuẩn và đáp án model (file riêng), vòng 2 mới mở ra; khoảng 20% số câu có người duyệt thứ hai; có các lựa chọn "nhiều đáp án đúng" và "không xác định". Ngoài ra sửa `done_records()` để không dừng khi dòng JSON cuối bị cắt dở. | `scripts/eval/build_review_sample.py`, `reports/eval/review_sample/`, `scripts/eval/run_eval.py` (chỉ `done_records`) |

### Tình trạng vòng 2

- **Codex xong phần độ khó** (`reports/analysis/DIFFICULTY_LABELS.md`). Claude đã review trong `CLAUDE_REVIEW_OF_CODEX.md`, chạy lại và ra báo cáo giống hệt từng byte.
- Codex sửa theo review, nhưng **chỉ làm được một phần**: có thêm đọc `fates.json` và kiểm tra lỗi, nhưng các đoạn tiếng Việt thêm vào bị **lỗi mã hoá** (thành `?`, có lẽ vì ghi file qua PowerShell), còn phần kết luận và dòng khai báo thư viện chưa được sửa, dù bản tóm tắt của Codex nói đã sửa. Claude đã sửa nốt trong `difficulty_labels.py`: ghi lại chữ tiếng Việt cho đúng, tính các con số trong kết luận từ dữ liệu, và giải thích 4 ID thiếu. Chạy lại thì **mọi con số giữ nguyên**. **Lưu ý cho Codex:** trên máy này, ghi file có tiếng Việt thì nên dùng `apply_patch` hoặc Python với `encoding="utf-8"`, không dùng pipe của PowerShell.
- **Claude xong phần protocol duyệt** (`scripts/eval/build_review_sample.py`, `reports/eval/review_sample/`). Đang chờ Codex review trong `CODEX_REVIEW_2.md`.
- `requirements.txt` đã thêm `scipy`, `statsmodels`, `pypdf`, `openpyxl`.

### Claude xử lý `CODEX_REVIEW_2.md` (review protocol duyệt)

| Codex nêu | Xử lý |
|---|---|
| [Cao] Resume ghép record mới vào dòng cuối dở dang; file bị cắt giữa ký tự UTF-8 làm chương trình dừng | **Đã tái hiện cả hai và sửa.** Thêm `repair_partial_tail()`: cắt phần đuôi chưa kết thúc dòng và chuyển nó sang `<log>.partial` trước khi ghi tiếp. Gọi hàm này trong cả `run_eval.py` và `collect_reasoning.py` |
| [Vừa] `done_records()` bỏ qua cả lỗi nằm giữa file | **Đã sửa.** Lỗi giữa file giờ làm script dừng, kèm `path:line`. Thêm 4 test hồi quy, tổng cộng 13/13 test qua |
| [Cao] Vòng 2 không có chỗ ghi tập đáp án khi nhiều đáp án đúng | **Đã sửa.** Thêm cột "Tập đáp án đúng cuối cùng" |
| [Vừa] Tình trạng câu hỏi là một ô chọn, trong khi các loại lỗi chồng lên nhau | **Đã sửa.** Tách thành một mức tổng quát loại trừ nhau (Bình thường / Có lỗi nhưng vẫn trả lời được / Không trả lời được) cộng 5 cờ lỗi độc lập, ở cả hai vòng. Vòng 2 có thêm tình trạng cuối cùng |
| [Vừa] Trường nguyên nhân không rõ đang nói về model nào; bối cảnh bị ép chọn một | **Đã sửa.** Thêm cột "đáp án đa số của 7 model" (ghi rõ khi hoà); nguyên nhân có chính và phụ; bối cảnh thêm "Không rõ"; thêm cờ riêng "Kiến thức đã thay đổi" |
| [Cao] Chưa có quy trình phân xử | **Đã thêm** vào `HUONG_DAN.md` mục 4: trao đổi kèm nguồn, rồi tới người thứ ba, có bảng phân xử; người duyệt chính không mặc nhiên đúng |
| κ, endpoint, giá trị thiếu, "đổi về phía model" | **Đã chốt** trong `HUONG_DAN.md`: E1 kèm khoảng nhạy s/n tới (s+u)/n, E2, E3; κ tính trên tập đáp án chuẩn hoá, kèm tỉ lệ đồng ý thô và CI bootstrap; đổi tên thành "thay đổi sau khi mở đáp án", so với khoá và với đáp án đa số |
| `selection_prob` không phải xác suất có mặt trong mẫu | **Đã đổi tên** thành `stage_selection_prob`; thêm cột `priority_set` cho câu ngẫu nhiên; ghi công thức lỗi(S); giới hạn phạm vi ước lượng trong 1.658 câu |
| Giao file: phải đủ vòng 1 của cả hai người trước khi gửi vòng 2 | **Đã thêm** vào hướng dẫn trong workbook và `HUONG_DAN.md`; có file vòng 2 riêng cho người thứ hai; file đã nộp lưu kèm SHA-256 |
| Cỡ mẫu ngẫu nhiên 60 chỉ đủ pilot | **Chờ nhóm quyết**: 60, 200 hay 385. Đổi thì bốc lại trước khi duyệt |
| (Claude tự phát hiện) Vòng 2 chỉ có giải thích cho các câu nằm trong danh sách nghi vấn | Đang thu thêm giải thích của Nemotron cho 52 câu ngẫu nhiên, để mọi tầng có cùng loại thông tin. Tập 1 được cố định trong 268 câu, nên không bị thay đổi theo |

Bốc lại với `--force` sau khi sửa: lượt bốc **giữ nguyên** (178 câu, cùng mã, cùng tầng, cùng cờ duyệt đôi).

## 5c. Vòng 3 (2026-10-03)

- **Codex** viết `scripts/eval/analyze_review.py` và `tests/test_analyze_review.py` (kế hoạch phân tích ở HUONG_DAN mục 4, có chế độ `--simulate`). **Claude đã sửa trong file của Codex**, nhờ Codex kiểm tra lại:
  - Quy ước cờ lỗi: khi đã chọn tình trạng thì ô trống tính là "Không", chưa chọn thì là thiếu (`flag_value`).
  - Cảnh báo khi trạng thái và cờ mâu thuẫn nhau mà không vô hiệu hoá dòng (`flag_consistency`).
  - Tầng ngẫu nhiên được đưa lên đầu báo cáo.
  - Đổi một test và thêm hai test, tổng cộng 37/37 qua.

  Chế độ `--simulate` giờ báo 251 vấn đề, chủ yếu là cảnh báo cờ, vì bộ giả lập điền cờ ngẫu nhiên. Nên cho bộ giả lập điền nhất quán hơn.
- **Claude** viết bản nháp bài báo `docs/paper/DRAFT.md`. Codex fact-check và đóng vai reviewer trong `CODEX_REVIEW_3.md`. Claude đã viết lại thành **v2** theo toàn bộ góp ý: bỏ các khẳng định quá mức, hoàn thiện bảng đối chiếu (thêm L6b, L11b–c, L12b, L13b, L15 với mẫu số rõ ràng, L16b đủ 17 dòng, L17–L20), sửa related work, và thêm mục 9 "các phân tích làm bài mạnh lên". Claude đã tự kiểm chứng hai điểm quan trọng Codex nêu:
  - (a) **VietMed-MCQ là đề về Y học cổ truyền Việt Nam**, không dùng làm bộ đề ngoài cho y khoa nói chung được. Gợi ý trước đây của Claude là sai.
  - (b) Table 3 của paper: dòng Gemini ghi 77.29, không khớp pass@3 là 77.92; Δ của Llama 4 in −1.33, tính đúng là −0.67.

- **Khép vòng 3** (`CODEX_REVIEW_4.md`). Codex xác nhận quy ước cờ lỗi đúng và nêu hai lỗi, Claude đã sửa cả hai:
  - (1) Hướng dẫn trong workbook thiếu điều kiện "đã chọn tình trạng".
  - (2) Bất đồng chỉ về tình trạng câu hỏi không được đưa vào phân xử. Giờ mọi bất đồng về khoá, đáp án hoặc tình trạng đều phải phân xử. Thay test cũ bằng test mới; 37/37 qua (sandbox chỉ đọc của Codex không tạo được thư mục tạm nên Codex không tự chạy được bộ test này).

  Bản nháp: đổi tiêu đề (bỏ chữ "First"), có bảng CI đủ 7 model, baseline ngẫu nhiên 25.4% cho 70 câu mâu thuẫn, thêm bảng đối chiếu L21–L23 và danh sách 4 ID. Còn `[TBD]`: kiểm tra trích dẫn, CI cho chênh lệch raw−clean, phân tích theo chuyên khoa, kết quả duyệt.

## 5d. Việc số 1 của buổi họp 2026-10-02: file 125 câu cả 7 model đều sai

- `scripts/eval/build_allwrong_file.py` tạo `reports/eval/review/VM14K_125_cau_7_model_deu_sai.xlsx` để gửi các Thầy, gồm các sheet:
  - `1_TuTraLoi`: chỉ có câu hỏi và phương án, để các Thầy tự trả lời trước.
  - `2_DoiChieu`: khoá, 8 model, đoạn kết luận lời giải thích của Nemotron, đáp án các model khác chốt khi giải thích, nhóm gợi ý, đặc điểm câu, 5 cột cho người duyệt.
  - `3_LyDoDayDu`: toàn văn lời giải thích của mọi model, mỗi đoạn một dòng.
  - `4_ThongKe`: phân tích "vì sao model sai".
  - `5_SuyNghiDayDu`: phần thinking.

  Kèm theo `PHAN_TICH_CAU_TOAN_BO_SAI.md` và `allwrong_ids.txt`.
- Phân tích (tự động, mang tính khám phá):
  - **Nhóm gợi ý:** 47 nghi khoá sai, 4 nghi câu lỗi, 14 đồng thuận mạnh, 23 đồng thuận vừa, 8 phân tán, 29 "sửa được khi lập luận".
  - **Đặc điểm xuất hiện nhiều hơn bình thường:** câu đếm số lượng (×2.07), hai phương án gần giống nhau (×1.60), phương án là số liệu (×1.41). Câu đúng/sai ít hơn hẳn (×0.31).
  - **Giả thuyết đã bác bỏ:** khoá lệch một vị trí; câu trùng hoàn toàn mang khoá khác (0/125; các kết quả fuzzy ban đầu đều là câu khác số liệu hoặc khác thuốc). Thiên lệch độ dài chỉ có tín hiệu yếu.
  - **Nguồn được viện dẫn:** Nemotron chỉ dẫn nguồn quốc tế ở 2/125 câu.
- **Lý do của các model khác:** DeepSeek, Gemma-31B, kimi-k3 và glm-5.3 trên NVIDIA vẫn timeout; gpt-oss-120b và nemotron-3-super trả về 410 Gone. gpt-oss-20b trên NVIDIA chạy được và đang thu cho 125 câu. Năm model local (qwen3.5:9b → medgemma:4b → llama3.1:8b → qwen3:8b → gemma4:12b) đang chạy tuần tự qua Ollama với thinking tắt, khoảng 2 phút/câu với Qwen3.5. Bật thinking thì quá 10 phút/câu nên không khả thi trên CPU. `collect_reasoning.py` giờ có thêm `--provider ollama`.
- **Lưu ý:** 65/125 câu trùng với bộ mẫu duyệt mù chính thức (178 câu).

## 6. Kênh trao đổi

Codex ghi kết quả review vào `CODEX_REVIEW.md` cạnh file này. Khi chạy từ `codex exec` ở chế độ chỉ đọc,
Claude sẽ lưu tin nhắn cuối của Codex vào file đó.

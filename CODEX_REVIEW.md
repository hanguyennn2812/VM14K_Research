## 1. Tính lại độc lập số liệu

**Cả sáu số đếm và bảng độ khó đều MATCH.** Tôi chạy Python riêng chỉ dùng thư viện chuẩn, không import các script đang review: đọc từng JSONL theo thứ tự file, giữ record cuối có `error is None` cho mỗi `id`, rồi tự so `pred` với đáp án trong `clean_final.jsonl`.

| Chỉ tiêu | HANDOFF | Giá trị tôi tính | Kết quả |
|---|---:|---:|---|
| `BatDong` | 238 | 238 | MATCH |
| Nemotron chọn cùng đáp án của hai model trong `BatDong` | 140 | 140 | MATCH |
| Nemotron có record không lỗi trong `BatDong` | 210 | 210 | MATCH |
| `ToanBoSai` | 125 | 125 | MATCH |
| Giao hai danh sách | 95 | 95 | MATCH |
| Hợp hai danh sách | 268 | 268 | MATCH |

Bảy run đầy đủ đều chứa đúng cùng 1.658 ID. Không có lệch `gold` so với dữ liệu sạch, hoặc lệch giữa trường `correct` và phép so `pred == gold`. `review_ids.txt` đúng bằng hợp hai danh sách.

Độ chính xác (%), làm tròn một chữ số:

| Model | Easy | Medium | Challenging | Hard |
|---|---:|---:|---:|---:|
| DeepSeek-v4.1-flash | 72.8 | 70.4 | 72.3 | 69.2 |
| Gemma-4-31B | 72.1 | 72.0 | 69.3 | 61.5 |
| Nemotron-3-Ultra | 63.9 | 68.1 | 67.6 | 60.0 |
| Gemma-4-12B | 60.7 | 59.3 | 61.4 | 53.8 |
| Qwen3.5-9B | 62.3 | 63.9 | 60.8 | 53.8 |
| Qwen3-8B | 56.2 | 53.4 | 54.2 | 69.2 |
| Llama-3.1-8B | 48.0 | 45.8 | 50.0 | 23.1 |
| MedGemma-4B | 50.9 | 45.1 | 45.8 | 23.1 |
| **Trung bình bảy model đầy đủ** | **60.4** | **58.5** | **59.1** | **50.5** |
| **Số câu** | **544** | **935** | **166** | **13** |
| **Đối chiếu HANDOFF** | **MATCH** | **MATCH** | **MATCH** | **MATCH** |

Nemotron dùng mẫu số riêng: 474 / 799 / 148 / 10; không được so trực tiếp từng cột với các model chạy đủ.

Tính thêm để kiểm tra phần reasoning: **108/237** đổi `pred`; phân bố trong `BatDong` là **130 / 72 / 35 / 1**, và **90/140** giữ đáp án đồng thuận ba model — đều khớp. Trong 237 record nhanh có một `pred=None`, nên “108 đổi đáp án” chính xác hơn nếu gọi là **108 thay đổi trạng thái dự đoán**, hoặc báo riêng chuyển từ không parse được sang có đáp án.

## 2. Review hai script

**Đề nghị sửa trước khi dùng workbook để duyệt chính thức.** Không thấy lỗi làm sai sáu số đếm hiện tại, nhưng có các lỗi thực chất sau.

1. **[Cao] Tạo lại workbook sẽ xóa phán quyết bác sĩ đã nhập.**  
   `scripts/eval/build_review_workbook.py:217` tạo năm cột duyệt trống; `:353` lưu đè cùng `VM14K_review.xlsx` mà không đọc hoặc giữ nội dung cũ. Chạy lại sau khi thêm reasoning sẽ mất phân loại, đáp án sửa, nguồn và người duyệt. Cần lưu phiên bản mới hoặc nhập lại annotation theo `id`; tốt nhất giữ annotation trong một nguồn riêng.

2. **[Vừa] Parser có thể lấy đáp án cũ dù kết luận cuối đã thay đổi hoặc từ chối chọn.**  
   `scripts/eval/collect_reasoning.py:58` lọc chữ hợp lệ **trước** khi lấy lần xuất hiện cuối; `:62` fallback sang parser lấy chữ cái trong dòng cuối. Tôi tái hiện được:
   - Bốn phương án, text `Đáp án: B\nĐáp án: G` → trả **B**, thay vì báo kết luận ngoài phạm vi.
   - `Đáp án: B\nĐáp án: không có phương án đúng` → trả **B**, mất trạng thái từ chối.
   - `Không chọn A hay B.` → trả **A**.
   
   Cần ưu tiên kết luận cuối, có trạng thái abstention rõ ràng và chỉ chấp nhận fallback khi dòng cuối thực sự là một đáp án. Đây là lỗi biên đã tái hiện; tôi chưa xác nhận nó làm sai `pred` nào trong log hiện tại.

3. **[Vừa] Hòa phiếu bị biểu diễn như có một phương án thắng duy nhất.**  
   `scripts/eval/build_review_workbook.py:255–257` dùng `Counter.most_common(1)`, nên hòa được quyết định theo thứ tự model. Có **tám câu** hòa cao nhất trong `ToanBoSai`. Ví dụ `31c5884bf0764ee0abec477fcb62680a`: B và D đều có ba phiếu, C có một. Các cột tại `:277–279` chỉ hiện một đáp án và nội dung của nó, dễ dẫn dắt người duyệt. Cần hiện tất cả phương án hòa và cờ hòa; số đếm 125 không bị ảnh hưởng.

4. **[Vừa] Các lần chạy reasoning khác cấu hình bị gộp âm thầm.**  
   `scripts/eval/build_review_workbook.py:113–122` đọc mọi JSONL, khóa theo tên model và `id`. Nếu có cả `think-on` và `think-off`, hoặc nhiều provider cho cùng model, file đứng sau theo tên sẽ ghi đè file trước. Đây không phải “record mới nhất” theo thời gian, cũng không phải cùng điều kiện thí nghiệm. Cần chọn run rõ ràng và giữ `provider`, `think`, cấu hình trong danh tính run. Hiện chỉ có một file reasoning nên chưa ảnh hưởng kết quả đã bàn giao.

5. **[Vừa] Resume coi phản hồi rỗng hoặc bị cắt ngắn là hoàn tất.**  
   `scripts/eval/collect_reasoning.py:79–90` có thể tạo kết quả rỗng từ response thiếu `choices`; `:151` vẫn ghi `error=None`. Tại `:131–132`, `done_records()` sẽ bỏ qua ID này trong lần chạy sau, kể cả `done_reason="length"`. Đổi `--max-tokens` cũng không tạo tên run mới (`:126–128`), nên tăng token rồi chạy lại chưa chắc hỏi lại câu bị cắt. Cần phân biệt thành công, abstention có chủ ý, phản hồi thiếu và truncation. Log hiện tại có **268/268 `stop`**, không có nội dung đáp án rỗng.

6. **[Vừa] Danh sách ID đầu vào có thể bị rút ngắn mà không báo.**  
   `scripts/eval/collect_reasoning.py:115–116` bỏ ID không có trong `by_id`. Hàm `load_rows()` được import còn loại mọi câu `contradiction_pending_review`, nên dùng script này để hỏi lại 62 câu mâu thuẫn sẽ âm thầm bỏ chúng — dù lấy giải thích không cần tin khóa đáp án. Cần kiểm tra ID thiếu và tách điều kiện “không được chấm điểm” khỏi “không được hỏi model”.

Các điểm không thấy sai:

- Quy tắc giữ record cuối không lỗi đúng; lỗi API về sau không xóa record thành công trước đó.
- Tính `pred=None` là sai đúng với định nghĩa đã công bố; trong 125 câu `ToanBoSai`, chỉ **một câu** có ít nhất một model không parse được.
- Cột “đổi từ X” tại `build_review_workbook.py:214–216` so với **cùng model**, không nhầm sang đáp án của cặp mạnh.
- Resume vẫn có điểm yếu khi JSONL bị đứt dòng cuối: `json.loads()` sẽ làm dừng cả chương trình. Không có dòng JSON hỏng trong các file tôi kiểm tra.

## 3a. Khóa đáp án có phải do GPT-4o sinh?

**Claude đúng khi yêu cầu diễn đạt thận trọng, nhưng sai ở nhận định paper “chỉ nói trích xuất và gán nhãn”.**

Tôi truy cập được [paper, §3.2.2 và Table 1](https://arxiv.org/html/2506.01305v1). Paper vừa mô tả GPT-4o/Gemini trích xuất và bổ sung nhãn, vừa ghi rõ `correctOption` là **“The correct answer according to GPT-4o”**. Sau đó paper mô tả xác minh bằng đáp án nguồn, foundation LLM và chuyên gia. Vì vậy, có bằng chứng cho vai trò GPT-4o trong tạo trường đáp án; chưa đủ để khẳng định mọi khóa cuối cùng đều do GPT-4o tự suy ra.

`VM14K_audit_notes.pdf`, trang 7, ghi thiếu cột hoặc hồ sơ tách đáp án nguồn, LLM và chuyên gia. Điều đó hỗ trợ kết luận **không kiểm toán được nguồn gốc từng khóa và phạm vi duyệt chuyên gia từ artifact hiện có**. Nó không chứng minh chuyên gia chưa từng kiểm tra.

Nên sửa mục 1.2a của `TONG_QUAN_VM14K_CHO_THAY.md` thành: paper mô tả đáp án theo GPT-4o và quy trình đối chiếu ba nguồn, nhưng bản phát hành không cung cấp hồ sơ đủ để xác minh từng khóa hoặc mức bao phủ duyệt chuyên gia. Cũng không nên gọi 4k/10k/2k là **train/val/test**: paper gọi đó là các phần public/private.

## 3b. Llama-3.1-8B 46.7 so với paper 48.73 có “khớp” không?

**Có thể nói “gần với mốc paper”, không nên nói “tái lập khớp”.**

Tôi tính được **775/1658 = 46.7431%**, Wilson 95% **[44.3517–49.1494]**. Số 48.73 nằm trong khoảng này; cách viết [44.3–49.1] chỉ lệch làm tròn nhẹ ở cận dưới.

Tuy nhiên, khoảng tin cậy chứa mốc paper không chứng minh tương đương. Hai kết quả khác tập câu hỏi, dữ liệu đã làm sạch, và cấu hình chạy; không phải phép so ghép cặp. `reports/eval/SUMMARY.md` đã nói đúng rằng đây là mốc tham khảo. `RAW_VS_CLEAN.md` còn ước lượng điểm trên bản thô khoảng **46.6**, cho thấy trong kiểm tra đó cleaning không giải thích phần lớn chênh lệch với 48.73.

Mốc **48.73** đúng với pass@1 trong [Table 2 của paper](https://arxiv.org/html/2506.01305v1).

## 3c. Câu “mức sinh thay thế”: B hay C?

**Tôi đồng ý khóa B có khả năng sai; C là lựa chọn đúng theo định nghĩa dân số học chuẩn.**

Câu `0e44bc5f2ac54a0b8b06c74bed3454be` hỏi “Mức sinh thay thế đạt được khi”, không nêu giả định loại bỏ tử vong. B là tỷ suất tái sinh thô = 1; C là tỷ suất tái sinh tinh = 1.

GRR không tính tử vong: sinh trung bình một con gái chưa bảo đảm thế hệ con gái sẽ thay thế thế hệ mẹ. NRR tính sống sót tới các độ tuổi sinh sản, nên **NRR = 1** là điều kiện thay thế. GRR = 1 chỉ phù hợp trong giả định không có tử vong liên quan. Định nghĩa của [UN Statistics Division](https://unstats.un.org/unsd/Demographic/products/dyb/DYBNat/NotesNatStatTab03.htm) phân biệt rõ hai trường hợp này.

Dù chọn C, tôi không chấp nhận nguyên xi toàn bộ reasoning Nemotron: mô tả NRR là sống sót “đến cuối kỳ sinh đẻ” không chính xác; cũng không được suy ra dân số lập tức ngừng tăng, vì còn quán tính dân số. Nên ghi câu này là **nghi khóa sai, bằng chứng mạnh**, rồi có người chuyên môn xác nhận để đưa vào bản sửa.

## 3d. Audit notes đã gạt hướng fine-tune rồi so frontier?

**Có cân nhắc và nghiêng sang audit; nói “đã quyết định gạt hẳn” thì quá mạnh.**

`docs/research/VM14K_audit_notes.pdf`, trang 8, nêu trực tiếp đề xuất train model y khoa tiếng Việt rồi so frontier, và các hạn chế: dữ liệu bẩn, chưa có split, chi phí cao, đóng góp có thể chỉ là một con số khó diễn giải. Ngay sau đó tài liệu đề xuất “Benchmark audit + cleaned release”.

Đây là bằng chứng rõ cho việc hướng đó đã được xem xét và bị đánh giá kém hấp dẫn. Tôi không thấy quyết định chính thức loại bỏ mọi fine-tune; mục 8 của bản tổng quan tháng 8 còn đề xuất fine-tune theo RAFT sau gate retrieval, với mục tiêu khác.

## 4. Phương pháp chọn câu bằng đồng thuận model

**Đồng ý dùng để ưu tiên duyệt, nhưng chưa đủ để ước lượng tỷ lệ lỗi của benchmark.**

Các thiên lệch chính:

- Model chia sẻ dữ liệu huấn luyện, nguồn kiến thức và lỗi phổ biến; bảy phiếu không phải bảy chuyên gia độc lập.
- Chọn theo bất đồng với khóa làm mẫu giàu câu khó, mơ hồ và lỗi model. Ngược lại, khóa sai mà model cùng học thuộc sẽ bị bỏ sót.
- Hai model mạnh được chọn làm cổng vào; tiêu chí này có thể thiên về chuyên khoa và loại câu chúng xử lý tốt.
- Cho bác sĩ nhìn khóa, phiếu và reasoning ngay từ đầu gây anchoring. Hướng dẫn “đọc trước” yếu hơn một giao diện thực sự che các thông tin đó.

Tôi đề nghị dành khoảng **150–200 câu** cho một thiết kế hai phần: mẫu ngẫu nhiên từ toàn bộ test để đo tỷ lệ lỗi, và mẫu ưu tiên từ các tầng đồng thuận, mọi model sai, câu lỗi cấu trúc hoặc khóa mâu thuẫn. Phân bổ trước, lưu xác suất chọn mẫu, báo kết quả từng tầng riêng; chỉ suy rộng bằng trọng số phù hợp.

Bác sĩ nên trả lời độc lập trước khi xem model; có người duyệt thứ hai trên một phần mẫu và cơ chế xử lý bất đồng. Đánh giá phương pháp chọn câu bằng **tỷ lệ lỗi được xác nhận trên số câu duyệt**, so với chọn ngẫu nhiên. Chưa duyệt phần không được chọn thì chưa thể biết recall phát hiện lỗi.

## 5. Đánh giá hướng nghiên cứu đề xuất

**Đồng ý lấy audit làm trục chính và để fine-tune làm phần phụ. Tôi sẽ thay đổi cách đóng khung bằng chứng và protocol.**

- Giữ trọng tâm vào artifact, phép kiểm tra tái lập, bộ sửa có nguồn và ảnh hưởng lên đánh giá. `VM14K_session_findings.md` hỗ trợ rõ vấn đề trùng lặp và hành vi dedup bỏ mâu thuẫn; suy luận từ đó sang chính xác dữ liệu dùng cho mọi kết quả paper vẫn cần thận trọng.
- Bảng độ khó cho thấy **khả năng phân biệt mức độ đối với các model này yếu**. Nó chưa chứng minh nhãn khó sai theo đánh giá con người; khó với bác sĩ và khó với LLM có thể khác nhau. Con số 19.8% cũng cần định nghĩa rõ mẫu số và không quy toàn bộ bất nhất cho cùng một lần chạy LLM khi thiếu provenance nhãn.
- Không ép bốn nhóm thành các nguyên nhân loại trừ nhau. Một câu có thể vừa lỗi đề vừa lỗi khóa. Nên tách trạng thái câu hỏi, trạng thái khóa, bối cảnh guideline và mức chắc chắn; giữ lựa chọn “chưa xác định” và “nhiều đáp án đúng”.
- Báo điểm trên khóa gốc và khóa đã duyệt cùng tập câu, kèm mức bao phủ duyệt. Công bố phiên bản sửa và giữ nguyên bản cũ. Nếu dùng test đã audit để tinh chỉnh cách huấn luyện, cần một tập đánh giá độc lập mới.
- Fine-tune đáng làm khi có giả thuyết về chuyển giao sang đề ngoài hoặc khả năng dùng bằng chứng. “Tăng điểm là điều ai cũng đoán” không đủ để bác bỏ nó, nhưng hiện chưa nên để nó chiếm nguồn lực của bước xác minh khóa.
- Mốc **ACL 2027 qua ARR tháng 1/2027** hiện được [trang Dates chính thức](https://aclrollingreview.org/dates) hỗ trợ ở cấp tháng; chưa có ngày cụ thể hoặc commitment date. Không nên ghi deadline chính xác hơn nguồn.

## 6. Ba việc ưu tiên tiếp theo

1. **Sửa parser và bảo vệ annotation khi tạo lại workbook**, đồng thời báo hòa phiếu và chọn run reasoning rõ ràng.
2. **Chốt protocol duyệt 150–200 câu có mẫu ngẫu nhiên và mẫu ưu tiên**, che khóa/model ở lượt đầu và có kiểm tra bất đồng chuyên gia.
3. **Sửa các khẳng định quá mạnh về nguồn khóa và nhãn khó**, rồi công bố audit cùng bản sửa có provenance và đánh giá ảnh hưởng; chỉ mở rộng fine-tune khi có đề ngoài.
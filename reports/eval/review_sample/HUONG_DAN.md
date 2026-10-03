# Protocol duyệt đáp án VM14K

Sinh bởi `scripts/eval/build_review_sample.py` (seed 42). Bộ mẫu đã cố định: script từ chối ghi đè
nếu không có `--force`, vì các file này sẽ chứa phần người duyệt điền. Đã chỉnh theo góp ý của Codex trong
`CODEX_REVIEW_2.md`.

> **Cần chốt trước khi gửi cho bác sĩ: cỡ mẫu ngẫu nhiên.** Hiện là 60 câu, chỉ đủ cho một **pilot**:
> 0/60 câu lỗi vẫn cho cận trên 95% là 6.0%; 5/60 cho 3.6–18.1%. Nếu muốn khoảng tin cậy rộng không quá
> ±5 điểm ở mọi tỉ lệ thì cần **385** câu ngẫu nhiên. **200** câu là phương án thực dụng: 20/200 cho
> 6.6–14.9%. Đổi cỡ mẫu thì bốc lại toàn bộ (`--n-random N --force`). Việc này chỉ được làm **trước khi** ai
> đó bắt đầu duyệt.

## 1. Phạm vi và hai loại mẫu

Mọi ước lượng chỉ áp dụng cho **1.658 câu test đã chạy eval**. Đó là split test cố định trừ 4 ID bị loại vì
trùng ở cleaning stage 12/14. Không suy rộng sang "toàn bộ VM14K".

| Câu hỏi | Mẫu dùng để trả lời |
|---|---|
| Tỉ lệ khoá sai / đề lỗi trong 1.658 câu là bao nhiêu? | Chỉ tầng `ngau_nhien` (ngẫu nhiên đơn giản, không hoàn lại) |
| Dùng đồng thuận model có tìm lỗi hiệu quả hơn chọn ngẫu nhiên không? | Tỉ lệ lỗi trong từng tập ưu tiên, so với tầng ngẫu nhiên |

Các tập ưu tiên được định nghĩa **theo thành viên** và không trùng nhau: mỗi câu thuộc tập đầu tiên mà nó
khớp. Các tập này chỉ xét trong 268 câu của BatDong ∪ ToanBoSai. Mẫu ngẫu nhiên được bốc **trước**, rồi mỗi
pool ưu tiên mới loại những câu đã có trong mẫu ngẫu nhiên.

| Tầng | Định nghĩa | Thành viên | Đã có trong mẫu ngẫu nhiên | Pool còn lại | Bốc | `stage_selection_prob` |
|---|---|---:|---:|---:|---:|---:|
| `ngau_nhien` | Ngẫu nhiên từ 1.658 câu | — | — | 1.658 | 60 | 0.036 |
| `uu_tien_1_tu_choi` | Nemotron, khi được yêu cầu giải thích, không chọn phương án nào | 4 | 1 | 3 | 3 | 1 |
| `uu_tien_2_dong_thuan_giu` | DeepSeek, Gemma-31B và Nemotron cùng chọn một đáp án khác khoá, và Nemotron giữ đáp án đó khi giải thích | 90 | 5 | 85 | 85 | 1 |
| `uu_tien_3_batdong_khac` | Phần còn lại của BatDong | 147 | 2 | 145 | 15 | 0.103 |
| `uu_tien_4_toanbosai_khac` | Phần còn lại của ToanBoSai | 27 | 0 | 27 | 15 | 0.556 |

**`stage_selection_prob` là xác suất được chọn ở bước bốc của tầng đó**, với điều kiện mẫu ngẫu nhiên đã cố
định. Nó **không phải** xác suất một câu có mặt trong mẫu cuối cùng: 5 câu của tập 2 rơi vào mẫu ngẫu nhiên
có xác suất ghi là 0.036, nhưng thực tế cả tập 2 đều được duyệt. **Không dùng cột này làm trọng số
Horvitz–Thompson cho cả 178 câu.**

Ước lượng số câu lỗi trong một tập ưu tiên S:

    lỗi(S) = số câu lỗi trong các câu ngẫu nhiên thuộc S  (cột priority_set của manifest)
           + pool_size(S) × tỉ lệ lỗi trong các câu được bốc ở tầng ưu tiên của S

Tổng cộng **178 câu**. Mỗi tầng có khoảng 20% câu (làm tròn lên) được duyệt thêm bởi người thứ hai, tổng
**36 câu**, trong đó 12 câu thuộc tầng ngẫu nhiên. `sample_manifest.csv` gồm mã câu, id, tầng, pool, xác suất,
tập ưu tiên và cờ duyệt đôi. **Không đưa file này cho người duyệt.**

## 2. Các file và quy tắc giao nhận

| File | Người nhận | Nội dung |
|---|---|---|
| `vong1_doc_lap.xlsx` | Người duyệt chính | 178 câu: chỉ có câu hỏi và các phương án, xếp ngẫu nhiên, mã `Q001…`. Không có id, khoá, đáp án model hay tầng |
| `vong1_doc_lap_nguoi2.xlsx` | Người duyệt thứ hai | 36 câu, cùng định dạng và cùng mã |
| `vong2_doi_chieu.xlsx` | Người duyệt chính | Thêm khoá, đáp án 8 model, đáp án đa số của 7 model và phần giải thích của Nemotron |
| `vong2_doi_chieu_nguoi2.xlsx` | Người duyệt thứ hai | Như trên, cho 36 câu |

Quy tắc:
1. Vòng 2 chỉ được gửi khi **cả hai người** đã nộp vòng 1.
2. File đã nộp là **bất biến**: lưu bản gốc kèm mã SHA-256 lúc nhận. Đổi ý thì ghi ở vòng 2, không sửa vòng 1.
3. Hai người không xem file của nhau ở bất kỳ vòng nào cho tới bước phân xử.
4. Ghi lại commit của script, seed và manifest dùng để sinh file. Hai file workbook chỉ *tạo điều kiện* để duyệt độc lập; việc làm độc lập thật sự dựa vào cam kết của người duyệt.

Phần giải thích của Nemotron được thu cho **mọi** câu trong mẫu, kể cả câu ngẫu nhiên, để vòng 2 cung cấp
cùng loại thông tin cho mọi tầng.

## 3. Các trường dữ liệu

- **Đáp án** (vòng 1: "Đáp án bạn chọn"; vòng 2: "Đáp án đúng cuối cùng"): chọn một chữ, hoặc "Nhiều đáp án đúng" (kèm **tập chữ**, ví dụ `AC`), "Không có đáp án đúng", "Không xác định được".
- **Tình trạng câu hỏi** (vòng 1) / **Tình trạng câu hỏi cuối cùng** (vòng 2): **một** mức loại trừ nhau, gồm "Bình thường", "Có lỗi nhưng vẫn trả lời được", "Không trả lời được". Thêm 5 cờ lỗi độc lập (mơ hồ, thiếu dữ kiện, thiếu hình, chính tả - đánh máy, phương án lỗi hoặc trùng) để đánh dấu mọi loại lỗi gặp phải. Cờ chỉ có lựa chọn "Có". **Khi đã chọn tình trạng tổng quát thì ô cờ trống được tính là "Không"**; chưa chọn tình trạng thì cờ là thiếu. Phiếu tự mâu thuẫn ("Bình thường" mà có cờ, hoặc "có lỗi" mà không đánh cờ nào) bị báo cảnh báo nhưng vẫn được dùng.
- **Vòng 2** có thêm:
  - trạng thái khoá: Đúng / Sai / Là một trong nhiều đáp án đúng / Không xác định;
  - bối cảnh kiến thức: quốc tế / phác đồ VN / Không rõ / Không áp dụng;
  - cờ riêng "Kiến thức đã thay đổi theo thời gian?";
  - nguyên nhân **chính** và **phụ** khiến **đáp án đa số của 7 model** (có cột riêng, ghi rõ khi hoà) khác khoá.

## 4. Kế hoạch phân tích (chốt trước khi có kết quả)

**Endpoint** (tính trên tầng ngẫu nhiên, n = số câu ngẫu nhiên, khoảng Wilson 95%):
- **E1 – Khoá sai đã xác nhận:** s/n, với s là số câu có trạng thái khoá cuối cùng "Sai". Báo kèm **khoảng nhạy** từ s/n tới (s+u)/n, trong đó u là số câu "Không xác định". Không loại câu không xác định khỏi mẫu số.
- **E2 – Đề lỗi ảnh hưởng tới việc trả lời:** tình trạng cuối cùng là "Không trả lời được", **hoặc** khoá là "Một trong nhiều đáp án đúng". Lỗi đánh máy vô hại không tính vào E2.
- **E3 – Hợp:** E1 hoặc E2.
- Mỗi tầng ưu tiên báo E1–E3 riêng, kèm ước lượng lỗi(S) ở mục 1.

**Đồng thuận giữa hai người duyệt** (36 cặp, vòng 1):
- Đáp án được so theo **tập đáp án chuẩn hoá**: chữ in hoa, sắp xếp. Một chữ X được coi là {X}. "Không có đáp án đúng" và "Không xác định được" là hai loại riêng. Ô trống là thiếu dữ liệu, bỏ ra và báo số lượng.
- Báo **tỉ lệ đồng ý thô** và **Cohen's κ**, kèm CI bootstrap theo câu. Làm như vậy cho đáp án, cho tình trạng tổng quát, và cho từng cờ lỗi.
- 36 cặp này được làm giàu câu nghi vấn (chỉ 12 cặp ngẫu nhiên), nên κ mô tả mẫu duyệt đôi, **không đại diện** cho cả benchmark.

**Phân xử:**
- Khi hai người khác nhau ở trạng thái khoá hoặc tập đáp án cuối cùng: hai người trao đổi và dẫn nguồn.
- Nếu vẫn không thống nhất: một **người thứ ba** (chuyên khoa phù hợp) quyết định, có nguồn kèm theo.
- Ghi quyết định cuối và lý do vào bảng phân xử. Người duyệt chính **không** mặc nhiên là đáp án đúng.
- Câu chỉ có một người duyệt thì lấy vòng 2 của người đó, kèm cờ "1 người duyệt".

**Thay đổi sau khi mở đáp án:**
- Tính tỉ lệ câu có tập đáp án ở vòng 2 khác vòng 1.
- Phân loại hướng thay đổi theo hai mốc đã định nghĩa trước: **khoá**, và **đáp án đa số của 7 model**.
- Thiết kế này **không tách được** ảnh hưởng của khoá, phiếu model, phần giải thích, hay đơn giản là việc người duyệt nghĩ lại. Chỉ báo như mô tả, không suy ra nguyên nhân.

Không báo **recall** của cách chọn câu, vì phần ngoài mẫu chưa được duyệt.

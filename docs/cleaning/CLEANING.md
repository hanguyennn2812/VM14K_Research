# VM14K — Làm sạch dữ liệu (gộp 1 doc, 1 script)

Toàn bộ pipeline làm sạch giờ nằm trong **1 script duy nhất**:
[`scripts/cleaning/clean_all.py`](../../scripts/cleaning/clean_all.py). Chạy 1 lần, ra đúng 3
file — không còn 11 script + 11 report JSON rải rác nữa.

```powershell
python scripts/cleaning/clean_all.py
```

| File | Ý nghĩa |
| --- | --- |
| `data/baseline/clean.jsonl` | Input — output của pipeline dedup gốc (không đổi, xem `scripts/analysis/`) |
| `data/cleaned/clean_final.jsonl` | **Dataset chính thức, dùng cái này** — 10,642 dòng |
| `data/quarantine/quarantine_all.jsonl` | Toàn bộ dòng bị loại, giữ nguyên gốc trong field `"row"`, có `"source_stage"` + `"reason"` để biết bị loại vì sao |
| `reports/cleaning/clean_final.report.json` | 1 report duy nhất: số dòng mỗi stage loại, hash, kết quả invariant check |

Script từ chối ghi đè file có sẵn trừ khi truyền `--force`.

## Pipeline làm gì (11 stage, chạy tuần tự trong 1 file)

`data/baseline/clean.jsonl` (10,956 dòng) → 11 stage → `clean_final.jsonl` (10,642 dòng).

| # | Stage | Loại | Số dòng ảnh hưởng | Vì sao |
| --- | --- | --- | ---: | --- |
| 01 | Xoá 1 dòng trùng nội dung còn sót | Xoá thẳng | 1 | Đã có trong audit gốc, key = câu hỏi+option đã normalize, giữ dòng đầu tiên |
| 02 | Câu hỏi rỗng / <2 option | Quarantine | 14 | Không đủ điều kiện là 1 câu MCQ |
| 03 | Option trùng nhau (so sánh bảo thủ: NFC+trim+casefold) | Quarantine | 199 | Không rõ option nào là đáp án đúng nếu 2 lựa chọn giống hệt nhau |
| 04 | Sửa 5 dòng `medical_topic` bị hỏng (ID cụ thể) | Sửa trực tiếp | 5 | Đã audit thủ công, không suy đoán chuyên khoa |
| 05 | Chuẩn hoá Unicode NFC + trim khoảng trắng ngoài | Sửa trực tiếp | 46 | Không đổi nghĩa |
| 06 | 12 câu cần hình/audio đã mất (ID cụ thể) | Quarantine | 12 | Câu hỏi phụ thuộc ảnh/âm thanh không còn tồn tại trong dữ liệu text |
| 07 | Option là placeholder rỗng (`optionA`, `....`) | Quarantine | 66 | Thiếu lựa chọn thật sự |
| 08 | Convert tag `<br>` thành xuống dòng | Sửa trực tiếp | 3 dòng / 12 tag | Không đụng vào dấu `<` `>` toán học (`<15`, `>=3`) |
| 09 | Decode HTML entity còn sót (`&gt;` `&quot;` `&nbsp;`) | Sửa trực tiếp | 6 | Step 08 bỏ sót entity, chỉ xử lý tag |
| 10 | Option bị hỏng ranh giới: dính chữ / lệch nhãn / rỗng (ID cụ thể, audit thủ công) | **Quarantine — không tự đoán** | 22 | Xem phần "Phát hiện quan trọng" bên dưới |
| 11 | Xoá nhãn `A./B./C./D.` dư thừa (khớp đúng vị trí) | Sửa trực tiếp | 9 dòng / 26 option | Nhãn trùng lặp với vị trí, xoá không mất thông tin |

Mỗi stage trong script đều có `assert_stage_count(...)` — nếu số dòng bị ảnh hưởng khác
con số đã audit ở trên, script **dừng ngay và báo lỗi**, không âm thầm chạy tiếp với rule
đã thay đổi phạm vi.

## Phát hiện quan trọng nhất: Stage 10 — option bị hỏng ranh giới (22 dòng)

Đây là lỗi **không thể bắt được bằng validate cấu trúc** (mỗi option vẫn là chuỗi
non-blank, khác nhau) — phải đọc nội dung thật mới thấy. Quét ra 78 candidate thô,
phần lớn false positive (tên vitamin A/B1/B12/E, chủng viêm gan A/C/D/E, thang điểm
"Cấp độ A,B,C,D"...). Đọc thủ công từng dòng, còn lại 22 dòng lỗi thật, chia 3 dạng:

**a) Option dính chữ vào nhau (9 dòng).** Ví dụ `ed63be9518874b9cbfa22a84c7006c8c`
("Giun tóc gây thiếu máu do"):
```
[0] "Hút máu ký chủ B. Xâm nhập mô ký chủ C. Tiết độc tố D. Ăn hồng"
[1] "cầu"
```
4 đáp án thật bị gộp thành 1 blob + 1 mảnh vụn mồ côi "cầu" (đuôi của "hồng cầu").

**b) Option lệch nhãn so với vị trí (8 dòng) — có thể làm SAI đáp án đúng.** Ví dụ
`62a96ed2071e48d4bcb645c666303617`:
```
answer: "C", answer_index: 2
[1] "C. UAG, UAA, UGA"     <- nội dung THẬT của "C"
[2] "D. UUG, UAA, UGA"     <- answer_index trỏ vào đây, nhưng tự nó ghi nhãn "D"
```
`answer` ghi "C" nhưng `answer_index` trỏ vào nội dung tự mang nhãn "D" — mâu thuẫn rõ
ràng, không phải lỗi hiển thị mà là lỗi logic đáp án.

**c) Option rỗng, chỉ còn nhãn (4 dòng).** VD `9dcb8a0294c741129690b05db893266a`:
`["A. Đúng", "B. Sai", "C.", "D."]` — 2 option cuối không có nội dung.

**Vì sao quarantine chứ không tự sửa:** tự sắp lại option theo nhãn nhúng có nguy cơ
đoán sai — nhiều dòng lỗi từ nhiều nguồn cùng lúc (dính chữ + ký tự OCR lạ `+`, `|`,
`Đ`, chữ Hy Lạp `Β` giả `B`...). Giữ nguyên byte-for-byte trong quarantine, không đoán
nội dung — đúng tinh thần các bước quarantine khác trong pipeline.

## Đã check nhưng không phải lỗi (loại trừ có chủ đích)

- Câu hỏi/option kết thúc bằng `...`/`…` (53/45 dòng): là format điền-vào-chỗ-trống
  hợp lệ, không phải bị cắt cụt.
- 1 dòng double-space trong câu hỏi (`a4c0e0be...`): giữ nguyên — internal whitespace
  được cố tình bảo toàn (không đổi cấu trúc câu đánh số (1)(2)(3)).
- ~40+ candidate "nhãn chữ cái" khác (tên vitamin, chủng virus, thang điểm, câu hỏi
  ngữ pháp có literal A/B/C/D...): đọc thủ công xác nhận là nội dung hợp lệ.

## Kết quả cuối

| | Trước | Sau |
| --- | ---: | ---: |
| Dataset | `data/baseline/clean.jsonl` | `data/cleaned/clean_final.jsonl` |
| Số dòng | 10,956 | **10,642** |
| Bị loại | — | 314 (1 dup xoá thẳng + 313 quarantine) |

Toàn bộ invariant cuối (unique id, question non-blank, ≥2 option, answer_index hợp lệ,
answer letter khớp index, topic non-blank, Unicode NFC, không còn HTML tag/entity,
không còn placeholder, không còn option lệch nhãn) được script tự check và in trong
`final_invariants` của report — **pass hết**.

## Dữ liệu trước khi clean — giữ nguyên để đối chiếu

- `data/raw/*.jsonl` — dữ liệu gốc, không đổi.
- `data/baseline/clean.jsonl` — input của `clean_all.py`, không đổi.
- `data/quarantine/quarantine_all.jsonl` — mọi dòng bị loại, giữ nguyên trong field
  `"row"`, có thể lọc theo `"source_stage"` để xem loại vì bước nào, hoặc theo
  `"reason"` để xem lý do cụ thể.
- Muốn xem lại dòng nào đó trước/sau khi clean: so `id` giữa `data/baseline/clean.jsonl`
  và `data/cleaned/clean_final.jsonl` (nếu không có trong final, tìm trong
  `quarantine_all.jsonl`).

## Còn lại (chưa làm, cần người có chuyên môn y khoa)

Xem [`REMAINING_REVIEW_BACKLOG.md`](REMAINING_REVIEW_BACKLOG.md): câu hỏi trùng stem,
câu quá ngắn/nghi gibberish, khả năng lộ đáp án trong câu hỏi, taxonomy chủ đề chồng
chéo, và quan trọng nhất — **đúng/sai về mặt y khoa của answer_index không có công cụ
nào tự động xác nhận được**.

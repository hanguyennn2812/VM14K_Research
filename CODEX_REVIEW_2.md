## 1. Thiết kế thống kê: mẫu ngẫu nhiên hợp lệ, nhưng cần sửa cách diễn giải xác suất và endpoint

Tôi tính lại độc lập từ JSONL, giữ record cuối không lỗi cho mỗi ID, rồi tái lập draw seed 42. **Manifest khớp toàn bộ 178 câu, mã câu, xác suất và 36 cờ duyệt đôi.**

| Pool ưu tiên, sau khi loại thành viên của pool trước | Trước khi loại mẫu ngẫu nhiên | Nằm trong mẫu ngẫu nhiên | Pool còn lại | Bốc thêm |
|---|---:|---:|---:|---:|
| Nemotron từ chối chọn | 4 | 1 | **3** | 3 |
| Đồng thuận ba model và giữ khi giải thích | 90 | 5 | **85** | 85 |
| BatDong còn lại | 147 | 2 | **145** | 15 |
| ToanBoSai còn lại | 27 | 0 | **27** | 15 |

Các tập gốc là BatDong **238**, ToanBoSai **125**, từ chối **4**, giữ đồng thuận **90**. Bốn pool cuối thực sự rời nhau và không giao với 60 câu ngẫu nhiên.

**60 câu là SRS không hoàn lại từ 1.658 câu đã chạy eval.** `build_review_sample.py:239` bốc trước khi loại các câu khỏi pool ưu tiên; đây là thứ tự đúng. Không nên loại pool ưu tiên khỏi khung bốc ngẫu nhiên, vì khi đó mẫu chỉ ước lượng phần còn lại. Tuy nhiên, không được gọi kết quả là tỷ lệ lỗi của toàn bộ VM14K: split lưu 1.662 ID test, trong đó bốn ID không còn trong dữ liệu sạch; khung thực tế chỉ có 1.658 câu.

**`selection_prob` đúng theo từng bước, nhưng không phải xác suất được đưa vào toàn bộ mẫu.** Tại `build_review_sample.py:236`, các giá trị là:

- Ngẫu nhiên: `60/1658 = 0.036188`.
- Ưu tiên: `1`, `1`, `15/145 = 0.103448`, `15/27 = 0.555556`, có điều kiện trên draw ngẫu nhiên đã cố định.

Ví dụ, năm câu thuộc nhóm giữ đồng thuận nhưng được bốc ngẫu nhiên mang xác suất `0.036188` trong manifest; xác suất chúng xuất hiện **qua bất kỳ đường nào** thực tế bằng 1, vì nhóm này được duyệt hết. Không được dùng cột hiện tại làm trọng số Horvitz–Thompson cho toàn bộ 178 câu. Nên đổi tên thành `stage_selection_prob` và ghi rõ điều kiện.

**“Tỷ lệ × pool_size” đúng cho pool còn lại**, theo SRS ở bước hai. Nó không tự động ước lượng toàn bộ nhóm ưu tiên trước khi loại mẫu ngẫu nhiên. Ví dụ, số lỗi trong nhóm 90 câu phải bằng lỗi quan sát ở năm câu ngẫu nhiên thuộc nhóm đó **cộng** lỗi trong 85 câu ưu tiên. Với nhóm BatDong còn lại: cộng lỗi ở hai câu ngẫu nhiên vào `145 × tỷ lệ lỗi của 15 câu ưu tiên`.

**60 câu chỉ phù hợp pilot.** Tôi tính Wilson 95%:

- `5/60`: **3,61–18,07%**, khớp ví dụ trong hướng dẫn.
- `0/60`: cận trên vẫn **6,02%**.

Tôi sẽ tiền đăng ký **385 câu ngẫu nhiên** nếu mục tiêu là CI có nửa độ rộng khoảng năm điểm phần trăm ngay cả khi tỷ lệ gần 50%, giữ Wilson thông thường. Nếu nguồn lực hạn chế, **200 câu ngẫu nhiên** là phương án thực dụng: `20/200` cho CI **6,57–14,94%**, nhưng không bảo đảm độ chính xác ±5 điểm ở mọi tỷ lệ. Công thức Wilson được đối chiếu với [NIST](https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm); các khoảng trên do tôi tính lại. Tăng n phải cập nhật bảng pool và thay mẫu trước khi duyệt.

Hai vấn đề trong kế hoạch phân tích cần chốt trước:

- `HUONG_DAN.md:35`: “Sai/60”, trong khi có câu chưa xác định, đo **tỷ lệ lỗi khóa đã xác nhận**, không mặc nhiên là tỷ lệ lỗi khóa thật. Báo thêm khoảng nhạy cảm `s/60` đến `(s+u)/60`, với `u` là số chưa xác định; không loại chúng khỏi mẫu số mà không giải thích.
- `HUONG_DAN.md:10` hứa đo “sai đáp án / lỗi đề”, nhưng `:35–36` chỉ đếm trạng thái khóa “Sai”. Cần endpoint riêng cho lỗi khóa, lỗi đề ảnh hưởng khả năng trả lời, và hợp của hai loại; quy định rõ cách tính câu nhiều đáp án đúng và lỗi đánh máy vô hại.

## 2. Blinding: đạt trong hai workbook hiện tại; độc lập phụ thuộc cách tổ chức duyệt

Tôi mở cả ba file bằng **openpyxl**. Hai file vòng 1 có đúng hai sheet nhìn thấy, 12 cột; không có sheet/cột/hàng ẩn, comment, formula, hyperlink, external link hoặc defined name. Metadata không chứa ID, khóa hay tầng. Question/options có cùng style trên mọi dòng; dropdown chỉ chứa lựa chọn duyệt chung.

**Không thấy kênh rò khóa, phiếu model hoặc tầng từ cấu trúc workbook.** Nội dung câu hỏi và phương án khớp dữ liệu nguồn; mã `Q001…Q178` được gán sau shuffle, không mã hóa tầng. Chuyên khoa là nhãn nguồn, không phải nhãn ưu tiên. Nội dung như “thiếu hình” có thể khiến người duyệt nghi câu thuộc nhóm nghi vấn, nhưng đó là suy đoán từ đề, không phải rò thông tin chọn mẫu.

File người thứ hai chứa đúng **36 câu** được đánh cờ: **12/1/17/3/3** theo năm tầng, mọi ô annotation trống. Nó giữ cùng mã và thứ tự tương đối với file chính; điều này hỗ trợ ghép cặp và không làm lộ câu trả lời người thứ nhất. Không cần shuffle riêng để có phán đoán độc lập.

Tuy nhiên, `HUONG_DAN.md:29` cần nói rõ: **chỉ mở vòng 2 sau khi cả hai người đã nộp vòng 1**, và người thứ hai không được xem file đã điền của người thứ nhất. Workbook riêng tạo điều kiện độc lập; nó không chứng minh hai người thực sự làm độc lập.

## 3. Thiết kế trường và tiền đăng ký: chưa đủ để phân tích không nhập nhằng

**[Cao] Vòng 2 mất danh sách đáp án khi có nhiều đáp án đúng.** `ROUND1_FIELDS` có cột ghi các chữ tại `build_review_sample.py:67`; `ROUND2_FIELDS` tại `:76` không có cột tương ứng. Sau reveal, chọn “Nhiều đáp án đúng” không cho biết tập đúng là `{A,B}` hay `{B,C}`. Không thể xác định chắc khóa thuộc tập đúng, thay đổi đáp án, hoặc mức đồng thuận với model. Cần lưu tập chữ chuẩn hóa ở cả hai vòng và quy định kiểm tra nhất quán với trạng thái khóa.

**[Vừa] Tình trạng câu hỏi là một dropdown đơn nhưng các loại lỗi chồng lấn.** `build_review_sample.py:69`: một câu có thể vừa thiếu hình vừa thiếu dữ kiện; phương án trùng cũng có thể gây mơ hồ. Không có quy tắc chọn nhãn chính. κ vẫn tính được về mặt số học, nhưng có thể đo khác biệt trong cách chọn nhãn hơn là khác biệt phán đoán. Nên tách trạng thái tổng quát thành một biến loại trừ nhau, rồi ghi từng loại lỗi bằng cờ riêng; κ tính trên biến tổng quát hoặc từng cờ.

Vòng 2 cũng thiếu trường **tình trạng câu hỏi cuối cùng**: người duyệt có thể đổi đánh giá đề sau khi đọc giải thích, nhưng chỉ ghi được trong ghi chú. Điều này cản endpoint lỗi đề cuối cùng.

**[Vừa] κ cho đáp án chưa có định nghĩa.** `HUONG_DAN.md:37` chưa quy định hai người cùng chọn “Nhiều đáp án đúng” nhưng ghi các tập chữ khác nhau có được tính là đồng thuận không. Cần tiền đăng ký so **tập đáp án chính xác** hay chỉ loại câu trả lời; chuẩn hóa thứ tự chữ, giá trị thiếu và “không xác định”. Báo thêm agreement thô và CI của κ. Với 36 cặp, trong đó chỉ 12 cặp ngẫu nhiên, κ gộp mô tả mẫu duyệt đôi được làm giàu câu nghi vấn, không đại diện toàn benchmark.

**[Vừa] Các trường vòng 2 vẫn ép những nguyên nhân có thể đồng thời xảy ra.** `build_review_sample.py:80–84`: một câu có thể vừa phụ thuộc thực hành Việt Nam vừa dùng kiến thức cũ; các model khác nhau cũng có thể sai vì những nguyên nhân khác nhau. Một ô “Vì sao model…” không xác định đang nói về model nào. Cần ghi model/nhóm model cụ thể và cho phép nhiều nguyên nhân; bối cảnh kiến thức cần lựa chọn “Không rõ”.

**[Cao] Chưa có quy trình phân xử bất đồng.** Hướng dẫn nói tính κ và “chốt” vòng 2, nhưng không quy định ai chốt khi hai bác sĩ khác nhau, cần nguồn nào để xác nhận lỗi, hay khi nào chuyển người thứ ba. Không được để người duyệt chính mặc nhiên trở thành ground truth chỉ vì đã thấy khóa và reasoning.

**“Đổi về phía model” chưa đo được theo định nghĩa hiện tại.** `HUONG_DAN.md:38`: tám model có thể chọn nhiều đáp án khác nhau. Phải định nghĩa trước đang so với cặp mạnh, Nemotron giải thích hay một tập đáp án model. Nên gọi đây là **thay đổi sau reveal**; thiết kế hiện tại không tách được tác động của khóa, phiếu model, reasoning và việc suy nghĩ lại.

## 4. Bug thực chất: sửa `done_records()` chưa giải quyết đầy đủ resume

**[Cao] Record mới bị dính vào dòng cuối dở dang không có newline.** `run_eval.py:291` bỏ qua dòng JSON hỏng, nhưng phần ghi hiện tại mở append tại `:461` và ghi ngay JSON mới tại `:438`. Dòng cuối cũ không bị loại hoặc ngăn cách.

Tôi tái hiện hoàn toàn trong bộ nhớ, không ghi file:

```text
{"id":"old","error":null}\n
{"id":"cut","error":
```

Sau khi nối record hợp lệ `{"id":"retried","error":null}\n`, lần resume tiếp theo chỉ trả về `old`: **record `retried` cũng bị bỏ qua**, vì cả dòng ghép là JSON hỏng. Sửa hiện tại giúp chương trình qua bước đọc nhưng không bảo toàn log mới. Cần xử lý ranh giới dòng trước khi append và bảo toàn phần log hợp lệ.

**[Cao] Cắt giữa ký tự UTF-8 vẫn làm chương trình dừng.** `run_eval.py:285–286` giải mã text trước khối `try` tại `:289`; chỉ bắt `JSONDecodeError` không bắt được `UnicodeDecodeError`. Tôi tái hiện với EOF nằm giữa ký tự tiếng Việt. Đây là trường hợp phù hợp với log ghi `ensure_ascii=False` tại `:438`.

**[Vừa] Phạm vi bỏ qua quá rộng.** `run_eval.py:291–294` bỏ qua mọi dòng JSON hỏng, kể cả giữa file. Hỏng nội dung ở giữa không phải tình huống “partial last line”; nên báo lỗi rõ thay vì tiếp tục như resume bình thường.

**Các artifact mặc định còn lại đạt:** manifest tái lập chính xác; câu/key/phiếu model trong workbook khớp nguồn; bảo vệ ghi đè hoạt động theo logic hiện tại. Không thấy bug chọn trùng câu hoặc rò dữ liệu vòng 1.

## Thay đổi ưu tiên

1. **Sửa resume** cho EOF không có newline và EOF giữa ký tự UTF-8; không bỏ qua vô điều kiện lỗi giữa file.
2. **Bổ sung tập đáp án vòng 2, trạng thái đề cuối cùng và quy trình phân xử**, rồi chốt định nghĩa endpoint, κ, missing/unknown và thay đổi sau reveal.
3. **Chốt lại n ngẫu nhiên trước duyệt**: ưu tiên 385 cho mục tiêu ±5 điểm; 200 nếu chấp nhận CI rộng hơn. Cập nhật draw, bảng pool và mẫu số phân tích cùng lúc.
4. **Đổi tên/giải thích xác suất theo bước**, giới hạn suy rộng ở 1.658 câu đã eval; phân biệt pool còn lại với nhóm ưu tiên đầy đủ.
5. **Chốt quy tắc giao file**: cả hai người nộp vòng 1 trước reveal; lưu bản đã nộp bất biến và phiên bản input/draw để tái lập.
# VM14K: self-contradictory answer keys

Same normalised question AND same normalised option set, but a different option is marked correct.

Normalisation: dedup_utils.normalize_vietnamese (authors' code)
Line numbers refer to data-processed-shuffled0.jsonl.

Groups: 67   Rows: 152

### Group 1 — topic: Urology, Gastroenterology
Q: Thăm trực tràng có thể phát hiện các thương tổn ngoài hậu môn – trực tràng sau:
Options (shared set): ['Tiền liệt tuyến ở nam', 'Tử cung và âm đạo nữ', 'Túi tinh và ống dẫn tinh ở nam', 'Tất cả đều đúng']
  line     47 | Medium      | id d2152e9da25b4f50bf3363f15cae5c06 | D -> Tất cả đều đúng
  line    672 | Medium      | id 7f48222b59054aae908619afe77c17a0 | A -> Tiền liệt tuyến ở nam

### Group 2 — topic: Urology, Surgery, Gastroenterology
Q: Thăm trực tràng có thể phát hiện các thương tổn ngoài hậu môn – trực tràng nào sau đây?
Options (shared set): ['Tiền liệt tuyến ở nam', 'Tử cung và âm đạo nữ', 'Túi tinh và ống dẫn tinh ở nam', 'Tất cả đều đúng']
  line     51 | Medium      | id 8b9c685693c044978144079f5b488ec7 | D -> Tất cả đều đúng
  line    830 | Medium      | id cac6b7691ccc41529ac6fabeb0b605cf | A -> Tiền liệt tuyến ở nam

### Group 3 — topic: Urology
Q: TC điển hình nhất của sỏi bàng quang niệu đạo
Options (shared set): ['đái buốt', 'đái rắt', 'đái mủ', 'đái tắc']
  line     56 | Medium      | id 2d01b27a6ea74ab9a216efba9ae953ac | D -> đái tắc
  line   1031 | Easy        | id 7154d7fd680948228aa6484b62c5c124 | B -> đái rắt

### Group 4 — topic: Nephrology, Urology
Q: Nguyên nhân gây vô niệu bao gồm : Chọn câu sai :
Options (shared set): ['Suy thận cấp', 'Sỏi kẹt niệu đạo', 'Hoại tử vỏ thận hai bên', 'Viêm ống thận cấp.']
  line    176 | Medium      | id 73f9b056cb6c4895b69dc25fb6712424 | B -> Sỏi kẹt niệu đạo
  line  11999 | Medium      | id 76c471b2d3274eb3bb8a9e1cd1df7cc0 | D -> Viêm ống thận cấp.

### Group 5 — topic: Urology, Infectious Diseases
Q: hai xét nghiệm nào dưới đây được sử dụng chẩn đoán viêm niệu đạo do lậu và không do lậu:
Options (shared set): ['Nhuộm gram và nuôi cấy', 'Soi tươi PCR', 'Soi tươi và nhuộm gram', 'Soi tươi và nuôi cấy']
  line    196 | Challenging | id 32acc6b9ceb6419284deb9c2f5b488f2 | A -> Nhuộm gram và nuôi cấy
  line   1674 | Challenging | id f440aef0b8f142b7a3aebc42e9a79dff | C -> Soi tươi và nhuộm gram
  line  10425 | Medium      | id bcd46782b6064aa19247e4568803cf62 | C -> Soi tươi và nhuộm gram

### Group 6 — topic: Urology, Oncology
Q: Ung thư biểu mô tuyến tiền liệt nếu không được tầm soát, phát hiện sớm sẽ tiến triển âm thầm và có thể bệnh chỉ được phát hiện, xác định khi tế bào u đã lan rộng hay di căn đến mô và cơ quan kế cận. Các mô và cơ quan kế cận thường gặp trong ung thư tuyến tiền liệt thường gặp nhất là gì?
Options (shared set): ['Xâm nhập mô của tuyến tiền liệt, lan rộng đến túi tinh, đại tràng, bàng quang', 'Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, đại tràng, bàng quang', 'Xâm nhập mô tuyến tiền liệt, lan rộng đến túi tinh, đại tràng, cột sống cùng cụt', 'Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, trực tràng, cột sống cùng cụt.']
  line    289 | Medium      | id cedee93db5ad4f5fb6b941bba7f41658 | D -> Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, trực tràng, cột sống cùng cụt.
  line   2015 | Medium      | id 76336bc395b34caf82851e45590e68b4 | B -> Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, đại tràng, bàng quang

### Group 7 — topic: Urology, Oncology, Pathology
Q: Ung thư biểu mô tế bào thận xâm lấn theo kiểu?
Options (shared set): ['Gieo hạt', 'Nẩy chồi', 'Chia nhánh', 'Vết dầu loang']
  line    298 | Medium      | id 08531b190cb54171a26246bad79d9070 | B -> Nẩy chồi
  line   2155 | Medium      | id eaec542c585c4f89836d26c47d08b8b4 | C -> Chia nhánh

### Group 8 — topic: Oncology, Urology
Q: Hút thuốc lá làm tăng nguy cơ tử vong của loại UT nào do làm tăng nguy cơ phát triển ác tính của loại UT này?
Options (shared set): ['UT gan', 'UT tuyến thượng thận', 'UT tiền liệt tuyến', 'UT tụy']
  line    301 | Medium      | id bf58f600f30c456ba73604bfbe613fe5 | D -> UT tụy
  line   2299 | Medium      | id b441984a74c844988652e0b6f2df8f47 | C -> UT tiền liệt tuyến

### Group 9 — topic: Nephrology, Pediatrics, Urology
Q: Thời gian xuất hiện của trung thận:
Options (shared set): ['Cuối tuần thứ 3.', 'Cuối tuần thứ 4.', 'Cuối tuần thứ 5.', 'Cuối tuần thứ 6.']
  line    307 | Easy        | id 5f5c7174642f4d69878c48127234c59b | B -> Cuối tuần thứ 4.
  line  11701 | Easy        | id d7becbe14f9a4f81b1c9f01f19001a37 | A -> Cuối tuần thứ 3.

### Group 10 — topic: Endocrinology, Gastroenterology
Q: TB thực hiện chức năng nội tiết?
Options (shared set): ['TB G', 'TB thành', 'TB D', 'TB chính']
  line    759 | Easy        | id 58fb5401cd394be9876864e3a546e3d8 | A -> TB G
  line   6418 | Medium      | id cfe53b1d93ec4eaf94271bbfbcee82f9 | C -> TB D

### Group 11 — topic: Endocrinology, Gastroenterology
Q: TB nào ở dạ dày là TB nội tiết:
Options (shared set): ['TB chính', 'TB nhầy', 'TB G', 'TB D']
  line    844 | Easy        | id 7189980ee4d94e14a3b5f17b7a9737df | C -> TB G
  line   6420 | Medium      | id bf85f120761f49158b1409970090aafd | D -> TB D

### Group 12 — topic: Gastroenterology, Endocrinology
Q: Rối loạn tiêu hoá nguyên nhân ngoài ruột dẫn đến giảm hấp thu gồm, trừ
Options (shared set): ['Suy thận', 'Suy giáp', 'Suy gan', 'Suy tuỵ']
  line    857 | Medium      | id 39b635d7fb20449191857daf6526817c | A -> Suy thận
  line   6423 | Medium      | id 06ae20f1c45947ef8046b064e676efa7 | B -> Suy giáp

### Group 13 — topic: Gastroenterology, Hematology
Q: Gan chứa bao nhiêu máu?
Options (shared set): ['100-200 g', '300-500 g', '600-700 g', '800-900 g']
  line    923 | Easy        | id d44ffd9e328f476ca18d7e406156300e | D -> 800-900 g
  line  11817 | Easy        | id b4e9050f941d46ffaba52b92880e37ba | B -> 300-500 g

### Group 14 — topic: Endocrinology, Gastroenterology
Q: Ý nghĩa tốt nhất cho từ được gạch chân là gì? Có sự gia tăng 'tạo đường mới' ở gan, hấp thụ glucose nhanh chóng qua đường tiêu hóa và có thể tăng kháng insulin.
Options (shared set): ['sản xuất đường từ glycogen', 'chức năng tuyến giáp quá cao', 'một lượng chất béo bất thường trong máu', 'liên quan đến lượng đường trong máu']
  line   1025 | Medium      | id 04f2f9c846cd42e4937ef632b5ee4bee | D -> liên quan đến lượng đường trong máu
  line   6087 | Medium      | id 408cb03727c94d24ad88e5dab103aa60 | A -> sản xuất đường từ glycogen

### Group 15 — topic: Pathology, Gastroenterology
Q: Một bệnh nhân vào nội soi thực quản dạ dày, sau khi được sinh thiết thực quản ở 1/3 dưới làm mô bệnh học, kết quả cho thấy biểu mô thực quản được phủ bởi biểu mô hình trụ, các tuyến tế bào hình trụ, nhân nhỏ tròn đều, chất nhiễm sắc mịn, tạo hình ống tuyến. Kết luận nào sau đây là đúng nhất?
Options (shared set): ['dị sản biểu mô thực quản', 'phì đại biểu mô thực quản', 'loạn sản biểu mô thực quản', 'teo biểu mô thực quản']
  line   1315 | Challenging | id 8e560bf180564a129dac549cd8da3dbc | A -> dị sản biểu mô thực quản
  line   2007 | Challenging | id 5b09855d43114b9da6f037000ab36694 | C -> Loạn sản biểu mô thực quản

### Group 16 — topic: Infectious Diseases, Pulmonology, Nephrology, Gastroenterology
Q: Xét nghiệm nào sau đây giúp đánh giá mức độ bệnh COVID-19?
Options (shared set): ['Công thức máu', 'Siêu âm phổi', 'Tets nhanh SARS-CoV-2', 'Chức năng gan, thận']
  line   1371 | Medium      | id 2205accd66ee4dc28eb62cd9f8162550 | D -> Chức năng gan, thận
  line   5039 | Medium      | id f3f71dfe458144edbd0f01db6d5b4fd2 | D -> Chức năng gan, thận
  line   5079 | Medium      | id c30e606ebe954fee94388a87a85d2f29 | D -> Chức năng gan, thận
  line   5163 | Medium      | id c716f9f3529e4cc08ea4790f256e44eb | B -> Siêu âm phổi

### Group 17 — topic: Oncology, Gastroenterology, Pathology
Q: Ung thư biểu mô tuyến đại tràng có tiên lượng xấu nhất thuộc loại nào?
Options (shared set): ['Biệt hoá cao .', 'Biệt hoá vừa .', 'Biệt hoá thấp .', 'Loại không biệt hoá']
  line   1577 | Medium      | id d2ec8e0f269045c19243478369450383 | D -> Loại không biệt hoá
  line   1610 | Medium      | id a4069d38abad4dfd869b6c921ff5ebcc | A -> Loại không biệt hóa
  line   1620 | Medium      | id 04b91faf2f18436ea1cc01f5dd64520a | D -> Loại không biệt hoá
  line  10583 | Medium      | id 090215da82c04b6b86f282afbaf5d2cd | C -> Biệt hoá thấp .

### Group 18 — topic: Geriatrics, Gastroenterology
Q: Sau 60 tuổi, quá trình hấp thu các chất bị ảnh hưởng , NGOẠI TRỪ
Options (shared set): ['Hấp thu lactose, mannitol , vit B12', 'Giảm hấp thu vitD, axit Folic', 'Giảm hấp thu axit béo và Cholesterol', 'Giảm hấp thu Calci, tăng hấp thu Đồng và Kẽm']
  line   1671 | Medium      | id f52a452b322148fc8f07140ebff66aea | D -> Giảm hấp thu Calci, tăng hấp thu Đồng và Kẽm
  line  10750 | Medium      | id 741a5a8913774f979acc29a0295efe50 | A -> Hấp thu lactose, mannitol , vit B12

### Group 19 — topic: Endocrinology, Gastroenterology
Q: Nhiễm độc giáp tác động đến tiêu hóa như thế nào?
Options (shared set): ['Nôn, vàng da, táo bón', 'Ăn nhiều gầy nhiều, tiêu chảy', 'Nôn, tiêu chảy, gan to', 'Nôn, tiêu chảy, vàng da']
  line   1675 | Medium      | id f6d2cc6fb30647a6bd038dad445a2dd2 | B -> Ăn nhiều gầy nhiều, tiêu chảy
  line   6839 | Medium      | id 89fe1755e9484a16af88cffc861e6cc4 | D -> Nôn, tiêu chảy, vàng da

### Group 20 — topic: Infectious Diseases, Gastroenterology
Q: đây là gì
Options (shared set): ['trứng giun tóc', 'trứng giun đũa', 'trứng giun móc', 'trứng giun kim']
  line   1767 | Medium      | id 76c400d1a93d41698b8f1161cc79b80f | A -> trứng giun tóc
  line   1768 | Medium      | id 2e08db5f2bd2432aac2648f54a897879 | A -> trứng giun đũa
  line   1769 | Medium      | id a36e2051ec994a44b7bab48087fa200c | B -> trứng giun móc

### Group 21 — topic: Infectious Diseases, Gastroenterology
Q: Đây là gì?
Options (shared set): ['Trứng sán lá ruột lớn', 'Trứng sán dây', 'Trứng sán lá gan nhỏ', 'Trứng sán lá phổi']
  line   1772 | Medium      | id 46f15e95ab5e4d1a87e44f75b3e8aacb | A -> Trứng sán lá ruột lớn
  line   1773 | Medium      | id e32fa65252a048b681a615fad3308648 | A -> Trứng sán lá gan nhỏ

### Group 22 — topic: Endocrinology, Gastroenterology
Q: Nhóm cơ chất nào sau đây có thể được cơ sử dụng để tổng hợp glucose
Options (shared set): ['Acid palmitic, acid aspartic, glycerol', 'Lactat, acid palmitic, acid stearic', 'Glycin, glycerol, mannose', 'AcetylCoA, glycerol, frutose']
  line   1852 | Medium      | id 55b9d99aad8547f1924bfd93fcb1eb15 | C -> Glycin, glycerol, mannose
  line   6976 | Medium      | id 7ecc2f84cf2a46c58dee83c2aaa48992 | A -> Acid palmitic, acid aspartic, glycerol

### Group 23 — topic: Endocrinology, Gastroenterology
Q: Nguyên liệu để tổng hợp glycogen là:
Options (shared set): ['Glucose dưới dạng UDP-G', 'Glucose dưới dạng G6P', 'Glucose dưới dạng tự do', 'Glucose dưới dạng G1P']
  line   1854 | Easy        | id f39860007f5245828140a02ba145f75a | A -> Glucose dưới dạng UDP-G
  line   6349 | Easy        | id 226b0e5d70df42d290e9f78e6b96be18 | D -> Glucose dưới dạng G1P

### Group 24 — topic: Endocrinology, Gastroenterology, Nephrology
Q: Trong trường hợp rối loạn chuyển hóa, các chất cetonic tăng cao trong máu và xuất hiện nước tiểu làm nước tiểu có?
Options (shared set): ['Hồng cầu', 'Sắc tố mật dương tính', 'Albumin niệu tăng', 'Protein']
  line   1922 | Challenging | id b0e48ac276a74892ab682f015636fb47 | D -> Protein
  line   6174 | Medium      | id 3034aa58bc5d4fd283c36a94abc7cb77 | B -> Sắc tố mật dương tính

### Group 25 — topic: Endocrinology, Gastroenterology
Q: Chọn tổ hợp đúng. 1. Tổng hợp acid béo ngoài bào tương chỉ tổng hợp được những aicd béo mạch ngắn. 2. Nguyên liệu tổng hợp acid béo ngoài bào tương là acetylCoA có nguồn gốc tại chỗ 3. Tổng hợp acid béo trong ty thể chất hoạt hóa là HSCoA, không cần có sự tham gia của phức hợp acid béo syntetase 4. Ngoài bào tương phải tạo malonylCoA
Options (shared set): ['1,2,3', '2,3,4', '1,2,4', '1,3,4']
  line   1925 | Challenging | id 23779a51e431493e80cc6c74fb3f1a4b | B -> 2,3,4
  line   6175 | Medium      | id c77f151506d141238f7c99c218521a74 | D -> 1,3,4

### Group 26 — topic: Endocrinology, Gastroenterology
Q: Nhóm cơ chất nào sau đây có thể được sử dụng để tổng hợp glucose?
Options (shared set): ['Acid palmitic, acid aspartic, glycerol', 'Lactat, acid palmitic, acid stearic', 'Glycin, glycertol, mannose', 'Acetyl CoA, glycerol, frutose']
  line   1944 | Challenging | id 5fd1e29e4fd348fa825f6bd40994ddd3 | C -> Glycin, glycertol, mannose
  line   6176 | Easy        | id b618386cbdc2482799c7a2537341474c | A -> Acid palmitic, acid aspartic, glycerol

### Group 27 — topic: Gastroenterology, Pathology
Q: Dưới đây là hình ảnh vi thể của xơ gan. Mũi tên đen chỉ tổn thương gì?
Options (shared set): ['Mạch máu tăng sinh', 'Ống mật tăng sinh', 'Xâm nhiễm viêm mạn tính', 'Tăng sinh tế bào sợi']
  line   2097 | Challenging | id d848f95395014a1084b355e51e258f94 | B -> Ống mật tăng sinh
  line   2098 | Challenging | id 534b8a8b19ab4dc896dcc3f20219ec2c | A -> Mạch máu tăng sinh
  line   2099 | Challenging | id 724d7282fa254bde9957e9c35a747b2d | C -> Xâm nhiễm viêm mạn tính

### Group 28 — topic: Gastroenterology, Pathology
Q: Dưới đây là hình ảnh vi thể của ổ loét dạ dày mạn tính. Lớp được chỉ ra trong hình (mũi tên) là lớp nào?
Options (shared set): ['Hoại tử tơ huyết', 'Phù dạng tơ huyết', 'Tổ chức hạt', 'Tổ chức xơ']
  line   2109 | Challenging | id 511e85d8c3ee4cc08ede89422f28a0ae | A -> Hoại tử tơ huyết
  line   2110 | Challenging | id 180756a0c06544b6a8a0840cfc0ef82f | C -> Tổ chức hạt

### Group 29 — topic: Obstetrics and Gynecology
Q: Chọn câu trả lời đúng về chửa trứng:
Options (shared set): ['Chửa trứng toàn phần là do sự kết hợp giữa 2 tinh trùng với một tế bào noãn bình thường.', 'Chửa trứng toàn phần là do sự thụ tinh của một noãn không nhân với một tinh trùng chứa nhiễm sắc thể X nhân đôi', 'Nhiễm sắc đồ XX của chửa trứng toàn phần có nguồn gốc 50% từ cha và 50% từ mẹ.', '94% chửa trứng toàn phần có nhiễm sác thể giới tính là XY.']
  line   2770 | Medium      | id 258718715ea74c95bd729a8c2c589504 | B -> Chửa trứng toàn phần là do sự thụ tinh của một noãn không nhân với một tinh trùng chứa nhiễm sắc thể X nhân đôi
  line   9441 | Easy        | id beb1ca6b89d84d568c8e4d156a352d54 | B -> Chửa trứng toàn phần là do sự thụ tinh của một noãn không nhân với một tinh trùng chứa nhiễm sắc thể X nhân đôi
  line  11557 | Medium      | id 38652386e8c7403badbe465af5722ece | A -> Chửa trứng toàn phần là do sự kết hợp giữa 2 tinh trùng với một tế bào noãn bình thường.

### Group 30 — topic: Obstetrics and Gynecology
Q: Vỡ tử cung ở tử cung có sẹo mổ cũ khác với không có sẹo ở điểm nào, chọn câu đúng:
Options (shared set): ['Thường chảy máu nhiều hơn', 'Kèm gây tổn thương các tạng lân cận', 'Không có triệu chứng dọa vỡ trước đó', 'Có triệu chứng dọa vỡ trước đó']
  line   2850 | Medium      | id 6b8c025ecc1a41babce92fa95f440f3c | C -> Không có triệu chứng dọa vỡ trước đó
  line  11949 | Medium      | id bff7d2ccad7d44df8103631c2c1c610e | D -> Có triệu chứng dọa vỡ trước đó

### Group 31 — topic: Obstetrics and Gynecology
Q: CHẢY MÁU BẤT THƯỜNG TỬ CUNG Rong kinh:
Options (shared set): ['Ra máu có chu kỳ', 'Kéo dài trên 7 ngày', 'Gồm có rong kinh cơ năng và rong kinh thực thể', 'Rong kinh là triệu chứng không phải là bệnh']
  line   3185 | Easy        | id ced9f1b8285e47feacbae114d1e7ead6 | B -> Kéo dài trên 7 ngày
  line   7883 | Easy        | id dab0c7fd10fe4d6daa0ce606834d4b51 | A -> Ra máu có chu kỳ

### Group 32 — topic: Obstetrics and Gynecology
Q: Dây chằng không tham gia giữ tử cung tại chỗ:
Options (shared set): ['Dây chằng tròn.', 'Dây chằng rộng.', 'Dây chằng thắt lưng buồng trứng.', 'Dây chằng tử cung cùng.']
  line   3277 | Medium      | id 960805aeec28484abe928083f3504bab | C -> Dây chằng thắt lưng buồng trứng.
  line  11956 | Easy        | id 3e5c725c89ee48158e2d883e78a27470 | B -> Dây chằng rộng.

### Group 33 — topic: Obstetrics and Gynecology
Q: Sau khi hút trứng, yếu tố quan trọng nhất để tiên l¬ượng bệnh là:
Options (shared set): ['Diễn tiến nồng độ hCG.', 'Hình ảnh mô học của mô trứng.', 'Nồng độ pregnandiol.', 'Nồng độ estriol.']
  line   3417 | Challenging | id 33c851fcd74740f0baa8ecc7fd3de6c9 | B -> Hình ảnh mô học của mô trứng.
  line   3895 | Challenging | id bd6026fce0644374bf40b583571b7978 | A -> Diễn tiến nồng độ hCG.

### Group 34 — topic: Obstetrics and Gynecology
Q: Theo vị trí giải phẩu, loại rau tiền đạo nào sau đây không có khả năng sanh đường âm đạo?
Options (shared set): ['Rau bám thấp', 'Rau bám bên', 'Rau bám mép', 'Rau bám bán trung tâm']
  line   3428 | Medium      | id 30db384134b7421498b7ca5e1c084478 | D -> Rau bám bán trung tâm
  line  11913 | Easy        | id d58c7632fc9d48199133bf6a8cc787dc | A -> Rau bám thấp

### Group 35 — topic: Obstetrics and Gynecology, Endocrinology
Q: U xơ tử cung có liên quan đến hormone sinh dục nên . . .:
Options (shared set): ['U xơ tử cung chỉ lớn lên khi chu kỳ có rụng trứng', 'U xơ tử cung sẽ nhỏ đi khi bệnh nhân bị phẫu thuật cắt 2 buồng trứng', 'U xơ tử cung sẽ tăng kích thước ở những bệnh nhân có chu kỳ kinh đều hơn là bệnh nhân có chu kỳ kinh không đều', 'Khi có thai, u xơ tử cung có xu hướng nhỏ lại']
  line   3566 | Medium      | id 566812ae558c47208c08c1b24c55533d | B -> U xơ tử cung sẽ nhỏ đi khi bệnh nhân bị phẫu thuật cắt 2 buồng trứng
  line   7077 | Medium      | id 1ed6c7fd09d34c20981286d6567d2386 | A -> U xơ tử cung chỉ lớn lên khi chu kỳ có rụng trứng

### Group 36 — topic: Obstetrics and Gynecology, Hematology
Q: Trên lâm sàng, rau tiền đạo chảy máu nhẹ là khi lượng máu của mẹ mất:
Options (shared set): ['<10% thể tích máu tuần hoàn', '<15% thể tích máu tuần hoàn', '<20% thể tích máu tuần hoàn', '<25% thể tích máu tuần hoàn']
  line   3613 | Medium      | id a83cb7446f9d407781b883866265f6af | B -> <15% thể tích máu tuần hoàn
  line  11799 | Medium      | id 9686c91f59d04872ab45e33768c30107 | A -> <10% thể tích máu tuần hoàn

### Group 37 — topic: Obstetrics and Gynecology, Infectious Diseases, Endocrinology
Q: Các yếu tố sau là nguy cơ gây viêm âm đạo-cổ tử cung, ngoại trừ:
Options (shared set): ['Dùng kháng sinh nhóm Beta-lactam', 'Dùng kháng sinh nhóm Tetracyclin', 'Dùng kháng sinh nhóm Quinolones', 'Bị đái tháo đường']
  line   3722 | Challenging | id 95ee81d4e95f42cfb18f48988bba45c4 | A -> Dùng kháng sinh nhóm Beta-lactam
  line   6190 | Medium      | id 98b8bcf5a5594f59a5f11d6967f184a7 | C -> Dùng kháng sinh nhóm Quinolones

### Group 38 — topic: Obstetrics and Gynecology, Pathology
Q: Đặc điểm giải phẫu bệnh của một u buồng trứng được mô tả như sau: U có dạng nang, đường kính lớn nhất 15cm, có hình nhiều thùy, diện cắt u xẹp, có vách ngăn, không tạo nhú; vi thể vách nang phủ bởi biểu mô vuông hay trụ thấp. Chẩn đoán nào phù hợp cho trường hợp này?
Options (shared set): ['U thanh dịch lành tính', 'U nhầy lành tính', 'U thanh dịch giáp biên ác', 'U nhầy giáp biên ác']
  line   3888 | Challenging | id 880d6f41c5e141119799f95346afce72 | B -> U nhầy lành tính
  line   8080 | Hard        | id 8f04078a1c5f4f41967053660fb0ded6 | A -> U thanh dịch lành tính

### Group 39 — topic: Obstetrics and Gynecology, Pulmonology
Q: Điều nào sau đây thường là ảnh hưởng của việc mang thai đối với bệnh nhân hen?
Options (shared set): ['Sự gia tăng các biến chứng của mẹ và con khi sinh', 'Trầm trọng hơn các triệu chứng', 'Cải thiện chức năng hô hấp', 'Giảm triệu chứng hen suyễn']
  line   4009 | Medium      | id 70049746aea1478eba5a721962ed4929 | B -> Trầm trọng hơn các triệu chứng
  line   4612 | Medium      | id 560273f725b34a6482eaa503d66349a1 | A -> Sự gia tăng các biến chứng của mẹ và con khi sinh

### Group 40 — topic: Obstetrics and Gynecology, Radiology
Q: Chụp X quang bụng không chuẩn bị có thể phát hiện được u nang:
Options (shared set): ['U nang nước', 'U nang nhầy', 'U nang bì', 'Cả 3 loại u nang trên']
  line   4054 | Medium      | id de12ad67647d41918f80e5abe1bd16eb | C -> U nang bì
  line   7964 | Medium      | id 9b4af78f3ee0441b9d38fe9f79edd98c | C -> U nang bì
  line  11911 | Easy        | id 96141447043542d5a290447c05465366 | D -> Cả 3 loại u nang trên

### Group 41 — topic: Obstetrics and Gynecology, Surgery
Q: Nói về điều trị u xơ tử cung:
Options (shared set): ['Chỉ có chỉ định phẫu thuật khi bệnh nhân đã vào giai đoạn tiền mãn kinh', 'Nếu có chỉ định phẫu thuật "cắt tử cung toàn phần" là phương pháp ưu tiên được chọn lựa', 'Chỉ bóc nhân xơ ở những bệnh nhân bị vô sinh nguyên phát', 'Tất cả đều sai']
  line   4126 | Challenging | id b276cc9b9d6947d188d6709f540ef7d7 | D -> Tất cả đều sai
  line   9642 | Medium      | id 78eeaa19e8bf44c49604f9c22a7089fb | B -> Nếu có chỉ định phẫu thuật "cắt tử cung toàn phần" là phương pháp ưu tiên được chọn lựa

### Group 42 — topic: Toxicology, Environmental Health
Q: Trong tự nhiên , Co không được tạo thành từ quá trình nào sau đây ?
Options (shared set): ['Hoạt động núi lửa', 'Phản ứng quang hoá', 'Cháy nổ hầm mỏ', 'Hàn hồ quang điện']
  line   4531 | Easy        | id aac1e3e4fed84a0cb4cb3ce37ee7e856 | B -> Phản ứng quang hoá
  line   4544 | Easy        | id eb33d70e519b4877ad96a406707fdd5b | D -> Hàn hồ quang điện
  line  11239 | Medium      | id 52cd9c1633264658941ef04317b3ea90 | B -> Phản ứng quang hoá
  line  11252 | Easy        | id 9c110b1dfb6343638e7cafca86a0a58a | D -> Hàn hồ quang điện

### Group 43 — topic: Toxicology, Environmental Health
Q: Asen nào làm thuốc trừ sâu?
Options (shared set): ['Asenat đồng crôm hóa', 'Asenat hidro chì', 'Asenua gali', 'Axetoasenit']
  line   4538 | Easy        | id afda36c2732540378e7216e6b294b40e | A -> Asenat đồng crôm hóa
  line   9624 | Medium      | id cefca2bbbd0840c483f25f9ced7d5ccd | B -> Asenat hidro chì
  line  11246 | Easy        | id 2b73ba4541ad43e089dc5f06ea3789d1 | A -> Asenat đồng crôm hóa

### Group 44 — topic: Toxicology, Environmental Health
Q: Trong công nghiệp, CO hiện diện ở đâu ?
Options (shared set): ['Nhà máy lò kỹ nghệ', 'Khói thải từ xe cộ', 'A và B đều đúng', 'A sai và B đúng']
  line   4546 | Easy        | id 2e4b6520025a4202a14ca144f69f00f4 | C -> A và B đều đúng
  line   8938 | Easy        | id 9a80ef5cd2d043eab20767026dea6ad3 | A -> Nhà máy lò kỹ nghệ
  line  11254 | Easy        | id 100a9bdde8c64f3b921f96d21ffe622c | C -> A và B đều đúng

### Group 45 — topic: Pulmonology, Radiology
Q: Các kỹ thuật phát hiện tràn dịch màng phổi tự do, theo độ nhạy giảm dần
Options (shared set): ['Siêu âm khoang màng phổi- phim phổi đứng , chụp nghiêng - phim phổi nằm nghiêng chụp thẳng, tia x chiếu ngang', 'Phim phổi đứng, chụp nghiêng – siêu âm khoang màng phổi - phim phổi đứng - chụp thẳng', 'Siêu âm khoang màng phổi - phim phổi nằm nghiêng chụp thẳng, tia Xchiếu ngang - phim phổi đứng - chụp nghiêng', 'Phim phổi đứng, chụp nghiêng - phim phổi nằm nghiêng chụp thẳng, tia X chiếu ngang - phim phổi đứng, chụp thẳng – siêu âm khoang màng phổi']
  line   4712 | Medium      | id fa71cdf70f0b47c7b6571ed8d240580e | C -> Siêu âm khoang màng phổi - phim phổi nằm nghiêng chụp thẳng, tia Xchiếu ngang - phim phổi đứng - chụp nghiêng
  line   4844 | Medium      | id 5a6e4b9d40114f608f404738c5e47f73 | C -> Siêu âm khoang màng phổi- phim phổi đứng - chụp nghiêng - phim phổi nằm nghiêng chụp thẳng, tia x chiếu ngang
  line   5599 | Medium      | id ac1c35aeb3794185a6e47ee058fbabb5 | A -> Siêu âm khoang màng phổi- phim phổi đứng , chụp nghiêng - phim phổi nằm nghiêng chụp thẳng, tia x chiếu ngang

### Group 46 — topic: Pulmonology, Radiology
Q: Dấu hiệu X quang nào sau đây KHÔNG phù hợp với áp xe phổi
Options (shared set): ['Thành dày, mặt trong không đều', 'Hình ảnh mức hơi dịch trong hang', 'Hình ảnh viêm phổi quanh hang', 'Thành hang mỏng, mặt trong đều']
  line   4736 | Medium      | id 05b642bb70f24ff3af8a1b96f10c992e | A -> Thành dày, mặt trong không đều
  line   4849 | Medium      | id 1a062ddbc7574533a7145c24c21a9aa3 | D -> Thành hang mỏng, mặt trong đều
  line   5624 | Medium      | id ade0decacd9041cab9d74a0bc7445bfe | A -> Thành dày, mặt trong không đều

### Group 47 — topic: Pulmonology, Infectious Diseases, Radiology
Q: Ý nào sau đây đúng khi nói về hình ảnh lao xơ hang trên phim chụp XQ tim phổi:
Options (shared set): ['Là tổn thương do vi khuẩn Lao mà một phần phổi đã khư trú và tạo thành hình hang', 'Do lao xơ tiến triển thành, các tổn thương lao biến thành hang lao do quá trình khu trú tổn thương của cơ thể', 'Do lao nốt tiến triển thành, các tổn thương lao biến thành hang lao do quá trình bã đậu hóa', 'Do lao xơ tiến triển thành']
  line   4744 | Medium      | id 6945f8d1e54249ba97c9a6815c2431bb | C -> Do lao nốt tiến triển thành, các tổn thương lao biến thành hang lao do quá trình bã đậu hóa
  line   4858 | Medium      | id 3eca8b10d2344f1a8bf930a2c1ad363a | A -> Là tổn thương do vi khuẩn Lao mà một phần phổi đã khư trú và tạo thành hình hang
  line   5631 | Medium      | id 6b8e03aba79a45499b8784a646c3015e | C -> Do lao nốt tiến triển thành, các tổn thương lao biến thành hang lao do quá trình bã đậu hóa

### Group 48 — topic: Pulmonology
Q: pH = 7.36, HCO3- = 25mmol/l, PaCo2 = 48 mmHg, kết quả nào sau là đúng
Options (shared set): ['Toan hô hấp mạn', 'Toan hô hấp cấp', 'Toan hỗn hợp', 'Toan đơn thuần']
  line   5152 | Medium      | id 8a3564e6ead04c2a9571a3f34be84017 | B -> Toan hô hấp cấp
  line   5802 | Medium      | id 9928e8e84e7c4e018c00f16f62456eb8 | C -> Toan hỗn hợp

### Group 49 — topic: Oncology, Pulmonology
Q: Hình ảnh dưới đây minh họa một trong các thể ung thư phổi phân chia theo hình ảnh đại thể. Đó là thể nào, chọn câu trả lời đúng nhất:
Options (shared set): ['Thể ngoại vi', 'Thể trung tâm', 'Thể lan tràn', 'Thể hỗn hợp']
  line   5869 | Medium      | id 40f195bb763e40f589014308f3afef53 | B -> Thể trung tâm
  line   5870 | Medium      | id 1826cfccfa5b40629951cae9a9b26ed6 | A -> Thể ngoại vi

### Group 50 — topic: Endocrinology, Nephrology
Q: Một trong các câu sau đây liên quan đến sự cân bằng kali trong bệnh tiểu đường nhiễm ceton-acid (DKA) là đúng…
Options (shared set): ['Khoảng 20% tổng số kali cơ thể là ở mạch máu.', 'Tăng kali máu trong DKA ban đầu là phổ biến.', 'Điều trị ban đầu DKA thường gây hạ kali huyết.', 'Nồng độ kali trong huyết thanh ban đầu > 3,3 mEq / L và <5,0 mEq / L, giảm bớt sự cần thiết phải bổ sung kali.']
  line   6093 | Medium      | id 3d98af5133f94e7b8882e79e0825e4be | C -> Điều trị ban đầu DKA thường gây hạ kali huyết.
  line  11996 | Medium      | id 8f7e6e302daf476c89447b3db31ed640 | B -> Tăng kali máu trong DKA ban đầu là phổ biến.

### Group 51 — topic: Endocrinology
Q: Ý nghĩa tốt nhất cho từ được gạch chân là gì? 'Cường giáp' thường liên quan đến việc kiểm soát đường huyết kém đi và tăng nhu cầu insulin.
Options (shared set): ['chức năng tuyến giáp bình thường', 'chức năng tuyến giáp quá cao', 'một lượng chất béo bất thường trong máu', 'liên quan đến lượng đường trong máu']
  line   6437 | Medium      | id b98e35a36e874b3b8cc6131833be5f80 | B -> chức năng tuyến giáp quá cao
  line   6438 | Medium      | id 90f27d2f9fdb4a7d929ade53df033e85 | D -> liên quan đến lượng đường trong máu

### Group 52 — topic: Endocrinology, Obstetrics and Gynecology
Q: Tác dụng của estrogen lên tuyến cổ tử cung làm tăng bài tiết:
Options (shared set): ['Dịch nhày kiềm.', 'Dịch nhày loãng, mỏng.', 'Dịch nhày quánh, kiềm.', 'Dịch nhày loãng, kiềm.']
  line   6571 | Medium      | id 1eeff47ead10426998d56518a6706257 | B -> Dịch nhày loãng, mỏng.
  line   6714 | Medium      | id 1ded77d992f14b7f912fa85f98720eb4 | C -> Dịch nhày quánh, kiềm.

### Group 53 — topic: Endocrinology
Q: Các yếu tố sau đây đều làm tăng bài tiết T3-T4, trừ:
Options (shared set): ['Nồng độ iod vô cơ trong tuyến giáp cao.', 'Nồng độ TSH trong máu cao.', 'Nồng độ iod hữu cơ trong máu giảm.', 'Khi bị lạnh hoặc stress.']
  line   6581 | Medium      | id c06671caa0a64e9c867ec75555bfb2cb | A -> Nồng độ iod vô cơ trong tuyến giáp cao.
  line   6681 | Medium      | id 7a89afcdd2b642e98137415abe523d49 | C -> Nồng độ iod hữu cơ trong máu giảm.

### Group 54 — topic: Nephrology, Endocrinology
Q: 3.74. Trong thí nghiệm về hiện tượng thẩm thấu, nếu nồng độ nước đường trong ống nhỏ hơn trong chậu thì mực nước đường trong ống sẽ cao hơn trong chậu. (Đúng/Sai)
Options (shared set): ['Đúng', 'Sai']
  line   6645 | Medium      | id a8d408dd91fb4b328a11581979a412a5 | B -> Sai
  line  12053 | Medium      | id 51adc5720299461e86a59b4ec8792f7e | A -> Đúng

### Group 55 — topic: Nephrology, Endocrinology
Q: Hạ Na máu kèm theo ứ muối và ứ nước toàn thể hạ Na máu do uống quá nhiều nước dùng gì?
Options (shared set): ['Demeclocycin.', 'Carbamazepin.', 'Furosemid.', 'Phenothiazin.']
  line   6769 | Medium      | id a028e874f7c448038e0d6b3d5c7cad70 | C -> Furosemid.
  line  12014 | Medium      | id e5ee51a1701f4a3c83986fd30b14d897 | A -> Demeclocycin.

### Group 56 — topic: Endocrinology, Radiology, Nuclear Medicine
Q: Để thăm dò hình thái của tuyến nội tiết thường dựa vào, trừ?
Options (shared set): ['Chụp phóng xạ', 'Siêu âm', 'Khám lâm sàng', 'X Quang']
  line   6842 | Medium      | id cd635edcc7334a0eb8e0d44b41984313 | A -> Chụp phóng xạ
  line   8115 | Medium      | id 7a224da7fa374709b055f66289b56f56 | B -> Siêu âm

### Group 57 — topic: Endocrinology, Obstetrics and Gynecology
Q: HCG là hocmon hướng sinh dục nhau thai được tiết ra từ:
Options (shared set): ['Tbao langhans của nhau thai', 'Lớp nội bào của nhau', 'Tế bào hạt của hoàng thể', 'Tế bào vỏ trong của trứng']
  line   6949 | Medium      | id 11e2e656db6a4a0795516f5dbc4297bc | A -> Tbao langhans của nhau thai
  line  11937 | Easy        | id f223fe92bfb247cf93a7bfa2ceba5e53 | B -> Lớp nội bào của nhau

### Group 58 — topic: Molecular Biology
Q: Enzyme nào tham gia tổng hợp mạch chậm DNA trong sao chép:
Options (shared set): ['DNA polymerase III', 'Ligase', 'Primase', 'Tất cả đều đúng']
  line   9175 | Easy        | id 1ae1080a6df7425e97f05ad153160ca9 | D -> Tất cả đều đúng
  line   9216 | Easy        | id 53ec114fe4b4441e8fe169441c1a39dc | A -> DNA polymerase III

### Group 59 — topic: Molecular Biology
Q: Enzyme nào có chức năng phiên mã ngược:
Options (shared set): ['Primase', 'DNA polymerase', 'RNA polymerase', 'Tất cả đều sai']
  line   9176 | Easy        | id 3885a07dee0f45ec84411def21fd2cdb | D -> Tất cả đều sai
  line   9217 | Easy        | id bb8112276d374dbda4edf92abfc23caf | B -> DNA polymerase

### Group 60 — topic: Molecular Biology
Q: Enzyme Topoisomerase có vai trò:
Options (shared set): ['Tách mạch tạo chẻ ba sao chép DNA.', 'Cắt một mạch DNA phía sau chẻ ba sao chép để tháo xoắn.', 'Sửa sai.', 'Làm mồi để tổng hợp các đoạn Okazaki.']
  line   9194 | Easy        | id 004756f0fc124700af61fe0f6528092d | D -> Làm mồi để tổng hợp các đoạn Okazaki.
  line   9224 | Easy        | id bb90ac026be9412b8c4daa7f413e87b7 | B -> Cắt một mạch DNA phía sau chẻ ba sao chép để tháo xoắn.

### Group 61 — topic: Molecular Biology
Q: Nếu một trong những enzyme sau đây vắng mặt thì không có nucleotide nào được gắn vào chẻ ba sao chép. Enzyme nào trong số này:
Options (shared set): ['Polymerase I (có hoạt tính polymer hóa).', "Polymerase I (có hoạt tính exonucleose 5'--->3').", 'Polymerase III.', 'DNA- ligase.']
  line   9198 | Easy        | id 2a4e2ffb7470475f842f77a4a0c647c5 | D -> DNA- ligase.
  line   9226 | Easy        | id 97d364f3e9804f53bdffdd857c7e5515 | B -> Polymerase III.

### Group 62 — topic: Obstetrics and Gynecology, Pediatrics, Genetics
Q: Double test được làm nhằm đánh giá nguy cơ:
Options (shared set): ['Khuyết tật ống thần kinh, trisomy 13, trisomy 18', 'Hội chứng Down, trisomy 13, trisomy 18', 'Hội chứng Down, khuyết tật ống thần kinh, trisomy 18', 'Hội chứng Down, khuyết tật ống thần kinh, trisomy 13']
  line   9496 | Medium      | id 454be956b8434e00bda52c8f3e1e3b6d | B -> Hội chứng Down, trisomy 13, trisomy 18
  line  11559 | Medium      | id 7ca4ba14794b4aef82d863c4bcbb75b9 | A -> Hội chứng Down, khuyết tật ống thần kinh, trisomy 18

### Group 63 — topic: Physical Medicine and Rehabilitation
Q: Vị trí chêm lót gối khi bệnh nhân nằm nghiêng bên liệt:
Options (shared set): ['Đầu, vai bên lành, chân và lưng bên liệt.', 'Đầu, chân bên lành, vai và lưng bên liệt.', 'Đầu, chân bên liệt, vai và lưng bên lành.', 'Đầu, lưng bên lành, chân và vai bên liệt.']
  line   9760 | Medium      | id dd30112ad5f3401185934c6b0ad88900 | B -> Đầu, chân bên lành, vai và lưng bên liệt.
  line   9791 | Easy        | id 30dde6f815144dd0bc70a956baf5126f | D -> Đầu, lưng bên lành, chân và vai bên liệt

### Group 64 — topic: Periodontology
Q: Sự khác biệt quan trọng nhất giữa sang chấn mô quanh răng tiên phát và thứ phát là:
Options (shared set): ['Đặc điểm mòn men và ngà răng.', 'Đặc điểm khớp cắn', 'Đặc điểm tiến triển của tổn thương', 'Đặc điểm mô quanh răng']
  line  10686 | Medium      | id 4f4afc942d01484ea68ab165057f69fb | D -> Đặc điểm mô quanh răng
  line  10716 | Medium      | id 7debccf752094f6d8b8f3a9a5166b6c6 | D -> Đặc điểm mô quanh răng
  line  11372 | Medium      | id ea6c1d89e4554ad4a4a465399a777db5 | C -> Đặc điểm tiến triển của tổn thương
  line  11414 | Easy        | id c4717e1884a348ce806060b1a9f88c0e | D -> Đặc điểm mô quanh răng

### Group 65 — topic: Periodontology, Pathology
Q: Đặc điểm khoảng gian bào của biểu mô nối trong vùng quanh răng?
Options (shared set): ['Khoảng gian bào chiếm khoảng 5% thể tích biểu mô', 'Khoảng gian bào chiếm khoảng 8% thể tích biểu mô', 'Khoảng gian bào chiếm khoảng 15% thể tích biểu mô', 'Khoảng gian bào chiếm khoảng 18% thể tích biểu mô']
  line  10726 | Easy        | id 097dfa27b2ec4f2f8ff90585732a93c0 | D -> Khoảng gian bào chiếm khoảng 18% thể tích biểu mô
  line  11441 | Easy        | id 026d27e6ae694ae29b2058a1fd21e161 | C -> khoảng gian bào chiếm khoảng 15% thể tích biểu mô

### Group 66 — topic: Dentistry
Q: tiêu xương ổ răng do sang chấn khớp cắn là tiêu xương
Options (shared set): ['ngang', 'chéo', 'tạo khuyết xương dạng nang', 'tạo khuyết xương trên bề mặt xương vỏ']
  line  11390 | Medium      | id f5866d8529014b2892bec9dfa19c6685 | D -> tạo khuyết xương trên bề mặt xương vỏ
  line  11407 | Easy        | id 11f7dea16a5542a093c469f41ab1eafe | B -> Chéo

### Group 67 — topic: Palliative Medicine, General Medicine
Q: Thuốc nào sau đây có thời gian khống chế cơn đau cao nhất?
Options (shared set): ['Codein', 'Morphine (time-release) (MS Contin)', 'Methadone', 'Levorphanol']
  line  12273 | Medium      | id 35a827edd9f140c5894be547281942c3 | D -> Levorphanol
  line  12298 | Medium      | id 84a1834026294ee18659efb995b2d621 | C -> Methadone


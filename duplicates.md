# VM14K: duplicate questions

Same normalised question AND same normalised option set (any order).

Normalisation: dedup_utils.normalize_vietnamese (authors' code)
Line numbers refer to data-processed-shuffled0.jsonl.

Groups: 1125   Rows: 2450

### Group 1 — topic: Urology, Nephrology
Q: Yếu tố thuận lợi hình thành sỏi là gì?
Options (shared set): ['Nam giới.', 'Thừa cân.', 'Tuổi <40 tuổi.', 'Ăn uống dư đạm.']
  line      1 | Easy        | id 33ec4246710149efab9d56f1141847d3 | D -> Ăn uống dư đạm.
  line  10467 | Medium      | id 83cf9e80ce75487d906d46ec455574bb | D -> Ăn uống dư đạm.

### Group 2 — topic: Nephrology, Urology
Q: Urobilinogen trong nước tiểu tăng lên trong trường hợp:
Options (shared set): ['tất cả', 'Thiếu máu tan huyết, sốt rét', 'sung huyết phổi, đa chấn thương', 'Viem gan virus, xơ gan']
  line      5 | Medium      | id 098b4e461dec44428168dccbe22787de | A -> tất cả
  line  10393 | Medium      | id 5538727fdbf64db4a47e14455710d9cf | A -> tất cả

### Group 3 — topic: Urology, Surgery
Q: Muốn phẫu thuật vòi thận bác sĩ sẽ chọn đường nào dưới đây để thuận tiện nhất?
Options (shared set): ['Đường vân giáp giữa xương sườn XII và bờ ngoài của cơ chung', 'Đường dọc theo bờ dưới xương sườn cuối', 'Dọc theo bờ ngoài khối cơ chung', 'Qua thành bụng trước']
  line      9 | Medium      | id c547ac45b6974cfdadb102dbf03a8b57 | A -> Đường vân giáp giữa xương sườn XII và bờ ngoài của cơ chung
  line    468 | Medium      | id 9ca1ec538be147279fd1158eae9e3e33 | A -> Đường vân giáp giữa xương sườn XII và bờ ngoài của cơ chung

### Group 4 — topic: Urology, Nephrology
Q: Các nguyên nhân ngoài hệ tiết niệu thường gây tắc đường dẫn niệu là:
Options (shared set): ['Xơ hóa sau phúc mạc', 'Khối u vùng tiểu khung', 'Khối u sau phúc mạc', 'Tất cả đều đúng']
  line     16 | Medium      | id 66cf0aff71d24e2799f320518ec9f869 | D -> Tất cả đều đúng
  line    248 | Medium      | id 42067a1e19694a2ea01779ec7a1cbf2e | D -> Tất cả đều đúng

### Group 5 — topic: Urology, Nephrology, Radiology
Q: Trên siêu âm không phân biệt thành phần cấu tạo của sỏi tiết niệu:
Options (shared set): ['Đúng', 'Sai']
  line     17 | Medium      | id 9868dc101a9b4d6baa3edc78f6cb160e | A -> Đúng
  line    249 | Medium      | id b8f370a4fbb64d96b273d4fa050265cd | A -> Đúng
  line  12038 | Medium      | id 66f77019a3f74f4088190cc64ea46b1d | A -> Đúng

### Group 6 — topic: Urology, Nephrology, Radiology
Q: Siêu âm có thể thấy tụ dịch quanh thận:
Options (shared set): ['Đúng', 'sai']
  line     18 | Medium      | id 550bdc79590a466fbda59f78eefc52a4 | A -> Đúng
  line  12048 | Easy        | id bf19a011976841d9b8e48b58d22ee00e | A -> Đúng

### Group 7 — topic: Urology, Nephrology, Radiology
Q: UIV là kỹ thuật ưu thế trong phát hiện u đường dẫn niệu.
Options (shared set): ['Đúng', 'Sai']
  line     19 | Medium      | id e1ef2f6107384ba9bb0d3964807e7b07 | A -> Đúng
  line    250 | Medium      | id ac76cf163f0d48ee8473e5b8c4f77b18 | A -> Đúng

### Group 8 — topic: Urology, Nephrology, Radiology
Q: Tỉ lệ tử vong do tai biến thuốc cản quang khi chụp niệu đồ tĩnh mạch là 1/10000
Options (shared set): ['Đúng', 'Sai']
  line     20 | Medium      | id ea40341e0e6f4588823b64bcdaa2ee19 | B -> Sai
  line    103 | Medium      | id 79c1cd06b5664e1b82e86ccc07c1e024 | B -> Sai

### Group 9 — topic: Urology, Nephrology, Radiology, Geriatrics, Pediatrics
Q: Chụp niệu đồ tĩnh mạch (UIV) là kỹ thuật nên hạn chế đối với trẻ sơ sinh < 15 ngày và người già >70 tuổi.
Options (shared set): ['Đúng', 'Sai']
  line     21 | Easy        | id 621ee610c58245a8908cd96e88c5a783 | A -> Đúng
  line    482 | Medium      | id ffdaa2463dec4aa580b95248f8063cbb | A -> Đúng

### Group 10 — topic: Pediatrics, Surgery, Urology
Q: Viêm ruột thừa ở trẻ em hay nhầm với sỏi tiết niệu đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line     24 | Medium      | id 9a1d243f04314509b581094cac640d66 | B -> Sai
  line     31 | Medium      | id 1ee1524ecd0d4f9e845830801e251965 | B -> Sai
  line     35 | Medium      | id 7f028f772bbe4598a3d3fbf6116066aa | B -> Sai

### Group 11 — topic: Urology
Q: Bí tiểu là bệnh nhân đi tiểu không ra nước tiểu đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line     29 | Easy        | id b8e40d1603aa46efac12f89eb964d1e2 | B -> Sai
  line     38 | Easy        | id a97a08822ffc4aa5b29f70505bf07e1c | B -> Sai

### Group 12 — topic: Urology, Radiology
Q: CT Scan là một xét nghiệm có giá trị nhất trong chẩn đoán vỡ bàng quang
Options (shared set): ['Đúng', 'Sai']
  line     30 | Medium      | id 60bdc8f94977423a99123e8d96a0d603 | A -> Đúng
  line     42 | Medium      | id 8f93082ce0184993938daf63b349dc7f | A -> Đúng

### Group 13 — topic: Urology, Oncology, Pulmonology
Q: Hút thuốc là nguyên nhân chính trong các trường hợp ung thư tuyến tiền liệt
Options (shared set): ['Đúng', 'Sai']
  line     32 | Easy        | id 045e82dfce8544729481e5730d536abc | B -> Sai
  line   4633 | Easy        | id c76ed43907284edf9957db3e301b1105 | B -> Sai

### Group 14 — topic: Urology, Nephrology
Q: Thăm khám lâm sàng luôn có thể chẩn đoán được sỏi niệu đạo kẹt niệu đạo - tiền liệt tuyến biến chứng bí tiểu cấp:
Options (shared set): ['Đúng', 'Sai']
  line     39 | Medium      | id 3bb6c02a2e7e4f87a4825603dd1f54df | B -> Sai
  line    259 | Medium      | id 25557a06ce574f85b03aa99cbef8df5c | B -> Sai

### Group 15 — topic: Urology, Nephrology
Q: Thăm khám lâm sàng có thể chẩn đoán được chính xác sỏi niệu đạo dương vật biến chứng bí tiểu cấp:
Options (shared set): ['Đúng', 'Sai']
  line     40 | Medium      | id fde5008d042a459db1ba1ec6a96bf891 | A -> Đúng
  line    260 | Medium      | id 75e3eb698bdc49e6be867fa6fc432c80 | A -> Đúng

### Group 16 — topic: Urology, Nephrology
Q: Không cần xét nghiệm cận lâm sàng để có thể chẩn đoán chính xác sỏi niệu đạo dương vật biến chứng bí tiểu cấp.
Options (shared set): ['Đúng', 'Sai']
  line     41 | Medium      | id fd51d653fc594e28898a0a0f9106901d | A -> Đúng
  line    261 | Medium      | id 4d3297072b034557aed86df6736565b5 | A -> Đúng

### Group 17 — topic: Infectious Diseases, Urology, Pediatrics
Q: Chọn một câu trả lời đúng. Đặc điểm viêm tinh hoàn trong quai bị ngoại trừ:
Options (shared set): ['Một số tác giả thấy tỷ lệ teo tinh hoàn do quai bị là 10 ÷ 15% sau 2 ÷ 4 tháng mắc bệnh.', 'Bệnh xuất hiện sau khi sưng tuyến mang tai 1 ÷ 2 tuần.', 'Sau 2 tháng mới đánh giá được tinh hoàn có bị teo hay không.', 'Bệnh nhân đau ở tinh hoàn sắp bị sưng, rồi tinh hoàn sưng to gấp 3 ÷ 4 lần bình thường, đau nhức, da bìu đỏ, đôi khi mào tinh cũng sưng to.']
  line     43 | Easy        | id cf8084523dad464f88aa7e107c69efa0 | D -> Bệnh nhân đau ở tinh hoàn sắp bị sưng, rồi tinh hoàn sưng to gấp 3 ÷ 4 lần bình thường, đau nhức, da bìu đỏ, đôi khi mào tinh cũng sưng to.
  line    603 | Medium      | id 3ec8a72f622f4e9a868f3cc76f41febe | D -> Bệnh nhân đau ở tinh hoàn sắp bị sưng, rồi tinh hoàn sưng to gấp 3 ÷ 4 lần bình thường, đau nhức, da bìu đỏ, đôi khi mào tinh cũng sưng to.

### Group 18 — topic: Urology, Gastroenterology
Q: Thăm trực tràng có thể phát hiện các thương tổn ngoài hậu môn – trực tràng sau:
Options (shared set): ['Tiền liệt tuyến ở nam', 'Tử cung và âm đạo nữ', 'Túi tinh và ống dẫn tinh ở nam', 'Tất cả đều đúng']
  line     47 | Medium      | id d2152e9da25b4f50bf3363f15cae5c06 | D -> Tất cả đều đúng
  line    672 | Medium      | id 7f48222b59054aae908619afe77c17a0 | A -> Tiền liệt tuyến ở nam

### Group 19 — topic: Surgery, Urology
Q: Trong những bệnh lý ở vùng bẹn ở 2 giới, bệnh lý nào hay gặp nhất?
Options (shared set): ['Thoát vị bẹn', 'Thoát vị đùi', 'Giãn TM thừng tinh bên phải', 'Hạch bẹn phì đại']
  line     50 | Medium      | id d21201c281874c7c9af98537a93f069c | A -> Thoát vị bẹn
  line    766 | Easy        | id 13c3c3866f09458db3e551d718c45260 | A -> Thoát vị bẹn

### Group 20 — topic: Urology, Surgery, Gastroenterology
Q: Thăm trực tràng có thể phát hiện các thương tổn ngoài hậu môn – trực tràng nào sau đây?
Options (shared set): ['Tiền liệt tuyến ở nam', 'Tử cung và âm đạo nữ', 'Túi tinh và ống dẫn tinh ở nam', 'Tất cả đều đúng']
  line     51 | Medium      | id 8b9c685693c044978144079f5b488ec7 | D -> Tất cả đều đúng
  line    830 | Medium      | id cac6b7691ccc41529ac6fabeb0b605cf | A -> Tiền liệt tuyến ở nam

### Group 21 — topic: Surgery, Gastroenterology, Urology
Q: Các tổn thương có thể gặp ở vùng tầng sinh môn sau là gì?
Options (shared set): ['Dò hậu môn – âm đạo', 'Dò hậu môn', 'Đứt niệu đạo sau chấn thương ngã ngồi trên mạn thuyền', 'Tất cả đều đúng']
  line     52 | Medium      | id c76e93634d7b4a088e952d830d90e58b | B -> Dò hậu môn
  line  10614 | Medium      | id bbaebeaaf12f400ebba655a9fd057cf2 | B -> Dò hậu môn

### Group 22 — topic: Urology
Q: TC điển hình nhất của sỏi bàng quang niệu đạo
Options (shared set): ['đái buốt', 'đái rắt', 'đái mủ', 'đái tắc']
  line     56 | Medium      | id 2d01b27a6ea74ab9a216efba9ae953ac | D -> đái tắc
  line   1031 | Easy        | id 7154d7fd680948228aa6484b62c5c124 | B -> đái rắt

### Group 23 — topic: Urology, Nephrology
Q: Sỏi thận gây?
Options (shared set): ['Đái máu', 'Suy thận', 'Viêm niệu đạo', 'Cả 3']
  line     58 | Medium      | id 11238acf7a24427983ea5ed32ac87c6d | D -> Cả 3
  line   1036 | Easy        | id 5638e77843a8409aadeba3e50b70004a | D -> Cả 3

### Group 24 — topic: Urology, Infectious Diseases
Q: Viêm bàng quang, niệu đạo do đâu?
Options (shared set): ['Tụ cầu', 'Phế cầu', 'Liên cầu', 'E.coli']
  line     59 | Medium      | id 62803f8f5bf84d42a516063c8f2e4b88 | D -> E.coli
  line   1041 | Easy        | id d003510a9e9747f2a376c4c6110e7512 | D -> E.coli

### Group 25 — topic: Urology, Nephrology
Q: Trên lâm sàng, đái máu đại thể cần phải chẩn đoán phân biệt với:
Options (shared set): ['Đái ra Myoglobin.', 'Xuất huyết niệu đạo', 'Đái ra dưỡng trấp.', 'Tụ máu quanh thận.']
  line     64 | Medium      | id fb590f60260e4385ad3c9065265f3ec0 | B -> Xuất huyết niệu đạo
  line   1044 | Medium      | id dd34096fc4074e93b2131961fb89f068 | B -> Xuất huyết niệu đạo

### Group 26 — topic: Nephrology, Urology
Q: Đái máu có hồng cầu nhỏ, méo mó không đều là đặc điểm của:
Options (shared set): ['Polype bàng quang.', 'Viêm cầu thận.', 'Viêm thận bể thận.', 'Ung thư thận.']
  line     65 | Challenging | id 60b2c7bbbed14b92bda1ff7bf4b63bdb | B -> Viêm cầu thận.
  line  12020 | Medium      | id b4baad97f74b4d199fe4ec35e75b64f8 | B -> Viêm cầu thận.

### Group 27 — topic: Nephrology, Urology
Q: Nguyên nhân không do nhiễm trùng của đái ra máu đại thể:
Options (shared set): ['Lao thận.', 'Viêm bàng quang xuất huyết.', 'Sỏi thận.', 'Viêm thận bể thận cấp.']
  line     75 | Medium      | id c948eae27a3b4789b62c7dc5a42782c4 | C -> Sỏi thận.
  line  10396 | Medium      | id 4c3043b21e054e75863483f15325bd52 | C -> Sỏi thận.

### Group 28 — topic: Nephrology, Urology
Q: Ba vị trí thường gặp hay gây đái máu đại thể là:
Options (shared set): ['Thận - Niệu quản - Bàng quang.', 'Niệu quản - Bàng quang - niệu đạo.', 'Thận - Bàng quang - Niệu đạo.', 'Thận - Niệu quản - Niệu đạo.']
  line     78 | Easy        | id f06e72992d934d06906680b35568f3a6 | C -> Thận - Bàng quang - Niệu đạo.
  line   1045 | Medium      | id eb9cbfa0e5bc42e2ac915f10ff7e42d3 | C -> Thận - Bàng quang - Niệu đạo.

### Group 29 — topic: Nephrology, Urology
Q: Yếu tố quan trọng nhất để xác định đái máu từ cầu thận:
Options (shared set): ['Trụ hồng cầu.', 'Protein niệu dương tính.', 'Tăng huyết áp.', 'Bệnh nhân phù to.']
  line     83 | Medium      | id 8d2e2093000c4bb29fc493d4571af8a5 | A -> Trụ hồng cầu.
  line    221 | Medium      | id 50b953995f984079a12417c2bdbd5663 | C -> Trụ hồng cầu

### Group 30 — topic: Pediatrics, Infectious Diseases, Urology
Q: Sau thời gian bao lâu thì có thể chẩn đoán Teo tinh hoàn ở bệnh nhân quai bị?
Options (shared set): ['2-6 tháng.', '1-3 tháng', '1-6 tháng', '3-6 tháng']
  line     85 | Easy        | id 22eed63968a64acca31c6510f3a2735b | A -> 2-6 tháng.
  line  10404 | Medium      | id 95226182a0994b01b002587c097ac84f | A -> 2-6 tháng.

### Group 31 — topic: Urology, Endocrinology
Q: Trong điều trị Viêm tinh hoàn, liều dùng Corticoid là bao nhiêu một ngày?
Options (shared set): ['Prednisolon 60mg/ ngày dùng 3-5 ngày', 'Prednisolon 60mg/ ngày dùng 5-7 ngày', 'Prednisolon 60mg/ ngày dùng 3-8 ngày', 'Prednisolon 60mg/ ngày dùng 6-10 ngày']
  line     88 | Medium      | id 110fd38e760240a08974c5201a2ff2ae | A -> Prednisolon 60mg/ ngày dùng 3-5 ngày
  line   6449 | Medium      | id d908b579af094bc8a897b494215bb5b1 | A -> Prednisolon 60mg/ ngày dùng 3-5 ngày

### Group 32 — topic: Urology, Endocrinology
Q: Thời gian bao nhiêu lâu sau đây mới đánh giá được tinh hoàn có bị teo hay không?
Options (shared set): ['3-5 tháng', '2-4 tháng', '2-6 tháng', '1-2 tháng']
  line     89 | Easy        | id ab6bbac5f1204032a220072f4310e78a | C -> 2-6 tháng
  line   6450 | Medium      | id a9aa507571624655a9a5e96ebb08cd8b | C -> 2-6 tháng

### Group 33 — topic: Urology, Infectious Diseases
Q: Thời gian tối ưu điều trị kháng sinh cho viêm tuyến tiền liệt cấp do vi khuẩn là.
Options (shared set): ['3 ngày.', '4 - 6 tuần.', '7 - 14 ngày.', '2 - 14 ngày.']
  line     91 | Easy        | id e79c47f942884522934a6ec52d5cfa82 | B -> 4 - 6 tuần.
  line   1086 | Medium      | id ac43ff1c2fc34c9a87718b7f45136b58 | B -> 4 - 6 tuần.

### Group 34 — topic: Urology, Oncology, Radiology
Q: NĐTM là kỹ thuật ưu thế trong phát hiện u đường dẫn niệu
Options (shared set): ['Đúng', 'Sai']
  line    101 | Medium      | id c5a66d8777974553abfcdddbec934b0c | A -> Đúng
  line  10441 | Medium      | id 528903fb95954377904929db6920db55 | A -> Đúng

### Group 35 — topic: Nephrology, Urology
Q: Đau quặn thận điển hình là do tắc nghẽn mạn tính đường tiết niệu trên:
Options (shared set): ['Đúng', 'Sai']
  line    115 | Medium      | id adc02c8db732475d91b384fe8123b74c | B -> Sai
  line    152 | Medium      | id 2f7b3a26cc444e7e973e7138a9b00854 | B -> Sai
  line    204 | Medium      | id 435034802c4c4bc0a2373d5464020f70 | B -> Sai

### Group 36 — topic: Nephrology, Urology
Q: Đau âm ỉ thắt lưng là do tắc nghẽn cấp tính đường tiết niệu trên
Options (shared set): ['Đúng', 'Sai']
  line    116 | Medium      | id 0eedc6b9d4af434ea175a5cc13078438 | B -> Sai
  line    153 | Medium      | id 2c7b5660550a4e59a322ccd12336936d | B -> Sai
  line    205 | Medium      | id 516e0b0051454dd6be37c4cd866b5a8c | B -> Sai

### Group 37 — topic: Urology, Oncology
Q: Khám lâm sàng nam thanh niên, phát hiện tinh hoàn một bên lớn. Nguyên nhân tinh hoàn lớn nghĩ tới là u tinh hoàn
Options (shared set): ['Đúng', 'Sai']
  line    117 | Challenging | id 8abdb625db474c2998d6c1bddfed10bc | B -> Sai
  line    154 | Challenging | id ff85a681abd34834b2dcfac20194233f | B -> Sai
  line    206 | Challenging | id 70bb245e0dd2439782bfc6c52aca11cc | B -> Sai

### Group 38 — topic: Urology, Endocrinology
Q: Thời gian tối đa khi sử dụng corticoid trong điều trị viêm tinh hoàn kéo dài bao nhiêu ngày
Options (shared set): ['5-7', '4-6', '6-10', '3-5']
  line    119 | Medium      | id d3483de20b2341e781f812596b953460 | A -> 5-7
  line   6483 | Medium      | id 95ba2236a8b246c0a64d019235aa1be8 | A -> 5-7

### Group 39 — topic: Urology, Surgery
Q: Rút dẫn lưu bàng quang trên xương mu vào thời điểm nào?
Options (shared set): ['Ngày thứ 3-4 sau mổ', 'Ngày thứ 7 và thay bằng một ống thông Nelaton qua niệu đạo', 'Sau ngày thứ 7, khi kẹp thử ống dẫn lưu, bệnh nhân tự đái được', 'Không có đáp án']
  line    129 | Medium      | id 5ac9456ffb524267bd749945b121b4f1 | C -> Sau ngày thứ 7, khi kẹp thử ống dẫn lưu, bệnh nhân tự đái được
  line  10463 | Medium      | id e727899457d34fb9b4b06cbbfa72ba77 | C -> Sau ngày thứ 7, khi kẹp thử ống dẫn lưu, bệnh nhân tự đái được

### Group 40 — topic: Infectious Diseases, Urology, Obstetrics and Gynecology
Q: Tìm ý đúng về khuẩn lậu:
Options (shared set): ['Neisseria gonorrhone song cầu, gram âm.', 'Sức đề kháng cao khó bị diệt bởi hóa chất và thuốc sát trùng thông thường.', 'Neisseria meningitides, song cầu, gram âm.', 'Không sinh bào tử, không có pili.(1 so co pili)']
  line    133 | Easy        | id c3d04116ad564f5fb63acbfd8b3cd47e | A -> Neisseria gonorrhone song cầu, gram âm.
  line   1231 | Medium      | id 6cacc405ead44f78ae7aaa7f5fc0ba9e | A -> Neisseria gonorrhone song cầu, gram âm.

### Group 41 — topic: Endocrinology, Urology
Q: LH có tác dụng:
Options (shared set): ['Kích thích tinh hoàn phát triển và bài tiết hormon.', 'Kích thích tế bào Leydig phát triển và bài tiết hormon.', 'Kích thích ống sinh tinh phát triển và sản sinh tinh trùng.', 'Kích thích tế bào Sertoli phát triển và bài tiết chất dinh dưỡng.']
  line    136 | Easy        | id 59cfa8ddddb6493fb10842c0a439c6f9 | B -> Kích thích tế bào Leydig phát triển và bài tiết hormon.
  line   6558 | Medium      | id ed999072bc8e444d98323a688d04e500 | B -> Kích thích tế bào Leydig phát triển và bài tiết hormon.
  line   6704 | Medium      | id 8407b632668b4f939a89cef165c0cdfa | B -> Kích thích tế bào Leydig phát triển và bài tiết hormon.

### Group 42 — topic: Endocrinology, Urology
Q: Hormon điều hoà sản sinh tinh trùng:
Options (shared set): ['FSH.', 'LH.', 'GnRH.', 'Inhibin.']
  line    137 | Easy        | id adca9e89369448709e68be242478eae0 | D -> Inhibin.
  line   6559 | Medium      | id 90ae7b30d8954444837198e4300cfced | D -> Inhibin.
  line   6583 | Medium      | id 8e54022243804c29b6bd7829a816b26b | D -> Inhibin.
  line   6706 | Medium      | id 741ff9c3c09d4a13a5a9fa303b532874 | D -> Inhibin.

### Group 43 — topic: Urology, Obstetrics and Gynecology
Q: Tinh trùng có khả năng di động và thụ tinh khi ở:
Options (shared set): ['Phần đầu ống mào tinh ngay khi vừa rời khỏi ống sinh tinh.', 'Trong ống mào tinh sau 24h kể từ khi rời ống sinh tinh.', 'Trong dịch ống phóng tinh.', 'Bất kỳ nơi nào khi tinh trùng đã được sản sinh và có đủ đầu, cổ, đuôi.']
  line    138 | Easy        | id 997503d8920a4b84b258251433d0b86e | C -> Trong dịch ống phóng tinh.
  line   3737 | Easy        | id 69b3698420f0484999b84aa5772db7af | C -> Trong dịch ống phóng tinh.

### Group 44 — topic: Endocrinology, Urology
Q: Tác dụng hormon sinh dục nam?
Options (shared set): ['Gây nam hoá, tác động lên bộ máy sinh dục nam, kích thích tổng hợp protein ở xương, giảm vận chuyển canxi ra khỏi xương', 'Gây nam hoá, tác động lên bộ máy sinh dục nam, tăng tổng hợp lipid', 'Gây nam hoá, tác động lên bộ máy sinh dục nam, tăng tổng hợp glucid', 'Gây nam hoá, tác động lên bộ máy sinh dục nam']
  line    139 | Easy        | id b7b85ee0f6ef4323ae6759046fdcf3d4 | A -> Gây nam hoá, tác động lên bộ máy sinh dục nam, kích thích tổng hợp protein ở xương, giảm vận chuyển canxi ra khỏi xương
  line   6635 | Medium      | id 18edd997be8f40c88e607741d66febe2 | A -> Gây nam hoá, tác động lên bộ máy sinh dục nam, kích thích tổng hợp protein ở xương, giảm vận chuyển canxi ra khỏi xương

### Group 45 — topic: Endocrinology, Urology
Q: Tác dụng của LH trên nam giới là:
Options (shared set): ['Kích thích phát triển ống sinh tinh.', 'Kích thích sản sinh tinh trùng', 'Kích thích làm nở to tinh hoàn.', 'Kích thích sản xuất testosteron.']
  line    140 | Easy        | id cdd711ec0cb546d2a90cd0f10b4995a8 | D -> Kích thích sản xuất testosteron.
  line   6669 | Medium      | id 9a63a30f60ba45399800149a974939fb | D -> Kích thích sản xuất testosteron.

### Group 46 — topic: Endocrinology, Obstetrics and Gynecology, Urology
Q: Rối loạn bài tiết T3 - T4 gây rối loạn chức năng sinh dục:
Options (shared set): ['Thiếu T3 - T4 làm tăng dục tính ở nam và vô kinh ở nữ.', 'Thiếu T3 - T4 làm mất dục tính ở nam và băng kinh ở nữ.', 'Thừa T3 - T4 làm mất dục tính ở nam và vô kinh ở nữ.', 'Thừa T3 - T4 làm mất dục tính ở nam và băng kinh ở nữ.']
  line    141 | Easy        | id bc0ff025abf14b6a854571be3b17482e | B -> Thiếu T3 - T4 làm mất dục tính ở nam và băng kinh ở nữ.
  line   1264 | Medium      | id f112b4e668d04fcfa91a7411ee6c49aa | B -> Thiếu T3 - T4 làm mất dục tính ở nam và băng kinh ở nữ.
  line   6104 | Medium      | id 11d51ad915ab4c07ae393df20f60900c | B -> Thiếu T3 - T4 làm mất dục tính ở nam và băng kinh ở nữ.
  line   6111 | Medium      | id 8e6b9d0353bb4bde9da3f217669beb3e | B -> Thiếu T3 - T4 làm mất dục tính ở nam và băng kinh ở nữ.
  line   8646 | Medium      | id 5a5b9a612fa347b38f113d075935bab8 | B -> Thiếu T3 - T4 làm mất dục tính ở nam và băng kinh ở nữ.

### Group 47 — topic: Endocrinology, Urology
Q: Hormone sinh dục nam testosterone chủ yếu tiết ra ở đâu?
Options (shared set): ['Mào tinh hoàn', 'Tinh hoàn', 'Tuyến thượng thận', 'Ống dẫn tinh']
  line    145 | Easy        | id c3bcffb8839b48a5bddc14a864a8ba11 | B -> Tinh hoàn
  line   6283 | Easy        | id 724141d26e8442a5a261b46d59065f97 | B -> Tinh hoàn

### Group 48 — topic: Urology, Oncology
Q: Ung thư biểu mô tuyến tiền liệt nếu không được tầm soát, phát hiện sớm sẽ tiến triển âm thầm và có thể bệnh chỉ được phát hiện, xác định khi tế bào u đã lan rộng hay di căn đến mô và cơ quan kế cận. Các mô và cơ quan kế cận thường gặp trong ung thư tuyến tiền liệt thường gặp nhất gì?
Options (shared set): ['Xâm nhập mô của tuyến tiền liệt, lan rộng đến túi tinh, đại tràng, bàng quang', 'Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, trực tràng, bàng quang', 'Xâm nhập mô tuyến tiền liệt, lan rộng đến túi tinh, đại tràng, cột sống cùng cụt', 'Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, trực tràng, cột sống cùng cụt']
  line    157 | Medium      | id b09cddab7e934a2eb6988eb314153960 | D -> Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, trực tràng, cột sống cùng cụt
  line    287 | Medium      | id 828528d89627412da0349556734726da | D -> Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, trực tràng, cột sống cùng cụt
  line   1353 | Medium      | id 3b0052045c8d45e98e2aae187aeaa603 | D -> Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, trực tràng, cột sống cùng cụt
  line   1998 | Medium      | id b15b7302132440bdbfd33eb0e485090c | D -> Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, trực tràng, cột sống cùng cụt

### Group 49 — topic: Urology, Pathology
Q: Tăng sản lành tính tuyến tiền liệt về vi thể có thể gặp tăng sản một hay nhiều hơn một các loại tế bào của tuyến tiền liệt. Chẩn đoán giải phẫu bệnh của bệnh tăng sản lành tính tuyến tiền liệt thường dựa vào yếu tố nào sau đây là phù hợp nhất?
Options (shared set): ['Tăng sản lành tính tuyến tiền liệt, típ tuyến xơ vì là típ thường gặp nhất', 'Tăng sản lành tính tuyến tiền liệt, típ xơ vì có tên gọi khác là u xơ tiền liệt', 'Chủ yếu là thường gặp là tăng sản mô xơ và mô cơ xơ hoá', 'Tuỳ theo thành phần nào chiếm ưu thế mà gọi tên']
  line    158 | Medium      | id 00ab5cd3fc63491db86bb5f12c81f1ab | D -> Tuỳ theo thành phần nào chiếm ưu thế mà gọi tên
  line    290 | Medium      | id 514edbb7cb044e948df7f55d04a9ff4d | D -> Tùy theo thành phần nào chiếm ưu thế mà gọi tên
  line   2016 | Medium      | id 0cb7b5516a4843d9a4050461f485a161 | D -> Tùy theo thành phần nào chiếm ưu thế mà gọi tên

### Group 50 — topic: Urology, Oncology
Q: Ung thư biểu mô tuyến tiền liệt có khả năng di căn xa đến nhiều Cơ quan khác trong cơ thể. Một vị trí đặc biệt, đặc trưng mà ung thư tuyến tiền liệt thường di căn đến là gì?
Options (shared set): ['Thận', 'Phổi', 'Xương sống', 'Trực tràng']
  line    159 | Medium      | id 134f0e7ed44640fda4ebde09cd86ee2d | C -> Xương sống
  line    285 | Medium      | id 2681bf65eb7a48b0bbc4e3584bff7b0d | C -> Xương sống
  line    286 | Medium      | id 97c4e38878f3493da9ff7136f85f8483 | C -> Xương sống
  line  10453 | Easy        | id 8b035a21632744cea1d2b46912998062 | C -> Xương sống

### Group 51 — topic: Gastroenterology, Urology
Q: Trĩ được gọi là trĩ triệu chứng gặp trong các trường hợp: u tiền liệt tuyến?
Options (shared set): ['Đúng', 'Sai']
  line    160 | Medium      | id 2acbdaf26cf348a395cb0b8f6fb7718b | A -> Đúng
  line   1413 | Challenging | id 92fa1a4ffb074e1f90ece0934bd1c7bf | A -> Đúng

### Group 52 — topic: Endocrinology, Internal Medicine, Urology
Q: Nhóm thuốc nào có tác dụng phụ nhiễm trùng sinh dục, nhiễm trùng tiểu..?
Options (shared set): ['Nhóm đồng vận GLP-1.', 'Nhóm ức chế SGLT-2.', 'Nhóm ức chế DPP-4', 'Nhóm ức chế men alpha-Glucosidase.']
  line    164 | Medium      | id 7784eca46c334ed5a972caa68c84519d | B -> Nhóm ức chế SGLT-2.
  line   6782 | Medium      | id 9cb56348c5ee4f8bb7c3ec6bd491cde1 | B -> Nhóm ức chế SGLT-2.

### Group 53 — topic: Neurology, Pulmonology, Urology
Q: Các biến chứng nào thường gặp trên bệnh nhân đột quỵ giai đoạn cấp?
Options (shared set): ['Teo cơ, cứng khớp', 'Rối loạn trầm cảm', 'Suy mòn, suy kiệt', 'Viêm đường hô hấp, viêm đường tiết niệu']
  line    165 | Medium      | id cac66efbc9144541b61acd53f6d94bfd | D -> Viêm đường hô hấp, viêm đường tiết niệu
  line   1512 | Challenging | id d3aea21cf5d041759c5db1cd2a9d155e | D -> Viêm đường hô hấp, viêm đường tiết niệu
  line   5153 | Medium      | id 1a5fc42956d147558bbf05ca6221e959 | D -> Viêm đường hô hấp, viêm đường tiết niệu
  line   5154 | Medium      | id 8a9f827d732b404b86623e1334ef9244 | D -> Viêm đường hô hấp, viêm đường tiết niệu

### Group 54 — topic: Endocrinology, Urology
Q: Phát biểu nào sau đây liên quan đến men Enzym và 5α reductase Testosteron/DHT là KHÔNG ĐÚNG?
Options (shared set): ['DHT góp phần vào sự tăng trưởng và biệt hoá của tế bào', '5α reductase chuyển Dihydrotestosteron (DHT) thành Testosteron', '5α reductase có trong màng nhân tế bào tuyến tiền liệt', 'DHT ức chế quá trình tự tiêu (Apeptosis)']
  line    170 | Medium      | id 1115a62cd69549c08c904991f53a825a | B -> 5α reductase chuyển Dihydrotestosteron (DHT) thành Testosteron
  line   6785 | Medium      | id ad7866af44864949a529cea0eacb3f98 | B -> 5α reductase chuyển Dihydrotestosteron (DHT) thành Testosteron
  line  10424 | Medium      | id 44c525ae602f42969537af24aa527b14 | B -> 5α reductase chuyển Dihydrotestosteron (DHT) thành Testosteron

### Group 55 — topic: Urology, Geriatrics
Q: Thuốc nào sau đây có tác dụng làm giảm kích thước tuyến tiền liệt ức chế ?
Options (shared set): ['5 α reductase', 'Thuốc chẹn α', 'Thuốc ức chế PDE-5', 'Thuốc kháng cholinergic']
  line    174 | Medium      | id e331ef874f594344a4f6d2bd562c32d4 | A -> 5 α reductase
  line  10739 | Medium      | id dfa87f1df27d4f98a55466dc96d1fbed | A -> 5 α reductase

### Group 56 — topic: Nephrology, Urology
Q: Nguyên nhân gây vô niệu bao gồm : Chọn câu sai :
Options (shared set): ['Suy thận cấp', 'Sỏi kẹt niệu đạo', 'Hoại tử vỏ thận hai bên', 'Viêm ống thận cấp.']
  line    176 | Medium      | id 73f9b056cb6c4895b69dc25fb6712424 | B -> Sỏi kẹt niệu đạo
  line  11999 | Medium      | id 76c471b2d3274eb3bb8a9e1cd1df7cc0 | D -> Viêm ống thận cấp.

### Group 57 — topic: Endocrinology, Urology, Infectious Diseases
Q: Thuốc điều trị đái tháo đường nào có thể gây nguy cơ nhiễm trùng đường tiểu?
Options (shared set): ['Chất ức chế kênh đồng vận chuyển natri-glucose 2', 'Chất “ bắt chước” GLP-1 “ ( đồng vận GLP-1)', 'Chất ức chế DPP-4', 'Chất đồng vận GIP']
  line    184 | Medium      | id 43cfb42217ed484b9f85e68ed20bfe02 | A -> Chất ức chế kênh đồng vận chuyển natri-glucose 2
  line   1633 | Challenging | id 4b4ace1390a34d72840d961c5eaf82b8 | A -> Chất ức chế kênh đồng vận chuyển natri-glucose 2
  line   6129 | Medium      | id 83c929c99edb4c3b9ddc8411b4cf21ee | A -> Chất ức chế kênh đồng vận chuyển natri-glucose 2

### Group 58 — topic: Endocrinology, Urology, Infectious Diseases
Q: Thuốc điều trị ĐTĐ nào có thể gây nguy cơ nhiễm trùng đường tiểu :
Options (shared set): ['Chất ức chế kênh đồng vận chuyển Natri- glucose 2.', 'Chất “ bắt chước " GLP-1" (Đồng vận GLP-1)', 'Chất ức chế DPP -4', 'Chất đồng vận GIP']
  line    186 | Medium      | id fee3bc7b1b2b47e8b6075475d4a701f1 | A -> Chất ức chế kênh đồng vận chuyển Natri- glucose 2.
  line   1640 | Challenging | id 92924c1d812e43ebbeca6ef18f422fb3 | A -> Chất ức chế kênh đồng vận chuyển Natri- glucose 2.
  line   6797 | Medium      | id 365bcc2164204e2f8558656eef9b0d57 | A -> Chất ức chế kênh đồng vận chuyển Natri- glucose 2.

### Group 59 — topic: Urology, Infectious Diseases
Q: hai xét nghiệm nào dưới đây được sử dụng chẩn đoán viêm niệu đạo do lậu và không do lậu:
Options (shared set): ['Nhuộm gram và nuôi cấy', 'Soi tươi PCR', 'Soi tươi và nhuộm gram', 'Soi tươi và nuôi cấy']
  line    196 | Challenging | id 32acc6b9ceb6419284deb9c2f5b488f2 | A -> Nhuộm gram và nuôi cấy
  line   1674 | Challenging | id f440aef0b8f142b7a3aebc42e9a79dff | C -> Soi tươi và nhuộm gram
  line  10425 | Medium      | id bcd46782b6064aa19247e4568803cf62 | C -> Soi tươi và nhuộm gram

### Group 60 — topic: Urology, Endocrinology
Q: Ở người quá trình sinh tinh mất khoảng thời gian từ
Options (shared set): ['30 đến 45 ngày', '24 đến 72 giờ', '15 đến 30 ngày', '65 đến 70 ngày']
  line    198 | Easy        | id fc1b1917e6ef4521ba8a5a5848ae1aab | D -> 65 đến 70 ngày
  line   6321 | Easy        | id 17ee2c61673b4390a8d49419ddd65a65 | D -> 65 đến 70 ngày

### Group 61 — topic: Urology, Endocrinology
Q: Số lượng tinh trùng trong 1ml tinh dịch khoảng …người đàn ông có nguy cơ bị vô sinh
Options (shared set): ['Dưới 20 triệu', 'Từ 20 triệu đến 50 triệu OOO', 'Từ 50 triệu đến 100 triệu', 'Từ 10 đến 50 triệu']
  line    199 | Easy        | id 4d6b5dbdf59542e7bc11bf495cc121f0 | A -> Dưới 20 triệu
  line   6322 | Easy        | id 788b6dd2b1974c618c541d51091ff4e5 | A -> Dưới 20 triệu

### Group 62 — topic: Endocrinology, Urology
Q: Tác dụng chính của testosterone sau dậy thì
Options (shared set): ['Phát triển dương vật', 'Thúc đẩy biệt hóa tinh trùng giai đoạn cuối', 'Thúc đẩy biệt hóa tinh trùng giai đoạn đầu', 'Đưa tinh hoàn từ ổ bụng xuống bìu']
  line    200 | Medium      | id 08ca3a0a03f64004ab88f4dbb6debc8b | B -> Thúc đẩy biệt hóa tinh trùng giai đoạn cuối
  line   6873 | Medium      | id 3872013bb03c4b7bb8aa981c5436db81 | B -> Thúc đẩy biệt hóa tinh trùng giai đoạn cuối

### Group 63 — topic: Endocrinology, Urology, Pediatrics
Q: Vai trò testosterone trong thời kỳ bào thai
Options (shared set): ['Tạo feedback âm điều hòa bài tiết testosterone', 'Biệt hóa Trung khu sinh dục ở vùng hạ đồi đưa tinh hoàn xuống bìu', 'Biệt hóa tinh trùng giai đoạn cuối', 'Làm xuất hiện đặc tính sinh dục thứ phát']
  line    201 | Medium      | id 33215a76a12e4ede843ae5c0dcc59db4 | B -> Biệt hóa Trung khu sinh dục ở vùng hạ đồi đưa tinh hoàn xuống bìu
  line   6874 | Medium      | id a74d3701f69048e39c9e55de46e203b7 | B -> Biệt hóa Trung khu sinh dục ở vùng hạ đồi đưa tinh hoàn xuống bìu

### Group 64 — topic: Nephrology, Urology
Q: 3 vị trí thường gặp gây đái máu đại thể là
Options (shared set): ['Thận - niệu quản - bàng quang', 'Thận - niệu quản - niệu đạo', 'Thận - bàng quang- niệu đạo', 'Niệu quản - bàng quang - niệu đạo']
  line    213 | Easy        | id 36768f1a6de54e1294f91ddf2e00687e | C -> Thận - bàng quang- niệu đạo
  line  10468 | Easy        | id 1450ae715d7e431692bba3b7d8283383 | C -> Thận- bàng quang- niệu đạo

### Group 65 — topic: Nephrology, Urology
Q: Chẩn đoán xác định đái máu có thể dựa vào
Options (shared set): ['Tìm hồng cầu trong nước tiểu hoặc đếm cặn Addis', 'Tìm hồng cầu trong nước tiểu qua soi kính hiển vi', 'Giấy thử nước tiểu', 'Đếm cặn Addis']
  line    218 | Medium      | id 5e8553c0c076494281158a9f2ce6402f | A -> Tìm hồng cầu trong nước tiểu hoặc đếm cặn Addis
  line  10390 | Medium      | id e44647b1ab254ffe91cd0a90559ddf25 | A -> Tìm hồng cầu trong nước tiểu hoặc đếm cặn Addis

### Group 66 — topic: Nephrology, Urology, Oncology
Q: Đái máu do ung thư thận có đặc điểm
Options (shared set): ['Do gắng sức', 'Kèm đái mủ', 'Đái máu tự nhiên, nhiều lần', 'Thường gặp ở người trẻ, thận lớn']
  line    220 | Medium      | id 012e571e39014b3497c0719bf092fa59 | C -> Đái máu tự nhiên, nhiều lần
  line  10406 | Medium      | id d0883b53515540c0a8d42ab0302b9678 | C -> Đái máu tự nhiên, nhiều lần

### Group 67 — topic: Nephrology, Urology
Q: 3 cốc nước tiểu đều đỏ suy ra vị trí hay gặp nhất là
Options (shared set): ['Niệu đạo', 'Thận', 'Niệu quản', 'Bàng quang']
  line    223 | Medium      | id 5b93569f06d6452eab1fb2d3eb38d444 | B -> Thận
  line  10423 | Medium      | id 529bb17968e447c89e5cc65cf954701e | B -> Thận

### Group 68 — topic: Nephrology, Urology
Q: Chọn nhận xét sai
Options (shared set): ['Thận giảm hoặc không lọc được nước tiểu gây bí đái', 'Đau buốt do nguyên nhân bàng quang', 'Viêm tuyến tiền liệt có thể gây đái buốt, bí đái', 'Đái buốt thường kèm theo đái dắt']
  line    224 | Medium      | id d77411d852e44a3fab3027e316d45407 | A -> Thận giảm hoặc không lọc được nước tiểu gây bí đái
  line  10426 | Medium      | id 4948cf28b03341bc8e44a57d9053bdc6 | A -> Thận giảm hoặc không lọc được nước tiểu gây bí đái

### Group 69 — topic: Nephrology, Urology
Q: Mặt cắt của thận viêm cấp có đặc điểm
Options (shared set): ['Vùng vỏ đục, ướt, rộng, hồng nhạt', 'Vùng vỏ đục, khô, rộng, hồng nhạt', 'Vùng vỏ trong, ướt, rộng, hồng nhạt', 'Vùng vỏ trong, khô, rộng, hồng nhạt']
  line    234 | Medium      | id d02599e972d842fc9771c43d6bad24b1 | A -> Vùng vỏ đục, ướt, rộng, hồng nhạt
  line  10460 | Medium      | id 403d7ed36ecc4798bad9b1cf3838cc1b | A -> Vùng vỏ đục, ướt, rộng, hồng nhạt

### Group 70 — topic: Nephrology, Urology
Q: Chẩn đoán xác định đái máu vi thể dựa vào
Options (shared set): ['Nghiệm pháp 3 cốc', 'Nghiệm pháp 2 cốc', 'Nghiệm pháp pha loãng nước tiểu', 'Nghiệm pháp đếm cặn Addis']
  line    245 | Medium      | id ceef9b92d61444c2862efe353e2680b1 | D -> Nghiệm pháp đếm cặn Addis
  line  10443 | Medium      | id 57bc7bd7b7a14ec99683fec11c7d2ae9 | D -> Nghiệm pháp đếm cặn Addis

### Group 71 — topic: Infectious Diseases, Gastroenterology, Urology, Obstetrics and Gynecology
Q: 1 đáp án) Đơn bào chuyển động bằng roi là
Options (shared set): ['Balantidium. Coli', 'Dientamoeba', 'Giardia intestinalis và Trichomonas vaginalis.', 'E.histolytica']
  line    255 | Easy        | id 88a3ba3346914a9e810d8870515b3480 | C -> Giardia intestinalis và Trichomonas vaginalis.
  line  10480 | Easy        | id b9b14df389334e61b8f6e3b5f95cd542 | C -> Giardia intestinalis và Trichomonas vaginalis.

### Group 72 — topic: Urology, Endocrinology
Q: Nhóm vitamin nào sau đây không có tác dụng kích thích sinh tinh:
Options (shared set): ['Vitamin A', 'Vitamin B.', 'Vitamin C.', 'Vitamin E.']
  line    272 | Medium      | id 5b83d67e196145d9a00df8a80b5b05e4 | A -> Vitamin A
  line   1969 | Medium      | id c9add96645384108b1e33a988551451e | A -> Vitamin A
  line   7118 | Medium      | id 640539d6abce44f4b038f4db54fc9781 | A -> Vitamin A

### Group 73 — topic: Urology
Q: Yếu tố nào sau đây ảnh hưởng đến khả năng sinh sản ở nam?
Options (shared set): ['Bất thường về sinh tinh', 'Bất thường về chức năng tình dục', 'Rối loạn nội tiết', 'Tất cả các câu trên đều đúng']
  line    277 | Medium      | id 3f30c2bebc3c4cd5bd232c684636ad52 | D -> Tất cả các câu trên đều đúng
  line  10420 | Medium      | id a7d5d0e2555a422fad0539a524873356 | D -> Tất cả các câu trên đều đúng

### Group 74 — topic: Obstetrics and Gynecology, Urology
Q: Thực hiện thụ tinh trong ống nghiệm bằng kỹ thuật ICSI, người ta có thể sử dụng giao tử đực là:
Options (shared set): ['Từ tinh nguyên bào trở đi', 'Từ tinh bào I trở đi', 'Từ tinh tử trở đi', 'Từ tinh trùng thu thập ở tinh hoàn trở đi']
  line    282 | Medium      | id 8ff3b9a4c11c455ab4faaa61a6d0e45b | C -> Từ tinh tử trở đi
  line  10478 | Medium      | id 960c5f8beedd4a9cb549780d7ebd36be | C -> Từ tinh tử trở đi

### Group 75 — topic: Obstetrics and Gynecology, Infectious Diseases, Urology
Q: Yếu tố nào KHÔNG là nguy cơ của thai ngoài tử cung:
Options (shared set): ['Các bệnh lây truyền qua đường tình dục', 'Các nhiễm trùng đường tiết niệu', 'Nạo phá thai', 'Sử dụng các biện pháp tránh thai: đặt vòng, thuốc tránh thai...']
  line    284 | Medium      | id 47c9edd0d5a349a09e9bbfd84888f112 | B -> Các nhiễm trùng đường tiết niệu
  line   3734 | Medium      | id a9b901e3dcb447708f22a09641941497 | B -> Các nhiễm trùng đường tiết niệu

### Group 76 — topic: Urology, Oncology, Pathology
Q: Trong ung thư biểu mô thận, típ mô bệnh học nào hay gặp nhất?
Options (shared set): ['Típ tuyển', 'Típ ổng', 'Típ tế bào nhẫn', 'Típ tế bào sáng']
  line    288 | Medium      | id 4d209c99c3b548519e2fbf485244a7ad | D -> Típ tế bào sáng
  line    291 | Medium      | id f97efb3ee9f14d5a8072c6bcf72735b1 | D -> Típ tế bào sáng

### Group 77 — topic: Urology, Oncology
Q: Ung thư biểu mô tuyến tiền liệt nếu không được tầm soát, phát hiện sớm sẽ tiến triển âm thầm và có thể bệnh chỉ được phát hiện, xác định khi tế bào u đã lan rộng hay di căn đến mô và cơ quan kế cận. Các mô và cơ quan kế cận thường gặp trong ung thư tuyến tiền liệt thường gặp nhất là gì?
Options (shared set): ['Xâm nhập mô của tuyến tiền liệt, lan rộng đến túi tinh, đại tràng, bàng quang', 'Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, đại tràng, bàng quang', 'Xâm nhập mô tuyến tiền liệt, lan rộng đến túi tinh, đại tràng, cột sống cùng cụt', 'Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, trực tràng, cột sống cùng cụt.']
  line    289 | Medium      | id cedee93db5ad4f5fb6b941bba7f41658 | D -> Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, trực tràng, cột sống cùng cụt.
  line   2015 | Medium      | id 76336bc395b34caf82851e45590e68b4 | B -> Xâm nhập vỏ bao của tuyến tiền liệt, lan rộng đến túi tinh, đại tràng, bàng quang

### Group 78 — topic: Urology, Oncology, Pathology
Q: Ung thư biểu mô tế bào thận xâm lấn theo kiểu?
Options (shared set): ['Gieo hạt', 'Nẩy chồi', 'Chia nhánh', 'Vết dầu loang']
  line    298 | Medium      | id 08531b190cb54171a26246bad79d9070 | B -> Nẩy chồi
  line   2155 | Medium      | id eaec542c585c4f89836d26c47d08b8b4 | C -> Chia nhánh

### Group 79 — topic: Endocrinology, Urology
Q: Nguồn giàu prostagladin nhất ở nam giới là gì?
Options (shared set): ['Nước tiểu', 'Dịch não tuỷ', 'Tinh dịch', 'Máu']
  line    300 | Easy        | id 257748c5bda646568021168dfaa3a097 | C -> Tinh dịch
  line   7152 | Medium      | id a80c0d430de2489c86abf354bdd3430b | C -> Tinh dịch

### Group 80 — topic: Oncology, Urology
Q: Hút thuốc lá làm tăng nguy cơ tử vong của loại UT nào do làm tăng nguy cơ phát triển ác tính của loại UT này?
Options (shared set): ['UT gan', 'UT tuyến thượng thận', 'UT tiền liệt tuyến', 'UT tụy']
  line    301 | Medium      | id bf58f600f30c456ba73604bfbe613fe5 | D -> UT tụy
  line   2299 | Medium      | id b441984a74c844988652e0b6f2df8f47 | C -> UT tiền liệt tuyến

### Group 81 — topic: Obstetrics and Gynecology, Pediatrics, Urology
Q: Thành phần không tham gia tạo ra những đường sinh dục trung tính:
Options (shared set): ['Dây nối niệu sinh dục.', 'ống trung thận ngang.', 'ống trung thận dọc và ống cận trung thận.', 'Xoang niệu-sinh dục.']
  line    303 | Easy        | id 0104a4e467d844279d62d42a69ac8527 | B -> ống trung thận ngang.
  line   2347 | Medium      | id a43fb2af153948baa809acfe52ab6c0a | B -> ống trung thận ngang.
  line   4006 | Medium      | id 78abe370056e4d0187ab9d7bb7197d38 | B -> ống trung thận ngang.

### Group 82 — topic: Obstetrics and Gynecology, Pediatrics, Urology
Q: Xoang niệu sinh dục không tạo ra đoạn:
Options (shared set): ['Đoạn bàng quang.', 'Đoạn chậu.', 'Đoạn sinh dục.', 'Đoạn củ sinh dục.']
  line    304 | Easy        | id 356cd40cb0be4c328430de1490b8d112 | D -> Đoạn củ sinh dục.
  line   2348 | Medium      | id 5af210c3afa941028e70b66aa14ebf0e | D -> Đoạn củ sinh dục.
  line   4007 | Medium      | id 7eaa670155c44bdab859f6d6299c6731 | D -> Đoạn củ sinh dục.

### Group 83 — topic: Nephrology, Pediatrics, Urology
Q: Thời gian xuất hiện của trung thận:
Options (shared set): ['Cuối tuần thứ 3.', 'Cuối tuần thứ 4.', 'Cuối tuần thứ 5.', 'Cuối tuần thứ 6.']
  line    307 | Easy        | id 5f5c7174642f4d69878c48127234c59b | B -> Cuối tuần thứ 4.
  line  11701 | Easy        | id d7becbe14f9a4f81b1c9f01f19001a37 | A -> Cuối tuần thứ 3.

### Group 84 — topic: Nephrology, Urology
Q: Một bệnh nhân mắc bệnh sỏi thận. Bác sĩ chỉ định làm xét nghiệm định lượng hàm lượng Ca2+ trong nước tiểu. Phương pháp phân tích nào được sử dụng để định lượng Ca2+?
Options (shared set): ['Phương pháp complexon', 'Phương pháp pemanganat', 'Phương pháp axit – bazo', 'Phương pháp kết tủa']
  line    318 | Medium      | id be22af7e29e241b9ab2ba3c993dc9806 | A -> Phương pháp complexon
  line    319 | Medium      | id 14d16e9556e1443b97c4424edd392d8c | A -> Phương pháp complexon

### Group 85 — topic: Urology, Infectious Diseases
Q: Bệnh nhân nam 45 tuổi đến khám với triệu chứng có ít dịch niệu đạo vào buổi sáng trước khi đi tiểu, thường chỉ có 1 giọt, cảm giác nóng, buốt nhẹ. Để chẩn đoán bệnh cần làm thêm xét nghiệm nào?
Options (shared set): ['PCR.', 'Soi trực tiếp', 'Clue cell', 'Nuôi cấy']
  line    320 | Challenging | id 7b8de4bb2df54b3ba0873e726a59ee65 | A -> PCR.
  line    346 | Challenging | id 7d60c77bf3204d90a4595a041db99cfc | A -> PCR.

### Group 86 — topic: Urology, Infectious Diseases
Q: Bệnh nhân nam 50 tuổi được chẩn đoán lậu mạn. Xét nghiệm nào được khuyến cáo nên làm ở bệnh nhân này?
Options (shared set): ['PCR.', 'Soi trực tiếp.', 'Nuôi cấy.', 'Clue cell.']
  line    321 | Challenging | id 857f3e0fde5247b1aef87973bb860038 | C -> Nuôi cấy.
  line    347 | Challenging | id bf4a842834f74578b430b95ee8432028 | C -> Nuôi cấy.

### Group 87 — topic: Urology, Infectious Diseases, Internal Medicine
Q: Bệnh nhân nam 25 tuổi đến khám với triệu chứng mệt, đại tiện táo, cảm giác nặng ở trực tràng, đái rắt hoặc bí đái, sốt 38 - 39°C, thăm trực tràng thấy tiền liệt tuyến to, Phác đồ điều trị nào sau đây phù hợp nhất với tình trạng bệnh trên?
Options (shared set): ['Ceftriaxone 1g/ngày. Clarithromycin 250mg/ngày.', 'Ceftriaxon 250mg tiêm liều duy nhất. Clarithromycin 250mg/ngày.', 'Ceftriaxon 250mg tiêm liều duy nhất. Clarithromycin 500mg/ngày.', 'Ceftriaxon 1g/ngày. Clarithromycin 500mg/ngày.']
  line    322 | Challenging | id 8da129703ae84884be6e6fa3bb657b04 | D -> Ceftriaxon 1g/ngày. Clarithromycin 500mg/ngày.
  line    340 | Challenging | id 0beffa3711434b51b633e57a19a1cb95 | D -> Ceftriaxon 1g/ngày. Clarithromycin 500mg/ngày.

### Group 88 — topic: Urology, Infectious Diseases, Internal Medicine
Q: Bệnh nhân nam 30 tuổi đến khám vì biểu hiện bằng tinh hoàn 1 bên sưng to, viêm nóng đỏ và rất đau, đau tăng khi đi lại, toàn thân sốt cao 39 - 40°c. Phác đồ điều trị nào sau đây phù hợp nhất với tình trạng bệnh trên?
Options (shared set): ['Ceftriaxon 1g/ngày. Erythromycin 500mg/ngày x 4 lần/ngày.', 'Ceftriaxon 250mg tiêm liều duy nhất. Erythromycin 500mg/ngày x2 lần/ngày.', 'Ceftriaxon 250mg tiêm liều duy nhất. Erythromycin 250mg/ngày x 4 lần/ngày.', 'Ceftriaxon 1g/ngày. Erythromycin 250mg/ngày x 2 lần/ngày']
  line    323 | Challenging | id 9c9a0e14809347d288fa95fd89bab857 | A -> Ceftriaxon 1g/ngày. Erythromycin 500mg/ngày x 4 lần/ngày.
  line    335 | Challenging | id 22bedd25d9ac4e19b466fd65f5fb93e1 | A -> Ceftriaxon 1g/ngày. Erythromycin 500mg/ngày x 4 lần/ngày.
  line    349 | Challenging | id 991829639ea94bc4a79cc821aaecf58c | A -> Ceftriaxon 1g/ngày. Erythromycin 500mg/ngày x 4 lần/ngày.

### Group 89 — topic: Urology, Infectious Diseases, Internal Medicine
Q: Bệnh nhân nam 20 tuổi, tiền sử quan hệ với gái mại dâm đến khám với triệu chứng đái buốt, đái rắt, tiết dịch đục ở niệu đạo. Phác đồ điều trị nào sau đây phù hợp nhất với tình trạng bệnh trên?
Options (shared set): ['Ceftriaxon 250mg tiêm liều duy nhất. Azithromycin 1g x 1 lần/ngày', 'Ceftriaxon 500mg uống liều duy nhất. Azithromycin 1g x 1 lần/ngày', 'Spectinomycin 2g liều duy nhất. Azithromycin 2g x 1 lần/ngày', 'Ceftriaxon 500mg tiêm liều duy nhất. Azithromycin 2g x 1 lần/ngày']
  line    324 | Challenging | id a55a0602c6e24de09bda05bd42cd9a78 | A -> Ceftriaxon 250mg tiêm liều duy nhất. Azithromycin 1g x 1 lần/ngày
  line    350 | Challenging | id e0b7b1abac9f497ba9b460f50f4559fb | A -> Ceftriaxon 250mg tiêm liều duy nhất. Azithromycin 1g x 1 lần/ngày
  line    355 | Challenging | id 7339d3f0882e44e6b1e78e1674f671f3 | A -> Ceftriaxon 250mg tiêm liều duy nhất. Azithromycin 1g x 1 lần/ngày

### Group 90 — topic: Urology, Infectious Diseases, Internal Medicine
Q: Bệnh nhân nam 20 tuổi, sau khi hoàn thành điều trị lậu cấp, khoảng 3 ngày nay bệnh nhân thấy xuất hiện các triệu chứng đái buốt, đái rắt, tiết dịch đục ở niệu đạo. Phác đồ điều trị nào sau đây phù hợp nhất với tình trạng bệnh trên?
Options (shared set): ['Ceftriaxon 500mg uống liều duy nhất + Azithromycin 2g uống liều duy nhất', 'Ceftriaxon 800mg uống liều duy nhất + Azithromycin 2g uống liều duy nhất', 'Ceftriaxon 800mg uống liều duy nhất + Azithromycin 1g uống liều duy nhất', 'Ceftriaxon 500mg uống liều duy nhất + Azithromycin 1g uống liều duy nhất']
  line    325 | Challenging | id d35bf444294042ff84bc6b7c17a8ac66 | A -> Ceftriaxon 500mg uống liều duy nhất + Azithromycin 2g uống liều duy nhất
  line    339 | Challenging | id c6e6c200f0d643eabca76836dfc4b199 | A -> Ceftriaxon 500mg uống liều duy nhất + Azithromycin 2g uống liều duy nhất

### Group 91 — topic: Urology, Infectious Diseases, Internal Medicine
Q: Bệnh nhân nam 20 tuổi, sau khi hoàn thành điều trị lậu cấp, khoảng 3 ngày nay bệnh nhân thấy xuất hiện các triệu chứng đái buốt, đái rắt, tiết dịch dục ở niệu đạo. Phác đồ điều trị nào sau đây phù hợp nhất với tình trạng bệnh trên?
Options (shared set): ['Gentamycin 240mg + Azithromycin 1g uống liều duy nhất.', 'Gentamycin 250mg + Azithromycin 1g uống liều duy nhất.', 'Gentamycin 250mg + Azithromycin 2g uống liều duy nhất.', 'Gentamycin 240mg + Azithromycin 2g uống liều duy nhất.']
  line    326 | Challenging | id 217e9c4c43394b66a4b3b7dfd2be439c | D -> Gentamycin 240mg + Azithromycin 2g uống liều duy nhất.
  line    333 | Challenging | id 8c7884fd50d14c92acf31645582739e4 | D -> Gentamycin 240mg + Azithromycin 2g uống liều duy nhất.
  line    351 | Challenging | id a48a06d532fa473ba8b3e9eea61849db | D -> Gentamycin 240mg + Azithromycin 2g uống liều duy nhất.

### Group 92 — topic: Urology, Infectious Diseases, Internal Medicine
Q: Bệnh nhân nam 20 tuổi, sau khi hoàn thành điều trị lậu cấp, khoảng 3 ngày nay bệnh nhân thấy xuất hiện các triệu chứng đái buốt, đái rắt, tiết dịch đục ở niệu đạo. Phác đồ điều trị nào sau đây phù hợp nhất với tình trạng bệnh trên?
Options (shared set): ['Spectinomycin 2g liều duy nhất. Azithromycin 2g uống liều duy nhất', 'Spectinomycin 2g liều duy nhất. Azithromycin 1g uống liều duy nhất', 'Spectinomycin 1g liều duy nhất. Azithromycin 2g uống liều duy nhất', 'Spectinomycin Ig liều duy nhất. Azithromycin 2g uống liều duy nhất']
  line    327 | Challenging | id 264f8cf328354b3ab67b423c633fc16d | A -> Spectinomycin 2g liều duy nhất. Azithromycin 2g uống liều duy nhất
  line    334 | Challenging | id 28042d5fb157446eb46a8fe242816186 | A -> Spectinomycin 2g liều duy nhất. Azithromycin 2g uống liều duy nhất
  line    352 | Challenging | id 80d2a80f541f40f6a392732c22776131 | A -> Spectinomycin 2g liều duy nhất. Azithromycin 2g uống liều duy nhất

### Group 93 — topic: Urology, Infectious Diseases, Internal Medicine
Q: Bệnh nhân nam 20 tuổi, sau khi hoàn thành điều trị lậu cấp, khoảng 3 ngày nay bệnh nhân thấy xuất hiện các triệu chứng đái buốt, đái rắt, tiết dịch đục ở niệu đạo. Phác đồ điều trị nào sau đây phù hợp nhất với tình trạng bệnh trên?
Options (shared set): ['Ceftriaxon 500mg liều duy nhất + Azithromycin 1g uống liều duy nhất.', 'Ceftriaxon 250 mg liều duy nhất + Azithromycin 1g uống liều duy nhất.', 'Ceftriaxon 500mg liều duy nhất + Azithromycin 2g uống liều duy nhất.', 'Ceftriaxon 250mg liều duy nhất + Azithromycin 2g uống liều duy nhất.']
  line    328 | Challenging | id 38e201b677704d87b2dc8ce617d4bb22 | C -> Ceftriaxon 500mg liều duy nhất + Azithromycin 2g uống liều duy nhất.
  line    353 | Challenging | id 945f1ad4d59740efa261375635ed9bb0 | C -> Ceftriaxon 500mg liều duy nhất + Azithromycin 2g uống liều duy nhất.

### Group 94 — topic: Urology, Infectious Diseases, Internal Medicine
Q: Bệnh nhân nam 30 tuổi đến khám vì đi tiểu nóng rát, đái buốt như dao khía, ra dịch đục ngày thứ 7 của bệnh, không sốt. Phác đồ điều trị nào sau đây phù hợp nhất với tình trạng bệnh trên?
Options (shared set): ['Ceftriaxon uống 800 mg liều duy nhất + Tetracyclin 500mg x 4 lần/ngày x 7 ngày', 'Ceftriaxon uống 400 mg liều duy nhất + Tetracyclin 500mg x 2 lần/ngày x 7 ngày', 'Ceftriaxon uống 800 mg liều duy nhất + Tetracyclin 500mg x 2 lần/ngày x 7 ngày', 'Ceftriaxon uống 400 mg liều duy nhất + Tetracyclin 500mg x 4 lần/ngày x 7 ngày']
  line    330 | Challenging | id 9657abbab49440f3a5ca2dbd51c83edd | D -> Ceftriaxon uống 400 mg liều duy nhất + Tetracyclin 500mg x 4 lần/ngày x 7 ngày
  line  10415 | Challenging | id 4306f8b5422347bea8a37a487144f1d3 | D -> Ceftriaxon uống 400 mg liều duy nhất + Tetracyclin 500mg x 4 lần/ngày x 7 ngày

### Group 95 — topic: Urology, Infectious Diseases, Internal Medicine
Q: Bệnh nhân nam 30 tuổi đến khám vì đi tiểu nóng rát, đái buốt như dao khía, ra dịch đục ngày thứ 7 của bệnh, không sốt. Phác đồ điều trị nào sau đây phù hợp nhất với tỉnh trạng bệnh trên?
Options (shared set): ['Ceftriaxone uống 800 mg liều duy nhất + Clarithromycin 250mg x 2 lần/ngày', 'Ceftriaxone uống 400mg liều duy nhất + Clarithromycin 250mg x 4 lần/ngày', 'Ceftriaxone uống 400mg liều duy nhất + Clarithromycin 250mg x 2 lần/ngày', 'Ceftriaxone uống 800mg liều duy nhất + Clarithromycin 250mg x 4 lần/ngày']
  line    331 | Challenging | id b979dabbf7564900a0f95fcbc665e948 | C -> Ceftriaxone uống 400mg liều duy nhất + Clarithromycin 250mg x 2 lần/ngày
  line    332 | Challenging | id 7f24132cebc0408d93533a8a68df64d2 | C -> Ceftriaxone uống 400mg liều duy nhất + Clarithromycin 250mg x 2 lần/ngày
  line    338 | Challenging | id 8bd5ec68b0774c0a91382aef32586d24 | C -> Ceftriaxone uống 400mg liều duy nhất + Clarithromycin 250mg x 2 lần/ngày

### Group 96 — topic: Urology, Infectious Diseases
Q: Bệnh nhân nam 45 tuổi đến khám với triệu chứng có ít dịch niệu đạo vào buổi sáng trước khi đi tiểu, thường chỉ có 1 giọt, cảm giác nóng, buốt nhẹ. Chẩn đoán nguyên nhân gây viêm niệu đạo nào phù hợp nhất với tình trạng bệnh trên?
Options (shared set): ['Candida.', 'Trùng roi.', 'Vi khuẩn.', 'Vi rút.']
  line    336 | Challenging | id 6dafeec4032b4b4fa2715610862e2f9c | C -> Vi khuẩn.
  line    343 | Challenging | id 9184c3b18afa4fce9da53d1607b5003e | C -> Vi khuẩn.

### Group 97 — topic: Urology, Infectious Diseases
Q: Bệnh nhân nam 30 tuổi đến khám vì nhôn nhốt ở niệu đạo, tiết dịch đục ngày thứ 6 của bệnh. Cần làm xét nghiệm nào để chẩn đoán bệnh?
Options (shared set): ['PCR', 'Clue', 'Nhuộm soi trực tiếp.', 'Nuôi cấy.']
  line    337 | Challenging | id 9b69f6f4faff4d67ab70ea88af62a476 | C -> Nhuộm soi trực tiếp.
  line    345 | Challenging | id 4a291c27d2a2495dbd7e453fc39a469d | C -> Nhuộm soi trực tiếp.

### Group 98 — topic: Infectious Diseases, Urology
Q: Bệnh nhân nam 30 tuổi đến khám vì nhôn nhốt ở niệu đạo, tiết dịch đục ngày thứ 3 của bệnh. Chẩn đoán nguyên nhân gây ra tình trạng viêm niệu đạo nào sau đây là phù hợp nhất?
Options (shared set): ['Lậu', 'Trùng roi', 'Tạp khuẩn.', 'Nấm Candida.']
  line    348 | Challenging | id 1d5aec4a8f38415790a65ddd6a096875 | A -> Lậu
  line   2422 | Challenging | id 6b040fa3c7b34bce9a7a6011c9ebd1a4 | A -> Lậu

### Group 99 — topic: Endocrinology, Gastroenterology
Q: Phát biểu nào sai về dùng thuốc phối hợp khi uống Corticoid?
Options (shared set): ['Kháng sinh nếu có nhiễm khuẩn', 'Giảm liều insulin ở bệnh nhân đái tháo đường', 'Uống thuốc chống loét dạ dày tá tràng (cách xa nhau)', 'Tất cả đều sai']
  line    356 | Medium      | id df977d3aaab542f383707363f3f3f6fc | B -> Giảm liều insulin ở bệnh nhân đái tháo đường
  line   7183 | Medium      | id 8f7b719a437c4e668a4e3263514d60f5 | B -> Giảm liều insulin ở bệnh nhân đái tháo đường

### Group 100 — topic: Gastroenterology, Radiology
Q: Dạ dày bị chèn đẩy khi:
Options (shared set): ['Đảo ngược các phủ tạng.', 'Có bệnh lý bên trong dạ dày.', 'Có bệnh lý ở thành dạ dày.', 'Khi có bất thường ở các tạng lân cận.']
  line    412 | Medium      | id 552ea295d3ec4aceb28e0ff6554e28f3 | D -> Khi có bất thường ở các tạng lân cận.
  line    474 | Medium      | id 18869db0b71449aeb76db6f2b2acb2ba | D -> Khi có bất thường ở các tạng lân cận.
  line   1101 | Medium      | id 699c4e92d42f474c9272d22798fcc5d5 | D -> Khi có bất thường ở các tạng lân cận.

### Group 101 — topic: Gastroenterology, Radiology
Q: Trên hình ảnh X quang, ổ loét dạ dày là:
Options (shared set): ['Ổ đọng thuốc, cố định thường xuyên', 'Ổ đục khoét vào thành dạ dày', 'Hình lồi không cố định, thường xuyên', 'Hình lồi không cố định, không thường xuyên']
  line    416 | Medium      | id af96c476310a44b1915e1404145dd35b | A -> Ổ đọng thuốc, cố định thường xuyên
  line   1103 | Medium      | id 9e58b5d57f7d4dd6a748572ddd16b91e | A -> Ổ đọng thuốc, cố định thường xuyên

### Group 102 — topic: Gastroenterology, Radiology
Q: Các hình ảnh sau, đâu là hình ảnh của túi thừa thực quản?
Options (shared set): ['Hình ảnh túi cản quang có cổ dính vào thành thực quản, thường nằm ở 1/3 giữa hoặc ngay trên cơ hoành.', 'Thực quản giống hình củ cải hay hình mũi kiếm, chụp baryte thấy thực quản bị hẹp ngay ở tâm vị, thẳng trục, phía trên giãn to đều.', 'Có các hình sáng tròn tập trung như chùm nho hoặc các vệt sáng dài ngoằn ngoèo, đôi khi tạo hình ảnh giả u.']
  line    422 | Easy        | id 9b351b93823246aeaa617c5b6a898001 | A -> Hình ảnh túi cản quang có cổ dính vào thành thực quản, thường nằm ở 1/3 giữa hoặc ngay trên cơ hoành.
  line   9156 | Medium      | id 498272fa659f438e89725677fd39b091 | A -> Hình ảnh túi cản quang có cổ dính vào thành thực quản, thường nằm ở 1/3 giữa hoặc ngay trên cơ hoành.

### Group 103 — topic: Gastroenterology, Radiology
Q: Phương pháp chẩn đoán hình ảnh tốt nhất với polyp túi mật là
Options (shared set): ['Siêu âm', 'XQ', 'CT', 'khác']
  line    425 | Easy        | id 848dd1d01d054462967206b12d7c0ae3 | A -> Siêu âm
  line   8606 | Easy        | id a0c9abfcd6ef49bbaf859c777d8c40d5 | A -> Siêu âm

### Group 104 — topic: Infectious Diseases, Gastroenterology
Q: Triệu chứng lâm sàng trong bệnh giun, sán ký sinh đóng vai trò:
Options (shared set): ['Định hướng trong chẩn đoán', 'Chuẩn đoán xác định bệnh', 'Chuẩn đoán nguyên nhân gây bệnh', 'Quyết định trong chuẩn đoán']
  line    450 | Easy        | id 625a53dc8e244a729c2e77c9e3631f5f | A -> Định hướng trong chẩn đoán
  line   9403 | Medium      | id 0bd97cdd531f4f75b064c006a74ed314 | A -> Định hướng trong chẩn đoán

### Group 105 — topic: Infectious Diseases, Gastroenterology
Q: Đường xâm nhập của mầm bệnh giun sán vào vật chủ gồm:
Options (shared set): ['Đường tiêu hóa, đường máu và qua da', 'Tất cả đều đúng', 'Đường tiêu hóa, đường máu và đường sinh dục', 'Đường sinh dục, đường máu và qua da']
  line    454 | Easy        | id 25aa59900e7d44c7bdc4a25fb4e9e088 | A -> Đường tiêu hóa, đường máu và qua da
  line   9430 | Easy        | id 057aef6c73a04bd992c30cace0307cc3 | A -> Đường tiêu hóa, đường máu và qua da

### Group 106 — topic: Gastroenterology, Internal Medicine
Q: Lách to kèm bụng báng thường gặp trong
Options (shared set): ['Tăng áp lực tĩnh mạch cửa do xơ gan', 'Viêm gan cấp', 'Ung thư gan', 'Gan nhiễm mỡ.']
  line    485 | Medium      | id f68adc0e9a92483aa77103cf98a77821 | A -> Tăng áp lực tĩnh mạch cửa do xơ gan
  line  10566 | Medium      | id 41e0dc2a103e4f9db9ff29d153205d85 | A -> Tăng áp lực tĩnh mạch cửa do xơ gan

### Group 107 — topic: Gastroenterology, Surgery
Q: Trong thủng ổ loét dạ dày tá tràng, gõ đục vùng thấp chứng tỏ có dịch khu trú trong ổ bụng đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line    494 | Medium      | id 632023909ec9477cb34970d95afe1926 | B -> Sai
  line    528 | Medium      | id d22c07cbb24543e4be2da89f5feeca4e | B -> Sai

### Group 108 — topic: Gastroenterology, Surgery
Q: Trong thủng ổ loét dạ dày tá tràng có triệu chứng cơ năng sau: Đau thường phải gập người lại, không dám cử động mạnh. Đau từng cơn, lan ra khắp ổ bụng?
Options (shared set): ['Đúng', 'Sai']
  line    495 | Medium      | id 936a2a0db3294f538230248f191f0b4f | B -> Sai
  line    529 | Medium      | id 4ebce568569c4cb89f13537a8f4b8de9 | B -> Sai.
  line    569 | Medium      | id 7bae55270f7e406eb5acd1ffb5db7da1 | B -> Sai

### Group 109 — topic: Gastroenterology, Surgery
Q: Trong thủng ổ loét dạ dày - tá tràng thì dấu hiệu bụng cứng như gỗ, co cứng thành bụng là một triệu chứng bao giờ cũng có nhưng ở mức độ khác nhau và có giá trị bậc nhất trong chẩn đoán?
Options (shared set): ['Đúng', 'Sai']
  line    496 | Medium      | id 17185163e3084528986b06cda2572fc4 | A -> Đúng
  line    530 | Medium      | id 3a4475c5386d43d88c3205b851b97868 | A -> Đúng
  line    570 | Medium      | id c6f76e0e742b46a8a9d8d9bb4d66e3c4 | A -> Đúng

### Group 110 — topic: Gastroenterology, Surgery
Q: Một trong những dấu hiệu phân biệt thủng ổ loét dạ dày tá tràng với viêm phúc mạc ruột thừa là “sốt” đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line    497 | Challenging | id 97c9fc125a3a47918c966cba278961f2 | A -> Đúng
  line    531 | Challenging | id 68c3bd9400ff4df9b5490806f03baee1 | A -> Đúng

### Group 111 — topic: Gastroenterology, Radiology
Q: Trên thực tế, để chẩn đoán thủng ổ loét dạ dày tá tràng người ta thường bơm thuốc cản quang chụp dạ dày tá tràng, nếu thấy thuốc thoát ra ngoài ổ bụng thì chẩn đoán thủng ổ loét dạ dày tá tràng đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line    498 | Medium      | id 4576ecfc94b74e3194994c2231d901f3 | B -> Sai
  line    532 | Medium      | id fc97e531b3a442a7a0fa0bd5069e30e6 | B -> Sai.
  line    571 | Medium      | id 88914ada4e20434b93ec2087ca44b743 | B -> Sai

### Group 112 — topic: Gastroenterology, Surgery
Q: Điều trị thủng ổ loét dạ dày - tá tràng bằng phương pháp hút liên tục không mổ là một phương pháp đơn giản nhưng có nhiều nhược điểm nên chỉ định rất giới hạn?
Options (shared set): ['Đúng', 'Sai']
  line    499 | Medium      | id bdff3501a92442bba7269fa08e1d881a | A -> Đúng
  line    533 | Medium      | id 57689ac1dbaa41b98b92250a205370de | A -> Đúng
  line    572 | Medium      | id 46539222579d409d88fae2f33912e14b | A -> Đúng

### Group 113 — topic: Gastroenterology, Surgery
Q: Trong thủng ổ loét dạ dày - tá tràng thì dấu hiệu bụng cứng như gỗ, co cứng thành bụng là một triệu chứng bao giờ cũng có nhưng ở các mức độ khác nhau và có giá trị bậc nhất trong chẩn đoán?
Options (shared set): ['Đúng', 'Sai']
  line    500 | Medium      | id 588f293d3a86475184a081d14bc01647 | A -> Đúng
  line    534 | Medium      | id 55d2bd392bd24274b3c86c1edc523f1a | A -> Đúng
  line    573 | Medium      | id ed3b55d713dc4b6289144a91dbd8e690 | A -> Đúng

### Group 114 — topic: Gastroenterology, Surgery
Q: Trong thủng ổ loét dạ dày - tá tràng thì bí trung, đại tiện là một dấu hiệu muộn vì thường là nó biểu hiện một tình trạng viêm phúc mạc toàn thể làm liệt ruột, ruột mất nhu động?
Options (shared set): ['Đúng', 'Sai']
  line    501 | Medium      | id ad0141ac4cfd41809bf52211a6146ec9 | A -> Đúng
  line    535 | Medium      | id 680fd3c5ecdd4aed81eecfa578230207 | A -> Đúng
  line    574 | Medium      | id 8fa46e7ad8344be39e074b0906f5a0c0 | A -> Đúng

### Group 115 — topic: Gastroenterology, Radiology
Q: Trong thủng dạ dày - tá tràng việc chụp X quang bụng không chuẩn bị để tìm liềm hơi dưới cơ hoành là cần thiết và bắt buộc?
Options (shared set): ['Đúng', 'Sai']
  line    502 | Medium      | id 64c7a6350bbd4a9ba335b2eda1b75a4e | A -> Đúng
  line    536 | Medium      | id 071179813c854d428214022a8bd938cb | A -> Đúng
  line    575 | Medium      | id b618f3685d2d46398f53653e60ee9057 | A -> Đúng

### Group 116 — topic: Gastroenterology
Q: Thẩm mật phúc mạc là tình trạng viêm phúc mạc do đường mật bị thủng, dịch mật vào ổ bụng gây viêm phúc mạc, đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line    504 | Easy        | id eb114506844841ca828af281013ec642 | B -> Sai
  line    577 | Easy        | id b1aa7a29eba143c3b9cd77c21c498fc2 | B -> Sai

### Group 117 — topic: Gastroenterology, Surgery
Q: Sỏi ống mật chủ được chỉ định mổ cấp cứu là tốt nhất?
Options (shared set): ['Đúng', 'Sai']
  line    506 | Medium      | id 98d1acc664b34c56acc80891283e56a0 | B -> Sai
  line    579 | Challenging | id 31c3a849e0e14d9a9c395dbb50789a63 | B -> Sai
  line   1818 | Challenging | id a55b3bf270014a689ed635b76b456a6c | B -> Sai

### Group 118 — topic: Gastroenterology, Surgery
Q: Sỏi ống mật chủ đơn thuần nằm ở vị trí trên cơ vòng Oddi chỉ định làm ERCP là hợp lý nhất?
Options (shared set): ['Đúng', 'Sai']
  line    507 | Medium      | id 9128005b98a84096b04620cb7180decb | A -> Đúng
  line    580 | Challenging | id 345d3635104d49da9ae665fa20fad2ee | A -> Đúng
  line   1819 | Challenging | id 3b3260e126de4821b4eda6efbfde90d6 | A -> Đúng

### Group 119 — topic: Surgery, Gastroenterology
Q: Áp xe ruột thừa là áp xe không có vỏ bọc?
Options (shared set): ['Đúng', 'Sai']
  line    512 | Easy        | id 3bd0908a0c384a2f9e8aff0d50a39020 | B -> Sai
  line    545 | Easy        | id 7fed9ecdc76f4c45919eb0585d9b356d | B -> Sai

### Group 120 — topic: Surgery, Gastroenterology
Q: Khi chẩn đoán là đám quánh ruột thừa thì có chỉ định mổ ngay?
Options (shared set): ['Đúng', 'Sai']
  line    513 | Medium      | id 93dc58b0aafd4efb9434a02597c4fd6c | B -> Sai
  line    546 | Medium      | id 5a0a07833ac7466795a147d2ed05a1a3 | B -> Sai

### Group 121 — topic: Surgery, Gastroenterology
Q: Ruột thừa là một phần của ống tiêu hoá không đảm nhiệm một chức năng sinh lý gì của cơ thể?
Options (shared set): ['Đúng', 'Sai']
  line    514 | Easy        | id 2adb1d5e23214ec1b44e08f727be3fe1 | B -> Sai
  line    547 | Easy        | id ded139d6c95241dcbca0c76bc09cca10 | B -> Sai
  line    583 | Easy        | id 0d9961810d554302a10deee2ffaaff8e | B -> Sai

### Group 122 — topic: Oncology, Gastroenterology
Q: Ung thư dạ dày thường được phát hiện sớm vì triệu chứng lâm sàng thường rõ ràng và điển hình?
Options (shared set): ['Đúng', 'Sai']
  line    515 | Medium      | id 1d052538e42646f0a45a7f7768636324 | B -> Sai
  line    539 | Medium      | id 17c12c58419e4400bc708ef9c4062952 | B -> Sai

### Group 123 — topic: Oncology, Gastroenterology, Radiology
Q: Trong ung thư dạ dày, các triệu chứng lâm sàng chỉ có tính chất gợi ý, để chẩn đoán xác định cần phải chụp X-quang và nội soi sinh thiết?
Options (shared set): ['Đúng', 'Sai']
  line    516 | Medium      | id e79ad0198b2b4fc3baa1bd87950ad609 | A -> Đúng
  line    540 | Medium      | id b647a6a2ee014924b588239e5b36846e | A -> Đúng

### Group 124 — topic: Oncology, Gastroenterology
Q: Trong ung thư dạ dày, nếu được chẩn đoán và phẫu thuật sớm (giai đoạn 0, I) tỷ lệ sống sau 5 năm là > 90%?
Options (shared set): ['Đúng', 'Sai']
  line    517 | Medium      | id 1712aaef301547c2b7ab7b7f7c14593f | B -> Sai
  line    541 | Medium      | id 4058b29f32564cfd9c2cf69c645eb688 | B -> Sai

### Group 125 — topic: Oncology, Gastroenterology
Q: Trong ung thư đại tràng, phân độ theo Dukes được sử dụng nhiều nhất, còn phân độ theo TMN ít sử dụng?
Options (shared set): ['Đúng', 'Sai']
  line    518 | Medium      | id dd5e44391d0f410cafd6448cb55e2bf4 | B -> Sai
  line    586 | Medium      | id 6ed9eadf836940e28b98c0913a008626 | B -> Sai

### Group 126 — topic: Oncology, Gastroenterology
Q: Điều trị hỗ trợ trong ung thư đại tràng bằng đa hoá trị liệu được chỉ định cho các của ung thư theo phân độ của Dukes?
Options (shared set): ['Đúng', 'Sai']
  line    519 | Medium      | id 9eed323bf32945d281a5f91317f8e0da | B -> Sai
  line    556 | Medium      | id 2b6cf52ddc1647cbbd585c92048e78bc | B -> Sai
  line    587 | Medium      | id bb1742bf6c5e4675a15c9d1e68547233 | B -> Sai

### Group 127 — topic: Pediatrics, Gastroenterology, Infectious Diseases
Q: Shigella gây bệnh theo cơ chế xâm nhập niêm mạc:
Options (shared set): ['Đúng', 'Sai']
  line    521 | Easy        | id 3c1eb4637e974162956889955dd13d55 | A -> Đúng
  line    568 | Easy        | id 206238f10ca5437ea0161c9b673ec7b8 | A -> Đúng

### Group 128 — topic: Pediatrics, Gastroenterology
Q: Hỏi kỹ về chất nôn có thể xác định nguyên nhân gây nôn.
Options (shared set): ['Đúng', 'Sai']
  line    523 | Medium      | id 3a26130931cb4fceae6e96f93040f6ff | B -> Sai
  line    561 | Easy        | id ea6d17b29c0346b08fe6f85845baf1bc | B -> Sai
  line    811 | Easy        | id 8484c47290104cf0bf6730096fc53fea | B -> Sai

### Group 129 — topic: Pediatrics, Gastroenterology, Surgery
Q: Dấu hiệu rắn bò kèm theo nôn thường xuất hiện khi trẻ bị hẹp phì đại môn vị.
Options (shared set): ['Đúng', 'Sai']
  line    524 | Medium      | id bba276c1c5cc4067a6bead50c96b7cf4 | B -> Sai
  line    563 | Medium      | id 167bd5c2240944fd964ec125109524b5 | B -> Sai
  line    812 | Medium      | id e3f8cd43f7c646d2918b843d7877c68b | B -> Sai

### Group 130 — topic: Pediatrics, Gastroenterology
Q: Bé Tâm, 3 tháng tuổi, thường bị nôn sau ăn. Để tránh tình trạng nôn, cần phải để Tâm nằm yên sau khi bú
Options (shared set): ['Đúng', 'Sai']
  line    526 | Medium      | id 8083aa233e2644d08ff708500553ff1f | B -> Sai
  line    813 | Medium      | id 370b330d4aa246bb9cc9865a52f4e3fc | B -> Sai

### Group 131 — topic: Gastroenterology
Q: Gan to trong sỏi ống mật có đặc điểm: to đều, mặt nhẵn, bờ sắc, ấn đau tức. đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line    537 | Medium      | id ff6fd5ef6ea3416ba81ddce8ce0cefa9 | B -> Sai
  line    576 | Medium      | id 3ba2ac29f8244c189a03072288c74df4 | B -> Sai

### Group 132 — topic: Gastroenterology
Q: Viêm phúc mạc mật là tình trạng viêm phúc mạc do đường mà dãn, dịch mật thâm qua thành đường mật gây viêm phúc mạc, đúng đến
Options (shared set): ['Đúng', 'Sai']
  line    538 | Easy        | id f38dc24847bf443c8e6882d4e6b0f72d | B -> Sai
  line    578 | Easy        | id ebc625875b944ccc9cb88ebb3a216a03 | B -> Sai

### Group 133 — topic: Gastroenterology, Surgery
Q: Sỏi ống mật chủ kẹt ở cơ vòng Oddi được xem là nguyên nhân chính gây nên viêm tụy cấp:
Options (shared set): ['Đúng', 'Sai']
  line    548 | Medium      | id 675c0decf74c4d02a6e51c1d1a7e0115 | A -> Đúng
  line    584 | Medium      | id 6eccb997589b4d4caa8583cc962a330d | A -> Đúng

### Group 134 — topic: Gastroenterology, Surgery
Q: Hẹp môn vị là một bệnh tiến triển nhanh và lúc đầu có thể xuất hiện từng đợt
Options (shared set): ['Đúng.', 'Sai.']
  line    550 | Medium      | id e44a4758f86e4cac979aa61aee4e8d04 | B -> Sai.
  line    585 | Medium      | id 173420eb281643e18ef6d5bb917e97e6 | B -> Sai

### Group 135 — topic: Pediatrics, Gastroenterology
Q: Thăm khám lâm sàng quan trọng nhất ở trẻ bị táo bón kéo dài là nghe nhu động ruột
Options (shared set): ['Đúng', 'Sai']
  line    565 | Medium      | id fb8bf875a2aa460c98e2879107f024c7 | B -> Sai
  line    816 | Medium      | id c2dd61cbca0c44938f2e982bfb417b78 | B -> Sai

### Group 136 — topic: Gastroenterology, Infectious Diseases
Q: Chọn một câu trả lời đúng. So với lỵ trực khuẩn, bệnh lỵ amips thường có các triệu chứng:
Options (shared set): ['Đau bụng cả hai hố chậu.', 'Đi ngoài nhiều lần hơn.', 'ít bị tái phát.', 'Sốt cao hơn.']
  line    595 | Medium      | id 88b13953f01b4a3f883eed044e17187d | A -> Đau bụng cả hai hố chậu.
  line    602 | Medium      | id 53483aa8dd4d42a5a42f4581d8686193 | A -> Đau bụng cả hai hố chậu.

### Group 137 — topic: Geriatrics, Gastroenterology
Q: Sự thay đổi chức năng sinh lý ống tiêu hóa ở người cao tuổi là
Options (shared set): ['Dòng máu qua tạng giảm', 'Thành phần Lipit giảm', 'Lượng abumin huyết tương giảm', 'Tổng lượng nước cơ thể giảm']
  line    615 | Medium      | id 4dd9e9e8277245ea85f0f10ff0ab1f3e | A -> Dòng máu qua tạng giảm
  line  10804 | Medium      | id 3492257a85b64300b85a97040cd294f8 | A -> Dòng máu qua tạng giảm

### Group 138 — topic: Pediatrics, Gastroenterology, Endocrinology
Q: Nguyên nhân táo bón kéo dài ở trẻ em hay gặp nhất:
Options (shared set): ['Suy giáp trạng', 'C: Đái tháo đường', 'Viêm đại tràng mãn', 'D: Còi xương, suy dinh dưỡng']
  line    632 | Medium      | id 9f1a98b84ae5431b9443a4a4eecd9fc5 | D -> D: Còi xương, suy dinh dưỡng
  line   6086 | Medium      | id 2ea4ba84308740b3977fc67677e048d8 | D -> D: Còi xương, suy dinh dưỡng

### Group 139 — topic: Pediatrics, Gastroenterology
Q: Dấu hiệu rắn bò kèm theo nôn thường xuất hiện khi trẻ bị hẹp phì đại môn vị
Options (shared set): ['Đ', 'S']
  line    636 | Medium      | id 689252dfa0f446c8b580aae453990c6b | B -> S
  line    645 | Medium      | id 3a95bd6bd5bf420c897eddb3113fad8a | B -> S

### Group 140 — topic: Pediatrics, Gastroenterology
Q: Bé Tâm, 3 tháng tuổi, thường bị nôn sau ăn. Để tránh tình trạng nôn, cần phải để Tâm nằm yên sau khi bú
Options (shared set): ['Đ', 'S']
  line    637 | Medium      | id ce71545039d94c80af1f90d40fe39178 | B -> S
  line    646 | Medium      | id c27451add16f4ccaab0c082e59452b49 | B -> S

### Group 141 — topic: Pediatrics, Gastroenterology
Q: Tìm lỗ dò hậu môn-trực tràng cần được thực hiện khi thăm khám trẻ bị táo bón
Options (shared set): ['Đ', 'S']
  line    638 | Medium      | id 0a4b759ae6844f4f8a594d7b01694550 | A -> Đ
  line    647 | Medium      | id c5317dda3e1842c3b38dc341987b89ee | A -> Đ

### Group 142 — topic: Pediatrics, Gastroenterology
Q: Ở trẻ sơ sinh bị táo bón, chậm đào thải phân su là dấu hiệu quan trọng nhất để hướng đến chẩn đoán trẻ bị phình đại tràng bẩm sinh
Options (shared set): ['Đ', 'S']
  line    639 | Medium      | id 514d8b433a1d4d8882fcadefcc101b43 | A -> Đ
  line    648 | Medium      | id 114e064453414daa92c45097482b96f9 | A -> Đ

### Group 143 — topic: Pediatrics, Gastroenterology
Q: Thăm khám lâm sàng quan trọng nhất ở trẻ bị táo bón kéo dài là nghe nhu động ruột
Options (shared set): ['Đ', 'S']
  line    640 | Medium      | id 3dc6b2e022c64f5eb3d69a2a836c4282 | B -> S
  line    649 | Medium      | id f9d4c06588bf418fa55a9c75f44d7d8e | B -> S

### Group 144 — topic: Pediatrics, Gastroenterology
Q: Bé Nga, 7 tháng tuổi thường bị táo bón, điều trị cần phải làm đầu tiên là tăng cường nước uống cho trẻ
Options (shared set): ['Đ', 'S']
  line    641 | Medium      | id 564a16cc9a11440e8938f6b233ffb015 | A -> Đ
  line    650 | Medium      | id e881fc395efa4dbe80acade529c15dce | A -> Đ

### Group 145 — topic: Otolaryngology, Gastroenterology
Q: Khi bị mất dấu hiệu chạm cột sống (lọc cọc thanh quản cột sống) tức là thực quản vùng cổ bình thường đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line    642 | Medium      | id 102898b2752f434b832b1aff048d2597 | B -> Sai
  line   1955 | Medium      | id ebff49f89da641e9b45b8071a7533d6c | B -> Sai

### Group 146 — topic: Otolaryngology, Gastroenterology
Q: Dị vật nhỏ sắc nhọn như xương cá hay gặp trong thực quản hơn vùng miệng đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line    643 | Medium      | id 415c155fbb46440ea5cddfe1be170c53 | B -> Sai
  line   1956 | Medium      | id 3b6bfbf86778494c84614c685232ffc4 | B -> Sai

### Group 147 — topic: Gastroenterology
Q: Yếu tố thuận lợi cho sự hình thành bệnh trĩ đã được khoa học chứng minh?
Options (shared set): ['Viêm đại tràng mạn tính và táo bón kinh niên', 'Uống nhiều café', 'Ăn nhiều tiêu, ớt', 'Người nằm lâu và nhiều']
  line    652 | Easy        | id 99612a079d324ed08536221b1ba5d50e | A -> Viêm đại tràng mạn tính và táo bón kinh niên
  line    818 | Easy        | id 05491775f7bf456ab99ea957a84b91ba | A -> Viêm đại tràng mạn tính và táo bón kinh niên

### Group 148 — topic: Gastroenterology
Q: Dịch báng trong xơ gan?
Options (shared set): ['Do áp lực keo huyết tương giảm', 'Do tăng áp lực TM cửa', 'Do tăng áp các TM tạng', 'Do tăng Aldosterol']
  line    659 | Medium      | id afd042d9f3194e09853990832b49f40a | B -> Do tăng áp lực TM cửa
  line    819 | Medium      | id 7d1db5aeff9a4792bb71600dc68433ab | B -> Do tăng áp lực TM cửa
  line  10546 | Medium      | id 46ef8faad1654fa3ad5766652753fcca | B -> Do tăng áp lực TM cửa

### Group 149 — topic: Gastroenterology
Q: Dịch báng kèm với dấu chứng đầu sứa nổi lên?
Options (shared set): ['Tắc TM trên gan', 'Nhồi máu TM cửa', 'Có shunt cửa chủ do tuần hoàn hệ cửa bị cản trở', 'Nhồi máu mạc treo']
  line    661 | Medium      | id 47c9a49c8e794989b80add49551b02b6 | C -> Có shunt cửa chủ do tuần hoàn hệ cửa bị cản trở
  line    821 | Medium      | id 740c146669de463493a2f5f66e7d99c9 | C -> Có shunt cửa chủ do tuần hoàn hệ cửa bị cản trở

### Group 150 — topic: Surgery, Gastroenterology
Q: Dấu hiệu co cứng thành bụng có tính chất:
Options (shared set): ['Tồn tại khách quan ngoài ý muốn của BN', 'Sờ ấn vào làm BN đau', 'Thường gặp trong ruột thừa viêm cấp chưa có biến chứng', 'Không có lựa chọn nào']
  line    679 | Medium      | id c9045aea4d554176a4c5ade49ad1853a | A -> Tồn tại khách quan ngoài ý muốn của BN
  line   9628 | Easy        | id 231624485d0e4aeda69addcc222023f3 | A -> Tồn tại khách quan ngoài ý muốn của BN

### Group 151 — topic: Gastroenterology, Endocrinology
Q: Người gầy, ăn mau đói do:
Options (shared set): ['Tỳ Vị thấp nhiệt', 'Vị hoả', 'Thận âm hư', 'Tâm hoả thịnh']
  line    682 | Medium      | id a95726ef39094596a8c94170b1792992 | B -> Vị hoả
  line   6417 | Medium      | id 25d752a63f934402b92ea78b4d2ef590 | B -> Vị hoả
  line   8489 | Medium      | id 609eba798a7e42c797005f278101baf1 | B -> Vị hoả

### Group 152 — topic: Gastroenterology
Q: Số lượng ổ loét trong viêm dạ dày cấp thường có?
Options (shared set): ['Loét đơn độc', 'Loét vài chỗ', 'Loét phối hợp', 'Thường nhiều']
  line    723 | Easy        | id 3401b1da146e493aa5363722f5fcf1ee | D -> Thường nhiều
  line  10573 | Easy        | id f5cedec7e1f941baabd0be9090fe8c1c | D -> Thường nhiều

### Group 153 — topic: Endocrinology, Gastroenterology
Q: TB thực hiện chức năng nội tiết?
Options (shared set): ['TB G', 'TB thành', 'TB D', 'TB chính']
  line    759 | Easy        | id 58fb5401cd394be9876864e3a546e3d8 | A -> TB G
  line   6418 | Medium      | id cfe53b1d93ec4eaf94271bbfbcee82f9 | C -> TB D

### Group 154 — topic: Surgery, Gastroenterology
Q: Dịch tiết gặp ở đâu, trừ trường hợp nào?
Options (shared set): ['Viêm phúc mạc', 'Thủng dạ dày', 'Nhồi máu mạc treo', 'D………….']
  line    785 | Medium      | id 190ad82a6ae44f559cf186561c1e5056 | C -> Nhồi máu mạc treo
  line   9700 | Medium      | id b06deccc055141f8b034219ee4b7d7de | C -> Nhồi máu mạc treo

### Group 155 — topic: Gastroenterology, Endocrinology
Q: Chất nào có cơ chế khác với các chất còn lại?
Options (shared set): ['Gastrin', 'Prostaglandin E2', 'Histamin', 'Glucocorticoid']
  line    795 | Medium      | id fa4cfb3a081740c4a1cdbefb0c3a5785 | B -> Prostaglandin E2
  line   6419 | Medium      | id d5eb6e23af6a4a3ca01572b325450203 | B -> Prostaglandin E2

### Group 156 — topic: Endocrinology, Gastroenterology
Q: TB nào ở dạ dày là TB nội tiết:
Options (shared set): ['TB chính', 'TB nhầy', 'TB G', 'TB D']
  line    844 | Easy        | id 7189980ee4d94e14a3b5f17b7a9737df | C -> TB G
  line   6420 | Medium      | id bf85f120761f49158b1409970090aafd | D -> TB D

### Group 157 — topic: Gastroenterology, Endocrinology
Q: Rối loạn tiêu hoá nguyên nhân ngoài ruột dẫn đến giảm hấp thu gồm, trừ
Options (shared set): ['Suy thận', 'Suy giáp', 'Suy gan', 'Suy tuỵ']
  line    857 | Medium      | id 39b635d7fb20449191857daf6526817c | A -> Suy thận
  line   6423 | Medium      | id 06ae20f1c45947ef8046b064e676efa7 | B -> Suy giáp

### Group 158 — topic: Endocrinology, Gastroenterology
Q: Hormone Glucocorticoid của vỏ thượng thận có tác dụng gì?
Options (shared set): ['Kích thích bài tiết pepsin', 'Ức chế bài tiết chất nhầy, tăng tiết HCl và pepsin', 'Kích thích bài tiết HCl', '........']
  line    860 | Easy        | id 1d49745af83548cfbe71f3fe96396f0e | B -> Ức chế bài tiết chất nhầy, tăng tiết HCl và pepsin
  line   6424 | Medium      | id 8cafdd6d39e54230ad32b92ba7256a90 | B -> Ức chế bài tiết chất nhầy, tăng tiết HCl và pepsin

### Group 159 — topic: Oncology, Gastroenterology, Pulmonology
Q: UT gan di căn theo đường nào nhiều nhất?
Options (shared set): ['Phổi', 'Lách', 'Thận', 'BQ']
  line    880 | Easy        | id 38d0d15a5e944216b2eb2e2409770a01 | A -> Phổi
  line   4667 | Easy        | id 1d02217a93914923bbbff7a32a60f55f | A -> Phổi

### Group 160 — topic: Gastroenterology, Pulmonology
Q: Cổ trướng gan khó thở như thế nào?
Options (shared set): ['Khi vận động', 'Khi nằm', 'Khi dịch tăng', 'Khi dịch đặc']
  line    886 | Medium      | id 8b472f3e3fef442585a682550a1a6e38 | B -> Khi nằm
  line   4668 | Medium      | id f77c485b334340ee96fe817ee5d75564 | B -> Khi nằm

### Group 161 — topic: Gastroenterology, Hematology
Q: Gan chứa bao nhiêu máu?
Options (shared set): ['100-200 g', '300-500 g', '600-700 g', '800-900 g']
  line    923 | Easy        | id d44ffd9e328f476ca18d7e406156300e | D -> 800-900 g
  line  11817 | Easy        | id b4e9050f941d46ffaba52b92880e37ba | B -> 300-500 g

### Group 162 — topic: Gastroenterology, Endocrinology
Q: TB D tiết ra chất gì?
Options (shared set): ['Histamin', 'Somatostatin', 'Chất nhày', 'HCl']
  line    943 | Easy        | id 22b24ace8672435680b9176732e946fb | B -> Somatostatin
  line   6425 | Medium      | id aebe2aba2a044e92a405e13d3799458b | B -> Somatostatin

### Group 163 — topic: Gastroenterology, Endocrinology
Q: TB chính tiết ra chất gì?
Options (shared set): ['HCl, yếu tố nội', 'Pepsinogen, lipase', 'Histamin, Somatostatin', 'Chất nhày']
  line    944 | Easy        | id 0bb8c4566b9944119a20e1f40522fc67 | B -> Pepsinogen, lipase
  line   6426 | Medium      | id 408dab334e7f4d24bae4ab552734ea3a | B -> Pepsinogen, lipase

### Group 164 — topic: Gastroenterology, Endocrinology
Q: Gan có chức năng chuyển hoá chất gì?
Options (shared set): ['Lipid', 'Protid', 'Glucid', 'Cả 3']
  line    951 | Easy        | id 3bb5cbdead714b06862be7ecf5c1c491 | D -> Cả 3
  line   6427 | Medium      | id 9405ed958e9e495ba79095c42df261b3 | D -> Cả 3

### Group 165 — topic: Gastroenterology, Endocrinology
Q: TB D ức chế chất gì?
Options (shared set): ['Histamin', 'Somatostatin', 'Chất nhày', 'HCl']
  line    953 | Medium      | id 64c0c6f2fd85455eacba5684a3c84221 | D -> HCl
  line   6428 | Medium      | id cb75810e381c47979c9a4b53ee746b13 | D -> HCl

### Group 166 — topic: Gastroenterology, Endocrinology
Q: Glucose được hấp thu bằng hình thức tích cực thứ phát, đồng vận chuyển với Na+. Đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line    961 | Medium      | id e71227a45b7f4d399f5a415ff53db3b8 | A -> Đúng
  line   6429 | Medium      | id a7ac2bcadae04b679350ea4bf5defe88 | A -> Đúng

### Group 167 — topic: Gastroenterology, Hematology
Q: Đặc điểm vàng da sau gan?
Options (shared set): ['Bilirubin gián tiếp tăng', 'Bilirubin trực tiếp tăng', 'Tăng cả Bilirubin trực tiếp và gián tiếp', 'Không tăng cả Bilirubin trực tiếp và gián tiếp']
  line    973 | Medium      | id 30f44334ba734d698ddbd6beaacd3aef | B -> Bilirubin trực tiếp tăng
  line  11857 | Easy        | id 6bf1c386a6e04549987b77ce0bce84d2 | B -> Bilirubin trực tiếp tăng

### Group 168 — topic: Gastroenterology, Endocrinology
Q: Lipase có tác dụng phân giải chất nào?
Options (shared set): ['Lipid', 'Protid', 'Glucid', 'Cả 3']
  line    984 | Easy        | id 12a8dfa56b954475821154dc2c2b002d | A -> Lipid
  line   6216 | Easy        | id ce6d09ee99f64b54bca8f310b6251563 | A -> Lipid

### Group 169 — topic: Gastroenterology, Hematology
Q: Yếu tố nội có vai trò hấp thu vitamin B12 ở hồi tràng?
Options (shared set): ['Đúng', 'Sai']
  line    989 | Easy        | id 3e33d47b10df449886fc8eaf31c626a8 | A -> Đúng
  line  11873 | Easy        | id f1d3a6d3216b4664b11b954db3656cb5 | A -> Đúng

### Group 170 — topic: Gastroenterology, Endocrinology
Q: Acid béo mạch dài hấp thu trực tiếp vào tĩnh mạch cửa?
Options (shared set): ['Đúng', 'Sai']
  line    991 | Medium      | id 8ad2964064ec4737a44d33889fe6dc51 | B -> Sai
  line   6430 | Medium      | id d1a009913bcb46aa8f162f5753dfd591 | B -> Sai

### Group 171 — topic: Gastroenterology, Endocrinology
Q: Secretin kích thích tụy bài tiết Bicarbonat?
Options (shared set): ['Đúng', 'Sai']
  line    992 | Medium      | id c018f5365a9144118c55d15292153d66 | A -> Đúng
  line   6431 | Medium      | id b61d15403bcd4c41881bc721ada16e51 | A -> Đúng

### Group 172 — topic: Endocrinology, Gastroenterology
Q: Mất tụy nội tiết gây rối loạn chuyển hóa?
Options (shared set): ['Đúng', 'Sai']
  line    997 | Medium      | id 4b2f6ac814b74fc3aab35a1982ed5ee1 | A -> Đúng
  line   6433 | Medium      | id e074cc9fe9a340f88c461d790999f428 | A -> Đúng

### Group 173 — topic: Gastroenterology, Endocrinology
Q: Tăng tiết Gastrin trong trường hợp:
Options (shared set): ['Có mặt polypeptid trong dạ dày', 'Có mặt glucid trong dạ dày', 'Có mặt lipid trong dạ dày', 'Cả 3']
  line   1011 | Medium      | id a7e3c7dee6b046528a807b133f7ede09 | A -> Có mặt polypeptid trong dạ dày
  line   6434 | Medium      | id 48f35839460f4c199b3054fad9ae238b | A -> Có mặt polypeptid trong dạ dày

### Group 174 — topic: Gastroenterology, Endocrinology
Q: Vận chuyển glucid, galactose là vận chuyển thứ phát, qua protein mang?
Options (shared set): ['Đ', 'S']
  line   1020 | Medium      | id 3ad635b1c57d41389cf88a2fabb44e63 | A -> Đ
  line   6435 | Medium      | id f13f40d891fa4ddfb8c39e32cfda71e3 | A -> Đ

### Group 175 — topic: Endocrinology, Gastroenterology
Q: Ý nghĩa tốt nhất cho từ được gạch chân là gì? Có sự gia tăng 'tạo đường mới' ở gan, hấp thụ glucose nhanh chóng qua đường tiêu hóa và có thể tăng kháng insulin.
Options (shared set): ['sản xuất đường từ glycogen', 'chức năng tuyến giáp quá cao', 'một lượng chất béo bất thường trong máu', 'liên quan đến lượng đường trong máu']
  line   1025 | Medium      | id 04f2f9c846cd42e4937ef632b5ee4bee | D -> liên quan đến lượng đường trong máu
  line   6087 | Medium      | id 408cb03727c94d24ad88e5dab103aa60 | A -> sản xuất đường từ glycogen

### Group 176 — topic: Gastroenterology, Hematology
Q: Vàng da mà sắc vàng ám tối (hoàng đản do ứ mật, tan huyết) là do?
Options (shared set): ['Hàn thấp', 'Thấp nhiệt', 'Tỳ hư', 'Phong hàn']
  line   1027 | Medium      | id 90122386b01c41db99778eab6deee101 | A -> Hàn thấp
  line   1109 | Medium      | id 5bd7bc1f6bb249b8ad84fc5bf8fb50fa | A -> Hàn thấp

### Group 177 — topic: Pulmonology, Gastroenterology
Q: Bệnh nào gây tràn dịch màng phổi trái?
Options (shared set): ['Viêm tụy cấp', 'Viêm thận bể thận T', 'Thủng tạng rỗng']
  line   1042 | Challenging | id 8f915e3eb8a047c0bdd522247f1aa3f1 | A -> Viêm tụy cấp
  line   4673 | Medium      | id 0b74f4bf0f9a48d9bc36adcf1be7d00b | A -> Viêm tụy cấp

### Group 178 — topic: Pulmonology, Gastroenterology
Q: Tràn dịch màng phổi nào là dịch thấm?
Options (shared set): ['Viêm tụy cấp', 'Viêm gan', 'K phổi']
  line   1043 | Challenging | id b0530e5937be478bb0c9f3763f736404 | B -> Viêm gan
  line   4674 | Medium      | id eaef4e692a9e41a380ae68dc49d4a008 | B -> Viêm gan

### Group 179 — topic: Pulmonology, Gastroenterology
Q: Eprazion gây long đờm nhưng không kích thích niêm mạc tiêu hoá?
Options (shared set): ['Đ', 'S']
  line   1048 | Medium      | id 9b82bd77208f46e089bbc0323889c60a | A -> Đ
  line   4677 | Medium      | id 20d3804c9822475a9db4618c0a572912 | A -> Đ

### Group 180 — topic: Pulmonology, Gastroenterology
Q: Thuốc long đờm nhưng không kích ứng niêm mạc tiêu hoá*
Options (shared set): ['Carbocystein', 'Ambroxol', 'Eprazinon', 'Bromhexin']
  line   1067 | Medium      | id 224411a9d4be4b9e80339429db7fda35 | C -> Eprazinon
  line   4752 | Medium      | id 35c7c467f9f54cb0af6ebdc2f9b994ca | C -> Eprazinon

### Group 181 — topic: Infectious Diseases, Pulmonology, Gastroenterology
Q: Rifampicin độc với gan khi dùng cùng thuốc nào?
Options (shared set): ['Streptomycin', 'Isoniazid', 'Ethambutol', 'Pyrazinamid']
  line   1072 | Medium      | id ddc3504dee65402aa5320c364c5b08ae | B -> Isoniazid
  line   4756 | Medium      | id 6189e5dbed644073bd379fce9a587382 | B -> Isoniazid

### Group 182 — topic: Endocrinology, Nephrology, Gastroenterology
Q: Chỉ định Corticoid điều hoà glucose trong?
Options (shared set): ['Suy gan', 'Suy thận cấp', 'Suy thận cấp và mạn', '...']
  line   1074 | Challenging | id 45448789ff9445e08bc2f9fcbc589ae7 | C -> Suy thận cấp và mạn
  line   6088 | Medium      | id 665e68b974d24aedb421e64bbac490d1 | C -> Suy thận cấp và mạn

### Group 183 — topic: Pulmonology, Gastroenterology
Q: Eprazion gây long đờm nhưng không kích thích niêm mạc tiêu hoá?
Options (shared set): ['Đúng', 'Sai']
  line   1076 | Medium      | id c80acdb5a20c4ab097eef5eaafd3e030 | A -> Đúng
  line   4759 | Easy        | id e607c29f106d4951a3c312fa5b06663d | A -> Đúng

### Group 184 — topic: Gastroenterology, Pulmonology
Q: Ho tồi tệ hơn ở vị trí nằm nghiêng cho thấy
Options (shared set): ['Thuyên tắc phổi.', 'Hen suyễn.', 'Trào ngược dạ dày.', 'Áp xe dưới cơ hoành.']
  line   1089 | Medium      | id 34db9f3bad9446c9844c3db13cc09953 | C -> Trào ngược dạ dày.
  line   4777 | Medium      | id c5a23baca6044f45a429a6d67cbd56a1 | C -> Trào ngược dạ dày.

### Group 185 — topic: Radiology, Pulmonology, Gastroenterology
Q: Trên phim phổi thẳng chụp đứng thấy túi hơi dạ dày dưới cơ hoành trái
Options (shared set): ['Đúng', 'Sai']
  line   1100 | Easy        | id f5a4eb6485ab42cd9453113a44f6a9c4 | A -> Đúng
  line   4796 | Easy        | id 4e35524542a645a9abbc661a8457c9d5 | A -> Đúng

### Group 186 — topic: Gastroenterology, Surgery
Q: Tắc ruột được định nghĩa là tình trạng tắc lòng ruột do vật cản:
Options (shared set): ['Đúng', 'Sai']
  line   1126 | Easy        | id aacce1b49c9148049f12709d6cc888a6 | B -> Sai
  line   1298 | Easy        | id 86b57a41b89b461f84ae8c27d053d882 | B -> Sai

### Group 187 — topic: Gastroenterology, Neurology, Surgery
Q: trong những nguyên nhân gây tắc ruột là tình trạng ruột không co bóp do hoặc là do nguyên nhân của cơ thành ruột hoặc là do nguyên nhân thần kinh ruột.
Options (shared set): ['Đúng', 'Sai']
  line   1127 | Medium      | id 708dcc59289a49819c8aa18132a5cf40 | A -> Đúng
  line   1299 | Medium      | id f889250f2adc406091b49cec1fbd181f | A -> Đúng
  line   1693 | Medium      | id 4b1a89a30dae46f89deca1a308b7eb3a | A -> Đúng

### Group 188 — topic: Gastroenterology, Surgery, Pediatrics, Oncology
Q: Các nguyên nhân gây tắc ruột cơ học bao gồm tắc ruột do bệnh phình đại tràng bẩm sinh, tắc ruột do viêm phúc mạc, tắc ruột do ung thư ruột.
Options (shared set): ['Đúng', 'Sai']
  line   1128 | Medium      | id aa2fafdd10f6492084780a7f4d2d1871 | B -> Sai
  line   1300 | Medium      | id 6d571796bbdb436e997b3d3f3a56f649 | B -> Sai

### Group 189 — topic: Gastroenterology, Surgery, Pediatrics, Oncology
Q: Các nguyên nhân gây tắc ruột cơ năng bao gồm tắc ruột do bệnh phình đại tràng bẩm sinh, tắc ruột do viêm phúc mạc, tắc ruột do ung thư ruột.
Options (shared set): ['Đúng', 'Sai']
  line   1129 | Medium      | id e25549183c404014999795d41cdf6474 | B -> Sai
  line   1301 | Medium      | id c137a46223234e89ac2b34c034cf1f5e | B -> Sai

### Group 190 — topic: Infectious Diseases, Gastroenterology
Q: Thức ăn là yếu tố truyền nhiễm độc nhất trong nhóm bệnh:
Options (shared set): ['Viêm gan virus A, bại liệt', 'Nhiễm trùng nhiễm độc thức ăn do các vi trùng gây bệnh là Salmonella, Staphylococci và Clostridium botulinum', 'Lỵ, tả', 'Thương hàn']
  line   1130 | Medium      | id 869b165c242a4f09af71f28f864d4454 | B -> Nhiễm trùng nhiễm độc thức ăn do các vi trùng gây bệnh là Salmonella, Staphylococci và Clostridium botulinum
  line   4341 | Medium      | id ca065ccec9d744f1948e5e4d0487d59b | B -> Nhiễm trùng nhiễm độc thức ăn do các vi trùng gây bệnh là Salmonella, Staphylococci và Clostridium botulinum

### Group 191 — topic: Infectious Diseases, Gastroenterology
Q: Tính chất phân điển hình của người bị bệnh tả là phân lỏng nhầy máu.
Options (shared set): ['Đúng', 'Sai']
  line   1135 | Easy        | id 3567185f20c446cf8cda2b0b5fcc3398 | B -> Sai
  line   2218 | Easy        | id f98a58aeee6a4596ac07aa930d8a23e2 | B -> Sai
  line   2290 | Easy        | id fde4dcfe50c34c4ba8419b19dc1529fe | B -> Sai

### Group 192 — topic: Gastroenterology, Infectious Diseases
Q: Bệnh Viêm gan A có tình trạng người mang trùng mạn tính sau khi khỏi bệnh
Options (shared set): ['Đúng', 'Sai']
  line   1136 | Easy        | id f87e64d5385c435896e0eb24112f478b | B -> Sai
  line  10275 | Easy        | id c862566b8fb64185933adb5be3c78c53 | A -> Sai

### Group 193 — topic: Infectious Diseases, Gastroenterology
Q: Vi khuẩn thương hàn có nhiều đường ra khỏi cơ thể ký chủ
Options (shared set): ['Đúng', 'Sai']
  line   1144 | Easy        | id 8c17fa78df7c40808b5cb030813199db | B -> Sai
  line   2285 | Easy        | id df6bea38a4f2492298d3f2ac4360a57b | B -> Sai

### Group 194 — topic: Endocrinology, Gastroenterology
Q: Trong bệnh về gan, thiếu hụt glucocorticoid, nhiễm trùng huyết, giảm dự trữ glycogen. Số các bệnh làm giảm đường huyết là:
Options (shared set): ['4', '3', '2', '1']
  line   1171 | Challenging | id 9c4fbde0b5ec42ebb0a9a3b4e9beacb6 | A -> 4
  line   6101 | Medium      | id 86b434a639e74039ab58c9cae0a49803 | A -> 4

### Group 195 — topic: Gastroenterology, Hematology
Q: Lượng bilirubine gián tiếp trong máu bình thường là:
Options (shared set): ['0.4 – 0.6 mg/dL', '0.6 – 0.8 mg/dL', '0.8 – 1.2 mg/dL', '1.2 – 1.4 mg/dL']
  line   1175 | Easy        | id 16466aecd98d408595ec7a7c9521c7b9 | B -> 0.6 – 0.8 mg/dL
  line  10601 | Easy        | id 0340cbea537d4dd5bb465ff6e94e8a11 | B -> 0.6 – 0.8 mg/dL

### Group 196 — topic: Gastroenterology, Endocrinology
Q: Hormon chủ yếu gây bài suất mật?
Options (shared set): ['Cholecystokinin', 'Secretin', 'Gastrin', 'Histamin']
  line   1239 | Easy        | id b1dd053e65814c2aaf789703399e467d | A -> Cholecystokinin
  line   6576 | Medium      | id 864d9a03b7ef4af58acda709b7006f10 | A -> Cholecystokinin

### Group 197 — topic: Gastroenterology
Q: Dịch nhầy ở dạ dày gồm những gì?
Options (shared set): ['Lipid, protein, hồng cầu', 'Glucoprotein, phospholipid, acid nucleic', 'Glucoprotein, cholesterol, acid amin', 'Phospholipid, acid nucleic, protein']
  line   1241 | Medium      | id 75e975ca37d446fc9faedaf172fbd63e | B -> Glucoprotein, phospholipid, acid nucleic
  line  10604 | Easy        | id 7b026fcc6b8f4807ba819cb1ddf21aee | B -> Glucoprotein, phospholipid, acid nucleic

### Group 198 — topic: Hematology, Gastroenterology, Endocrinology
Q: Suy giảm chức năng cơ quan nào sau đây không liên quan đến quá trình sản sinh hồng cầu?
Options (shared set): ['Thận', 'Gan', 'Tụy', 'Dạ dày (sản sinh yếu tố nội)']
  line   1248 | Medium      | id 0d4949ffcb4f480eb2718bf86409097f | C -> Tụy
  line   6592 | Medium      | id 977a6f0b712843b599742b7c00a31643 | C -> Tụy

### Group 199 — topic: Hematology, Gastroenterology
Q: Số lượng hồng cầu trong máu ngoại vi: Giảm do bị ỉa chảy mất nước?
Options (shared set): ['Đúng', 'Sai']
  line   1249 | Medium      | id 876c2625c9ea45019a1e8139d814929f | B -> Sai
  line  10561 | Medium      | id 523213ceeb9c44bea5066ab3c99efaa2 | B -> Sai

### Group 200 — topic: Gastroenterology, Endocrinology
Q: Sự thuỷ phân Triglycerid là không hoàn toàn ở Hành tá tràng nên tạo hỗn hợp gồm
Options (shared set): ['Triglycerid, Diglycerid, Monoglycerid, Acid béo, glycerol', 'Triglycerid, Diglycerid, Monoglycerid, Acid béo', 'Triglycerid, Diglycerid, Monoglycerid, Acid béo, amin', 'Triglycerid, Diglycerid, Monoglycerid, glycerol']
  line   1251 | Medium      | id 4d9c6389248c46b1a453da598caf58c5 | A -> Triglycerid, Diglycerid, Monoglycerid, Acid béo, glycerol
  line   6602 | Medium      | id a05f6d1316d24840b184ad648789ee2a | A -> Triglycerid, Diglycerid, Monoglycerid, Acid béo, glycerol

### Group 201 — topic: Endocrinology, Gastroenterology
Q: Glucagon:
1/Mô đích tác dụng là gan mỡ
2/Hoạt hoá glycogen phosphrylase làm tăng thoái hoá
3/Giảm tổng hợp glycogen ở gan
số kết luận đúng
Options (shared set): ['3', '2', '1', 'kết quả khác']
  line   1252 | Challenging | id e5c5d0cfe58948d0adc321778eeb77df | A -> 3
  line   6628 | Medium      | id 1331491505184f69950ce228218f351c | A -> 3

### Group 202 — topic: Endocrinology, Gastroenterology
Q: Thoái hoá Glucid ( Đi từ Glucose ) theo con đường Hexose DiP Trong điều kiện hiếu khí cho:
Options (shared set): ['38 ATP', '12 ATP', '2 ATP', '42 ATP']
  line   1253 | Medium      | id 9cb5ce4b5e3b4cceac6e1302d60b06b5 | A -> 38 ATP
  line   6632 | Medium      | id 4122a05971a846b7b52652930ad9da8f | A -> 38 ATP

### Group 203 — topic: Endocrinology, Gastroenterology
Q: Thoái hoá Glucid ( đi từ Glycogen ) theo con đường Hexose DiP trong điều kiện yếm khí cho:
Options (shared set): ['2 ATP', '38 ATP', '24 ATP', '4 ATP']
  line   1254 | Medium      | id 6f1d9aa4e1e74a45876a4f1dccc6f9b9 | A -> 2 ATP
  line   6633 | Medium      | id 256f5ed0536441c29f8d1e49f18951b0 | A -> 2 ATP

### Group 204 — topic: Endocrinology, Gastroenterology
Q: Chọn câu đúng:
Options (shared set): ['Thoái hoá Glucose theo con đường hexose phosphat cung cấp các đường 5C cho cơ thể', 'Thoái hoá Glucose theo con đường đường phân cholactat', 'Thoái hoá Glucose theo con đường đường phân ChoacetylCoA', 'Thoái hoá Glucose theo con đường đường phân Glycerol']
  line   1256 | Medium      | id 6c9f50814ae74f369fd7252ce431c202 | A -> Thoái hoá Glucose theo con đường hexose phosphat cung cấp các đường 5C cho cơ thể
  line   6634 | Medium      | id f718c08edbaf4891abe635a107c79452 | A -> Thoái hoá Glucose theo con đường hexose phosphat cung cấp các đường 5C cho cơ thể

### Group 205 — topic: Endocrinology, Gastroenterology
Q: Glucagon:
1/Mô đích tác dụng là gan và mỡ
2/Hoạt hoá glycogen phosphrylase làm tăng thoái hoá
3/Giảm tổng hợp Glycogen ở gan
Số kết luận đúng
Options (shared set): ['3', '2', '1', 'khác']
  line   1258 | Challenging | id 4bfa9bde572244628e78278a2a006475 | A -> 3
  line   6639 | Medium      | id bf91cc733a194e3ba018aab212ad0da4 | A -> 3

### Group 206 — topic: Endocrinology, Gastroenterology
Q: Somatostatin làm chậm quá trình tiêu hoá và hấp thụ thức ăn, được tạo thành từ:
Options (shared set): ['Tuyến tuỵ và niêm mạc đường tiêu hoá', 'Tuyến tuỵ', 'Niêm mạc đường tiêu hoá', 'Gan']
  line   1259 | Easy        | id a1fa64aaa5014ba799f9f09d1b58cf72 | A -> Tuyến tuỵ và niêm mạc đường tiêu hoá
  line   6640 | Medium      | id fca3761a10f5492c83635670c43431f8 | A -> Tuyến tuỵ và niêm mạc đường tiêu hoá

### Group 207 — topic: Endocrinology, Gastroenterology
Q: Tác dụng của hormon tuyến tuỵ
Options (shared set): ['Tiết ra insulin gây hạ đường huyết, glucagon làm tăng đường máu', 'Tiết ra insulin gây hạ đường huyết, kích thích chuyển hoá năng lượng, tăng chuyển hoá cơ bản', 'Tăng phân huỷ Triglycerid, Phospholipid, Cholesterol, Tiết ra insulin gây hạ đường huyết , glucagon làm tăng đường máu', 'tăng hấp thu glucose ở ruột, tăng phân giải glycogen nên làm tăng đường huyết']
  line   1260 | Easy        | id 414b42b4c5654f478cf74bfa27d445de | A -> Tiết ra insulin gây hạ đường huyết, glucagon làm tăng đường máu
  line   6642 | Medium      | id e163345d58c048e3bfc2182624699dd0 | A -> Tiết ra insulin gây hạ đường huyết, glucagon làm tăng đường máu

### Group 208 — topic: Gastroenterology, Nephrology
Q: Glucose qua bờ bàn chải của tế bào biểu mô niêm mạc ruột và ống thận theo hình thức:
Options (shared set): ['Vận chuyển tích cực thứ phát.', 'Khuếch tán đơn thuần.', 'Khuếch tán được tăng cường.', 'Đồng vận chuyển cùng chất mang với ion Na.']
  line   1261 | Medium      | id da9c5c5775ea478c974f7a7f123b466a | D -> Đồng vận chuyển cùng chất mang với ion Na.
  line  10605 | Easy        | id b824ed2849c843f2aad16b33a7cd7fbb | D -> Đồng vận chuyển cùng chất mang với ion Na.

### Group 209 — topic: Endocrinology, Gastroenterology
Q: T3-T4 làm tăng đường huyết do các tác dụng sau đây, trừ:
Options (shared set): ['Tăng phân giải glycogen thành glucose.', 'Tăng hấp thu glucose ở ruột.', 'Tăng tạo đường mới.', 'Giảm thoái hoá glucose ở tế bào.']
  line   1263 | Medium      | id 3749b3fb93a44e6e86b3d0cfe8300a89 | D -> Giảm thoái hoá glucose ở tế bào.
  line   6679 | Medium      | id 010def983ad24ce4862bb31ff1d9d0b1 | D -> Giảm thoái hoá glucose ở tế bào.

### Group 210 — topic: Pulmonology, Gastroenterology
Q: Có một nguy cơ hơi tăng phát triển nhiễm trùng ngực hoặc viêm phổi sau khi nội soi dạ dày.
Options (shared set): ['Đúng', 'Sai']
  line   1274 | Medium      | id 7e50efb7bdce4c40b4ec5d8dc7bfb36c | A -> Đúng
  line   5003 | Medium      | id ad2465b377ac42d980085356b58639bf | A -> Đúng

### Group 211 — topic: Gastroenterology
Q: Vàng da do chít hẹp cơ Oddi là loại vàng da do nguyên nhân sau gan?
Options (shared set): ['Đúng', 'Sai']
  line   1292 | Medium      | id 615f4115430044beb44b508ee6b9db8a | A -> Đúng
  line   1692 | Medium      | id 064e4e7d4bba4caba64ad6197bb70f13 | A -> Đúng

### Group 212 — topic: Gastroenterology, Infectious Diseases
Q: Về xét nghiệm chẩn đoán tác nhân gây tiêu chảy, câu nào sau đây đúng
Options (shared set): ['Chẩn đoán xác định Tả bằng xét nghiệm soi phân tươi thấy vi khuẩn gram âm di động', 'Chẩn đoán xác định lị amip cấp bằng xét nghiệm soi phân tươi thấy bào nang amip', 'Chẩn đoán xác định lị trực trùng bằng xét nghiệm cấy phân, phân lập Shighella', 'Chẩn đoán xác định tiêu chảy do virus bằng xét nghiệm độc tố của virus trong phân']
  line   1304 | Challenging | id 24777bef037b4e168daed76518c3e80b | C -> Chẩn đoán xác định lị trực trùng bằng xét nghiệm cấy phân, phân lập Shighella
  line   1357 | Challenging | id 6149233d544b4dc392af1e6febcf3b87 | C -> Chẩn đoán xác định lị trực trùng bằng xét nghiệm cấy phân, phân lập Shighella
  line   1373 | Challenging | id 9f65cbb590e64cc8ba617806c8718c32 | C -> Chẩn đoán xác định lị trực trùng bằng xét nghiệm cấy phân, phân lập Shighella

### Group 213 — topic: Infectious Diseases, Gastroenterology
Q: Chọn câu đúng khi nói về bệnh thương hàn
Options (shared set): ['Ở thể điển hình, bệnh có thể tự khỏi sau 4 tuần không cần điều trị kháng sinh', 'Vẻ mặt typhus trong bệnh thương hàn là do liệt cơ mặt', 'Bệnh gây vết loét ở đoạn hồi tràng, có thể gây chảy máu, nhưng không bao giờ gây thủng ruột', 'Bệnh thương hàn là bệnh nhiễm trùng tại chỗ ở đường tiêu hóa']
  line   1307 | Medium      | id a0a913ad9f014193a8581d0e41b4405b | A -> Ở thể điển hình, bệnh có thể tự khỏi sau 4 tuần không cần điều trị kháng sinh
  line   1363 | Medium      | id 5d71133aee434efeb3cb3bd68079d20f | A -> Ở thể điển hình, bệnh có thể tự khỏi sau 4 tuần không cần điều trị kháng sinh
  line   1374 | Medium      | id a7afd0cd2ae2413393c6e3a4f5b7b769 | A -> Ở thể điển hình, bệnh có thể tự khỏi sau 4 tuần không cần điều trị kháng sinh

### Group 214 — topic: Infectious Diseases, Gastroenterology
Q: Diễn tiến tự nhiên của bệnh thuơng hàn
Options (shared set): ['Bệnh có thể tự khỏi sau 4 tuần dù không điều trị kháng sinh, nhưng bệnh nhân suy kiệt và có thể xảy ra biến chứng', 'Bệnh diễn tiến sang biến chứng xuất huyết tiêu hóa, thủng ruột ở giai đoạn toàn phát nếu không điều trị kháng sinh', 'Bệnh lành tính và tự khỏi sau 1 tuần, không có biến chứng', 'Bệnh có thể tự khỏi sau 1 tuần dù không điều trị kháng sinh, nhưng bệnh nhân mang vi trùng kéo dài lây lan cho cộng đồng']
  line   1308 | Medium      | id 77510a79cbbe420995f7e0e9bba8d4b7 | A -> Bệnh có thể tự khỏi sau 4 tuần dù không điều trị kháng sinh, nhưng bệnh nhân suy kiệt và có thể xảy ra biến chứng
  line   1375 | Medium      | id 41575ecf10d94995986cd36919917fa6 | A -> Bệnh có thể tự khỏi sau 4 tuần dù không điều trị kháng sinh, nhưng bệnh nhân suy kiệt và có thể xảy ra biến chứng

### Group 215 — topic: Gastroenterology, Infectious Diseases
Q: Biện pháp quan trọng nhất điều trị viêm gan siêu vi cấp
Options (shared set): ['Điều trị kháng virus tùy theo nguyên nhân', 'Điều trị hỗ trợ, giảm gánh nặng cho gan', 'Kháng sinh ngừa bội nhiễm', 'Các thuốc có nguồn gốc thảo dược có tác dụng tốt']
  line   1309 | Medium      | id 5580be091d764449aeff4a37824ef932 | B -> Điều trị hỗ trợ, giảm gánh nặng cho gan
  line   1376 | Medium      | id 98c508ab48e94446a3ed8fff5b17aaaa | B -> Điều trị hỗ trợ, giảm gánh nặng cho gan

### Group 216 — topic: Gastroenterology, Infectious Diseases, Obstetrics and Gynecology
Q: Viêm gan siêu vi E cấp là bệnh lành tính, hầu hết tự khỏi. Cơ địa nào sau đây khi bị viêm gan siêu vi E cấp dễ có biến chứng suy gan cấp
Options (shared set): ['Phụ nữ có thai', 'Người già', 'Trẻ em', 'Người lao động cường độ cao']
  line   1310 | Medium      | id fc4e5f9c6659496d99122fea01fb9de7 | A -> Phụ nữ có thai
  line   1359 | Medium      | id 5d6fdd2667fc40389bd76729e55fa54c | A -> Phụ nữ có thai
  line   1366 | Medium      | id b622b49c57054bd9b456cf90fca3aa1f | A -> Phụ nữ có thai
  line   1377 | Medium      | id c2a81f40a6194669a1f4bc8575426123 | A -> Phụ nữ có thai
  line  11000 | Medium      | id 1f28505cc5d9474bbc3aec39ba70348d | A -> Phụ nữ có thai

### Group 217 — topic: Infectious Diseases, Gastroenterology
Q: Tiêu chuẩn chẩn đoán viêm gan siêu vi B cấp
Options (shared set): ['HBV DNA dương tính ít nhất 6 tháng', 'Men gan tăng gấp 2-5 ULN', 'HBsAg và HBeAg dương tính', 'HBsAg dương tính và biến mất trong vòng 6 tháng']
  line   1311 | Medium      | id 43d11cc28b144ada888e88a5a4926268 | D -> HBsAg dương tính và biến mất trong vòng 6 tháng
  line   1379 | Medium      | id 97caf34bfc9149f0b70701e7b5ef2068 | D -> HBsAg dương tính và biến mất trong vòng 6 tháng

### Group 218 — topic: Infectious Diseases, Gastroenterology
Q: Mô tả giai đoạn hồi phục của viêm gan siêu vi cấp
Options (shared set): ['Ăn uống tốt, vàng da, vàng mắt giảm dần, tuy nhiên có thể tiểu sậm kéo dài', 'Tiểu trong, ăn uống tốt, vàng da vàng mắt giảm dần, có thể có vàng da, vàng mắt kéo dài nhưng không quá 6 tháng', 'Tiểu trong, ăn uống tốt, tuy nhiên triệu chứng vàng mắt vàng da còn kéo dài ít nhất 6 tháng', 'tiểu trong, ăn uống tốt, vàng da, vàng mắt giảm dần tuy nhiên có thể xảy ra biến chứng viêm gan tối cấp vào giai đoạn này']
  line   1312 | Medium      | id 606846a16a344d31862a3d1cdd1bfdb9 | B -> Tiểu trong, ăn uống tốt, vàng da vàng mắt giảm dần, có thể có vàng da, vàng mắt kéo dài nhưng không quá 6 tháng
  line   1361 | Medium      | id d55f5160e93a4337ac55e70c1c0b3dec | B -> Tiểu trong, ăn uống tốt, vàng da vàng mắt giảm dần, có thể có vàng da, vàng mắt kéo dài nhưng không quá 6 tháng
  line   1369 | Medium      | id 6a657eead6164e798c59681ae1ad397d | B -> Tiểu trong, ăn uống tốt, vàng da vàng mắt giảm dần, có thể có vàng da, vàng mắt kéo dài nhưng không quá 6 tháng
  line   1380 | Medium      | id 1aecf525effa438da88993ae26e93a00 | B -> Tiểu trong, ăn uống tốt, vàng da vàng mắt giảm dần, có thể có vàng da, vàng mắt kéo dài nhưng không quá 6 tháng

### Group 219 — topic: Infectious Diseases, Gastroenterology, Radiology
Q: Hình ảnh siêu âm bụng có thể gặp trong giai đoạn mạn của bệnh nhiễm sán lá gan lớn?
Options (shared set): ['Hình ảnh đường hầm có tính di chuyển trong gan', 'Hình ảnh khối sán làm nghẽn đường mật hoặc hình ảnh vôi hóa, tạo sỏi do sán', 'Hình ảnh dày vách túi mật', 'Hình ảnh tràn dịch màng phổi, màng bụng']
  line   1313 | Medium      | id 44b039b181f74ce0b2c09e1871640df3 | B -> Hình ảnh khối sán làm nghẽn đường mật hoặc hình ảnh vôi hóa, tạo sỏi do sán
  line   1382 | Medium      | id d2553a49fecc4e179506123f11f35fc2 | B -> Hình ảnh khối sán làm nghẽn đường mật hoặc hình ảnh vôi hóa, tạo sỏi do sán
  line   4328 | Challenging | id 0d40bd085d254d478560e2d1242af581 | B -> Hình ảnh khối sán làm nghẽn đường mật hoặc hình ảnh vôi hóa, tạo sỏi do sán

### Group 220 — topic: Pathology, Gastroenterology
Q: Bệnh nhân nữ 53 tuổi vào viện khám vì đau thượng vị, có ợ hơi, ăn khó tiêu, sau khi khám được chỉ định nội soi và sinh thiết dạ dày làm mô bệnh học, kết quả cho thấy tuyến dạ dày được thay bởi tuyến của ruột kèm các ổ cấu trúc tuyến ít nhiều thay đổi, nhân tế bào hơi to nhỏ không đều, chất nhiếm sắc hơi thôi, kiềm tính vừa, còn cực tính. Tổn thương này phù hợp nhất với loại nào?
Options (shared set): ['dị sản tuyến dạ dày', 'loạn sản, dị sản tuyến dạ dày', 'quá sản, dị sản tuyến dạ dày', 'loạn sản, quá sản tuyến dạ dày']
  line   1314 | Challenging | id 8753a3a6d35a43aaa36219ac65537a25 | B -> loạn sản, dị sản tuyến dạ dày
  line   2008 | Challenging | id 484f0b949baf44fe862ff21fd4a5a472 | C -> Loạn sản, dị sản tuyến dạ dày
  line  10596 | Challenging | id 7cd28731146347d6830ed3ad5e846310 | B -> loạn sản, dị sản tuyến dạ dày

### Group 221 — topic: Pathology, Gastroenterology
Q: Một bệnh nhân vào nội soi thực quản dạ dày, sau khi được sinh thiết thực quản ở 1/3 dưới làm mô bệnh học, kết quả cho thấy biểu mô thực quản được phủ bởi biểu mô hình trụ, các tuyến tế bào hình trụ, nhân nhỏ tròn đều, chất nhiễm sắc mịn, tạo hình ống tuyến. Kết luận nào sau đây là đúng nhất?
Options (shared set): ['dị sản biểu mô thực quản', 'phì đại biểu mô thực quản', 'loạn sản biểu mô thực quản', 'teo biểu mô thực quản']
  line   1315 | Challenging | id 8e560bf180564a129dac549cd8da3dbc | A -> dị sản biểu mô thực quản
  line   2007 | Challenging | id 5b09855d43114b9da6f037000ab36694 | C -> Loạn sản biểu mô thực quản

### Group 222 — topic: Gastroenterology, Infectious Diseases
Q: Áp xe gan do amip thường ở vị trí nào:
Options (shared set): ['gan phải', 'gan trái', 'đường mật trong gan', 'có thể gặp ở cả 3 vị trí với tỉ lệ như nhau']
  line   1319 | Medium      | id 19a64436c2cf43e0a1931d998c6066c2 | A -> gan phải
  line   1744 | Medium      | id c02ecdb189b047579f203b1af57e902c | A -> gan phải

### Group 223 — topic: Gastroenterology, Pathology
Q: Các tuyến trong viêm dạ dày mạn tính không có đặc điểm nào sau đây:
Options (shared set): ['các tuyến không có sự thay đổi gì.', 'các tuyến giảm thể tích', 'các tuyến mất hẳn.', 'tăng sinh phản ứng các tuyến.']
  line   1320 | Medium      | id fe2c9ca9cd884c35b2eb68c3e81f15d5 | A -> các tuyến không có sự thay đổi gì.
  line   1745 | Medium      | id 68b5ffdcd45b45929674f09880c3c717 | A -> các tuyến không có sự thay đổi gì.

### Group 224 — topic: Oncology, Gastroenterology
Q: Phân loại ung thư dạ dày giai đoạn sớm không có thể?
Options (shared set): ['thể lồi', 'thể phẳng', 'thể xơ đét', 'cả 3 thể đều đúng.']
  line   1321 | Medium      | id 0c992dfee31d464d8ce56cee2cdc62d8 | C -> thể xơ đét
  line   1746 | Medium      | id 90469fa75f22426f9fb608d3e7db1b30 | C -> thể xơ đét

### Group 225 — topic: Oncology, Gastroenterology
Q: Đâu là tổn thương tiền ung thư?
Options (shared set): ['xơ gan', 'khô da nhiễm sắc tố', 'polyp tuyến đại trực tràng.', 'viêm loét đại tràng.']
  line   1322 | Medium      | id e36ce45c83524e508640e0ab23e00151 | C -> polyp tuyến đại trực tràng.
  line   1747 | Medium      | id ba09fabea39748cbaa99d42bab680df1 | C -> polyp tuyến đại trực tràng.

### Group 226 — topic: Gastroenterology, Pathology
Q: Xơ gan do rượu có dạng thoái hoá nào sau đây?
Options (shared set): ['thoái hoá nước', 'thoái hoá mỡ', 'thoái hoá dạng tơ huyết', 'thoái hoá kính.']
  line   1323 | Medium      | id a8b10f9676a0434d9f6cd384aa902af7 | B -> thoái hoá mỡ
  line   1748 | Medium      | id 247a0a8e05414d5689740620c6fcbfba | B -> thoái hoá mỡ

### Group 227 — topic: Gastroenterology, Pathology
Q: Xơ gan bình thường?
Options (shared set): ['To hơn bình thường hoặc teo nhỏ', 'Kích thước gan to hơn bình thường', 'Gan teo nhỏ', 'Kích thước gan ít thay đổi']
  line   1333 | Medium      | id d606930797964d11964a63fcf1db6dae | A -> To hơn bình thường hoặc teo nhỏ
  line   1756 | Medium      | id c173fff7279443ccaf1be3322bb4cc87 | A -> To hơn bình thường hoặc teo nhỏ

### Group 228 — topic: Gastroenterology, Oncology, Pathology
Q: Trong các u đại tràng u nào thường gặp nhất?
Options (shared set): ['Ung thư biểu mô', 'U lympho ác tính', 'Polyp biểu mô', 'U mô đệm dạ dày ruột']
  line   1334 | Medium      | id 7e991295b4c3405c948f0a52244de098 | C -> Polyp biểu mô
  line   1757 | Medium      | id f40179ba15ec40278b3c443eeb40f315 | C -> Polyp biểu mô

### Group 229 — topic: Gastroenterology, Pathology
Q: Xơ gan nốt nhỏ khi kích thước nốt gan tân tạo nhỏ hơn?
Options (shared set): ['2mm', '2cm', '3mm', '3cm']
  line   1335 | Medium      | id 3fd021749ce248e9ac60bdf338813291 | C -> 3mm
  line   1758 | Medium      | id a0fae88750aa43eda82b8259bbd3be53 | C -> 3mm

### Group 230 — topic: Gastroenterology, Oncology, Pathology
Q: Theo hiệp hội chống ung thư quốc tế(UICC) về giai đoạn U trong ung thư biểu mô đại tràng, T2 tương ứng với tổn thương nào sau đây?
Options (shared set): ['U xâm nhập vào lớp cơ', 'U xâm nhập lớp dưới niêm mạc', 'U xâm nhập hết lớp cơ và lớp d thanh mạc', 'U xâm nhập đến thanh mạc']
  line   1337 | Medium      | id 4398bd69ac0e41aa945e40b7f22a2edf | A -> U xâm nhập vào lớp cơ
  line   1759 | Medium      | id d78988c53a844ee5abcd9327a8ac8ea5 | A -> U xâm nhập vào lớp cơ

### Group 231 — topic: Gastroenterology, Oncology, Pathology
Q: Theo UICC về tình trạng di căn hạch của ung thư biểu mô đại tràng, giai đoạn N2 tổn thương nào sau đây:
Options (shared set): ['U chưa di căn hạch', 'U di căn hạch xa', 'U di căn lớn hơn hoặc bằng 4 hạch quanh đại tràng và quang trực tràng', 'U di căn 1-3 hạch quanh đại tràng hoặc trực tràng']
  line   1338 | Medium      | id d5b0f12f928a4ea0af197da33f2f8b8d | C -> U di căn lớn hơn hoặc bằng 4 hạch quanh đại tràng và quang trực tràng
  line   1760 | Medium      | id 7ce54e61b04947d7927fea79037cbfb9 | C -> U di căn lớn hơn hoặc bằng 4 hạch quanh đại tràng và quang trực tràng

### Group 232 — topic: Gastroenterology, Oncology, Pathology
Q: Tiên lượng của biểu mô đại tràng phụ thuộc vào các yếu tố sau ngoại trừ?
Options (shared set): ['Giới tính', 'Tình trạng di căn hạch', 'Độ xâm nhập vào các lớp của đại tràng', 'Độ biệt hoá mô học']
  line   1340 | Medium      | id 8027d41adfed433cbcd7cac1ae70e1bd | A -> Giới tính
  line   1761 | Medium      | id 2d606360fb7346f9a93333db20dbe07e | A -> giới tính

### Group 233 — topic: Gastroenterology, Oncology, Surgery
Q: Phân loại dukes sửa đổi, giai đoạn Duke B2 tương ứng với tổn thương nào sau đây?
Options (shared set): ['Tổn thương khu trú ở niêm mạc', 'Tổn thương lan hết vách ruột và có di căn', 'Tổn thương lan hết vách ruột nhưng không di căn', 'Tổn thương ăn lan nhưng không vượt qua cơ niêm']
  line   1341 | Medium      | id 78d7399b16784da3a5e286b6ef057a23 | C -> Tổn thương lan hết vách ruột nhưng không di căn
  line   1762 | Medium      | id 825f7ba29f394e589e1d429dce6366d2 | C -> tổn thương lan hết vách ruột nhưng không di căn

### Group 234 — topic: Gastroenterology, Oncology, Pathology
Q: Một trong những đặc điểm quan trọng của ung thư gan thể bè?
Options (shared set): ['Các bè gan nhiều hơn hai hàng', 'Các bè gan xếp không song song', 'Các bè gan dài', 'Các bè gan dày']
  line   1342 | Challenging | id 7dead97625a842cc9d9491a010881488 | A -> Các bè gan nhiều hơn hai hàng
  line   1763 | Challenging | id 23e773b59d1a40cc8ce321f772aa31b5 | A -> các bè gan nhiều hơn hai hàng

### Group 235 — topic: Gastroenterology, Pathology
Q: Một bệnh nhân vào nội soi thực quản dạ dày, sau khi được sinh thiết thực quản ở 1/3 dưới làm mô bệnh học, kết quả cho thấy biểu mô thực quản được phủ biểu mô hình trụ, các tuyến tế bào hình trụ, nhân nhỏ tròn đều, chất nhiễm sắc mịn, tạo hình ống tuyến. Kết luận nào sau đây là đúng nhất?
Options (shared set): ['Teo biểu mô thực quản', 'Loạn sản biểu mô thực quản', 'Dị sản biểu mô thực quản', 'Phì đại biểu mô thực quản']
  line   1344 | Challenging | id c418b6101ed84510ba4f4fc4d6a3270c | C -> Dị sản biểu mô thực quản
  line   1995 | Challenging | id 2ad93b6b33ac4dbab9b5ad97e79f301f | D -> Dị sản biểu mô thực quản
  line   2006 | Challenging | id 4f6cdedd3d7d4d8f8cdd0991e7aad697 | C -> Dị sản biểu mô thực quản

### Group 236 — topic: Gastroenterology, Infectious Diseases, Oncology
Q: Theo Tổ chức Y tế Thế giới, vi khuẩn HP được xếp vào nhóm nào trong các nguy cơ gây ung thư dạ dày?
Options (shared set): ['Nhóm 1', 'Nhóm 2', 'Nhóm 3', 'Nhóm 4']
  line   1347 | Easy        | id 1fdb7dd1fdd0454cb45836c2f689bb5c | A -> Nhóm 1
  line   2010 | Medium      | id 19330a830771417d970c42bf72e096ec | A -> Nhóm 1

### Group 237 — topic: Gastroenterology, Infectious Diseases, Oncology
Q: Yếu tố thuận lợi nào thường gây bệnh ung thư biểu mô tế bào gan?
Options (shared set): ['Viêm gan virus B hoặc D, Aflatoxin B1, tắc mật', 'Viêm gan virus B hoặc C, Aflatoxin B1, xơ gan', 'Viêm gan virus B hoặc E, Aflatoxin B1, xơ gan', 'Viêm gan virus B hoặc C, Aflatoxin B1, tắc mật']
  line   1348 | Medium      | id 06fd1e7067ab4933a97baecc8c8613c6 | B -> Viêm gan virus B hoặc C, Aflatoxin B1, xơ gan
  line   2002 | Medium      | id d4b386d7d86040ab8c74e691e3fc3226 | B -> Viêm gan virus B hoặc C, Aflatoxin B1, Xơ gan

### Group 238 — topic: Gastroenterology, Oncology
Q: Vị trí thường gặp nhất của ung thư dạ dày là vùng nào?
Options (shared set): ['Bờ cong nhỏ', 'Hang - môn vị', 'Tâm vị', 'Bờ Cong lớn']
  line   1349 | Easy        | id 67a9a5c0c55844b29e5e94a690239491 | B -> Hang - môn vị
  line   2001 | Medium      | id 59df0633be6e4683ba7dd6bdf17c8028 | B -> Hang - môn vị

### Group 239 — topic: Gastroenterology, Oncology, Pathology
Q: Trong ung thư gan, cấu trúc tuyến ống thường gặp trong:
Options (shared set): ['Ung thư biểu mô ống mật trong gan', 'Ung thư tế bào gan.', 'U nguyên bào gan', 'Ung thư không biệt hóa']
  line   1354 | Medium      | id 404563e95ff2447482ab1a4e27950895 | A -> Ung thư biểu mô ống mật trong gan
  line   1997 | Medium      | id 67f3df0f76b749f3864dac21e5359f19 | A -> Ung thư biểu mô ống mật trong gan
  line  10152 | Medium      | id e769d378dc9e4e0aae9d5027e5f84d3a | A -> Ung thư biểu mô ống mật trong gan

### Group 240 — topic: Gastroenterology, Oncology
Q: Hai loại ung thư gan nguyên phát thường gặp ở người lớn:
Options (shared set): ['Ung thư biểu mô tế bào gan (HCC) và ung thư nguyên bào gan', 'Ung thư nguyên bào gan và u lymphô ác tính', 'Ung thư biểu mô tế bào gan và ung thư biểu mô đường mật trong gan', 'Ung thư nguyên bào gan và biểu mô ống mật']
  line   1355 | Easy        | id 82f6a940a9524ce4a915f696d4188641 | C -> Ung thư biểu mô tế bào gan và ung thư biểu mô đường mật trong gan
  line   1996 | Easy        | id e0b5e37b0aa94915aec7f27ad402142e | C -> Ung thư biểu mô tế bào gan và ung thư biểu mô đường mật trong gan
  line   2017 | Easy        | id 2ac277719ad84ec28a4efa9db1599c57 | C -> Ung thư biểu mô tế bào gan và ung thư biểu mô đường mật trong gan

### Group 241 — topic: Gastroenterology, Infectious Diseases, Internal Medicine
Q: Biện pháp quan trọng nhất điều trị viêm gan siêu vi cấp là gì?
Options (shared set): ['Điều trị kháng virus tùy theo nguyên nhân', 'Điều trị hỗ trợ, giảm gánh nặng cho gan', 'Kháng sinh ngừa bội nhiễm', 'Các thuốc có nguồn gốc thảo dược có tác dụng tốt']
  line   1358 | Medium      | id e5110177b6e1475da3bb63fc949ccb39 | B -> Điều trị hỗ trợ, giảm gánh nặng cho gan
  line   1365 | Medium      | id 8bbce71577324cd2a34d572e6933b0f0 | B -> Điều trị hỗ trợ, giảm gánh nặng cho gan

### Group 242 — topic: Gastroenterology, Infectious Diseases, Internal Medicine
Q: Tiêu chuẩn chẩn đoán viêm gan siêu vi B cấp là gì?
Options (shared set): ['HBV DNA dương tính ít nhất 6 tháng', 'Men gan tăng gấp 2-5 ULN', 'HBsAg và HBeAg dương tính', 'HBsAg dương tính và biến mất trong vòng 6 tháng']
  line   1360 | Medium      | id 32bca427eed14664baee0856eb0b01b6 | D -> HBsAg dương tính và biến mất trong vòng 6 tháng
  line   1368 | Medium      | id f8a4be1ca5af4370ba3d4816d3566d1e | D -> HBsAg dương tính và biến mất trong vòng 6 tháng

### Group 243 — topic: Gastroenterology, Infectious Diseases, Internal Medicine
Q: Xét nghiệm để chẩn đoán viêm gan siêu vi B cấp trong giai đoạn cửa sổ miễn dịch là gì?
Options (shared set): ['HBsAg', 'HBeAg', 'IgM AntiHbc', 'Anti HBs']
  line   1362 | Challenging | id bf85fefae4054581a47be50fc656d26b | C -> IgM AntiHbc
  line   1370 | Challenging | id a7b090e0b6c14e4aa05bf4f99124dc8d | C -> IgM AntiHbc

### Group 244 — topic: Infectious Diseases, Pulmonology, Nephrology, Gastroenterology
Q: Xét nghiệm nào sau đây giúp đánh giá mức độ bệnh COVID-19?
Options (shared set): ['Công thức máu', 'Siêu âm phổi', 'Tets nhanh SARS-CoV-2', 'Chức năng gan, thận']
  line   1371 | Medium      | id 2205accd66ee4dc28eb62cd9f8162550 | D -> Chức năng gan, thận
  line   5039 | Medium      | id f3f71dfe458144edbd0f01db6d5b4fd2 | D -> Chức năng gan, thận
  line   5079 | Medium      | id c30e606ebe954fee94388a87a85d2f29 | D -> Chức năng gan, thận
  line   5163 | Medium      | id c716f9f3529e4cc08ea4790f256e44eb | B -> Siêu âm phổi

### Group 245 — topic: Infectious Diseases, Gastroenterology
Q: Xét nghiệm để chẩn đoán viêm gan siêu vi B cấp trong giai đoạn cửa sổ miễn dịch là?
Options (shared set): ['HBsAg', 'HBeAg', 'IgM AntiHbc', 'Anti HBs']
  line   1381 | Challenging | id bad797faed41438c8eeb62893cad7ee2 | C -> IgM AntiHbc
  line   9071 | Challenging | id ec09317bc0c84e15a0da4569d14786e0 | C -> IgM AntiHbc

### Group 246 — topic: Gastroenterology, Surgery
Q: Bệnh nhân bị trĩ chấp nhận đi khám và chữa trị rất muộn vì: bệnh nhân không phát hiện ra bị bệnh
Options (shared set): ['Đ', 'S']
  line   1428 | Easy        | id 3dbd10d038db4a56bec3325ffd2f19d0 | B -> S
  line   9629 | Medium      | id bd1edc5a97bc4500b1aded512363ca9a | B -> S

### Group 247 — topic: Pediatrics, Gastroenterology
Q: Nguyên nhân xuất huyết tiêu hoá trên thường gặp nhất ở trẻ nhũ nhi là gì?
Options (shared set): ['Hội chứng Mallory - Weiss', 'Giãn vỡ tĩnh mạch thực quản', 'Viêm loét dạ dày tá tràng', 'Dị dạng mạch máu']
  line   1487 | Medium      | id bd66d54c365b43288999dd956f9ec6cb | C -> Viêm loét dạ dày tá tràng
  line   1826 | Medium      | id 78bd1aaec6b44b6cb9e2dff5a34de44d | C -> viêm loét dạ dày tá tràng
  line   1979 | Medium      | id 4f64d163454148f08e0564f1823293dd | C -> Viêm loét dạ dày tá tràng

### Group 248 — topic: Pediatrics, Gastroenterology
Q: Xuất huyết tiêu hoá dưới do lồng ruột có biểu hiện nào sau đây?
Options (shared set): ['Thường gặp ở trẻ <6 tháng tuổi', 'Tiêu phân nhầy máu mũi', 'Triệu chứng xuất hiện âm thầm, dai dẳng', 'Khó phát hiện khối lồng bằng siêu âm']
  line   1488 | Medium      | id 39637eed34b54723bc25b8541bdbe547 | B -> Tiêu phân nhầy máu mũi
  line   1828 | Medium      | id 260b566d61a44c4397416b7b4555a9ba | B -> Tiêu phân nhầy máu mũi
  line   1981 | Medium      | id f357d54564704c779ef85d30e63e13cd | B -> Tiêu phân nhầy máu mũi

### Group 249 — topic: Pediatrics, Gastroenterology, Pulmonology
Q: Đau bụng tái diễn trừ:
Options (shared set): ['Lồng ruột non', 'B.Viêm đáy phổi P', 'C.U nang ống mật chủ', 'D.Xoay ruột dở dang']
  line   1490 | Challenging | id b073422e0e3a45cd948d29af82d8b222 | B -> B.Viêm đáy phổi P
  line   5130 | Medium      | id 4eb1bbdfe4d84101b96d6d7c35c69099 | B -> B.Viêm đáy phổi P

### Group 250 — topic: Gastroenterology, Internal Medicine
Q: Các yếu tố cần điều chỉnh trước khi dùng thuốc lợi tiểu cho BN báng bụng?
Options (shared set): ['XHTH, suy thận, hạ Natri máu, tăng Kali máu', 'HC gan phổi, suy thận, bệnh não gan, hạ Natri máu', 'Bệnh thận mạn, XHTH, bệnh não gan, tăng Kali máu', 'Suy thượng thận, suy gan cấp, hạ Kali máu, hạ Natri máu']
  line   1497 | Challenging | id 6e93e69ded174d8eb9121feb466aabfa | A -> XHTH, suy thận, hạ Natri máu, tăng Kali máu
  line   1877 | Challenging | id cf658229ad81445492ee0edac0e32b7c | A -> XHTH, suy thận, hạ Natri máu, tăng Kali máu
  line   1974 | Challenging | id cc6c550293b34ab98933123769d85da7 | A -> XHTH, suy thận, hạ Natri máu, tăng Kali máu

### Group 251 — topic: Gastroenterology, Internal Medicine
Q: Chuột rút ở BN xơ gan: chọn câu đúng
Options (shared set): ['Điều trị bằng lợi tiểu', 'Điều trị bằng albumin', 'Điều trị bằng chế độ ăn', 'Điều trị bằng baclofen 50mg/ngày']
  line   1498 | Challenging | id 9ae5e2931ee34953936e73aa475b3d7c | B -> Điều trị bằng albumin
  line   1503 | Challenging | id 6b9ee78b7f194c2fa07b62ac51fb1ffb | B -> Điều trị bằng albumin

### Group 252 — topic: Gastroenterology, Internal Medicine
Q: Hội chứng PPCD: post paracentesis circulatory dysfuction biểu hiện
Options (shared set): ['Suy thận', 'Tăng Natri máu', 'Tăng Kali máu', 'XHTH']
  line   1499 | Easy        | id ad810acfa6994bc988ae2347374e2976 | A -> Suy thận
  line   1870 | Medium      | id 684b0e1335b24940a066209d0268df08 | A -> Suy thận

### Group 253 — topic: Gastroenterology, Infectious Diseases, Internal Medicine
Q: Chẩn đoán và điều trị viêm phúc mạc nhiễm khuẩn tự phát: chọn câu đúng?
Options (shared set): ['Chọc dịch báng xét nghiệm trước khi điều trị kháng sinh ở tất cả các BN nghi ngờ viêm phúc mạc nhiễm khuẩn tự phát', 'Chờ kết quả kháng sinh đồ và lựa chọn kháng sinh điều trị', 'Tránh điều trị kháng sinh theo kinh nghiệm để đề phòng kháng thuốc', 'Đánh giá điều trị sau 72 giờ: gọi là thất bại nếu triệu chứng lâm sàng không giảm hoặc nặng hơn.']
  line   1500 | Challenging | id 11c33da701444391a716035565f47685 | A -> Chọc dịch báng xét nghiệm trước khi điều trị kháng sinh ở tất cả các BN nghi ngờ viêm phúc mạc nhiễm khuẩn tự phát
  line   1874 | Challenging | id e6ab30161d994a33a109068d19ec3add | A -> Chọc dịch báng xét nghiệm trước khi điều trị kháng sinh ở tất cả các BN nghi ngờ viêm phúc mạc nhiễm khuẩn tự phát

### Group 254 — topic: Gastroenterology, Internal Medicine
Q: Phân loại suy gan cấp nào là phù hợp?
Options (shared set): ['Tối cấp: xuất hiện bệnh não gan dưới 6 tuần từ khi khởi phát', 'Tối cấp: xuất hiện bệnh não gan dưới 8 tuần từ khi khởi phát', 'Gần tối cấp: xuất hiện bệnh não gan dưới 6 – 26 tuần từ khi khởi phát', 'Tối cấp: xuất hiện bệnh não gan dưới 8 – 28 tuần từ khi khởi phát']
  line   1501 | Medium      | id 206a856cb3974cb895798da8a197c324 | B -> Tối cấp: xuất hiện bệnh não gan dưới 8 tuần từ khi khởi phát
  line   1505 | Medium      | id 5f57ced8a28f46b092499c1b5908a33d | B -> Tối cấp: xuất hiện bệnh não gan dưới 8 tuần từ khi khởi phát
  line   1863 | Medium      | id 7f3a081b20b746bdb5887427be7271f4 | B -> Tối cấp: xuất hiện bệnh não gan dưới 8 tuần từ khi khởi phát
  line   1876 | Medium      | id 98d7998037f1426489630de8ac904421 | B -> Tối cấp: xuất hiện bệnh não gan dưới 8 tuần từ khi khởi phát
  line   1970 | Medium      | id 3623e7bb5c9040a0b915a61e7fe60949 | B -> Tối cấp: xuất hiện bệnh não gan dưới 8 tuần từ khi khởi phát
  line   1975 | Medium      | id 6757e84491f74e91bb3052cebd94f850 | B -> Tối cấp: xuất hiện bệnh não gan dưới 8 tuần từ khi khởi phát

### Group 255 — topic: Nephrology, Gastroenterology, Endocrinology
Q: Hạ Na máu kèm theo giảm thể tích ngoài tế bào nào sau đây đúng (Na niệu < 20 mmol/L)?
Options (shared set): ['Hội chứng thận hư, xơ gan cổ chứng, suy thượng thận, suy tim.', 'Do dùng lợi tiểu, suy thượng thận, bệnh thận kẽ.', 'Mồ hôi, bỏng, chấn thương, tiêu chảy nôn, dò tiêu hoá.', 'Mất qua da, chấn thương, qua tiêu hoá, suy giáp.']
  line   1506 | Medium      | id 02ab4d7dd7394d01adfd7c47ad5f3f9d | C -> Mồ hôi, bỏng, chấn thương, tiêu chảy nôn, dò tiêu hoá.
  line   6768 | Medium      | id ec8fce20b23d4e52a6347dc796c0720f | C -> Mồ hôi, bỏng, chấn thương, tiêu chảy nôn, dò tiêu hoá.

### Group 256 — topic: Endocrinology, Internal Medicine, Gastroenterology
Q: Tác dụng phụ khi dùng Nhóm thuốc Biguanides - Metformin này?
Options (shared set): ['Tiêu chảy đầy bụng, nôn ói, chán ăn có vị tanh kim loại.', 'Tăng cân, hạ đường huyết, phát ban', 'Đầy bụng, sinh hơi, tiêu chảy.', 'Tăng cân, hạ đường huyết, tiêu chảy.']
  line   1507 | Medium      | id c0ce4141d11949059f9779988a1161b5 | A -> Tiêu chảy đầy bụng, nôn ói, chán ăn có vị tanh kim loại.
  line   6776 | Medium      | id dc64cae9b2de4ab9a717cb39abd75d0d | A -> Tiêu chảy đầy bụng, nôn ói, chán ăn có vị tanh kim loại.

### Group 257 — topic: Endocrinology, Gastroenterology
Q: Theo nghiên cứu của Talcashi Satoh- Journal of Ethnopharmacology - Volume 161 . 23 February 2015 dịch chiết nước trà có thể làm giảm hấp thu Glucose tại ruột do tác động nào sau đây?
Options (shared set): ['Ức chế α glucosidase', 'Ức chế α galactosidase', 'Ức chế α amylase', 'Ức chế α amylase và α glucosidase']
  line   1514 | Challenging | id 11a72611fba1466189f698475402739a | A -> Ức chế α glucosidase
  line   6123 | Medium      | id 8aa37bc9da1e440f9f4e143db3e1fc3d | A -> Ức chế α glucosidase

### Group 258 — topic: Gastroenterology
Q: Nguyên nhân làm mất khoảng Traube dạ dày khi gõ?
Options (shared set): ['Gan to', 'U dạ dày', 'Lách to và u dạ dày', 'Gan to và u dạ dày']
  line   1532 | Medium      | id 4b60c5d5c97144028cdf80642f0dca1d | D -> Gan to và u dạ dày
  line  10598 | Medium      | id 6fbd50a4ede64777afddc7dd756fec2a | D -> Gan to và u dạ dày

### Group 259 — topic: Gastroenterology, Surgery
Q: Bệnh lý nào sau đây gây đau bụng vùng thượng vị có tính chất cấp cứu ngoại khoa?
Options (shared set): ['Áp xe ruột thừa vỡ', 'Viêm tụy hoại tử xuất huyết', 'Sỏi túi mật', 'Nang gan']
  line   1541 | Challenging | id b8a511cd5d6a45718d33abdd9d3f3e0f | B -> Viêm tụy hoại tử xuất huyết
  line   9657 | Medium      | id 972c071a82f545228451fab10481d423 | B -> Viêm tụy hoại tử xuất huyết

### Group 260 — topic: Gastroenterology, Hematology, Endocrinology
Q: Tăng bilirubin tự do gặp trong các trường hợp sau, NGOẠI TRỪ:
Options (shared set): ['Nhịn đói kéo dài', 'Do uống probenecid', 'Do uống methyl testosterone', 'Hội chứng Gilbert']
  line   1551 | Challenging | id b376886eb2e84f67a7d73e3cba02c0c0 | C -> Do uống methyl testosterone
  line   6127 | Medium      | id 10c520f76f37417e8a290de7ca689bff | C -> Do uống methyl testosterone

### Group 261 — topic: Obstetrics and Gynecology, Gastroenterology, Infectious Diseases
Q: Lao màng bụng nữ hay gặp ở độ tuổi
Options (shared set): ['“ mãn kinh”', '“ sinh đẻ”', '“ chưa sinh đẻ”', '“ dậy thì”']
  line   1561 | Easy        | id a113ede9a6a14dabba289d1f9e530422 | B -> “ sinh đẻ”
  line   3600 | Medium      | id 7d4a0d50ef8741d2b373b24d36d0fe3e | B -> “ sinh đẻ”

### Group 262 — topic: Endocrinology, Gastroenterology
Q: _________ là các quá trình hóa học và vật lý mà một sinh vật sống sử dụng thức ăn để tạo năng lượng và phát triển.
Options (shared set): ['sự trao đổi chất', 'đơn thuốc', 'độc chất học']
  line   1562 | Easy        | id eb0ec1e7ce614737894d06c8e2aa72e6 | A -> sự trao đổi chất
  line   6305 | Easy        | id c80413c91d9c4c459473c7b542d38740 | A -> sự trao đổi chất

### Group 263 — topic: Endocrinology, Gastroenterology
Q: các quá trình hóa học và vật lý mà một sinh vật sống sử dụng thức ăn để tạo năng lượng và phát triển
Options (shared set): ['sự trao đổi chất', 'ác tính', 'thuốc giải độc']
  line   1563 | Easy        | id 2a5ea9d66d134f4d816a479783ef4038 | A -> sự trao đổi chất
  line   6306 | Easy        | id cd1819d9a3114690993433724dee9d70 | A -> sự trao đổi chất
  line  10554 | Easy        | id 6cb03303913b45f4925f8d95b5d99cd1 | A -> sự trao đổi chất

### Group 264 — topic: Oncology, Gastroenterology
Q: Tỉ lệ mắc ung thư đại tràng giữa nam và nữ như thế nào?
Options (shared set): ['Nam nhiều gấp đôi nữ.', 'Nữ nhiều gấp đôi nam.', 'Nam và nữ bằng nhau.', 'Nam nhiều gấp 1,5 lần nữ.']
  line   1574 | Easy        | id 0066e40aabe2471cb8e93ba51abdf65c | D -> Nam nhiều gấp 1,5 lần nữ.
  line  10638 | Easy        | id 4f932cd31a2d4439aaef8b489edc7803 | D -> Nam nhiều gấp 1,5 lần nữ.

### Group 265 — topic: Oncology, Gastroenterology, Pathology
Q: Ung thư biểu mô tuyến đại tràng có tiên lượng xấu nhất thuộc loại nào?
Options (shared set): ['Biệt hoá cao .', 'Biệt hoá vừa .', 'Biệt hoá thấp .', 'Loại không biệt hoá']
  line   1577 | Medium      | id d2ec8e0f269045c19243478369450383 | D -> Loại không biệt hoá
  line   1610 | Medium      | id a4069d38abad4dfd869b6c921ff5ebcc | A -> Loại không biệt hóa
  line   1620 | Medium      | id 04b91faf2f18436ea1cc01f5dd64520a | D -> Loại không biệt hoá
  line  10583 | Medium      | id 090215da82c04b6b86f282afbaf5d2cd | C -> Biệt hoá thấp .

### Group 266 — topic: Gastroenterology, Oncology
Q: Hãy tìm ra câu trả lời đúng về nguy cơ cao nhất dẫn đến ung thư tế bào gan
Options (shared set): ['Xơ gan (không phân biệt nguyên nhân) .', 'Viêm gan B mạn tính .', 'Viêm gan C mạn tính .', 'Viêm gan do rượu .']
  line   1580 | Medium      | id dd4161a2c7b8497899a63028821d9808 | A -> Xơ gan (không phân biệt nguyên nhân) .
  line   1622 | Medium      | id f638800815c84a7ba32407801a8144f5 | A -> Xơ gan (không phân biệt nguyên nhân)

### Group 267 — topic: Gastroenterology, Oncology
Q: Trong ung thư gan nguyên phát thì ung thư tế bào gan (HCC) chiếm:
Options (shared set): ['80-90%', 'Không học về quê lấy chồng']
  line   1585 | Medium      | id a04df705c2344161b3c66bc0dd9bee09 | A -> 80-90%
  line  10079 | Easy        | id abbbfab2d2f44ad1909ef7b18d02cef8 | A -> 80-90%

### Group 268 — topic: Gastroenterology, Oncology
Q: Hãy tìm ra câu trả lời đúng nhất trong các câu trả lời dưới đây
Options (shared set): ['Chẩn đoán xác định ung thư tế bào gan bắt buột phải tiến sinh thiết gan để làm chẩn đoán tế bào học', 'Chẩn đoán xác định ung thư tế bào chỉ tiến hành sinh thiết, làm chẩn đoán bào học khi các phương pháp khác không đủ dữ liệu chấn đoán xác định', 'C. Chẩn đoán xác định ủng thư tế bào gan 1 chỉ cần dựa vào xét nghiệm AFP> 200ng/ml', 'D. Chẩn đoán xác định ung thư tế bào gan chỉ cần dựa vào siêu âm Dopple']
  line   1591 | Challenging | id 5d718b0f9522453ebf4de5b4249ef4f8 | B -> Chẩn đoán xác định ung thư tế bào chỉ tiến hành sinh thiết, làm chẩn đoán bào học khi các phương pháp khác không đủ dữ liệu chấn đoán xác định
  line  10595 | Medium      | id 3cdd3c5b785b4f66aa9b08fe882799b5 | B -> Chẩn đoán xác định ung thư tế bào chỉ tiến hành sinh thiết, làm chẩn đoán bào học khi các phương pháp khác không đủ dữ liệu chấn đoán xác định

### Group 269 — topic: Infectious Diseases, Pulmonology, Gastroenterology
Q: Vi khuẩn lao lan tràn đến màng bụng bằng con đường nào?
Options (shared set): ['Đường máu', 'Cả 3 đường', 'Tiếp cận', 'Bạch huyết']
  line   1619 | Medium      | id 6fb77bb12a3e41cab9fb0f0a94ea1ab3 | B -> Cả 3 đường
  line   5318 | Medium      | id c56249ed52a54cc4ab0ede309e9f65bc | B -> Cả 3 đường

### Group 270 — topic: Nephrology, Gastroenterology, Endocrinology
Q: Khi nói đến bệnh nhân suy thận và gan nên uống?
Options (shared set): ['D2', 'Pre D3', 'Calcitriol', 'Calcifediol']
  line   1628 | Challenging | id 9f230b298aff448e904cd8b12ff20fc9 | C -> Calcitriol
  line   6128 | Medium      | id 9e1f2411438a4ca9bd01622f6f8ca183 | C -> Calcitriol

### Group 271 — topic: Gastroenterology, Infectious Diseases
Q: Helicobacter pylori không tiết ra chất nào sau đây?
Options (shared set): ['Urease', 'Protease', 'Lipase', 'Bicarbonat']
  line   1632 | Medium      | id 5c9f5234f5034d158fc5bdff74c606dc | D -> Bicarbonat
  line   1639 | Medium      | id 683e4c3047d847b9926af29ac64cd2f9 | D -> Bicarbonat

### Group 272 — topic: Gastroenterology
Q: Phát biểu nào về Dexlansoprazol là không đúng?
Options (shared set): ['Thuốc chỉ nên dùng 1lần/ ngày cho tất cả các chỉ định vì tác dụng của thuốc kéo dài', 'Thuốc cần môi trường dạng acid để chuyển thành dạng hoạt tính', 'Cơ chế tác dụng của thuốc là ức chế bơm proton ở thành tế bào', 'Khi dùng thuốc lâu dài bệnh nhân tăng nguy cơ nhiễm trùng']
  line   1635 | Challenging | id e795abcc20274a62a03549640175b72f | A -> Thuốc chỉ nên dùng 1lần/ ngày cho tất cả các chỉ định vì tác dụng của thuốc kéo dài
  line  10636 | Medium      | id 82949521b46147379f12b5164ad01de3 | A -> Thuốc chỉ nên dùng 1lần/ ngày cho tất cả các chỉ định vì tác dụng của thuốc kéo dài

### Group 273 — topic: Hematology, Gastroenterology
Q: Thiếu Vitamin B12 có thể gây ra :
Options (shared set): ['Thiếu máu ưu sắc, hồng cầu to', 'Thiếu máu nhược sắc, hồng cầu nhỏ', 'Thời gian đông máu tăng', 'Thời gian chảy máu tăng']
  line   1643 | Medium      | id 0a79fc41e06a4620871e6c7db3178629 | A -> Thiếu máu ưu sắc, hồng cầu to
  line   1644 | Medium      | id 2212b74884ca4695a029bab6606a03d9 | A -> Thiếu máu ưu sắc, hồng cầu to

### Group 274 — topic: Endocrinology, Gastroenterology
Q: Cách khắc phục tác dụng phụ tiêu chảy của Metformin:
Options (shared set): ['Uống trước khi ăn', 'Tăng liều dần dần, sử dụng dạng phóng thích kéo dài', 'Uống cách xa bữa ăn', 'Tất cả đều đúng.']
  line   1646 | Medium      | id e04a4401d1394797839ae1a68449efb2 | B -> Tăng liều dần dần, sử dụng dạng phóng thích kéo dài
  line   6803 | Medium      | id 220cd1222a23408a877f016b91434f8f | B -> Tăng liều dần dần, sử dụng dạng phóng thích kéo dài

### Group 275 — topic: Infectious Diseases, Pulmonology, Gastroenterology
Q: Thuốc kháng lao nào sau đây ít có nguy cơ gây độc trên gan nhất?
Options (shared set): ['Ethambutol', 'Isoniazid', 'Pyrazinamide', 'Rifampicin']
  line   1651 | Medium      | id 0d70c8e0377546018439c6c1f867609a | A -> Ethambutol
  line   5358 | Medium      | id 7c1686b887d94445bbd488f381d9cb1b | A -> Ethambutol

### Group 276 — topic: Endocrinology, Gastroenterology
Q: Cho 2 phản ứng.
Glycogen → Glucose-1-phosphat → Glucose-6-phosphat
Tập hợp các enzym nào dưới đầy xúc tác 2 phản ứng trên?
Options (shared set): ['Glucokinase; isomerase', 'Phosphorylase, phosphogluco isomerase', 'Phosphorylase, phosphogluco mutase', 'Hexokinase, phosphoglucomutase']
  line   1662 | Medium      | id 9c97c40556174c01a0f61c2a7972d70e | C -> Phosphorylase, phosphogluco mutase
  line   6824 | Medium      | id 2326a3720ac747a5bc2c05ddb715f249 | C -> Phosphorylase, phosphogluco mutase

### Group 277 — topic: Gastroenterology, Endocrinology
Q: Mục đích quan trọng nhất của glycogenlysis ở gan là:
Options (shared set): ['Cung Sắp ATP cho tổ chức gan hoạt động', 'Cung cấp glucose tự do, là nguyên liệu cần thiết cho sự hoạt động của gan', 'Cung cấp glucose, là tiền nguyên liệu cần thiết tổng hợp acid glucuronic tham gia vào quá trình khử độc tại gan', 'Cung cấp glucose tự do cho máu, từ đó phân phối tổ chức']
  line   1663 | Medium      | id 695441280c4247518a81a0685d254f69 | D -> Cung cấp glucose tự do cho máu, từ đó phân phối tổ chức
  line   6825 | Medium      | id 2fd1dd6ebcfc4b46ad38d5d6f121c4e5 | D -> Cung cấp glucose tự do cho máu, từ đó phân phối tổ chức

### Group 278 — topic: Gastroenterology
Q: Amylase là enzym thủy phân tinh bột được tiết bởi:
Options (shared set): ['Tuyến nước bọt, dịch vị', 'Tuyến nước bọt, dịch tụy', 'Tuyến nước bọt, dịch vị và dịch tụy', 'Tuyến nước bọt, ruột non']
  line   1664 | Easy        | id a78e6aed35cf4696898551520ca9eb58 | B -> Tuyến nước bọt, dịch tụy
  line   1894 | Easy        | id 8502a023d7b8494999d8b5c037df16ed | B -> Tuyến nước bọt, dịch tụy

### Group 279 — topic: Gastroenterology
Q: Loại enzym nào sau đây hoạt động tối ưu ở pH acid:
Options (shared set): ['Amylase nước bọt và tụy', 'Chymotrypsin tụy', 'Trypsin tụy', 'Pepsin dịch vị']
  line   1665 | Medium      | id a67a99b4d98f4dde9613ad803fe7fb16 | D -> Pepsin dịch vị
  line   1893 | Medium      | id 8eb0dcbe380d4b8294e9a3fe8859f934 | D -> Pepsin dịch vị

### Group 280 — topic: Gastroenterology
Q: Loại enzym nào sau đây hoạt động tối ưu ở pH trung tính:
Options (shared set): ['Amylase nước bọt', 'Pepsin dịch vị', 'Typsin dịch tụy', 'Chymotrysin dịch tụy']
  line   1666 | Medium      | id d7749e541ad0419184b1e8569bcddf8b | A -> Amylase nước bọt
  line   1895 | Medium      | id f574523dbdc44e8bbbad5d6449621454 | A -> Amylase nước bọt

### Group 281 — topic: Gastroenterology
Q: Nhóm enzym nào sau đây thủy phân tinh bột và các loại disacarid:
Options (shared set): ['Amylase, maltase, lactase, lipase', 'Amylase, maltase, pepsin, trypsin', 'Amylase, pepsin, trypsin, chymotrypsin', 'Maltase, lactase, sacarase']
  line   1667 | Medium      | id f09ba508d10b41398b479901f3e51c3b | D -> Maltase, lactase, sacarase
  line   1896 | Medium      | id 18ac48ccd63b4d51b987e7b9af4e13de | D -> Maltase, lactase, sacarase

### Group 282 — topic: Gastroenterology
Q: Chọn câu đúng:
Options (shared set): ['pH thích hợp của pepsin =7', 'pH thích hợp của trypsin=1,5', 'pH thích hợp của chymotrypsin = 6', 'pH thích hợp của amylase nước bọt =7']
  line   1670 | Medium      | id 82809deaa3694322bfbc1e4610282b6f | D -> pH thích hợp của amylase nước bọt =7
  line   1898 | Medium      | id 67fdf25856ba4cc6b76f07827461e283 | D -> pH thích hợp của amylase nước bọt =7

### Group 283 — topic: Geriatrics, Gastroenterology
Q: Sau 60 tuổi, quá trình hấp thu các chất bị ảnh hưởng , NGOẠI TRỪ
Options (shared set): ['Hấp thu lactose, mannitol , vit B12', 'Giảm hấp thu vitD, axit Folic', 'Giảm hấp thu axit béo và Cholesterol', 'Giảm hấp thu Calci, tăng hấp thu Đồng và Kẽm']
  line   1671 | Medium      | id f52a452b322148fc8f07140ebff66aea | D -> Giảm hấp thu Calci, tăng hấp thu Đồng và Kẽm
  line  10750 | Medium      | id 741a5a8913774f979acc29a0295efe50 | A -> Hấp thu lactose, mannitol , vit B12

### Group 284 — topic: Endocrinology, Gastroenterology
Q: Nhiễm độc giáp tác động đến tiêu hóa như thế nào?
Options (shared set): ['Nôn, vàng da, táo bón', 'Ăn nhiều gầy nhiều, tiêu chảy', 'Nôn, tiêu chảy, gan to', 'Nôn, tiêu chảy, vàng da']
  line   1675 | Medium      | id f6d2cc6fb30647a6bd038dad445a2dd2 | B -> Ăn nhiều gầy nhiều, tiêu chảy
  line   6839 | Medium      | id 89fe1755e9484a16af88cffc861e6cc4 | D -> Nôn, tiêu chảy, vàng da

### Group 285 — topic: Endocrinology, Gastroenterology
Q: RL tiêu hóa ở bệnh nhân Basedow biểu hiện
Options (shared set): ['Phân lỏng, nát', 'Khó tiêu', 'Phân khô, rắn', 'Đầy hơi']
  line   1676 | Easy        | id 7b999ede8062438f8013789580b5f373 | A -> Phân lỏng, nát
  line   6858 | Medium      | id 9d72ca8b085b4980b69fa698f6ae2230 | A -> Phân lỏng, nát

### Group 286 — topic: Oncology, Gastroenterology
Q: Các yếu tố làm tăng nguy cơ ung thư đại tràng là:
Options (shared set): ['Thức ăn dầu mỡ và đạm động vật', 'Thức ăn có nhiều rau', 'Hoa quả', 'Vi rút viêm gan B']
  line   1681 | Easy        | id ac4bf8740683417887417164846f6560 | A -> Thức ăn dầu mỡ và đạm động vật
  line   1712 | Easy        | id 127c6780a8f441498ad20ed3cbd0d6d7 | A -> Thức ăn dầu mỡ và đạm động vật

### Group 287 — topic: Gastroenterology, Pathology
Q: Khi cắt bỏ một phần gan, phần còn lại phải hoạt động bù trừ, trong trường hợp này, tế bào gan to ra một cách sinh lý?
Options (shared set): ['Đúng', 'Sai']
  line   1715 | Challenging | id e30242e66ce849bab9b3d39164193bc6 | B -> Sai
  line   9698 | Medium      | id ca3af311b53d4ce487c11349fabffecf | B -> Sai

### Group 288 — topic: Pathology, Gastroenterology, Pulmonology
Q: Mảnh bệnh phẩm nội soi (dạ dày, phế quản, đại tràng...) gửi làm sinh thiết lạnh tốt nhất nên:
Options (shared set): ['Áp ra một vài lam rồi gửi tươi ngay trong 15 phút', 'Cố định ngay trong dung dịch phù hợp, gửi trong ngày', 'Không cố định, gửi ngay trong 15 phút', 'Áp ra một vài lam rồi cố định, gửi trong ngày']
  line   1717 | Medium      | id 563613a6b8c5404198b31b6567fdd432 | A -> Áp ra một vài lam rồi gửi tươi ngay trong 15 phút
  line   5375 | Medium      | id 6fc3d10d956d4666955e85389391d798 | A -> Áp ra một vài lam rồi gửi tươi ngay trong 15 phút

### Group 289 — topic: Gastroenterology, Pulmonology, Oncology
Q: Yếu tố di truyền trong ung thư dạ dày cao hơn hẳn trong ung thư phế quản phải không?
Options (shared set): ['Đúng', 'Sai']
  line   1741 | Easy        | id 07b6560d3d9b458f982d8b2db69268f6 | A -> Đúng
  line   5398 | Medium      | id 2e74cdc602554ae897aa04deacdb9448 | A -> Đúng

### Group 290 — topic: Endocrinology, Gastroenterology
Q: Tiểu đường ít gây tổn thương vi mạch ở:
Options (shared set): ['mắt.', 'da.', 'thận.', 'ruột']
  line   1743 | Medium      | id 1dcf2f813b25407f859573d6c2f98479 | D -> ruột
  line   6900 | Medium      | id 3d66da33d76c495a9f3dc7c592af070b | D -> ruột

### Group 291 — topic: Oncology, Gastroenterology, Pathology
Q: Loại mô bệnh học phổ biến nhất của ung thư dạ dày là gì?
Options (shared set): ['Ung thư biểu mô tuyến', 'Ung thư biểu mô không xếp loại', 'Ung thư biểu mô không biệt hoá', 'Ung thư biểu mô tế bào vảy']
  line   1764 | Medium      | id 60eba0762fd94b248d44b17d50e2ee39 | A -> Ung thư biểu mô tuyến
  line  10101 | Medium      | id 62e38c84e46446b1b8c2b678f3718f9a | A -> Ung thư biểu mô tuyến

### Group 292 — topic: Obstetrics and Gynecology, Gastroenterology
Q: Chọn 1 câu sai về chẩn đoán phân biệt của thai ngoài TC:
Options (shared set): ['Sẩy thai', 'Lỵ amip', 'Vỡ nang degraff', 'Viêm phần phụ']
  line   1766 | Challenging | id aa97c2e2ccb140488bc91a9e6bb2f007 | B -> Lỵ amip
  line   3599 | Challenging | id 3e97a5d7a777421590f372801fc4dc64 | B -> Lỵ amip

### Group 293 — topic: Infectious Diseases, Gastroenterology
Q: đây là gì
Options (shared set): ['trứng giun tóc', 'trứng giun đũa', 'trứng giun móc', 'trứng giun kim']
  line   1767 | Medium      | id 76c400d1a93d41698b8f1161cc79b80f | A -> trứng giun tóc
  line   1768 | Medium      | id 2e08db5f2bd2432aac2648f54a897879 | A -> trứng giun đũa
  line   1769 | Medium      | id a36e2051ec994a44b7bab48087fa200c | B -> trứng giun móc

### Group 294 — topic: Infectious Diseases, Gastroenterology
Q: đây là gì
Options (shared set): ['trứng giun kim', 'trứng giun móc', 'trứng sán là gan nhỏ', 'trứng sán là ruột lớn']
  line   1770 | Medium      | id 65e57b882c8f4b61b6a3a5f25ce14d8b | A -> trứng giun kim
  line  10565 | Medium      | id 1e71505e68c142d3ac1d5211fe26ce21 | A -> trứng giun kim

### Group 295 — topic: Infectious Diseases, Gastroenterology
Q: Đây là gì?
Options (shared set): ['Trứng sán lá ruột lớn', 'Trứng sán dây', 'Trứng sán lá gan nhỏ', 'Trứng sán lá phổi']
  line   1772 | Medium      | id 46f15e95ab5e4d1a87e44f75b3e8aacb | A -> Trứng sán lá ruột lớn
  line   1773 | Medium      | id e32fa65252a048b681a615fad3308648 | A -> Trứng sán lá gan nhỏ

### Group 296 — topic: Pulmonology, Gastroenterology
Q: Trong các nguyên nhân sau đây có nguyên nhân KHÔNG gây tràn khí trung thất, đó là:
Options (shared set): ['Thủng dạ dày', 'Thủng thực quản', 'Vỡ khí phế quản', 'Vỡ kén khí phế nang']
  line   1777 | Challenging | id eaafc17fb8c740d890b28383fe34835c | A -> Thủng dạ dày
  line   5612 | Medium      | id 9e0193ac3d0447518d383da1b205fa24 | A -> Thủng dạ dày

### Group 297 — topic: Pulmonology, Gastroenterology
Q: Ho khan tăng khi nằm, về đêm , nóng rát sau ức
Options (shared set): ['Hen', 'Bệnh mạch vành', 'Suy tim', 'Trào ngược dạ dày thực quản']
  line   1778 | Challenging | id 86c7c84b21734296b729c97be89a41bb | D -> Trào ngược dạ dày thực quản
  line   5702 | Medium      | id 986922459e7a488b939123e3f0b365bf | D -> Trào ngược dạ dày thực quản

### Group 298 — topic: Gastroenterology, Pediatrics
Q: Tiêu chuẩn chẩn đoán nhiễm HP ở trẻ viêm loét dạ dày tá tràng là gì?
Options (shared set): ['Clotest và PCR', 'Sinh thiết mô học và Clotest', 'XN có Hp trong phân', 'Test Hp hơi thở dương tính']
  line   1829 | Medium      | id fbe2639041004b2b96dbd33c41a417cc | B -> Sinh thiết mô học và Clotest
  line   1963 | Medium      | id 806e229941c74dc7af9b9a048c733878 | B -> *Sinh thiết mô học và Clotest
  line   1984 | Medium      | id 660dbcf0b9a3498c97c325518418fbd2 | B -> Sinh thiết mô học và Clotest

### Group 299 — topic: Gastroenterology, Pediatrics
Q: Nguyên nhân XHTH trên thường gặp nhất ở trẻ sơ sinh là gì?
Options (shared set): ['Thiếu Vitamin K', 'Viêm thực quản', 'VLDDTT', 'HC Mallory Wess']
  line   1831 | Medium      | id 8e70db59e10446d19ea0f814430c0bbe | A -> Thiếu Vitamin K
  line   1964 | Medium      | id 3b1b00679bc149d7b05e81f8304b2176 | A -> *Thiếu Vitamin K

### Group 300 — topic: Gastroenterology, Pediatrics
Q: Nguyên nhân XHTH dưới thường gặp nhất ở trẻ dưới 3 tháng tuổi là gì?
Options (shared set): ['Viêm túi thừa mackel', 'Lồng ruột', 'Polyp đại trực tràng', 'Trĩ']
  line   1832 | Medium      | id 34ff4078e0f84787898e9191e65ea609 | B -> Lồng ruột
  line   1965 | Medium      | id 75bf83ad4a964523b4aee7d354800278 | B -> *Lồng ruột
  line   1987 | Medium      | id 4bde7714664240ff9af25ad2ba503521 | B -> Lồng ruột

### Group 301 — topic: Gastroenterology
Q: XHTH do dãn vỡ tĩnh mạch thực quản có có các biểu hiện nào sau
Options (shared set): ['Thường xuất huyết nhẹ', 'Thường nôn máu đỏ thẫm, máu cục, đi cầu phân đen', 'Thường theo gan lách to và tuần hoàn bang hệ', 'Thường đau bụng từng cơn và đi cầu phân đen']
  line   1833 | Medium      | id deacd59dd1994c769e43bd505b55a6fe | C -> Thường theo gan lách to và tuần hoàn bang hệ
  line   1966 | Medium      | id 207ebd77d07846acb0ea2a329d4a7d56 | C -> *Thường theo gan lách to và tuần hoàn bang hệ
  line   1988 | Medium      | id 752419d0fc8f41c5bc043aa5a3426caf | C -> Thường theo gan lách to và tuần hoàn bang hệ

### Group 302 — topic: Pediatrics, Gastroenterology
Q: Bé trai 2 tháng tuổi vào viện vì nôn ói và đau bụng, bé đau bụng dữ dội, từng cơn khoảng 5 phút và tiêu phân nhầy máu mũi, không sốt, chẩn đoán phù hợp nhất là gì?
Options (shared set): ['Lồng ruột', 'Lỵ trực khuẩn', 'Lỵ amip', 'Scholein Henoch']
  line   1834 | Challenging | id 266aa630d94f4922ab261e4c7cc09ae6 | A -> Lồng ruột
  line   1967 | Challenging | id ce1dc36bf8d74bb79544383343f5d592 | A -> *Lồng ruột

### Group 303 — topic: Pediatrics, Gastroenterology, Infectious Diseases
Q: Bệnh nhi nam 6 tuổi vào viện vì nôn ói và đau bụng vùng thượng vị. Nội soi: Phù sung huyết niêm mạc dạ dày, loét hành tá tràng, mô học dương tính và clotest dương tính với Hp, điều trị phù hợp nhất là gì?
Options (shared set): ['Ức chế bơm proton + Amoxicillin + Metronidaziol liều chuẩn', 'Ức chế bơm proton + amoxicillin + clarimycin + bismusth', 'Ức chế bơm proton + Amoxicillin + clarimycin + metronidazole liều chuẩn', 'Ức chế bơm proton + clarimycin + metronidazole']
  line   1836 | Challenging | id 384699efce0e462c81337403c2e4c255 | C -> Ức chế bơm proton + Amoxicillin + clarimycin + metronidazole liều chuẩn
  line  11709 | Challenging | id d118a43acbaf418e90ad23cf72daa720 | C -> Ức chế bơm proton + Amoxicillin + clarimycin + metronidazole liều chuẩn

### Group 304 — topic: Gastroenterology, Pediatrics
Q: Bệnh nhi nam, 6 tuổi, vào viện vì nôn ói và đau bụng. Bệnh 3 ngày với triệu chứng đau bụng từng cơn, buồn nôn, ngày nay cháu đau bụng nhiều, nôn 2 lần nên xin nhập viện. Vào viện: tỉnh, môi hồng, mạch rõ, chi ấm, nôn ra thức ăn lẫn máu đỏ tươi, van đau bụng vùng thượng vị, bụng mềm, ấn đau thượng vị và hạ sườn trái, chưa đi cầu, cơ quan khác chưa phát hiện bệnh lý. Tiền căn: thường xuyên đau bụng sau ăn hơn 3 tháng nay, thỉnh thoảng đi cầu phân đen lỏng. Chẩn đoán phù hợp nhất ở bệnh nhi này là?
Options (shared set): ['XHTH trên nghi do VLDDTT', 'XHTH trên nghi do vỡ giãn tĩnh mạch thực quản', 'XHTH trên nghi do HC Malory Wess', 'XHTH trên nghi do SXH Dengue']
  line   1838 | Challenging | id b5012315e0394f80a6fc34b6cc1d1c3d | A -> XHTH trên nghi do VLDDTT
  line   1983 | Challenging | id 65a7b3f7d67f4388b73aa4a889c32aa0 | A -> XHTH trên nghi do VLDDTT

### Group 305 — topic: Gastroenterology, Endocrinology, Internal Medicine
Q: Trong suy gan, bệnh nhân có thể phù do:
Options (shared set): ['Giảm Pkeo, rối loạn chuyển hóa glucid', 'Giảm Pkeo, tăng aceton máu', 'Giảm Pkeo, giảm khả năng chuyển hóa hormon steroid', 'Giảm Pkeo gây ảnh hưởng đến quá trình đào thải muối, nước ở ống thận']
  line   1839 | Challenging | id cdb23d0145e94d1db5a9953c0fb10915 | C -> Giảm Pkeo, giảm khả năng chuyển hóa hormon steroid
  line   6161 | Medium      | id 5f8ac6803f5a4b379083f35551292919 | C -> Giảm Pkeo, giảm khả năng chuyển hóa hormon steroid

### Group 306 — topic: Endocrinology, Gastroenterology
Q: Những coenzym nào sau đây tham gia vào quá trình tổng hợp acid béo:
Options (shared set): ['Glutathion dạng khử và dạng oxy hoá', 'NAD, NADHH', 'FAD, FADH2', 'NADP, NADPHH']
  line   1842 | Medium      | id 4c117b2903cf4819b63e273ec8cc1197 | D -> NADP, NADPHH
  line   1911 | Medium      | id 0d317fd6de0249c2a44dddd41a04f908 | C -> NADP, NADPHH+
  line   6967 | Medium      | id 21426027fe874dfda35a7ce0c59e8b6e | D -> NADP, NADPHH
  line   7012 | Medium      | id bf8fe199193f491dabb40718b9dd4f44 | C -> NADP, NADPHH+

### Group 307 — topic: Endocrinology, Gastroenterology
Q: Đây là sản phẩm thuộc chu trình pentoé, phản ứng này có tên enzym và sản phẩm tạo thành là gì? (2) Sed.7P + PGA ---->
Options (shared set): ['Transaldolase, F6P + PGA', 'Transcetolase, F6P + Ery.4P', 'Transaldolase, F6P + Ery.4P', 'Transcetolase, F6P + PGA']
  line   1843 | Medium      | id 2f83e6449d4844bf96e6a1a2c3edd5a0 | B -> Transcetolase, F6P + Ery.4P
  line   6968 | Medium      | id 6bbac87942114de489f7f35b24da52f8 | B -> Transcetolase, F6P + Ery.4P

### Group 308 — topic: Endocrinology, Gastroenterology
Q: Trong thoái hoá hiếu khí acid pyruvic dẫn tới acetylCoA, các coenzym tham gia theo thứ tự lần lượt là:
Options (shared set): ['TPP, HSCoA, NAD, FAD', 'TPP, Acid lipoic, HSCoA, NAD, NAD', 'TPP, Acid lipoic, HSCoA, FAD, NAD', 'TPP, HSCoA, Acid lipoic, FAD, NAD']
  line   1844 | Medium      | id f4223bc9ceb945bdb6331154f0be967a | C -> TPP, Acid lipoic, HSCoA, FAD, NAD
  line   6969 | Medium      | id 0d74d60dbade4e97baeb5c8404f25e38 | C -> TPP, Acid lipoic, HSCoA, FAD, NAD

### Group 309 — topic: Endocrinology, Gastroenterology
Q: Khi Glucose máu tăng cao, cơ thể điều hoà bằng cách: 1. Tăng tổng hợp enzym glucose-6-phosphatase 2. Giảm tổng hợp enzym glucose-6-phosphatase 3. Tăng tổng hợp enzym glucose styetase 4. Giảm tổng hợp enzym glucose styetase 5. Tăng tân tạo đường Hãy chọn tập hợp đúng
Options (shared set): ['2,4', '2,3', '4,5', '1,2']
  line   1845 | Medium      | id 70b9174be1ee458597700b1e783a43b7 | B -> 2,3
  line   6970 | Medium      | id 4f0c1a100f7a438aaeb1096542b98a74 | B -> 2,3

### Group 310 — topic: Gastroenterology, Endocrinology
Q: GPT xúc tác phản ứng nào sau đây?
Options (shared set): ['Alanin + Oxaloacetat Pyruvat + Aspartat', 'Glutamat + Phenylpyruvat Oxaloacetat + Phenylalanin', 'Alanin + α-cetoglutarat Pyruvat + Glutamat', 'Alanin + α-cetoglutarat Oxaloacetat + Glutamat']
  line   1846 | Medium      | id bdf2397521794d31b13dacd801ae6876 | C -> Alanin + α-cetoglutarat Pyruvat + Glutamat
  line   1930 | Medium      | id 8494df8a891743c8a323431cac8ea8e5 | A -> Alanin + α-cetoglutarat ↔ Pyruvat + Glutamat
  line   6971 | Medium      | id a0f6f8e87bd3495ab0737a9aca970e03 | C -> Alanin + α-cetoglutarat Pyruvat + Glutamat

### Group 311 — topic: Endocrinology, Gastroenterology
Q: Chọn câu đúng:
Options (shared set): ['SusuccinylCoA tham gia vào quá trình tạo globin', 'Chu trình Krebs liên quan với chu trình Ure qua Citrulin', 'Oxaloacetat của thoái hoá glucid kéo theo acetylCoA của β-Oxy hoá acid béo vào chu trình Krebs', 'Con đường đường phân cung cấp Ribose-5P và NADHH+']
  line   1847 | Medium      | id 5b9aeecdcab747e5b97488c453da1631 | C -> Oxaloacetat của thoái hoá glucid kéo theo acetylCoA của β-Oxy hoá acid béo vào chu trình Krebs
  line   6972 | Medium      | id 02bab40e5b2948788224589f87f63e7a | C -> Oxaloacetat của thoái hoá glucid kéo theo acetylCoA của β-Oxy hoá acid béo vào chu trình Krebs

### Group 312 — topic: Endocrinology, Gastroenterology
Q: Trong chuỗi phản ứng dưới đây: Glucose Glucose-6-P ? Glycogen
Options (shared set): ['Fructose-1,6-P', 'Fructose-6P', 'Fructose-1P', 'Glucose-1P']
  line   1848 | Medium      | id ae73050a82404dfc88cf47acbbf1a749 | D -> Glucose-1P
  line   6973 | Medium      | id 978092e989974a3394d77ba9f6e7295b | D -> Glucose-1P

### Group 313 — topic: Endocrinology, Gastroenterology
Q: Nói về chu trình Krebs: 1. Từ Citrat Isocitrat được xúc tác bởi enzym có tên là Citrat-Isomerase 2. Từ Citrat Isocitrat là phản ứng trực tiếp 3. Từ Oxalosuccinat α-cetoglutarat là phản ứng loại CO2 4. Từ SuccinylCoA Succinat là phản ứng tạo ATP thông qua GTP 5. Enzym xúc tác từ Fumarat Malat có tên Fumarase Hãy chọn tập hợp đúng:
Options (shared set): ['1, 2, 2003', '2, 3, 2004', '3, 4, 2005', '2, 3, 2005']
  line   1849 | Challenging | id a6bbed78566749ae8e11be644cb55404 | C -> 3, 4, 2005
  line   6974 | Medium      | id cfbaa386945444e185884c469ec21c64 | C -> 3, 4, 2005

### Group 314 — topic: Endocrinology, Gastroenterology
Q: Peptid nào sau đây đóng vai trò quan trọng trong điều hoà đường huyết?
Options (shared set): ['Insulin và glutathion', 'Insulin và Glucagon', 'Glutathion và glucagon', 'Insulin và Vasopresin']
  line   1850 | Medium      | id 1a8eaf81745843529e838bfe2df39982 | B -> Insulin và Glucagon
  line   6975 | Medium      | id 2dd93f5a10814e69bf9f48aa74d15783 | B -> Insulin và Glucagon
  line   7060 | Medium      | id c649e82f032d4c6cafd233ad7f50b046 | B -> Insulin và glucagon

### Group 315 — topic: Endocrinology, Gastroenterology
Q: Nhóm cơ chất nào sau đây có thể được cơ sử dụng để tổng hợp glucose
Options (shared set): ['Acid palmitic, acid aspartic, glycerol', 'Lactat, acid palmitic, acid stearic', 'Glycin, glycerol, mannose', 'AcetylCoA, glycerol, frutose']
  line   1852 | Medium      | id 55b9d99aad8547f1924bfd93fcb1eb15 | C -> Glycin, glycerol, mannose
  line   6976 | Medium      | id 7ecc2f84cf2a46c58dee83c2aaa48992 | A -> Acid palmitic, acid aspartic, glycerol

### Group 316 — topic: Endocrinology, Gastroenterology
Q: Tập hợp các chất nào dưới đây tham gia vào quá trình tổng hợp mạch thẳng của glycogen
Options (shared set): ['ATP, G6P, glycogen syntetase', 'Glycogensyntetase, phosphorylase, G1P', 'Chuỗi polysaccasid mồi, glycogensyntetase, phosphatase', 'Tất cả các gợi ý đều sai']
  line   1853 | Challenging | id b05a12737a7e4b4587074c7e382c3e27 | D -> Tất cả các gợi ý đều sai
  line   6169 | Medium      | id 4bf9507aa78749baa6c582a2206a218a | D -> Tất cả các gợi ý đều sai

### Group 317 — topic: Endocrinology, Gastroenterology
Q: Nguyên liệu để tổng hợp glycogen là:
Options (shared set): ['Glucose dưới dạng UDP-G', 'Glucose dưới dạng G6P', 'Glucose dưới dạng tự do', 'Glucose dưới dạng G1P']
  line   1854 | Easy        | id f39860007f5245828140a02ba145f75a | A -> Glucose dưới dạng UDP-G
  line   6349 | Easy        | id 226b0e5d70df42d290e9f78e6b96be18 | D -> Glucose dưới dạng G1P

### Group 318 — topic: Nephrology, Gastroenterology
Q: Trong chu trình ure, acid aspartic đóng vai trò là chất
Options (shared set): ['Trung gian vận chuyển nhóm amin', 'Trung gian vận chuyển năng lượng', 'Trung gian vận chuyển nhóm carbocyl', 'Trung gian vận chuyển nhóm metyl']
  line   1855 | Medium      | id 3abf48458e914d98a8871a540b358679 | A -> Trung gian vận chuyển nhóm amin
  line   1928 | Medium      | id 3db362f3ea58443983de15925188e633 | B -> Trung gian vận chuyển nhóm amin

### Group 319 — topic: Gastroenterology, Infectious Diseases
Q: Chẩn đoán và điều trị viêm phúc mạc nhiễm khuẩn tự phát: chọn câu đúng?
Options (shared set): ['Chọc dịch báng xét nghiệm trước khi điều trị kháng sinh ở tất cả các bệnh nhân nghi ngờ viêm phúc mạc nhiễm khuẩn tự phát', 'Chờ kết quả kháng sinh đồ và lựa chọn kháng sinh điều trị', 'Tránh điều trị kháng sinh theo kinh nghiệm để phòng đề kháng thuốc', 'Đánh giá điều trị sau 72 giờ: gọi là thất bại nếu triệu – chứng lâm sàng không giảm hoặc nặng hơn']
  line   1864 | Challenging | id cc728024454f4d98b5aa2bd7516089c3 | A -> Chọc dịch báng xét nghiệm trước khi điều trị kháng sinh ở tất cả các bệnh nhân nghi ngờ viêm phúc mạc nhiễm khuẩn tự phát
  line   1971 | Challenging | id e95d2ec2338747a19880da0376466e58 | A -> Chọc dịch báng xét nghiệm trước khi điều trị kháng sinh ở tất cả các bệnh nhân nghi ngờ viêm phúc mạc nhiễm khuẩn tự phát

### Group 320 — topic: Gastroenterology, Nephrology
Q: Hội chứng PPCD: post-paracentesis circulatory dysfunction biểu hiện?
Options (shared set): ['Suy thận', 'Tăng natri máu', 'Tăng kali máu', 'Xuất huyết tiêu hóa']
  line   1865 | Medium      | id 6d084a2375084261bf832ad1c1dae68b | A -> Suy thận
  line   1972 | Medium      | id 971f23cda14c4bcea797ba9ceac26e1e | A -> Suy thận

### Group 321 — topic: Gastroenterology
Q: Chuột rút ở bệnh nhân xơ gan: chọn câu đúng?
Options (shared set): ['Điều trị bằng lợi tiểu', 'Điều trị bằng albumin', 'Điều trị bằng chế độ ăn', 'Điều trị bằng baclofen 50mg/ngày']
  line   1866 | Challenging | id 5fbaa9faef314bdab71e6c831183f6dd | B -> Điều trị bằng albumin
  line   1869 | Challenging | id ad1ca8d8d1934b859ad4f73ebf1943d5 | B -> Điều trị bằng albumin

### Group 322 — topic: Gastroenterology, Nephrology
Q: Các yếu tố cần điều chỉnh trước khi dùng thuốc lợi tiểu cho bệnh nhân báng bụng?
Options (shared set): ['Xuất huyết tiêu hóa, Suy thận, hạ Natri máu, tăng kali máu', 'Hội chứng gan phổi, suy thận, bệnh não gan, hạ natri máu', 'Bệnh thận mạn, xuất huyết tiêu hóa, bệnh não gan, Tăng kali máu', 'Suy thượng thận, Suy gan cấp, hạ kali máu, hạ Natri máu']
  line   1867 | Challenging | id a901313791504a2080ae6d83c04d301d | A -> Xuất huyết tiêu hóa, Suy thận, hạ Natri máu, tăng kali máu
  line   1973 | Challenging | id c79a93a3206347278afd9ac34316b4ad | A -> Xuất huyết tiêu hóa, Suy thận, hạ Natri máu, tăng kali máu

### Group 323 — topic: Gastroenterology
Q: Các yếu tố cần điều chỉnh trước khi dùng thuốc lợi tiểu cho bệnh nhân báng bụng?
Options (shared set): ['XHTH, suy thận, hạ Natri máu, tăng Kali máu', 'HC gan phổi, suy thận, bệnh não gan, hạ Natri máu', 'Bệnh thận mạn, XHTH, bệnh não gan, tăng Kali máu', 'Suy thượng thận, suy gan cấp, hạ Kali máu, hạ Natri máu']
  line   1868 | Challenging | id 913ac033f6524302bc271a8b1a36e48c | A -> XHTH, suy thận, hạ Natri máu, tăng Kali máu
  line   1872 | Challenging | id 204abc719f754dafafcfa3064d3c0e1b | A -> XHTH, suy thận, hạ Natri máu, tăng Kali máu

### Group 324 — topic: Endocrinology, Gastroenterology
Q: Thoái hóa glucose theo con đường hexosemonophosphat (HMP) xảy ra mạnh ở các tổ chức như:
Options (shared set): ['Mô mỡ, tế bào niêm mạc ruột non, gan', 'Mô cơ, tế bào ống thận, gan', 'Tế bào ống thận, tổ chức gan, tim', 'Mô cơ, tổ chức thần kinh, thận']
  line   1899 | Medium      | id a2eda079ec0743989b5bbad2ff23be22 | A -> Mô mỡ, tế bào niêm mạc ruột non, gan
  line   7003 | Medium      | id 71fd213c679f4b3186ffe6eb0b703365 | A -> Mô mỡ, tế bào niêm mạc ruột non, gan

### Group 325 — topic: Gastroenterology, Endocrinology
Q: Mục đích quan trọng nhất của glycogenlysis ở gan là:
Options (shared set): ['Cung cấp ATP cho tổ chức gan hoạt động', 'Cung cấp glucose tự do, là nguyên liệu cần thiết cho sự hoạt động của gan', 'Cung cấp glucose, là tiền nguyên liệu cần thiết tổng hợp acid glucuronic tham gia vào quá trình khử độc tại gan', 'Cung cấp glucose tự do cho máu, từ đó phân phối tổ chức.']
  line   1900 | Medium      | id ec847f93a3294d65bc25943261c11762 | D -> Cung cấp glucose tự do cho máu, từ đó phân phối tổ chức.
  line   7004 | Medium      | id ca7de04bb56848c6ba107fbc7530059f | D -> Cung cấp glucose tự do cho máu, từ đó phân phối tổ chức.

### Group 326 — topic: Endocrinology, Gastroenterology
Q: Số phận của acetylCoA có nguồn gốc từ thoái hóa acid béo có thể là gì? (Chọn câu trả lời đúng nhất)
Options (shared set): ['Tạo cetonic để gan trực tiếp sử dụng', 'Theo chu trình Krebs hoặc tạo tiền chất của Hb', 'Tổng hợp glucid, lipid, acid béo, acid nucleic', 'Thoái hóa đến cùng tạo CO2 + H2O, tạo thể cetonic, tổng hợp acid béo, tổng hợp cholesterol và một số chất khác']
  line   1903 | Medium      | id bed48709695e45188ed37e5230bab657 | D -> Thoái hóa đến cùng tạo CO2 + H2O, tạo thể cetonic, tổng hợp acid béo, tổng hợp cholesterol và một số chất khác
  line   7005 | Medium      | id 4fa3ad99596f4e77a4c22d161b0055f1 | D -> Thoái hóa đến cùng tạo CO2 + H2O, tạo thể cetonic, tổng hợp acid béo, tổng hợp cholesterol và một số chất khác

### Group 327 — topic: Endocrinology, Gastroenterology
Q: Thoái hóa 1 phân tử acid palmitic thành các mẫu 2 carbon cần bao nhiêu HSCoA?
Options (shared set): ['5', '8', '7', '10']
  line   1904 | Medium      | id 5d6fffd4889c45dea446dd1df9c30af7 | B -> 8
  line   7006 | Medium      | id 79f9559d03294c20bbac68a9f49ff551 | B -> 8

### Group 328 — topic: Endocrinology, Gastroenterology
Q: Thoái hóa acid béo bão hòa có số C lẻ khác với số C chẵn ở điểm nào?
Options (shared set): ['Tạo acetylCoA', 'Tạo hợp chất trung gian là crotonyl', 'Tạo propionylCoA', 'Có sự tham gia của enzym enoyl hydratase']
  line   1905 | Medium      | id 8b1538bf2a384474914d29f64c49d06a | C -> Tạo propionylCoA
  line   7007 | Medium      | id e7a0174b108c420886e7bb18f2dab5f8 | C -> Tạo propionylCoA

### Group 329 — topic: Endocrinology, Gastroenterology
Q: Trong tổng hợp acid béo, Coenzym cung cấp hydro là gì?
Options (shared set): ['NADHH+', 'FADH2', 'NADHH+ và FADH2', 'NADPHH+']
  line   1906 | Easy        | id c9cc2380f1bf4eb8856fced855672714 | D -> NADPHH+
  line   6356 | Easy        | id 8ec2b365f4cb467f977ed461741cc2a1 | D -> NADPHH+

### Group 330 — topic: Endocrinology, Gastroenterology
Q: Nguồn cung cấp NADPHH+ cho tổng hợp acid béo là từ đâu?
Options (shared set): ['Con đường đường phân', 'Con đường hexosemonophosphat', 'Chu trình Krebs', 'Phản ứng khử carbocyl oxy hóa isocitrat']
  line   1907 | Medium      | id 4c003e269fd04c548ba4ed72aeaefd84 | B -> Con đường hexosemonophosphat
  line   7008 | Medium      | id 590f5f135e6c41f286c477ed5251b7d2 | B -> Con đường hexosemonophosphat

### Group 331 — topic: Endocrinology, Gastroenterology
Q: Chất nào sau đây là chất trung gian quan trọng trong quá trình tổng hợp triglycerid và phospholipid?
Options (shared set): ['Diglycerid', 'Glycerol', 'Glycerophosphat', 'Acid phosphatidic']
  line   1908 | Medium      | id 9506d68b1397453ba9a35b9f5cc5a9cf | D -> Acid phosphatidic
  line   7009 | Medium      | id 5df77f1baf8e42b2ae98da363d041f20 | D -> Acid phosphatidic

### Group 332 — topic: Endocrinology, Gastroenterology
Q: Adenosin-methionin tham gia vào quá trình tổng hợp chất nào?
Options (shared set): ['Sphingomelin', 'Lecithin', 'Cephalin', 'Phosphatidylserin']
  line   1909 | Medium      | id 54e97cd9e55044e092c7da2d3f2d5e81 | B -> Lecithin
  line   7010 | Medium      | id 896f5de4480e4a4ea08e82e5d828d9e2 | B -> Lecithin

### Group 333 — topic: Endocrinology, Gastroenterology
Q: Chất nào sau đây không liên quan đến sản phẩm chuyển hóa của cholesterol?
Options (shared set): ['Vitamin D', 'Hormon vỏ thượng thận', 'Sắc tố mật', 'Muối mật, acid mật']
  line   1910 | Medium      | id 9a55f4bb93ca42c4b938cff1a33a288f | C -> Sắc tố mật
  line   7011 | Medium      | id 0662f50f2ab447f7bf457fc10b44eb08 | C -> Sắc tố mật

### Group 334 — topic: Endocrinology, Gastroenterology
Q: Những coenzym nào sau đây tham gia vào quá trình oxy hóa acid béo bão hòa theo trình tự các phản ứng:
Options (shared set): ['NAD, FAD', 'FAD, NAD', 'NADP, FAD', 'FAD, NADP']
  line   1912 | Medium      | id e4aa38e0cf5245579a84bc9aece0d43c | B -> FAD, NAD
  line   7013 | Medium      | id 499f3210a2c44315972783ab22ee1be4 | B -> FAD, NAD

### Group 335 — topic: Endocrinology, Gastroenterology
Q: Sản phẩm thủy phân của lecithin gồm:
Options (shared set): ['3RCOOH, glycrophosphat, cholin', '2RCOOH, glycerol, cholin', '2RCOOH, glycerophosphat, cholamin', '2RCOOH, glycerophosphat, cholin']
  line   1913 | Medium      | id e3d5fd5ad1dc46cda18069c0cb95454c | D -> 2RCOOH, glycerophosphat, cholin
  line   7014 | Medium      | id 33c9bb3e9d3b49f8bbd9b74e84263087 | D -> 2RCOOH, glycerophosphat, cholin

### Group 336 — topic: Endocrinology, Gastroenterology
Q: Về tổng hợp triglycerid. Hãy chọn câu đúng:
Options (shared set): ['Nguyên liệu tổng hợp là glycerol và các acid béo tự do', 'Có enzym glycerophosphatase tham gia', 'Có enzym diglycerid acyl transferase tham gia', 'Không thông qua hợp chất trung gian là acid phosphatidic trong quá trình tổng hợp']
  line   1914 | Medium      | id ce3f2736990345baaae34e5a7e5dd64e | C -> Có enzym diglycerid acyl transferase tham gia
  line   7015 | Medium      | id 2b8acffed6fb4e7fb9f517f9cfa58725 | C -> Có enzym diglycerid acyl transferase tham gia

### Group 337 — topic: Endocrinology, Gastroenterology
Q: Aceto acetylCoA được tạo thành từ:
Options (shared set): ['AcetylCoA + acid acetic', '2.AcetylCoA', '2.AcetylCoA loại HSCoA', 'AcetylCoA + butirylCoA loại HSCoA']
  line   1915 | Medium      | id 91ac8c98a5d041b6a2ed9daab671ab02 | C -> 2.AcetylCoA loại HSCoA
  line   7016 | Medium      | id ec5dcb53ec4c40f08cda626cb44e5d69 | C -> 2.AcetylCoA loại HSCoA

### Group 338 — topic: Endocrinology, Gastroenterology
Q: Chọn câu đúng:
Options (shared set): ['Tổng hợp acid béo ngoài tương bào không cần sự tham gia của phức hợp acid béo syntetase', 'Tổng hợp acid béo trong ty thể là sự ngưng tụ dần với malonylCoA', 'Ngoài bào tương không có khả năng tổng hợp acid béo mạch carbon dài', 'Nguyên liệu của tổng hợp acid béo trong ty thể được chuyển từ ngoài bào tương vào, đa phần chúng là sản phẩm thoái hóa của glucid']
  line   1916 | Medium      | id 07937883fd084d5e8d8fff6a5f5cf6c9 | C -> Ngoài bào tương không có khả năng tổng hợp acid béo mạch carbon dài
  line   7017 | Medium      | id 381eee9631234270b3ca86e990382b6b | C -> Ngoài bào tương không có khả năng tổng hợp acid béo mạch carbon dài

### Group 339 — topic: Endocrinology, Gastroenterology
Q: Một chất vận chuyển trung gian có ở màng ty thể ở quán trình thoái hóa β -oxy hóa:
Options (shared set): ['AcylCoA', 'Carnitin', 'Acylcarnitin', 'AcetylCoA']
  line   1917 | Medium      | id 524a7e3df22a407a93da233db3162a65 | B -> Carnitin
  line   7018 | Medium      | id 0a80a429955b4ec4b326095216ff7dd2 | B -> Carnitin

### Group 340 — topic: Endocrinology, Gastroenterology
Q: Trong quá trình thoái hóa β-oxy hóa, hoạt hóa acid béo→AcylCoA(bào tương) cần mấy ATP:
Options (shared set): ['1 ATP', '2 ATP', '3 ATP', '4 ATP']
  line   1918 | Medium      | id e63bb8e9d2994871bec8bdace047f7e0 | B -> 2 ATP
  line   7019 | Medium      | id 8d70e2fd38b84639880a50c689d9c4f4 | B -> 2 ATP

### Group 341 — topic: Endocrinology, Gastroenterology
Q: Enzym xúc tác quá trình vận chuyển acylCoA từ bào tương vào trong ty thể là gì?
Options (shared set): ['Cartinin transferase', 'Acylcartinin transferase', 'Carnitin Transferase', 'Acylcarnitin transferase']
  line   1919 | Medium      | id c7775533df2b4f73be8a459952e385e4 | D -> Acylcarnitin transferase
  line   7020 | Medium      | id 11e13cb0730b4d448028ffff0a48519a | D -> Acylcarnitin transferase

### Group 342 — topic: Endocrinology, Gastroenterology
Q: Sự thoái hóa acid béo bão hòa có số carbon lẻ, sản phẩm cuối sẽ là gì?
Options (shared set): ['AcetylCoA', 'AcylCoA', 'PropionylCoA', 'PronylCoA']
  line   1920 | Medium      | id cb4326c6ac0e4bf5b7279c3c802f5b0b | C -> PropionylCoA
  line   7021 | Medium      | id c1549ea7e7ef48c08ab233d60ce9ed8b | C -> PropionylCoA

### Group 343 — topic: Endocrinology, Gastroenterology
Q: AcetylCoA có nguồn gốc của hoái hóa acid béo, có thể chuyển hóa theo mấy con đường?
Options (shared set): ['1', '2', '3', '4']
  line   1921 | Medium      | id b3139ba7994b4995b8571f0fe47497b4 | C -> 3
  line   7022 | Medium      | id 52f8a37a887b44889002bc172af00995 | C -> 3

### Group 344 — topic: Endocrinology, Gastroenterology, Nephrology
Q: Trong trường hợp rối loạn chuyển hóa, các chất cetonic tăng cao trong máu và xuất hiện nước tiểu làm nước tiểu có?
Options (shared set): ['Hồng cầu', 'Sắc tố mật dương tính', 'Albumin niệu tăng', 'Protein']
  line   1922 | Challenging | id b0e48ac276a74892ab682f015636fb47 | D -> Protein
  line   6174 | Medium      | id 3034aa58bc5d4fd283c36a94abc7cb77 | B -> Sắc tố mật dương tính

### Group 345 — topic: Endocrinology, Gastroenterology
Q: Ngoài bào tương và ty thể, acid béo còn có thể tổng hợp ở đâu?
Options (shared set): ['Lysosome', 'Microsom', 'Dexsosome', 'Cả 3 đều sai']
  line   1923 | Medium      | id b302fd4029c842b3905e9f188d9d1d44 | B -> Microsom
  line   7023 | Medium      | id 56ed2632c3924b96bbc7f9c867f7e5c4 | B -> Microsom

### Group 346 — topic: Endocrinology, Gastroenterology
Q: Tổng hợp acid béo ngoài bào tương có sự tham gia của phức hợp multienzym mà chất hoạt hóa là?
Options (shared set): ['PDA', 'ACP', 'ATP', 'NAD']
  line   1924 | Medium      | id 8ca4bada015f4be5b7e59820be0d7af7 | B -> ACP
  line   7024 | Medium      | id 8ff8850b756e470cbfcf1ffcba3bd884 | B -> ACP

### Group 347 — topic: Endocrinology, Gastroenterology
Q: Chọn tổ hợp đúng. 1. Tổng hợp acid béo ngoài bào tương chỉ tổng hợp được những aicd béo mạch ngắn. 2. Nguyên liệu tổng hợp acid béo ngoài bào tương là acetylCoA có nguồn gốc tại chỗ 3. Tổng hợp acid béo trong ty thể chất hoạt hóa là HSCoA, không cần có sự tham gia của phức hợp acid béo syntetase 4. Ngoài bào tương phải tạo malonylCoA
Options (shared set): ['1,2,3', '2,3,4', '1,2,4', '1,3,4']
  line   1925 | Challenging | id 23779a51e431493e80cc6c74fb3f1a4b | B -> 2,3,4
  line   6175 | Medium      | id c77f151506d141238f7c99c218521a74 | D -> 1,3,4

### Group 348 — topic: Endocrinology, Gastroenterology
Q: Nhóm chất nào sau đây có cấu trúc gồm các gốc αD-glucose liên kết với nhau bằng liên kết α-1,4-glucosid và α-1,6- glucosid
Options (shared set): ['Amylose, glycogen, dextran', 'Amylopeptin, cellulose, dextrin', 'Cellulose, glycogen, tinh bột', 'Amylopeptin, glycogen, dextrin']
  line   1940 | Medium      | id c82a532866924e168355507ca57b50fc | D -> Amylopeptin, glycogen, dextrin
  line   7028 | Medium      | id d6c7c0deceb24f6782d814bf1337c368 | D -> Amylopeptin, glycogen, dextrin

### Group 349 — topic: Endocrinology, Gastroenterology
Q: Đường nào sau đây thuộc polysaccarid thuần, trong cấu trúc chỉ gồm các glucose?
Options (shared set): ['Tinh bột, glycogen, hyaluronic', 'Glycogen, maltose, fructose', 'Tinh bột, glycogen, dextran', 'Maltose, saccarose, lactose']
  line   1941 | Medium      | id 78d501b6c3cd4f6db3e1d7326862bb25 | C -> Tinh bột, glycogen, dextran
  line   7030 | Medium      | id e36276fc29c84c84b6edde4067d712ad | C -> Tinh bột, glycogen, dextran

### Group 350 — topic: Endocrinology, Gastroenterology
Q: Nhóm nào sau đây gồm những pentose
Options (shared set): ['Sacarose, ribose, deoxyribose', 'Fructose, ribose, deoxyribose', 'Fructose, maltose, ribose', 'Ribose, deoxyribose, xylulose']
  line   1942 | Medium      | id 1a9d97469f07461cb74af89f4f79d73d | D -> Ribose, deoxyribose, xylulose
  line   7031 | Medium      | id 11b36341d78b4f41ab3151e7282d70a9 | D -> Ribose, deoxyribose, xylulose

### Group 351 — topic: Endocrinology, Gastroenterology
Q: Các dạng glucid cơ bản trong cơ thể?
Options (shared set): ['Dự trữ, điều hòa, vận chuyển', 'Dự trữ, vận chuyển, tham gia cấu tạo chất', 'Vận chuyển, điều hòa, tham gia cấu tạo chất', 'Vận chuyển, chuyển đổi, dự trữ']
  line   1943 | Easy        | id 295651e3e6a7402c833383cc9ffdfa38 | B -> Dự trữ, vận chuyển, tham gia cấu tạo chất
  line   7032 | Medium      | id d754d5c915de45c98469468ab87efd66 | B -> Dự trữ, vận chuyển, tham gia cấu tạo chất

### Group 352 — topic: Endocrinology, Gastroenterology
Q: Nhóm cơ chất nào sau đây có thể được sử dụng để tổng hợp glucose?
Options (shared set): ['Acid palmitic, acid aspartic, glycerol', 'Lactat, acid palmitic, acid stearic', 'Glycin, glycertol, mannose', 'Acetyl CoA, glycerol, frutose']
  line   1944 | Challenging | id 5fd1e29e4fd348fa825f6bd40994ddd3 | C -> Glycin, glycertol, mannose
  line   6176 | Easy        | id b618386cbdc2482799c7a2537341474c | A -> Acid palmitic, acid aspartic, glycerol

### Group 353 — topic: Endocrinology, Gastroenterology
Q: Đường nào sau đây tham gia cấu tạo acid nucleic?
Options (shared set): ['Ribose và deoxyribose', 'Glucose và deoxyribose', 'Ribose và fructose', 'Glucose và fructose']
  line   1945 | Easy        | id 7a43c59fa9bd42a9b10fa51f4ea58d27 | A -> Ribose và deoxyribose
  line   6359 | Easy        | id c2973c0afb06499492e361b7b23defce | A -> Ribose và deoxyribose

### Group 354 — topic: Endocrinology, Gastroenterology
Q: Nhóm đường nào sau đây thuộc monosaccarid?
Options (shared set): ['Glucose, fructose, lactose', 'Glucose, maltose, galactose', 'Glucose, maltose, lactose', 'Glucose, fructose, galactose']
  line   1947 | Easy        | id 702e474d5dcc466e8a96a5717e5d92e1 | D -> Glucose, fructose, galactose
  line   6360 | Easy        | id 9cfe8f047705457280917e87f818bad7 | D -> Glucose, fructose, galactose

### Group 355 — topic: Endocrinology, Gastroenterology
Q: : Nhóm đường nào sau đây thuộc disaccarid?
Options (shared set): ['Glucose, fructose, lactose', 'Saccarose, lactose, maltose', 'Maltose, saccarose, glucose', 'Fructose, maltose, lactose']
  line   1948 | Easy        | id d6033813e4b34a7bb56a7d2231bc383d | B -> Saccarose, lactose, maltose
  line   6361 | Easy        | id a026539b29d4416bbfb2ce7a47472d55 | B -> Saccarose, lactose, maltose

### Group 356 — topic: Endocrinology, Gastroenterology
Q: Monosaccarid gặp nhiều nhất trong cơ thể?
Options (shared set): ['Erythose', 'Hexose', 'Pentose', 'Triose']
  line   1949 | Easy        | id 5b490f4b807d404a9dd2cea7455d7849 | B -> Hexose
  line   6363 | Easy        | id 8cd43bc0cbfa454db349934d48e4bb74 | B -> Hexose

### Group 357 — topic: Gastroenterology, Otolaryngology
Q: Trào ngược dạ dày-thực quản không phải là nguyên nhân thuận lợi gây viêm họng mạn tính?
Options (shared set): ['Đúng', 'Sai']
  line   1953 | Medium      | id 36922ba02ec04dc088f01cc58b49e284 | B -> Sai
  line   1958 | Medium      | id fa3f6ba3ba984389bfe8c9b76e15fb74 | B -> Sai

### Group 358 — topic: Pediatrics, Gastroenterology
Q: Chỉ định tiệt trừ Hp ở bệnh nhân VLDDTT có nhiễm Hp là gì?
Options (shared set): ['Sung huyết hang vị', 'Viêm teo dạ dày chuyển sản ruột', 'Tự bịa', 'Tự bịa']
  line   1985 | Medium      | id 49f3635d1ab241a1917027da7ebe537c | B -> Viêm teo dạ dày chuyển sản ruột
  line  10613 | Medium      | id d9a9ff98906e4ad0865d6c1f72a1a9a4 | B -> Viêm teo dạ dày chuyển sản ruột

### Group 359 — topic: Gastroenterology, Pathology, Oncology
Q: Trên hình ảnh mô bệnh học từ mảnh sinh thiết dạ dày của một bệnh nhân có hình ảnh quá sản các tế bào không điển hình, bào tương rộng, chứa chất nhầy, nhân bị lệch về một phía, các tế bào này xâm lấn mô đệm xung quanh. Kết quả phù hợp nhất với tổn thương này là gì?
Options (shared set): ['Ung thư biểu mô dạ dày típ tuyến nhầy', 'Ung thư biểu mô dạ dày típ vảy', 'Ung thư biểu mô dạ dày típ tế bào nhẫn', 'Ung thư biểu mô dạ dày típ kém biệt hóa']
  line   1999 | Challenging | id ec82c1f524db48e3b72f5b425112a002 | C -> Ung thư biểu mô dạ dày típ tế bào nhẫn
  line   8893 | Challenging | id ce291148a9bc4b3093e040d6fd2444b0 | C -> Ung thư biểu mô dạ dày típ tế bào nhẫn

### Group 360 — topic: Hematology, Gastroenterology
Q: Thiếu máu thiếu sắt không gặp trong trường hợp nào sau đây:
Options (shared set): ['Thiếu HCl.', 'Tan máu bẩm sinh.', 'Nhiễm giun móc.', 'Loét dạ dày tá tràng.']
  line   2019 | Medium      | id b02b7d50f3ca4f779752344305287503 | B -> Tan máu bẩm sinh.
  line   2020 | Medium      | id d0957aa7dc3c468581e0e8214f94e152 | B -> Tan máu bẩm sinh.

### Group 361 — topic: Infectious Diseases, Gastroenterology
Q: Bệnh truyền nhiễm đường tiêu hóa là bệnh:
Options (shared set): ['Bại liệt', 'Viêm gan B', 'Viêm gan C', 'Sởi']
  line   2026 | Medium      | id 29fc5bffb300429db00b17be6c543899 | A -> Bại liệt
  line   2035 | Medium      | id b19d78aef0ca404cb3045f8a466273fa | D -> Bại liệt

### Group 362 — topic: Gastroenterology, Pathology
Q: Dưới đây là hình ảnh vi thể của xơ gan. Mũi tên đen chỉ tổn thương gì?
Options (shared set): ['Mạch máu tăng sinh', 'Ống mật tăng sinh', 'Xâm nhiễm viêm mạn tính', 'Tăng sinh tế bào sợi']
  line   2097 | Challenging | id d848f95395014a1084b355e51e258f94 | B -> Ống mật tăng sinh
  line   2098 | Challenging | id 534b8a8b19ab4dc896dcc3f20219ec2c | A -> Mạch máu tăng sinh
  line   2099 | Challenging | id 724d7282fa254bde9957e9c35a747b2d | C -> Xâm nhiễm viêm mạn tính

### Group 363 — topic: Gastroenterology, Pathology
Q: Dưới đây là hình ảnh vi thể của ổ loét dạ dày mạn tính. Lớp được chỉ ra trong hình (mũi tên) là lớp nào?
Options (shared set): ['Hoại tử tơ huyết', 'Phù dạng tơ huyết', 'Tổ chức hạt', 'Tổ chức xơ']
  line   2109 | Challenging | id 511e85d8c3ee4cc08ede89422f28a0ae | A -> Hoại tử tơ huyết
  line   2110 | Challenging | id 180756a0c06544b6a8a0840cfc0ef82f | C -> Tổ chức hạt

### Group 364 — topic: Gastroenterology, Pathology
Q: Giai đoạn đầu của xơ gan kích thước gan thay đổi như thế nào?
Options (shared set): ['Không thay đổi', 'To lên', 'Nhỏ lại', 'Không rõ sự thay đổi']
  line   2129 | Easy        | id bb1fb529c7c5443fbad7347e9b970aad | B -> To lên
  line   8195 | Easy        | id c243dbc8d0e04eef93322e6516a2ccd9 | B -> To lên

### Group 365 — topic: Gastroenterology, Endocrinology
Q: Loét Zollinger – Ellison là loét dạ dày cấp tính do nguyên nhân:
Options (shared set): ['Tăng áp lực nội sọ', 'U tiểu đảo Langerhans tế bào alpha ở tụy', 'Do bỏng diện rộng', 'Do stress']
  line   2165 | Medium      | id f71cfcc943ee414e95f30315d9fce84e | B -> U tiểu đảo Langerhans tế bào alpha ở tụy
  line   7142 | Medium      | id b65c7b8642c94580aa8f334d55805e49 | B -> U tiểu đảo Langerhans tế bào alpha ở tụy

### Group 366 — topic: Gastroenterology, Oncology
Q: Ung thư gan di căn xa đến cơ quan nào là chủ yếu, trừ
Options (shared set): ['Não', 'Thận', 'Phổi', 'Cột sống']
  line   2183 | Medium      | id 60824370219b4e79aa69ea2e6cee3b06 | B -> Thận
  line  10620 | Medium      | id 5aa04020f61c4f21ab1980ac1e4391b2 | B -> Thận

### Group 367 — topic: Gastroenterology, Surgery
Q: Bệnh nhân nam, 45 tuổi, vào viện với lý do chướng bụng, mệt mỏi ăn uống kém. Khám xác định bệnh nhân có gan to, tuần hoàn bàng hệ vùng quanh rốn. Tuần hoàn bàng hệ là do vòn nối của những tĩnh mạch dây trằng tròn (tĩnh mạch gan) với tĩnh mạch nào?
Options (shared set): ['Tĩnh mạch rốn', 'Tĩnh mạch mạc treo tràng trên, dưới', 'Tĩnh mạch thượng vị trên, dưới', 'Tĩnh mạch thắt lưng phải, trái']
  line   2190 | Challenging | id d8db18ff9a274a5dae909a92541adb9b | C -> Tĩnh mạch thượng vị trên, dưới
  line   9652 | Medium      | id acf56857817145e48cb45cda6388cd3a | C -> Tĩnh mạch thượng vị trên, dưới

### Group 368 — topic: Gastroenterology, Endocrinology
Q: Yếu tố cần thiết để glucose thành glycogen trong gan là gì?
Options (shared set): ['Acid lactic', 'UTP', 'Acid pyruvic', 'GTP']
  line   2196 | Medium      | id 0717ede7e5164d91ba846f9947b70684 | B -> UTP
  line   7148 | Medium      | id 4da4198c2fbc45a7a81ce49009a47da7 | B -> UTP

### Group 369 — topic: Gastroenterology, Internal Medicine
Q: Cơ chế gây vàng da tắc mật:
Options (shared set): ['Giảm chức năng gan liên hợp của gan gây ứ đọng bilirubin trực tiếp', 'Tắc mật gây tổn thương tế bào gan làm mất trân vào máu', 'Bilirubin liên hợp không xuống được ruột, ứ lại ở gan, thấm vào máu', 'Bilirubin gián tiếp tăng cao gây vàng da']
  line   2202 | Medium      | id 7d216fa848e048b2b8e94e3a87046d72 | C -> Bilirubin liên hợp không xuống được ruột, ứ lại ở gan, thấm vào máu
  line  10996 | Medium      | id 7fdb09b376cd474f9f870f0f4624f5b1 | C -> Bilirubin liên hợp không xuống được ruột, ứ lại ở gan, thấm vào máu

### Group 370 — topic: Gastroenterology, Internal Medicine
Q: pH tối thích cho enzyme pepsin là:
Options (shared set): ['4,0-5,0', '5,8-6,2', '5,2-6,0', '1,0-2,0']
  line   2203 | Easy        | id ff09a61a979a49c5a18d2d24205a1aef | D -> 1,0-2,0
  line   2214 | Easy        | id 355a78dfcb764523b71bc87c170ea428 | D -> 1,0-2,0

### Group 371 — topic: Oncology, Palliative Medicine, Gastroenterology
Q: Ăn kiêng hoặc nhịn ăn để khối u phát triển châm lại , thậm chí nó sẽ chết đi là quan điểm đúng hay sai ?
Options (shared set): ['Đúng', 'Sai']
  line   2301 | Medium      | id decf8bfbf9594d579d5dc9c682ec3b51 | B -> Sai
  line  10105 | Medium      | id 5eb622c26c2c4c54ae820bc76a6bfea6 | B -> Sai

### Group 372 — topic: Pediatrics, Gastroenterology
Q: Chiều dài thực quản ở trẻ sơ sinh là bao nhiêu?
Options (shared set): ['12 cm', '16 cm', '18 cm', '10-11 cm']
  line   2337 | Easy        | id e7761e52d66247a1a47535e23ba6355d | D -> 10-11 cm
  line  11686 | Easy        | id 3e6f5efe2ed641d6a53cfb2bdcf55240 | D -> 10-11 cm

### Group 373 — topic: Neurology, Pulmonology, Gastroenterology
Q: Hãy cho biết hoạt động của các cơ quan hô hấp , tiêu hóa trong cơ thể chịu sự chi phối của hệ thần kinh nào sau đây ?
Options (shared set): ['hệ thần kinh giao cảm và hệ thần kinh trung ương', 'hệ thần kinh phó giao cảm và hệ thần kinh vận động', 'cả hai hệ thần kinh giao cảm và phó giao cảm', 'hệ thần kinh trung ương và hệ thần kinh phó giao cảm']
  line   2346 | Easy        | id cf42ae143b53442f964317bdbd43621d | C -> cả hai hệ thần kinh giao cảm và phó giao cảm
  line   5992 | Easy        | id 50f5f8b933d5479eba47d31db7cb33df | C -> cả hai hệ thần kinh giao cảm và phó giao cảm

### Group 374 — topic: Gastroenterology, Pathology, Endocrinology
Q: Tế bào tuyến đáy vì chế tiết serotonin:
Options (shared set): ['Tế bào trụ tiết nhảy.', 'Tế bào chính', 'Tế bào ưa bạc', 'Tế bào viên.']
  line   2387 | Medium      | id 4b5a4551d28d40488ccca1c0111f0724 | C -> Tế bào ưa bạc
  line   7172 | Medium      | id 220775262f5c41e99ff8dbabd1400b31 | C -> Tế bào ưa bạc

### Group 375 — topic: Hematology, Gastroenterology
Q: Khi cơ thể thiếu Sắt dẫn đến hiện tượng gì? Thiếu máu, tăng hấp thu Pb từ đường tiêu hóa
Options (shared set): ['Thiếu máu, tăng hấp thu Pb từ đường tiêu hóa', 'Giảm Canxi trong xương do Canxi trong xương được lấy ra để bù lượng Fe thiếu hụt, gây loãng xương', 'Thiếu máu, bệnh vàng da', 'Giảm khả năng tái tạo hồng cầu, bệnh máu trắng']
  line   2404 | Medium      | id a0f062cafa0048149a776ecb7cbf49c4 | A -> Thiếu máu, tăng hấp thu Pb từ đường tiêu hóa
  line  10625 | Medium      | id 133aa2facb3941b188dd300c73c9754f | A -> Thiếu máu, tăng hấp thu Pb từ đường tiêu hóa

### Group 376 — topic: Gastroenterology, Endocrinology
Q: Gan cung cấp glucose cho máu chủ yếu bằng cách?
Options (shared set): ['Thoái hóa glycogen', 'Tân tạo glucose từ protid', 'Tân tạo glucose từ acid béo', 'tạo Glucose từ acid lactic']
  line   2409 | Medium      | id b1868607f2454b099b3f91a806baf38a | A -> Thoái hóa glycogen
  line   7176 | Medium      | id aef11dea1fce42cebcabb12fb06d2434 | A -> Thoái hóa glycogen

### Group 377 — topic: Gastroenterology, Endocrinology
Q: Tăng cholesterol máu sẽ dẫn đến nhiễm mỡ gan.
Options (shared set): ['Đúng', 'Sai']
  line   2416 | Medium      | id 2eb91f5aeef7421d86d0496030e3dfed | A -> Đúng
  line   7179 | Medium      | id 32ecc887b55840bc9dba5271e1aa3eb6 | A -> Đúng

### Group 378 — topic: Pulmonology, Gastroenterology
Q: 10. Tràn dịch màng phổi do viêm tụy ?
Options (shared set): ['Thường bên trái', 'Đau vùng thượng vị lan ra sau lưng', 'Amylase máu và trong dịch màng phổi tăng cao', 'Tất cả đúng@']
  line   2426 | Challenging | id 5b6b11a330ed44caaebbf417a1608bb9 | D -> Tất cả đúng@
  line   6039 | Medium      | id 0546c1db72a043dbabcd91e00818d17e | D -> Tất cả đúng@

### Group 379 — topic: Obstetrics and Gynecology
Q: Cuộc chuyển dạ bình thường của người con dạ là 8-12 giờ. (Đúng/Sai)
Options (shared set): ['Đúng', 'Sai']
  line   2534 | Easy        | id 777600d5353141f1ac1292bd74e8c7ae | A -> Đúng
  line  11898 | Easy        | id b91bafac3c004e67a0360c1ac1ce53ff | A -> Đúng

### Group 380 — topic: Obstetrics and Gynecology
Q: Thời gian chuyển dạ trung bình một cuộc đẻ thường là 15 giờ. (Đúng/Sai)
Options (shared set): ['Đúng', 'Sai']
  line   2535 | Easy        | id ebfe2a01dc3a45139b66184162a893c6 | A -> Đúng
  line   8800 | Easy        | id b954735e8fbf41268b4c2ab53034546b | A -> Đúng

### Group 381 — topic: Obstetrics and Gynecology
Q: Chọn tình huống thường xảy ra nhất: Khi tuổi thai > 38 tuần, thai phụ thấy ra chất nhầy có màu hồng, có thể nghĩ đến:
Options (shared set): ['Dấu hiệu của rau tiền đạo bám thấp.', 'Dấu hiệu của chuyển dạ.', 'Dấu hiệu của rau bong non.', 'Dấu hiệu của thai chết lưu.']
  line   2545 | Easy        | id 8c932a949e4f40ee97bb6edd7f318c24 | B -> Dấu hiệu của chuyển dạ.
  line   7950 | Medium      | id f7f4dd882f2b4eb3ab6b59b00e05c4cd | B -> Dấu hiệu của chuyển dạ.

### Group 382 — topic: Obstetrics and Gynecology
Q: Đầu ối được thành lập vào thời điểm:
Options (shared set): ['Từ tuần thứ 36 của thai kỳ.', 'Từ tuần thứ 38 của thai kỳ.', 'Khi tiền chuyển dạ.', 'Khi bắt đầu chuyển dạ']
  line   2546 | Easy        | id d8b789cadd58465dbeb99f54d19e0d18 | D -> Khi bắt đầu chuyển dạ
  line  11952 | Easy        | id 1e2c47612f78425cb30c68591330945d | D -> Khi bắt đầu chuyển dạ

### Group 383 — topic: Obstetrics and Gynecology
Q: Cơ chế cầm máu quan trọng nhất trong giai đoạn sổ rau là:
Options (shared set): ['Tăng các yếu tố đông máu khi có thai', 'Đông máu trong các mạch máu ở thành tử cung do hiện tượng co mạch', 'Co thắt các bó cơ đan chéo ở thân tử cung', 'Giảm rõ rệt áp lực máu ở các tiểu động mạch tử cung']
  line   2627 | Medium      | id 13a40865d8c24278b71993f1fce0edf7 | C -> Co thắt các bó cơ đan chéo ở thân tử cung
  line   7999 | Challenging | id f6590563a5e5458db57d3c6823d5e9ad | C -> Co thắt các bó cơ đan chéo ở thân tử cung

### Group 384 — topic: Obstetrics and Gynecology
Q: Tất cả những câu sau đây về sẩy thai đều đúng, NGOẠI TRỪ:
Options (shared set): ['Hiệu quả điều trị dọa sẩy với progesterone chưa được kiểm chứng.', 'Gọi là sẩy thai khi trọng lượng thai nhi tống xuất ra ngoài <500 gr.', 'Giao hợp trong lúc có thai là một nguyên nhân chính gây sẩy thai.', 'Xuất độ sẩy thai sớm cao hơn so với sẩy thai muộn.']
  line   2647 | Medium      | id b0e7a9caab12443fb153a77869769e98 | C -> Giao hợp trong lúc có thai là một nguyên nhân chính gây sẩy thai.
  line  11921 | Easy        | id c4dc3e98d9b644a086f8983e99fa5606 | C -> Giao hợp trong lúc có thai là một nguyên nhân chính gây sẩy thai.

### Group 385 — topic: Obstetrics and Gynecology
Q: Gọi là sẩy thai sớm khi thai bị sẩy vào thời điểm nào?
Options (shared set): ['Trước tuần lễ vô kinh thứ 12.', 'Trước tuần lễ vô kinh thứ 20.', 'Trước tuần lễ vô kinh thứ 14.', 'Trước tuần lễ vô kinh thứ 10.']
  line   2648 | Easy        | id 07c8e6ba858e4437ba40e73aa1eba2aa | C -> Trước tuần lễ vô kinh thứ 14.
  line   8203 | Easy        | id 44bfbd1526be426eabe5db2107b0aa17 | C -> Trước tuần lễ vô kinh thứ 14.

### Group 386 — topic: Obstetrics and Gynecology
Q: Câu nào sau đây ĐÚNG NHẤT trong đĩnh nghĩa sảy thai:
Options (shared set): ['Thai sảy ra có trọng lượng < 500g', 'Thai bị tống ra khỏi buồng tử cung trước thời điểm có thể sống được.', 'Gọi là sảy thai khi tuổi thai < 28 tuần', 'Gọi là sảy thai khi tuổi thai <22 tuần']
  line   2673 | Easy        | id ead51adb7c47462897e2210524cf5a30 | B -> Thai bị tống ra khỏi buồng tử cung trước thời điểm có thể sống được.
  line   7864 | Easy        | id b26e21ad90464b96912794eac2e75623 | B -> Thai bị tống ra khỏi buồng tử cung trước thời điểm có thể sống được.

### Group 387 — topic: Obstetrics and Gynecology
Q: Gọi là sẩy thai sớm khi thai bị sẩy trước tuần lễ vô kinh thứ mấy:
Options (shared set): ['6', '10', '12', '16']
  line   2690 | Easy        | id 871b163f553d4fdfa128ed36e0a5c60d | C -> 12
  line   8202 | Easy        | id b2347e1f521a49d9973c49b481d42592 | C -> 12

### Group 388 — topic: Obstetrics and Gynecology
Q: Yếu tố nào không là nguyên nhân của thai ngoài tử cung:
Options (shared set): ['Tiền sử viêm vòi tử cung', 'Vòi tử cung dài bất thường', 'Các xơ dính do hậu quả phẫu thuật vùng bụng trước đó', 'Tiền sử sinh đẻ nhiều lần']
  line   2695 | Medium      | id 02aeebb4f3dd43f08454a1002b69cede | D -> Tiền sử sinh đẻ nhiều lần
  line   9090 | Medium      | id d80319bb302a4d5ab3f85f390029857e | D -> Tiền sử sinh đẻ nhiều lần

### Group 389 — topic: Obstetrics and Gynecology
Q: Phương pháp vừa có tác dụng chẩn đoán vừa có tác dụng điều trị chửa ngoài tử cung là:
Options (shared set): ['Điều trị bằng hoá chất.', 'Dùng thuốc giảm đau và theo dõi.', 'Nạo niêm mạc tử cung.', 'Nội soi ổ bụng.']
  line   2715 | Challenging | id 54a7f5f067d34a149dee20712453d922 | D -> Nội soi ổ bụng.
  line   8612 | Hard        | id a37a3fad0b61465bb62a36d1ed4c425c | D -> Nội soi ổ bụng.

### Group 390 — topic: Obstetrics and Gynecology
Q: Các xét nghiệm nào sau đây được chỉ định khi theo dõi điều trị nội khoa thai ngoài tử cung. Chọn một câu đúng nhất:
Options (shared set): ['Siêu âm ,công thức máu ,giải phẫu bệnh lý', 'Siêu âm, định lượng nồng độ Estrogene trong máu, công thức máu', 'Siêu âm, định lượng ß - hCG và/hoặc nồng độ progesteron / máu', 'Siêu âm, Định lượng nồng độ Progesteron và Estrogène trong máu']
  line   2725 | Medium      | id c134d966de634fb6979f449ed2a3f227 | C -> Siêu âm, định lượng ß - hCG và/hoặc nồng độ progesteron / máu
  line   3910 | Medium      | id af1411ef5bae42929bbc6d193dc93f1f | C -> Siêu âm, định lượng ß - hCG và/hoặc nồng độ progesteron / máu

### Group 391 — topic: Obstetrics and Gynecology
Q: Trong thai trứng, Biến chứng nguy hiểm đến tính mạng bệnh nhân là:
Options (shared set): ['Mẹ mệt do nghén nặng.', 'Tử cung căng quá mức.', 'Băng huyết do sẩy trứng.', 'Ung thư nguyên bào nuôi.']
  line   2746 | Medium      | id 2957d57e99fe42868a1d5f6738d25cb4 | C -> Băng huyết do sẩy trứng.
  line   3386 | Challenging | id 8eeace30585b4deabf365732681a9d8e | C -> Băng huyết do sẩy trứng.

### Group 392 — topic: Obstetrics and Gynecology
Q: Sau hút trứng, yếu tố quan trọng nhất để đánh giá và tiên lượng bệnh nhân là:
Options (shared set): ['Nồng độ hCG.', 'Thể tích tử cung.', 'Nồng độ estradiol.', 'Nang hoàng tuyến.']
  line   2747 | Medium      | id 0ad91f8a3c9b4d56b58b415c9c5fef50 | A -> Nồng độ hCG.
  line   3387 | Medium      | id 381bc67802a54237b92957dc990d68da | A -> Nồng độ hCG.

### Group 393 — topic: Obstetrics and Gynecology
Q: Dấu hiệu nào là dấu hiệu tiến triển tốt sau nạo trứng:
Options (shared set): ['Tử cung to, nang hoàng tuyến tồn tại dai dẳng', 'Xuất hiện nhân di căn âm đạo', 'Ra huyết dai dẳng sau nạo trứng', 'HCG biến mất nhanh sau 8 tuần']
  line   2756 | Medium      | id 169899e8059b4b899dcbe8bc156cfb0c | D -> HCG biến mất nhanh sau 8 tuần
  line  11950 | Easy        | id eebe8b386f994e07aa8d5db3f1dcc7f7 | D -> HCG biến mất nhanh sau 8 tuần

### Group 394 — topic: Obstetrics and Gynecology
Q: Thai trứng xâm lấn thường xảy ra:
Options (shared set): ['Sau thai ngoài tử cung.', 'Sau đẻ thường.', 'Sau sảy thai.', 'Sau thai trứng.']
  line   2762 | Medium      | id 70cb3e24726a47caa8b4c611a9c0115f | D -> Sau thai trứng.
  line   3824 | Medium      | id 73974551cf354a7091a030ad774b216e | D -> Sau thai trứng.

### Group 395 — topic: Obstetrics and Gynecology
Q: Chọn câu SAI, nang hoàng tuyến là nang:
Options (shared set): ['Cơ năng do kích thích của hCG.', 'Nếu to có thể chọc hút qua siêu âm hay nội soi.', 'Chỉ cần điều trị nội khoa khi xoắn hay vỡ', 'Thường trở lại kích thước bình thường sau 8-10 tuần.']
  line   2767 | Medium      | id f65afe3c379a438cae58f2c37ecbe67a | C -> Chỉ cần điều trị nội khoa khi xoắn hay vỡ
  line   7133 | Medium      | id dd05f6e52ac3464da13f005eba3bf0f1 | C -> Chỉ cần điều trị nội khoa khi xoắn hay vỡ

### Group 396 — topic: Obstetrics and Gynecology
Q: Chọn câu trả lời đúng về chửa trứng:
Options (shared set): ['Chửa trứng toàn phần là do sự kết hợp giữa 2 tinh trùng với một tế bào noãn bình thường.', 'Chửa trứng toàn phần là do sự thụ tinh của một noãn không nhân với một tinh trùng chứa nhiễm sắc thể X nhân đôi', 'Nhiễm sắc đồ XX của chửa trứng toàn phần có nguồn gốc 50% từ cha và 50% từ mẹ.', '94% chửa trứng toàn phần có nhiễm sác thể giới tính là XY.']
  line   2770 | Medium      | id 258718715ea74c95bd729a8c2c589504 | B -> Chửa trứng toàn phần là do sự thụ tinh của một noãn không nhân với một tinh trùng chứa nhiễm sắc thể X nhân đôi
  line   9441 | Easy        | id beb1ca6b89d84d568c8e4d156a352d54 | B -> Chửa trứng toàn phần là do sự thụ tinh của một noãn không nhân với một tinh trùng chứa nhiễm sắc thể X nhân đôi
  line  11557 | Medium      | id 38652386e8c7403badbe465af5722ece | A -> Chửa trứng toàn phần là do sự kết hợp giữa 2 tinh trùng với một tế bào noãn bình thường.

### Group 397 — topic: Obstetrics and Gynecology
Q: Rau tiền đạo bán trung tâm là:
Options (shared set): ['Khi khám, sờ thấy cả màng ối và rau.', 'Chỉ sờ thấy toàn rau, chảy máu nhiều.', 'Khi thai 20 tuần, siêu âm thấy mép bánh rau cách lỗ trong cổ tử cung 3 cm.', 'Kết hợp giữa B và C.']
  line   2789 | Easy        | id da74c61803e64844b9b063230a8d9643 | A -> Khi khám, sờ thấy cả màng ối và rau.
  line   3434 | Medium      | id 20ecb9b782634d589a07e0bd499b331e | A -> Khi khám, sờ thấy cả màng ối và rau.

### Group 398 — topic: Obstetrics and Gynecology
Q: Chọn câu SAI trong nhau bong non thể nặng:
Options (shared set): ['Tử cung co cứng như gỗ', 'Thường gây thai chết trong tử cung', 'Gây rối loạn đông máu', 'Biến chứng kèm theo suy tim']
  line   2827 | Medium      | id 41da80145d5445859d5d3a31d9669af0 | D -> Biến chứng kèm theo suy tim
  line   3469 | Medium      | id f1e128808cec410388af2fa85c539aaa | D -> Biến chứng kèm theo suy tim

### Group 399 — topic: Obstetrics and Gynecology
Q: Hướng xử trí đầu tiên của rau bong non sau khi thai ra:
Options (shared set): ['Thuốc hạ áp.', 'Kích thích bằng thuốc tăng co.', 'Truyền fibrinogen.', 'Truyền máu tươi.']
  line   2832 | Medium      | id df822b2add444fb79c7d867e9968c006 | B -> Kích thích bằng thuốc tăng co.
  line   3475 | Medium      | id eba841a2557140d2a669f78ce23e97c4 | B -> Kích thích bằng thuốc tăng co.

### Group 400 — topic: Obstetrics and Gynecology
Q: Trong trường hợp vỡ tử cung hoàn toàn, thai nhi bị đẩy vào trong ổ bụng và thường chết nhanh chóng là do nguyên nhân, chọn câu đúng:
Options (shared set): ['Thai không được bảo vệ bởi ối', 'Thai bị chèn ép bởi các cơ quan trong ổ bụng', 'Vở tử cung gây bong rau', 'Thay đổi áp suất trong ổ bụng']
  line   2836 | Challenging | id 45cfa219df8b44598d9a834a39e18af2 | C -> Vở tử cung gây bong rau
  line   3482 | Medium      | id bb1f0ece839c409982990af8476cdfb1 | C -> Vỡ tử cung gây bong rau

### Group 401 — topic: Obstetrics and Gynecology
Q: Vỡ tử cung ở tử cung có sẹo mổ cũ khác với không có sẹo ở điểm nào, chọn câu đúng:
Options (shared set): ['Thường chảy máu nhiều hơn', 'Kèm gây tổn thương các tạng lân cận', 'Không có triệu chứng dọa vỡ trước đó', 'Có triệu chứng dọa vỡ trước đó']
  line   2850 | Medium      | id 6b8c025ecc1a41babce92fa95f440f3c | C -> Không có triệu chứng dọa vỡ trước đó
  line  11949 | Medium      | id bff7d2ccad7d44df8103631c2c1c610e | D -> Có triệu chứng dọa vỡ trước đó

### Group 402 — topic: Obstetrics and Gynecology
Q: Các câu dưới đây đều đúng khi nói về vỡ tử cung, NGOẠI TRỪ:
Options (shared set): ['Có thể gặp trong thời kỳ thai nghén', 'Là một trong năm tai biến sản khoa', 'Có biện pháp phòng ngừa hữu hiệu', 'Là một tai biến khó chẩn đoán']
  line   2851 | Medium      | id ec9b0817ed9c412b8a88a0b1ca68f65d | D -> Là một tai biến khó chẩn đoán
  line   7567 | Medium      | id f4520c57e091435892147a89f12244fd | D -> Là một tai biến khó chẩn đoán

### Group 403 — topic: Obstetrics and Gynecology
Q: Nhịp tim thai chậm được định nghĩa là:
Options (shared set): ['<100 lần/ p', '<120 lần/ p', '<130 lần/ p', '<140 lần/ p']
  line   2862 | Easy        | id 36d5fbd7009243b3b554a572d6abe22b | B -> <120 lần/ p
  line   8505 | Easy        | id 8bf635d7f43c43e1b712009fc22c744f | D -> <120 lần/ p

### Group 404 — topic: Obstetrics and Gynecology
Q: Nhịp tim thai nhanh được định nghĩa là:
Options (shared set): ['>180lần/ p', '>170 lần/ p', '>160 lần/ p', '>150 lần/ p']
  line   2863 | Easy        | id d012e13937a147a58f84648baefd8432 | C -> >160 lần/ p
  line   8506 | Easy        | id 08625c181a144149937ca96f83f0418b | D -> >160 lần/ p

### Group 405 — topic: Obstetrics and Gynecology
Q: KHÔNG cần làm xét nghiệm beta HCG để:
Options (shared set): ['Xác định chửa trứng.', 'Xác định thai dị dạng.', 'Xác định thai lưu.', 'Xác định thai ngoài tử cung.']
  line   2881 | Medium      | id d5174696dc014d83a98181e1e1910d39 | B -> Xác định thai dị dạng.
  line   3504 | Medium      | id 0e36248934224401a5e5dbfb827fd94e | B -> Xác định thai dị dạng.
  line   8314 | Easy        | id 1a66d743b53f48d68247edef86dd8455 | B -> Xác định thai dị dạng.

### Group 406 — topic: Obstetrics and Gynecology
Q: Các nguyên nhân làm xét nghiệm HCG(+) giả, NGOẠI TRỪ:
Options (shared set): ['Nước tiểu có hồng cầu.', 'Khi tiêm corticoid.', 'Dụng cụ thử thai có chất tẩy rửa tổng hợp.', 'Khi có thai hơn 1 tháng.']
  line   2882 | Challenging | id 18b4d23495ed475db1e09364c44b7caa | D -> Khi có thai hơn 1 tháng.
  line   3506 | Challenging | id a31252a0b57b4148b113003c666bac41 | D -> Khi có thai hơn 1 tháng.

### Group 407 — topic: Obstetrics and Gynecology
Q: Không làm phiến đồ âm đạo khi:
Options (shared set): ['Ngoài giai đoạn hành kinh.', 'Không có nhiễm khuẩn âm đạo.', 'Người bệnh không rửa âm đạo trong vòng 24h trước đó.', 'Sau khi quan hệ tình dục.']
  line   2883 | Medium      | id a383e699e07d4902a2ab0a1828472d94 | D -> Sau khi quan hệ tình dục.
  line   3507 | Medium      | id 8019cd305122407188dcab0c3b46ecc5 | D -> Sau khi quan hệ tình dục.

### Group 408 — topic: Obstetrics and Gynecology
Q: AFP( alpha-fetoprotein) tổng hợp chủ yếu bởi gan của thai nhi thải trừ qua nước tiểu vào buồng ối và lưu thông vào tuần hoàn của mẹ
Options (shared set): ['Đúng', 'Sai']
  line   2885 | Medium      | id 54802e13a1384fe280ff9c21f1aad269 | A -> Đúng
  line   3942 | Medium      | id be5a0f41946a4c75b4f7ebfea73211f6 | A -> Đúng

### Group 409 — topic: Obstetrics and Gynecology
Q: Khi xác định ngôi ngang, ta phải có điểm mốc của ngôi là:
Options (shared set): ['Mỏm vai thai nhi', 'Bụng thai nhi', 'Lưng thai nhi', 'Khuỷu tay thai nhi']
  line   2902 | Easy        | id 643b04f2936048f180996dac6ab62484 | A -> Mỏm vai thai nhi
  line   8309 | Medium      | id d3e076ed562e40da8100526fc7ff2b01 | A -> Mỏm vai thai nhi

### Group 410 — topic: Obstetrics and Gynecology
Q: Trong các câu dưới đây hãy xác định một câu mà ngôi có kiểu thế đó đẻ được đường dưới:
Options (shared set): ['Ngôi trán:Mũi chậu trái trước', 'Ngôi mặt - cằm cùng', 'Ngôi mặt cằm vệ', 'Ngôingang: vai chậu phải trước']
  line   2911 | Medium      | id 02507f392dc3426b960a1ed8a52244c9 | C -> Ngôi mặt cằm vệ
  line   2924 | Medium      | id 79c9ef3f39c94bab98bb59cd345b61ea | D -> Ngôi mặt cằm vệ

### Group 411 — topic: Obstetrics and Gynecology
Q: Trong điều kiện bình thường ngôi thai nào không đẻ được đường dưới:
Options (shared set): ['Ngôi mặt cằm vệ', 'Ngôi chỏm', 'Ngôi mông', 'Ngôi trán']
  line   2912 | Medium      | id 74dcfed8dc444f38bad503331898036c | D -> Ngôi trán
  line   2925 | Medium      | id 73bd0154a78e4d7b8d0bb258e55bec0e | D -> Ngôi trán

### Group 412 — topic: Obstetrics and Gynecology
Q: Trong những biến chứng kể sau, biến chứng nào không liên quan đến tiền sản giật:
Options (shared set): ['Sẩy thai.', 'Thai chết lưu.', 'Sản giật.', 'Thai kém phát triển trong tử cung.']
  line   2929 | Medium      | id 6b5605e254bf40dab79d617d3d27edf6 | A -> Sẩy thai.
  line   3320 | Medium      | id ad91a95abadb4a91a560f087e1f6cf78 | A -> Sẩy thai.

### Group 413 — topic: Obstetrics and Gynecology
Q: Theo phân loại huyết áp cao trong thai kỳ, hội chứng tiền sản giật- sản giật thuộc nhóm:
Options (shared set): ['Huyết áp cao do thai đơn thuần.', 'Huyết áp cao do thai có kèm protein/niệu hoặc phù.', 'Huyết áp cao mãn tính có kèm theo biến chứng ở thận.', 'Huyết áp cao ngẫu nhiên phối hợp với thai kỳ.']
  line   2947 | Medium      | id e807c40403b744418ef1f645ecd696d8 | B -> Huyết áp cao do thai có kèm protein/niệu hoặc phù.
  line   8787 | Easy        | id a74b2905dc5546d49b3d7f3884bcc56c | B -> Huyết áp cao do thai có kèm protein/niệu hoặc phù.

### Group 414 — topic: Obstetrics and Gynecology
Q: Tổn thương thận hay kết hợp với tiền sản giật nhất là:
Options (shared set): ['Phù nề nội mô cầu thận.', 'Viêm đài bể thận.', 'Hoại tử vỏ thận.', 'Hoại tử ống thận cấp.']
  line   2948 | Medium      | id df06cfb678dc40bf8c3bb7143b4c0c2d | A -> Phù nề nội mô cầu thận.
  line   3749 | Medium      | id 2103611103d14e8a99fd1cbac2742f77 | A -> Phù nề nội mô cầu thận.

### Group 415 — topic: Obstetrics and Gynecology
Q: Thuốc nào sau đây không được sử dụng trong tiền sản giật- sản giật:
Options (shared set): ['Papaverin', 'Magesium sulfate', 'Ergometrin', 'Seduxen']
  line   2957 | Medium      | id f3649c7df5ec4533804f7ec1505355ce | C -> Ergometrin
  line  11892 | Easy        | id 98e7af1f9d8b44db992a871dcf6cc759 | C -> Ergometrin

### Group 416 — topic: Obstetrics and Gynecology
Q: Thai chậm phát triển trong tử cung thường xãy ra trong bệnh lý tiền sản giật là do:
Options (shared set): ['Bất thường về thai', 'Bất thường về cấu trúc rau', 'Suy tuần hoàn tử cung- rau mãn tính', 'Chế độ ăn uống kiêng kem khi mang thai']
  line   2960 | Medium      | id 0c28a478b2d240b39e95f4a854b1e4dd | C -> Suy tuần hoàn tử cung- rau mãn tính
  line   3959 | Medium      | id 1807fb31d9c54cf48f879028ef07b145 | C -> Suy tuần hoàn tử cung- rau mãn tính

### Group 417 — topic: Obstetrics and Gynecology
Q: Nguyên nhân gây ra những tổn thương thiếu máu cục bộ, xuất huyết hoại tử tại các cơ quan quan trọng ở giai đoạn cuối của Tiền sản giật là:
Options (shared set): ['Thiếu máu ở thận làm hoạt hóa hệ thống Renin – Angiotensine', 'Rối loạn chức năng nội tiết của rau thai', 'Co mạch và tổn thương tế bào nội mô mạch', 'Do yếu tố miễn dịch - di truyền']
  line   2961 | Medium      | id 0a2db2ba3ec74281b930e5f222b0d8d4 | C -> Co mạch và tổn thương tế bào nội mô mạch
  line   3909 | Challenging | id a3779b65ccf14c1e8906381d0aa2a474 | C -> Co mạch và tổn thương tế bào nội mô mạch

### Group 418 — topic: Obstetrics and Gynecology
Q: Hiện nay thuốc điều trị chọn lọc để dự phòng lên cơn co giật và chống co giật là:
Options (shared set): ['Magesium sulfate', 'Seduxen', 'Hydralazin', 'Coctaillytic']
  line   2966 | Medium      | id b10ec091460c49b99c75edf1110ff5ba | A -> Magesium sulfate
  line   3758 | Medium      | id 61c3964e12d246108e97c4a2d5d1a22f | A -> Magesium sulfate

### Group 419 — topic: Obstetrics and Gynecology
Q: Tỉ lệ gặp U nang nhầy buồng trứng là:
Options (shared set): ['Khoảng 60%', 'Khoảng 30%', 'Khoảng 10%', 'Khoảng 1%']
  line   3059 | Easy        | id 92a2b0a9784140249e138ab90dc69a28 | A -> Khoảng 60%
  line   8863 | Easy        | id 3c536bb9247f48f3a3eb5c31e8a0c1f3 | A -> Khoảng 60%

### Group 420 — topic: Obstetrics and Gynecology
Q: Triệu chứng nào sau đây ít khi do u nang buồng trứng gây nên?
Options (shared set): ['Đau hoặc tức nặng bụng dưới', 'Bụng to dần', 'Mất kinh', 'Rối loạn tiểu tiện']
  line   3075 | Medium      | id 1d4386928b514ef787626ccaa5c942ae | C -> Mất kinh
  line  11930 | Easy        | id 589561625a9d4f6a98815ab3af23bd0b | C -> Mất kinh

### Group 421 — topic: Obstetrics and Gynecology
Q: Khi nghe, đếm nhịp tim thai, cần bắt mạch quay để phân biệt với mạch mẹ vì:
Options (shared set): ['Nhịp tim thai chậm hơn mạch quay', 'Nhịp tim thai nhanh hơn mạch quay', 'Nhịp tim thai trùng với mạch quay', 'Tất cả đều sai']
  line   3097 | Medium      | id 03932453010f44f3aa453a1bad322253 | B -> Nhịp tim thai nhanh hơn mạch quay
  line  11890 | Easy        | id 2b41c4373bf54baead221d17e8cfd3fa | B -> Nhịp tim thai nhanh hơn mạch quay

### Group 422 — topic: Obstetrics and Gynecology
Q: Khám thai nhằm mục đích:
Options (shared set): ['Xác định tuổi thai', 'Xác định thai bình thường hay thai bệnh lý', 'Xác định các dấu hiệu phát triển bình thường của thai', 'Tất cả đều đúng']
  line   3098 | Easy        | id e0cdae77f5d44ac386f11f461046f6c0 | D -> Tất cả đều đúng
  line   8272 | Medium      | id 71bf9b6936d84714a5ac0276d6720f7f | D -> Tất cả đều đúng

### Group 423 — topic: Obstetrics and Gynecology
Q: Chọn một câu sai về ối vỡ sớm:
Options (shared set): ['Gây ngôi thai bất thường', 'Gây chuyển dạ kéo dài', 'Gây suy thai', 'Gây nhiễm khuẩn ối']
  line   3104 | Medium      | id 21d59fc3974a447e9eed21e55c38fd87 | A -> Gây ngôi thai bất thường
  line  11910 | Medium      | id 9598a57b75bb4c4e941d4a829f3bced6 | A -> Gây ngôi thai bất thường

### Group 424 — topic: Obstetrics and Gynecology
Q: Nguyên nhân thai chết mà không bị tống xuất ra ngay là:
Options (shared set): ['Nhau còn tiết ra progesterone một thời gian sau khi thai chết', 'Thai chết khi cơ tử cung chưa tiếp nhận Oxytocin nội sinh', 'Thai chết tiết ra một yếu tố làm cơ tử cung không đối với Prostaglandine', 'Do tình trạng bệnh lý của mẹ khiến cơ tử cung co không đủ mạnh']
  line   3124 | Medium      | id 717ef19605f44e73b60272bfdf10f6f4 | A -> Nhau còn tiết ra progesterone một thời gian sau khi thai chết
  line   3229 | Challenging | id 2533c6e838a94445bdda53ed8a4ae6f6 | A -> Nhau còn tiết ra progesterone một thời gian sau khi thai chết

### Group 425 — topic: Obstetrics and Gynecology
Q: Nguyên nhân của thiểu ối là:
Options (shared set): ['Bất sản thận.', 'Teo thực quản.', 'Đa thai.', 'Bất đồng nhóm máu giữa mẹ và con.']
  line   3129 | Medium      | id ace83dc56ece47dc934856adfa349d36 | A -> Bất sản thận.
  line   3747 | Medium      | id df0fa26d073d4a68972577ed23a589c5 | A -> Bất sản thận.

### Group 426 — topic: Obstetrics and Gynecology
Q: Khi phát hiện thiểu ối vào quí hai của thai kỳ, thăm dò cần thực hiện ngay là:
Options (shared set): ['Nhiễm sắc thể đồ.', 'Định lượng α - fetoprotein', 'Khảo sát cấu trúc âm học của thận.', 'Triple test']
  line   3130 | Medium      | id b578c55902f84210b79d717ea2b7c246 | C -> Khảo sát cấu trúc âm học của thận.
  line   3748 | Challenging | id 85df3cfd878545549de474df5bea9557 | C -> Khảo sát cấu trúc âm học của thận.

### Group 427 — topic: Obstetrics and Gynecology
Q: Trong trường hợp thai 28 tuần, rách trung sản mạc. Bạn sẽ lựa chọn phương pháp điều trị nào sau đây:
Options (shared set): ['Khâu vòng cổ tử cung', 'Kháng sinh, theo dõi', 'Mổ lấy thai', 'Đẻ chỉ huy.']
  line   3136 | Challenging | id a192892e3aaf4a4d8f5635d8ad4bf448 | B -> Kháng sinh, theo dõi
  line   3655 | Challenging | id 0393147e3b43409983c6a4d229d2ca61 | B -> Kháng sinh, theo dõi
  line   8974 | Hard        | id 842cee6e8c784298ada7810543d9a055 | B -> Kháng sinh, theo dõi

### Group 428 — topic: Obstetrics and Gynecology
Q: Rong kinh rong huyết cơ năng là:
Options (shared set): ['Chảy máu bất thường ở đường sinh dục.', 'Do tử cung bị nạo hút quá nhiều.', 'Hay gặp ở tuổi dạy thì hoặc tuổi tiền mãn kinh.', 'Hay gặp ở những người có bệnh về máu.']
  line   3150 | Medium      | id fd1acc41a94247abb85735c3c50026b3 | C -> Hay gặp ở tuổi dạy thì hoặc tuổi tiền mãn kinh.
  line  11944 | Easy        | id 36c2c0259b22443a9e120cb910ca6466 | C -> Hay gặp ở tuổi dạy thì hoặc tuổi tiền mãn kinh.

### Group 429 — topic: Obstetrics and Gynecology
Q: Một câu sau đây không đúng trong tính chất chung của rong kinh rong huyết cơ năng:
Options (shared set): ['Chu kỳ kinh nguyệt ít nhiều bị rối loạn.', 'Máu từ tử cung ra quá nhiều, điều trị rất khó khăn, thường phải cắt tử cung.', 'Toàn trạng có biểu hiện thiếu máu do kinh ra nhiều.', '30% rong kinh cơ năng ở tuổi mãn kinh cần theo dõi tiền ung thư.']
  line   3151 | Medium      | id e12811c9b5254b338fc4da3bda001427 | B -> Máu từ tử cung ra quá nhiều, điều trị rất khó khăn, thường phải cắt tử cung.
  line   8396 | Hard        | id fbc05e7c5c184801b7aead5afae68ec0 | B -> Máu từ tử cung ra quá nhiều, điều trị rất khó khăn, thường phải cắt tử cung.

### Group 430 — topic: Obstetrics and Gynecology
Q: Chu kỳ kinh được tính từ lúc:
Options (shared set): ['Sạch kinh đến ngày đầu của kỳ kinh sau.', 'Ngày đầu của kỳ kinh này đến ngày kết thúc kỳ kinh sau.', 'Ngày đầu của kỳ kinh này đến ngày đầu kỳ kinh sau.', 'Ngày sạch của kỳ kinh này đến ngày sạch kỳ kinh sau.']
  line   3154 | Easy        | id f7c332d4859e40b9adbab2fb32b97e81 | C -> Ngày đầu của kỳ kinh này đến ngày đầu kỳ kinh sau.
  line   7957 | Easy        | id abb86d62c4a644a9a82defb1029153f7 | C -> Ngày đầu của kỳ kinh này đến ngày đầu kỳ kinh sau.

### Group 431 — topic: Obstetrics and Gynecology
Q: Thời điểm thích hợp để áp dụng phương pháp hút thai với bơm Karmann 1 van là:
Options (shared set): ['Chậm kinh 2 ngày', 'Chậm kinh 1 tuần', 'Chậm kinh 2 tuần', 'Chậm kinh 4 tuần']
  line   3170 | Medium      | id 9a334471088a4537be750b96ec9a3ad1 | C -> Chậm kinh 2 tuần
  line   3516 | Medium      | id a5ab5bbd8a4c4534ad57b5380e4b549c | C -> Chậm kinh 2 tuần

### Group 432 — topic: Obstetrics and Gynecology
Q: Hút thai có ưu điểm hơn nạo thai vì:
Options (shared set): ['Không phải nong cổ tử cung', 'Ít chảy máu', 'Ít đau', 'Ít nhiễm trùng']
  line   3171 | Medium      | id aed032b71ee8418ab46ce558f88e85b3 | D -> Ít nhiễm trùng
  line   3517 | Medium      | id b1614dc8382f41e285efce971207cc29 | D -> Ít nhiễm trùng

### Group 433 — topic: Obstetrics and Gynecology
Q: Một người phụ nữ có chu kỳ kinh nguyệt không đều (dài hoặc ngắn hơn bình thường) thì rụng trứng có thể xảy ra vào ngày. Chọn câu đúng nhất:
Options (shared set): ['14-16 ngày sau khi sạch kinh', 'Giữa chu kỳ kinh', 'Khoảng 14 ngày trước kỳ kinh tới', 'Không thể xác định được khoảng thời gian xảy ra rụng trứng']
  line   3183 | Challenging | id 8a573c3bf65f490cad1d3564eb2bcf62 | D -> Không thể xác định được khoảng thời gian xảy ra rụng trứng
  line   7137 | Medium      | id 838699de403e4053aa9afca8e01c6282 | D -> Không thể xác định được khoảng thời gian xảy ra rụng trứng
  line   7580 | Medium      | id 19374455d07c4082b7f0773f347c5b10 | D -> Không thể xác định được khoảng thời gian xảy ra rụng trứng

### Group 434 — topic: Obstetrics and Gynecology
Q: CHẢY MÁU BẤT THƯỜNG TỬ CUNG Rong kinh:
Options (shared set): ['Ra máu có chu kỳ', 'Kéo dài trên 7 ngày', 'Gồm có rong kinh cơ năng và rong kinh thực thể', 'Rong kinh là triệu chứng không phải là bệnh']
  line   3185 | Easy        | id ced9f1b8285e47feacbae114d1e7ead6 | B -> Kéo dài trên 7 ngày
  line   7883 | Easy        | id dab0c7fd10fe4d6daa0ce606834d4b51 | A -> Ra máu có chu kỳ

### Group 435 — topic: Obstetrics and Gynecology
Q: Loại đầu ối nào sau đây đặc trưng cho thai lưu.
Options (shared set): ['Đầu ối phồng.', 'Đầu ối dẹt.', 'Đầu ối hình quả lê.', 'không hình thành đầu ối.']
  line   3204 | Medium      | id ec5bcce75f0a436e82bbc5a247e63d2f | C -> Đầu ối hình quả lê.
  line   3897 | Medium      | id 48e21f9749724805b362e99ec244e689 | C -> Đầu ối hình quả lê

### Group 436 — topic: Obstetrics and Gynecology
Q: Câu nào sau đây không đúng đối với thai lưu:
Options (shared set): ['Có thể gây rối loạn đông máu.', 'Gây tâm lý hoang mang lo lắng cho bà mẹ.', 'Cuộc đẻ thường tiến triển nhanh vì thai dễ sổ.', 'Thường phải chủ động kiểm soát tử cung sau đẻ vì dễ sót rau.']
  line   3222 | Medium      | id 415e16e8d1fe4c9e8cd3d3c373a788c1 | C -> Cuộc đẻ thường tiến triển nhanh vì thai dễ sổ.
  line   7865 | Medium      | id 0c1db649e3ed4a0683b10714d477d6c4 | C -> Cuộc đẻ thường tiến triển nhanh vì thai dễ sổ.

### Group 437 — topic: Obstetrics and Gynecology
Q: Dịch tiết sinh lý thường gặp:
Options (shared set): ['Ở trẻ vị thành niên', 'Phụ nữ sau đẻ', 'Quanh ngày phóng noãn', 'Phụ nữ đã mãn kinh.']
  line   3245 | Easy        | id 471b14cebcda48f8a36bb2e86db79ea2 | C -> Quanh ngày phóng noãn
  line  11893 | Easy        | id e539ed05d74146c08a701357cc1f7b02 | C -> Quanh ngày phóng noãn

### Group 438 — topic: Obstetrics and Gynecology
Q: Dây chằng không tham gia giữ tử cung tại chỗ:
Options (shared set): ['Dây chằng tròn.', 'Dây chằng rộng.', 'Dây chằng thắt lưng buồng trứng.', 'Dây chằng tử cung cùng.']
  line   3277 | Medium      | id 960805aeec28484abe928083f3504bab | C -> Dây chằng thắt lưng buồng trứng.
  line  11956 | Easy        | id 3e5c725c89ee48158e2d883e78a27470 | B -> Dây chằng rộng.

### Group 439 — topic: Obstetrics and Gynecology
Q: Nguyên nhân chính gây sa sinh dục là:
Options (shared set): ['Do chửa đẻ nhiều lần.', 'Do lao động nặng và sớm sau đẻ.', 'Do cơ địa bẩm sinh.', 'Do rối loạn dinh dưỡng.']
  line   3278 | Medium      | id b336411a99d0427baee3eb45e7739494 | A -> Do chửa đẻ nhiều lần.
  line   8465 | Medium      | id 83b66bac472d4aadb0bd5877b372f41b | A -> Do chửa đẻ nhiều lần.

### Group 440 — topic: Obstetrics and Gynecology
Q: Hình ảnh nào sau đây qua soi cổ tử cung không cần thiết phải sinh thiết:
Options (shared set): ['Lộ tuyến', 'Lát đá', 'Chấm đáy', 'Mạch máu không điển hình']
  line   3284 | Medium      | id 81527029fa634684b6bd52f660fda37b | A -> Lộ tuyến
  line   3817 | Medium      | id fbd1f291d9104d78b43f9f960859c636 | A -> Lộ tuyến

### Group 441 — topic: Obstetrics and Gynecology
Q: Test sau giao hợp được thực hiện trong thời điểm:
Options (shared set): ['Ngay sau giao hợp', 'Sau giao hợp 2-4 giờ', 'Sau giao hợp 4-8 giờ', 'Sau giao hợp 8-12 giờ']
  line   3287 | Medium      | id ddc727ffe3ec40609039c5f71653dba6 | D -> Sau giao hợp 8-12 giờ
  line   3560 | Medium      | id 8a02c211ea5b4bec9768267710adfb4d | D -> Sau giao hợp 8-12 giờ
  line   7071 | Medium      | id 471379aeea7646678a884b55622b2079 | D -> Sau giao hợp 8-12 giờ

### Group 442 — topic: Obstetrics and Gynecology
Q: Nội soi tiểu khung trong phụ khoa nhằm mục đích:
Options (shared set): ['Chẩn đoán một số bệnh lý phụ khoa', 'Kết hợp phẩu thuật', 'Chẩn đoán viêm phúc mạc tiểu khung', 'A và B đúng']
  line   3292 | Medium      | id 2df4a4de44c04793aa37e2e7736a2832 | D -> A và B đúng
  line   4111 | Medium      | id 395d42069e114f8b9dc5b4e87498ad1c | D -> A và B đúng

### Group 443 — topic: Obstetrics and Gynecology
Q: Dịch nhầy cổ tử cung có “hình ảnh con ngươi”, chứa dịch trong loãng, dễ kéo sợi vào:
Options (shared set): ['Vào ngày đầu tiên sau sạch kinh', 'Vào ngày rụng trứng', 'Vào ngày trước kỳ kinh', 'Chỉ A,C đúng']
  line   3297 | Medium      | id 87ed170859934ca48726514028ae5e7e | B -> Vào ngày rụng trứng
  line   3562 | Medium      | id 37ec260fa25a4bc882f1a5d85b7da2fc | B -> Vào ngày rụng trứng
  line   7073 | Medium      | id 74671dd75dd845f6ad52413efa090017 | B -> Vào ngày rụng trứng
  line   7115 | Medium      | id dac63dd2076648e091671867cb739115 | B -> Vào ngày rụng trứng

### Group 444 — topic: Obstetrics and Gynecology
Q: Một phụ nữ 42 tuổi bị băng kinh, cách xử trí đúng nhất là:
Options (shared set): ['Thuốc nội tiết progesten, khi cầm máu cần nạo hút buồng tử cung làm GPBL', 'Thuốc oxytocin + ecgometrin, khi cầm máu cần nạo hút buồng tử cung làm GPBL', 'Thuốc oxytocin + ecgometrin, cần nạo hút buồng tử cung ngay làm GPBL', 'Thuốc estrogen + progesten, 24 giờ sau cần nạo hút buồng tử cung làm GPBL']
  line   3298 | Challenging | id cfa295e744e24c59820bd7c81eab1012 | C -> Thuốc oxytocin + ecgometrin, cần nạo hút buồng tử cung ngay làm GPBL
  line   3630 | Challenging | id 95a810551f254358baa25ee5af578e58 | C -> Thuốc oxytocin + ecgometrin, cần nạo hút buồng tử cung ngay làm GPBL

### Group 445 — topic: Obstetrics and Gynecology
Q: Chỉ định mổ nào dưới đây là chỉ định mổ vì nguyên nhân của thai
Options (shared set): ['Ngôi ngang', 'Sa dây rau', 'Thiểu ối', 'Rối loạn cơn co tử cung']
  line   3313 | Medium      | id a11fb970da2e42b89cf50b8dbad9913e | A -> Ngôi ngang
  line   9703 | Medium      | id f558eeea2d9a47b9ab03d02246716f47 | A -> Ngôi ngang

### Group 446 — topic: Obstetrics and Gynecology
Q: Thăm khám cận lâm sàng nào có giá trị nhất chẩn đoán u nang buồng trứng?
Options (shared set): ['Chụp bụng không chuẩn bị.', 'Chụp tử cung vòi trứng có chuẩn bị.', 'Siêu âm.', 'Tế bào âm đạo.']
  line   3330 | Medium      | id 312a5450c0e44bd8aa5bf4a11bbc3164 | C -> Siêu âm.
  line   4055 | Medium      | id 3f712ccb20964e65926cb5d105a1b830 | C -> Siêu âm.

### Group 447 — topic: Obstetrics and Gynecology
Q: Xét nghiệm nào dưới đây không phải xét nghiệm thăm dò trong vô sinh:
Options (shared set): ['Tinh dịch đồ.', 'Soi và sinh thiết cổ tử cung.', 'Nạo sinh thiết niêm mạc tử cung.', 'Chụp tử cung – vòi trứng']
  line   3351 | Medium      | id d8c0ad73f2474f62aac53aafcca1e3c9 | B -> Soi và sinh thiết cổ tử cung.
  line  11936 | Easy        | id 3b431921092b4048baba64fe8866ac41 | B -> Soi và sinh thiết cổ tử cung.

### Group 448 — topic: Obstetrics and Gynecology
Q: Các yếu tố thuận lợi sau đây cho bệnh thai trứng đều đúng, ngoại trừ:
Options (shared set): ['Có rối loạn nhiễm sắc thể', 'Bệnh di truyền', 'Thiếu dinh dưỡng, suy giảm miễn dịch', 'Đẻ nhiều, đẻ dầy khi tuổi mẹ < 20 và > 40']
  line   3382 | Medium      | id 289fe81f7ff447aa93a00960cf0ff25e | B -> Bệnh di truyền
  line   9492 | Medium      | id 4b53c82a62db4cfaab805ec134783843 | B -> Bệnh di truyền

### Group 449 — topic: Obstetrics and Gynecology
Q: Siêu âm nếu thấy túi thai và tim thai nằm cạnh tử cung hướng xử trí tiếp theo là:
Options (shared set): ['Định lượng progesterone.', 'Định lượng hCG.', 'Điều trị nội khoa bằng MTX.', 'Nội soi ổ bụng ngay.']
  line   3408 | Challenging | id 5e719d2869654273a08852654920f09e | D -> Nội soi ổ bụng ngay.
  line   4024 | Challenging | id 3e054dcac7484c3882f7803db2be73d3 | D -> Nội soi ổ bụng ngay

### Group 450 — topic: Obstetrics and Gynecology
Q: Sau khi hút trứng, yếu tố quan trọng nhất để tiên l¬ượng bệnh là:
Options (shared set): ['Diễn tiến nồng độ hCG.', 'Hình ảnh mô học của mô trứng.', 'Nồng độ pregnandiol.', 'Nồng độ estriol.']
  line   3417 | Challenging | id 33c851fcd74740f0baa8ecc7fd3de6c9 | B -> Hình ảnh mô học của mô trứng.
  line   3895 | Challenging | id bd6026fce0644374bf40b583571b7978 | A -> Diễn tiến nồng độ hCG.

### Group 451 — topic: Obstetrics and Gynecology
Q: Theo vị trí giải phẩu, loại rau tiền đạo nào sau đây không có khả năng sanh đường âm đạo?
Options (shared set): ['Rau bám thấp', 'Rau bám bên', 'Rau bám mép', 'Rau bám bán trung tâm']
  line   3428 | Medium      | id 30db384134b7421498b7ca5e1c084478 | D -> Rau bám bán trung tâm
  line  11913 | Easy        | id d58c7632fc9d48199133bf6a8cc787dc | A -> Rau bám thấp

### Group 452 — topic: Obstetrics and Gynecology
Q: Tất cả những câu sau đây về nhau tiền đạo đều đúng, NGOẠI TRỪ:
Options (shared set): ['Thể nhau tiền đạo trung tâm thường gây chảy máu trầm trọng hơn thể nhau bám thấp.', 'Ngoài gây chảy máu trước sanh, còn có nguy cơ gây băng huyết sau sanh.', 'Thường gặp ở các sản phụ lớn tuổi, đa sản, có tiền căn nạo thai nhiều lần.', 'Nói chung, tỉ lệ sanh ngả âm đạo trong nhau tiền đạo cao hơn tỉ lệ mổ lấy thai.']
  line   3429 | Medium      | id b397203c48c243a9899296dc056ea2b9 | D -> Nói chung, tỉ lệ sanh ngả âm đạo trong nhau tiền đạo cao hơn tỉ lệ mổ lấy thai.
  line   7554 | Challenging | id 5315a49ce74e4155b25e16ead83eff8d | D -> Nói chung, tỉ lệ sanh ngả âm đạo trong nhau tiền đạo cao hơn tỉ lệ mổ lấy thai.

### Group 453 — topic: Obstetrics and Gynecology
Q: Thái độ xử trí trong phong huyết tử cung rau là:
Options (shared set): ['Hồi sức mẹ, cho thai ra càng sớm càng tốt.', 'Hồi sức mẹ, hồi sức thai, đẻ chỉ huy.', 'Truyền fibrinogen ,bấm ối, theo dõi thêm ,', 'Hồi sức mẹ, mổ lấy thai, cắt tử cung tùy tổn thương.']
  line   3474 | Medium      | id 1bbe670f281a4c2daa6d80dff8b5da9e | D -> Hồi sức mẹ, mổ lấy thai, cắt tử cung tùy tổn thương.
  line  11916 | Medium      | id 79183ec4309a427a8b0e4f8a55565d6b | D -> Hồi sức mẹ, mổ lấy thai, cắt tử cung tùy tổn thương.

### Group 454 — topic: Obstetrics and Gynecology
Q: Triệu chứng nào sau đây không phải là tác dụng của viên thuốc tránh thai:
Options (shared set): ['Nám mặt', 'Tăng cân', 'Đau bụng', 'Buồn nôn']
  line   3510 | Easy        | id c0e70beb375e47e9854951a9c8cddc8a | C -> Đau bụng
  line   7095 | Medium      | id e92357970be74efbab331a0f24533793 | C -> Đau bụng

### Group 455 — topic: Obstetrics and Gynecology
Q: Các mạch máu rốn được nuôi dưỡng bằng :
Options (shared set): ['Tự thẩm thấu trong lòng mạch', 'Nước ối', 'Thạch Wharton', 'Các mao mạch từ mạch máu rốn']
  line   3521 | Easy        | id 58ea184c87fa4f50b72a2288ac96a761 | C -> Thạch Wharton
  line   7493 | Easy        | id c04781b8e199480fbb1d768f0db611f7 | C -> Thạch Wharton

### Group 456 — topic: Obstetrics and Gynecology, Endocrinology
Q: Chức năng quan trọng của progesteron là gì?
Options (shared set): ['Tạo các đặc tính nữ', 'Bảo vệ tim mạch ở phụ nữ mãn kinh', 'Làm dày lớp niêm mạc tử cung', 'Ngăn ngừa rụng trứng']
  line   3548 | Easy        | id a3163c4c24324554bf6238077a2b75a5 | C -> Làm dày lớp niêm mạc tử cung
  line   6214 | Easy        | id 8b1d0785f0184b03be9177fe2bd6e213 | C -> Làm dày lớp niêm mạc tử cung

### Group 457 — topic: Obstetrics and Gynecology, Endocrinology
Q: HCG được bài tiết:
Options (shared set): ['Từ lúc trứng được thụ tinh, nồng độ tăng dần và cao nhất vào tháng cuối rồi giảm trước khi đẻ.', 'Từ ngày thứ 8 kể từ ngày rụng trứng, nồng độ tăng dần, cao nhất vào tháng thứ 2-3 sau đó giảm dần cho đến khi đẻ.', 'Từ ngày thứ 8 kể từ ngày rụng trứng, nồng độ tăng dần, cao nhất vào tháng thứ 4-5 sau đó giảm dần cho đến khi đẻ.', 'Từ ngày thứ 8 kể từ ngày rụng trứng, nồng độ tăng dần, cao nhất vào tháng thứ 2-3 sau đó giảm dần đến tháng thứ 4-5 nồng độ còn rất thấp và mất đi ít ngày trước khi đẻ.']
  line   3549 | Easy        | id 3014ef0c0e034ebc8f7259c93834ed22 | D -> Từ ngày thứ 8 kể từ ngày rụng trứng, nồng độ tăng dần, cao nhất vào tháng thứ 2-3 sau đó giảm dần đến tháng thứ 4-5 nồng độ còn rất thấp và mất đi ít ngày trước khi đẻ.
  line   6557 | Medium      | id fea1d912697a48f3b513fdc1c1c5406c | D -> Từ ngày thứ 8 kể từ ngày rụng trứng, nồng độ tăng dần, cao nhất vào tháng thứ 2-3 sau đó giảm dần đến tháng thứ 4-5 nồng độ còn rất thấp và mất đi ít ngày trước khi đẻ.
  line   6709 | Medium      | id 1f545943678f493bb10e750a6e4d1f8e | D -> Từ ngày thứ 8 kể từ ngày rụng trứng, nồng độ tăng dần, cao nhất vào tháng thứ 2-3 sau đó giảm dần đến tháng thứ 4-5 nồng độ còn rất thấp và mất đi ít ngày trước khi đẻ.

### Group 458 — topic: Obstetrics and Gynecology, Endocrinology
Q: 21. Một ví dụ về điều hòa ngược dương tính:
Options (shared set): ['Điều nhiệt', 'Điều hòa nồng độ glucose/máu', 'Sổ thai', 'Điều hòa nồng độ calci/máu']
  line   3550 | Medium      | id b0f22c2c07ef46da8e9d254fc655a59d | C -> Sổ thai
  line   6647 | Medium      | id 544a61f67fe64884bf405d98737868b2 | C -> Sổ thai

### Group 459 — topic: Obstetrics and Gynecology, Endocrinology
Q: Progesteron là hormon dưỡng thai vì:
Options (shared set): ['Phát triển niêm mạc tử cung trong phù hợp để trứng đã thụ tinh dễ làm tổ ở niêm mạc tử cung.', 'Phát triển mạch máu do đó làm tăng lượng máu đến nuôi thai.', 'Giảm co bóp cơ tử cung.', 'Bài tiết dịch có nhiều chất dinh dưỡng nuôi thai.']
  line   3551 | Medium      | id eacec978c0214a6193e7c1f916e08c2d | C -> Giảm co bóp cơ tử cung.
  line   6728 | Medium      | id 13b5fb93d4f74510a3071cde8adf8076 | C -> Giảm co bóp cơ tử cung.

### Group 460 — topic: Obstetrics and Gynecology, Endocrinology
Q: Estrogen có tác dụng trong mỗi chu kỳ kinh nguyệt:
Options (shared set): ['Tạo feedback dương dẫn tới chín và phóng noãn.', 'Làm giảm co bóp cơ tử cung.', 'Tái tạo và phát triển lớp niêm mạc nền tử cung.', 'Gây hiện tượng tăng thân nhiệt.']
  line   3552 | Medium      | id f8c7adfc98684c1094b595f47e9fcbd8 | A -> Tạo feedback dương dẫn tới chín và phóng noãn.
  line   6729 | Medium      | id 2c2b91606ea74f90a77feb69786f4be6 | A -> Tạo feedback dương dẫn tới chín và phóng noãn.

### Group 461 — topic: Obstetrics and Gynecology, Endocrinology
Q: Chọn một câu đúng nhất trong những câu sau về nguyên nhân gây ra chuyển dạ:
Options (shared set): ['Chuyển dạ xảy ra là do sự căng quá mức của cơ tử cung', 'Nguyên nhân chính gây ra chuyển dạ là sự giảm đột ngột của 2 nội tiết Estrogen và Progesteron', 'Các chất Prostaglandin có vai trò chính gây ra chuyển dạ', 'Các chất Prostaglandin có vai trò cơ bản trong một chuỗi các cơ chế gây chuyển dạ']
  line   3553 | Medium      | id 4cf695f99b2e4ab7b3ce3ccb48bb4beb | D -> Các chất Prostaglandin có vai trò cơ bản trong một chuỗi các cơ chế gây chuyển dạ
  line   7061 | Medium      | id 469274b6852241a7b04cd925059d72f3 | D -> Các chất Prostaglandin có vai trò cơ bản trong một chuỗi các cơ chế gây chuyển dạ

### Group 462 — topic: Obstetrics and Gynecology, Endocrinology
Q: Sự sản xuất prostaglandin trong thai kỳ đạt tỷ lệ cao nhất vào thời điểm:
Options (shared set): ['Trong 3 tháng đầu', 'Trong 3 tháng giữa', 'Trong 3tháng cuối', 'Bắt đầu chuyển dạ']
  line   3554 | Medium      | id 7e7c377b3ec94796a56553cc70d32047 | D -> Bắt đầu chuyển dạ
  line   7062 | Medium      | id 64971f8ea2664b9ba011adae74172ee7 | D -> Bắt đầu chuyển dạ

### Group 463 — topic: Obstetrics and Gynecology, Endocrinology
Q: Progesteron liều cao dùng trong trường hợp doạ sẩy có thể:
Options (shared set): ['Giúp cho nhau tiếp tục hoạt động tốt', 'Kích thích hoàng thể thai kỳ hoạt đông tốt hơn', 'Giúp cho phôi thai tiếp tục phát triển', 'Nếu thai chết thì có thể lưu lại lâu trong buồng tử cung.']
  line   3555 | Medium      | id d840f95dc7f849f58232aa55ddf258c2 | D -> Nếu thai chết thì có thể lưu lại lâu trong buồng tử cung.
  line   7064 | Medium      | id 2b190c8f74c3431695ff47eda5a1827e | D -> Nếu thai chết thì có thể lưu lại lâu trong buồng tử cung.

### Group 464 — topic: Obstetrics and Gynecology, Endocrinology
Q: Sử dụng đơn độc nội tiết nào sau đây có thể làm tăng nguy cơ chửa ngoài tử cung:
Options (shared set): ['Estrogen.', 'Progesteron.', 'Androgen.', 'Growth hormone']
  line   3556 | Medium      | id b170fab1187045879b0f97fbe25c363d | B -> Progesteron.
  line   6196 | Medium      | id bcbe7c682cef4c4a8c8f26cb05e63183 | B -> Progesteron.
  line   7065 | Medium      | id 35140ffd3545427f8f3202dd369e46b2 | B -> Progesteron.

### Group 465 — topic: Obstetrics and Gynecology, Endocrinology
Q: Trong trường hợp thai trứng thì:
Options (shared set): ['hCG tăng và hPL tăng', 'hCG tăng và hPL giảm', 'hCG giảm và hPL tăng', 'hCG giảm và hPL giảm']
  line   3557 | Medium      | id 55b188b2718f4517b9ea1d1fbf2b84c3 | B -> hCG tăng và hPL giảm
  line   7066 | Medium      | id 3389f2165ac947be8be8ddc4f4a03621 | B -> hCG tăng và hPL giảm
  line   7132 | Medium      | id 6149a229c4f84e29a078d6c6eebd0c55 | B -> hCG tăng và hPL giảm

### Group 466 — topic: Obstetrics and Gynecology, Endocrinology
Q: Về ý nghĩa của các dạng biểu đồ thân nhiệt, chọn câu đúng:
Options (shared set): ['Một biểu đồ thân nhiệt bất thường chứng tỏ có sự rối loạn chức năng ở buồng trứng', 'Nếu thân nhiệt ở giai đoạn sau lên xuống bất thường chứng tỏ có một tình trạng nhiễm trùng ở cơ quan sinh dục', 'Nếu sự gia tăng thân nhiệt kéo dài hơn 14 ngày phải nghĩ đến khả năng có thai', 'Dù có dạng 2 pha nhưng nếu pha noãn kéo dài chứng tỏ có suy hoàng thể']
  line   3558 | Medium      | id b830c4f16c5c4734b5d3c2d42c7d866b | C -> Nếu sự gia tăng thân nhiệt kéo dài hơn 14 ngày phải nghĩ đến khả năng có thai
  line   7068 | Medium      | id 978101bbcfc3428fa2df16b4a43954e3 | C -> Nếu sự gia tăng thân nhiệt kéo dài hơn 14 ngày phải nghĩ đến khả năng có thai
  line   7107 | Medium      | id 50ec93512ce54469af85ae9d7172a346 | C -> Nếu sự gia tăng thân nhiệt kéo dài hơn 14 ngày phải nghĩ đến khả năng có thai

### Group 467 — topic: Obstetrics and Gynecology, Endocrinology
Q: Khi nghiên cứu chất nhầy cổ tử cung ta có thể đánh giá được:
Options (shared set): ['Nhiểm trùng âm đạo cổ tử cung hay không', 'Đánh giá ảnh hưởng của Oestrogen ngay trước ngày phóng noãn', 'Đánh giá tác động của progesteron', 'A, B, C đúng']
  line   3559 | Medium      | id a91445f4e9084372948656b43c6fcd62 | D -> A, B, C đúng
  line   7070 | Medium      | id ee7808245333499786bc3a29e74dc90e | D -> A, B, C đúng
  line   7109 | Medium      | id fabdc5835f27406d82bb4335f650b9b2 | D -> A, B, C đúng
  line   7113 | Medium      | id 7d774007c5b943bb808d1850eaee4b61 | D -> A, B, C đúng

### Group 468 — topic: Obstetrics and Gynecology, Endocrinology
Q: Thời điểm để định lượng Hormon căn bản là:
Options (shared set): ['Trong nửa đầu của chu kỳ kinh', 'Từ ngày thứ 1 đến ngày thứ 4 của chu kỳ kinh', 'Giữa chu kỳ kinh', 'Nửa cuối chu kỳ kinh']
  line   3561 | Medium      | id 0a69713a1c83474f808e3fa1171680b2 | B -> Từ ngày thứ 1 đến ngày thứ 4 của chu kỳ kinh
  line   7072 | Medium      | id d1fa78fb167449e3bea7863ebe500278 | B -> Từ ngày thứ 1 đến ngày thứ 4 của chu kỳ kinh
  line   7110 | Medium      | id f0047771c9db4b488b6977590405aa97 | B -> Từ ngày thứ 1 đến ngày thứ 4 của chu kỳ kinh
  line   7114 | Medium      | id 673d7dc6ce7c4b79903f0cbb73ba617b | B -> Từ ngày thứ 1 đến ngày thứ 4 của chu kỳ kinh

### Group 469 — topic: Obstetrics and Gynecology, Endocrinology
Q: Một phụ nữ 35 tuổi khoẻ mạnh bình thường, vài tháng gần đây thấy thị lực giảm dần, vú tiết dịch, kinh nguyệt thưa và ít. Nội tiết đầu tiên cần thăm dò định lượng là:
Options (shared set): ['Estrogen / huyết thanh', 'Progesteron / huyết thanh', 'Protein / huyết thanh', 'Prolactin / huyết thanh']
  line   3563 | Challenging | id 5d6a6b1a058245df9a75f57fb6478493 | D -> Prolactin / huyết thanh
  line   6177 | Challenging | id 804b3f1b606e4a728e5f1d217a082091 | D -> Prolactin / huyết thanh
  line   6191 | Challenging | id b7096466ce0c4202a4d74c4752ce143a | D -> Prolactin / huyết thanh

### Group 470 — topic: Obstetrics and Gynecology, Endocrinology
Q: U xơ tử cung chịu ảnh hưởng trực tiếp của hormone:
Options (shared set): ['Estrogen', 'FSH', 'LH', 'GnRH']
  line   3564 | Medium      | id 208b26c9f8214db2b1027fb07bde71b7 | A -> Estrogen
  line   7075 | Medium      | id e46307623205441abdbb45b277a237c3 | A -> Estrogen

### Group 471 — topic: Obstetrics and Gynecology, Endocrinology
Q: 15. Tình trạng cường estrogen sẽ làm cho nhân xơ tử cung:
Options (shared set): ['Thoái hóa nước', 'Tăng kích thước', 'Ung thư hóa', 'Giảm kích thước']
  line   3565 | Medium      | id 1b740ba9807a4e379eb34a3120716e9b | B -> Tăng kích thước
  line   7076 | Medium      | id 483adb9ec110489a98b6dfc18189cd20 | B -> Tăng kích thước

### Group 472 — topic: Obstetrics and Gynecology, Endocrinology
Q: U xơ tử cung có liên quan đến hormone sinh dục nên . . .:
Options (shared set): ['U xơ tử cung chỉ lớn lên khi chu kỳ có rụng trứng', 'U xơ tử cung sẽ nhỏ đi khi bệnh nhân bị phẫu thuật cắt 2 buồng trứng', 'U xơ tử cung sẽ tăng kích thước ở những bệnh nhân có chu kỳ kinh đều hơn là bệnh nhân có chu kỳ kinh không đều', 'Khi có thai, u xơ tử cung có xu hướng nhỏ lại']
  line   3566 | Medium      | id 566812ae558c47208c08c1b24c55533d | B -> U xơ tử cung sẽ nhỏ đi khi bệnh nhân bị phẫu thuật cắt 2 buồng trứng
  line   7077 | Medium      | id 1ed6c7fd09d34c20981286d6567d2386 | A -> U xơ tử cung chỉ lớn lên khi chu kỳ có rụng trứng

### Group 473 — topic: Obstetrics and Gynecology, Endocrinology
Q: U xơ tử cung chịu tác động của hormone:
Options (shared set): ['Oxytocin', 'FSH', 'Estrogen', 'Tất cả đều sai']
  line   3567 | Medium      | id d65f56ea8d9747fd93a66dcafefeecdc | C -> Estrogen
  line   7078 | Medium      | id e2fd211c67734872ae924b8b1cc38f58 | C -> Estrogen

### Group 474 — topic: Obstetrics and Gynecology, Endocrinology
Q: U xơ tử cung chịu ảnh hưởng trực tiếp của hormone:
Options (shared set): ['LH', 'FSH', 'Progesterone', 'GnRH']
  line   3568 | Medium      | id 38cad3eeb93744729453bb9a9abd05e2 | C -> Progesterone
  line   7079 | Medium      | id 892da73fc9f644b88f72f2a587d66365 | C -> Progesterone

### Group 475 — topic: Obstetrics and Gynecology, Endocrinology
Q: Nói về tác động của hormone (nội tiết tố):
Options (shared set): ['U xơ tử cung chỉ chịu tác động của nội tiết tố ngoại sinh', 'Estrogen có thể làm tăng kích thước của u xơ', 'Prolactin có thể làm giảm kích thước của u xơ', 'Thuốc đối kháng GnRh có thể làm tăng kích thước khối u']
  line   3569 | Medium      | id 6191559f2a754ae0ad3568365b11469d | B -> Estrogen có thể làm tăng kích thước của u xơ
  line   7080 | Medium      | id d3ba7929de7c4b4198bbd00a05791543 | B -> Estrogen có thể làm tăng kích thước của u xơ

### Group 476 — topic: Obstetrics and Gynecology, Endocrinology
Q: Rong kinh, rong huyết tuổi trẻ:
Options (shared set): ['Thường gặp ở tuổi dậy thì Nguyên nhân do cường Estrogen', 'Do nồng độ Progesterone trong máu thấp', 'Thường gặp ở chu ký kinh có phóng noãn', 'và B đúng']
  line   3570 | Medium      | id bce2a481c2894ec4904606966b1cfa5d | A -> Thường gặp ở tuổi dậy thì Nguyên nhân do cường Estrogen
  line   7081 | Medium      | id 1f09cb12354e45ca9c3c0a11cf0ffcb1 | A -> Thường gặp ở tuổi dậy thì Nguyên nhân do cường Estrogen

### Group 477 — topic: Obstetrics and Gynecology, Endocrinology
Q: Khối u buồng trứng gây triệu chứng rối loạn kinh nguyệt thường do:
Options (shared set): ['U nang nước', 'U nang nhầy', 'U nang bì', 'U nội tiết']
  line   3571 | Medium      | id f3c655f45b4b4621a08b50baa0768eec | D -> U nội tiết
  line   7082 | Medium      | id 84525e02af0940cc8259d9b0ca5cea09 | D -> U nội tiết
  line   7117 | Medium      | id fec1760003df4f52acfccc8285f37fa3 | D -> U nội tiết
  line   8313 | Medium      | id b4ab0fd26c0844d29602dba7e6ae9185 | D -> U nội tiết

### Group 478 — topic: Obstetrics and Gynecology, Endocrinology
Q: Chọn xét nghiệm tin cậy nhất để xác định sự có mặt của hCG:
Options (shared set): ['Xét nghiệm nước tiểu định lượng hCG bằng phương pháp sinh vật', 'Xét nghiệm nước tiểu định lượng hCG bằng phương pháp miễn dịch', 'Xét nghiệm máu định lượng hCG bằng phương pháp miễn dịch', 'Cả 3 loại xét nghiệm đều có độ tin cậy ngang nhau']
  line   3572 | Medium      | id 401afd938c5446dd84439357b52ed245 | C -> Xét nghiệm máu định lượng hCG bằng phương pháp miễn dịch
  line   7084 | Medium      | id 8e202c3ba9674827aa66fbb1995a1ae6 | C -> Xét nghiệm máu định lượng hCG bằng phương pháp miễn dịch

### Group 479 — topic: Obstetrics and Gynecology, Endocrinology
Q: Đối với thai chết lưu dưới 8 tuần, tất cả các triệu chứng sau đều đúng, NGOẠI TRỪ:
Options (shared set): ['Ra máu âm đạo đỏ thẫm, dai dẳng, liên tục', 'Khối lượng tử cung có thể bình thường', 'Siêu âm chưa có âm vang thai', 'Định lượng ßhCG sau 48 giờ tăng gấp hai lần']
  line   3573 | Medium      | id 40a8e32608ab401eb9bc0cd9cf1f4f02 | D -> Định lượng ßhCG sau 48 giờ tăng gấp hai lần
  line   7085 | Medium      | id 685e8b8f72ba4defadd807ee18188eef | D -> Định lượng ßhCG sau 48 giờ tăng gấp hai lần
  line   8157 | Challenging | id 9c8e5f6351c54493b55c42c3f61498ee | D -> Định lượng ßhCG sau 48 giờ tăng gấp hai lần

### Group 480 — topic: Obstetrics and Gynecology, Endocrinology
Q: Mãn kinh sớm là không có kinh trước
Options (shared set): ['35 tuổi', '40 tuổi', '45 tuổi', 'Từ 45 tuổi đến 50 tuổi']
  line   3574 | Easy        | id 468cdd2fa83249a2b0346467978cd30c | B -> 40 tuổi
  line   6367 | Easy        | id 6e44b048b8b44f149389cb6cad87e2f8 | B -> 40 tuổi

### Group 481 — topic: Obstetrics and Gynecology, Endocrinology
Q: Nguyên nhân của vòng kinh không phóng noãn chủ yếu do:
Options (shared set): ['Thời gian hoàng thể kéo dài.', 'Suy buồng trứng.', 'Không có mặt của estrogene mà có sự thay đổi nồng độ của progesterone.', 'Không có mặt của progesterone mà có sự thay đổi nồng độ của estrogene.']
  line   3575 | Medium      | id 79b8aa3034cc49bda802802735335640 | D -> Không có mặt của progesterone mà có sự thay đổi nồng độ của estrogene.
  line   7088 | Medium      | id 7fbbc10a311d464fbf23ee03d0a85035 | D -> Không có mặt của progesterone mà có sự thay đổi nồng độ của estrogene.

### Group 482 — topic: Obstetrics and Gynecology, Endocrinology
Q: Chọn một câu đúng sau đây về tình trạng vô kinh:
Options (shared set): ['Gọi là vô kinh nguyên phát khi đến 18 tuổi vẫn chưa có kinh.', 'Gọi là vô kinh giả khi nguyên nhân từ buồng trứng chứ không phải từ tử cung.', 'Một nguyên nhân có thể có là do cường vỏ thượng thận.', 'Chỉ có thể điều trị bằng nội tiết.']
  line   3576 | Medium      | id 25ce3c6a062b4acf9d3480e984cbb4a5 | C -> Một nguyên nhân có thể có là do cường vỏ thượng thận.
  line   7089 | Medium      | id 0db6a03def07475f87aea516ba44f244 | C -> Một nguyên nhân có thể có là do cường vỏ thượng thận.

### Group 483 — topic: Obstetrics and Gynecology, Endocrinology
Q: Trong trường hợp đa kinh (kinh mau), hướng điều trị là?
Options (shared set): ['Dùng estrogen đầu chu kỳ kinh, khi sắp có kinh dùng thêm progesterone.', 'Dùng progesterone đầu chu kỳ kinh, sắp có kinh dùng thêm estrogen.', 'Dùng estrogen vào khoảng giữa chu kỳ kinh.', 'Dùng progesterone khoảng giữa chu kỳ kinh.']
  line   3577 | Challenging | id b6c326a6a2854c4cb5d4451b4bb9d509 | A -> Dùng estrogen đầu chu kỳ kinh, khi sắp có kinh dùng thêm progesterone.
  line   6179 | Medium      | id 96fbd05aa6ec406e8095b346ed27a57a | A -> Dùng estrogen đầu chu kỳ kinh, khi sắp có kinh dùng thêm progesterone.
  line   8972 | Hard        | id 32c9bda5c1934c3096b46ed19b39b4ce | A -> Dùng estrogen đầu chu kỳ kinh, khi sắp có kinh dùng thêm progesterone.

### Group 484 — topic: Obstetrics and Gynecology, Endocrinology
Q: Sự xuất hiện kinh nguyệt hàng tháng ở phụ nữ ở tuổi sinh đẻ có thể chỉ cần:
Options (shared set): ['Giảm progesteron', 'Giảm estrogen và progesteron', 'Tăng progesteron', 'Tăng estrogen']
  line   3578 | Medium      | id 064231890019456bbe0d365723838782 | B -> Giảm estrogen và progesteron
  line   7090 | Medium      | id c62873927af64e46b8bd3cb668b29749 | B -> Giảm estrogen và progesteron

### Group 485 — topic: Obstetrics and Gynecology, Endocrinology
Q: Hành kinh là do:
Options (shared set): ['Tăng FSH', 'Tăng LH', 'Giảm Gn-RH', 'Giảm đột ngột Estrogen và Progesteron']
  line   3579 | Medium      | id 238408858f6f4833ae03ff01bf859a8a | D -> Giảm đột ngột Estrogen và Progesteron
  line   7092 | Medium      | id 4a05fbc6c2154d719bb8d2a20c58f12f | D -> Giảm đột ngột Estrogen và Progesteron

### Group 486 — topic: Obstetrics and Gynecology, Endocrinology
Q: Cơ chế tránh thai của viên thuốc ngừa thai loại phối hợp là:
Options (shared set): ['Ức chế rụng trứng và làm đặc chất nhầy cổ tử cung', 'Gây phản ứng viêm tại nội mạc tử cung', 'Tăng nhu động của vòi trứng', 'Diệt tinh trùng và trứng']
  line   3580 | Medium      | id 5520a1ef73d64bcba58dab738b5a7826 | A -> Ức chế rụng trứng và làm đặc chất nhầy cổ tử cung
  line   7093 | Medium      | id 281004b0cde74c64a89c452f82352e5d | A -> Ức chế rụng trứng và làm đặc chất nhầy cổ tử cung
  line   7134 | Medium      | id 29b3ec7086844b0c894c2006bbc0feaf | A -> Ức chế rụng trứng và làm đặc chất nhầy cổ tử cung

### Group 487 — topic: Obstetrics and Gynecology, Endocrinology
Q: Tác dụng chính của thuốc ngừa thai kết hợp là:
Options (shared set): ['Tác dụng chủ yếu đến niêm mạc tử cung', 'Tác dụng đến niêm dịch cổ tử cung', 'Tác dụng ức chế phóng noãn', 'Ngăn cản sự di chuyển của tinh trùng']
  line   3581 | Medium      | id fa7ae2a1e7a1456a8dfecc7d813dd0e2 | C -> Tác dụng ức chế phóng noãn
  line   7094 | Medium      | id ad6860644d404037902666885572b1b8 | C -> Tác dụng ức chế phóng noãn
  line   7135 | Medium      | id 96953fd985f94f08acae9eee4f473da3 | C -> Tác dụng ức chế phóng noãn

### Group 488 — topic: Obstetrics and Gynecology, Endocrinology
Q: Rigevidon là thuốc ngừa thai uống dạng:
Options (shared set): ['Chứa Progesteron đơn thuần', 'Viên thuốc kết hợp', 'Tthuốc 3 pha', 'Loại kế tiếp']
  line   3582 | Easy        | id 43f526d221e54218803c89575ce384fa | B -> Viên thuốc kết hợp
  line   6369 | Easy        | id 31f38fd076f84bc387172ec6d729e39d | B -> Viên thuốc kết hợp

### Group 489 — topic: Obstetrics and Gynecology, Endocrinology
Q: Cơ chế tránh thai của biện pháp cho bú vô kinh là:
Options (shared set): ['Tác dụng lên vùng dưới đồi, gây vô kinh', 'Tác dụng lên vùng dưới đồi, ảnh hưởng đến sự tiết các hormon của buồng trứng, ức chế sự rụng trứng', 'Tác dụng lên vùng dưới đồi, ảnh hưởng đến sự tiết các hormon giải phóng, ức chế sự rụng trứng', 'Tác dụng lên vùng dưới đồi, gây rối loạn kinh nguyệt, ức chế rụng trứng']
  line   3583 | Medium      | id 895ae5d964a640e18464bab09d8d0edd | C -> Tác dụng lên vùng dưới đồi, ảnh hưởng đến sự tiết các hormon giải phóng, ức chế sự rụng trứng
  line   7096 | Medium      | id a986e91752e6461689f7c30cc61fb765 | C -> Tác dụng lên vùng dưới đồi, ảnh hưởng đến sự tiết các hormon giải phóng, ức chế sự rụng trứng

### Group 490 — topic: Obstetrics and Gynecology, Endocrinology
Q: Viên thuốc tránh thai Progestin đơn thuần liều thấp phù hợp nhất đối với:
Options (shared set): ['Chủ yếu với mục đích điều trị', 'Phụ nữ muốn tránh thai tạm thời', 'Phụ nữ đang cho con bú', 'Phụ nữ không sử dụng được viên tránh thai phối hợp']
  line   3584 | Challenging | id 8c8fc1624bb643c2819c6725dd32baa7 | C -> Phụ nữ đang cho con bú
  line   6183 | Medium      | id 132e50b27d454448b9d1a68d22dc7b66 | C -> Phụ nữ đang cho con bú

### Group 491 — topic: Obstetrics and Gynecology, Endocrinology
Q: Tác dụng phụ của viên thuốc tránh thai phối hợp là, NGOẠI TRỪ:
Options (shared set): ['Nhức đầu, thay đổi tâm lý, libido.', 'Cảm giác nặng chân gặp ở một vài phụ nữ.', 'Cao huyết áp, tăng cân do giữ muối, giữ nước.', 'Gây rối loạn kinh nguyệt: kinh ít, kinh thưa, dùng lâu gây mất kinh']
  line   3585 | Challenging | id 22c4f58b12fb4c2fa942d3d51fdcef4e | D -> Gây rối loạn kinh nguyệt: kinh ít, kinh thưa, dùng lâu gây mất kinh
  line   6184 | Medium      | id 1f5b52fb1843489aa1214fcba6d22926 | D -> Gây rối loạn kinh nguyệt: kinh ít, kinh thưa, dùng lâu gây mất kinh

### Group 492 — topic: Obstetrics and Gynecology, Endocrinology
Q: Cách sử dụng viên thuốc tránh thai phối hợp vỉ 28 viên có hàm lượng Ê 30mg NGOẠI TRỪ
Options (shared set): ['Uống viên thứ nhất sau khi sạch kinh 5 ngày', 'Uống vào một giờ nhất định trong ngày', 'Nếu quên 2 viên thì ngừng thuốc và dùng biện pháp khác', 'Uống viên đầu tiên vào ngày thứ 1 của chu kỳ']
  line   3586 | Challenging | id 4fca41995b044601bced26ff4180281d | A -> Uống viên thứ nhất sau khi sạch kinh 5 ngày
  line   6185 | Medium      | id 82a1d0a2378447e480b246a577acc76d | A -> Uống viên thứ nhất sau khi sạch kinh 5 ngày

### Group 493 — topic: Obstetrics and Gynecology, Endocrinology
Q: Chọn một câu sai sau đây về thuốc viên tránh thai loại phối hợp:
Options (shared set): ['Có chống chỉ định ở người bị bệnh tim', 'Ngoài tác dụng tránh thai, có thể dùng cho người bị đau bụng kinh vì có thể làm giảm được triệu chứng này', 'Có chống chỉ định ở người bị u vú', 'Có chống chỉ định ở phụ nữ có u buồng trứng nhỏ, nghi là u cơ năng']
  line   3587 | Medium      | id 5c35d512640d44d581106ead7af2f41f | D -> Có chống chỉ định ở phụ nữ có u buồng trứng nhỏ, nghi là u cơ năng
  line   7097 | Medium      | id b1b2b8de2493424093860b56ee8de5ff | D -> Có chống chỉ định ở phụ nữ có u buồng trứng nhỏ, nghi là u cơ năng

### Group 494 — topic: Obstetrics and Gynecology, Endocrinology
Q: Rong kinh, rong huyết tuổi trẻ:
Options (shared set): ['Thường gặp ở tuổi dậy thì Nguyên nhân do cường Estrogen', 'Do nồng độ Progesterone trong máu thấp', 'Thường gặp ở chu ký kinh có phóng noãn', 'A và B đúng']
  line   3588 | Medium      | id 362608c2df3f41a2a01b8be954ed1659 | A -> Thường gặp ở tuổi dậy thì Nguyên nhân do cường Estrogen
  line   7098 | Medium      | id 7a3f1e9511f34a89b2eeb7154c95a3ba | A -> Thường gặp ở tuổi dậy thì Nguyên nhân do cường Estrogen

### Group 495 — topic: Obstetrics and Gynecology, Endocrinology
Q: Xét nghiệm tế bào học nội tiết nhằm mục đích, chọn câu đúng nhất:
Options (shared set): ['Đánh giá tác dụng của progesteron', 'Đánh giá tác dụng của oestrogen', 'Đánh giá tác dụng của của progesteron và oestrogen', 'Đánh giá tình trạng viêm nhiểm đường sinh dục']
  line   3589 | Medium      | id 6758d27359f84e7fa2e59c522b8b24e7 | C -> Đánh giá tác dụng của của progesteron và oestrogen
  line   7069 | Medium      | id 2d03e4098cfd4ef79b49e1df75750e16 | C -> Đánh giá tác dụng của của progesteron và oestrogen
  line   7108 | Medium      | id 7fc9ce777f6b4fa0bd22d9993a930f1c | C -> Đánh giá tác dụng của của progesteron và oestrogen
  line   7112 | Medium      | id 21e58b0d793947b584c5793bc91e1965 | C -> Đánh giá tác dụng của của progesteron và oestrogen

### Group 496 — topic: Obstetrics and Gynecology, Endocrinology
Q: Để đánh giá hoạt động nội tiết của buồng trứng và sự đáp ứng nội tiết của nội mạc tử cung, cần thực hiện sinh thiết nội mạc để làm GPBL vào khoảng ngày nào của chu kỳ kinh 28 ngày?
Options (shared set): ['Vào khoảng ngày thứ 7 đến 10 của chu kỳ kinh 28 ngày', 'Vào khoảng ngày thứ 13 đến 15 của chu kỳ kinh 28 ngày', 'Vào khoảng ngày thứ 17 đến 19 của chu kỳ kinh 28 ngày', 'Vào khoảng ngày thứ 21 đến 23 của chu kỳ kinh 28 ngày']
  line   3590 | Medium      | id a9e5ae7abf974bbfad624c7746c0a581 | D -> Vào khoảng ngày thứ 21 đến 23 của chu kỳ kinh 28 ngày
  line   7111 | Medium      | id 3dce5f7ff7544a95a0ebd8af0eb6de8b | D -> Vào khoảng ngày thứ 21 đến 23 của chu kỳ kinh 28 ngày

### Group 497 — topic: Obstetrics and Gynecology, Endocrinology
Q: Trước một trường hợp nghi có rối loạn phóng noãn, các xét nghiệm sau đây là cần thiết, NGOẠI TRỪ:
Options (shared set): ['Prolactine huyết tương.', 'Siêu âm với đầu dò đường âm đạo.', 'Biểu đồ thân nhiệt.', 'Testostérome, FSH, LH.']
  line   3591 | Challenging | id f8011f8f559044409c145bd9d596b77d | C -> Biểu đồ thân nhiệt.
  line   6192 | Challenging | id 5509a4006e9d43ee9c3b596a3254f9ec | C -> Biểu đồ thân nhiệt.

### Group 498 — topic: Obstetrics and Gynecology, Endocrinology
Q: Nội tiết được lựa chọn trong điều trị dọa sảy thai:
Options (shared set): ['Progesterone tổng hợp.', 'Estrogene thiên nhiên.', 'Estrogene tổng hợp.', 'Progesterone nhiên nhiên.']
  line   3592 | Medium      | id 5bbd55c3842e443bb31484be8208d944 | D -> Progesterone nhiên nhiên.
  line   7129 | Medium      | id bb7f5fd7aa594e09bd46bd06bc68b7de | D -> Progesterone nhiên nhiên.

### Group 499 — topic: Obstetrics and Gynecology, Endocrinology
Q: Nguyên nhân của sự xuất hiện nang hoàng tuyến trong chửa trứng:
Options (shared set): ['Do sự bất thường về nhiễm sắc thể', 'Gia tăng Follicle - stimulating hormmone.', 'Gia tăng Lutein - Hormon', 'Gia tăng chorionic gonadotropin']
  line   3593 | Medium      | id 4638da9f8c6549c298aead4bb36556b2 | D -> Gia tăng chorionic gonadotropin
  line   7130 | Medium      | id 9d09ad923b43483f845f25f257c0c1f8 | D -> Gia tăng chorionic gonadotropin

### Group 500 — topic: Obstetrics and Gynecology, Endocrinology
Q: Hiệu quả của viên tránh thai phối hợp cao chủ yếu là do:
Options (shared set): ['Progestin', 'Ức chế giải phóng LH nên ức chế phóng noãn.', 'Chất nhầy cổ tử cung đặc lại ảnh hưởng đến sự di chuyển của tinh trùng.', 'Estrogen và progestin đều có tác dụng đồng vận lên tuyến yên làm tăng hiệu quả tránh thai']
  line   3594 | Medium      | id ea7170157a434abf8fd1d25bcb832e9e | D -> Estrogen và progestin đều có tác dụng đồng vận lên tuyến yên làm tăng hiệu quả tránh thai
  line   6182 | Medium      | id cd9322c07b514065ba80f48e6cb7395f | D -> Estrogen và progestin đều có tác dụng đồng vận lên tuyến yên làm tăng hiệu quả tránh thai
  line   7136 | Medium      | id c08faa72e71444f99b251b89078a14cd | D -> Estrogen và progestin đều có tác dụng đồng vận lên tuyến yên làm tăng hiệu quả tránh thai

### Group 501 — topic: Obstetrics and Gynecology, Endocrinology, Oncology
Q: Chọn câu SAI trong những câu sau đây về thai trứng:
Options (shared set): ['Tỷ lệ cường giáp khoảng 30 %', '80 - 90 % tiến triển tốt sau nạo trứng', 'Xuất độ ở các nước Đông Nam Á cao hơn Châu Âu', 'Có thể có nồng độ hCG trong máu không cao']
  line   3595 | Medium      | id bcd65117b71444f1a27b66b590c28306 | A -> Tỷ lệ cường giáp khoảng 30 %
  line   7131 | Medium      | id 4e28493ca6544f298208dbf903046d71 | A -> Tỷ lệ cường giáp khoảng 30 %

### Group 502 — topic: Obstetrics and Gynecology, Endocrinology, Oncology
Q: Khi so sánh nồng độ Estrogen nước tiểu trong thai thường và thai trứng ta thấy:
Options (shared set): ['Estron, Estradiol và Estriol trong thai trứng đều thấp hơn trong thai thường', 'Estron, Estradiol và Estriol trong thai trứng đều cao hơn trong thai thường', 'Estron, Estradiol trong thai trứng cao hơn trong thai thường - Estriol thì ngược lại', 'Estron, Estradiol trong thai trứng thấp hơn trong thai thường - Estriol thì ngược lại']
  line   3596 | Challenging | id 8defb450084a42cfb27edac5bdd4c608 | A -> Estron, Estradiol và Estriol trong thai trứng đều thấp hơn trong thai thường
  line   6197 | Medium      | id 0b87930e0cef4da99b497b4a1e7a4a1f | A -> Estron, Estradiol và Estriol trong thai trứng đều thấp hơn trong thai thường
  line   7067 | Medium      | id 86718477e872447e96ef76087ef5ab22 | A -> Estron, Estradiol và Estriol trong thai trứng đều thấp hơn trong thai thường

### Group 503 — topic: Obstetrics and Gynecology, Endocrinology, Oncology
Q: Bệnh lý nào sau đây chống chỉ định dùng viên thuốc tránh thai loại phối hợp:
Options (shared set): ['Lao phổi', 'U thư đại tràng', 'U nang buồng trứng cơ năng', 'U tiết prolactine']
  line   3597 | Medium      | id c94d8b4a5cca41d28b0067dcb10d3e9e | D -> U tiết prolactine
  line   7138 | Medium      | id 73342762987e40ba8adc465a479b0484 | D -> U tiết prolactine

### Group 504 — topic: Obstetrics and Gynecology, Endocrinology, Pediatrics
Q: Vai trò dinh dưỡng của bánh rau, chọn một câu sai:
Options (shared set): ['Trao đổi nước và chất điện giải qua gai rau theo cơ chế thẩm thấu', 'Glucose, Lipid, Protein qua rau thai dễ', 'Tổng hợp các nội tiết tố Steroit', 'Câu a, c đúng']
  line   3598 | Medium      | id f79ea8a7d21d4bf29f81b8e6ca6214ff | B -> Glucose, Lipid, Protein qua rau thai dễ
  line   7139 | Medium      | id 770d921574a6492091a57700eb189e5e | B -> Glucose, Lipid, Protein qua rau thai dễ

### Group 505 — topic: Obstetrics and Gynecology, Geriatrics
Q: Nguy cơ lo ngại nhất của người phụ nữ trên 40 tuổi sinh con sẽ làm:
Options (shared set): ['Tăng nguy cơ đẻ khó', 'Tăng tỷ lệ mổ lấy thai', 'Tăng tỷ lệ bất thường cho trẻ em', 'Các câu trên đều đúng']
  line   3604 | Medium      | id f873e8b146a2444fb1740bc11e7a1d50 | D -> Các câu trên đều đúng
  line  10824 | Medium      | id a555d57365a4406c8a7c60d8c1989718 | D -> Các câu trên đều đúng

### Group 506 — topic: Obstetrics and Gynecology, Hematology
Q: Trên lâm sàng, rau tiền đạo chảy máu nhẹ là khi lượng máu của mẹ mất:
Options (shared set): ['<10% thể tích máu tuần hoàn', '<15% thể tích máu tuần hoàn', '<20% thể tích máu tuần hoàn', '<25% thể tích máu tuần hoàn']
  line   3613 | Medium      | id a83cb7446f9d407781b883866265f6af | B -> <15% thể tích máu tuần hoàn
  line  11799 | Medium      | id 9686c91f59d04872ab45e33768c30107 | A -> <10% thể tích máu tuần hoàn

### Group 507 — topic: Obstetrics and Gynecology, Infectious Diseases
Q: Thai chết lưu thường gặp trong những trường hợp:
Options (shared set): ['A. Mẹ mắc các bệnh lý mạn tính', 'B. Mẹ bị nhiễm khuẩn cấp tính', 'C. Mẹ có tiền sử đẻ nhiều lần', 'Cả câu A và B đúng']
  line   3658 | Medium      | id 93a2bced4d33487daabee6913ae58dcf | D -> Cả câu A và B đúng
  line  11924 | Easy        | id 062adaba606a4f1fac7d052110ed4721 | D -> Cả câu A và B đúng

### Group 508 — topic: Obstetrics and Gynecology, Infectious Diseases
Q: Khí hư trong viêm âm đạo do nấm có đặc điểm:
Options (shared set): ['Nhầy, lẫn mủ.', 'Loãng, có bọt.', 'Đặc, dính như hồ.', 'Xanh, lẫn mủ có mùi hôi.']
  line   3688 | Medium      | id fe8c5eed0dd44c949fa9de6118ae8664 | C -> Đặc, dính như hồ.
  line   8298 | Medium      | id 940f4ff2e1fa42a4b16acb3b0ecbb05a | C -> Đặc, dính như hồ.

### Group 509 — topic: Obstetrics and Gynecology, Infectious Diseases
Q: Nguyên nhân bị sùi mào gà âm hộ - âm đạo do:
Options (shared set): ['Nạo hút thai nhiều lần.', 'Môi trường nước sử dụng mất vệ sinh.', 'Viêm lộ tuyến cổ tử cung kéo dài, không điều trị triệt để.', 'Lây nhiễm qua đường tình dục.']
  line   3694 | Medium      | id 5c55fc449f0f4dc1ac2e50c5e5ce6cdd | D -> Lây nhiễm qua đường tình dục.
  line   3700 | Medium      | id b4392dcc126c4343bfe2d5f35fb100a7 | D -> Lây nhiễm qua đường tình dục.

### Group 510 — topic: Obstetrics and Gynecology, Infectious Diseases
Q: Các triệu chứng viêm âm đạo sau đây đều do nấm Candida, ngoại trừ:
Options (shared set): ['Khí hư khô đặc, đóng thành vẩy.', 'Ngứa rát âm hộ, âm đạo.', 'Đau khi giao hợp.', 'Cổ tử cung có nhiều đảo tuyến.']
  line   3699 | Medium      | id b39abfe2029548f7b6d8027248fd268a | D -> Cổ tử cung có nhiều đảo tuyến.
  line   3714 | Medium      | id ec16ea32f098405c85b0a890295fe2e0 | D -> Cổ tử cung có nhiều đảo tuyến

### Group 511 — topic: Obstetrics and Gynecology, Infectious Diseases
Q: Yếu tố thuận lợi gây tổn thương nghịch sản cổ tử cung là:
Options (shared set): ['Quan hệ tình dục', 'Rối loạn nội tiết', 'Sang chấn sản khoa', 'do HPV']
  line   3715 | Medium      | id 3925a56ee6ac4d5bb2e203ae452c4186 | D -> do HPV
  line   9103 | Challenging | id f2c0c1eb49094291af0a872e44c5a71b | D -> do HPV

### Group 512 — topic: Obstetrics and Gynecology, Infectious Diseases, Endocrinology
Q: Các yếu tố sau là nguy cơ gây viêm âm đạo-cổ tử cung, ngoại trừ:
Options (shared set): ['Dùng kháng sinh nhóm Beta-lactam', 'Dùng kháng sinh nhóm Tetracyclin', 'Dùng kháng sinh nhóm Quinolones', 'Bị đái tháo đường']
  line   3722 | Challenging | id 95ee81d4e95f42cfb18f48988bba45c4 | A -> Dùng kháng sinh nhóm Beta-lactam
  line   6190 | Medium      | id 98b8bcf5a5594f59a5f11d6967f184a7 | C -> Dùng kháng sinh nhóm Quinolones

### Group 513 — topic: Obstetrics and Gynecology, Infectious Diseases, Ophthalmology
Q: Sản phụ mắc bệnh lậu có thể gây ra hậu quả nghiêm trọng nào sau đây cho bé khi sinh qua đường âm đạo:
Options (shared set): ['Mắc bệnh lậu do mẹ truyền sang', 'Vô sinh sau này', 'Viêm kết mạc mắt do lậu gây mù', 'Không ảnh hưởng gì']
  line   3729 | Medium      | id d616dec15af84115b714085157518f20 | C -> Viêm kết mạc mắt do lậu gây mù
  line   4293 | Medium      | id 831bb84af1dc498d9b440d90e7a18aee | C -> Viêm kết mạc mắt do lậu gây mù

### Group 514 — topic: Obstetrics and Gynecology, Infectious Diseases, Pulmonology
Q: Dạng rối loạn kinh nguyệt thường thấy trong lao sinh dục là:
Options (shared set): ['Rong kinh.', 'Cường kinh.', 'Rong huyết.', 'Kinh ít và thưa.']
  line   3733 | Medium      | id 1d9cceb528bb4680944030e026624090 | D -> Kinh ít và thưa.
  line   5797 | Medium      | id f63a3e9f777c4008b5e1e69aac550897 | D -> Kinh ít và thưa.

### Group 515 — topic: Obstetrics and Gynecology, Oncology
Q: U nguyên bào nuôi di căn nhiều nhất ở:
Options (shared set): ['phổi', 'não', 'gan', 'thận']
  line   3762 | Medium      | id da9e54332a6b4362a74c9eea52636267 | A -> phổi
  line   3776 | Medium      | id 3d7a54415f254e648e93751caac78628 | A -> phổi

### Group 516 — topic: Obstetrics and Gynecology, Oncology
Q: U nào không thuộc u nguyên phát buồng trứng
Options (shared set): ['U Krukenberg', 'U Brenner', 'U tế bào Sertoli- leydig', 'Ung thư dạng nội mạc']
  line   3764 | Medium      | id 597c0c0bcfe84f71a2d59f917eb4d140 | A -> U Krukenberg
  line   9002 | Medium      | id df378e7620b14967af338ee5b99d31e2 | A -> U Krukenberg

### Group 517 — topic: Obstetrics and Gynecology, Oncology
Q: Trong phân loại u buồng trứng có nhiều típ mô học. Típ mô học nào sau đây thường gặp nhất?
Options (shared set): ['U quái', 'U thanh dịch', 'U nhầy', 'U nang buồng trứng']
  line   3767 | Easy        | id 1c015ad79287442393c16ff4a96afe78 | B -> U thanh dịch
  line   3831 | Medium      | id 83a8d404c11d4614a64df2930d3611d8 | B -> U thanh dịch

### Group 518 — topic: Obstetrics and Gynecology, Oncology
Q: Ung thư cổ tử cung có nguồn gốc từ?
Options (shared set): ['Tế bào biểu mô lát tầng ( cổ tử cung ngoài)', 'Tế bào biểu mô trụ ( cổ tử cung trong)', 'Tế bào nội mạc tử cung', 'Chọn A B']
  line   3771 | Medium      | id f81696dce7c444f1990ef429040db082 | D -> Chọn A B
  line   3848 | Medium      | id ea712812ac0a460a99d1d9f90bcfb0af | D -> Chọn A B

### Group 519 — topic: Obstetrics and Gynecology, Oncology
Q: Loại (typ) vi thể ung thư biểu mô tuyến nội mạc tử cung hay gặp?
Options (shared set): ['UTBM tuyến tế bào sáng', 'UTBM tuyến nội mạc tử cung', 'UTBM pha dạng biểu bì – tuyến', 'UTBM tuyến - nhú']
  line   3775 | Medium      | id 5cfa8c8232564e62aa128a2fed892eea | B -> UTBM tuyến nội mạc tử cung
  line   3850 | Medium      | id 0a9ad534750f4c07b34d3e98186bf247 | B -> UTBM tuyến nội mạc tử cung

### Group 520 — topic: Obstetrics and Gynecology, Oncology
Q: Ung thư nguyên bào nuôi là một u nguyên phát của:
Options (shared set): ['Màng rụng.', 'Tế bào nuôi.', 'Cơ tử cung.', 'Những tế bào sinh dục không biệt hoá.']
  line   3782 | Challenging | id 06a1952c8a2e4b09907603dda3122c3e | B -> Tế bào nuôi.
  line   3822 | Medium      | id 69c551a3536842eba0f5804e61777144 | B -> Tế bào nuôi.

### Group 521 — topic: Obstetrics and Gynecology, Oncology
Q: Vị trí di căn hay gặp nhất của ung thư nguyên bào nuôi là:
Options (shared set): ['Âm đạo.', 'Phổi.', 'Gan.', 'Buồng trứng.']
  line   3784 | Medium      | id dd434d9b4d7847daa92dd368c4faa5a1 | B -> Phổi.
  line   4012 | Medium      | id af098b3044054bbcb9395ff894a844bf | B -> Phổi.
  line   5821 | Easy        | id 9c6be6da2edf40c5a8b4c767021a2c89 | B -> Phổi.

### Group 522 — topic: Obstetrics and Gynecology, Oncology
Q: Trong tất cả những trường hợp rối loạn kinh nguyệt tuổi tiền mãn kinh đều phải nghi ngờ có nguyên nhân ác tính
Options (shared set): ['Đúng', 'Sai']
  line   3791 | Medium      | id bb1ccb1e083f433fa41c9714713dd2f1 | A -> Đúng
  line  10133 | Medium      | id ec52e5432ddb431fb9206b82d1ece263 | A -> Đúng

### Group 523 — topic: Obstetrics and Gynecology, Oncology
Q: Tỉ lệ ác tính hay xảy ra nhất với loại u buồng trứng nào sau đây?
Options (shared set): ['U tiết dịch nhầy.', 'U tiết dịch trong.', 'U dạng bì.', 'U nang hoàng tuyến.']
  line   3792 | Medium      | id 8729f6bf12094bf58501ce7d4924dd04 | B -> U tiết dịch trong.
  line  10111 | Medium      | id e0b7acf828444ccb8d55b273b6833c76 | B -> U tiết dịch trong.

### Group 524 — topic: Obstetrics and Gynecology, Oncology
Q: Tần suất xuất hiện ung thư BT trên u nang thực thể của BT là bao nhiêu?
Options (shared set): ['< 1% u thực thể chẩn đoán trước mãn kinh, 15% xuất hiện sau mãn kinh', '5% u thực thể chẩn đoán trước mãn kinh, 15% xuất hiện sau mãn kinh', '< 1% u thực thể chẩn đoán trước mãn kinh, 25% xuất hiện sau mãn kinh', '5% u thực thể chẩn đoán trước mãn kinh, 25% xuất hiện sau mãn kinh']
  line   3793 | Medium      | id 72afd1a30b0145b6a37f85b618df8fa8 | B -> 5% u thực thể chẩn đoán trước mãn kinh, 15% xuất hiện sau mãn kinh
  line  10076 | Easy        | id ca380af84d37409794aa60d6aab29f80 | B -> 5% u thực thể chẩn đoán trước mãn kinh, 15% xuất hiện sau mãn kinh

### Group 525 — topic: Obstetrics and Gynecology, Oncology
Q: Mục đích của sinh thiết cổ tử cung sau đây đều đúng, NGOẠI TRỪ:
Options (shared set): ['Giúp chẩn đoán vi thể về mặt tế bào học', 'Chẩn đoán sớm ung thư cổ tử cung', 'Có thể yên tâm để đốt cổ tử cung điều trị viêm lộ tuyến', 'Giúp chẩn đoán sớm ung thư thân tử cung']
  line   3796 | Medium      | id 2c8e9973dd8a41faae460b2907ea5a3a | D -> Giúp chẩn đoán sớm ung thư thân tử cung
  line   8420 | Medium      | id 813f482b93ac42178d74d118a2c13e8d | D -> Giúp chẩn đoán sớm ung thư thân tử cung

### Group 526 — topic: Obstetrics and Gynecology, Oncology
Q: Khi khám phụ khoa định kỳ, cần làm tế bào học âm đao cổ tử cung Pap’mear để:
Options (shared set): ['Phân biệt chủng vi khuẩn gây viêm âm đạo cổ tử cung', 'Đánh giá mức độ tổn thương viêm cổ tử cung', 'Phát hiện sự có mặt của tế bào ung thư cổ tử cung', 'Đánh giá mức độ lộ tuyến cổ tử cung']
  line   3806 | Medium      | id ab7c985bbdfc4e419ed6f207893a4bfd | C -> Phát hiện sự có mặt của tế bào ung thư cổ tử cung
  line  10150 | Medium      | id 8bf6e3c48e6a4510b04d71c5a1074807 | C -> Phát hiện sự có mặt của tế bào ung thư cổ tử cung

### Group 527 — topic: Obstetrics and Gynecology, Oncology
Q: Để phát hiện sớm ung thư cổ tử cung, khi khám phụ khoa thường quy cần chú ý:
Options (shared set): ['Siêu âm đầu dò âm đạo và soi cổ tử cung', 'Soi cổ tử cung và làm test HPV', 'Soi cổ tử cung và làm Pap’mear', 'Soi cổ tử cung và làm test Schiller']
  line   3808 | Medium      | id 253f91dd474144b3ada4f0ad1af3323a | C -> Soi cổ tử cung và làm Pap’mear
  line   4210 | Medium      | id 97fa9c603a4344d193c486964faf6c92 | C -> Soi cổ tử cung và làm Pap’mear

### Group 528 — topic: Obstetrics and Gynecology, Oncology
Q: Một bệnh nhân 16 tuổi. Khám chẩn đoán có khối u buồng trứng to, dính, kèm theo có dịch cổ trướng, thể trạng gầy sút. Hướng xử trí đúng là:
Options (shared set): ['Mổ cắt khối u buồng trứng kết hợp điều trị hoá chất.', 'Mổ cắt khối u buồng trứng và phần phụ bên đối diện.', 'Mổ cắt tử cung và 2 phần phụ.', 'Mổ cắt tử cung và phần phụ 2 bên kết hợp điều trị hoá chất.']
  line   3820 | Challenging | id 14a20f5515bb4abdbc1e3208371a7abd | D -> Mổ cắt tử cung và phần phụ 2 bên kết hợp điều trị hoá chất.
  line   3872 | Challenging | id 5d13e7b0ba744638b8bf655b2cdb0652 | D -> Mổ cắt tử cung và phần phụ 2 bên kết hợp điều trị hoá chất.

### Group 529 — topic: Obstetrics and Gynecology, Oncology
Q: U thanh dịch và u dịch nhầy là 2 loại u buồng trứng thường gặp nhất. Điểm chung của 2 loại này đều có nguồn gốc từ tế bào nào dưới đây?
Options (shared set): ['Tế bào nội mạc tử cung hoặc biểu mô ống dẫn trứng', 'Tế bào mầm của buồng trứng', 'Tế bào biểu mô bề mặt buồng trứng', 'Tế bào dây sinh dục đệm buồng trứng']
  line   3829 | Medium      | id 04c857b98cdb4fad8bef9ab30c615289 | C -> Tế bào biểu mô bề mặt buồng trứng
  line  11897 | Medium      | id 9bb20827682e427ab9d5ad3373329acc | C -> Tế bào biểu mô bề mặt buồng trứng

### Group 530 — topic: Obstetrics and Gynecology, Oncology
Q: U dịch nhầy là loại u buồng trứng thường gặp. Đặc điểm nào dưới đây là phù hợp nhất cho khối u này?
Options (shared set): ['Chiếm tỷ lệ cao nhất trong các u biểu mô buồng trứng nói chung', '50% u dịch nhầy là u ác tính, u lành tính và giáp biên ít hơn', 'Diện cắt thường đặc, có nước chảy ra và u xẹp lại', 'Các tế bào biểu mô chế tiết chất nhầy, phản ứng PAS dương tính']
  line   3830 | Medium      | id 7f137829bfa34429bbb03b934732ac99 | D -> Các tế bào biểu mô chế tiết chất nhầy, phản ứng PAS dương tính
  line   9001 | Challenging | id 1a31d024b8b142c58106250da05bc425 | D -> Các tế bào biểu mô chế tiết chất nhầy, phản ứng PAS dương tính

### Group 531 — topic: Obstetrics and Gynecology, Oncology
Q: Tổn thương tiền ung thư cổ tử cung thường xảy ra ở vị trí nào của cổ tử cung. Chọn ý đúng nhất theo thứ tự thường gặp?
Options (shared set): ['Cổ ngoài và cổ trong', 'Vùng chuyển tiếp và ổng CTC', 'Cổ trong và cổ ngoài', 'Vùng chuyển tiếp và cổ ngoài']
  line   3836 | Medium      | id 5ed39e19afcf429ba90813c39d2b2148 | D -> Vùng chuyển tiếp và cổ ngoài
  line   3838 | Medium      | id adba5250b57a40bcb5fef7d63de66f36 | D -> Vùng chuyển tiếp và cổ ngoài.

### Group 532 — topic: Obstetrics and Gynecology, Oncology, Pathology
Q: Tiêu chuẩn vi thể quan trọng nhất của ung thư cổ tử cung tại chỗ:
Options (shared set): ['toàn bộ biểu mô vảy loạn sản, kém biệt hoá, sắp xếp lộn xộn.', 'màng đáy bị phá vỡ.', 'màng đáy còn nguyên vẹn.', 'cả a và c']
  line   3852 | Challenging | id f548bc7c155f479ab032623c7e3e1778 | D -> cả a và c
  line   3855 | Challenging | id a0a9d85d6bcb428da9a3ac124be3f478 | D -> cả a và c

### Group 533 — topic: Obstetrics and Gynecology, Oncology, Pathology
Q: Khối u buồng trứng, type mô học nào sau đây thường gặp nhất:
Options (shared set): ['U nhầy', 'U quái', 'U thanh dịch', 'U tế bào hạt']
  line   3853 | Medium      | id c65c1e342b0344ca9ede06c61058ba65 | C -> U thanh dịch
  line  10093 | Easy        | id 5736ec0a9f094281941223de562602e6 | C -> u thanh dịch

### Group 534 — topic: Obstetrics and Gynecology, Oncology, Pathology
Q: U brenner
Options (shared set): ['Là u ác tính di căn đến buồng trứng', 'Là mô u được cấu tạo gồm: mô đệm phong phú và các đám tế bào biểu mô dạng chuyển tiếp', 'Xuất phát từ dây sinh dục đệm của buồng trứng', 'U thường là giáp biên ác và ác tính']
  line   3857 | Medium      | id 53c19a1d24894f109d245a1632f850a5 | B -> Là mô u được cấu tạo gồm: mô đệm phong phú và các đám tế bào biểu mô dạng chuyển tiếp
  line   3883 | Medium      | id 9289aa5685d740e8bc2c70cdf041316f | B -> Là mô u được cấu tạo gồm: mô đệm phong phú và các đám tế bào biểu mô dạng chuyển tiếp

### Group 535 — topic: Obstetrics and Gynecology, Oncology, Surgery
Q: Bệnh nhân 54 tuổi được mổ vì có khối u vùng chậu, vào bụng thấy có u buồng trứng một bên với di căn mạc nối lớn. Phẫu thuật thích hợp nhất là:
Options (shared set): ['Sinh thiết mạc nối lớn.', 'Sinh thiết buồng trứng.', 'Cắt phần di căn mạc nối lớn và cắt u buồng trứng.', 'Cắt toàn bộ mạc nối lớn, cắt tử cung toàn phần và 2 phần phụ.']
  line   3871 | Challenging | id cb90f6586cea42f4b9a6d3dcf409e08c | D -> Cắt toàn bộ mạc nối lớn, cắt tử cung toàn phần và 2 phần phụ.
  line   9676 | Hard        | id dd1ad688ab25422685620fec94763c00 | D -> Cắt toàn bộ mạc nối lớn, cắt tử cung toàn phần và 2 phần phụ.

### Group 536 — topic: Obstetrics and Gynecology, Pathology
Q: U xơ tuyến vú:
Options (shared set): ['Phổ biến ở tuổi 30', 'Phát triển từ mô đệm trong thuỳ tuyến chuyên biệt', 'Về vi thể: chủ yếu là các tuyến được phủ bởi mô đệm xơ', 'Vị trí thường gặp ở 1/4 trên của vú']
  line   3884 | Medium      | id b6d0526728ca494e8716908eafb3fc15 | C -> Về vi thể: chủ yếu là các tuyến được phủ bởi mô đệm xơ
  line  10145 | Medium      | id 7fb7506d563a41f0aa90be7b03f4e37e | C -> về vi thể: chủ yếu là các tuyến được phủ bởi mô đệm xơ

### Group 537 — topic: Obstetrics and Gynecology, Pathology
Q: Đặc điểm giải phẫu bệnh của một u buồng trứng được mô tả như sau: U có dạng nang, đường kính lớn nhất 15cm, có hình nhiều thùy, diện cắt u xẹp, có vách ngăn, không tạo nhú; vi thể vách nang phủ bởi biểu mô vuông hay trụ thấp. Chẩn đoán nào phù hợp cho trường hợp này?
Options (shared set): ['U thanh dịch lành tính', 'U nhầy lành tính', 'U thanh dịch giáp biên ác', 'U nhầy giáp biên ác']
  line   3888 | Challenging | id 880d6f41c5e141119799f95346afce72 | B -> U nhầy lành tính
  line   8080 | Hard        | id 8f04078a1c5f4f41967053660fb0ded6 | A -> U thanh dịch lành tính

### Group 538 — topic: Obstetrics and Gynecology, Pediatrics
Q: Sự tái tạo nước ối, chọn câu đúng nhất:
Options (shared set): ['Do nội sản mạc tiết ra', 'Do thấm từ máu mẹ qua màng ối vào', 'Do thai nhi bài tiết', 'Cả 3 câu trên đều đúng']
  line   3974 | Medium      | id f0ac99f56f6a45efb180328450648a08 | D -> Cả 3 câu trên đều đúng
  line  11707 | Easy        | id 216d85e1b11640d583165b97ce067286 | D -> Cả 3 câu trên đều đúng

### Group 539 — topic: Obstetrics and Gynecology, Pediatrics, Pulmonology
Q: Việc quản lý thai nghén tốt không giúp làm giảm tần suất bệnh màng trong, hít nước ối phân su, nhiễm trùng phổi sơ sinh.
Options (shared set): ['Đúng', 'Sai']
  line   4001 | Medium      | id 3e76b39c2329455ab17714221f0417bb | B -> Sai
  line   5127 | Medium      | id 0fd2d8ae039c4ba1bbe6d5ddbfed1945 | B -> Sai

### Group 540 — topic: Obstetrics and Gynecology, Pediatrics, Pulmonology
Q: Chẩn đoán hít nước ối phân su cũng cần được nghĩ đến cả trước sinh, khi có nước ối bẩn, suy thai.
Options (shared set): ['Đúng', 'Sai']
  line   4002 | Medium      | id e92dd4faa40e4999b7ffa9b2e0ff9ef3 | A -> Đúng
  line   5128 | Medium      | id c061662be4d94114b86a58225699d36b | A -> Đúng

### Group 541 — topic: Obstetrics and Gynecology, Pediatrics, Pulmonology
Q: Vai trò hô hấp của bánh rau, chọn một câu đúng nhất
Options (shared set): ['Nhờ cơ chế khuyếch tán', 'Phụ thuộc vào dòng máu đến bánh rau', 'Trường hợp cao huyết áp, cơn co tử cung cường tính máu đến rau sẽ giảm', 'Cả 3 câu trên đều đúng']
  line   4004 | Medium      | id 074b2cb4e3d04a7a8169a9b7218b59d2 | D -> Cả 3 câu trên đều đúng
  line   5823 | Medium      | id 527bc6893886496abcf41e2cc31260ab | D -> Cả 3 câu trên đều đúng

### Group 542 — topic: Obstetrics and Gynecology, Pulmonology
Q: Điều nào sau đây thường là ảnh hưởng của việc mang thai đối với bệnh nhân hen?
Options (shared set): ['Sự gia tăng các biến chứng của mẹ và con khi sinh', 'Trầm trọng hơn các triệu chứng', 'Cải thiện chức năng hô hấp', 'Giảm triệu chứng hen suyễn']
  line   4009 | Medium      | id 70049746aea1478eba5a721962ed4929 | B -> Trầm trọng hơn các triệu chứng
  line   4612 | Medium      | id 560273f725b34a6482eaa503d66349a1 | A -> Sự gia tăng các biến chứng của mẹ và con khi sinh

### Group 543 — topic: Obstetrics and Gynecology, Pulmonology
Q: Theo dõi sau nạo trứng, chụp phổi cần phải tiến hành:
Options (shared set): ['Một tháng sau nạo thai trứng.', 'Mỗi tháng một lần trong ba tháng đầu.', 'Ba tháng một lần.', 'Chỉ có chỉ định chụp phổi khi nồng độ hCG còn cao bất thường.']
  line   4010 | Medium      | id c7e6f580eeb9420f9a5f40e0110ee21b | D -> Chỉ có chỉ định chụp phổi khi nồng độ hCG còn cao bất thường.
  line   5790 | Medium      | id e4c6079489ed477aadb24d83c34ddc7c | D -> Chỉ có chỉ định chụp phổi khi nồng độ hCG còn cao bất thường.

### Group 544 — topic: Obstetrics and Gynecology, Pulmonology
Q: Biến chứng của tình trạng thiểu ối trong thai kỳ là:
Options (shared set): ['Thiểu sản gan.', 'Thiểu sản đường tiêu hóa.', 'Thiểu sản thận .', 'Thiểu sản phổi .']
  line   4011 | Medium      | id a349bbe8749b4ac6ac93e652d5861834 | D -> Thiểu sản phổi .
  line   5792 | Medium      | id cfe5a1c05e35407787a846164cd4c92c | D -> Thiểu sản phổi .
  line   5795 | Medium      | id f838a31b2bbc4803ba90e6fe5fe24bc1 | D -> Thiểu sản phổi .

### Group 545 — topic: Obstetrics and Gynecology, Radiology
Q: Phương tiện tốt nhất & nhanh nhất giúp chẩn đoán chính xác đa ối:
Options (shared set): ['Khám lâm sàng', 'X quang', 'Siêu âm', 'Soi ối']
  line   4014 | Medium      | id 7febd36c1122413685c39566ad2afe97 | C -> Siêu âm
  line   8615 | Medium      | id 51e73d61d5d44682872de554abf9a063 | C -> Siêu âm

### Group 546 — topic: Obstetrics and Gynecology, Radiology
Q: Một phụ nữ sẩy thai đã 3 tuần rong huyết dai dẳng. Khám thấy cổ tử cung đóng, thân tử cung hơi to. Việc nào cần thực hiện nào dưới đây?
Options (shared set): ['Chọc dò cùng đồ sau.', 'Chụp buồng tử cung-vòi trứng có cản quang.', 'Siêu âm vùng chậu.', 'Nội soi ổ bụng.']
  line   4019 | Challenging | id aa8f134e588b479a8d566c347ed4c62f | C -> Siêu âm vùng chậu.
  line   9157 | Challenging | id 56276cebcffd4df4bf6b6e09e4f79070 | C -> Siêu âm vùng chậu.

### Group 547 — topic: Obstetrics and Gynecology, Radiology
Q: Chỉ định chụp tử cung vòi trứng nào sau đây là đúng:
Options (shared set): ['Vô sinh chưa rõ nguyên nhân', 'U xơ tử cung', 'U nang buồng trứng', 'U lạc nội mạc tử cung']
  line   4031 | Medium      | id cf12bbd0c62d4e3692b2c3c855377d92 | A -> Vô sinh chưa rõ nguyên nhân
  line   7909 | Challenging | id e9a70ec209a44eb9ba8d87890ccd7860 | A -> Vô sinh chưa rõ nguyên nhân
  line   9158 | Medium      | id 23e6dcf591444d20a02641fc836d70d1 | A -> Vô sinh chưa rõ nguyên nhân

### Group 548 — topic: Obstetrics and Gynecology, Radiology
Q: Khi chỉ có khối u buồng trứng đơn thuần, chụp tử cung vòi trứng có thuốc cản quang sẽ thấy:
Options (shared set): ['Vòi trứng bên có khối u bị co ngắn lại', 'Vòi trứng bên có khối u bị kéo dài ra.', 'Vòi trứng bên có khối u bị bít tắc.', 'Cả A, B, C đều đúng.']
  line   4032 | Challenging | id 8286ec05300f400bbede1b7587acd423 | B -> Vòi trứng bên có khối u bị kéo dài ra.
  line   8291 | Medium      | id dae56bd86a1649e29b24068a5045c700 | B -> Vòi trứng bên có khối u bị kéo dài ra.

### Group 549 — topic: Obstetrics and Gynecology, Radiology
Q: Thời điểm tốt nhất để siêu âm hình thái học của thai nhi là:
Options (shared set): ['Tuần 11 - 15', 'Tuần 16 - 20', 'Tuần 21 - 24', 'Sau tuần lễ thứ 24']
  line   4041 | Easy        | id 779eee5a60aa432f8d42f43fbf32c5f1 | B -> Tuần 16 - 20
  line   9123 | Easy        | id 9d58aca26a704257b08fc0a4daf5ca8e | B -> Tuần 16 - 20

### Group 550 — topic: Obstetrics and Gynecology, Radiology
Q: Xác định tuổi thai 12 tuần, yếu tố nào chính xác nhất
Options (shared set): ['Kích thước túi thai (GS: gestation sac).', 'Túi ối (amniotic sac: AS)', 'Chiều dài đầu mông (CRL: Crown-rump length).', 'Đường kính lưỡng đỉnh, chiều dài xương đùi...']
  line   4042 | Medium      | id e2f151b4213840568c54fc9cd9b69cba | C -> Chiều dài đầu mông (CRL: Crown-rump length).
  line   4091 | Medium      | id 3c29adf605ff47be9ef3885a359bcb48 | C -> Chiều dài đầu mông (CRL: Crown-rump length).

### Group 551 — topic: Obstetrics and Gynecology, Radiology
Q: Chụp X quang bụng không chuẩn bị có thể phát hiện được u nang:
Options (shared set): ['U nang nước', 'U nang nhầy', 'U nang bì', 'Cả 3 loại u nang trên']
  line   4054 | Medium      | id de12ad67647d41918f80e5abe1bd16eb | C -> U nang bì
  line   7964 | Medium      | id 9b4af78f3ee0441b9d38fe9f79edd98c | C -> U nang bì
  line  11911 | Easy        | id 96141447043542d5a290447c05465366 | D -> Cả 3 loại u nang trên

### Group 552 — topic: Obstetrics and Gynecology, Radiology
Q: Với u nang buồng trứng, hình ảnh khi chụp TC – vòi trứng thường thấy:
Options (shared set): ['Buồng TC bên có U bị choán chỗ', 'Vòi trứng bên có U bị dãn to', 'Vòi trứng bên có U bị kéo dài', 'Thấy rõ khối u buồng trứng']
  line   4056 | Medium      | id 3ed2207af8af43639bee60ce9baf52af | C -> Vòi trứng bên có U bị kéo dài
  line   9067 | Medium      | id 821f613afea84180aabe9f42b3942ee7 | C -> Vòi trứng bên có U bị kéo dài

### Group 553 — topic: Obstetrics and Gynecology, Radiology
Q: Trong 3 tháng đầu của thời kỳ thai nghén, siêu âm giúp chẩn đoán, NGOẠI TRỪ:
Options (shared set): ['Thai trong tử cung: đơn hoặc đa thai', 'Dọa sảy thai', 'Rau tiền đạo', 'Dị dạng thai nhi']
  line   4059 | Medium      | id cefca2ed3d6e4d27ab63756ed5b25f55 | C -> Rau tiền đạo
  line  11918 | Easy        | id d007fe3be3b94e6f98869b10c363c587 | C -> Rau tiền đạo

### Group 554 — topic: Obstetrics and Gynecology, Radiology
Q: Hình ảnh thai chết lưu trên 20 tuần ở trên phim Xquang có:
Options (shared set): ['Dấu hiệu Piszkacsek', 'Dấu hiệu Noble', 'Dấu hiệu Spanding', 'Dấu hiệu Bandl- Frommel']
  line   4061 | Medium      | id cff06e37cceb42039d15f66be1091191 | C -> Dấu hiệu Spanding
  line   9134 | Medium      | id c0b41f8df09047739960733dc5fc14f7 | C -> Dấu hiệu Spanding

### Group 555 — topic: Obstetrics and Gynecology, Radiology
Q: Thai lưu dưới 12 tuần có hình ảnh siêu âm nào thường gặp.
Options (shared set): ['Túi thai không chứa phôi hay có phôi nhưng không có tim phôi.', 'Thai bị gập lại.', 'Gai nhau thoái hóa nước.', 'Dấu hiệu chồng khớp sọ.']
  line   4068 | Medium      | id c277e8c41e6d471cb8a7a239a44a3604 | A -> Túi thai không chứa phôi hay có phôi nhưng không có tim phôi.
  line   9127 | Medium      | id c43ca20645634704bb04579401c192a4 | A -> Túi thai không chứa phôi hay có phôi nhưng không có tim phôi.

### Group 556 — topic: Obstetrics and Gynecology, Radiology
Q: Về siêu âm chẩn đoán trong phụ khoa, tất cả các câu sau đây đều đúng, NGOẠI TRỪ:
Options (shared set): ['Hiện nay có thể thay thế hoàn toàn phương pháp X quang trong chẩn đoán phụ khoa.', 'Kết quả thu được tùy thuộc vào kinh nghiệm của người đọc siêu âm', 'Có thể được dùng để chẩn đoán còn vòng tránh thai trong tử cung hay không', 'Có thể gợi ý đến khả năng ác tính của một khối u buồng trứng']
  line   4077 | Challenging | id dc5dbe4d931d4f66b6021e0ba3b92004 | A -> Hiện nay có thể thay thế hoàn toàn phương pháp X quang trong chẩn đoán phụ khoa.
  line   9033 | Easy        | id 84ad458891f2427b964e3797d2599793 | A -> Hiện nay có thể thay thế hoàn toàn phương pháp X quang trong chẩn đoán phụ khoa.

### Group 557 — topic: Obstetrics and Gynecology, Radiology
Q: Chẩn đoán rau tiền đạo bằng siêu âm có giá trị khi tuổi thai mấy tuần:
Options (shared set): ['32', '34', '36', '38']
  line   4083 | Medium      | id 46932f07dcc24be691e44ffad5a8112d | B -> 34
  line   7888 | Easy        | id ada48c97611944b6a8586afdd3f99910 | D -> 34

### Group 558 — topic: Obstetrics and Gynecology, Radiology
Q: Trường hợp đang mang dụng cụ tử cung mà có thai, muốn siêu âm xác định còn vòng trong tử cung không thì phải thực hiện trong khoảng thời gian nào để dễ thấy được dụng cụ tử cung:
Options (shared set): ['Khoảng 5 tuần vô kinh', 'Khoảng 12 tuần vô kinh', 'Khoảng 16 tuần vô kinh', 'Bất cứ thời điểm nào cũng được']
  line   4089 | Medium      | id 5c49915f1f7f46a9bcf938ae96bdf65c | A -> Khoảng 5 tuần vô kinh
  line   9146 | Medium      | id ba7a591d3811456dbcb7f71d72a287cc | A -> Khoảng 5 tuần vô kinh

### Group 559 — topic: Obstetrics and Gynecology, Surgery
Q: 19.đặc điểm cắt tầng sinh môn theo đường chéo bên(5h-7h):
Options (shared set): ['thuận lợi dễ cắt', 'tổn thương cơ vòng hậu môn& có thể nới rộng khi cần thiết', 'vết khâu dễ kành hơn so với vị trí 6h', 'biến chứng đau khi giao hợp về sau']
  line   4102 | Medium      | id 24d2f11db6514fc9aad5e26d1894994f | B -> tổn thương cơ vòng hậu môn& có thể nới rộng khi cần thiết
  line   9709 | Medium      | id a1a8e6cc81eb447282871d7ca71ff0e4 | B -> tổn thương cơ vòng hậu môn& có thể nới rộng khi cần thiết

### Group 560 — topic: Obstetrics and Gynecology, Surgery
Q: Tất cả những câu sau nói về ưu điểm phẫu thuật mổ lấy thai qua đoạn dưới so với mổ thân tử cung lấy thai đều đúng, NGOẠI TRỪ:
Options (shared set): ['Lớp phúc mạc dễ bóc tách có thể che phủ được vết mổ.', 'Dễ lấy thai.', 'Ít gây chẩy máu.', 'Sẹo mềm.']
  line   4104 | Medium      | id eb00d8b5426b4df7b92524719b1a54d4 | B -> Dễ lấy thai.
  line   9683 | Medium      | id 5056ad63d93046499697e6034f1d3008 | B -> Dễ lấy thai.

### Group 561 — topic: Obstetrics and Gynecology, Surgery
Q: Nói về điều trị u xơ tử cung:
Options (shared set): ['Chỉ có chỉ định phẫu thuật khi bệnh nhân đã vào giai đoạn tiền mãn kinh', 'Nếu có chỉ định phẫu thuật "cắt tử cung toàn phần" là phương pháp ưu tiên được chọn lựa', 'Chỉ bóc nhân xơ ở những bệnh nhân bị vô sinh nguyên phát', 'Tất cả đều sai']
  line   4126 | Challenging | id b276cc9b9d6947d188d6709f540ef7d7 | D -> Tất cả đều sai
  line   9642 | Medium      | id 78eeaa19e8bf44c49604f9c22a7089fb | B -> Nếu có chỉ định phẫu thuật "cắt tử cung toàn phần" là phương pháp ưu tiên được chọn lựa

### Group 562 — topic: Obstetrics and Gynecology, Surgery
Q: Điều trị ngoại khoa u xơ tử cung, CHỌN SAI:
Options (shared set): ['Có nhiều phương pháp phẫu thuật u xơ tử cung', 'Chỉ định phương pháp phẫu thuật u xơ tử cung tùy thuộc vào nhiều yếu tố', 'Không bóc nhân xơ nếu bệnh nhân đã có 2 con', 'Không để lại 2 phần phụ nếu bệnh nhân đã mãn kinh']
  line   4128 | Challenging | id f75684c26dc046cdb0a46cf00b30bb72 | C -> Không bóc nhân xơ nếu bệnh nhân đã có 2 con
  line   9637 | Medium      | id 4509d46dd1a24c5ebd43a6e6d3163552 | C -> Không bóc nhân xơ nếu bệnh nhân đã có 2 con

### Group 563 — topic: Public Health, Preventive Healthcare
Q: Quyết định phân công nhiệm vụ cho cán bộ hợp lý để:
Options (shared set): ['Phát huy tối đa việc quy hoạch đội ngũ cán bộ', 'Phát huy tính ổn định cán bộ trong đơn vị', 'Phát huy tối đa hiệu quả thực hiện của nguồn nhân lực hiện có.', 'Phát huy sử dụng hiệu quả nguồn nhân lực trong tương lai']
  line   4205 | Easy        | id 8c935a25868047e68978ac7874e59579 | C -> Phát huy tối đa hiệu quả thực hiện của nguồn nhân lực hiện có.
  line   4242 | Easy        | id 3a747fbf945c41728c604201572aa7fa | C -> Phát huy tối đa hiệu quả thực hiện của nguồn nhân lực hiện có.

### Group 564 — topic: Infectious Diseases, Pulmonology
Q: Người bị mắc bệnh lao, khi tiến hành test tuberculin chắc chắn cho kết quả dương tính hoặc dương tính mạnh.
Options (shared set): ['đúng', 'sai']
  line   4292 | Medium      | id 809120eb798541999a89b7ffd67bc1de | B -> sai
  line   4595 | Medium      | id ce7f6d7634d943f290ef9d88eb957804 | B -> sai
  line   6027 | Medium      | id 743f458522a04c01991769882f764fb8 | B -> sai

### Group 565 — topic: Pulmonology, Infectious Diseases
Q: Lâm sàng của viêm phổi KHÔNG gặp dấu hiệu nào sau đây:
Options (shared set): ['Tam chứng màng phổi.', 'Hội chứng trung thất', 'Hội chứng đông đặc phổi.', 'Hội chứng suy hô hấp']
  line   4304 | Medium      | id 74030450066e4afbb98742d450af14e6 | B -> Hội chứng trung thất
  line   5753 | Medium      | id e2cf4d2894ca48618d0df240b0245b76 | B -> Hội chứng trung thất

### Group 566 — topic: Otolaryngology, Infectious Diseases
Q: Khi xét nghiệm dịch xuất tiết ở thanh quản có BK (+) ở một người đang khàn tiếng, người ta nói rằng bệnh nhân này bị viêm thanh quản lao?
Options (shared set): ['Đúng', 'Sai']
  line   4318 | Medium      | id dcd06e84246242be9718d43890c42647 | A -> Đúng
  line   5779 | Medium      | id 474a9c8e3f6941239f3fcb1c209457bc | A -> Đúng

### Group 567 — topic: Pulmonology, Infectious Diseases, Pathology
Q: Chọn câu trả lời đúng nhất, trong viêm phổi thùy, hình ảnh vi thể “lòng các phế nang chứa các sợi tơ huyết tạo thành khuôn trong đó chứa đầy hồng cầu” là tổn thương đặc trưng ở giai đoạn nào?
Options (shared set): ['Gan hóa đỏ', 'Tổ chức hóa', 'Phổi lách hóa', 'Áp xe hóa']
  line   4327 | Challenging | id 63df415fa61945e9bf529bd23cf57601 | A -> Gan hóa đỏ
  line   5857 | Medium      | id d2024a1033ca4736bd9f206268d7948e | A -> Gan hóa đỏ

### Group 568 — topic: Pulmonology, Infectious Diseases
Q: Nguyên nhân gây viêm phổi thường gặp nhất là gì?
Options (shared set): ['Virus', 'Vi khuẩn', 'Ký sinh trùng', 'Nấm']
  line   4351 | Easy        | id 6ac3ca12efbf48a69c774bacf56a4c54 | A -> Virus
  line   5476 | Easy        | id dddeff2101594ba9be97c0405b27ad8a | A -> Virus

### Group 569 — topic: Public Health, Preventive Healthcare
Q: Thông thường, nghiên cứu can thiệp là nghiên cứu:
Options (shared set): ['Tình trạng phơi nhiễm của các đối tượng nghiên cứu xảy ra tự nhiên, người nghiên cứu chỉ quan sát và ghi nhận lại', 'Tình trạng phơi nhiễm của các đối tượng nghiên cứu do chính họ lựa chọn', 'Tình trạng phơi nhiễm của các đối tượng nghiên cứu do người nghiên cứu chỉ định', 'Cả ba tình huống trên đều được']
  line   4367 | Medium      | id b050a37d26674ee1bd6bdac132d6c93c | C -> Tình trạng phơi nhiễm của các đối tượng nghiên cứu do người nghiên cứu chỉ định
  line  11075 | Medium      | id 50e0723d245146ffa2fca0be8314d013 | C -> Tình trạng phơi nhiễm của các đối tượng nghiên cứu do người nghiên cứu chỉ định

### Group 570 — topic: Public Health
Q: Khi dùng phương pháp so sánh để đánh giá kết quả GDSK. có thể áp dụng những mô hình so sánh sau, NGOẠI TRỪ
Options (shared set): ['So sánh sự thay đổi hành vi sức khỏe của nhóm đối tượng giáo dục sức khỏe trước và sau khi thực hiện GDSK', 'So sánh sự thay đổi hành vi sức khỏe của nhóm đối tượng đã được giáo dục sức khỏe với nhóm đối tượng chưa được giáo dục sức khỏe', 'So sánh mức độ thay đổi hành vi sức khỏe của nhóm được giáo dục sức khỏe với các tiêu chuẩn mà mục tiêu GDSK đề ra', 'So sánh sự thay đổi hành vi sức khỏe giữa các đối tượng được giáo dục sức với nhau']
  line   4368 | Medium      | id 7938b7bb57cb48479aa4e1d23991185e | D -> So sánh sự thay đổi hành vi sức khỏe giữa các đối tượng được giáo dục sức với nhau
  line  11076 | Medium      | id 0d6a42cb679f40b691626d61d6920be0 | D -> So sánh sự thay đổi hành vi sức khỏe giữa các đối tượng được giáo dục sức với nhau

### Group 571 — topic: Public Health, Preventive Healthcare
Q: Nhân viên y tế thôn bản tốt nhất là những người:
Options (shared set): ['Xuất thân từ cộng đồng', 'Xuất thân từ cộng đồng', 'được đào tạo để làm việc cho cộng đồng', 'có mối liên hệ mật thiết với hệ thống chăm sóc sức khỏe']
  line   4369 | Medium      | id a825cad1fa824de093e59851e7c4a94c | B -> Xuất thân từ cộng đồng
  line  11077 | Medium      | id 8bbc42c09c79422ba58a705943a15433 | B -> Xuất thân từ cộng đồng

### Group 572 — topic: General Medicine, Public Health
Q: Nội dung của thanh tra dược:
Options (shared set): ['Thanh tra việc chấp hành các VB PL quy chế dược', 'Thanh tra xuất nhập khẩu thuốc', 'Thanh tra chất lượng thuốc', 'Ngăn ngừa các hoạt động vi phạm']
  line   4370 | Easy        | id aab9cff1c7b840879fbb7e53eb82963e | A -> Thanh tra việc chấp hành các VB PL quy chế dược
  line  11078 | Easy        | id 0030efff761c4695b8837acfa90b0c24 | A -> Thanh tra việc chấp hành các VB PL quy chế dược

### Group 573 — topic: Public Health, Preventive Healthcare
Q: Chọn 1 đáp án đúng nhất: Giống như các dây truyền dịch tễ học, khống chế yếu tố ô nhiễm với môi trường là:
Options (shared set): ['Khống chế nguồn gây ô nhiễm.', 'Ngăn chặn sự phát tán yếu tố ô nhiễm.', 'Bảo vệ những đối tượng tiếp xúc.', 'Cả 3 đáp án trên đều đúng']
  line   4371 | Medium      | id 5beb25ee50b24dd799ef7670c6318f6e | D -> Cả 3 đáp án trên đều đúng
  line  11079 | Medium      | id a764b5c134e14eb2b4f17ef5c19e48f2 | D -> Cả 3 đáp án trên đều đúng

### Group 574 — topic: General Medicine, Public Health
Q: Sự khác nhau của hệ thống y tế các nước là do:
Options (shared set): ['Nguồn đầu tư cho y tế', 'Các định chế chính trị', 'Các chính sách của nhà nước', 'Các yếu tố xã hội']
  line   4372 | Medium      | id 285a42d7ece44bd0aaf80e99c1222c57 | A -> Nguồn đầu tư cho y tế
  line  11080 | Medium      | id 71305e53d2f747628815785ca124fd36 | A -> Nguồn đầu tư cho y tế

### Group 575 — topic: Public Health, Preventive Healthcare
Q: Chức năng của kinh tế y tế là phân tích việc sử dụng các nguồn lực?
Options (shared set): ['Đúng', 'Sai']
  line   4373 | Easy        | id b26b9db7b2804d9ea878e753e06b0751 | A -> Đúng
  line  11081 | Easy        | id 6e57cc550515424dae296efd7faf8409 | A -> Đúng

### Group 576 — topic: Public Health, Preventive Healthcare
Q: Nguyên tắc cơ bản về tổ chức hệ thống y tế VN hiện nay xây dựng theo hướng:
Options (shared set): ['Chủ yếu là điều trị', 'Giáo dục sức khỏe', 'Dự phòng hiện đại', 'Khám và điều trị tại nhà']
  line   4374 | Easy        | id 37af0e91da5b4d8299f876001952ef0e | C -> Dự phòng hiện đại
  line  11082 | Easy        | id 3d54cfa3b3474429846db54fe967f6a9 | C -> Dự phòng hiện đại

### Group 577 — topic: Public Health, Preventive Healthcare
Q: 1. Khái niệm đánh giá là:
Options (shared set): ['Hỗ trợ cán bộ y tế hoàn thành mục tiêu và tìm ra nguyên nhân dẫn đến kết quả đó.', 'Đối chiếu kết quả sau can thiệp so với mục tiêu đề ra', 'Đo lường các chỉ số, đưa ra kết luận về mức độ hoàn thành so với mục tiêu, hiệu quả tương xứng với nguồn lực; tìm ra những nguyên nhân dẫn đến các kết quả đó.', 'Đo lường các chỉ số, hỗ trợ cán bộ y tế làm việc cho đúng chất lượng']
  line   4375 | Easy        | id 136e54b8acbf4f13b082f160fd371b0c | C -> Đo lường các chỉ số, đưa ra kết luận về mức độ hoàn thành so với mục tiêu, hiệu quả tương xứng với nguồn lực; tìm ra những nguyên nhân dẫn đến các kết quả đó.
  line  11083 | Easy        | id bc79091eed844bb38f718f0e532da58f | C -> Đo lường các chỉ số, đưa ra kết luận về mức độ hoàn thành so với mục tiêu, hiệu quả tương xứng với nguồn lực; tìm ra những nguyên nhân dẫn đến các kết quả đó.

### Group 578 — topic: Infectious Diseases, Gastroenterology, Public Health, Preventive Healthcare
Q: Các vụ dịch bệnh nhiễm trùng đường ruột xảy ra hàng loạt trong một thời gian nhất định và không theo khu vực địa lý, thường lan truyền qua:
Options (shared set): ['Thực phẩm', 'Đất bị nhiễm chất thải của người bệnh', 'Ruồi', 'Không khí']
  line   4376 | Medium      | id 8e000f23f70f4082ac21487f309c1015 | A -> Thực phẩm
  line  11084 | Medium      | id a9a67e40be264c1089271618362473db | A -> Thực phẩm

### Group 579 — topic: Public Health, Preventive Healthcare
Q: Trong khi điều khiển xe cơ giới, bạn ................... uống rượu và lái xe.
Options (shared set): ['must', 'mustn’t', 'don’t have to', 'have to']
  line   4377 | Easy        | id 800c692da32b464c9df0cbe946b8769c | B -> mustn’t
  line  11085 | Easy        | id 5bcc1f8d21994d7daa6a2b749a533bcd | B -> mustn’t

### Group 580 — topic: Preventive Healthcare, Cardiology, Public Health
Q: Vận động gia đình bệnh nhân mua bảo hiểm y tế là biện pháp thiết thực phòng bệnh THA cho cộng đồng?
Options (shared set): ['Đúng', 'Sai']
  line   4378 | Easy        | id 517b7253135c4adfb2a0f8d23bccf3f2 | A -> Đúng
  line  11086 | Medium      | id 2ee0a61641b7470dbea95e33eb757767 | A -> Đúng

### Group 581 — topic: Public Health, Preventive Healthcare
Q: Mục tiêu cụ thể của truyền thông giáo dục sức khỏe là đối tượng đạt được sự thay đổi về:
Options (shared set): ['Nhận thức', 'Thái độ', 'Niềm tin', 'Hành vi sức khỏe']
  line   4379 | Easy        | id da18fbac9b2749c89622f9b439cba24f | D -> Hành vi sức khỏe
  line  11087 | Easy        | id 726e388bfb61475a9b0b0add51e6a1da | D -> Hành vi sức khỏe

### Group 582 — topic: Infectious Diseases, Public Health
Q: Ở đồng bằng sông cửu long muỗi phát triển quanh năm. Vậy muốn phòng sốt rét có hiệu quả nên?
Options (shared set): ['Xịt thuốc diệt muỗi định kì và thường xuyên', 'Phát quang hết bụi rậm phá chỗ ở của muỗi', 'Tuyên truyền giáo dục dân chúng phòng chống tối đa muỗi đốt bằng mọi phương pháp', 'Khai thông ao tù nước đọng để hạn chế muỗi sinh sản']
  line   4380 | Medium      | id cea77a222f4a4c8eaaf20a3d3a74a37b | C -> Tuyên truyền giáo dục dân chúng phòng chống tối đa muỗi đốt bằng mọi phương pháp
  line  11088 | Medium      | id c178fe2299994b049d13c334339dbf62 | C -> Tuyên truyền giáo dục dân chúng phòng chống tối đa muỗi đốt bằng mọi phương pháp

### Group 583 — topic: Public Health, Preventive Healthcare
Q: Thay đổi áp phích thường xuyên để gây sự chú ý của mọi người.
Options (shared set): ['Đúng', 'Sai']
  line   4381 | Easy        | id 20bded0920c441a2b03e790059bb7a4e | A -> Đúng
  line  11089 | Medium      | id eb5b7f310139485dac83b3e174fe5b20 | A -> Đúng

### Group 584 — topic: Public Health, Preventive Healthcare
Q: “Chúng ta bước đi như thế nào?” thuộc quy trình lập kế hoạch hoạt động từ dưới lên nào?
Options (shared set): ['Kế hoạch hành động', 'Xác định vấn đề', 'Lựa chọn giải pháp', 'Xây dựng mục tiêu']
  line   4382 | Easy        | id 48c1d877314e4dac8043a97d29df889f | A -> Kế hoạch hành động
  line  11090 | Medium      | id 7baf2364bcb6429c922406d8d18fef21 | A -> Kế hoạch hành động

### Group 585 — topic: Obstetrics and Gynecology, Public Health, Preventive Healthcare
Q: Tỷ lệ phụ nữ áp dụng các biện pháp tránh thai để
Options (shared set): ['Đánh giá kết quả của dịch vụ cung cấp các biện pháp tránh thai', 'Đánh giá hiệu quả của hoạt động sinh đẻ có kế hoạch', 'Đánh giá nhu cầu sử dụng các biện pháp tránh thai của cộng đồng', 'Đánh giá dịch vụ kế hoạch hóa gia tỉnh của cơ sở y tế']
  line   4383 | Medium      | id 915f457e747940c2b73f44e80c5e6dbc | B -> Đánh giá hiệu quả của hoạt động sinh đẻ có kế hoạch
  line  11091 | Medium      | id d77aff91b43f421691c4cf60f14a886e | B -> Đánh giá hiệu quả của hoạt động sinh đẻ có kế hoạch

### Group 586 — topic: Public Health, Preventive Healthcare
Q: Để thực hiện giai đoạn chiến lược dân số Việt Nam 2001-2010 giai đoạn 2 (2006-2010), bộ nông nghiệp và phát triển nông thôn lồng ghép các nội dung dân số vào các chương trình khuyến nông, khuyến lâm, khuyến ngư và phát triển nông thôn. Đúng hay sai?
Options (shared set): ['Đúng', 'Sai', '--', '--']
  line   4384 | Medium      | id 03c8a1319b04438db4efa4373d871303 | A -> Đúng
  line  11092 | Medium      | id 31e71ecffb3f4149b20d52282062ba77 | A -> Đúng

### Group 587 — topic: Public Health, Preventive Healthcare
Q: Danh sách các đơn vị mẫu hoặc bản đồ phân bố các đơn vị mẫu được chọn từ 1 quần thể nghiên cứu gọi là gì?
Options (shared set): ['Đơn vị mẫu', 'Khung nghiên cứu', 'Công cụ nghiên cứu', 'Khung chọn mẫu']
  line   4385 | Easy        | id 72c4222c8d98472fb5f72cead2ea7ce8 | D -> Khung chọn mẫu
  line  11093 | Easy        | id 43f96101b6ea42c0a27b93a3964598bd | D -> Khung chọn mẫu

### Group 588 — topic: Pediatrics, Public Health
Q: Theo quy định của Tổ chức Y tế Thế giới, giai đoạn vị thành niên được tính từ:
Options (shared set): ['10 tuổi đến 19 tuổi', '10 tuổi đến 18 tuổi', '13 tuổi đến 18 tuổi', '13 tuổi đến 19 tuổi']
  line   4386 | Easy        | id 3cd2b04d3410454b90b8145cb904dc55 | A -> 10 tuổi đến 19 tuổi
  line  11094 | Easy        | id ca0fb2c913cd4a30b4ab23d8dede746f | A -> 10 tuổi đến 19 tuổi

### Group 589 — topic: General Medicine, Preventive Healthcare, Public Health
Q: Phát biểu nào sau đây là đúng nhất
Options (shared set): ['Hầu hết bệnh không lây nhiễm là bệnh mạn tính, khó chữa khỏi, phát triển và tiến triển chậm kéo dài.', 'Hầu hết bệnh không lây nhiễm là bệnh mạn tính, có thể chữa khỏi, phát triển và tiến triển chậm kéo dài', 'Hầu hết bệnh không lây nhiễm là bệnh mạn tính, có thể chữa khỏi, phát triển và tiến triển nhanh.', 'Hầu hết bệnh không lây nhiễm là bệnh cấp tính, có thể chữa khỏi, phát triển và tiến triển nhanh.']
  line   4387 | Medium      | id 2401642601b740099af62606b979981a | A -> Hầu hết bệnh không lây nhiễm là bệnh mạn tính, khó chữa khỏi, phát triển và tiến triển chậm kéo dài.
  line  11095 | Medium      | id 426eaf274b8d4888b36ce1ada9762ed2 | A -> Hầu hết bệnh không lây nhiễm là bệnh mạn tính, khó chữa khỏi, phát triển và tiến triển chậm kéo dài.

### Group 590 — topic: Public Health
Q: Chiến lược giáo dược phẩm giúp doanh nghiệp có thể đảm bảo được thu nhập, duy trì uy tín, định giá và quản lý giá khá dễ dàng đó là:
Options (shared set): ['Chiến lược giá linh hoạt', 'Chiến lược một giá', 'Chiến lược giá hớt váng', 'Chiến lược giá ngự trị']
  line   4388 | Easy        | id 370f9e6705ac45cfa2b02692afa7e957 | B -> Chiến lược một giá
  line  11096 | Easy        | id 55ecd22eb52043e895fda928dd20baee | B -> Chiến lược một giá

### Group 591 — topic: Preventive Healthcare, Public Health
Q: Trong kết hợp phát triển kinh tế xã hội với tăng cường, củng cố quốc phòng, an ninh, giải pháp nào được xác định là quan trọng hàng đầu và đang là đòi hỏi cấp thiết đối với cán bộ và nhân dân cả nước ta hiện nay?
Options (shared set): ['Hoàn chỉnh hệ thống pháp luật, cơ chế chính sách có liên quan đến thực hiện kết hợp phát triển kinh tế xã hội với tăng cường củng cố quốc phòng, an ninh trong tình hình mới', 'Bồi dưỡng nâng cao kiến thức, kinh nghiệm kết hợp phát triển kinh tế xã hội với tăng cường củng cố quốc phòng, an ninh cho các đối tượng', 'Xây dựng chiến lược tổng thể kết hợp phát triển kinh tế xã hội với tăng cường củng cố quốc phòng, an ninh trong thời kỳ mới', 'Tăng cường sự lãnh đạo của Đảng và hiệu lực quản lí Nhà nước của chính quyền các cấp trong thực hiện kết hợp phát triển kinh tế xã hội với tăng cường củng cố quốc phòng, an ninh']
  line   4389 | Medium      | id 447ea6cca45a45c1b19513416eb85ba3 | D -> Tăng cường sự lãnh đạo của Đảng và hiệu lực quản lí Nhà nước của chính quyền các cấp trong thực hiện kết hợp phát triển kinh tế xã hội với tăng cường củng cố quốc phòng, an ninh
  line  11097 | Medium      | id 2a117d05c0474a07a4c63af504e8b0ee | D -> Tăng cường sự lãnh đạo của Đảng và hiệu lực quản lí Nhà nước của chính quyền các cấp trong thực hiện kết hợp phát triển kinh tế xã hội với tăng cường củng cố quốc phòng, an ninh

### Group 592 — topic: Public Health, Preventive Healthcare
Q: Có bao nhiêu nội dung trong phương châm quản lý sức khỏe tại Việt Nam :
Options (shared set): ['4 nội dung', '5 nội dung', '6 nội dung', '7 nội dung .']
  line   4390 | Easy        | id 587d2e729bdb4d7380228cdbe3d4efda | B -> 5 nội dung
  line  11098 | Easy        | id 6b6c35f303f94101aa070208f5117458 | B -> 5 nội dung

### Group 593 — topic: Public Health
Q: Phương pháp nghiên cứu mô tả cắt ngang có đặc điểm:
Options (shared set): ['Không xác định được phơi nhiễm là xảy ra trước khi mắc nhiễm', 'Tối ưu khi nghiên cứu các phơi nhiễm hiếm', 'Xác định được tỷ lệ mới mắc bệnh trong quần thể', 'Không xác định được phơi nhiễm trong hiện tại và quá khứ']
  line   4391 | Medium      | id 14b9d771a4ed440bb1730d589028d706 | A -> Không xác định được phơi nhiễm là xảy ra trước khi mắc nhiễm
  line  11099 | Medium      | id 8141915c81e846959c82628bf7f65728 | A -> Không xác định được phơi nhiễm là xảy ra trước khi mắc nhiễm

### Group 594 — topic: Infectious Diseases, Public Health
Q: Ruồi và gián là các véc-tơ truyền bệnh sinh học, có thể truyền các bệnh lỵ, ỉa chảy, tả, thương hàn,…
Options (shared set): ['Sai', 'Đúng', 'Không có', 'Không có']
  line   4392 | Easy        | id b54db2abcfb64869934d2c6ed182a55a | A -> Sai
  line  11100 | Easy        | id 4801f895f8a4488b918ceac7097fc45a | A -> Sai

### Group 595 — topic: Public Health, Preventive Healthcare
Q: Tư vấn sức khỏe là hình thức giáo dục sức khỏe cho?
Options (shared set): ['Cộng đồng', 'Cá nhân', 'Nhóm nhỏ', 'Nhóm lớn']
  line   4393 | Easy        | id c71c6f3cfe9b4cf2b43356926685fd6f | B -> Cá nhân
  line  11101 | Medium      | id aed4e355b3994e529b320104623c9f3a | B -> Cá nhân

### Group 596 — topic: Public Health, Preventive Healthcare
Q: Yếu tố ảnh hưởng gián tiếp đến hệ sinh thái là:
Options (shared set): ['Đánh bắt cá quá mức', 'Biến đổi khí hậu', 'Thay đổi đất ở, đất canh tác', 'Văn hóa và tôn giáo']
  line   4394 | Easy        | id 6ed44a393c8d44bda0ab93e391072e6b | D -> Văn hóa và tôn giáo
  line  11102 | Medium      | id 06e19d39520b4d9a8775d54d1066f123 | D -> Văn hóa và tôn giáo

### Group 597 — topic: Public Health, Preventive Healthcare
Q: Bản chất của hoạt động giám sát.
Options (shared set): ['Xem xét các công việc có được tiến hành theo đúng luật pháp.', 'Xem xét các công việc có được tiến hành theo đúng kỹ thuật.', 'Là hoạt động hỗ trợ của người quản lí đối với người thực hiện', 'Kiểm soát chất lượng các nội dung công việc.một cá nhân']
  line   4395 | Medium      | id 96da2d691c3d417d81d78cfccb0c7418 | C -> Là hoạt động hỗ trợ của người quản lí đối với người thực hiện
  line  11103 | Medium      | id 1a4a3ed434164e2db4fa9c1df2cf1735 | C -> Là hoạt động hỗ trợ của người quản lí đối với người thực hiện

### Group 598 — topic: Public Health, Preventive Healthcare
Q: Bước 1 trong chu trình lập kế hoạch là gì?
Options (shared set): ['Xác định nguồn lực', 'Xác định mục tiêu', 'Xác định tình hình', 'Lựa chọn giải pháp']
  line   4396 | Easy        | id 82b274af8cfd4aadace05b5c226e4d55 | C -> Xác định tình hình
  line  11104 | Easy        | id 604c4000617a42548065eff25d6db81f | C -> Xác định tình hình

### Group 599 — topic: General Medicine, Public Health
Q: Theo WHO, BS gia đình đóng vai trò...trong việc đạt được các mục tiêu về chất lượng chi phí – hiệu quả tính công bằng trong các hệ thống chăm sóc sức khỏe
Options (shared set): ['Chính', 'Trực tiếp', 'Quan trọng', 'Trung tâm']
  line   4397 | Easy        | id ee6b88944d014a18bf7a16c141786a34 | C -> Quan trọng
  line  11105 | Easy        | id 43f7070ec4444323ba6a83992a812531 | C -> Quan trọng

### Group 600 — topic: Public Health
Q: Biểu đồ hình đường dùng để:
Options (shared set): ['Biểu thị sự tăng tỷ lệ của một hiện tượng theo thời gian', 'Biểu thị sự giảm tỷ lệ của một hiện tượng theo thời gian', 'Biểu thị sự tăng và giảm của một hiện tượng theo thời gian', 'Biểu thị sự biến thiên của một hiện tượng theo thời gian']
  line   4398 | Easy        | id bd89c61166aa478cb16f71a0bc4bdf8c | D -> Biểu thị sự biến thiên của một hiện tượng theo thời gian
  line  11106 | Easy        | id 6d2a6a96849a4adfac272d3e162a032c | D -> Biểu thị sự biến thiên của một hiện tượng theo thời gian

### Group 601 — topic: Public Health, Preventive Healthcare
Q: Một sức khỏe phản ánh bất kì mối quan hệ nào giữa:
Options (shared set): ['Động vật và môi trường', 'Con người, động vật và môi trường', 'Con người và môi trường', 'Động vật và con người']
  line   4399 | Easy        | id 5fcc594b0ebb40c595d0e5e5d4e5a4c4 | B -> Con người, động vật và môi trường
  line  11107 | Medium      | id 0124c96575084a5386e2a692e22781f7 | B -> Con người, động vật và môi trường

### Group 602 — topic: Public Health, Preventive Healthcare
Q: Thiết kế nghiên cứu cung cấp hình ảnh chụp nhanh về tình trạng sức khỏe của quần thể tại thời điểm nghiên cứu là:
Options (shared set): ['Nghiên cứu trường hợp bệnh', 'Nghiên cứu mô tả cắt ngang', 'Nghiên cứu tương quan', 'Nghiên cứu chùm bệnh']
  line   4400 | Easy        | id 4c0ff5cace63435dbbdcf1070b058e3f | B -> Nghiên cứu mô tả cắt ngang
  line  11108 | Easy        | id 5199d41b8fb5410993c118247370fc45 | B -> Nghiên cứu mô tả cắt ngang

### Group 603 — topic: Infectious Diseases, Public Health, Preventive Healthcare
Q: Đặc điểm của muỗi Anopheles:
Options (shared set): ['Trên đường sống cánh có đốm đen trắng ở cánh, Hút máu vào ban ngày, Tư thế đậu song song với mặt phẳng đậu', 'Hút máu vào ban ngày, Tư thế đậu song song với mặt phẳng đậu, Đẻ trứng rời nhau, có phao', 'Tư thế đậu song song với mặt phẳng đậu, Đẻ trứng rời nhau, có phao, Hút máu vào ban ngày', 'Trên đường sống cánh có đốm đen trắng ở cánh, Đẻ trứng rời nhau, có phao, Pan dài xấp xỉ vòi']
  line   4401 | Medium      | id ce3e25dd6a08404ebcf3c91b034acc1f | B -> Hút máu vào ban ngày, Tư thế đậu song song với mặt phẳng đậu, Đẻ trứng rời nhau, có phao
  line  11109 | Medium      | id 3e92f4f1fefb495daa6e0a9246130f83 | B -> Hút máu vào ban ngày, Tư thế đậu song song với mặt phẳng đậu, Đẻ trứng rời nhau, có phao

### Group 604 — topic: Public Health, Preventive Healthcare
Q: Điền cụm từ thích hợp: Quá trình đô thị hóa và phát triển kinh tế bằng con đường công nghiệp hoá đòi hỏi nhu cầu về năng lượng, nguyên liệu ngày càng to lớn, kéo theo chất lượng ….. ngày càng xấu đi nếu không có các biện pháp hữu hiệu ngay từ đầu.
Options (shared set): ['Môi trường làm việc', 'Con người', 'Môi trường sống']
  line   4402 | Easy        | id 1976abf9aa1e4ba8b848b68dba6261e3 | C -> Môi trường sống
  line  11110 | Easy        | id 8957c9c04f4f4d5d99ac0ba7351a3ad1 | C -> Môi trường sống

### Group 605 — topic: Public Health, Infectious Diseases
Q: Vụ dịch có thể xảy ra với những đặc điểm dưới đây NGOẠI TRỪ:
Options (shared set): ['1 ca bệnh truyền nhiễm xảy ra cũng có thể coi là có vụ dịch nếu như bệnh đó rất nguy hiểm', 'ở một hoặc nhiều cộng đồng, quốc gia', 'kéo dài từ nhiều ngày đến nhiều năm.', 'bệnh đó đã không xảy ra trong một thời kỳ dài và đột nhiên xuất hiện lại.']
  line   4403 | Medium      | id a0c4e6370aba41e3a1e80f3d1224af14 | D -> bệnh đó đã không xảy ra trong một thời kỳ dài và đột nhiên xuất hiện lại.
  line  11111 | Medium      | id 58c01135a49645958e281c89c1b663a0 | D -> bệnh đó đã không xảy ra trong một thời kỳ dài và đột nhiên xuất hiện lại.

### Group 606 — topic: Public Health
Q: Nguyên tắc cơ bản trong lập kế hoạch giáo dục sức khỏe là: ?
Options (shared set): ['Lồng ghép với các chương trình văn hoá xã hội đang triển khai tại địa phương', 'Phối hợp với các lãnh đạo cộng đồng', 'Huy động sự tham gia của cộng đồng', 'Huy động sự tham gia của các tổ chức đoàn thể câu hỏi trên']
  line   4404 | Easy        | id ac2a702b8785479f943b5e3fa921245a | A -> Lồng ghép với các chương trình văn hoá xã hội đang triển khai tại địa phương
  line  11112 | Easy        | id 572384a2faec4ce6b3e6ed81f6355f03 | A -> Lồng ghép với các chương trình văn hoá xã hội đang triển khai tại địa phương

### Group 607 — topic: Infectious Diseases, Gastroenterology, Public Health
Q: Trong một số bệnh sán, nước không những là đường truyền nhiễm mà còn là nơi ký sinh vật trải qua chu trình phát triển trong cơ thể vật chủ trung gian?
Options (shared set): ['Đúng', 'Sai']
  line   4405 | Easy        | id de5c82a2836e45f5a0f5480de2c93a3e | A -> Đúng
  line  11113 | Medium      | id 735c7d94654f467d8d045f092c5bee12 | A -> Đúng

### Group 608 — topic: Public Health, Preventive Healthcare
Q: Nghiên cứu nào sau đây thuộc nhóm nghiên cứu phân tích quan sát?
Options (shared set): ['Nghiên cứu chùm bệnh', 'Nghiên cứu can thiệp', 'Nghiên cứu tương quan', 'Nghiên cứu bệnh chứng']
  line   4406 | Medium      | id 9aa5c6501411487382ed3a281f9e3daf | C -> Nghiên cứu tương quan
  line  11114 | Medium      | id ea13aad1afd9400e9dca5dd5b017a015 | C -> Nghiên cứu tương quan

### Group 609 — topic: Obstetrics and Gynecology, Public Health, Preventive Healthcare
Q: Hoạt động nào sau đây không phải là chăm sóc sức khỏe ban đầu:
Options (shared set): ['Chăm sóc sản phụ sau sinh mổ tại viện', 'Tiêm phòng vắc xin uốn ván', 'Chăm sóc rốn trẻ sơ sinh', 'Khám thai định kì']
  line   4407 | Medium      | id 8ee8f861bf49433d81456e7380cbaccc | A -> Chăm sóc sản phụ sau sinh mổ tại viện
  line  11115 | Medium      | id 1bfcba691389433bbe52537ff2233524 | A -> Chăm sóc sản phụ sau sinh mổ tại viện

### Group 610 — topic: Public Health, Preventive Healthcare
Q: Trích dẫn tài liệu tham khảo nào đúng?: Phạm Hồng Lâm (2020), “Tình hình ngộ độc thực phẩm tại Hà Nội năm 2020”, Tạp chí Y học thực hành, 2(5), 10-15.
Options (shared set): ['Phạm Hồng Lâm (2020), Tình hình ngộ độc thực phẩm tại Hà Nội năm 2020, Tạp chí Y học thực hành, 2(5), 10-15.', 'Phạm Hồng Lâm (2020), Tình hình ngộ độc thực phẩm tại Hà Nội năm 2020, Tạp chí Y học thực hành, 2(5), 10-15.', 'Phạm Hồng Lâm (2020), “Tình hình ngộ độc thực phẩm tại Hà Nội năm 2020”, Tạp chí Y học thực hành, 2(5), 10-15.', 'Phạm Hồng Lâm (2020), Tình hình ngộ độc thực phẩm tại Hà Nội năm 2020, Tạp chí Y học thực hành, (2)(5), 10-15.']
  line   4408 | Medium      | id 1913e04c15bb492b92a7dafa90b68c45 | A -> Phạm Hồng Lâm (2020), Tình hình ngộ độc thực phẩm tại Hà Nội năm 2020, Tạp chí Y học thực hành, 2(5), 10-15.
  line  11116 | Medium      | id dfcda85c5b254b7e8e919b6663e4b854 | A -> Phạm Hồng Lâm (2020), Tình hình ngộ độc thực phẩm tại Hà Nội năm 2020, Tạp chí Y học thực hành, 2(5), 10-15.

### Group 611 — topic: Pharmacognosy
Q: Cách thu hái Ma Hoàng:
Options (shared set): ['Thu hái toàn cây cả rễ, bỏ mấu, quả phơi khô nơi mát', 'Thu hải phần trên mặt đất, bỏ mấu, quả, phơi khô nơi mát', 'Thu hái phần trên mặt đất, bỏ mấu, quả, phơi khô nơi mát, phần rễ nếu cần thì thu hái riêng', 'Thu hái phần trên mặt đất, làm sạch, bỏ rễ con, phơi khô nơi mát']
  line   4409 | Easy        | id 524b5bfe159b46b7a6c98b37df053d54 | C -> Thu hái phần trên mặt đất, bỏ mấu, quả, phơi khô nơi mát, phần rễ nếu cần thì thu hái riêng
  line  11117 | Easy        | id fb74c496a8b542deb289fd05462a65cb | C -> Thu hái phần trên mặt đất, bỏ mấu, quả, phơi khô nơi mát, phần rễ nếu cần thì thu hái riêng

### Group 612 — topic: Pharmacognosy
Q: Ma hoàng có chất lượng cao nhất khi thu hái vào thời điểm nào dưới đây
Options (shared set): ['đầu mùa xuân', 'khi cây hết quả', 'Khi cây chuẩn bị ra hoa', 'Cuối thu trước khi sang đông']
  line   4410 | Medium      | id 18801d022616464884c178e4e50d586f | A -> đầu mùa xuân
  line  11118 | Medium      | id 42e8b585f91a403fac3664197a6e07ed | A -> đầu mùa xuân

### Group 613 — topic: Pharmacognosy
Q: Điều nào dưới đây KHÔNG ĐÚNG với cây tỏi độc
Options (shared set): ['Được trồng ở vùng Nam và Trung Âu', 'Alkaloid chính là một Alkaloid có N nằm ngoài vòng', 'Alkaloid chính là 1 protoalkaloid', 'Có tác dụng trong bệnh thống phong']
  line   4411 | Medium      | id 5255b2e769dc49b7b7f0849fe662da77 | B -> Alkaloid chính là một Alkaloid có N nằm ngoài vòng
  line  11119 | Medium      | id e2c330c44a9f4c7dbe793e79f30547ba | B -> Alkaloid chính là một Alkaloid có N nằm ngoài vòng

### Group 614 — topic: Pharmacognosy
Q: Alkaloid nhân tropan có thể gặp trong họ nào sau đây
Options (shared set): ['Họ coca', 'Họ thuốc phiện', 'Họ rau dền', 'Họ đậu']
  line   4412 | Easy        | id 4a1caf8aa7d1418d98e4301694d57371 | A -> Họ coca
  line  11120 | Easy        | id ba01ae2f6ddc4045b1eab8783102a2fc | A -> Họ coca

### Group 615 — topic: Pharmacognosy
Q: Alkaloid nhân tropan có thể gặp trong họ nào sau đây
Options (shared set): ['Họ sen', 'Họ Bìm bìm', 'Họ Bí', 'Họ cải']
  line   4413 | Easy        | id 8f6b5b0f28f84fb298fbde07c4c0bffc | B -> Họ Bìm bìm
  line  11121 | Easy        | id e4ba9cc7500749f09aec03e5b1fa1bd1 | B -> Họ Bìm bìm

### Group 616 — topic: Pharmacognosy
Q: Alkaloid nhân tropan có thể gặp trong họ nào sau đây
Options (shared set): ['Họ củ nâu, họ coca', 'họ ráy, họ thuốc phiện', 'họ cúc, họ rau dền', 'họ gai, họ đậu']
  line   4414 | Easy        | id 920ce24d4f4f4a4a88678a544431acde | A -> Họ củ nâu, họ coca
  line  11122 | Easy        | id 7e109ebf3cda4e0b8f2ee9c0a3e502e6 | A -> Họ củ nâu, họ coca

### Group 617 — topic: Pharmacognosy
Q: Câu nào dưới đây KHÔNG ĐÚNG
Options (shared set): ['Cocain là 1 Alkaloid có nhân tropan', 'Cây coca có nguồn gốc Nam Mỹ', 'C Cocain là 1 Alkaloid có nhãn ergonin', 'cocain có câu trúc là 1 cinamoyl ester']
  line   4415 | Medium      | id 00a9ec97463f47f791be724b3f5e11ab | C -> C Cocain là 1 Alkaloid có nhãn ergonin
  line  11123 | Medium      | id 70c922494df0476cbcd60164473c077d | C -> C Cocain là 1 Alkaloid có nhãn ergonin

### Group 618 — topic: Pharmacognosy
Q: Tỷ lệ các Alkaloid chính trong là cả độc được là
Options (shared set): ['Scopolamin > Hyoscyamin', 'Scopolamin < Hyoscyamin', 'Tùy theo từng cây, từng vùng, từng loài', 'Không so sánh được']
  line   4416 | Medium      | id 1a289294900e432abd15a3723180a2a1 | C -> Tùy theo từng cây, từng vùng, từng loài
  line  11124 | Medium      | id 13494c4b171f4d42a84bd0a5908c20cb | C -> Tùy theo từng cây, từng vùng, từng loài

### Group 619 — topic: Pharmacognosy
Q: Hàm lượng Alkaloid toàn phần trong Cà độc dược cao nhất ở
Options (shared set): ['lá', 'hoa', 'hạt', 'rễ']
  line   4417 | Easy        | id dd1d3dfd34ff4579ade7ef163e7585fa | A -> lá
  line  11125 | Easy        | id a2cfa8b2ca3b43f19627c629f9c140a9 | A -> lá

### Group 620 — topic: Pharmacognosy
Q: Alkaloid có hàm lượng cao nhất trong Cà Độc Dược là
Options (shared set): ['Atropin', 'Hyoscyamin', 'Scopolamin', 'Meteloidin']
  line   4418 | Easy        | id d95cbddab87e4bee850c4da47566f924 | B -> Hyoscyamin
  line  11126 | Easy        | id a43e5a2b039749cba66bbf45017e7d24 | B -> Hyoscyamin

### Group 621 — topic: Pharmacognosy
Q: Xét tỉ lệ phần trăm %, hàm lượng Alkaloid trong dược liệu nào dưới đây lớn nhất
Options (shared set): ['Canhkina', 'Cà phê', 'Nhựa thuốc Phiện', 'Thuốc lá']
  line   4419 | Medium      | id 0af7f6e73f9f493cbe6c5f25f630a680 | C -> Nhựa thuốc Phiện
  line  11127 | Medium      | id 0999cdcf38fa46b2a47fbfa8b366d00a | C -> Nhựa thuốc Phiện

### Group 622 — topic: Pharmacognosy
Q: Trong Canhkina có 2 nhóm alkaloid chính là
Options (shared set): ['Quinolin, quinilon', 'Quinolin. Indol', 'Quinolin, Indolin', 'Quinolon, Imidazol']
  line   4420 | Easy        | id b9b56abf44d241468a578fa860171396 | B -> Quinolin. Indol
  line  11128 | Easy        | id 0a1a519aab5142889341e9934e7fee0c | B -> Quinolin. Indol

### Group 623 — topic: Anatomy
Q: Cơ phân chia thành tam giác cảnh và tam giác cảnh dưới là:
Options (shared set): ['Nhị thân', 'Thang', 'Vai móng', 'Ức đòn chũm']
  line   4421 | Medium      | id c91cf114a3464cfa9f782bea2c6b1292 | D -> Ức đòn chũm
  line  11129 | Medium      | id 71dd2c5866b64be3b7668cd107acc6fe | D -> Ức đòn chũm

### Group 624 — topic: Pulmonology, Anatomy
Q: Đặc điểm của cơ Reissesen ở thành tiểu phế quản:
Options (shared set): ['Tế bào cơ hình thoi', 'Có nhiều vạch bậc thang', 'Có nhiều vân ngang', 'Không có các xơ cơ']
  line   4422 | Easy        | id 104b37475f684b3990343329e9a44f5d | A -> Tế bào cơ hình thoi
  line  11130 | Easy        | id ada57018e1d7436da84974a28c58cd90 | A -> Tế bào cơ hình thoi

### Group 625 — topic: Obstetrics and Gynecology, Anatomy
Q: Đường kính lưỡng ụ ngồi bao nhiêu cm?
Options (shared set): ['9.5', '11', '12', '13']
  line   4423 | Easy        | id fdbde2e9b0bc46b9b5c9386860e213b8 | B -> 11
  line  11131 | Easy        | id 6e96596e12854366b9f8790afb58efc5 | B -> 11

### Group 626 — topic: Anatomy, Cardiology
Q: Cung gan chân cấp máu cho?
Options (shared set): ['Gan chân và các ngón chân', 'Gan chân', 'Ngón chân', '……']
  line   4424 | Medium      | id 4cfb3df030fe47b6b76661be2bc85626 | A -> Gan chân và các ngón chân
  line   9678 | Easy        | id 969621d3b5cb40b6b54254a04a0f15d4 | A -> Gan chân và các ngón chân
  line  11132 | Medium      | id ac74e71b8b9c41f1af791b18802714b5 | A -> Gan chân và các ngón chân

### Group 627 — topic: Anatomy, Neurology
Q: Dây thần kinh nào vận động hầu hết các cơ vùng cẳng tay trước ?
Options (shared set): ['Thần kinh giữa', 'Thần kinh trụ', 'Thần kinh quay', 'Thần kinh cơ bì']
  line   4425 | Easy        | id b51d095395834df7b93fb921ccd35e50 | A -> Thần kinh giữa
  line  11133 | Easy        | id a66dc949e6cc41d28cb09994090ccf1f | A -> Thần kinh giữa

### Group 628 — topic: Anatomy
Q: Đường ngang qua gai vai của xương bả vai tương ứng với đốt sống:
Options (shared set): ['Đốt sống C7 -N1', 'Đốt sống N2 - N3', 'Đốt sống N1 –N2', 'Đốt sống N3 –N4']
  line   4426 | Medium      | id 7745e3e6e81b4ab59e194cd7762225da | A -> Đốt sống C7 -N1
  line  11134 | Medium      | id 9f8394e76fdb43d686c527e46b4577c4 | A -> Đốt sống C7 -N1

### Group 629 — topic: Anatomy, Otolaryngology
Q: Xương nào sau đây thuộc xương sọ mặt?
Options (shared set): ['Xương xoăn mũi dưới', 'Xương châm', 'Xương đinh', 'Xương trán']
  line   4427 | Easy        | id a80c78de0355468bb4e2e601ddefb6dd | A -> Xương xoăn mũi dưới
  line  11135 | Easy        | id aaaf56e3268b463095ed7cb7ee22f4a5 | A -> Xương xoăn mũi dưới

### Group 630 — topic: General Medicine, Anatomy
Q: Nói về giới hạn vùng bụng, câu nào sau đây đúng?
Options (shared set): ['Phía trên là cơ hoành', 'Hai bên là mạn sườn', 'Phía sau là cột sống và các cơ lưng', 'Phía dưới là hai xương chậu']
  line   4428 | Easy        | id 920ca640b7044eb98847aa89394064ac | B -> Hai bên là mạn sườn
  line  11136 | Easy        | id 121a19133b4341329c2c3124bfce57b2 | B -> Hai bên là mạn sườn

### Group 631 — topic: Anatomy
Q: Chi tiết nào sau đây thuộc về đầu dưới xương cánh tay?
Options (shared set): ['Hố quay', 'Khuyết ròng rọc', 'Rãnh gian cũ', 'A và b đúng']
  line   4429 | Easy        | id 6fbd68333d3846a38f2aea270aaaf739 | D -> A và b đúng
  line  11137 | Easy        | id 92e33a3cf2d945409005a3348eb16d0b | D -> A và b đúng

### Group 632 — topic: Anatomy
Q: Cơ nào sau đây vừa có động tác sấp cẳng tay, vừa có động tác ngửa cẳng tay:
Options (shared set): ['Cơ ngửa', 'Cơ sấp vuông', 'Cơ cánh tay', 'Cơ cánh tay quay']
  line   4430 | Easy        | id 46705efa53804e23905abd57db829dc4 | D -> Cơ cánh tay quay
  line  11138 | Medium      | id 0cc8630a6aee45af93fff0ca4f7026b5 | D -> Cơ cánh tay quay

### Group 633 — topic: General Medicine, Anatomy
Q: Ngành động vật nào dưới đây thuộc nhóm động vật có đối xứng hai bên?
Options (shared set): ['Giun dẹp (1)', 'Đúng cả (1), (2), (3)', 'Giun đất (3)', 'Giun tròn (2)']
  line   4431 | Easy        | id 3b8939ef7c6643488c695220b1a75be9 | B -> Đúng cả (1), (2), (3)
  line  11139 | Easy        | id a0ea8ce4a88948b2b545700fedd9a3f3 | B -> Đúng cả (1), (2), (3)

### Group 634 — topic: Anatomy
Q: Cơ ngực lớn, cơ ngực bé tạo nên thành nào của nách?
Options (shared set): ['Thành trước', 'Thành sau', 'Thành trong', 'Thành ngoài']
  line   4432 | Easy        | id 43675677681546e595a8f281d9b43c76 | A -> Thành trước
  line  11140 | Medium      | id 5427d6c9c5d64d36920413b398f187f6 | A -> Thành trước

### Group 635 — topic: Cardiology, Anatomy
Q: Tim trong trung thất
Options (shared set): ['Giữa', 'Trước', 'Sau', 'Dưới']
  line   4433 | Easy        | id d5a2f20b570a4aefa1f95be690df8823 | A -> Giữa
  line  11141 | Easy        | id 4fc2f93f6d4145cd9b3821bb64f2a980 | A -> Giữa

### Group 636 — topic: Obstetrics and Gynecology, Anatomy
Q: Các tuyến trong bộ phận nào khi có thai thường chế tiết rất ít hoặc không chế tiết?
Options (shared set): ['Sừng tử cung', 'Thân tử cung', 'Eo tử cung', 'Cổ tử cung']
  line   4434 | Easy        | id 0be335a876a64114b9123196a60a04d6 | D -> Cổ tử cung
  line  11142 | Easy        | id 7eb0ca28d62a4cffb7d48df9238b4c50 | D -> Cổ tử cung

### Group 637 — topic: General Medicine, Anatomy
Q: Đường nách giữa là gì?
Options (shared set): ['Đường nách trước', 'Đường nách giữa', 'Đường nách sau', 'Giữa hõm nách']
  line   4435 | Easy        | id c9692373603d443cb1c13ff154f24bc4 | D -> Giữa hõm nách
  line  11143 | Easy        | id cf39237132ef406fa65fa16163ff9aeb | D -> Giữa hõm nách

### Group 638 — topic: Radiology, Anatomy
Q: Đoạn cột sống nào khó chụp X-quang?
Options (shared set): ['Đoạn cổ', 'Đoạn lưng', 'Đoạn cùng', 'Đoạn cụt']
  line   4436 | Medium      | id 06d66f2b10a941fdb03b4c437740e30b | C -> Đoạn cùng
  line  11144 | Medium      | id 8c1ce1f28cc64a7cb8c42e0fc7484189 | C -> Đoạn cùng

### Group 639 — topic: General Medicine, Anatomy
Q: Trong cách phân chia vùng bụng dựa vào 2 đường thẳng ngang và 2 đường thẳng dọc, bụng được chia thành 9 vùng, trong đó 2 vùng dưới rốn là hạ vị và tầng sinh môn?
Options (shared set): ['Đúng', 'Sai', 'Không có', 'Không có']
  line   4437 | Medium      | id fff05d6d49d64e3aa31a0d05fd31804a | B -> Sai
  line  11145 | Medium      | id f65cd222d4064885b1cf6251f7e74107 | B -> Sai

### Group 640 — topic: Pulmonology, Anatomy
Q: Xác định thứ tự nhỏ dần của các đơn vị phổi
Options (shared set): ['Thùy phổi, phân thùy phổi, tiểu thùy, phế nang', 'Phân thùy phổi, tiểu thùy, phế nang, thùy phổi', 'Thùy phổi, phân thùy phổi, phế nang tiểu thùy', 'Phân thùy phổi, phân thùy phổi, tiểu thùy, phế nang']
  line   4438 | Easy        | id aef3d76556db4d4f85330f69aaa2c0cb | A -> Thùy phổi, phân thùy phổi, tiểu thùy, phế nang
  line  11146 | Easy        | id dd9fd99b729e4b51be7f012782902199 | A -> Thùy phổi, phân thùy phổi, tiểu thùy, phế nang

### Group 641 — topic: General Medicine, Anatomy
Q: Khi phân chia vùng bụng dựa vào 2 đường thẳng ngang và 2 đường thẳng dọc, bụng được chia thành 8 vùng
Options (shared set): ['Đúng', 'Sai', 'Biết đếm là chọn đúng liền nè :v.', 'Không có']
  line   4439 | Easy        | id b24917efb1444d939599bdff83e0b502 | B -> Sai
  line  11147 | Easy        | id 79c2755794ce4f75b29bca21139b9701 | B -> Sai

### Group 642 — topic: Hematology, Anatomy
Q: Các thân bạch huyết nào đổ vào ống ngực?
Options (shared set): ['thân cảnh trái,thân dưới đòn trái', 'thân cảnh phải thân dưới đòn phải', 'thân thắt lưng,thân cảnh phải', 'thân dưới đòn phải,thân ruột']
  line   4440 | Medium      | id 86d7b2329f2c4ffd8b5471db12962bee | A -> thân cảnh trái,thân dưới đòn trái
  line  11148 | Medium      | id 2a9b02385a954675960e278125ebc524 | A -> thân cảnh trái,thân dưới đòn trái

### Group 643 — topic: Obstetrics and Gynecology, Anatomy
Q: Khi có thai, hình dáng cổ tử cung thay đổi nhiều?
Options (shared set): ['Đ', 'S']
  line   4441 | Medium      | id 95c9829eef43468faec81c4115006aeb | A -> Đ
  line  11149 | Medium      | id 69ee9183effb498fabb8b94c315c280d | A -> Đ

### Group 644 — topic: Otolaryngology, Anatomy
Q: Xương nào tham gia tạo nên sàn hốc mũi?
Options (shared set): ['Xương lệ', 'Xương khẩu cái', 'Xương sàng', 'Xương trán']
  line   4442 | Easy        | id 45a964f839a8425d9913bcd183d080a8 | B -> Xương khẩu cái
  line  11150 | Easy        | id 4e3a3160f0f24923b7c6f822f45e18c8 | B -> Xương khẩu cái

### Group 645 — topic: Anatomy, Immunology
Q: Tế bào võng – biểu mô, đại thực bào và tế bào nội mô mao mạch vùng vỏ tuyến ức đảm nhiệm vai trò nào sau đây?
Options (shared set): ['Tạo ra những tiểu thể Hassell', 'Sinh sản lympho T và lympho B', 'Biệt hóa tế bào võng biểu mô', 'Ngăn lympho T tiếp xúc với kháng nguyên']
  line   4443 | Medium      | id cf3f1e748dc741f0802f5f09f67167b7 | D -> Ngăn lympho T tiếp xúc với kháng nguyên
  line   7790 | Medium      | id 161e8fc915c34f2094aaafab2465b02d | A -> Ngăn lympho T tiếp xúc với kháng nguyên
  line  11151 | Medium      | id abc62f92631e48078e6128ed86a6f45e | D -> Ngăn lympho T tiếp xúc với kháng nguyên

### Group 646 — topic: Neurology, Ophthalmology, Anatomy
Q: Bệnh nhân nữ 25 tuổi, vào viện với lý do nhãn cầu không nhìn được xuống dưới ra ngoài, đi cầu thang hay bị ngã. Liệt cơ nào sau đây là nguyên nhân của biểu hiện nói trên?
Options (shared set): ['Cơ thẳng trong', 'Cơ thẳng ngoài', 'Cơ chéo trên', 'Cơ chéo dưới']
  line   4444 | Medium      | id dd0f99f418e04a47848e2a08396a94ca | C -> Cơ chéo trên
  line  11152 | Medium      | id cc82869475a74b3bbee3f6e13b36fb7b | C -> Cơ chéo trên

### Group 647 — topic: Obstetrics and Gynecology, Anatomy
Q: trong các dây chằng tử cung, dây chằng nào đi vào ống bẹn?
Options (shared set): ['Dây chằng rộng', 'Dây chằng tròn', 'Dây chằng tử cung cùng', 'Dây chằng ngang cổ tử cung']
  line   4445 | Medium      | id d5af5989aa884d9cbf7fac0331a65661 | B -> Dây chằng tròn
  line  11153 | Medium      | id 2e56a81c25b941ac90ead111fb4e9a54 | B -> Dây chằng tròn

### Group 648 — topic: Anatomy
Q: Cơ tùy hành động mạch quay là cơ ...
Options (shared set): ['Cơ gan tay bé.', 'Cơ gan tay lớn.', 'Cơ ngửa dài (cánh tay quay).', 'Cơ trụ trước.']
  line   4446 | Easy        | id 878c25ddc11f4386a5cfff2593bc4b8f | C -> Cơ ngửa dài (cánh tay quay).
  line  11154 | Easy        | id df5ebd21e59c46d28fa0fa561553de02 | C -> Cơ ngửa dài (cánh tay quay).

### Group 649 — topic: Pulmonology, Cardiology, Anatomy
Q: Có bao nhiêu tĩnh mạch phổi đổ về nhĩ trái?
Options (shared set): ['4', '2', '3', '6']
  line   4447 | Easy        | id d7afdb4ef1d2422aafabb73afec276b4 | A -> 4
  line  11155 | Easy        | id 31a4419acfe944af9afb7ff9400ff050 | A -> 4

### Group 650 — topic: Otolaryngology, Anatomy
Q: Hệ thống xoang sau gồm có:
Options (shared set): ['Xoang sàng trước và xoang trán', 'Xoang hàm và xoang trán', 'Xoang bướm và xoang sàng sau', 'Xoang bướm và xoang hàm']
  line   4448 | Easy        | id bcfb2f5b5fb947fd9e522a97d4aaa840 | C -> Xoang bướm và xoang sàng sau
  line  11156 | Easy        | id f8b5a95d61724d60911e46e722f6e41d | C -> Xoang bướm và xoang sàng sau

### Group 651 — topic: Pulmonology, Anatomy
Q: Phần nào không được màng phổi bao bọc?
Options (shared set): ['Rốn phổi', 'Cuống phổi', 'Đỉnh phổi', 'Đáy phổi']
  line   4449 | Easy        | id 0838d3d1f50f45a483803bffe9908fef | A -> Rốn phổi
  line  11157 | Easy        | id 79e33f98f05943bea359f40593e86c47 | A -> Rốn phổi

### Group 652 — topic: Neurology, Anatomy
Q: Dây thần kinh số XII chui qua lỗ nào của nền sọ?
Options (shared set): ['Lỗ rách sau', 'Lỗ tai trong', 'Lỗ chẩm', 'Lỗ hạ thiệt']
  line   4450 | Medium      | id d5d13094e4f8457681596c1dfa72f115 | D -> Lỗ hạ thiệt
  line  11158 | Medium      | id 60f53aecd45f4c2b9f6ad735f56366ce | D -> Lỗ hạ thiệt

### Group 653 — topic: Cardiology, Anatomy
Q: Mô tả nào dưới đây là đúng về hệ thống tĩnh mạch?
Options (shared set): ['Tĩnh mạch chủ trên dẫn máu đổ về tâm nhĩ trái', 'Tĩnh mạch phổi dẫn máu đổ về tâm nhĩ phải', 'TM cửa đổ trực tiếp vào TM chủ dưới', 'TM phổi dẫn máu đỏ tươi về tâm nhĩ trái']
  line   4451 | Medium      | id 15b0b13a1450458395c49990846e2027 | D -> TM phổi dẫn máu đỏ tươi về tâm nhĩ trái
  line  11159 | Medium      | id 9a8d1c9f20874120aceec67bf7e2e954 | D -> TM phổi dẫn máu đỏ tươi về tâm nhĩ trái

### Group 654 — topic: Urology, Anatomy
Q: Hiện tượng cương dương vật là do nguyên nhân nào sau đây?
Options (shared set): ['Máu ứ đầy trong vật hang và vật xốp', 'Máu ứ giữa lớp mạc nông và lớp mạc sâu dương vật', 'Máu ứ ở các tĩnh mạch nông của dương vật', 'Các tạng cương dương vật bị xơ hóa tạm thời']
  line   4452 | Medium      | id dc7a940cf49d44399755230a1eb7a23e | A -> Máu ứ đầy trong vật hang và vật xốp
  line  11160 | Medium      | id 74ed621b303c4a8e9448816b2a326fb7 | A -> Máu ứ đầy trong vật hang và vật xốp

### Group 655 — topic: Anatomy
Q: Rãnh chữ H chia gan làm 4 thùy là:
Options (shared set): ['Thùy đuôi', 'Thùy đầu', 'Thùy trái, Thùy đuôi', 'Thùy phải, Thùy trái, Thùy đuôi']
  line   4453 | Medium      | id c567baaf093e4a50bf97d1aadec57a5e | D -> Thùy phải, Thùy trái, Thùy đuôi
  line  11161 | Medium      | id 0d58a3e7de8d4a3f85c8a12a4c8fd9a7 | D -> Thùy phải, Thùy trái, Thùy đuôi

### Group 656 — topic: Urology, Anatomy
Q: Độ dài ống dẫn tinh, đường kính ngoài, đường kính trong?
Options (shared set): ['35-40, 4-5, 1', '40-45, 4-5, 1', '40-45, 2-3, 0,5', '35-40, 2-3, 0,5']
  line   4454 | Medium      | id 0361b4ed40c747cd9a991e1c9feabc2f | C -> 40-45, 2-3, 0,5
  line  11162 | Medium      | id 95ff3722859a43fd9cf70881b4e5bdd8 | C -> 40-45, 2-3, 0,5

### Group 657 — topic: Obstetrics and Gynecology, Anatomy
Q: Đoạn nào của vòi trúng có đường kính lớn nhất
Options (shared set): ['Đoạn thành', 'Đoạn co', 'Đoạn bóng', 'Đoạn loa']
  line   4455 | Easy        | id a095a58485054f1aa14ce9c7811fb0e0 | C -> Đoạn bóng
  line  11163 | Easy        | id 448d419646c84d05b59ff05d32c49d6e | C -> Đoạn bóng

### Group 658 — topic: Neurology, Anatomy
Q: Cơ mông nhỡ, cơ mông bé và cơ căng mạc đùi, do dây thần kinh nào vận động ?
Options (shared set): ['Thần kinh mông trên', 'Thần kinh mông dưới', 'Thần kinh tọa', 'Thần kinh bịt']
  line   4456 | Easy        | id b2de53ed20bb45369da7c4552c47fe7e | A -> Thần kinh mông trên
  line  11164 | Easy        | id 6c140436e4614edfa2b13aaaf0aa4d90 | A -> Thần kinh mông trên

### Group 659 — topic: Otolaryngology, Anatomy
Q: Nhóm nào sau đây thuộc nhóm cơ thớ vòng trong hầu
Options (shared set): ['Cơ trâm hầu, Cơ vòi hầu, Cơ khẩu cái hầu', 'Cơ khẩu cái hầu, Cơ khít hầu , Cơ vòi hầu', 'Cơ vòi hầu,Cơ trâm hầu, Cơ khẩu cái hầu', 'Ba cơ khít hầu']
  line   4457 | Medium      | id b31a423cd19d467fb1fbf9de80aaf515 | D -> Ba cơ khít hầu
  line  11165 | Medium      | id 8976940aee634c07a40cb8d892e989bc | D -> Ba cơ khít hầu

### Group 660 — topic: General Medicine, Anatomy
Q: Đặc điểm chỉ có khi cơ co:
Options (shared set): ['Xơ actin lồng vào xơ myozin.', 'Đĩa A không đổi.', 'Vạch H hẹp lại.', 'Xơ actin trượt trên xơ myozin.']
  line   4458 | Medium      | id 39369ce14a854461a7984eef7310e0ef | D -> Xơ actin trượt trên xơ myozin.
  line  11166 | Medium      | id a63f9a79d07544f18c25e8fc20bcc09f | D -> Xơ actin trượt trên xơ myozin.

### Group 661 — topic: Otolaryngology, Anatomy
Q: Amidan được nuôi dưỡng bởi các động mạch sau, NGOẠI TRỪ:
Options (shared set): ['Khẩu cái xuống', 'Khẩu cái lên', 'Bướm khẩu cái', 'Nhánh khẩu cái của động mạch hầu']
  line   4459 | Medium      | id b4f877a9619e487fad7129f186cdfa7f | C -> Bướm khẩu cái
  line  11167 | Medium      | id 99ae1395374342929e745db8a2328a8c | C -> Bướm khẩu cái

### Group 662 — topic: Dentistry, Anatomy
Q: Khe chân bướm hàm là:
Options (shared set): ['Khe hình giọt nước, giới hạn phía trước là bờ sau xương hàm dưới, phía sau là phần trước mỏm chân bướm của xương bướm', 'Khe hình giọt nước, giới hạn phía sau là bờ sau xương hàm trên, phía trước là phần trước mỏm chân bướm của xương bướm', 'Điểm thấp nhất của khe chân bướm hàm là PNS', 'Khe hình giọt nước, giới hạn phía trước là bờ sau xương hàm trên, phía trước là phần trước mỏm chân bướm của xương bướm']
  line   4460 | Medium      | id d38ce9f8f6a94f38acb936636fa368bb | A -> Khe hình giọt nước, giới hạn phía trước là bờ sau xương hàm dưới, phía sau là phần trước mỏm chân bướm của xương bướm
  line  11168 | Medium      | id b0cce3a25b4d4da28fe624c5b7556f7f | A -> Khe hình giọt nước, giới hạn phía trước là bờ sau xương hàm dưới, phía sau là phần trước mỏm chân bướm của xương bướm

### Group 663 — topic: Pathology, Anatomy
Q: Cấu trúc không có ở vùng tuỷ của hạch:
Options (shared set): ['Mô võng.', 'Xoang trung gian.', 'Dây xơ.', 'Dây tuỷ.']
  line   4461 | Easy        | id 415076fd525441bea282cb008ef07e50 | C -> Dây xơ.
  line  11169 | Easy        | id 2f363a2f63b24e879c3bdc83f47563f5 | C -> Dây xơ.

### Group 664 — topic: Anatomy
Q: Thành phần không tham gia cấu tạo tuỷ trắng của lách:
Options (shared set): ['Tiểu động mạch lách.', 'Trung tâm sinh sản.', 'áo bạch huyết.', 'Mô võng.']
  line   4462 | Easy        | id a5f9e862e10b428c9b7f123588f71cf4 | A -> Tiểu động mạch lách.
  line  11170 | Easy        | id 5e122fbe747249b2b0e7451283df7e38 | A -> Tiểu động mạch lách.

### Group 665 — topic: Anatomy
Q: Tĩnh mạch nông ở cổ liên quan với thần kinh ngang cổ và thần kinh trên vai là?
Options (shared set): ['Tĩnh mạch tai sau', 'Tĩnh mạch cảnh trước', 'Tĩnh mạch cảnh trong', 'Tĩnh mạch cảnh ngoài']
  line   4463 | Easy        | id 2a697c6305bf4875afdd308d5fe5f08c | D -> Tĩnh mạch cảnh ngoài
  line  11171 | Easy        | id f83e060a9a3541daaba68a3f53956130 | D -> Tĩnh mạch cảnh ngoài

### Group 666 — topic: Neurology, Anatomy
Q: Não được tưới máu bởi hai hệ thống động mạch:
Options (shared set): ['Hệ động mạch cảnh trong, Hệ thống động mạch thái dương', 'Hệ động mạch cảnh trong, Hệ thống mạch sống - nền', 'Hệ động mạch cảnh ngoài, Hệ thống mạch sống - nền', 'Hệ động mạch cảnh ngoài, Hệ thống động mạch thái dương']
  line   4464 | Medium      | id b155ae22fb4c468d93e87391e1ed1906 | B -> Hệ động mạch cảnh trong, Hệ thống mạch sống - nền
  line  11172 | Medium      | id 48e059f5eca349cabeb216566d4efad8 | B -> Hệ động mạch cảnh trong, Hệ thống mạch sống - nền

### Group 667 — topic: Cardiology, Pulmonology, Anatomy
Q: Hệ động mạch phổi bắt nguồn từ …
Options (shared set): ['Tâm thất phải, có nhiệm vụ trao đổi khí.', 'Tâm thất trái, có nhiệm vụ nuôi dưỡng.', 'Tâm thất phải, có nhiệm vụ nuôi dưỡng.', 'Tâm thất trái, có nhiệm vụ trao đổi khí.']
  line   4465 | Medium      | id e45ba4ef2041441c999d74d7c03b0e28 | A -> Tâm thất phải, có nhiệm vụ trao đổi khí.
  line  11173 | Medium      | id 88ee7a4bb6b3473b95e02e4521a9e1da | A -> Tâm thất phải, có nhiệm vụ trao đổi khí.

### Group 668 — topic: Anatomy
Q: Bạch huyết của mũi đổ vào đâu?
Options (shared set): ['Các hạch cổ sâu', 'Các hạch cổ nông', 'Ống ngực', 'Thân bạch huyết dưới đòn trái']
  line   4466 | Easy        | id 456fb3ca42614444b11cc9a961348459 | A -> Các hạch cổ sâu
  line  11174 | Easy        | id c44b00b412cb4ec499810d3c143787d2 | A -> Các hạch cổ sâu

### Group 669 — topic: Dermatology, Anatomy
Q: Đâu không phải đặc điểm cấu tạo của móng?
Options (shared set): ['Phần biểu bì dưới thân móng gọi là giường móng', 'Móng có 4 bờ: bờ tự do, sau và 2 bờ bên', 'Phần móng bị nếp gấp trên che mất là rễ móng', 'Phần biểu bì dưới rễ móng gọi là liềm móng']
  line   4467 | Medium      | id 4f5ca7a88f6048e7bbd98324c6ee67cd | D -> Phần biểu bì dưới rễ móng gọi là liềm móng
  line  11175 | Medium      | id b9698e6580634bdab3ceaae5ec833f0f | D -> Phần biểu bì dưới rễ móng gọi là liềm móng

### Group 670 — topic: Anatomy
Q: Các khe và rãnh chia tủy gai thành các thừng chất trắng:
Options (shared set): ['Thừng bên: Ở giữa rãnh sau và khe giữa', 'Thừng bên: Ở giữa rãnh bên trước và rãnh bên sau', 'Thừng sau: ở giữa rãnh bên trước và rãnh giữa', 'Thừng sau: ở giữa rãnh bên trước và khe giữa']
  line   4468 | Medium      | id 015779359f854acb94298bd167efa70e | B -> Thừng bên: Ở giữa rãnh bên trước và rãnh bên sau
  line  11176 | Medium      | id e554adb5a1a349d9b6734c50ad1c9f17 | B -> Thừng bên: Ở giữa rãnh bên trước và rãnh bên sau

### Group 671 — topic: Urology, Anatomy
Q: Vị trí nào là vị trí của túi tinh:
Options (shared set): ['Mặt sau bàng quang', 'Mặt sau tử cung', 'Mặt sau tuyến tiền liệt', 'Mặt sau tinh hoàn']
  line   4469 | Easy        | id 06e00c85131f41ea8fa4138a3c33116a | A -> Mặt sau bàng quang
  line  11177 | Easy        | id 2899476eefcd4c45a13165b7cb8c1133 | A -> Mặt sau bàng quang

### Group 672 — topic: Anatomy, Neurology
Q: Chọn ý đúng: Hố lào chứa...
Options (shared set): ['Nhánh sâu của dây thần kinh quay.', 'Động mạch quay.', 'Gân duỗi riêng ngón trỏ.', 'Tĩnh mạch đầu.']
  line   4470 | Medium      | id 8e25f78e99d748c2a84f4b581ad75a32 | B -> Động mạch quay.
  line  11178 | Medium      | id 43e361917b8f404c8afeec0022b264af | B -> Động mạch quay.

### Group 673 — topic: Anatomy
Q: Cơ thuộc thành sau vùng nách là cơ nào?
Options (shared set): ['Cơ đen ta, cơ tam đầu', 'Cơ dưới vai, cơ tam đầu, cơ lưng rộng, cơ tròn lớn, cơ tròn bé, cơ trên gai, cơ dưới gai']
  line   4471 | Medium      | id 21384629025c48a8b7b11891e23d1ac9 | B -> Cơ dưới vai, cơ tam đầu, cơ lưng rộng, cơ tròn lớn, cơ tròn bé, cơ trên gai, cơ dưới gai
  line  11179 | Medium      | id de506b87dcd7480a925b0de83357e27a | B -> Cơ dưới vai, cơ tam đầu, cơ lưng rộng, cơ tròn lớn, cơ tròn bé, cơ trên gai, cơ dưới gai

### Group 674 — topic: Obstetrics and Gynecology, Anatomy
Q: Động mạch tử cung là nhánh của
Options (shared set): ['Động mạch chậu chung', 'Động mạch chậu trong', 'Động mạch chậu ngoài', 'Động mạch sinh dục']
  line   4472 | Easy        | id 1c6b233a62e148be8800f06d206503ae | B -> Động mạch chậu trong
  line  11180 | Easy        | id 37a3f801eccb4d88b88afc98d3aeca86 | B -> Động mạch chậu trong

### Group 675 — topic: Gastroenterology, Anatomy
Q: 14. độ đài tá tràng:
Options (shared set): ['15-25cm', '20-30cm', '30cm', '20-25cm']
  line   4473 | Easy        | id 23b9628928254b93900c944b9ea6507e | D -> 20-25cm
  line  11181 | Easy        | id c5c4fe683e7c4a0a860749aae164df1c | D -> 20-25cm

### Group 676 — topic: Ophthalmology, Anatomy
Q: Bộ phận trong suốt của mắt là gì?
Options (shared set): ['Giác mạc', 'Mống mắt', 'Thủy tinh thể', 'Nhân mắt']
  line   4474 | Easy        | id cd64d8e9ea6e46708a854f10cb581ab5 | A -> Giác mạc
  line  11182 | Easy        | id a6d6a6c437334f15ad8d3c9809219bac | A -> Giác mạc

### Group 677 — topic: Obstetrics and Gynecology, Anatomy
Q: Dây chằng nào nối buồng trứng với vòi trứng?
Options (shared set): ['Dây chằng treo buồng trứng', 'Dây chằng riêng buồng trứng', 'Dây chằng rộng', 'Dây chằng tròn']
  line   4475 | Easy        | id 6866310f7d3f4a6da670cd30138d5199 | A -> Dây chằng treo buồng trứng
  line  11183 | Easy        | id 207e870d27514c4fa228d47a2dcea77f | A -> Dây chằng treo buồng trứng

### Group 678 — topic: Anatomy, Otolaryngology
Q: Vị trí ngăn cách của khoang miệng với đằng trước và đằng sau?
Options (shared set): ['Tiền đình miệng', 'Eo miệng và khẩu hầu', 'Khe miệng và eo họng', 'Eo họng']
  line   4476 | Medium      | id c6a0f451ac5444f6b22637c36c2020f2 | B -> Eo miệng và khẩu hầu
  line  11184 | Medium      | id db4d51021fa544ae9e558b9a2aab3b04 | B -> Eo miệng và khẩu hầu

### Group 679 — topic: Anatomy, Neurology
Q: Thành phần nào sau đây KHÔNG nằm trong tam giác dưới hàm?
Options (shared set): ['Động mạch lưỡi', 'Động mạch mặt', 'Thần kinh XI', 'Thần kinh XII']
  line   4477 | Medium      | id df2cf7824b644e94a6288075d795db80 | C -> Thần kinh XI
  line  11185 | Medium      | id 758e85ecc30f4ee6abfc6b1ff0bffab7 | C -> Thần kinh XI

### Group 680 — topic: Gastroenterology, Anatomy
Q: Ống Wirsung thuộc tuyến gì?
Options (shared set): ['Ống tuyến tụy', 'Ống mật chủ', 'Không có đáp án', 'Không có đáp án']
  line   4478 | Easy        | id 835bac542ac049da943ca389b2395b2c | A -> Ống tuyến tụy
  line  11186 | Easy        | id 49ca040cff3244bd92c7969b5deb82cd | A -> Ống tuyến tụy

### Group 681 — topic: Anatomy, Pulmonology
Q: Phân thùy phổi
Options (shared set): ['Có hình trụ, đáy ở bề mặt phổi,đỉnh ở rốn phổi', 'Có hình trụ, đáy ở rốn phổi,đỉnh ở bề mặt phổi', 'Có hình tháp, đáy ở rốn phổi,đỉnh ở bề mặt phổi', 'Có hình tháp, đáy ở bề mặt phổi,đỉnh ở rốn phổi']
  line   4479 | Easy        | id 5791002e594845b7b31ec0ca938d749d | D -> Có hình tháp, đáy ở bề mặt phổi,đỉnh ở rốn phổi
  line  11187 | Easy        | id e70c27bfc752428daadf611d1d646957 | D -> Có hình tháp, đáy ở bề mặt phổi,đỉnh ở rốn phổi

### Group 682 — topic: Cardiology, Anatomy
Q: Về cấu tạo của cơ tim: Giống cơ trơn là có các vân sáng và vân tối.
Options (shared set): ['Đúng', 'Sai']
  line   4480 | Medium      | id 0f6a930f961f4f1aaaf7891f2121f90f | B -> Sai
  line  11188 | Medium      | id 13750ee0922a4d198d795445c07bcb20 | B -> Sai

### Group 683 — topic: Anatomy
Q: Cơ nào KHÔNG thuộc nhóm cơ vùng cẳng chân sau?
Options (shared set): ['Cơ bụng chân', 'Cơ dép', 'Cơ chày sau', 'Cơ duỗi ngón cái dài']
  line   4481 | Easy        | id bd259cf26eec49b2abf4306b65c009d7 | D -> Cơ duỗi ngón cái dài
  line  11189 | Easy        | id 0d9ef04a54d3417e86659c57936300c9 | D -> Cơ duỗi ngón cái dài

### Group 684 — topic: Otolaryngology, Anatomy
Q: Lòng thanh quản:
Options (shared set): ['Là một ống dài, các chiều bằng nhau', 'Là một ống hẹp bề ngang và rộng theo chiều trước sau', 'Bằng với hạ họng và nằm gọn ở giữa hạ họng', 'Có lỗ trên trên bình diện ngang']
  line   4482 | Easy        | id f1190a26fc19478ba74962657b9b6e52 | B -> Là một ống hẹp bề ngang và rộng theo chiều trước sau
  line  11190 | Easy        | id 667f6526ca41423b923cacda3f668c04 | B -> Là một ống hẹp bề ngang và rộng theo chiều trước sau

### Group 685 — topic: Ophthalmology, Anatomy
Q: Thành phần cấu tạo nên màng bồ đào:
Options (shared set): ['Mống mắt, thể mi, giác mạc', 'Mống mắt, giác mạc, củng mạc', 'Mống mắt, thể mi, hắc mạc', 'Mống mắt, võng mạc, hắc mạc']
  line   4483 | Easy        | id fb9774f5e68c4ca3b9abdc2faba4b218 | C -> Mống mắt, thể mi, hắc mạc
  line  11191 | Easy        | id b786404645a84e4984e13d8341145aac | C -> Mống mắt, thể mi, hắc mạc

### Group 686 — topic: Anatomy, Neurology
Q: Chi tiết số 5 là
Options (shared set): ['Rễ trước tủy sống', 'Rễ sau tủy sống', 'Dây thần kinh sống', 'Nhánh trước dây thần kinh sống']
  line   4484 | Medium      | id a7cf2befa0154d07b10be542e5b839a9 | A -> Rễ trước tủy sống
  line  11192 | Medium      | id 0fb3b3c5fa4e4e98a2f2af208853bfbf | A -> Rễ trước tủy sống

### Group 687 — topic: Neurology, Anatomy
Q: Dây thần kinh nào chi phối cơ căng mạc đùi?
Options (shared set): ['TK mông trên', 'TK mông dưới', 'Nhánh của đám rối TK cùng', 'Tk đùi']
  line   4485 | Medium      | id 34711b5911ea47ef87150ac8a8621dfc | A -> TK mông trên
  line  11193 | Medium      | id 7d9c2b41a6214d7287f48228820bd10c | A -> TK mông trên

### Group 688 — topic: Gastroenterology, Anatomy
Q: Ruột già gồm những thành phần nào:
Options (shared set): ['Tá tràng, hỗng tràng, hồi tràng', 'Tá tràng, đại tràng, manh tràng', 'Manh tràng, trực tràng, đại tràng, ống hậu môn', 'Đại tràng, tiểu tràng, ống hậu môn']
  line   4486 | Easy        | id 569b6148ee374b3d9636d21824ac4d59 | C -> Manh tràng, trực tràng, đại tràng, ống hậu môn
  line  11194 | Easy        | id 2a1d47ac5c014a00b319d06d6061dec8 | C -> Manh tràng, trực tràng, đại tràng, ống hậu môn

### Group 689 — topic: Anatomy, Hematology
Q: Thành phần tham gia cấu trúc tuỷ trắng của lách:
Options (shared set): ['Dây xơ.', 'Dây Billroth.', 'Dây tuỷ.', 'Trung tâm sinh sản.']
  line   4487 | Easy        | id 4daf89b933ba4abc8c7c8e62b2db1c08 | D -> Trung tâm sinh sản.
  line  11195 | Easy        | id 7721fd14467c4507b090d62ae3b16f86 | D -> Trung tâm sinh sản.

### Group 690 — topic: Anatomy
Q: Hệ bạch huyết của lưỡi chủ yếu đổ vào
Options (shared set): ['Các hạch khẩu cái', 'Các hạch cổ sâu', 'Các hạch lợi', 'Các hạch dưới hàm']
  line   4488 | Easy        | id 1a8cbc0ee1a34671ad6cc1c6f785d3a3 | B -> Các hạch cổ sâu
  line  11196 | Easy        | id 43dfcdb834d04f22a1587b098ff69144 | B -> Các hạch cổ sâu

### Group 691 — topic: Dermatology, Anatomy
Q: Chức năng của da là:
Options (shared set): ['Bảo vệ cơ thể', 'Bài tiết mồ hôi và điều hòa thân nhiệt', 'Cơ quan xúc giác', 'Tât cả đều đúng']
  line   4489 | Easy        | id a0e6560bf10846e0a81ea7bae7cdcb81 | D -> Tât cả đều đúng
  line  11197 | Easy        | id ed89246ed3ec45698bdacc691648c18f | D -> Tât cả đều đúng

### Group 692 — topic: Cardiology, Anatomy
Q: Mô tả nào đúng về đặc điểm của van hai lá
Options (shared set): ['Van hai lá chỉ cho máu chảy từ nhĩ trái xuống thất phải', 'Van hai lá ngăn giữa buồng nhĩ trái và nhĩ phải', 'Van hai lá cho dòng chảy từ nhĩ trái xuống thất phải', 'Van hai lá chỉ cho dòng máu chảy từ thất trái lên nhĩ trái']
  line   4490 | Medium      | id 8387a3b380704f0c9594658433165afc | A -> Van hai lá chỉ cho máu chảy từ nhĩ trái xuống thất phải
  line  11198 | Medium      | id c734369463eb4aaf9e65946c1e2a6c89 | A -> Van hai lá chỉ cho máu chảy từ nhĩ trái xuống thất phải

### Group 693 — topic: Urology, Obstetrics and Gynecology, Anatomy
Q: Bàng quang nữ không liên quan đến cơ quan nào?
Options (shared set): ['Tử cung', 'Xương mu', 'Trực tràng', 'Phúc mạc']
  line   4491 | Easy        | id 765ff95febe944e28187516c0ffe031f | C -> Trực tràng
  line  11199 | Easy        | id 86ce24f3435e4d4798fec15c619aa103 | C -> Trực tràng

### Group 694 — topic: Anatomy
Q: Vi nhung mao là:
Options (shared set): ['Tơ trương lực', 'Nhánh bào tương mặt ngọn tb hấp thu', 'Vi sợi', 'Ống siêu vi']
  line   4492 | Easy        | id e2d2a553167a4a05accade26d8795361 | B -> Nhánh bào tương mặt ngọn tb hấp thu
  line  11200 | Easy        | id 21a6c51b63544171a66a4752c8f03e10 | B -> Nhánh bào tương mặt ngọn tb hấp thu

### Group 695 — topic: Anatomy, Gastroenterology
Q: Tuyến nước bọt dưới lưỡi?
Options (shared set): ['Ống Wirsung', 'Ống Wharton', 'Ống Hering']
  line   4493 | Easy        | id b7c2b3ec207e42bf814a25bcf02e5da9 | B -> Ống Wharton
  line  11201 | Easy        | id 1552d8eee2b14f398d0a17fe08a25a9e | B -> Ống Wharton

### Group 696 — topic: Gastroenterology, Anatomy
Q: Tiểu thùy gan cổ điển có thành phần cấu tạo nào dưới đây?
Options (shared set): ['Khoảng cửa', 'Tĩnh mạch cửa', 'Ống mật', 'Mao mạch nan hoa']
  line   4494 | Easy        | id b2601400dc6b4bafb5df46cd6cc68ff2 | D -> Mao mạch nan hoa
  line  11202 | Easy        | id ffe399df271e4c05833dd8d87e5ea317 | D -> Mao mạch nan hoa

### Group 697 — topic: Anatomy
Q: Các cơ nào sau đây KHÔNG thuộc nhóm cơ vùng mông?
Options (shared set): ['Cơ mông lớn, cơ mông nhỡ', 'Cơ mông bé, cơ hình lê', 'Cơ bịt trong, cơ sinh đôi trên', 'Cơ bịt ngoài, cơ lược']
  line   4495 | Easy        | id 71ba78ce0b6041d09e7ac01f4de291cb | D -> Cơ bịt ngoài, cơ lược
  line  11203 | Easy        | id 374e4f16376144a3af34df1948bde8a5 | D -> Cơ bịt ngoài, cơ lược

### Group 698 — topic: Anatomy, General Medicine
Q: Cách xác định các cột sống:
Options (shared set): ['Xác định C6, D12 và khe liên đốt L4-L5', 'Xác định C7, D11 và khe liên đốt L3-L4', 'Xác định C7, D12 và khe liên đốt L3-L4', 'Xác định C7, D12 và khe liên đốt L4-L5']
  line   4496 | Medium      | id 7ea61acbe6a646d9ae704a0dd0f888af | D -> Xác định C7, D12 và khe liên đốt L4-L5
  line  11204 | Medium      | id 2a26ea02721446d5b42aaaeac031b34a | D -> Xác định C7, D12 và khe liên đốt L4-L5

### Group 699 — topic: Gastroenterology, Anatomy
Q: Hành tá tràng là phần nối tiếp với dạ dày qua lỗ tâm vị
Options (shared set): ['A. Đúng', 'B. Sai', 'C.', 'D.']
  line   4497 | Easy        | id 9dcb8a0294c741129690b05db893266a | B -> B. Sai
  line  11205 | Easy        | id e698c1c6174946aaacdb7a4c47abe926 | B -> B. Sai

### Group 700 — topic: Anatomy, Pulmonology
Q: Trung thất trên
Options (shared set): ['Nằm phía dưới mặt phẳng đi ngang qua ngay phía trên màng ngoài tim', 'Phía sau ngang mức góc ức', 'Phía trước ngang mức khe đốt sống ngực IV và V', 'Chứa tuyến ức, khí quản,các mạch máu lớn của tim, các dây tk lang thang và Tk hoành']
  line   4498 | Easy        | id 322379a48aa04ee98f898c431a0518a2 | D -> Chứa tuyến ức, khí quản,các mạch máu lớn của tim, các dây tk lang thang và Tk hoành
  line  11206 | Easy        | id bffd346569c645e5853fc5d7c82521ea | D -> Chứa tuyến ức, khí quản,các mạch máu lớn của tim, các dây tk lang thang và Tk hoành

### Group 701 — topic: Neurology, Anatomy
Q: Bệnh nhân nam 49 tuổi, tiền sử đột quỵ nhồi máu não vùng bao trong bên trái di chứng liệt mặt, vào viện khám thấy: liệt ¼ dưới của mặt bên phải: khi nhe răng miệng lệch về bên trái, mất động tác thổi lửa bên phải, dấu hiệu Charles - Bell bên phải âm tính. Cơ nào sau đây là cơ bám da của nửa dưới mặt?
Options (shared set): ['Cơ cười, cơ cắn, cơ nâng góc miệng', 'Cơ cười, cơ cắn, cơ hạ góc miệng', 'Cơ nâng góc miệng, cơ hạ góc miệng, cơ cười', 'Cơ nâng góc miệng, cơ hạ góc miệng, cơ cắn']
  line   4499 | Challenging | id d4f91a03e99748e3ac0be466e430e923 | C -> Cơ nâng góc miệng, cơ hạ góc miệng, cơ cười
  line  11207 | Challenging | id 052c9e3baf6946edb7da4de137b12568 | C -> Cơ nâng góc miệng, cơ hạ góc miệng, cơ cười

### Group 702 — topic: Nephrology, Anatomy
Q: Động mạch thận phải dài hơn động mạch thận trái là do gan đè thận phải xuống?
Options (shared set): ['Đúng', 'Sai', 'Không có', 'Không có']
  line   4500 | Medium      | id d7938a37598944898f8ce53e522f12e9 | A -> Đúng
  line  11208 | Medium      | id a901ab95df7a475ea1f7f1ed9180ab23 | A -> Đúng

### Group 703 — topic: Hematology, Anatomy
Q: Nơi đổ về của ống ngực?
Options (shared set): ['Tĩnh mạch cảnh trong phải', 'Tĩnh mạch chủ trên', 'Hội lưu Pirogoff ở nền cổ', 'Tĩnh mạch cánh tay đầu']
  line   4501 | Easy        | id b74fd928ebe84ecf91fb0fb7987fabd3 | B -> Tĩnh mạch chủ trên
  line  11209 | Easy        | id a4bcbeb4b3b241f4b21935fede43cb90 | B -> Tĩnh mạch chủ trên

### Group 704 — topic: Pulmonology, Anatomy
Q: Thành phần cấu tạo nào sau đây để phân biệt giữa tiểu phế quản và phế quản?
Options (shared set): ['Sụn trong', 'Cơ Reisessen', 'Lớp đệm', 'Tế bào trụ có lông chuyển']
  line   4502 | Medium      | id bef27959c17d4a859c8db89c38405317 | B -> Cơ Reisessen
  line  11210 | Medium      | id 70cfcb16121846f08b513345100ba37c | B -> Cơ Reisessen

### Group 705 — topic: Anatomy
Q: Đường ngang qua hai mào chậu tương ứng với đốt sống thắt lưng:
Options (shared set): ['Đốt sống thắt lưng L1', 'Đốt sống thắt lưng L2', 'Đốt sống thắt lưng L3', 'Đốt sống thắt lưng L4']
  line   4503 | Easy        | id e4b36df7f73f492da6acda9c8e26f090 | D -> Đốt sống thắt lưng L4
  line  11211 | Easy        | id 3c454c37b4c14169a1db6a8028318ca4 | D -> Đốt sống thắt lưng L4

### Group 706 — topic: Otolaryngology, Anatomy
Q: Vòng bạch huyết quanh hầu Waldeyer không bao gồm:
Options (shared set): ['VA, Amidan khẩu cái', 'Amidan hầu', 'Amidan lưỡi', 'Họng hạt']
  line   4504 | Easy        | id f6accef83a524cc9a9fea19a83e8ac17 | D -> Họng hạt
  line  11212 | Easy        | id 244deb543128426b8c6d6ec6167b87da | D -> Họng hạt

### Group 707 — topic: Surgery, Anatomy
Q: Vùng bẹn được định nghĩa là vùng thấp nhất của ổ bụng?
Options (shared set): ['Đúng', 'Sai']
  line   4505 | Easy        | id e2659203f0a64a149a46c9ce82ad252f | B -> Sai
  line  11213 | Easy        | id 0f0b26d9fa5c4e2885da46c18100a129 | B -> Sai

### Group 708 — topic: Anatomy
Q: Cơ quan nào liên quan đến Bàng Quang?
Options (shared set): ['Tá tràng', 'Tử cung', 'Ống trực tràng', 'Không có thông tin']
  line   4506 | Easy        | id 3efbefc7ab4f426abb1b3d3b1f3dc993 | B -> Tử cung
  line  11214 | Easy        | id 3188ebdab54c4303894bad4d39194b94 | B -> Tử cung

### Group 709 — topic: Obstetrics and Gynecology, Anatomy
Q: Kích thước thành sau tiểu khung?
Options (shared set): ['4 cm', '10 cm', '4-10 cm', '12-15 cm']
  line   4507 | Easy        | id da78e5dbed7a46b2a3ea0ac722d9e0d0 | C -> 4-10 cm
  line  11215 | Easy        | id 3c74271c41364333a8307372af2ea93f | C -> 4-10 cm

### Group 710 — topic: Anatomy
Q: Cơ nào sau đây thuộc nhóm cơ ngoại lai thanh quản?
Options (shared set): ['Cơ liên phiễu', 'Cơ nhẫn giáp', 'Cơ nhẫn phễu bên', 'Cơ ức giáp và giáp móng']
  line   4508 | Easy        | id b21511deb02e432689b76674234c2b3c | D -> Cơ ức giáp và giáp móng
  line  11216 | Easy        | id 82e4d271c0624738812a3641f5a2da3f | D -> Cơ ức giáp và giáp móng

### Group 711 — topic: Anatomy
Q: Đi qua tứ giác Velpeau có...
Options (shared set): ['Động mạch vai dưới và thần kinh vai dưới.', 'Động mạch mũ và thần kinh mũ.', 'Động mạch cùng vai ngực và thần kinh trên vai.', 'Động mạch ngực ngoài và thần kinh ngực dài.']
  line   4509 | Easy        | id ac244f4d994a4202930a0a7019aeabfa | A -> Động mạch vai dưới và thần kinh vai dưới.
  line  11217 | Easy        | id 8061c0efb82a4358aa2589dbca3fc465 | A -> Động mạch vai dưới và thần kinh vai dưới.

### Group 712 — topic: Infection Diseases, General Medicine
Q: Hãy chọn một ý đúng/ đúng nhất trong những câu trả lời sau: Trong quá trình rửa tay ngoại khoa, điều dưỡng phải để tay cao trên mức khuỷu tay. Điều dưỡng đang theo nguyên tắc nào?
Options (shared set): ['Các vật hay các vùng ở bên dưới eo cơ thể người là nhiễm khuẩn.', 'Các vật dụng hay các vùng vô khuẩn trở nên nhiễm khuẩn do tiếp xúc lâu với không khí.', 'Chỉ các vật dụng vô khuẩn mới có thể đặt vào các vùng vô khuẩn.', 'Một vật vô khuẩn sẽ trở nên bị nhiễm bẩn nếu bị chảy các dịch bẩn khác vào.']
  line   4510 | Medium      | id f97ef19168074e33b518a29d0250a7a0 | D -> Một vật vô khuẩn sẽ trở nên bị nhiễm bẩn nếu bị chảy các dịch bẩn khác vào.
  line  11218 | Medium      | id e4543e4165e14e08b63af7c0fb6bc466 | D -> Một vật vô khuẩn sẽ trở nên bị nhiễm bẩn nếu bị chảy các dịch bẩn khác vào.

### Group 713 — topic: Infection Diseases, General Medicine
Q: 80. Thời gian hấp ướt kim loại?
Options (shared set): ['Tối thiểu 15p', 'Tối thiểu 20p', 'Tối thiểu 10p', 'Tối thiểu 30p']
  line   4511 | Easy        | id bbda0b5c11a240ce8ed99fe941b7efba | B -> Tối thiểu 20p
  line  11219 | Easy        | id 30164b17e76840cab6628d243822e0a9 | B -> Tối thiểu 20p

### Group 714 — topic: Infection Diseases, General Medicine
Q: 82. Bước đầu của hấp ướt / khô?
Options (shared set): ['khử nhiễm', 'khử trùng', 'khử khuẩn']
  line   4512 | Easy        | id 7ec43039521c4b7391aad21a3932c4bb | A -> khử nhiễm
  line  11220 | Easy        | id 7695231f5d13479d9e27c434dd00e4cc | A -> khử nhiễm

### Group 715 — topic: Toxicology, Environmental Health
Q: Nồng độ chì tối đa cho phép có trong nước uống
Options (shared set): ['40 ppb', '20 ppb', '20 ppm', '40 ppm']
  line   4513 | Easy        | id f41ce79be5894f76a9f899c9ea85c28e | B -> 20 ppb
  line  11221 | Easy        | id dcadcf7cd69c4b908366b5d67314a386 | B -> 20 ppb

### Group 716 — topic: Toxicology, Environmental Health
Q: Mipxin là thuốc trừ sâu thuộc loại
Options (shared set): ['Thuốc trừ sâu hữu cơ nhóm pyrethroid', 'Thuốc trừ sâu hữu cơ có clor', 'Thuốc trừ sâu hữu cơ có dị vòng carbamat', 'Thuốc trừ sâu hữu cơ có phosphor']
  line   4514 | Easy        | id 2031b759ef1f457b8cc800737e97cf3a | D -> Thuốc trừ sâu hữu cơ có phosphor
  line  11222 | Easy        | id 0c72d1cc8c7b4da391b4127f36c8ee37 | D -> Thuốc trừ sâu hữu cơ có phosphor

### Group 717 — topic: Toxicology, Environmental Health
Q: Người ta dùng hydrophosphur (H3P) làm thuốc diệt chuột dưới dạng
Options (shared set): ['Bạc phosphor', 'Kẽm phosphor', 'Đồng phosphor', 'Sắt phospho']
  line   4515 | Easy        | id 87e436d7ed5d423b8258114a6806d563 | B -> Kẽm phosphor
  line  11223 | Medium      | id 26e8f48734784e94a3d879b63883069d | B -> Kẽm phosphor

### Group 718 — topic: Toxicology, Environmental Health
Q: Furadan là thuốc trừ sâu thuộc loại:
Options (shared set): ['Thuốc diệt côn trùng dị vòng carbamat']
  line   4516 | Easy        | id fd6d1063f1614cba9c18bfac8fe57d5e | A -> Thuốc diệt côn trùng dị vòng carbamat
  line  11224 | Easy        | id d15f0dae172248e6944c765ed5544482 | A -> Thuốc diệt côn trùng dị vòng carbamat

### Group 719 — topic: Toxicology, Environmental Health
Q: Tác động của Pyrethrum và các dẫn chất tổng hợp Pyrethrin tương tự như:
Options (shared set): ['HCH', 'DDT', 'DDD', 'Parathion']
  line   4517 | Easy        | id e51e1f2102dc41ea8b1d54a71b72bb80 | B -> DDT
  line  11225 | Medium      | id 55ddc77c2224494f9073c8709fffe6fe | B -> DDT

### Group 720 — topic: Toxicology, Environmental Health
Q: Thuốc trừ sâu hữu cơ dị vòng carbamat có đặc điểm, ngoại trừ:
Options (shared set): ['Được sử dụng để thay thế clor hữu cơ (vì tác dụng tích lũy nguy hiểm)', 'Tác động ức chế lên enzym cholinesterase', 'Tác động ức chế lên ATPase gây ức chế thần kinh', 'Được sử dụng để thay thế phosphor hữu cơ (vì độc tính quá cao)']
  line   4518 | Easy        | id 1d9770c239094c0092fb32052de88658 | C -> Tác động ức chế lên ATPase gây ức chế thần kinh
  line  11226 | Medium      | id 54e9f9aa875c466ebdf207aa13e5e196 | C -> Tác động ức chế lên ATPase gây ức chế thần kinh

### Group 721 — topic: Toxicology, Environmental Health
Q: Dioxin là tạp chất của
Options (shared set): ['2,4 D và 2,4,5 T', 'Picloram', 'Dimetyl acenic acid', 'D.O.C']
  line   4519 | Easy        | id 85bd9e00891748f5b41e837b33fc5c99 | A -> 2,4 D và 2,4,5 T
  line  11227 | Easy        | id 74b4e7c4877942638db70729fcdb1655 | A -> 2,4 D và 2,4,5 T

### Group 722 — topic: Toxicology, Environmental Health
Q: Hợp chất diethyl, dimethyl thủy ngân được sử dụng để:
Options (shared set): ['Thuốc trừ sâu, diệt nấm', 'Trị bệnh giang mai → Hg(CN)2', 'Thuốc sát trùng → Mercurochrom, Thimerosal', 'Tẩy giun hay nhuận tràng → Calomel (HgCl)']
  line   4520 | Medium      | id bf13d99c5e8e48ed9ca38e273f1c928f | A -> Thuốc trừ sâu, diệt nấm
  line  11228 | Medium      | id 66bae2a75a484790a5199c9bfd4e68f8 | A -> Thuốc trừ sâu, diệt nấm

### Group 723 — topic: Toxicology, Occupational Health, Environmental Health
Q: Nồng độ chì vô cơ cho phép trong không khí ở nơi làm việc là:
Options (shared set): ['\uf0a3 0,05 g/m3 không khí', '\uf0a3 0,05 mg/m3 không khí', '\uf0a3 0,5 g/m3 không khí', '\uf0a3 0,5 mg/m3 không khí']
  line   4521 | Easy        | id a45620fb31214365a028e77c6c4d76e3 | B ->  0,05 mg/m3 không khí
  line  11229 | Easy        | id b75e9b7e7c504cf7a1f1fd70b8bba976 | B ->  0,05 mg/m3 không khí

### Group 724 — topic: Toxicology, Environmental Health
Q: Ngộ độc Rotenone ở người thì:
Options (shared set): ['Hiếm gặp', 'Thường gặp', 'Không gặp', 'Phổ biến ở vùng cao']
  line   4522 | Easy        | id e3dc9b2448f4453f96dfef400a91d0f3 | A -> Hiếm gặp
  line  11230 | Easy        | id 2371352192f04ddf82833d61dd116ef8 | A -> Hiếm gặp

### Group 725 — topic: Toxicology, Environmental Health
Q: Hợp chất màu da cam là hỗn hợp của
Options (shared set): ['2,4D và Dioxin', '2,4D và 2,4,5T', '2,4D và Picloram → Trắng', '2,4,5T và Picloram']
  line   4523 | Easy        | id 450efff5d29b44d595641ac5286c4781 | B -> 2,4D và 2,4,5T
  line  11231 | Medium      | id ca694432df4a433d98911c4aa5458210 | B -> 2,4D và 2,4,5T

### Group 726 — topic: Toxicology, Environmental Health
Q: CO không có nguồn gốc
Options (shared set): ['Hoạt động của núi lửa, cháy nhà, cháy rừng, cháy hầm mỏ', 'Phản ứng quang hóa của tầng đối lưu', 'Sự đốt cháy không hoàn toàn các hợp chất hữu cơ', 'Quá trình hàn hồ quang điện, ma điện, chạm khắc']
  line   4524 | Easy        | id 3733a8162f2b42638e7406f654546397 | B -> Phản ứng quang hóa của tầng đối lưu
  line  11232 | Easy        | id 203e54c73c764f018adb31080a79c6a3 | B -> Phản ứng quang hóa của tầng đối lưu

### Group 727 — topic: Toxicology, Environmental Health
Q: Chọn phát biểu sai:
Options (shared set): ['Arsenate là muối của acid arsennic được dùng trong các thuốc bảo vệ thực vật', 'Arsen nguyên tố ở thể tinh khiết rất độc', 'Hydro arsenur là chất khí độc, mùi tỏi', 'Arsen trioxide là tinh thể không màu, không mùi, rất độc']
  line   4525 | Easy        | id a992d9347ff34f91a13663f82f500edc | D -> Arsen trioxide là tinh thể không màu, không mùi, rất độc
  line  11233 | Easy        | id 827b3c6bd99e4662b97a3af07d8da6db | D -> Arsen trioxide là tinh thể không màu, không mùi, rất độc

### Group 728 — topic: Toxicology, Environmental Health
Q: Nồng độ gây độc chì vô cơ trong không khí là:
Options (shared set): ['0,075 mg/m3 không khí', '700 mg/m3 không khí', '0,05 mg/m3 không khí', '40 mg/m3 không khí']
  line   4526 | Easy        | id 70ce463f73664c848047ff0606b4d6a5 | C -> 0,05 mg/m3 không khí
  line  11234 | Easy        | id ccda8c74173748fb83340030cf1e34e1 | C -> 0,05 mg/m3 không khí

### Group 729 — topic: Toxicology, Environmental Health
Q: Liều gây chết của thuốc trừ sâu dị vòng carbamat thường là:
Options (shared set): ['1 mg - 100 mg', '10 mg – 100 mg', 'Vài mg', '100 mg – 1g']
  line   4527 | Easy        | id da942156563441b79e967eac17cb05e1 | A -> 1 mg - 100 mg
  line  11235 | Easy        | id 4c28ef2dc6144df4b6d88892845619dc | A -> 1 mg - 100 mg

### Group 730 — topic: Toxicology, Environmental Health
Q: Nồng độ gây độc chì hữu cơ (chì tetraethyl) trong không khí là:
0,075mg/m3 không khí
Options (shared set): ['0,075mg/m3 không khí']
  line   4528 | Easy        | id 9fb01ed2d63c47b789c2edeb5d8b1901 | A -> 0,075mg/m3 không khí
  line  11236 | Easy        | id 06de5d4f68f549e4b916233c993d2e7c | A -> 0,075mg/m3 không khí

### Group 731 — topic: Toxicology, Environmental Health
Q: Dạng thủy ngân có thể tích lũy trong các loài hải sản gây ngộ độc là:
Methyl Hg
Options (shared set): ['Methyl Hg']
  line   4529 | Easy        | id 536373eb1834407d81c17d8fc4813f07 | A -> Methyl Hg
  line  11237 | Easy        | id a3eb81bf9c9f4785ac9ec3a03525986b | A -> Methyl Hg

### Group 732 — topic: Toxicology, Environmental Health
Q: 48.Khi tiếp xúc với chất độc có nghĩa là bị __ với chất độc đó:
Options (shared set): ['Nhiễm trực tiếp', 'Nhiễm gián tiếp', 'Phơi nhiễm', 'Miễn nhiễm']
  line   4530 | Easy        | id a5c271b1c13c48fb859275e8bc7241c4 | C -> Phơi nhiễm
  line  11238 | Easy        | id 357f2340339840f0991427623eedf8d1 | C -> Phơi nhiễm

### Group 733 — topic: Toxicology, Environmental Health
Q: Trong tự nhiên , Co không được tạo thành từ quá trình nào sau đây ?
Options (shared set): ['Hoạt động núi lửa', 'Phản ứng quang hoá', 'Cháy nổ hầm mỏ', 'Hàn hồ quang điện']
  line   4531 | Easy        | id aac1e3e4fed84a0cb4cb3ce37ee7e856 | B -> Phản ứng quang hoá
  line   4544 | Easy        | id eb33d70e519b4877ad96a406707fdd5b | D -> Hàn hồ quang điện
  line  11239 | Medium      | id 52cd9c1633264658941ef04317b3ea90 | B -> Phản ứng quang hoá
  line  11252 | Easy        | id 9c110b1dfb6343638e7cafca86a0a58a | D -> Hàn hồ quang điện

### Group 734 — topic: Toxicology, Environmental Health
Q: Carbon monoxide và Nitrogen oxide cùng hiện diện trong nguồn nào sau 
đây ?
Options (shared set): ['Khói thuốc lá', 'Khói thải xe cộ', 'Khói lò than', 'Khói lò sưởi']
  line   4532 | Easy        | id eb0d80c0193a493f91ea7bc95d400ad7 | B -> Khói thải xe cộ
  line   4545 | Easy        | id 34bcf70d41e74beb8c344434f281f5bc | B -> Khói thải xe cộ
  line  11240 | Easy        | id d45f8fbfa47642919c97220f14d2739e | B -> Khói thải xe cộ
  line  11253 | Easy        | id 8b66dd7b3f514652befd8cad5185d33e | B -> Khói thải xe cộ

### Group 735 — topic: Toxicology, Environmental Health
Q: 60.Nguồn gốc của nitrogen oxide :
Options (shared set): ['Được phóng thích từ phản ứng giữa acid nitric hay acid nitrous với các chất \nhữu cơ', 'Từ sự đốt cháy nitrocellulose và các sản phẩm khác', 'Hiện diện trong khói thải xe cộ', 'Tất cả đều đúng']
  line   4533 | Medium      | id 7152385def6e4bafa9a81cc9b2cbeabd | D -> Tất cả đều đúng
  line  11241 | Medium      | id fcac8a2d436e4cbc937fe17b1b29b33c | D -> Tất cả đều đúng

### Group 736 — topic: Toxicology, Environmental Health
Q: 67. Thiết bị nào sau đây có thể gây nhiễn độc khí CO?
Options (shared set): ['bếp nấu bằng ga', 'máy lạnh', 'tủ lạnh', 'máy giặt']
  line   4534 | Easy        | id 2f65eeff82024f7bb6e24e773ae7dbd3 | A -> bếp nấu bằng ga
  line  11242 | Easy        | id f2a734024b1648afafbb9380b9d9d4e0 | A -> bếp nấu bằng ga

### Group 737 — topic: Toxicology, Environmental Health
Q: 92.Nguồn gốc sinh ra khí CO:
Options (shared set): ['Nhiên liệu có chứa C', 'Sự chuyển hóa của metylcloride tại gan', 'Đốt cháy hợp chất hữu cơ', 'A và C']
  line   4535 | Easy        | id de6a6bda11824d6c9932fdd47cd98376 | D -> A và C
  line  11243 | Medium      | id 5dc9f8b3f301430ab6212ae6139e0c2f | D -> A và C

### Group 738 — topic: Toxicology, Environmental Health
Q: 103. Xác định CO trong không khí không gồm phương pháp nào sau đây?
Options (shared set): ['Phổ hấp thu của CO trong vùng tử ngoại (UV).', 'Định lượng nhanh.', 'Dựa vào phản ứng khử I2O5.', 'Phản ứng với KI.']
  line   4536 | Easy        | id cf21874a65ea40a09a4929648ff2a228 | D -> Phản ứng với KI.
  line  11244 | Easy        | id 4e56343bb8f747578915ead4dea645a1 | D -> Phản ứng với KI.

### Group 739 — topic: Toxicology, Environmental Health
Q: Trong xăng người ta thường pha gì?
Options (shared set): ['Chì Tetraethyl', 'Chì Acetat', 'Asenua gali', 'Thủy ngân']
  line   4537 | Easy        | id cb2d969b38714224af33b944af9aa256 | A -> Chì Tetraethyl
  line   4552 | Easy        | id d373a67d0fcc40dfb47eda52c2928625 | A -> Chì Tetraethyl
  line  11245 | Easy        | id 7c95d970b1cf44209b4340a57edf5aae | A -> Chì Tetraethyl
  line  11260 | Easy        | id 7ff13f3d9c2c435e830db4411bd63d16 | A -> Chì Tetraethyl

### Group 740 — topic: Toxicology, Environmental Health
Q: Asen nào làm thuốc trừ sâu?
Options (shared set): ['Asenat đồng crôm hóa', 'Asenat hidro chì', 'Asenua gali', 'Axetoasenit']
  line   4538 | Easy        | id afda36c2732540378e7216e6b294b40e | A -> Asenat đồng crôm hóa
  line   9624 | Medium      | id cefca2bbbd0840c483f25f9ced7d5ccd | B -> Asenat hidro chì
  line  11246 | Easy        | id 2b73ba4541ad43e089dc5f06ea3789d1 | A -> Asenat đồng crôm hóa

### Group 741 — topic: Toxicology, Pharmacology, Environmental Health
Q: H. Dư lượng thuốc bảo vệ thực vật là những chất xất hiện trong lương thực thực phẩm do sử dụng thuốc BVTV gây nên trong toàn quá trình sản xuất lương thực và thực phẩm, trong sản phẩm nông nghiệp và trong thức ăn vật nuôi.
141.
1. Nicotin là chất tác dụng ở 2 pha: kích thích ở liều thấp và ức chế ở liều cao.
2. Rotenone ảnh hưởng đến quá trình chuyển hóa do ức chế sự oxy hóa NADH → NAD đối với cơ chất như glutamic, ẞ-ketoglutarate, nên gây ảnh hưởng đến 1 số quá trình chuyển hóa.
Chọn câu trả lời đúng:
Options (shared set): ['1 đúng, 2 sai', '1 sai, 2 đúng', 'Cả 2 đều đúng', 'Cả 2 đều sai']
  line   4539 | Medium      | id 918dc150e5b34b6c8e6023db8317b99b | C -> Cả 2 đều đúng
  line  11247 | Medium      | id 539995f7991d409ba07ae81fb2cbb1f9 | C -> Cả 2 đều đúng

### Group 742 — topic: Toxicology, Environmental Health
Q: Dioxin là tạp chất của?
Options (shared set): ['2,4 D và 2,4,5 T.', 'Picloram.', '2,4D và Picloram.', 'Dimetylacenic.']
  line   4540 | Easy        | id 1c48458daf484c36829ea3877ef36b00 | A -> 2,4 D và 2,4,5 T.
  line   9594 | Easy        | id 2e40826488cc43b7ad78f1275ad46e49 | A -> 2,4 D và 2,4,5 T.
  line  11248 | Easy        | id 6c3d8ed1201947ba8feaf8864f78f7f1 | A -> 2,4 D và 2,4,5 T.

### Group 743 — topic: Toxicology, Environmental Health
Q: Dioxin là:
(3) Cảm ứng sinh tổng hợp porphyrin và chuyển hóa của Cyt P450
(4) Là tạp chất của 2,4D và 2,4,5T
Options (shared set): ['(1) Đúng, (2) Đúng', '(1) Sai, (2) Đúng', '(1) Đúng, (2) Sai', '(1) Sai, (2) Sai']
  line   4541 | Medium      | id 96e4fd62790945feb5232ad190c3029b | A -> (1) Đúng, (2) Đúng
  line  11249 | Medium      | id 956021c7f95a4fd1b953976862d187c5 | A -> (1) Đúng, (2) Đúng

### Group 744 — topic: Toxicology, Environmental Health, Public Health
Q: Nồng độ cho phép trong không khí của D.O.C là:
Options (shared set): ['0,01 mg/l.', '0,001mg/l.', '0,1mg/l.', '1mg/l.']
  line   4542 | Easy        | id 915759b1be7d41508ea5bec847f37b17 | B -> 0,001mg/l.
  line  10490 | Easy        | id 694ecb3a12194525bd259fc77c5e14a4 | B -> 0,001mg/l.
  line  11250 | Easy        | id 8b6064a4592447cca1695dcea491e2e0 | B -> 0,001mg/l.

### Group 745 — topic: Toxicology, Environmental Health
Q: 11. Chọn đáp án Sai:
A. Độc chất học là môn học nghiên cứu về tính chất lý hóa và tác động của chất độc trong các
cơ thể sông
B. Độc tính là một khái niệm liều lượng dùng để miêu tả tính chất gây độc của một chất đối
với cơ thể sống và được thể hiện bằng liều gây độc
C. Độc chất học góp phần xây dựng tiêu chuẩn dư lượng của thuốc ảo vệ thực vật
D. Chất độc là bất kỳ chất nào khi đi vào cơ thể trong những điều kiện nhất định gây ra
những biến đổi về mặc sinh lý.
Options (shared set): ['Độc chất học là môn học nghiên cứu về tính chất lý hóa và tác động của chất độc trong các\ncơ thể sông', 'Độc tính là một khái niệm liều lượng dùng để miêu tả tính chất gây độc của một chất đối\nvới cơ thể sống và được thể hiện bằng liều gây độc', 'Độc chất học góp phần xây dựng tiêu chuẩn dư lượng của thuốc ảo vệ thực vật', 'Chất độc là bất kỳ chất nào khi đi vào cơ thể trong những điều kiện nhất định gây ra\nnhững biến đổi về mặc sinh lý.']
  line   4543 | Easy        | id 0129d30a7e2449958c19d10f39b6221b | A -> Độc chất học là môn học nghiên cứu về tính chất lý hóa và tác động của chất độc trong các
cơ thể sông
  line  11251 | Medium      | id ba84413624fb4e53bb8f0e4ae63ea7ff | A -> Độc chất học là môn học nghiên cứu về tính chất lý hóa và tác động của chất độc trong các
cơ thể sông

### Group 746 — topic: Toxicology, Environmental Health
Q: Trong công nghiệp, CO hiện diện ở đâu ?
Options (shared set): ['Nhà máy lò kỹ nghệ', 'Khói thải từ xe cộ', 'A và B đều đúng', 'A sai và B đúng']
  line   4546 | Easy        | id 2e4b6520025a4202a14ca144f69f00f4 | C -> A và B đều đúng
  line   8938 | Easy        | id 9a80ef5cd2d043eab20767026dea6ad3 | A -> Nhà máy lò kỹ nghệ
  line  11254 | Easy        | id 100a9bdde8c64f3b921f96d21ffe622c | C -> A và B đều đúng

### Group 747 — topic: Toxicology, Environmental Health
Q: Nguồn gốc của nitrogen oxide :
Options (shared set): ['Được phóng thích từ phản ứng giữa acid nitric hay acid nitrous với các chất hữu cơ', 'Từ sự đốt cháy nitrocellulose và các sản phẩm khác', 'Hiện diện trong khói thải xe cộ', 'Tất cả đều đúng']
  line   4547 | Easy        | id 8f229ca601f64ceeab3db9189c5c44cb | D -> Tất cả đều đúng
  line  11255 | Medium      | id 40a2b37db86f41fba916b7f0036a6ffa | D -> Tất cả đều đúng

### Group 748 — topic: Toxicology, Environmental Health
Q: Trong tự nhiên nitrogen oxide được tạo thành :
Options (shared set): ['Quá trình oxy hóa các hợp chất có chứa nitơ như than, dầu diesel...', 'Trong khói thải xe cộ', 'Trong quá trình sản xuất sơn mài, thuốc nhuộm, những hóa chất khác', 'Trong khói quang hóa']
  line   4548 | Medium      | id 91a3a6d24bbc4257b26b68390319dced | A -> Quá trình oxy hóa các hợp chất có chứa nitơ như than, dầu diesel...
  line  11256 | Medium      | id 22eba1a8afba4a8aa6021a72160121e5 | A -> Quá trình oxy hóa các hợp chất có chứa nitơ như than, dầu diesel...

### Group 749 — topic: Toxicology, Environmental Health
Q: Thiết bị nào sau đây có thể gây nhiễn độc khí CO?
Options (shared set): ['bếp nấu bằng ga', 'máy lạnh', 'tủ lạnh', 'máy giặt']
  line   4549 | Easy        | id c8f5a7e26eb54bb8b0ecb8c8be2b4ff8 | A -> bếp nấu bằng ga
  line  11257 | Easy        | id d29259a53312412f96b6ed832f23cf3b | A -> bếp nấu bằng ga

### Group 750 — topic: Toxicology, Biochemistry, Environmental Health
Q: Nguồn gốc sinh ra khí CO:
Options (shared set): ['Nhiên liệu có chứa C', 'Sự chuyện hóa của metylcloride tại gan', 'Đốt cháy hợp chất hữu cơ', 'A và C']
  line   4550 | Easy        | id 51260d550fe944a595818d287127a1aa | D -> A và C
  line  11258 | Medium      | id c33a7d34d89b4d07b5381f076049a13c | D -> A và C

### Group 751 — topic: Toxicology, Public Health, Environmental Health
Q: Theo WHO giới hạn cho phép của arsen trong nước uống là:
Options (shared set): ['0.1mg/L', '0.01mg/L', '0.1g/L', '0.01g/L']
  line   4551 | Easy        | id 20a75e5832164cf1a779c3e73addd71c | B -> 0.01mg/L
  line  11259 | Easy        | id 1a427cd942074130940f35ff8f9fedc8 | B -> 0.01mg/L
  line  11786 | Easy        | id f287bca0840a45dcb31ca2bd4ecdaa8a | B -> 0.01mg/L

### Group 752 — topic: Toxicology, Chemistry, Public Health, Environmental Health
Q: Hợp chất nào sau đây dùng trong xăng dầu?
Options (shared set): ['H3AsO3', 'HgNO3', 'Pb(NO3)2', 'Pb(C2H5)4']
  line   4553 | Easy        | id a203454042ca4d80878a5531b0cca39f | D -> Pb(C2H5)4
  line  11261 | Easy        | id ee0e6ce3abab406c938ab0953973eeee | D -> Pb(C2H5)4

### Group 753 — topic: Toxicology, Public Health, Environmental Health
Q: Giới hạn của arsen trong nước uống là:
Options (shared set): ['0.01mg/L', '<0.01mg/L', '>0.01mg/L', '0.05mg/L']
  line   4554 | Easy        | id 0b2c426415084613a971f5ba91b95c2f | A -> 0.01mg/L
  line  11262 | Easy        | id 5ed503f44b114c698c176339ecdede74 | A -> 0.01mg/L

### Group 754 — topic: Toxicology, Environmental Health
Q: Liều độc LD50 của Dioxin đối với heo theo đường tĩnh mạch là:
Options (shared set): ['1 mg/kg', '10 mg/kg', '0, 001 mg/kg', '0,1 mg/kg']
  line   4555 | Easy        | id e31754a2295e404bac3ebd35a10496d7 | A -> 1 mg/kg
  line  11263 | Easy        | id 25090254dbd749a4a4503f4bb5a82c02 | A -> 1 mg/kg

### Group 755 — topic: Infectious Diseases, Environmental Health
Q: Trứng giun đũa ở ngoại cảnh có thể như thế nào?
Options (shared set): ['Sống tốt trong điều kiện thuận lợi', 'Chuyển từ thể hoạt động sang thể ngủ', 'Bị tiêu diệt bởi ánh nắng mặt trời và thời tiết khô hanh', 'Sống tốt với bất kì điều kiện ngoại cảnh nào']
  line   4556 | Easy        | id bb6b2a1feb404e4fb1f6b8d724eb11f5 | A -> Sống tốt trong điều kiện thuận lợi
  line  11264 | Medium      | id 6feed0d8db1444ddbceb2077424c5a14 | A -> Sống tốt trong điều kiện thuận lợi

### Group 756 — topic: Otolaryngology, Environmental Health
Q: Tiếp xúc thường xuyên với hơi độc và hoá chất sẽ dẫn đến viêm mũi xoang?
Options (shared set): ['Đúng', 'Sai']
  line   4557 | Easy        | id 9b74f94e28e24d3c96288a5fef92fdfd | A -> Đúng
  line  11265 | Easy        | id 3bf5fd871fcd4fcda0a05cd42d86cf30 | A -> Đúng

### Group 757 — topic: Pulmonology, Environmental Health
Q: Những biến chứng nào sau đây KHÔNG phải là biến chứng của bệnh bụi phổi:
Options (shared set): ['Khí phế thủng', 'Viêm phế quản cấp', 'Viêm màng phổi.', 'Tâm phế mạn.']
  line   4558 | Medium      | id 8058ef4b34504af3ae707228502fa60e | B -> Viêm phế quản cấp
  line  11266 | Medium      | id 8b524da5cb274801b1b6e0877580de5f | B -> Viêm phế quản cấp

### Group 758 — topic: Infectious Diseases, Environmental Health, Public Health
Q: Sự xuất hiện nhiều bệnh mới nổi là do:
Options (shared set): ['Có thay đổi về sự tương tác giữa người và động vật', 'Có thay đổi về sự tương tác giữa người và môi trường', 'Có thay đổi về sự tương tác giữa người, động vật và môi trường', 'Có những thay điều kiện tự nhiên và lạm dụng thuốc.']
  line   4559 | Easy        | id c9d9d17b1595415696aa1425b68240f7 | C -> Có thay đổi về sự tương tác giữa người, động vật và môi trường
  line  11267 | Medium      | id 5dbd0fc9593d48bd9980baeefeb8a210 | C -> Có thay đổi về sự tương tác giữa người, động vật và môi trường

### Group 759 — topic: Infectious Diseases, Environmental Health, Public Health
Q: Sự quay trở lại của nhiều loại bệnh là do:
Options (shared set): ['Thay đổi điều kiện sống và môi trường', 'Bệnh xuất hiện theo chu kỳ ng', 'Do tương tác giữa người, động vật và môi trường thay đổi.', 'Thay đổi điều kiện tự nhiên và lạm dụng thuốc.']
  line   4560 | Easy        | id 1584c31aa69c46448060086c376a9461 | C -> Do tương tác giữa người, động vật và môi trường thay đổi.
  line  11268 | Medium      | id 80bbd0be6efd445dac0480f186ec1a56 | C -> Do tương tác giữa người, động vật và môi trường thay đổi.

### Group 760 — topic: Public Health, Environmental Health
Q: Yếu tố nào tạo điều kiện cho những vấn đề về sức khỏe.
Options (shared set): ['Sự thay đổi về dân số', 'Sự thay đổi về kinh tế', 'Thay đổi hệ thống chăn nuôi gia súc', 'Biến động về môi trường']
  line   4561 | Easy        | id 6f2827506dd848f79d942e39474105c2 | D -> Biến động về môi trường
  line  11269 | Easy        | id cb6d3eb00c704e668188776e4e4c20fe | D -> Biến động về môi trường

### Group 761 — topic: Pharmaceutical, Public Health
Q: Căn cứ phân phối lợi nhuận sau thuế của công ty cổ phần dược phẩm theo quy định là:
Options (shared set): ['Luật thuế doanh nghiệp', 'Quy định trong điều lệ của công ty', 'Chế độ tài chính quy định hiện hành', 'Quyết định của tổng giám đốc']
  line   4562 | Easy        | id ebc9476fc75d423ba8d643b3c50bf9bf | B -> Quy định trong điều lệ của công ty
  line  11270 | Easy        | id 46aed22956164d04825b09bcdd557cf2 | B -> Quy định trong điều lệ của công ty

### Group 762 — topic: Pharmaceutical, Public Health
Q: Căn cứ phân phối lợi nhuận sau thuế của công ty TNHH dược theo quy định là:
Options (shared set): ['Luật thuế doanh nghiệp', 'Quy định trong điều lệ của công ty', 'Chế độ tài chính quy định hiện hành', 'Quy quyết định của tổng giám đốc']
  line   4563 | Medium      | id 1d53668f02004aa5ab251d6ea097055c | B -> Quy định trong điều lệ của công ty
  line  11271 | Medium      | id a2022bd971a444aab4abdba7f4c1a9de | B -> Quy định trong điều lệ của công ty

### Group 763 — topic: Pharmaceutical, Public Health
Q: Tỷ suất lợi nhuận vốn lưu động bình quân của doanh nghiệp dược T có lợi nhuận từ tiêu thụ sản phẩm = 12 tỷ đồng, tổng vốn lưu động bình quân = 70 tỷ đồng, nguyên giá tài sản cô định = 180 tỷ đồng, số khấu hao tài sản cố định = 50 tỷ đồng là:
Options (shared set): ['6%.', '17.14%', '4%', '3.60%']
  line   4564 | Challenging | id fc91b67c5e9b41c49685d1ddfba668ca | B -> 17.14%
  line  11272 | Challenging | id e243750532ef4a11a10a9ad85543d341 | B -> 17.14%

### Group 764 — topic: Gastroenterology, Pharmacology
Q: Phát biểu KHÔNG ĐÚNG về thuốc nhuận tràng tạo khối:
Options (shared set): ['Trị táo bón mạnh và hoàn toàn hơn loại nhuận tràng kích thích.', 'Sẽ gây táo bón nếu bệnh nhân uống ít nước hoặc không uống nước.', 'Là các chất polysaccharide thiên nhiên hoặc tổng hợp.', 'Hút nước tạo khối gel kích thích nhu động ruột.']
  line   4565 | Medium      | id 91d6dfba2ff84ee2a6c2145262d2b2e5 | A -> Trị táo bón mạnh và hoàn toàn hơn loại nhuận tràng kích thích.
  line  11273 | Medium      | id f910331f60894016a9d5d0012a34808e | A -> Trị táo bón mạnh và hoàn toàn hơn loại nhuận tràng kích thích.

### Group 765 — topic: Pulmonology, Infectious Diseases
Q: Người chưa từng nhiễm vi khuẩn lao, khi tiến hành test tuberculin:
Options (shared set): ['chắc chắn cho kết quả âm tính', 'có thể cho kết quả dương tính', 'có thể cho kết quả dương tính mạnh', 'cả 3 lựa chọn trên đều sai']
  line   4593 | Medium      | id 737883fa65c94b3696dd26c86c47c49c | B -> có thể cho kết quả dương tính
  line   6025 | Medium      | id 77c792fcedcf429da50df5743d62ccd0 | B -> có thể cho kết quả dương tính

### Group 766 — topic: Pulmonology, Infectious Diseases
Q: Người đã từng nhiễm vi khuẩn lao, khi tiến hành test tuberculin:
Options (shared set): ['chắc chắn cho kết quả dương tính', 'có thể cho kết quả âm tính', 'chắc chắn cho kết quả dương tính mạnh', 'cả 3 lựa chọn trên đều sai']
  line   4594 | Medium      | id f8bcd8a0d39e42f9b6ee2774806f0811 | B -> có thể cho kết quả âm tính
  line   6026 | Medium      | id 0dd7c1dc1383495c80085f79cf4a1f7e | B -> có thể cho kết quả âm tính

### Group 767 — topic: Pulmonology, Infectious Diseases
Q: Test tuberculin dương tính chứng tỏ bệnh nhân đã nhiễm vi khuẩn lao.
Options (shared set): ['đúng', 'sai']
  line   4596 | Medium      | id 4ab1737624114cb6a13147c46caee4c8 | B -> sai
  line   6028 | Medium      | id 4d1060b2dc8648cba9c85de2395d3b90 | B -> sai

### Group 768 — topic: Pulmonology, Radiology
Q: Bệnh nhân nữ tuổi trung niên, nhiệt độ 38,8 độ C, nhịp tim 105 nhịp mỗi phút, huyết áp 140/75 mmHg, độ bão hòa oxy 92%, ho có đờm mủ và chẩn đoán xác định là viêm phổi màng phổi. X quang phổi sau đây là thích hợp nhất cho việc đánh giá có thể ở bệnh nhân
Options (shared set): ['Phim chụp nghiêng', 'Phim thẳng và nghiêng', 'Phim thẳng', 'Phim chụp khi thở và thở ra']
  line   4614 | Challenging | id 84da185df5b0436abedd761b746e799c | B -> Phim thẳng và nghiêng
  line   9139 | Challenging | id cd2ef26890ab4b30b9efc7b0cb6c59cb | B -> Phim thẳng và nghiêng

### Group 769 — topic: Endocrinology, Oncology, Pulmonology
Q: Ung thư nào sau đây không liên quan đến nội tiết?
Options (shared set): ['Ung thư vú', 'Ung thư phổi', 'Ung thư tuyến tiền liệt', 'Ung thư nội mạc tử cung']
  line   4634 | Medium      | id 430f5111425f4952834367b6e0b206e4 | B -> Ung thư phổi
  line   6412 | Medium      | id ec45e5a7ae874e12a9318f0e2ead4caa | B -> Ung thư phổi

### Group 770 — topic: Infectious Diseases, Pulmonology
Q: Chọn một câu trả lời đúng. Đặc điểm nào sau đây không phải là đặc điểm của bệnh cúm?
Options (shared set): ['Dễ ngăn chặn vì bệnh lành tính.', 'Gây tác hại lớn cho sức khoẻ cộng đồng.', 'Số lượng người mắc nhiều.', 'Gây thành dịch lớn.']
  line   4646 | Easy        | id 9b141ea2aaef4087970ef2cf1823390f | A -> Dễ ngăn chặn vì bệnh lành tính.
  line  10051 | Medium      | id b4c0e60159424ea58a36eb2fa76e349d | A -> Dễ ngăn chặn vì bệnh lành tính.

### Group 771 — topic: Infectious Diseases, Pulmonology, Obstetrics and Gynecology
Q: Chọn một câu trả lời đúng. Đặc điểm biến chứng viêm phổi thủy đậu:
Options (shared set): ['Phụ nữ có thai hay diễn biến nặng.', 'Biến chứng này ít nguy hiểm với trẻ em.', 'Viêm phổi thường xuất hiện sau khi nốt phỏng khô.', 'Hiếm gặp người lớn, hiếm gặp trẻ em.']
  line   4651 | Medium      | id b72f7c5076f648b287cede2c9fdcf9a1 | A -> Phụ nữ có thai hay diễn biến nặng.
  line  10000 | Medium      | id 1a70a564b4df42ddaa20c76f69e7308a | A -> Phụ nữ có thai hay diễn biến nặng.

### Group 772 — topic: Pulmonology, Otolaryngology
Q: Hội chứng ngưng thở khi ngủ ( Trong 7 giờ ngủ đêm):
Options (shared set): ['Bệnh nhân ngưng thở dưới 30 lần, mỗi lần dưới 10 giây', 'Bệnh nhân ngưng thở hơn 30 lần, mỗi lần trên 10 giây', 'Bệnh nhân ngưng thở hơn 30 lần, mỗi lần dưới 10 giây', 'Bệnh nhân ngưng thở dưới 30 lần, mỗi lần trên 10 giây']
  line   4655 | Medium      | id a014a337dae74175b5eb5ca05371aca7 | B -> Bệnh nhân ngưng thở hơn 30 lần, mỗi lần trên 10 giây
  line   5770 | Medium      | id 307e1142ed4c463db9a56825ce23c9dd | B -> Bệnh nhân ngưng thở hơn 30 lần, mỗi lần trên 10 giây
  line   5776 | Medium      | id 50a50f78be894db6b6326561110fa658 | B -> Bệnh nhân ngưng thở hơn 30 lần, mỗi lần trên 10 giây
  line   5782 | Medium      | id e638f19543d94ce5becc46a97d0cfd67 | B -> Bệnh nhân ngưng thở hơn 30 lần, mỗi lần trên 10 giây

### Group 773 — topic: Otolaryngology, Infectious Diseases, Pulmonology
Q: Nguyên nhân gây viêm mũi mạn tính trọng cộng đồng chủ yếu là do virus đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line   4656 | Easy        | id 2f2c7f30322f4e85b79dc6092b1a9289 | B -> Sai
  line   5783 | Easy        | id 8eea286e014140ceb45edbfc89cc4204 | B -> Sai

### Group 774 — topic: Otolaryngology, Pulmonology
Q: Mở khí quản đôi khi làm nặng thêm bệnh chính đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line   4658 | Medium      | id cc8cd619856e4acb9f6953109cde97f5 | B -> Sai
  line   5771 | Medium      | id fb3ca5b10c824b08980575e61cebd517 | B -> Sai
  line   5777 | Medium      | id 86104049db5c4c6d8051f278f2018514 | B -> Sai
  line   5784 | Medium      | id 681d83ca7a2e4be18c0774c92674b349 | B -> Sai

### Group 775 — topic: Otolaryngology, Pulmonology
Q: Thanh quản có vai trò bảo vệ đường hô hấp thông qua phản xạ co thắt thanh quản và phạn xạ ho đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line   4662 | Medium      | id 290ce6bb891f4807927c83c7eba2f150 | B -> Sai
  line   5773 | Medium      | id 8222dfb38bc9467a9568db0add154fc5 | B -> Sai
  line   5780 | Medium      | id f695287e0d0f4ab8bb69a6df1e62c616 | B -> Sai
  line   5786 | Medium      | id 7898cb939a7d47a796e954232086e4b4 | B -> Sai
  line   9888 | Medium      | id f5f815fa86874bfdaab2f6443bd5df77 | B -> Sai
  line   9926 | Easy        | id a86f3bd92a2e40629d25b2b86be107b8 | B -> Sai

### Group 776 — topic: Oncology, Otolaryngology, Pulmonology
Q: Khó thở là triệu chứng không gặp trong ung thư vòm họng
Options (shared set): ['Đúng', 'Sai']
  line   4663 | Medium      | id 097e6d04516848bfbc27e521606e98e0 | A -> Đúng
  line   5775 | Medium      | id 6947b4431901413ea3b869125cf0489e | A -> Đúng
  line   5787 | Medium      | id f19e844ebb494e6e8a2e1bd8548abced | A -> Đúng

### Group 777 — topic: Pulmonology
Q: Phổi P có mấy rãnh liên thùy?
Options (shared set): ['2', '1', '3', '4']
  line   4683 | Easy        | id a23e936d906e4d0ca8ea08d5d5ebc4c3 | A -> 2
  line   4809 | Easy        | id ed501972223d44b0928ec9d40ffb350a | B -> 2

### Group 778 — topic: Pulmonology
Q: Dấu hiệu chữ S ngược có trong:
Options (shared set): ['Xẹp phổi', 'Viêm phổi', 'Tràn dịch khu trú khoang màng phổi', 'Dày dính khoang màng phổi']
  line   4684 | Medium      | id 68fc2da8d724430eb175328954070324 | A -> Xẹp phổi
  line   4814 | Medium      | id 76b6f0ab3391486ead8da8a39e74693c | A -> Xẹp phổi

### Group 779 — topic: Pulmonology, Radiology
Q: Hình mờ hình tam giác có đỉnh quay về rốn phổi, đáy quay ra vùng ngoại vi trên phim chụp XQ tim phổi thường có trong:
Options (shared set): ['Viêm phổi thùy', 'U phế quản phổi', 'U phổi', 'Tràn dịch khoang màng phổi']
  line   4685 | Medium      | id 5cc3dbcc217848afa17547b1cfcc8f6e | A -> Viêm phổi thùy
  line   4818 | Medium      | id fd1b633332294edabf4267186103d892 | C -> Viêm phổi thuỳ
  line   5575 | Medium      | id 076f8b8da8ab4599b2bcbb752f687b35 | A -> Viêm phổi thùy

### Group 780 — topic: Pulmonology, Radiology
Q: Hình mờ hình tam giác có đỉnh quay về rốn phổi, đáy quay ra vùng ngoại vi trên phim chụp XQ tim phổi thường có trong:
Options (shared set): ['Xẹp phổi', 'U phổi', 'Tràn dịch khu trú khoang màng phổi', 'Dầy dính khoang màng phổi']
  line   4686 | Medium      | id de30545c3a734ffb83ea155b3477213c | A -> Xẹp phổi
  line   5576 | Medium      | id c6c8091a7a1a403c8d806d55ca21e661 | A -> Xẹp phổi

### Group 781 — topic: Pulmonology
Q: Tràn dịch màng phổi dưới phổi là
Options (shared set): ['Tràn dịch màng phổi thể hoành', 'Tràn dịch màng phổi thể tự do', 'Tràn dịch màng phổi khu trú', 'Tràn dịch rãnh liên thùy']
  line   4690 | Medium      | id 30872cea328845c5bdcd7f63a6d3f618 | A -> Tràn dịch màng phổi thể hoành
  line   4804 | Medium      | id 827c08298f00484daaf80a8590356f0e | B -> Tràn dịch màng phổi thể hoành
  line   5580 | Medium      | id f7f744fc2f1d466885ec487400c8ccc0 | A -> Tràn dịch màng phổi thể hoành

### Group 782 — topic: Radiology, Pulmonology
Q: Chụp XQ tim phổi thẳng tư thế đứng,đúng kỹ thuật khi
Options (shared set): ['Ngực sát phim', 'Lưng sát phim', 'Thấy được đầu trước của 5 cung xương sườn', 'Chụp khi hít vào tối đa']
  line   4694 | Easy        | id 78ee6c3a08f1431fb46c52cd4e5aba95 | D -> Chụp khi hít vào tối đa
  line   4815 | Easy        | id e433a1105583435e81b75a5f6efe833d | D -> Chụp khi hít vào tối đa

### Group 783 — topic: Infectious Diseases, Pulmonology
Q: Thâm nhiễm mau bay do
Options (shared set): ['Ấu trùng giun đũa hoặc viêm phổi do virus', 'Vi khuẩn, ấu trùng sán', 'Giun đũa, giun kim', 'Virus,ấu trùng sán']
  line   4695 | Easy        | id 92b8fcd6153847529cebbefa79bf5bde | A -> Ấu trùng giun đũa hoặc viêm phổi do virus
  line   5583 | Medium      | id 2dd0ecf366e9457cb71112f44f17d047 | A -> Ấu trùng giun đũa hoặc viêm phổi do virus

### Group 784 — topic: Pulmonology
Q: Tràn dịch màng phổi được hiểu là:
Options (shared set): ['Có dịch trong khoang màng phổi', 'Có dịch ở giữa màng phổi và trung thất', 'Ứ dịch ở tổ chức kẽ dưới màng phổi', 'Có dịch giữa màng phổi và thành ngực']
  line   4696 | Easy        | id c3f014fb326d4de8a255b03e68401234 | A -> Có dịch trong khoang màng phổi
  line   4822 | Easy        | id 486109d2a2a640308204606441253b5c | C -> Có dịch trong khoang màng phổi
  line   5584 | Easy        | id 7c6cdb4d6ca34024b517177d17ab32bd | A -> Có dịch trong khoang màng phổi

### Group 785 — topic: Pulmonology, Radiology
Q: Tràn dịch khoang màng phổi tự do lượng ít, dấu hiệu X quang trên phim chụp phổi
Options (shared set): ['Tư thế thẳng, bệnh nhân đứng có hình tù góc sườn hoành', 'Tư thế thẳng, bệnh nhân nằm ngửa mờ dạng kính mờ giới hạn không rõ', 'Tư thế nghiêng, bệnh nhân đứng, thấy tù góc sườn hoành trước', 'Thấy rõ nhất ở phim chụp thì thở ra']
  line   4697 | Medium      | id 366ba418b0f341f98be362c7222199f5 | A -> Tư thế thẳng, bệnh nhân đứng có hình tù góc sườn hoành
  line   4826 | Medium      | id 6f4aac2383cc4cf1a4bf90254623b93b | D -> Tư thế thẳng, bệnh nhân đứng có hình tù góc sườn hoành

### Group 786 — topic: Pulmonology, Radiology
Q: Tràn dịch khoang màng phổi tự do trên phim chụp phổi thẳng có các dấu hiệu:
Options (shared set): ['Dịch luôn luôn tập trung ở vị trí thấp của khoang màng phổi theo tư thế chụp', 'Vùng tràn dịch có hình mờ không đồng nhất trên phim chụp', 'Không thấy rõ vòm hoành và bờ tim', 'Giới hạn trên là đường thẳng mờ, nằm ngang.']
  line   4699 | Medium      | id 260cbe7ea0fa4883ad67be193fe2276d | A -> Dịch luôn luôn tập trung ở vị trí thấp của khoang màng phổi theo tư thế chụp
  line   4801 | Medium      | id 6a96526a78cd492996f689787d05bdcf | C -> Dịch luôn luôn tập trung ở vị trí thấp của khoang màng phổi theo tư thế chụp
  line   5586 | Medium      | id 341b694e81a447bfb34b264c467cedd8 | A -> Dịch luôn luôn tập trung ở vị trí thấp của khoang màng phổi theo tư thế chụp

### Group 787 — topic: Pulmonology, Radiology
Q: Trên phim chụp tim phổi: tràn dịch khoang màng phổi
Options (shared set): ['Không phân biệt được bản chất dịch', 'Phát hiện tràn dịch màng phổi sớm hơn siêu âm', 'Không phát hiện được tràn dịch khu trú', 'Không thấy đường cong Damoiseau']
  line   4700 | Medium      | id abaa56fb7265483295c9d0ad8d8cb80a | A -> Không phân biệt được bản chất dịch
  line   4806 | Medium      | id 99796cebc83146458b6beef936ecaa2b | A -> Không phân biệt được bản chất dịch
  line   5587 | Medium      | id e1c632ee40c0470ea5c1ddfd98516474 | A -> Không phân biệt được bản chất dịch

### Group 788 — topic: Pulmonology, Radiology
Q: Phương pháp nào sau đây có giá trị nhất trong chẩn đoán giãn phế nang
Options (shared set): ['Chụp cắt lớp vi tính phổi với máy có độ phân giải cao', 'Chụp XQ tim phổi', 'Chụp MRI phổi với từ lực lớn', 'Siêu âm phổi- màng phổi']
  line   4702 | Medium      | id deaf0ff3da7040269a6b7b06a73ddea0 | A -> Chụp cắt lớp vi tính phổi với máy có độ phân giải cao
  line   4816 | Medium      | id 74f0defca00c46f7847c436c037afa05 | B -> Chụp cắt lớp vi tính phổi với máy có độ phân giải cao
  line   5589 | Medium      | id 2ce488f2fa7a43389b358a4074f35f0b | A -> Chụp cắt lớp vi tính phổi với máy có độ phân giải cao

### Group 789 — topic: Pulmonology
Q: Ý nào sau đây đúng nhất khi nói về hình ảnh viêm dày dính màng phổi
Options (shared set): ['Di chứng của tràn dịch màng phổi', 'Di chứng của tràn khí màng phổi', 'Không gây tù góc sườn hoành', 'Không gây co kéo các khu vực lân cận']
  line   4703 | Medium      | id 2f99012410d14a98ab906919aa3a6cb2 | A -> Di chứng của tràn dịch màng phổi
  line   4820 | Medium      | id 922a269a2783452da60d66f0b08e7e0c | D -> Di chứng của tràn dịch màng phổi
  line   5590 | Medium      | id d87c8a888b494739bf257f181442ce2c | A -> Di chứng của tràn dịch màng phổi

### Group 790 — topic: Pulmonology
Q: Tràn dịch khoang màng phổi được hiểu là:
Options (shared set): ['Có dịch trong khoang màng phổi', 'Có dịch ở giữa màng phổi và phổi', 'Ứ dịch ở tổ chức kẽ dưới màng phổi', 'Có dịch giữa màng phổi và thành ngực']
  line   4705 | Easy        | id 93cba8253b3645638690f4da12ba0aef | A -> Có dịch trong khoang màng phổi
  line   4827 | Easy        | id 761f34d0a93e4eba86e62e7171226cfa | A -> Có dịch trong khoang màng phổi
  line   5592 | Easy        | id 8598046da7464c92b35685df15b2d155 | A -> Có dịch trong khoang màng phổi

### Group 791 — topic: Pulmonology, Oncology
Q: Ý nào sau đây đúng khi nói về các ổ ung thư hoại tử khu trú trong nhu mô phổi
Options (shared set): ['Thường khu trú ở phần giữa hoặc dưới trường phổi', 'Thường khu trú ở đỉnh phổi', 'Thường có ở vùng ngọa vi của phổi', 'Thường khu trú ở dưới trường phổi']
  line   4706 | Medium      | id 37f713b1149e4e6290287c344a1b678f | A -> Thường khu trú ở phần giữa hoặc dưới trường phổi
  line   5593 | Medium      | id 427d5431bf9b45a8979aa988d1cd90aa | A -> Thường khu trú ở phần giữa hoặc dưới trường phổi

### Group 792 — topic: Pulmonology, Radiology
Q: Tràn dịch khoang màng phổi tự do lượng ít, dấu hiệu X quang trên phim chụp phổi
Options (shared set): ['Tư thế thẳng, bệnh nhân đứng có hình tù góc sườn hoành', 'Tư thế thẳng, bệnh nhân nằm ngửa mờ dạng kính mờ giới hạn không rõ', 'Tư thế nghiêng, bệnh nhân đứng, thấy sớm tù góc sườn hoành trước', 'Thấy rõ nhất ở phim chụp thì thở ra']
  line   4707 | Medium      | id 85845a35d9164103a5b0d01084dedb57 | A -> Tư thế thẳng, bệnh nhân đứng có hình tù góc sườn hoành
  line   4833 | Medium      | id d957e4c4593346fc98bd279afcb0bfc8 | C -> Tư thế thẳng, bệnh nhân đứng có hình tù góc sườn hoành

### Group 793 — topic: Pulmonology, Oncology
Q: Ý nào sau đây đúng khi nói về các ổ ung thư hoại tử trong nhu mô phổi
Options (shared set): ['Thường là 1 hốc đơn độc, thành dày,bờ trong nham nhở', 'Thường là 1 hốc đơn độc, thành mỏng cứng, bờ trong nham nhở', 'Thường nhiều hốc, thành dày cứng, bờ trong nham nhở', 'Thường nhiều hốc, thành mỏng cứng, bờ trong nham nhở']
  line   4708 | Medium      | id 23138dc517994d53940c7e5f90f89dc6 | A -> Thường là 1 hốc đơn độc, thành dày,bờ trong nham nhở
  line   4835 | Easy        | id aff5b24802ed4e43b2f750c6ad8459ed | D -> Thường là 1 hốc đơn độc, thành dày,bờ trong nham nhở
  line   5594 | Medium      | id 10c485c4316240d4af42649ed33255f8 | A -> Thường là 1 hốc đơn độc, thành dày,bờ trong nham nhở
  line  10095 | Medium      | id 053a5b93d2dc4059846fe55b755578e3 | A -> Thường là 1 hốc đơn độc, thành dày,bờ trong nham nhở

### Group 794 — topic: Pulmonology, Infectious Diseases, Radiology
Q: Lao sơ nhiễm có hình ảnh XQ điển hình là:
Options (shared set): ['Hình quả tạ(hình trùy)', 'Hình thả bong', 'Hình nốt mờ lan tỏa 2 phổi', 'Hình hang tập trung vùng đỉnh phổi']
  line   4709 | Medium      | id 4a109a4e54c54d65b673fe77ebe495ca | A -> Hình quả tạ(hình trùy)
  line   5595 | Medium      | id af69d4f58ce541cca256c0485182c743 | A -> Hình quả tạ(hình trùy)

### Group 795 — topic: Pulmonology, Radiology
Q: Hình ảnh tràn dịch khoang màng phổi,có thể thấy được khi siêu âm ổ bụng là
Options (shared set): ['Hình rỗng âm trên cơ hoành tăng âm', 'Hình tăng âm trên cơ hoành giảm âm', 'Hình rỗng âm trên bóng gan giảm âm', 'Hình rỗng âm ở trên cơ hoành chỉ thấy ở tư thế ngồi']
  line   4710 | Medium      | id 649fd0278b94462b90cb5ab39ab8e2bd | A -> Hình rỗng âm trên cơ hoành tăng âm
  line   4840 | Medium      | id b4949e2a688948a1aeace4cfe829fc49 | A -> Hình rỗng âm trên cơ hoành tăng âm
  line   5597 | Medium      | id 59216418284c408ab3ddf11d1d533e2a | A -> Hình rỗng âm trên cơ hoành tăng âm

### Group 796 — topic: Pulmonology, Infectious Diseases
Q: Ý nào sau đây đúng khi nói về thâm nhiễm mau bay trong bệnh Lao
Options (shared set): ['Phản ứng Tuberculin âm tính, do ký sinh trùng (giun đũa) , virus', 'Phản ứng Tuberculin dương tính, do kí sinh trùng (giun đũa)', 'Phản ứng Tuberculin dương tính, do virus', 'Phản ứng Tuberculin âm tính, do kí sinh trùng (giun đũa)']
  line   4711 | Medium      | id a0edc30a33a3475a8256debe386ee938 | A -> Phản ứng Tuberculin âm tính, do ký sinh trùng (giun đũa) , virus
  line   5598 | Medium      | id e11738d5119d45a1b2024c18e02822ed | A -> Phản ứng Tuberculin âm tính, do ký sinh trùng (giun đũa) , virus

### Group 797 — topic: Pulmonology, Radiology
Q: Các kỹ thuật phát hiện tràn dịch màng phổi tự do, theo độ nhạy giảm dần
Options (shared set): ['Siêu âm khoang màng phổi- phim phổi đứng , chụp nghiêng - phim phổi nằm nghiêng chụp thẳng, tia x chiếu ngang', 'Phim phổi đứng, chụp nghiêng – siêu âm khoang màng phổi - phim phổi đứng - chụp thẳng', 'Siêu âm khoang màng phổi - phim phổi nằm nghiêng chụp thẳng, tia Xchiếu ngang - phim phổi đứng - chụp nghiêng', 'Phim phổi đứng, chụp nghiêng - phim phổi nằm nghiêng chụp thẳng, tia X chiếu ngang - phim phổi đứng, chụp thẳng – siêu âm khoang màng phổi']
  line   4712 | Medium      | id fa71cdf70f0b47c7b6571ed8d240580e | C -> Siêu âm khoang màng phổi - phim phổi nằm nghiêng chụp thẳng, tia Xchiếu ngang - phim phổi đứng - chụp nghiêng
  line   4844 | Medium      | id 5a6e4b9d40114f608f404738c5e47f73 | C -> Siêu âm khoang màng phổi- phim phổi đứng - chụp nghiêng - phim phổi nằm nghiêng chụp thẳng, tia x chiếu ngang
  line   5599 | Medium      | id ac1c35aeb3794185a6e47ee058fbabb5 | A -> Siêu âm khoang màng phổi- phim phổi đứng , chụp nghiêng - phim phổi nằm nghiêng chụp thẳng, tia x chiếu ngang

### Group 798 — topic: Pulmonology, Infectious Diseases
Q: Hang lao và các tổ chức thâm nhiễm lao thường khu trú ở:
Options (shared set): ['Đỉnh phổi', 'Rốn phổi', 'Đáy phổi', 'Màng phổi']
  line   4714 | Medium      | id 66896700528e4605be513186af30aa9b | A -> Đỉnh phổi
  line   4848 | Medium      | id 0b2cb4d9f6fb4099b0f626929a29d77b | B -> Đỉnh phổi
  line   5601 | Medium      | id 1592f6de1ec544b2bc3d4f82ace18c92 | A -> Đỉnh phổi

### Group 799 — topic: Pulmonology, Radiology
Q: Dấu hiệu nào sau đây KHÔNG phù hợp với tràn dịch-tràn khí khoang màng phổi:
Options (shared set): ['Giới hạn giữa dịch và khí là hình đường cong Damoiseau', 'Phần thấp mờ, phần cao quá sáng', 'Giới hạn giữa dịch và khí là đường thẳng nằm ngang rõ nét trên phim chụp đứng', 'Nhu mô phổi bị xẹp và nằm quanh rốn']
  line   4715 | Medium      | id 3fbf471bdcf84ad08114f9d5634350ac | A -> Giới hạn giữa dịch và khí là hình đường cong Damoiseau
  line   5602 | Medium      | id 8937a82425fd43978e82124f1f2483ed | A -> Giới hạn giữa dịch và khí là hình đường cong Damoiseau

### Group 800 — topic: Pulmonology, Radiology
Q: Hình ảnh quá sáng ở phía cao, hình mờ ở phần thấp, giới hạn giữa 2 phần là một đường ngang gặp trong bệnh lý
Options (shared set): ['Tràn dịch – tràn khí phối hợp khoang màng phổi', 'Tràn dịch khoang màng phổi khư trú', 'Tràn khí khoang màng phổi khư trú', 'Abscess phổi']
  line   4716 | Medium      | id ea63bffe1c954ac3bb34ba5fc063d9c5 | A -> Tràn dịch – tràn khí phối hợp khoang màng phổi
  line   5603 | Medium      | id 560a873ba98b471587e96ac58a2c3e2b | A -> Tràn dịch – tràn khí phối hợp khoang màng phổi

### Group 801 — topic: Pulmonology, Radiology
Q: Ý nào sau đây đúng khi nói về các khe liên thùy và thùy phổi
Options (shared set): ['Phổi phải có 2 khe liên thùy chia thành 3 thùy', 'Phổi phải có 2 khe liên thùy', 'Phổi trái có 2 khe liên thùy chia thành 3 thùy', 'Phổi trái có 1 khe liên thùy']
  line   4717 | Easy        | id 4d70de459049442c9c842c507e252a03 | A -> Phổi phải có 2 khe liên thùy chia thành 3 thùy
  line   5604 | Easy        | id 500f95123f244d76825c9f2ea93521ee | A -> Phổi phải có 2 khe liên thùy chia thành 3 thùy

### Group 802 — topic: Radiology, Pulmonology
Q: Trên phim chụp tim phổi thẳng các hình mờ sau đây có thể NHẦM là tổn thương của phổi tiến triển, trừ một trường hợp
Options (shared set): ['Hình súng hai nòng (hình phế quản, đường ray )', 'Bóng mờ cơ ngực lớn', 'Bóng mờ của vú và núm vú', 'Bóng mờ cơ ức đòn chũm']
  line   4718 | Medium      | id ab822bc36198494283098458596033ee | A -> Hình súng hai nòng (hình phế quản, đường ray )
  line   5605 | Medium      | id fbe1ad19c6d44925ac192978a38a1077 | A -> Hình súng hai nòng (hình phế quản, đường ray )

### Group 803 — topic: Radiology, Pulmonology
Q: Khi chụp phổi bệnh nhân phải hít hơi vào sâu trước khi nín thở, có mục đích:
Options (shared set): ['Trường phổi dãn rộng', 'Tăng lượng oxy trong phế nang', 'Để nín thở lâu khi chụp phim', 'Để lồng ngực giãn rộng']
  line   4719 | Easy        | id 9bf859404bb249e1948d7c085ef015fb | A -> Trường phổi dãn rộng
  line   5606 | Easy        | id fe2fab69e8d74f91a7fd54f2a5911bff | A -> Trường phổi dãn rộng

### Group 804 — topic: Radiology, Pulmonology
Q: Phim chụp XQ tim phổi thẳng đứng đúng kỹ thuật
Options (shared set): ['Tách được 2 xương bả vai ra ngoài trường phổi', 'Hít vào sâu', 'Thấy được toàn bộ cột sống ngực', 'Đứng thẳng']
  line   4720 | Easy        | id 9f9097e6fb204cdeaadcd9ecb8128104 | A -> Tách được 2 xương bả vai ra ngoài trường phổi
  line   5607 | Easy        | id 63dc2124bf3f49528e5d2b860f52fe98 | A -> Tách được 2 xương bả vai ra ngoài trường phổi

### Group 805 — topic: Pulmonology, Radiology
Q: Câu trả lời nào sau đây là SAI:
Options (shared set): ['Hình ảnh các phế huyết quản là do các nhánh động tĩnh mạch phổi tạo nên', 'Bình thường các nhánh phế huyết quản chỉ thấy cho đến cách ngoại vi 15mm', 'Bình thường các phế quản có hình đường ray chia nhánh theo các động mạch phổi', 'Hình ảnh rốn phổi tạo nên là do động mạch phổi, tĩnh mạch phổi, phế quản gốc, mạch và hạch bạch huyết, dây thần kinh, tổ chức liên kết.']
  line   4721 | Medium      | id c964aa21e50e420aa735aaae2622ad38 | A -> Hình ảnh các phế huyết quản là do các nhánh động tĩnh mạch phổi tạo nên
  line   4803 | Medium      | id f7d3ada82a444fe5aa226e6aa48ff684 | A -> Hình ảnh các phế huyết quản là do các nhánh động tĩnh mạch phổi taọ nên
  line   5608 | Medium      | id 0fa6205ae8b441a282d4f59da3d1888b | A -> Hình ảnh các phế huyết quản là do các nhánh động tĩnh mạch phổi tạo nên

### Group 806 — topic: Oncology, Pulmonology
Q: Các loại U nào sau đây thường gặp ở trung thất sau
Options (shared set): ['U thần kinh', 'Bướu giáp', 'U màng phổi', 'U hạch bạch huyết']
  line   4722 | Medium      | id a0efd1846a3d409882fbbd6a4f192fa5 | A -> U thần kinh
  line   4808 | Medium      | id aeef461f333f44819cc1d2ae7b59acc0 | A -> U thần kinh
  line   5609 | Medium      | id 77b1f493fcd3431b9ad0b4e35d762156 | A -> U thần kinh

### Group 807 — topic: Pulmonology, Radiology
Q: Bóng mờ bất thường ở trung thất thông thường là do hạch bạch huyết lớn, có thể gặp:
Options (shared set): ['Mọi vùng của trung thất', 'Trung thất trước', 'Trung thất sau', 'Trung thất giữa']
  line   4723 | Medium      | id 22d76c38ee8447beba67c751abc0ceba | A -> Mọi vùng của trung thất
  line   4813 | Medium      | id 93aa0ae9694f4a038d86c2bc38572fd2 | B -> Mọi vùng của trung thất
  line   5610 | Medium      | id 18ba033b445e49989603c882876f063b | A -> Mọi vùng của trung thất

### Group 808 — topic: Pulmonology, Radiology
Q: Hình ảnh khí quản trên phim chụp tim phổi thẳng
Options (shared set): ['Khí quản là dải sáng ở giữa và trước cột sống', 'Khí quản là dải mờ giới hạn rõ ở giữa và trước cột sống', 'Khí quản là dải sáng ở giữa, ở phía sau cột sống', 'Khí quản là dải mờ, giới hạn rõ, ở phía sau cột sống']
  line   4724 | Easy        | id def73c4d75f0416ba393465df65db9b6 | A -> Khí quản là dải sáng ở giữa và trước cột sống
  line   4817 | Easy        | id 69a59d8f31ad46dcbde515003f8e5d23 | C -> Khí quản là dải sáng ở giữa và trước cột sống
  line   5611 | Easy        | id dc2412b2486346429182fc5d7ac1b1ef | A -> Khí quản là dải sáng ở giữa và trước cột sống

### Group 809 — topic: Pulmonology, Infectious Diseases, Radiology
Q: Ý nào sau đây đúng nhất khi miêu tả về hang lao.
Options (shared set): ['Thành của hang dày, bờ trong không đồng đều , nhu mô phổi lân cận bị thâm nhiễm', 'Thành của hang mỏng, bờ trong không đồng đều, nhu mô phổi lân cận bị thâm nhiễm', 'Thành của hang mỏng, bờ trong đồng đều, nhu mô phổi lân cận bị thâm nhiễm', 'Thành của hang dày, bờ trong đồng đều, nhu mô phổi lân cận bị thâm nhiễm']
  line   4725 | Medium      | id ef0e742d73d8420c83ef67dbaa713e12 | A -> Thành của hang dày, bờ trong không đồng đều , nhu mô phổi lân cận bị thâm nhiễm
  line   4824 | Easy        | id 86da98c905e94569b579294db0faf07d | A -> Thành của hang dày, bờ trong không đồng đều , nhu mô phổi lân cận bị thâm nhiễm
  line   5613 | Medium      | id 2a5d3dcc39fb4ab5bb1ae3417821a5c4 | A -> Thành của hang dày, bờ trong không đồng đều, nhu mô phổi lân cận bị thâm nhiễm

### Group 810 — topic: Pulmonology, Radiology
Q: Trong bệnh lý hệ hô hấp, siêu âm thường dùng để thăm khám
Options (shared set): ['Tràn dịch khoang màng phổi', 'Tràn khí khoang màng phổi', 'Kén khí phổi', 'Viêm phổi']
  line   4726 | Medium      | id b8bdd5779ffa480fa94b7319ab9f5a7c | A -> Tràn dịch khoang màng phổi
  line   4828 | Medium      | id 2afd83fbb5d04ea29a7ce31ae9387314 | A -> Tràn dịch khoang màng phổi
  line   5614 | Medium      | id efb8538fa3be436b9cd984e5dbb60901 | A -> Tràn dịch khoang màng phổi

### Group 811 — topic: Pulmonology, Radiology
Q: Siêu âm thường không thăm khám được nhu mô phổi, vì lý do
Options (shared set): ['Khí dẫn truyền sóng âm kém', 'Không có đầu dò tần số cao', 'Không cho kết quả tin cậy như chụp phim phổi', 'Các xương sườn là trở ngại chính']
  line   4727 | Medium      | id b64c32e9830f4e478f61be17e9e5e00c | A -> Khí dẫn truyền sóng âm kém
  line   4832 | Medium      | id f5acfdd7a0c94dddaaab119ad4203ffb | A -> Khí dẫn truyền sóng âm kém
  line   5615 | Medium      | id 486b852d9b8847c5b0040826d2d2ee2c | A -> Khí dẫn truyền sóng âm kém

### Group 812 — topic: Pulmonology, Radiology
Q: Các bệnh lý sau đây có thể được thăm khám bằng siêu âm, trừ trường hợp
Options (shared set): ['Kén khí lớn sát màng phổi', 'U cơ hoành', 'U tuyến ức ở trẻ em', 'Vỡ cơ hoành']
  line   4728 | Medium      | id ba015beb64244c35990e99c1d4dc5ecb | A -> Kén khí lớn sát màng phổi
  line   4834 | Medium      | id c9934971940a412594c2ecb32f658c28 | A -> Kén khí lớn sát màng phổi
  line   5616 | Medium      | id 2894e13f8659492f989323becbcb24a7 | A -> Kén khí lớn sát màng phổi

### Group 813 — topic: Pulmonology, Radiology
Q: Hình ảnh hay gặp trong tràn khí trung thất:
Options (shared set): ['Dải sáng dọc 2 bờ trung thất', 'Thấy cơ hoành liên tục', 'Tuyến ức nổi ở trẻ nhỏ', 'Trung thất sáng hơn bình thường']
  line   4729 | Medium      | id 62de984e433a4f3a9f2a2836e6d41745 | A -> Dải sáng dọc 2 bờ trung thất
  line   4836 | Medium      | id cc042744334244648772332d038e98e8 | A -> Dải sáng dọc 2 bờ trung thất
  line   5617 | Medium      | id 43990fe8c9cf4e8bb332258e2adf07ce | A -> Dải sáng dọc 2 bờ trung thất

### Group 814 — topic: Pulmonology, Radiology
Q: Bệnh lý nào sau đây KHÔNG gây hội chứng phế nang:
Options (shared set): ['Bệnh bụi phổi', 'Phù phổi cấp', 'Ung thư tiểu phế quản phế nang', 'Lao phổi']
  line   4730 | Medium      | id 441ac25919ad45c7892af5a5d84242f3 | A -> Bệnh bụi phổi
  line   4838 | Medium      | id af07cb4dfbaf41aea8cf157058adf744 | A -> Bệnh bụi phổi
  line   5618 | Medium      | id 9ef6383cafc54751b3ea51c671f54aae | A -> Bệnh bụi phổi

### Group 815 — topic: Pulmonology, Radiology
Q: Hình nhánh phế quản khí trong đám mờ phế nang do:
Options (shared set): ['Phế quản chứa khí bình thường trong đám mờ của các phế nang', 'Phế quản dãn', 'Tắc phế quản không hoàn toàn', 'Thành phế quản dày hơn bình thường']
  line   4731 | Medium      | id 87a4201771de4b2bb0bc5678fd897040 | A -> Phế quản chứa khí bình thường trong đám mờ của các phế nang
  line   4839 | Medium      | id 9aa518a385644cdeb96b0b9b2cc327a1 | A -> Phế quản chứa khí bình thường trong đám mờ của các phế nang
  line   5619 | Medium      | id 0d24ad189c6b4ccf98a981b4d1e2c72b | A -> Phế quản chứa khí bình thường trong đám mờ của các phế nang
  line  10020 | Medium      | id 2317fd6cc48b43beabb5055d62d4db02 | A -> Phế quản chứa khí bình thường trong đám mờ của các phế nang

### Group 816 — topic: Pulmonology, Radiology
Q: Dấu hiệu X quang của áp xe phổi:
Options (shared set): ['Hang thành mỏng,bờ trong đều, bờ ngoài không rõ nét', 'Hang áp xe thành mỏng, mặt trong và ngoài đều', 'Hang áp xe có thành mỏng, bờ trong đều, bờ ngoài không rõ nét, tổ chức phổi xung quanh tổn thương nhiều', 'Hang áp xe có thành trong và ngoài không đều, nhu mô phổi xung quanh ít bị tổn thương']
  line   4732 | Medium      | id 27c0b7d8eb694d40a5f557fd4832affa | A -> Hang thành mỏng,bờ trong đều, bờ ngoài không rõ nét
  line   4841 | Medium      | id 405667d7355c453c89062c9ac80153f1 | A -> Hang thành mỏng,bờ trong đều, bờ ngoài không rõ nét
  line   5620 | Medium      | id 65a530e2f23049c4b3b2139777649d48 | A -> Hang thành mỏng,bờ trong đều, bờ ngoài không rõ nét

### Group 817 — topic: Pulmonology, Radiology
Q: Hình ảnh quá sáng ở phổi có thể do:
Options (shared set): ['Giãn phế nang', 'Tăng áp lực động mạch phổi', 'Co thắt phế quản', 'Co thắt động mạch phổi']
  line   4733 | Medium      | id 43168c3d945a4e9595579adca00fef40 | A -> Giãn phế nang
  line   5621 | Medium      | id b25ad253edf64cf3923bff54e98be02e | A -> Giãn phế nang

### Group 818 — topic: Pulmonology, Radiology, Infectious Diseases
Q: Hình ảnh của viêm phổi thùy trên phim chụp X quang là:
Options (shared set): ['Đám mờ tập trung dạng thùy, phân thùy', 'Đám mờ phế nang, bờ rõ, có nhánh phế quản khí', 'Đám mờ cánh bướm bờ rõ nét', 'Đám mờ, bờ rõ']
  line   4734 | Medium      | id fbcbc92d4f6d4ecd915202198cde8627 | A -> Đám mờ tập trung dạng thùy, phân thùy
  line   4845 | Medium      | id e0409d3ff1a2407886a7cd4e78398b1a | A -> Đám mờ tập trung dạng thùy, phân thùy
  line   5622 | Medium      | id ecfa474ccfdb4f7eacc93e9c3fb14915 | A -> Đám mờ tập trung dạng thùy, phân thùy

### Group 819 — topic: Pulmonology, Radiology
Q: Dấu hiệu X quang nào sau đây KHÔNG phù hợp với áp xe phổi
Options (shared set): ['Thành dày, mặt trong không đều', 'Hình ảnh mức hơi dịch trong hang', 'Hình ảnh viêm phổi quanh hang', 'Thành hang mỏng, mặt trong đều']
  line   4736 | Medium      | id 05b642bb70f24ff3af8a1b96f10c992e | A -> Thành dày, mặt trong không đều
  line   4849 | Medium      | id 1a062ddbc7574533a7145c24c21a9aa3 | D -> Thành hang mỏng, mặt trong đều
  line   5624 | Medium      | id ade0decacd9041cab9d74a0bc7445bfe | A -> Thành dày, mặt trong không đều

### Group 820 — topic: Pulmonology, Radiology, Infectious Diseases
Q: Ý nào sau đây đúng nhất khi nói về viêm phổi thùy
Options (shared set): ['Hình mờ hình tam giác có bờ lồi đỉnh quay về rốn phổi, đáy quay ra vùng ngoại vi', 'Hình mờ hình tam giác có bờ lõm đỉnh quay về rốn phổi, đáy quay ra vùng ngoại vi', 'Hình mờ hình tam giác đỉnh quay về rốn phổi, đáy quay ra vùng ngoại vi', 'Hình mờ hình tam giác đáy quay về rốn phổi, đỉnh quay ra vùng ngoại vi']
  line   4737 | Medium      | id 18a31dc3891240449c280ede43175e56 | A -> Hình mờ hình tam giác có bờ lồi đỉnh quay về rốn phổi, đáy quay ra vùng ngoại vi
  line   4850 | Medium      | id 5a87bf00f84c41888524453fd5eea784 | A -> Hình mờ hình tam giác có bờ lồi đỉnh quay về rốn phổi, đáy quay ra vùng ngoại vi
  line   5625 | Medium      | id cfa6a2f828b64f78bd7f8f587bfff5c9 | A -> Hình mờ hình tam giác có bờ lồi đỉnh quay về rốn phổi, đáy quay ra vùng ngoại vi

### Group 821 — topic: Pulmonology, Infectious Diseases
Q: Ý nào sau đây đúng nhất khi nói về viêm phổi thùy ở người lớn?
Options (shared set): ['Hay xảy ra ở thùy dưới bên phải', 'Hay xảy ra thùy dưới bên trái', 'Hay xảy ra thùy giữa bên phải', 'Hay xảy ra thùy trên bên trái']
  line   4738 | Medium      | id c6b425c1c26a4de3b1965f860066f110 | A -> Hay xảy ra ở thùy dưới bên phải
  line   4852 | Medium      | id 5fd45f9a277443da98d12144825b18d2 | A -> Hay xảy ra ở thùy dưới bên phải
  line   5626 | Medium      | id b850cca52933492ebb47ec640da06363 | A -> Hay xảy ra ở thùy dưới bên phải

### Group 822 — topic: Pulmonology, Oncology
Q: Dạng tổn thương ung thư di căn phổi cho hình ảnh trên phim phổi?
Options (shared set): ['Hình thả bóng', 'Nốt mờ đồng đều', 'Nốt mờ to nhỏ không đều', 'Nốt mờ và mờ dạng lưới']
  line   4739 | Medium      | id d57655332cac4281bb762e2546f003e6 | A -> Hình thả bóng
  line   4853 | Medium      | id 0f7184449ec7406996a5c9883a59a9d2 | A -> Hình thả bóng
  line   5627 | Medium      | id db1dc6f78b6646ce9b14102f7f252806 | A -> Hình thả bóng

### Group 823 — topic: Pulmonology, Infectious Diseases
Q: Lao xơ có đặc điểm tổn thương trên phim chụp?
Options (shared set): ['Là các dải mờ không có hướng ở vùng tổn thương lao', 'Dải xơ phát triển mạnh phối hợp thêm các ổ lao và hang lao (khả năng cao)', 'Tập trung ở phần dưới của trường phổi', 'Có hình ảnh quá sáng ở phần phổi lành do thở bù và không gây các cấu trúc lân cận']
  line   4740 | Medium      | id d496e27ec83c49afa77dd63dbca0d7aa | A -> Là các dải mờ không có hướng ở vùng tổn thương lao
  line   4854 | Medium      | id e687ccc47cdd423e8d3a65c582fe7640 | A -> Là các dải mờ không có hướng ở vùng tổn thương lao

### Group 824 — topic: Pulmonology, Oncology
Q: Ung thư phổi nguyên phát thường có:
Options (shared set): ['1 khối', '2 khối', '3 khối', '2 khối ở 2 phổi']
  line   4741 | Easy        | id 22c5a59799b843ac9fa130792c828044 | A -> 1 khối
  line   4855 | Easy        | id 3fa1fd85fe3940e18478b2ff55dc24b9 | A -> 1 khối
  line   5628 | Easy        | id 1bd86a98800347518db4c0f3c021c0f9 | A -> 1 khối

### Group 825 — topic: Pulmonology, Oncology
Q: Ung thư phổi chủ yếu là:
Options (shared set): ['Ung thư phế quản', 'Ung thư hạch rốn phổi', 'Ung thư màng phổi', 'Ung thư từ trung thất phát triển vào phổi']
  line   4742 | Easy        | id 14415977173545e5a5be10ebb69753b3 | A -> Ung thư phế quản
  line   4856 | Easy        | id 42db0af8c07c4890906a97caae12f58e | A -> Ung thư phế quản
  line   5629 | Easy        | id 0871dc4b167e4dc98efa6821b22fe0bf | A -> Ung thư phế quản

### Group 826 — topic: Pulmonology, Infectious Diseases, Radiology
Q: Ý nào sau đây đúng khi nói về hình ảnh lao kê trên phim chụp XQ tim phổi?
Options (shared set): ['Hình mờ nhỏ như hạt kê ở hầu hết 2 trường phổi', 'Hình mờ như những hạt kê 2 trường phổi, tập trung ở phía dưới trường phổi 2 bên', 'Là những nốt mờ to, nhỏ khác nhau khu trú vùng đỉnh hay giữa đòn', 'Là những nốt mờ to, nhỏ khác nhau tập trung ở phía dưới trường phổi']
  line   4743 | Medium      | id f167ee625e3244c5b9b95c42b3a92b77 | A -> Hình mờ nhỏ như hạt kê ở hầu hết 2 trường phổi
  line   4857 | Medium      | id 2b341a39ea994923845987254be317fc | A -> Hình mờ nhỏ như hạt kê ở hầu hết 2 trường phổi
  line   5630 | Medium      | id 12818ad9d611464f9c8d4e44ca049299 | A -> Hình mờ nhỏ như hạt kê ở hầu hết 2 trường phổi

### Group 827 — topic: Pulmonology, Infectious Diseases, Radiology
Q: Ý nào sau đây đúng khi nói về hình ảnh lao xơ hang trên phim chụp XQ tim phổi:
Options (shared set): ['Là tổn thương do vi khuẩn Lao mà một phần phổi đã khư trú và tạo thành hình hang', 'Do lao xơ tiến triển thành, các tổn thương lao biến thành hang lao do quá trình khu trú tổn thương của cơ thể', 'Do lao nốt tiến triển thành, các tổn thương lao biến thành hang lao do quá trình bã đậu hóa', 'Do lao xơ tiến triển thành']
  line   4744 | Medium      | id 6945f8d1e54249ba97c9a6815c2431bb | C -> Do lao nốt tiến triển thành, các tổn thương lao biến thành hang lao do quá trình bã đậu hóa
  line   4858 | Medium      | id 3eca8b10d2344f1a8bf930a2c1ad363a | A -> Là tổn thương do vi khuẩn Lao mà một phần phổi đã khư trú và tạo thành hình hang
  line   5631 | Medium      | id 6b8e03aba79a45499b8784a646c3015e | C -> Do lao nốt tiến triển thành, các tổn thương lao biến thành hang lao do quá trình bã đậu hóa

### Group 828 — topic: Infectious Diseases, Pulmonology
Q: Liều lượng Streptomycin điều trị lao ở người lớn?
Options (shared set): ['5 mg/kg/ngày', '10 mg/kg/ngày', '15 mg/kg/ngày', '20 mg/kg/ngày']
  line   4755 | Medium      | id 1eb58b71d5844638997087dda50b27e8 | C -> 15 mg/kg/ngày
  line   8337 | Medium      | id 49084ff4ee6340efaad047a3e952c396 | C -> 15 mg/kg/ngày

### Group 829 — topic: Pulmonology, Endocrinology, Ophthalmology
Q: Tác dụng không mong muốn của Corticoid đường khí dung?
Options (shared set): ['Ức chế thượng thận', 'Nấm Candia ở miệng', 'Loãng xương, tăng nhãn áp', 'Cả 3']
  line   4762 | Medium      | id 843e7c09183b4565813a94435e0500ff | D -> Cả 3
  line   6457 | Medium      | id 2eb647f2778f425c906cd990725c1457 | D -> Cả 3

### Group 830 — topic: Pulmonology, Endocrinology
Q: Một bệnh nhân với PCO2 động mạch 30 mm Hg, xem xét nào sau đây trong chẩn đoán phân biệt
Options (shared set): ['Tắc nghẽn cấp tính đường hô hấp.', 'Bệnh phổi kẽ.', 'Thuyên tắc phổi.', 'Nhiễm ceton acid tiểu đường.']
  line   4778 | Challenging | id ba7ed98224dc46fab0152de7e9d73171 | D -> Nhiễm ceton acid tiểu đường.
  line   6091 | Challenging | id 535d56332e4d477d89bb00c9a051566a | D -> Nhiễm ceton acid tiểu đường.

### Group 831 — topic: Radiology, Pulmonology
Q: Các kỹ thuật x quang hiện nay không hoặc rất hiếm khi chỉ định là chụp cắt lớp cổ điển, chụp phế quản cản quang, chụp động mạch phổi
Options (shared set): ['Đúng', 'Sai']
  line   4792 | Easy        | id c301a92853e0485f8a981b5cb27e041b | A -> Đúng
  line   9120 | Easy        | id d55b37a54d3b4332914529cebd9ddf0e | A -> Đúng

### Group 832 — topic: Pulmonology
Q: Khoang màng phổi là 1 khoang ảo được hiểu là khoang?
Options (shared set): ['Có dung tích, không có thể tích', 'Có thể tích,không có dung tích', 'Có dung tích và thể tích xác định', 'Có thể tích và dung tích nhỏ']
  line   4800 | Easy        | id e7eb5e84195d4c73b86fd999244db4f5 | A -> Có dung tích, không có thể tích
  line   5582 | Easy        | id f825958c33944cf2a8f580034d9c78fc | A -> Có dung tích, không có thể tích

### Group 833 — topic: Pulmonology, Radiology
Q: Đặc điểm tràn dịch khe liên thùy?
Options (shared set): ['Hình chữ S đảo ngược', 'Có dấu hiệu hội tụ rốn phổi', 'Có hình mờ dạng hình thoi, nằm theo khe liên thùy', 'Hình mờ dạng hình thoi nằm theo khe liên thùy thấy được trên cả phim chụp tim phổi thẳng và nghiêng']
  line   4810 | Medium      | id e4a84bb903374f1f94529b23bc81d4fa | C -> Có hình mờ dạng hình thoi, nằm theo khe liên thùy
  line   5581 | Medium      | id dd8d2867b4514dd9ad70543c91df7e7b | A -> Có hình mờ dạng hình thoi, nằm theo khe liên thùy

### Group 834 — topic: Pulmonology, Infectious Diseases
Q: Cần chẩn đoán phân biệt lao kê với?
Options (shared set): ['Ứ huyết phổi, bụi phổi', 'Ứ huyết phổi, Di căn ung thư thể thả bóng', 'Bụi phổi, Di căn ung thư thể thả bóng', 'Di căn ung thư thể thả bóng']
  line   4823 | Medium      | id 0405602cd14f48ffa9b8dcdeaba40452 | A -> Ứ huyết phổi, bụi phổi
  line   5591 | Medium      | id ab115cf0a34d419abf726c0dfa1ad559 | A -> Ứ huyết phổi, bụi phổi

### Group 835 — topic: Pulmonology, Radiology
Q: Đặc điểm hình ảnh của tràn dịch khoang màng phổi thể tự do trên phim chụp tim phổi thẳng
Options (shared set): ['Bờ của trung thất, vòm hoành không bị xóa', 'Trong hình mờ vẫn thấy được hình nhu mô phổi', 'Dịch tập trung ở vùng đáy phổi khi chụp ở tư thế đứng', 'Hình mờ đồng đều']
  line   4825 | Medium      | id b8fe4cc6dbf142a3ae5b115709ca43c9 | C -> Dịch tập trung ở vùng đáy phổi khi chụp ở tư thế đứng
  line   5577 | Medium      | id ea25f49103aa46b7b0482189892a717c | A -> Dịch tập trung ở vùng đáy phổi khi chụp ở tư thế đứng

### Group 836 — topic: Pulmonology, Radiology
Q: Đặc điểm tràn dịch khoang màng phổi lượng nhiều thể tự do điển hình trên phim chụp XQ tim phổi thẳng :
Options (shared set): ['Có hình của đường cong Damoiseau', 'Không thấy được hình nhu mô phổi vùng tràn dịch', 'Bờ trung thất và vòm hoành không bị xóa', 'Trung thất bị đẩy sang bên lành']
  line   4829 | Medium      | id 22ed2acddb064fb1b4b9567e40a4c0cb | A -> Có hình của đường cong Damoiseau
  line   5578 | Medium      | id 55bb2c1656814b4782834ad022b9886b | A -> Có hình của đường cong Damoiseau

### Group 837 — topic: Infectious Diseases, Pediatrics, Pulmonology
Q: Biểu hiện lâm sàng của bệnh ho gà kéo dài lâu nhưng thời kỳ có thể lây bệnh kết thúc trước khi kết thúc biểu hiện lâm sàng
Options (shared set): ['Đúng', 'Sai']
  line   4877 | Medium      | id ece085b4c3b141f0a297f713763487d4 | A -> Đúng
  line   5923 | Medium      | id e4ef4097bd2449f7982166b6b65a57ee | A -> Đúng

### Group 838 — topic: Pediatrics, Infectious Diseases, Pulmonology
Q: Ho gà là bệnh lây qua đường hô hấp truyền từ động vật sang người.
Options (shared set): ['Đúng', 'Sai']
  line   4879 | Easy        | id ca7afccea37a4b8596b37b82f64a048a | B -> Sai
  line   5930 | Easy        | id 65d0ffd07054409f8c58e484efbd302f | B -> Sai

### Group 839 — topic: Pulmonology
Q: Dung tích sống:
Options (shared set): ['Là số lít khí hít vào tối đa sau khi hít vào bình thường.', 'Là số lít khí thở ra tối đa sau thở ra bình thường.', 'Là số lít khí thở ra tối đa sau khi hít vào bình thường.', 'Là số lít khí thở ra tối đa sau hít vào tối đa.']
  line   4938 | Easy        | id 5f0d6d75caac468cb83c9fedf7498b12 | D -> Là số lít khí thở ra tối đa sau hít vào tối đa.
  line   4974 | Easy        | id 8aad73f0241e42b388271ca0987991d8 | D -> Là số lít khí thở ra tối đa sau hít vào tối đa.

### Group 840 — topic: Pulmonology
Q: Ở mô, máu nhận CO2 từ mô do:
Options (shared set): ['Phân áp CO2 ở mô cao hơn phân áp CO2 trong máu.', 'Tăng quá trình bão hoà oxyhemoglobin (HbO2).', 'Tăng khuếch tán ion Cl- từ hồng cầu ra huyết tương.', 'CO2 đi vào hồng cầu và ion Cl- đi ra huyết tương.']
  line   4940 | Medium      | id 4fcfd1cb460e4c1ba4ba7f1a8e026550 | A -> Phân áp CO2 ở mô cao hơn phân áp CO2 trong máu.
  line   4991 | Easy        | id 8b7e4109b3ae4c50a2b293a1665d4456 | A -> Phân áp CO2 ở mô cao hơn phân áp CO2 trong máu.

### Group 841 — topic: Pulmonology
Q: Áp suất khoang màng phổi:
Options (shared set): ['Có tác dụng làm cho phổi luôn giãn sát với lồng ngực.', 'Có giá trị thấp nhất ở thì hít vào thông thường.', 'Được tạo ra do tính đàn hồi của lồng ngực.', 'Có giá trị cao hơn áp suất khí quyển ở cuối thì thở ra.']
  line   4941 | Medium      | id ffe1a764479d43a99b920553131c5982 | A -> Có tác dụng làm cho phổi luôn giãn sát với lồng ngực.
  line   4969 | Medium      | id f29f609cf0f0475ebe10a4190d7b3261 | A -> Có tác dụng làm cho phổi luôn giãn sát với lồng ngực.

### Group 842 — topic: Pulmonology
Q: Áp suất âm màng phổi có các ý nghĩa sau đây, trừ:
Options (shared set): ['Lồng ngực dễ di động khi thở.', 'Phổi co giãn theo sự di động của lồng ngực.', 'Máu về tim và lên phổi dễ dàng.', 'Hiệu suất trao đổi khí đạt mức tối đa.']
  line   4942 | Medium      | id 49ea416be96f43d692c50f4c62cd1328 | A -> Lồng ngực dễ di động khi thở.
  line   4971 | Medium      | id cd84697b43da453182fda1cadb0b9f42 | A -> Lồng ngực dễ di động khi thở.

### Group 843 — topic: Pulmonology
Q: Dung tích toàn phổi (TLC) bằng:
Options (shared set): ['IC + FRC.', 'FRC + IRV.', 'TV + IRV + ERV.', 'IC + TV + FRC.']
  line   4943 | Easy        | id 7f57682d60cf4da6a9226c65983c3392 | A -> IC + FRC.
  line   4975 | Easy        | id 19b09393bed84408857f9eb125c7d86c | A -> IC + FRC.

### Group 844 — topic: Pulmonology
Q: Giá trị áp suất màng phổi qua các động tác hô hấp:
Options (shared set): ['Cuối thì thở ra tối đa là +7 mmHg.', 'Cuối thì thở ra bình thường là 0 mmHg.', 'Cuối thì hít vào bình thường là -7 mmHg.', 'Cuối thì hít vào tối đa là -15 mmHg']
  line   4944 | Easy        | id 82a3230f45f94f3dabbc4823a9eb7d67 | C -> Cuối thì hít vào bình thường là -7 mmHg.
  line   4970 | Medium      | id 0d5376f76be54eea8d4cc1e58123e3e5 | C -> Cuối thì hít vào bình thường là -7 mmHg.

### Group 845 — topic: Pulmonology
Q: Các thông số đánh giá hạn chế hô hấp là:
Options (shared set): ['TLC, RV, FRC.', 'VC, TLC.', 'VC, FRC, MMEF.', 'TLC, FEV1, FRC.']
  line   4945 | Easy        | id 060f184ee5bd47d8bc7994ba7335ceb9 | B -> VC, TLC.
  line   4976 | Easy        | id 175f53946549448987726fbf9c4703db | B -> VC, TLC.

### Group 846 — topic: Pulmonology
Q: Tác động của các cơ hô hấp lên phổi được thực hiện gián tiếp thông qua sự thay đổi áp suất khoang màng phổi.
Options (shared set): ['Đúng', 'Sai']
  line   4956 | Medium      | id 20a43ba37fb341fda7237cef1570e58e | A -> Đúng
  line   5454 | Medium      | id ee91ba7e61304831af2341f40ad9ba6e | A -> Đúng

### Group 847 — topic: Pulmonology
Q: Nguyên nhân trực tiếp làm cho không khí di chuyển qua đường hô hấp là sự dao động có chu kỳ của áp suất khoang màng phổi.
Options (shared set): ['Đúng', 'Sai']
  line   4957 | Medium      | id cfdb088bc7e443a696ec40b112e6b7ec | B -> Sai
  line   5456 | Medium      | id c28cbde277314c0ba340777f0519e0b0 | B -> Sai

### Group 848 — topic: Pulmonology, Hematology
Q: Dạng vận chuyển chủ yếu CO2 trong máu là:
Options (shared set): ['Dạng hoà tan.', 'Dạng kết hợp với Hb.', 'Dạng kết hợp với muối kiềm.', 'Dạng kết hợp với protein.']
  line   4980 | Easy        | id 8b6e4c57ea7d41eaa56180fe4bddd5ba | C -> Dạng kết hợp với muối kiềm.
  line  10064 | Easy        | id ae1f0c6ecfd44eaa8e4ce69307b384c9 | C -> Dạng kết hợp với muối kiềm.

### Group 849 — topic: Pulmonology, Neurology
Q: Vai trò của CO2 trong điều hoà hô hấp:
Options (shared set): ['CO2 tác động trực tiếp lên trung tâm hô hấp.', 'CO2 tác động trực tiếp lên trung tâm hít vào.', 'CO2 tác động trực tiếp lên trung tâm hoá học.', 'CO2 tác động lên trung tâm hô hấp thông qua ion H+.']
  line   4983 | Medium      | id 1f84025466c643a5ac3ca8e826dac879 | D -> CO2 tác động lên trung tâm hô hấp thông qua ion H+.
  line  10014 | Medium      | id 0da759ec93c04ded805ed0caa55882cf | D -> CO2 tác động lên trung tâm hô hấp thông qua ion H+.

### Group 850 — topic: Pulmonology, Hematology
Q: Oxy kết hợp với Hb ở nơi có:
Options (shared set): ['Phân áp O2 cao, phân áp CO2 cao.', 'Phân áp O2 cao, phân áp CO2 thấp.', 'Phân áp O2 thấp, phân áp CO2 cao.', 'Phân áp O2 thấp, phân áp CO2 thấp.']
  line   4985 | Easy        | id 005a6a2b71dc4edfbd28bf9343e1acdd | B -> Phân áp O2 cao, phân áp CO2 thấp.
  line  11832 | Easy        | id 3232e23ef3484a95b3206b994efdc91e | B -> Phân áp O2 cao, phân áp CO2 thấp.

### Group 851 — topic: Pulmonology, Otolaryngology
Q: Hạt thực vật thường mắc ở:
Options (shared set): ['Thanh quản', 'Khí quản', 'Phế quản gốc trái', 'Phế quản gốc phải']
  line   5021 | Medium      | id 98d20bafed204153b22188430bd0dce2 | D -> Phế quản gốc phải
  line   9915 | Medium      | id fffdc3084e8b45d193f0251fff679c52 | D -> Phế quản gốc phải

### Group 852 — topic: Infectious Diseases, Pulmonology
Q: Điều nào sau đây không đúng với bệnh bạch hầu
Options (shared set): ['Người bệnh là nguồn bệnh duy nhất', 'Lây lan chủ yếu qua đường hô hấp', 'Vi trùng bạch hầu có sức đề kháng tốt với môi trường', 'Chỉ trực khuẩn bạch hầu sinh độc tố mới có khả năng gây bệnh nặng']
  line   5033 | Medium      | id 9949d90bbb2346038f3408db55cbcbf0 | A -> Người bệnh là nguồn bệnh duy nhất
  line   5066 | Medium      | id c77bdae0f28e4326b286cf74b47ca633 | A -> Người bệnh là nguồn bệnh duy nhất
  line   5075 | Medium      | id 8796feb673b64ce1be1708787e547f58 | A -> Người bệnh là nguồn bệnh duy nhất
  line   5082 | Medium      | id 6988234fce134a52b183fa8cd4f3bf3c | A -> Người bệnh là nguồn bệnh duy nhất

### Group 853 — topic: Infectious Diseases, Pulmonology
Q: Bệnh nhân bạch hầu thanh quản nhập viện ngày 3 của bệnh, liều SAD là
Options (shared set): ['20.000 đơn vị', '20.000-40.000 đơn vị', '60.000-80.000 đơn vị', '80.000-120.000 đơn vị']
  line   5035 | Medium      | id 82efa04b0c5144a4ac733d3aa99ab3d1 | B -> 20.000-40.000 đơn vị
  line   5067 | Medium      | id 4f48b3e5dd0941fc9edee13ca35db1eb | B -> 20.000-40.000 đơn vị

### Group 854 — topic: Infectious Diseases, Pulmonology
Q: Nhiễm trùng cơ hội phổ biến nhất trên bệnh nhân AIDS ở Việt Nam là
Options (shared set): ['Viêm phổi PCP', 'Lao phổi', 'Nhiễm nấm huyết Talaromyces marneffei', 'Viêm não do Toxoplasma Gondii']
  line   5036 | Easy        | id 62377fe824534c9096d0541d8d21b2d6 | B -> Lao phổi
  line   5083 | Medium      | id 576df8343c1049bcaf0228c5145a4cdc | B -> Lao phổi

### Group 855 — topic: Infectious Diseases, Pulmonology
Q: Điều nào sau đây đúng khi nói về bệnh cúm
Options (shared set): ['Tiêm vắc xin cúm có khả năng bảo vệ trên 90%', 'Hạ sốt bằng lau mát, paracetamol hoặc aspirin', 'Không được xông hơi vì dễ gây mất nước', 'Thuốc kháng virus đặc hiệu chỉ được dùng trong trường hợp cúm biến chứng hoặc cơ địa dễ bị biến chứng']
  line   5037 | Medium      | id ae5159ccccec495782b786818454f6b8 | D -> Thuốc kháng virus đặc hiệu chỉ được dùng trong trường hợp cúm biến chứng hoặc cơ địa dễ bị biến chứng
  line   5077 | Medium      | id 3000533fc87645229067c9bc012d09c6 | D -> Thuốc kháng virus đặc hiệu chỉ được dùng trong trường hợp cúm biến chứng hoặc cơ địa dễ bị biến chứng
  line   5084 | Medium      | id d450e60621134aceb72fe95eb0a66449 | D -> Thuốc kháng virus đặc hiệu chỉ được dùng trong trường hợp cúm biến chứng hoặc cơ địa dễ bị biến chứng

### Group 856 — topic: Infectious Diseases, Pulmonology, Radiology
Q: Bệnh nhân sốt, đau cơ, ho khan 3 ngày. Trước hai ngày khởi bệnh, bệnh nhân có tiếp xúc với người hàng xóm bị cúm. X-quang phổi có hình ảnh kính mờ lan tỏa. Tác nhân gây viêm phổi nào nghĩ tới nhiều nhất
Options (shared set): ['Staptococcus aureus', 'Streptococcus pneumonia', 'Influenza', 'Mycobacterium tuberculosis']
  line   5038 | Challenging | id fb0acce401d448c4abb95715a0971f0c | C -> Influenza
  line   5070 | Challenging | id 9da73810f03c448b85e8e9d477f10699 | C -> Influenza
  line   5078 | Challenging | id 0eb88b6cf02b4ddb8fcdfb950f56ce6b | C -> Influenza

### Group 857 — topic: Infectious Diseases, Pulmonology, Internal Medicine
Q: Chẩn đoán mức độ bệnh COVID-19 không dựa vào yếu tố nào sau đây?
Options (shared set): ['Tình trạng suy hô hấp', 'Cơ địa của bệnh nhân', 'Mức độ tổn thương phổi trên X-quang', 'Tri giác của bệnh nhân']
  line   5040 | Medium      | id 381be70b3bb64b7f8f943d67af800b0f | C -> Mức độ tổn thương phổi trên X-quang
  line   5072 | Medium      | id 3a7bdc8e2fbd4a8ca7e63576913907c2 | C -> Mức độ tổn thương phổi trên X-quang
  line   5080 | Medium      | id 6b4b5bb125aa46da965b881ab7353ea3 | C -> Mức độ tổn thương phổi trên X-quang
  line   5086 | Medium      | id aee05d60c533440c929e40740234bb7e | C -> Mức độ tổn thương phổi trên X-quang

### Group 858 — topic: Infectious Diseases, Pulmonology, Internal Medicine
Q: Bệnh nhân nữ, 19 tuổi, sốt, ho, đau họng ngày thứ 3. Bệnh nhân nhập viện trong tình trạng thở nhanh 23 lần/ph, SpO2 95% với khí trời, tỉnh táo, mạch 90l/ph, HA 120/70mmHg, X-quang phổi có tổn thương nhỏ dạng kính mờ ở rìa phổi, test nhanh SARS-CoV-2 dương tính. Bệnh nhân được chẩn đoán COVID-19 mức độ nào?
Options (shared set): ['Mức độ nhẹ', 'Mức độ trung bình', 'Mức độ nặng', 'Mức độ nguy kịch']
  line   5041 | Challenging | id 76eefc0144624da9a4bdba7137a61d66 | A -> Mức độ nhẹ
  line   5073 | Challenging | id 7264639f83824544a3805c1460821cfa | A -> Mức độ nhẹ
  line   5087 | Challenging | id 3a16f381ba934fce9e353159247fdf41 | A -> Mức độ nhẹ

### Group 859 — topic: Infectious Diseases, Pulmonology, Internal Medicine
Q: Bệnh nhân nam, 65 tuổi, tiền căn COPD 10 năm. Bệnh nhân sốt, ho ngày thứ 5, nhập viện trong tình trạng tỉnh táo, không khó thở, SpO2 97%/khí trời, sinh hiệu ổn định. Bệnh nhân được chẩn đoán COVID-19 mức độ nhẹ. Có thể can thiệp hỗ trợ hô hấp cho bệnh nhân bằng biện pháp gì?
Options (shared set): ['Thở oxy qua gọng mũi 1-2 lít/phút, theo dõi', 'Thở oxy qua gọng mũi 5-6 lít/phút, theo dõi', 'Thở oxy qua mask có túi thở lại, nằm sấp nếu có thể', 'Thở CPAP, BPAP, nằm sấp nếu có thể']
  line   5042 | Challenging | id 92f58d955f704069bcfbb2371d5d728b | A -> Thở oxy qua gọng mũi 1-2 lít/phút, theo dõi
  line   5074 | Challenging | id d5cd745ecf604aaf8316e85f4caeb11c | A -> Thở oxy qua gọng mũi 1-2 lít/phút, theo dõi
  line   5081 | Challenging | id 76dabca4b5f6457998fc01e95ecb6e97 | A -> Thở oxy qua gọng mũi 1-2 lít/phút, theo dõi
  line   5088 | Challenging | id 8835c58f4a7a43d894cdb54b2db6f7a1 | A -> Thở oxy qua gọng mũi 1-2 lít/phút, theo dõi

### Group 860 — topic: Pulmonology, Infectious Diseases
Q: Một bệnh nhân nam 50 tuổi, có biểu hiện lâm sàng sốt, ho, khó thở, vào bệnh viện được chẩn đoán ban đầu là viêm màng phổi, gây tràn dịch màng phổi. Bệnh nhân được chọc dịch màng phổi làm xét nghiệm sinh hoá tế bào, kết quả xét nghiệm nào sau đây phù hợp bệnh cảnh trên?
Options (shared set): ['Giàu protein, TLPT >1020 Dalton, nhiều tế bào viêm', 'Giàu protein, TLPT <1020 Dalton, ít tế bào viêm', 'Nghèo protein, TLPT >1020 Dalton, nhiều tế bào viêm', 'Nghèo protein, TLPT <1020 Dalton, ít tế bào viêm']
  line   5043 | Challenging | id da0ee9a6b05944e3a6c2d36c7c0925cc | A -> Giàu protein, TLPT >1020 Dalton, nhiều tế bào viêm
  line   5373 | Challenging | id e1f3b821f3d64b4187c244aadb49acb4 | A -> giàu protein, TLPT >1020 Dalton, nhiều tế bào viêm

### Group 861 — topic: Pathology, Pulmonology
Q: Nhồi máu trắng không gặp ở
Options (shared set): ['Tim', 'Phổi', 'Não', 'Lách']
  line   5045 | Easy        | id fbac26ba69b743aa974091fe87ac9d68 | B -> Phổi
  line   5399 | Medium      | id dc4de57817ca4028ac3f5911cc705dfd | B -> Phổi

### Group 862 — topic: Infectious Diseases, Pulmonology
Q: Phản ứng Tuberculin thể hiện:
Options (shared set): ['nếu phản ứng dương tính chắc chắn cơ thể đang mắc lao.', 'nếu phản ứng âm tính chắc chắn cơ thể hiện không mắc lao.', 'phản ứng dương tính gợi ý cơ thể đã từng nhiễm lao trước đây.', 'phản ứng âm tính chứng tỏ có thể chưa từng mắc lao trước đây.']
  line   5046 | Medium      | id a567980e1d60484e84ea67105aa39f0b | C -> phản ứng dương tính gợi ý cơ thể đã từng nhiễm lao trước đây.
  line   5400 | Medium      | id 1ee0a5fa9acf485ab138f494a82452fc | C -> phản ứng dương tính gợi ý cơ thể đã từng nhiễm lao trước đây.

### Group 863 — topic: Pulmonology, Infectious Diseases
Q: Tiến triển của viêm phế quản, trừ:
Options (shared set): ['áp xe phổi', 'nhục hoá', 'giãn phế quản', 'đục khoét nhu mô phổi . Tiến triển của viêm phế quản gồm: áp xe phổi, nhục hoá, giãn phế quản, xơ hoá.']
  line   5047 | Medium      | id a6d99611eccd44d1bc7eeb707594ac8f | D -> đục khoét nhu mô phổi . Tiến triển của viêm phế quản gồm: áp xe phổi, nhục hoá, giãn phế quản, xơ hoá.
  line   5401 | Medium      | id f3fc076cbded40acba0860cc9413516a | D -> đục khoét nhu mô phổi . Tiến triển của viêm phế quản gồm: áp xe phổi, nhục hoá, giãn phế quản, xơ hoá.

### Group 864 — topic: Pulmonology, Pathology
Q: Tổn thương cơ bản của phế nang, trừ:
Options (shared set): ['tăng tiết.', 'biến hình đại thực bào.', 'dị sản.', 'teo và biến..Tổn thương cơ bản của phế nang gồm: biến hình đại thực bào, teo và biến, dị sản, viêm, u.']
  line   5048 | Medium      | id b0fc6667299d4d9884789e07d1a0a295 | A -> tăng tiết.
  line   5402 | Medium      | id 16b21efaaa664a348b4d2cf3156ab542 | A -> tăng tiết.

### Group 865 — topic: Pulmonology, Infectious Diseases, Pathology
Q: Về mặt vi thể, nang lao không có:
Options (shared set): ['trung tâm là chất hoại tử bã đậu.', 'ngoại vi là các tế bào dạng biểu mô sắp xếp lộn xộn.', 'bản chất vi thể là các tế bào u sắp xếp thành nang.', 'cả 3 đều đúng.']
  line   5049 | Easy        | id 70cde2a4cf724e2bbc5e89acdf576c69 | C -> bản chất vi thể là các tế bào u sắp xếp thành nang.
  line   5403 | Easy        | id 3928af3341464d4886c02623e2335e65 | C -> bản chất vi thể là các tế bào u sắp xếp thành nang.

### Group 866 — topic: Infectious Diseases, Pulmonology, Pathology
Q: Hoại tử bã đậu đặc trưng của viêm lao được hình thành do
Options (shared set): ['Các thành phần có ở lớp vỏ của vi khuẩn', 'Các thành phần của mô đệm liên kết', 'Trực khuẩn lao ái khí', 'Các yếu tố hóa hướng động của vi khuẩn']
  line   5051 | Easy        | id 8c1ee0577cb248ca9f6f11919474f109 | A -> Các thành phần có ở lớp vỏ của vi khuẩn
  line   5406 | Easy        | id b8723b45233f45f082f5903e704f4cd3 | A -> các thành phần có ở lớp vỏ của vi khuẩn
  line  10069 | Medium      | id 151c18ee70a84e39a799da1c497fce67 | A -> Các thành phần có ở lớp vỏ của vi khuẩn

### Group 867 — topic: Infectious Diseases, Pulmonology
Q: Đường xâm nhập gây viêm do trực khuẩn lao thường gặp
Options (shared set): ['Đường sinh dục', 'Đường qua da, niêm mạc', 'Đường hô hấp', 'Đường tiêu hóa']
  line   5052 | Easy        | id 9457ba3488844edb8a361a7266aecd7f | C -> Đường hô hấp
  line   5407 | Easy        | id f44568a266f54d66abaace28f0196126 | C -> Đường hô hấp

### Group 868 — topic: Infectious Diseases, Pulmonology, Pathology
Q: Trong viêm lao, chất hoạt tử bão đậu không tiến triển theo chiều hướng?
Options (shared set): ['Vôi hóa', 'Xơ hóa', 'Tự tiêu hóa', 'Nhuyễn hóa']
  line   5053 | Medium      | id 8245ac026be14ce7870e23c8c87c805f | A -> Vôi hóa
  line   5408 | Medium      | id 365d833f540942af81312e38f9855034 | A -> Vôi hóa

### Group 869 — topic: Pulmonology, Pathology
Q: Trong dị sản vảy, tế bào biểu mô phế quản, tế bào biểu mô trụ biến thành tế bào biểu mô lát tầng?
Options (shared set): ['Đúng', 'Sai']
  line   5054 | Medium      | id 78d87f0db73a4771b5bf3297687f8519 | A -> Đúng
  line   5409 | Easy        | id 3b463244c75342b18f1736ae449a037f | A -> Đúng

### Group 870 — topic: Pulmonology, Oncology, Pathology
Q: Hiện tượng hoại tử mỡ nhiều ổ ở phổi là dấu hiệu tổn thương hay gặp đi kèm trong?
Options (shared set): ['Phế viêm', 'Ung thư phế quản', 'Phế quản phế viêm', 'Lao phổi']
  line   5055 | Medium      | id 13d8ec38a3bd45c7ac96bec9adb187be | B -> Ung thư phế quản
  line   5410 | Medium      | id df871d6545324dc2a2abf138b45e8600 | B -> Ung thư phế quản
  line  10057 | Medium      | id d27d23da428f41b8988ca8d5e7b4efab | B -> Ung thư phế quản

### Group 871 — topic: Pulmonology, Infectious Diseases
Q: Viêm thuỳ phổi là nguyên nhân gây tử vong nhiều nhất trong các bệnh nhiễm trùng ở phổi?
Options (shared set): ['Đúng', 'Sai']
  line   5056 | Easy        | id 26d67d34ba8945fb828f1e898e6e2447 | B -> Sai
  line   5411 | Easy        | id 3e45ca7167564af38aed02dbf5ab3b3b | B -> sai

### Group 872 — topic: Pulmonology, Oncology, Pathology
Q: Trong các khối u ác tính của phổi, ung thư biểu mô tế bào lớn là loại có độ tiến triển ác tính cao nhất?
Options (shared set): ['Đúng', 'Sai']
  line   5057 | Easy        | id a3399658c9eb466d8ddf09ef9b4d3f14 | B -> Sai
  line   5412 | Medium      | id 97187a57481d453086f8400e357f5f21 | B -> sai

### Group 873 — topic: Infectious Diseases, Pulmonology, Pathology
Q: Bệnh viêm lao còn được gọi tên: tuberculosis dựa vào tổn thương cơ bản là:
Options (shared set): ['Nang lao', 'Củ lao', 'Hang lao', 'Chất bã đậu']
  line   5058 | Easy        | id 68639979cce6419d85942e4db7916328 | A -> Nang lao
  line   5413 | Medium      | id 0700bbd0af1941eb9436e35a33f98292 | A -> nang lao

### Group 874 — topic: Pulmonology, Pediatrics
Q: Tăng tiết là tổn thương hay gặp ở giai đoạn cuối của bệnh viêm phế quản - phổi?
Options (shared set): ['Đúng', 'Sai']
  line   5059 | Easy        | id 7ebc15801030404dbf892ad124aa9657 | B -> Sai
  line   5414 | Medium      | id a0de155fa5244de4b1ce16946f609206 | B -> sai

### Group 875 — topic: Pulmonology, Pediatrics, Infectious Diseases
Q: Bệnh phế quản - phế viêm ở trẻ em gặp trong mùa lạnh nhiều gấp 2-3 lần mùa nóng do:
Options (shared set): ['Do vi khuẩn tăng động lực trong mùa lạnh', 'Giảm sức đề kháng cơ thể', 'Do thiếu ánh nắng mặt trời nên vi khuẩn phát triển', 'Do để ứ đọng dịch tiết trong phế quản, phế nang do lạnh']
  line   5060 | Medium      | id 1d623650b1984baab55b327a3f236fef | B -> Giảm sức đề kháng cơ thể
  line   5415 | Medium      | id 8f616af00ff44fcaa888128ea45145c3 | B -> giảm sức đề kháng cơ thể

### Group 876 — topic: Pulmonology, Pathology, Infectious Diseases
Q: Tổn thương điểm hình nhất của viêm phế quản- phổi là các hạt Chacot- Rindfleichs gồm?
Options (shared set): ['Viêm phế quản và viêm phế nang mủ', 'Viêm phế nang mủ', 'Viêm phế quản và chảy máu', 'Viêm phế quản mủ và viêm phế quản nang các loại']
  line   5061 | Medium      | id 8392ceb93cc245de8d7af6e085e2bcb1 | D -> Viêm phế quản mủ và viêm phế quản nang các loại
  line   5416 | Medium      | id 1cecfca665fa420f9f925bf92fc76093 | D -> viêm phế quản mủ và viêm phế quản nang các loại

### Group 877 — topic: Pulmonology, Infectious Diseases
Q: Một bệnh nhân nam 50 tuổi có biểu hiện lâm sàng sốt, ho, khó thở, vào bệnh viện được chẩn đoán ban đầu là viêm phổi màng phổi gây tràn dịch màng phổi. Bệnh nhân được chọc dịch màng phổi làm xét nghiệm sinh hóa tế bào, kết quả xét nghiệm nào sau đây là phù hợp với bệnh cảnh trên nhất?
Options (shared set): ['Giàu protein, trọng lượng phân tử > 1020 Dalton, nhiều tế bào viêm', 'Giàu protein, trọng lượng phân tử < 1020 Dalton, ít tế bào viêm', 'Nghèo protein, trọng lượng phân tử > 1020 Dalton, nhiều tế bào viêm', 'Nghèo protein, trọng lượng phân tử < 1020 Dalton, ít tế bào viêm']
  line   5065 | Challenging | id 1b6a6f44565c4a4e9552dd54412503b5 | A -> Giàu protein, trọng lượng phân tử > 1020 Dalton, nhiều tế bào viêm
  line   5834 | Challenging | id f26a547eba704186a111ccfb73272df0 | A -> Giàu protein, trọng lượng phân tử > 1020 Dalton, nhiều tế bào viêm

### Group 878 — topic: Pulmonology, Surgery
Q: Tai biến của sinh thiết màng phổi mù:
Options (shared set): ['Tràn máu màng phổi', 'Nhiễm trùng khoang màng phổi', 'Tràn khí màng phổi', 'Tất cả đều đúng']
  line   5105 | Medium      | id 96c0c8163e52406682e840347590fdb2 | D -> Tất cả đều đúng
  line   9705 | Medium      | id 14980c42ec3b4a7382b782ba889d4319 | D -> Tất cả đều đúng

### Group 879 — topic: Pulmonology, Otolaryngology
Q: Nguyên nhân tắc đường hô hấp trên ngoại sinh là
Options (shared set): ['Phù thanh quản', 'Liệt dây thanh 2 bên', 'U hạch', 'Sập các tổ chức phần mềm vùng họng miệng']
  line   5135 | Medium      | id e1069854b9de411a8276bfc1351612c6 | C -> U hạch
  line   5805 | Medium      | id 3611127f894b44009cc0fa4ffb5935ec | C -> U hạch

### Group 880 — topic: Pulmonology
Q: Biểu hiện đợt cấp bệnh phổi tắc nghẽn mạn tính mức độ nặng, chọn câu đúng?
Options (shared set): ['Rối loạn ý thức', 'Hô hấp nghịch thường', 'Tụt huyết áp', 'Khó thở liên tục']
  line   5136 | Medium      | id 016a85dce2684488b43bed50a80a9d9a | D -> Khó thở liên tục
  line   5804 | Medium      | id 34eb6b9ac13c4267891f8855791d1802 | D -> Khó thở liên tục

### Group 881 — topic: Pulmonology
Q: Kết quả khí máu: pH = 7.6, PaCO2 = 20mmHg, HCO3- = 20mmol/l, kết luận là:
Options (shared set): ['Kiềm hô hấp cấp', 'Toan chuyển hóa', 'Toan hô hấp cấp', 'Kiềm hô hấp mạn']
  line   5151 | Medium      | id 65781b0984d44655aa5f8688a22ab894 | A -> Kiềm hô hấp cấp
  line   5801 | Medium      | id 69fc618cba4b4e6cabb5f0dad97f2287 | A -> Kiềm hô hấp cấp
  line  10962 | Medium      | id e11b966e0fd641f2983adfbc3a6bc9a4 | A -> Kiềm hô hấp cấp

### Group 882 — topic: Pulmonology
Q: pH = 7.36, HCO3- = 25mmol/l, PaCo2 = 48 mmHg, kết quả nào sau là đúng
Options (shared set): ['Toan hô hấp mạn', 'Toan hô hấp cấp', 'Toan hỗn hợp', 'Toan đơn thuần']
  line   5152 | Medium      | id 8a3564e6ead04c2a9571a3f34be84017 | B -> Toan hô hấp cấp
  line   5802 | Medium      | id 9928e8e84e7c4e018c00f16f62456eb8 | C -> Toan hỗn hợp

### Group 883 — topic: Infectious Diseases, Pulmonology
Q: Điều kiện cần để mắc LSN?
Options (shared set): ['Chưa chủng ngừa BCG', 'Suy dinh dưỡng', 'Tiếp xúc với vk lao', 'Dùng corticoide kéo dài']
  line   5168 | Medium      | id 3695888cfb084352934501f13596c813 | C -> Tiếp xúc với vk lao
  line   5192 | Medium      | id 73608b8521db4fc083f88760ceea6173 | C -> Tiếp xúc với vk lao

### Group 884 — topic: Infectious Diseases, Pulmonology
Q: Lao phổi
Options (shared set): ['Là lao nguyên phát', 'Là lao sơ nhiễm', 'Là lao thứ phát', 'Thường là lao thứ phát']
  line   5169 | Easy        | id 22d0151d7a854be8b29218b5f1b9874d | D -> Thường là lao thứ phát
  line   5193 | Easy        | id 8588bcd06a7c42918472a1585e70a9c2 | D -> Thường là lao thứ phát

### Group 885 — topic: Pulmonology, Infectious Diseases
Q: Trong lao sơ nhiễm, tiếng ral rít, ral ngáy ở KLS 3-4 trước ngực (P) thường do nguyên nhân gì gây nên?
Options (shared set): ['Do phù nề phế quản', 'Do viêm phế quản', 'Do viêm phế nang', 'Do hạch trung thất chèn ép']
  line   5170 | Medium      | id cb7fbd6cb3184efd8bab5971bb2378ee | D -> Do hạch trung thất chèn ép
  line   5194 | Medium      | id 2f8cb57b74e244d39eef80dd483ea46b | D -> Do hạch trung thất chèn ép

### Group 886 — topic: Pulmonology, Infectious Diseases, Pathology
Q: Trong chẩn đoán lao phổi, dấu hiệu nào sau đây giúp ta khẳng định chẩn đoán?
Options (shared set): ['Xquang phổi có hang nghi ngờ do lao', 'Bệnh nhân ho kéo dài trên 2 tuần không rõ nguyên nhân', 'Bệnh nhân ho ra máu kéo dài', 'Soi tươi đờm có trực khuẩn bắt màu đỏ Fusin']
  line   5172 | Medium      | id f2fad0fe9e4d4c8d9f12617953c23185 | D -> Soi tươi đờm có trực khuẩn bắt màu đỏ Fusin
  line   5196 | Medium      | id e48ed55098dd4334b2c263b19fa8a08d | D -> Soi tươi đờm có trực khuẩn bắt màu đỏ Fusin

### Group 887 — topic: Pulmonology, Infectious Diseases
Q: Các tổn thương ít gặp trong lao phổi gồm:
Options (shared set): ['Hang lao', 'Củ lao', 'Hạch lao', 'Tổn thương xơ']
  line   5173 | Easy        | id 7afbd97eb18f4bf4a0ae14c837423bbe | C -> Hạch lao
  line   5197 | Medium      | id d58eb1dd6da34087b17feb1683e0e363 | C -> Hạch lao

### Group 888 — topic: Pulmonology, Infectious Diseases
Q: Bệnh lao là bệnh di truyền?
Options (shared set): ['đúng do gen di truyền', 'sai có truyền nhưng truyền nhiễm']
  line   5174 | Easy        | id e1fa3a47ccb0462f83c9ec7dd8d5f121 | B -> sai có truyền nhưng truyền nhiễm
  line   5186 | Easy        | id 344b332cdcf84aee81918d38633ca823 | B -> sai có truyền nhưng truyền nhiễm

### Group 889 — topic: Pulmonology, Infectious Diseases, Pathology
Q: Vi khuẩn lao không bị tiêu diệt bởi cồn 70 độ?
Options (shared set): ['Đúng', 'Sai']
  line   5177 | Easy        | id 15e2048ff82e455e832400365be8aca0 | B -> Sai
  line   5187 | Easy        | id 9e0d88bbab7e4d039102638f61f2d77f | B -> Sai

### Group 890 — topic: Pulmonology, Infectious Diseases
Q: Lao phổi thường là lao thứ phát?
Options (shared set): ['đúng', 'sai']
  line   5183 | Easy        | id 3569bf1ff01441d1b0efea7ae1e15e6c | A -> đúng
  line   5188 | Easy        | id 99a3690f29284760bd9e63ccc021bb9a | A -> Đúng

### Group 891 — topic: Endocrinology, Pulmonology
Q: Hormon nào sau đây có tác động điều hòa lưu lượng khí vào phổi ?
Options (shared set): ['Cortisol', 'Catecholamin', 'Aldosterol', 'Serotonin']
  line   5256 | Medium      | id 95b72438a0fd465eb76419f66e347af0 | B -> Catecholamin
  line   6789 | Medium      | id 81ee172bc58a47ff85ba1d20bfbcd9bc | B -> Catecholamin

### Group 892 — topic: Pulmonology, Sports Medicine
Q: Chọn câu đúng. Khi lao động nặng:
Options (shared set): ['Giảm PCO2 trong máu', 'Tăng phân ly O2 với Hb', 'Tăng vận chuyển O2 trong hồng cầu', 'pH máu tăng']
  line   5262 | Medium      | id ee0c5f584b024ecd95093eb45e5f14cb | B -> Tăng phân ly O2 với Hb
  line  12157 | Easy        | id b8627ad625c940e9be9e986ab44361f2 | B -> Tăng phân ly O2 với Hb

### Group 893 — topic: Pulmonology, Infectious Diseases
Q: Lao phổi điều trị thất bại là?
Options (shared set): ['Bệnh nhân còn vi khuẩn lao sau điều trị 5 tháng', 'Bệnh nhân còn vi khuẩn lao sau điều trị 3 tháng', 'Bệnh nhân còn vi khuẩn lao sau điều trị 4 tháng', 'Bệnh nhân còn vi khuẩn lao sau điều trị 2 tháng']
  line   5316 | Medium      | id 5ae63707cd424bc097ebc1291a6e6f7d | A -> Bệnh nhân còn vi khuẩn lao sau điều trị 5 tháng
  line   9984 | Medium      | id a39bb5e4fd1c4b9e8bff659d933f75f5 | A -> Bệnh nhân còn vi khuẩn lao sau điều trị 5 tháng

### Group 894 — topic: Pulmonology, Sports Medicine
Q: Thuốc nào sau đây được sử dụng trong hen suyễn do gắng sức
Options (shared set): ['Cromolyn', 'Salbutamol', 'Theophylin', 'Corticoid']
  line   5329 | Medium      | id 8d35f8d7e4d34062860783582a5825f7 | A -> Cromolyn
  line  12097 | Medium      | id 8be8cdc430f04f72bd6c545b0424b442 | A -> Cromolyn

### Group 895 — topic: Pulmonology
Q: Chỉ số Tiffeneau được định nghĩa:
Options (shared set): ['Thể tích khí lưu thông', 'Thể tích cặn (sau khi đã thở ra gắng sức)', 'Dung tích phổi (toàn bộ) trừ đi thể tích cặn', 'Tỷ lệ % của FEV1/FVC']
  line   5332 | Easy        | id 632221eb15b84a6e830cee1d33ed5697 | D -> Tỷ lệ % của FEV1/FVC
  line   5341 | Easy        | id 13bdd9db370249689e674abb3e2e062b | D -> Tỷ lệ % của FEV1/FVC

### Group 896 — topic: Pulmonology, Endocrinology
Q: Tác nhân nào sau đây KHÔNG làm giảm kali huyết ở bệnh nhân hen suyễn?
Options (shared set): ['Tăng nhịp thở ở bệnh nhân hen suyễn', 'Thuốc corticoid', 'Thuốc chủ vận beta-2', 'Theophyllin 2']
  line   5342 | Medium      | id 74bb9ab343504d419c2b74c7baaadaaf | A -> Tăng nhịp thở ở bệnh nhân hen suyễn
  line   6821 | Medium      | id d8c785242b8d4f32838a0d9ca8e3fd42 | A -> Tăng nhịp thở ở bệnh nhân hen suyễn

### Group 897 — topic: Infectious Diseases, Pulmonology
Q: Điều nào dưới đây phù hợp với bệnh cúm
Options (shared set): ['Tác nhân gây bệnh là 5 loại virus Ifluenza A,B,C,D,E', 'Virus cúm B và C hay gây các trận dịch lớn cho cộng đồng', 'Người bệnh và người lành mang trùng là nguồn bệnh duy nhất', 'Bệnh cúm bắt đầu lây khi bệnh nhân khởi sự sốt cao']
  line   5366 | Medium      | id 98a63b4450e847da8bd53e413ed2f3af | C -> Người bệnh và người lành mang trùng là nguồn bệnh duy nhất
  line   5372 | Medium      | id c8a825c4d5254c7aaa3c472721c9fa6b | C -> Người bệnh và người lành mang trùng là nguồn bệnh duy nhất

### Group 898 — topic: Pediatrics, Pulmonology
Q: Một trẻ 25 ngày tuổi ho, sốt 39 độ, thở 65 lần/phút, được xếp loại theo TC YTTG như thế nào?
Options (shared set): ['Viêm phổi, uống kháng sinh tại nhà', 'Không viêm phổi, chăm sóc tại nhà', 'Viêm phổi nặng, dùng kháng sinh và chuyển đến bệnh viện', 'Bệnh rất nặng, dùng kháng sinh và chuyển đến bệnh viện']
  line   5468 | Challenging | id 75116c4f186f4008ad8424367d030c53 | D -> Bệnh rất nặng, dùng kháng sinh và chuyển đến bệnh viện
  line  10019 | Challenging | id 4621d736b74d4d4880448e2039155fb4 | D -> Bệnh rất nặng, dùng kháng sinh và chuyển đến bệnh viện

### Group 899 — topic: Pulmonology, Infectious Diseases
Q: Virus gây viêm phổi nặng hay gặp nhất là?
Options (shared set): ['Hợp bào hô hấp', 'Á cúm', 'Cúm A H5N1', 'Adenovirus']
  line   5479 | Easy        | id 4a395f8426db43be8e04a3942f899cec | A -> Hợp bào hô hấp
  line   5552 | Easy        | id e4f639bc905e45588663ec4ed5ce0cbb | B -> hợp bào hô hấp

### Group 900 — topic: Pediatrics, Pulmonology, Infectious Diseases
Q: Viêm phổi do Mycoplasma thường gặp ở trẻ?
Options (shared set): ['< 1 tuổi', '1-2 tuổi', '3-4 tuổi', '> 5 tuổi']
  line   5483 | Easy        | id 69bdd06c56b6442989fb3a397cd3b0a3 | D -> > 5 tuổi
  line   5555 | Easy        | id 6c792f75722643c2a2601723ff16c703 | D -> >5 tuổi

### Group 901 — topic: Pulmonology
Q: Cơn hen điển hình hay xảy ra
Options (shared set): ['Buổi sáng', 'Buổi chiều', 'Ban đêm', 'Nửa đêm về sáng']
  line   5503 | Medium      | id f9e313e394c2492095fd326a690f73c3 | D -> Nửa đêm về sáng
  line   5988 | Easy        | id 7e81f499939c425f9ad0124754d2af69 | D -> Nửa đêm về sáng

### Group 902 — topic: Pulmonology
Q: Trong cơn hen gõ phổi thấy
Options (shared set): ['Trong đều 2 bên', 'Đục rải rác', 'Gõ vang hơn bình thường', 'Gần như binh thường']
  line   5505 | Medium      | id 2d3321af2de54b80be476e291c3496d4 | C -> Gõ vang hơn bình thường
  line   5989 | Medium      | id 969cff6fc39d44ccacfd00d7f28f00ca | C -> Gõ vang hơn bình thường

### Group 903 — topic: Pulmonology, Radiology
Q: Chụp phổi trong hen thường thấy gì?
Options (shared set): ['Lồng ngực căng phồng', 'Khoang gian sườn giãn rộng', 'Vòm hoành hạ thấp', '2 phế trường tăng sáng']
  line   5514 | Medium      | id 73d8ad78f1284902a12c19d423d24b72 | D -> 2 phế trường tăng sáng
  line   9162 | Medium      | id fa128456a83242ecae2b05095417489c | D -> 2 phế trường tăng sáng

### Group 904 — topic: Infectious Diseases, Pulmonology
Q: Nhiễm khuẩn cấp tính đường hô hấp trên phần lớn do
Options (shared set): ['Vi khuẩn', 'Virus', 'Cảm lạnh', 'Vi khuẩn, virus']
  line   5522 | Easy        | id d876ad905b3146fbbb09271101deabc1 | B -> Virus
  line   5548 | Easy        | id 35d8e72c2f794599893cfca473970dab | D -> virus

### Group 905 — topic: Infectious Diseases, Pulmonology
Q: Viêm họng do virus thường
Options (shared set): ['Sốt nhẹ', 'Sốt cao', 'Sốt vừa', 'Không sốt']
  line   5523 | Medium      | id 8cf054dac8af47298ea89b89345b126d | A -> Sốt nhẹ
  line   5549 | Medium      | id a5aceefba4ef4f4787062b565fccd951 | A -> sốt nhẹ

### Group 906 — topic: Pulmonology
Q: Triệu chứng có giá trij chẩn đoán viêm phổi là
Options (shared set): ['ran ẩm tô hạt', 'ran ẩm nhỏ hạt', 'ran ngáy', 'ran rít']
  line   5564 | Medium      | id c13d6ca44b614096b82f95d88f869339 | B -> ran ẩm nhỏ hạt
  line  10038 | Medium      | id 035e4913d8ea4aae884a9554b8b30162 | B -> ran ẩm nhỏ hạt

### Group 907 — topic: Pulmonology, Pathology
Q: Thành vách phế nang dày, mao mạch sung huyết; phế nang nhiều tơ huyết ,hồng cầu,ít dịch phù
Options (shared set): ['Sung huyết', 'Gan hoá đỏ', 'Gan hoá xám', 'Mô hoá']
  line   5651 | Medium      | id 750f924cc76e49dfb63de1e9c1d5a7f1 | B -> Gan hoá đỏ
  line   8772 | Challenging | id c9d27a9e4ef245c8a7fec80f2bce0493 | B -> Gan hoá đỏ

### Group 908 — topic: Pulmonology
Q: Tràn dịch màng phổi dịch tiết trừ
Options (shared set): ['Lao', 'Ung thư', 'Xơ gan', 'Tắc động mạch phổi']
  line   5706 | Medium      | id ac08dbf823784d40ae93a21437b437db | C -> Xơ gan
  line  10017 | Medium      | id 5ea059796d194aafb662f543138077a6 | C -> Xơ gan

### Group 909 — topic: Neurology, Pulmonology, Internal Medicine
Q: Nhóm bệnh nào sau đây có thể dẫn đến tình trạng nhiễm base hô hấp
Options (shared set): ['U não, xuất huyết não- màng não, chấn thương não- màng não', 'U não, xuất huyết não- màng não, xẹp phổi', 'Xẹp phổi, hen phế quản, suy tim trái', 'U não, xuất huyết não- màng não, ung thư giai đoạn cuối']
  line   5742 | Medium      | id 5d22ca7019044fcea70bb591385fc59c | A -> U não, xuất huyết não- màng não, chấn thương não- màng não
  line   5762 | Medium      | id 3f53ef107fc74a048e01752562a11eec | A -> U não, xuất huyết não - màng não, chấn thuong não - màng não

### Group 910 — topic: Pulmonology, Neurology, Internal Medicine
Q: Chọn câu đúng:
Options (shared set): ['Nhiễm acid hô hấp gồm tất cả các nguyên nhân dẫn đến tình trạng tăng thông khí ở phổi', 'Nhiễm acid hô hấp gồm tất cả các nguyên nhân dẫn đến tình trạng tăng PCO2 ở máu và các dịch ngoại bào', 'Bệnh nhân có tổn thương thần kinh trung ương có nguy cơ nhiễm acid chuyển hóa', 'Bệnh nhân có tổn thương thần kinh trung ương có nguy cơ nhiễm base chuyển hóa']
  line   5743 | Medium      | id a820925ce2e14acfbf073495238eaa9a | B -> Nhiễm acid hô hấp gồm tất cả các nguyên nhân dẫn đến tình trạng tăng PCO2 ở máu và các dịch ngoại bào
  line   5763 | Medium      | id f6d674861a4f497a971c94ccc40e9e26 | B -> Nhiễm acid hô hấp gồm tất cả các nguyên nhân dẫn đến tình trạng tăng PCO2 ở máu và các dịch ngoại bào

### Group 911 — topic: Pulmonology
Q: Cơ chế nào sau đây KHÔNG phù hợp trong Bệnh phổi tắc nghẽn mạn tính
Options (shared set): ['Viêm là cơ chế bệnh sinh then chốt', 'Mất cân bằng giữa hoạt động của protease và anti-protease', 'Mất cân bằng giữa oxidant và antioxidant', 'Đột biến gen']
  line   5756 | Medium      | id 1a77a55eb2b143f8a322be5d0da5629a | D -> Đột biến gen
  line   5815 | Medium      | id ab258e70a57d4c05a5215e6e790db8a6 | D -> Đột biến gen
  line  10001 | Medium      | id 08f467a38ac9474d92281d87a36a1840 | D -> Đột biến gen

### Group 912 — topic: Pulmonology
Q: Các triệu chứng có thể gặp trong Bệnh phổi tắc nghẽn mạn tính KHÔNG bao gồm triệu chứng nào sau đây
Options (shared set): ['Nhức đầu buổi sáng.', 'Đa hồng cầu.', 'Tăng cân.', 'Phù chân']
  line   5757 | Medium      | id e90dc9ef75214617a7a2507b69606320 | C -> Tăng cân.
  line   5816 | Medium      | id a94a9b2b5635434290fe037b0765b504 | C -> Tăng cân

### Group 913 — topic: Pulmonology
Q: Đánh giá nào sau đây KHÔNG đúng trong đánh giá nguy cơ đợt cấp của bệnh phổi tắc nghẽn mạn tính
Options (shared set): ['Được đánh giá là đợt cấp khi các triệu chứng lâm sàng nặng lên cần thay đổi điều trị', 'Đợt cấp thường xuyên khi ≥ 3 đợt/năm', 'Nguy cơ đợt cấp tăng nếu bệnh nhân có tắc nghẽn đường thở nặng', 'Đợt cấp bệnh phổi tắc nghẽn mạn tính phải nhập viện có nguy cơ tử vong cao']
  line   5758 | Medium      | id b9af4d71b91f4a3fa6ab833604878509 | B -> Đợt cấp thường xuyên khi ≥ 3 đợt/năm
  line   5817 | Medium      | id 05ac9db806cc43f785d8cfbe5819ab8b | B -> Đợt cấp thường xuyên khi ≥ 3 đợt/năm

### Group 914 — topic: Pulmonology
Q: Tổn thương đường thở trung tâm ở bệnh nhân BPTNMT là:
Options (shared set): ['Là quá trình viêm mạn tính, gây tổn thương và tái tạo đường thở', 'Phá huỷ đường thở, điển hình gây khí phế thủng', 'Các tuyến tiết nhầy dưới niêm mạc to ra', 'Tiểu phế quản bị giãn ra và bị phá huỷ']
  line   5759 | Medium      | id 8410eec7063848068211dad42360e574 | C -> Các tuyến tiết nhầy dưới niêm mạc to ra
  line   5798 | Medium      | id c77a52fe96054ad7bc4dcb72975034c8 | C -> Các tuyến tiết nhầy dưới niêm mạc to ra
  line   5818 | Medium      | id 56324444dfc4475a82b44f7fb105d01e | C -> Các tuyến tiết nhầy dưới niêm mạc to ra

### Group 915 — topic: Otolaryngology, Pulmonology
Q: Thuốc lá là một trong những nguyên nhân hàng đầu gây viêm thanh quản
Options (shared set): ['Đúng', 'Sai']
  line   5772 | Easy        | id 5794270f568b4303ab7dde5629034151 | B -> Sai
  line   5778 | Easy        | id 4e9501c731bb48099e7fda588fcd4d2d | B -> Sai
  line   5785 | Easy        | id 17d5bb51ccf348f2a70bbd5d3bd6f2bb | B -> Sai

### Group 916 — topic: Otolaryngology, Pulmonology
Q: Có hội chứng xâm nhập có nghĩa là dị vật có chạm đến thanh quản đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line   5781 | Medium      | id 41428b61d6bf4221b2d0cd1a545eb9ba | A -> Đúng
  line   5789 | Medium      | id 47a3c721bc284b0a8fb035982fc3baa0 | A -> Đúng

### Group 917 — topic: Pulmonology
Q: Điều trị đợt cấp COPD mạn tính, chỉ định chuyển hồi sức tích cực khi, chọn câu SAI?
Options (shared set): ['Rối loạn ý thức', 'Oxy máu không cải thiện dù thông khí đủ', 'Cần thông khí xâm nhập kéo dài', 'Rối loạn nhịp thở']
  line   5811 | Medium      | id d5e6f3f3cf44484ab80b79faf8469b57 | D -> Rối loạn nhịp thở
  line   8131 | Challenging | id 68a13ad0d436461f9fcf957d0c161e0e | D -> Rối loạn nhịp thở

### Group 918 — topic: Pulmonology, Pathology, Oncology
Q: Trên hình ảnh vị thể từ mẫu sinh thiết của bệnh nhân nam 50 tuổi cho thấy cấu trúc nhu mô phổi bị biến đổi, các tế bào biểu mô có kích thước lớn, hạt nhân rõ, tập trung thành đám, tạo cấu trúc cầu sừng. Tổn thương nào phù hợp nhất trên bệnh nhân này?
Options (shared set): ['Ung thư biểu mô phế quản tế bào nhỏ', 'Ung thư biểu mô phế quản típ vảy biệt hóa tốt', 'Ung thư biểu mô phế quản típ vảy biệt hóa vừa', 'Ung thư biểu mô phế quản tế bào lớn']
  line   5826 | Medium      | id bcdf2e964bc14abd895abc942388b856 | B -> Ung thư biểu mô phế quản típ vảy biệt hóa tốt
  line   5833 | Medium      | id 1b681ec4d5594445ac3c5a6fefdfbaaf | B -> Ung thư biểu mô phế quản típ vảy biệt hóa tốt

### Group 919 — topic: Infectious Diseases, Orthopedics, Pulmonology, Pathology
Q: Hình ảnh vi thể viêm xương do lao điển hình không có thành phần nào:
Options (shared set): ['Hoại tử bã đậu và tế bào dạng biểu mô', 'Tế bào khổng lồ Langhans', 'Tế bào viêm lympho và tế bào sợi', 'Bạch cầu đa nhân trung tính']
  line   5853 | Medium      | id a07a6faae9b34135aee08da8fc6239fd | D -> Bạch cầu đa nhân trung tính
  line   5908 | Medium      | id 8689379d90b941bbbc2a0529276cb7a2 | D -> Bạch cầu đa nhân trung tính

### Group 920 — topic: Oncology, Pulmonology
Q: Hình ảnh dưới đây minh họa một trong các thể ung thư phổi phân chia theo hình ảnh đại thể. Đó là thể nào, chọn câu trả lời đúng nhất:
Options (shared set): ['Thể ngoại vi', 'Thể trung tâm', 'Thể lan tràn', 'Thể hỗn hợp']
  line   5869 | Medium      | id 40f195bb763e40f589014308f3afef53 | B -> Thể trung tâm
  line   5870 | Medium      | id 1826cfccfa5b40629951cae9a9b26ed6 | A -> Thể ngoại vi

### Group 921 — topic: Pulmonology, Infectious Diseases, Pathology
Q: Trong viêm lao, sự xuất hiện của các tế bào dạng biểu mô, tế bào khổng lồ Langhans là biểu hiện của hiện tượng nào trong viêm?
Options (shared set): ['Hiện tượng huy động tế bào', 'Hiện tượng biến dạng tế bào', 'Hiện tượng xuyên mạch', 'Hiện tượng tăng sinh sản tế bào']
  line   5897 | Medium      | id f040aab84d4c484793808afb5b0f9272 | B -> Hiện tượng biến dạng tế bào
  line   5915 | Medium      | id 17f658bc54da4c0aadf851cd3f7e72b4 | C -> Hiện tượng biến dạng tế bào

### Group 922 — topic: Pulmonology, Oncology, Pathology
Q: Dưới đây là hình ảnh vi thể tổ chức u phổi của bệnh nhân ung thư biểu mô tế bào nhỏ của phổi. Chọn câu trả lời đúng nhất về đặc điểm vi thể của các tế bào u của loại u này
Options (shared set): ['Các tế bào có cấu trúc tuyến, nhân lớn, tăng kiềm tính', 'Các tế bào đứng thành đám, nhân lớn, bào tương rộng', 'Các tế bào có nhân hình bầu dục, chất nhiễm sắc mịn', 'Các tế bào có cấu trúc nhú, nhân nhỏ, bào tương hẹp']
  line   5903 | Medium      | id a759d883bc0d40cdb1f72447310f565f | C -> Các tế bào có nhân hình bầu dục, chất nhiễm sắc mịn
  line  10033 | Medium      | id 07d63c10064b4a568d479edeaf7eec51 | C -> Các tế bào có nhân hình bầu dục, chất nhiễm sắc mịn

### Group 923 — topic: Endocrinology, Pulmonology, Nephrology
Q: Chất nào từ khói thuốc vào máu làm ngăn cản oxy kết hợp với máu, tăng sản xuất hồng cầu, gây tăng các biến chứng suy thận, mù mắt, hoại tử bàn chân, đột quỵ ở bệnh nhân ĐTĐ?
Options (shared set): ['Nicotine', 'Cacbon dioxide']
  line   5940 | Easy        | id 5c44ce6a693848b6a9131af85a5b461b | B -> Cacbon dioxide
  line   6204 | Medium      | id ee6292b153c444a8b9a481f8ac7dd91c | B -> Cacbon dioxide

### Group 924 — topic: Endocrinology, Pulmonology
Q: Chất nào từ khói thuốc vào máu làm co thắt các mạch máu nhỏ, làm chậm sự hấp thu của insulin, gây khó kiểm soát đường huyết ở bệnh nhân insulin?
Options (shared set): ['Cacbon dioxide', 'Nicotine']
  line   5941 | Easy        | id 2c9a4eecbce44594aa2ca5d3d5778d2b | B -> Nicotine
  line   6205 | Medium      | id 2950bac7e6b240b791580fa665ce15e2 | B -> Nicotine

### Group 925 — topic: Pulmonology, Radiology
Q: Chụp phổi trong hen thường thấy:
Options (shared set): ['Lồng ngực căng phồng', 'Khoang gian sườn giãn rộng', 'Vòm hoành hạ thấp', '2 phế trường tăng sáng']
  line   5984 | Medium      | id 6535718f6ab449778d67a008e2b16dfa | D -> 2 phế trường tăng sáng
  line   9114 | Medium      | id 07a9fce239564fcb8abc4ce7957f2694 | D -> 2 phế trường tăng sáng

### Group 926 — topic: Pediatrics, Pulmonology
Q: Trẻ < 24 tháng hen dễ nhầm nhất với:
Options (shared set): ['Viêm tiểu phế quản', 'Viêm phế quản phổi', 'Dị vật đường thở', 'Trào ngược dạ dày thực quản']
  line   5987 | Medium      | id d9d4baba0fb44f898f6f631b7ab77cb5 | A -> Viêm tiểu phế quản
  line  11760 | Medium      | id b4fcad80721b4ec59c224f22b7e1afeb | A -> Viêm tiểu phế quản

### Group 927 — topic: Pulmonology
Q: Montelukast tạo ra tác dụng dược lý nào sau đây ở BN hen phế quản?
Options (shared set): ['Giãn phế quản', 'Ức chế tăng đáp ứng phế quản', 'Ổn định tế bào mast', 'Vừa ức chế tăng đáp ứng phế quản và vừa ổn định tế bào mast']
  line   6003 | Medium      | id 848dbcc8a0204baabd8b5bc194ae1b59 | D -> Vừa ức chế tăng đáp ứng phế quản và vừa ổn định tế bào mast
  line  10027 | Medium      | id 6dd40be9eb934458b2a76880d1965148 | D -> Vừa ức chế tăng đáp ứng phế quản và vừa ổn định tế bào mast

### Group 928 — topic: Pulmonology, Radiology
Q: Chẩn đoán tràn dịch màng phổi khu trú thể trên hoành dựa vào dấu hiệu nào sau đây:
Options (shared set): ['Jose Remy.', 'Chiêu cao cơ hoành.', 'Bề dày cơ hoành.', 'A và C đều đúng.']
  line   6076 | Medium      | id ee7c5d7832ab497cb84c15e81e2ab53e | D -> A và C đều đúng.
  line   9145 | Medium      | id 5bceef51064d4674af4c190920a2d8b8 | D -> A và C đều đúng.

### Group 929 — topic: Endocrinology, Nephrology
Q: Một trong các câu sau đây liên quan đến sự cân bằng kali trong bệnh tiểu đường nhiễm ceton-acid (DKA) là đúng…
Options (shared set): ['Khoảng 20% tổng số kali cơ thể là ở mạch máu.', 'Tăng kali máu trong DKA ban đầu là phổ biến.', 'Điều trị ban đầu DKA thường gây hạ kali huyết.', 'Nồng độ kali trong huyết thanh ban đầu > 3,3 mEq / L và <5,0 mEq / L, giảm bớt sự cần thiết phải bổ sung kali.']
  line   6093 | Medium      | id 3d98af5133f94e7b8882e79e0825e4be | C -> Điều trị ban đầu DKA thường gây hạ kali huyết.
  line  11996 | Medium      | id 8f7e6e302daf476c89447b3db31ed640 | B -> Tăng kali máu trong DKA ban đầu là phổ biến.

### Group 930 — topic: Endocrinology, Rheumatology, Orthopedics
Q: Các bệnh có hình ảnh khuyết xương, trừ
Options (shared set): ['Cường giáp', 'VKDT', 'Gout', 'U xương']
  line   6103 | Medium      | id c58a54e559ad42c6a184aa35588bae1a | A -> Cường giáp
  line   6476 | Medium      | id 6c1181d1d59e4f4e81dddfdfe5a37c0d | A -> Cường giáp

### Group 931 — topic: Nephrology, Endocrinology
Q: Ở ngưỡng ADH tối đa, việc tiêm Desmopressin sẽ không làm tăng độ thẩm thấu nước tiểu (1), trừ khi sự phóng thích ADH bị suy yếu (2)
Options (shared set): ['Mệnh đề (1) đúng, (2) đúng', 'Mệnh đề (1) đúng, (2) sai', 'Mệnh đề (1) sai, (2) đúng', 'Mệnh đề (1) sai, (2) sai']
  line   6114 | Medium      | id 7ca618d567874eaaa1fdaea758e7efbd | A -> Mệnh đề (1) đúng, (2) đúng
  line   6149 | Medium      | id f70f1c17d7d04c35845e5e6ce4ebcfaa | A -> Mệnh đề (1) đúng, (2) đúng

### Group 932 — topic: Endocrinology, Nephrology
Q: Nguyên nhân hạ đường huyết ở những bệnh nhân không uống thuốc đái tháo đường( chọn câu sai)?
Options (shared set): ['Suy gan nặng', 'Suy thận mạn', 'Suy thượng thận', 'Suy giáp']
  line   6120 | Medium      | id 4ecf3fa09a7944c19285745c008df79b | B -> Suy thận mạn
  line   6756 | Medium      | id 4c418ce223cc4654ad3f191b8becf65f | B -> Suy thận mạn
  line   7123 | Medium      | id e1152bec74574a978040924de08d01c0 | B -> Suy thận mạn

### Group 933 — topic: Endocrinology
Q: Chọn câu đúng:
Options (shared set): ['Hydroxylase đóng vai trò trong tổng hợp các hormon peptid', 'Multienzym là tập hợp của nhiều enzym xúc tác phản ứng oxy hóa khử', 'Sự tổng hợp acid béo được xúc tác bởi phức hợp enzym có tên là Acid béo syntetase', 'Các cytocrom được hòa tan trong bào tương tế bào']
  line   6140 | Medium      | id e18d2597d4fb447885058067499e89ee | C -> Sự tổng hợp acid béo được xúc tác bởi phức hợp enzym có tên là Acid béo syntetase
  line   7001 | Medium      | id ac3d93802564442983a336cfe23712ee | C -> Sự tổng hợp acid béo được xúc tác bởi phức hợp enzym có tên là Acid béo syntetase
  line   7002 | Medium      | id 56438e33bdf6489fa2c197ca206086e2 | C -> Sự tổng hợp acid béo được xúc tác bởi phức hợp enzym có tên là Acid béo syntetase

### Group 934 — topic: Oncology, Endocrinology, Pathology
Q: 51. Hình ảnh vi thể của ung thư biểu mô tuyến giáp không biệt hóa gồm, trừ một?
Options (shared set): ['Tế bào u đa dạng', 'Tế bào nhiểu nhân quái, nhân chia', 'Tế bào khổng lồ nhiều nhân', 'Tế bào khổng lồ nhiều nhân Langhans']
  line   6153 | Medium      | id b57cfb0655f4415c92aa6b17899e99cf | D -> Tế bào khổng lồ nhiều nhân Langhans
  line  10151 | Medium      | id 7de3131fa1fd4adf87ff6aefa7954b75 | D -> Tế bào khổng lồ nhiều nhân Langhans

### Group 935 — topic: Endocrinology
Q: Bệnh lý tăng tiết GH người trưởng thành thường xuất hiện muộn và khó chẩn đoán?
Options (shared set): ['Đúng', 'Sai']
  line   6157 | Medium      | id 047823eec713493ea18716b715d247a4 | A -> Đúng
  line   7386 | Challenging | id aebbeb9565a64a70a5cb13425ee4a2fb | A -> Đúng

### Group 936 — topic: Nephrology, Endocrinology
Q: Nhóm bệnh nào sau đây làm tăng số lượng nước tiểu đào thải?
Options (shared set): ['Tiểu đường, suy tim', 'Tiểu đường, các bệnh thận', 'Tiểu đường, thiếu ADH', 'Suy tim, bệnh của ống thận']
  line   6166 | Medium      | id 028355e31e524fa3a4880c167ea4df3a | C -> Tiểu đường, thiếu ADH
  line   6171 | Medium      | id 5cd5bf5531b54cb39a9a264549abe3cf | C -> Tiểu đường, thiếu ADH

### Group 937 — topic: Endocrinology
Q: Hiện tượng glycosyl hóa liên quan đến:
Options (shared set): ['HbA1C', 'GOT', 'GPT', 'HDL']
  line   6234 | Easy        | id 18880fdaf92a4366a7c316caec5fdf7c | A -> HbA1C
  line   6261 | Easy        | id 5f28a20d9bc540979ee6be3808921348 | A -> HbA1C

### Group 938 — topic: Endocrinology, Obstetrics and Gynecology
Q: Tác dụng của estrogen trên tuyến vú:Phát triển mô đệm và lớp mỡ.
Options (shared set): ['Đúng', 'Sai']
  line   6240 | Easy        | id 6d56c25f5f6743c7b2452a75453886c8 | A -> Đúng
  line   8697 | Medium      | id cd85f0c195ba4391b5169541e94c68dd | A -> Đúng

### Group 939 — topic: Endocrinology, Obstetrics and Gynecology
Q: Estrogen là một steroid có:
Options (shared set): ['17 carbon.', '18 carbon.', '19 carbon.', '21 carbon.']
  line   6253 | Easy        | id 1a5ddcb9956b4ba6bb57dd6d1db03886 | B -> 18 carbon.
  line   6278 | Easy        | id f38c40cbda3b4d3eb1e8d1c9c86de71d | B -> 18 carbon.

### Group 940 — topic: Endocrinology, Obstetrics and Gynecology
Q: Bản chất hoá học của progesteron là steroid có:
Options (shared set): ['17 carbon.', '18 carbon.', '19 carbon.', '21 carbon.']
  line   6254 | Easy        | id a2d77fcbe04340a1a0fdbccdad3dab51 | D -> 21 carbon.
  line   6279 | Easy        | id ea91a214249b46f1b9c7e9d9a100009f | D -> 21 carbon.

### Group 941 — topic: Endocrinology, Internal Medicine
Q: TG, Photpholipid, Cholesterol, Cholester rol este, protein <br /> Số các thành phần tham gia vào cấu tạo hạt vận chuyển Lipid ( Lipoprotein) là
Options (shared set): ['5', '4', '3', '2']
  line   6256 | Easy        | id 7ada39c1051740bf8ec973276be4b1e9 | A -> 5
  line  10987 | Easy        | id 9263338a698d475592b25868c676321b | A -> 5

### Group 942 — topic: Endocrinology, Obstetrics and Gynecology
Q: Ở người phụ nữ bình thường, nơi bài tiết progesteron chủ yếu là:
Options (shared set): ['Nang noãn.', 'Hoàng thể.', 'Rau thai.', 'Vỏ thượng thận.']
  line   6280 | Easy        | id 751902ef00e04946a12a9ffdc87bd498 | B -> Hoàng thể.
  line   6575 | Medium      | id 2025aeef2940434eaa64ab03ce7a6d6f | B -> Hoàng thể.

### Group 943 — topic: Endocrinology, Internal Medicine
Q: Hạ đường huyết là đường huyết dưới ngưỡng nào?
Options (shared set): ['3.0mmol/L', '3.9mmol/L', '5.0mmol/L', '2.8mmol/L']
  line   6294 | Easy        | id c76abe9dda9e45b895c726456d67eb7b | B -> 3.9mmol/L
  line   6371 | Easy        | id ed306bdc86d9438ba8f812b880a47d85 | B -> 3.9mmol/L

### Group 944 — topic: Endocrinology, Internal Medicine
Q: Hạ đường huyết thông thường là đường huyết dưới ngưỡng:
Options (shared set): ['5 mmol/l', '3,9 mmol/l', '3.0 mmol/l', '2,8 mmol/l']
  line   6295 | Easy        | id 2c038b5acfdc4b43b3cefc7bff78b8f1 | B -> 3,9 mmol/l
  line   6298 | Easy        | id 78c1053a60b4402f85f1ba5ee578731f | B -> 3,9 mmol/l

### Group 945 — topic: Endocrinology
Q: Tuyến giáp là tuyến nội tiết, cấu trúc mô học gồm các nang tuyến, xen kẽ là hệ thống các ống dẫn để dẫn các chất bài xuất của tuyến ra ngoài?
Options (shared set): ['Đúng', 'Sai']
  line   6327 | Easy        | id 2e23e4bbc87440bb967c05dffd64c41b | B -> Sai
  line   8987 | Easy        | id 7bc38740407a47549850d2e42727aeb3 | B -> Sai

### Group 946 — topic: Endocrinology
Q: Bản chất của hormon là những
Options (shared set): ['Protein hoặc peptid', 'Dẫn xuất của acid amin', 'Steroid', 'Cả 3 đáp án trên']
  line   6345 | Easy        | id 13c126d8bcbb464da3ac9ce863cd5d19 | D -> Cả 3 đáp án trên
  line   6352 | Easy        | id 8562d460e2914d8289e58e0476cc961c | D -> Cả 3 đáp án trên

### Group 947 — topic: Endocrinology
Q: Các hormon vỏ thượng thận thuộc nhóm
Options (shared set): ['Protein và peptid', 'Steroid', 'Acid amin', 'Dẫn xuất của acid amin']
  line   6347 | Easy        | id b904b896cb20489ca8a281bc898e7daf | B -> Steroid
  line   6354 | Easy        | id a596938f86a3423283b43e7e7a3c5156 | B -> Steroid

### Group 948 — topic: Endocrinology
Q: Các hormon tuyến giáp thuộc nhóm
Options (shared set): ['Protein và peptid', 'Steroid', 'Dẫn xuất của phenylalanin', 'Dẫn xuất của tyrosin']
  line   6348 | Easy        | id e8ba65b0d234406ab54ff30642233c5c | D -> Dẫn xuất của tyrosin
  line   6355 | Easy        | id 8b8521c4772947678a1efa9ca55343e8 | D -> Dẫn xuất của tyrosin

### Group 949 — topic: Endocrinology
Q: Triệu chứng lâm sàng của bệnh Basedow là gì?
Options (shared set): ['Run tay chân.', 'Gầy sút nhanh.', 'Ăn ít, tiểu ít.', 'Trầm cảm.']
  line   6382 | Medium      | id 94de36418cf24398a77c6054b47736d6 | B -> Gầy sút nhanh.
  line   8903 | Challenging | id acf18c67460f4738a76d63473ea6d4d8 | B -> Gầy sút nhanh.

### Group 950 — topic: Nephrology, Endocrinology
Q: Chọn câu sai. Tăng natri máu gặp trong tình trạng nào
Options (shared set): ['Thuốc lợi tiểu Thiazid', 'Tình trạng mất nước', 'Đái tháo nhạt', 'Tăng aldosteron tiên phát']
  line   6388 | Medium      | id 99b9bca47d8a45eabd39883c9be5606d | A -> Thuốc lợi tiểu Thiazid
  line   7938 | Medium      | id 082f5c874d24486b807a5f532f6ed349 | A -> Thuốc lợi tiểu Thiazid

### Group 951 — topic: Nephrology, Endocrinology
Q: Ảnh hưởng của nhiễm kiềm với nồng độ các chất hòa tan là:
Options (shared set): ['Tăng kali huyết', 'Hạ natri máu', 'Hạ kali máu', 'Bình thường']
  line   6405 | Medium      | id 2ad8f150cbdf4818911c8ba60b28c7c2 | C -> Hạ kali máu
  line   6463 | Medium      | id 2798dd30afc448aba4845a3b5eca7f47 | C -> Hạ kali máu.

### Group 952 — topic: Endocrinology, Oncology
Q: Một trong những nguyên nhân gây ra ung thư tuyến giáp là
Options (shared set): ['Virut', 'Hoá chất', 'Gen', 'Tia xạ']
  line   6409 | Medium      | id 8849c4b4d73344989fae661c1b146613 | D -> Tia xạ
  line   8418 | Medium      | id 615704a2a79b47678acd91e803e73e5b | D -> Tia xạ

### Group 953 — topic: Endocrinology
Q: Ý nghĩa tốt nhất cho từ được gạch chân là gì? 'Cường giáp' thường liên quan đến việc kiểm soát đường huyết kém đi và tăng nhu cầu insulin.
Options (shared set): ['chức năng tuyến giáp bình thường', 'chức năng tuyến giáp quá cao', 'một lượng chất béo bất thường trong máu', 'liên quan đến lượng đường trong máu']
  line   6437 | Medium      | id b98e35a36e874b3b8cc6131833be5f80 | B -> chức năng tuyến giáp quá cao
  line   6438 | Medium      | id 90f27d2f9fdb4a7d929ade53df033e85 | D -> liên quan đến lượng đường trong máu

### Group 954 — topic: Ophthalmology, Endocrinology
Q: Khi bệnh nhân có bệnh võng mạc đái tháo đường cần làm xét nghiệm nào:
Options (shared set): ['chụp mạch võng mạc huỳnh quang', 'siêu âm dịch kính võng mạc', 'doppler động mạch mắt', 'sắc giác']
  line   6472 | Medium      | id 9dfc4ccd61584e8dbf17f5afb0d70bbb | A -> chụp mạch võng mạc huỳnh quang
  line  11593 | Medium      | id f0f3136ad6324d1bac2eb808f4beb7bd | A -> Chụp mạch võng mạc huỳnh quang

### Group 955 — topic: Ophthalmology, Endocrinology
Q: Bệnh mắt do cường năng tuyến giáp gồm có:
Options (shared set): ['loét giác mạc nếu lồi mắt quá nhiều', 'bệnh lý thị thần kinh do chèn ép', 'lồi mắt, co rút mi trên', 'tất cả các trường hợp trên']
  line   6474 | Medium      | id a00a46bd14364d3cb06fbc7ced17b8c8 | D -> tất cả các trường hợp trên
  line  11627 | Easy        | id b61d041311114c98bfb56b41f50f78db | D -> tất cả các trường hợp trên

### Group 956 — topic: Orthopedics, Endocrinology
Q: Trường hợp không phải gãy xương tự nhiên:
Options (shared set): ['Loãng xương', 'K xương', 'Suy tuyến thượng thận', 'U tuỷ xương']
  line   6477 | Medium      | id f05a86b602e34c5ca729e24335d431c0 | C -> Suy tuyến thượng thận
  line   6541 | Medium      | id 34dc360aa38748e9b9113cb0439705a2 | C -> Suy tuyến thượng thận

### Group 957 — topic: Endocrinology, Orthopedics
Q: Bệnh có sưng không viêm trừ:
Options (shared set): ['Suy giáp', 'Suy tuyến yên', 'Di chứng hư khớp', 'A và B']
  line   6478 | Medium      | id 42f6d4e596bd42a981d0aa605c63b62b | D -> A và B
  line   6542 | Medium      | id 31203aa52b084950a371d8d17944ff79 | D -> A và B

### Group 958 — topic: Endocrinology, Geriatrics
Q: Loãng xương lan toả không phải bệnh hệ thống?
Options (shared set): ['Đ', 'S']
  line   6479 | Medium      | id 85f7db3f56bd43f88ba3696dfa3f830b | B -> S
  line   6543 | Medium      | id 8c63954867a945c2a91868a88856ada4 | B -> S
  line  10820 | Medium      | id 1df5efd403864273ab0eb64827a25263 | B -> S

### Group 959 — topic: Pediatrics, Endocrinology
Q: Chân hình chữ X hoặc chữ O ở trẻ em do?
Options (shared set): ['Thiếu Vitamin PP', 'Thiếu Vitamin D', 'Thiếu Vitamin C', 'Thiếu Vitamin K']
  line   6480 | Medium      | id 3380dafb256948edb00cd3868e12fad4 | B -> Thiếu Vitamin D
  line   6544 | Medium      | id eac2f496773748c38a5cadd4b282209c | B -> Thiếu Vitamin D

### Group 960 — topic: Radiology, Orthopedics, Endocrinology
Q: Biểu hiện loãng xương trên phim chụp XQ?
Options (shared set): ['Hình ảnh kính', 'Vỏ xương dày', 'Thớ xương dày', 'Mật độ xương tăng']
  line   6481 | Medium      | id 5d60f50447654af0a0e5a065f357294d | A -> Hình ảnh kính
  line   6545 | Medium      | id 22d56d5f71ea4e2fa31ea581a4d1bfbf | A -> Hình ảnh kính

### Group 961 — topic: Endocrinology, Neurology
Q: Hội chứng co cơ giảm Ca2+ máu là:
Options (shared set): ['Tetani', 'Động kinh', 'Ngộ độc Schychnos', 'Uốn ván']
  line   6482 | Medium      | id 4744624cd88a460bb1667872fc9d3f0f | A -> Tetani
  line   6546 | Medium      | id 2f5c63cf65284f49935813b0dab31000 | A -> Tetani

### Group 962 — topic: Endocrinology, Obstetrics and Gynecology
Q: Hormon có tác dụng kích thích trực tiếp bài tiết estrogen trong chu kỳ kinh nguyệt là:
Options (shared set): ['FSH.', 'LH.', 'HCG.', 'GnRH.']
  line   6563 | Medium      | id ac5ce762d6874ee0b1425569d85c1e41 | B -> LH.
  line   6717 | Medium      | id c9d816af7283462fabb40cd103ec4b37 | B -> LH.

### Group 963 — topic: Endocrinology, Obstetrics and Gynecology
Q: Trong chu kỳ kinh nguyệt hormon trực tiếp kích thích bài tiết progesteron là:
Options (shared set): ['GnRH.', 'HCG.', 'FSH.', 'LH.']
  line   6564 | Medium      | id af42d73e7f1540008688c9f15e900153 | D -> LH.
  line   6720 | Medium      | id 35f2e8972d4b4c7583cdb73594c6f43c | D -> LH.

### Group 964 — topic: Endocrinology, Obstetrics and Gynecology
Q: Sau đây là các tác dụng của estrogen lên cơ tử cung, trừ:
Options (shared set): ['Tăng co bóp cơ tử cung.', 'Tăng hàm lượng actomyosin ở cơ tử cung.', 'Tăng lưu lượng máu đến cơ tử cung.', 'Giảm tính nhậy cảm của cơ tử cung với oxytocin.']
  line   6566 | Medium      | id 750469ab185f40a1bc79cfd53951506d | D -> Giảm tính nhậy cảm của cơ tử cung với oxytocin.
  line   6712 | Medium      | id f2f5d60d42694eafa2e12a4f6284c4c3 | D -> Giảm tính nhậy cảm của cơ tử cung với oxytocin.

### Group 965 — topic: Endocrinology, Obstetrics and Gynecology
Q: Tác dụng của progesteron lên cổ tử cung:
Options (shared set): ['Tăng bài tiết dịch nhày loãng, mỏng.', 'Tăng bài tiết dịch nhày kiềm.', 'Tăng bài tiết dịch nhày quánh.', 'Tăng bài tiết dịch nhày quánh, dày.']
  line   6567 | Medium      | id 03bbd46794c34ab4b13f6554a8d315c7 | D -> Tăng bài tiết dịch nhày quánh, dày.
  line   6719 | Medium      | id ee8c4f1e2858409f9be4f746ed1feefe | D -> Tăng bài tiết dịch nhày quánh, dày.

### Group 966 — topic: Endocrinology, Obstetrics and Gynecology
Q: Tác dụng của estrogen lên chuyển hoá protein là:
Options (shared set): ['Tăng tổng hợp DNA ở các mô của cơ thể.', 'Tăng quá trình sao chép RNAm ở các mô của cơ thể.', 'Tăng tổng hợp protein ở các mô của cơ thể.', 'Tăng tổng hợp protein ở một số cơ quan đích.']
  line   6568 | Medium      | id 1d4504e5725a440ca8f38b3a420201f7 | D -> Tăng tổng hợp protein ở một số cơ quan đích.
  line   6710 | Medium      | id 105a30cb86ba48dfb54e7c5889f1dec7 | D -> Tăng tổng hợp protein ở một số cơ quan đích.

### Group 967 — topic: Endocrinology, Obstetrics and Gynecology
Q: Tác dụng của estrogen trên xương là:
Options (shared set): ['Tăng hoạt tính của huỷ cốt bào.', 'Tăng hoạt tính của tạo cốt bào.', 'Tăng nồng độ ion Ca++ trong máu.', 'Tăng hấp thu ion Ca++ ở ruột.']
  line   6569 | Medium      | id 132097ae4fed4a2891c27a6788881c50 | B -> Tăng hoạt tính của tạo cốt bào.
  line   6713 | Medium      | id e4935184fb924912934235ce99a16e81 | B -> Tăng hoạt tính của tạo cốt bào.

### Group 968 — topic: Endocrinology, Obstetrics and Gynecology
Q: Estrogen làm phát triển cơ quan sinh dục từ:
Options (shared set): ['Thời kỳ bào thai.', 'Sau khi sinh đến tuổi trưởng thành.', 'Tuổi dậy thì đến mãn kinh.', 'Tuổi dậy thì và khi có thai.']
  line   6570 | Medium      | id 7364649d749b4a818c976efc2e24dfb1 | C -> Tuổi dậy thì đến mãn kinh.
  line   6711 | Medium      | id 4abcc7d0b9f44c56b969bb07c0f4e473 | C -> Tuổi dậy thì đến mãn kinh.

### Group 969 — topic: Endocrinology, Obstetrics and Gynecology
Q: Tác dụng của estrogen lên tuyến cổ tử cung làm tăng bài tiết:
Options (shared set): ['Dịch nhày kiềm.', 'Dịch nhày loãng, mỏng.', 'Dịch nhày quánh, kiềm.', 'Dịch nhày loãng, kiềm.']
  line   6571 | Medium      | id 1eeff47ead10426998d56518a6706257 | B -> Dịch nhày loãng, mỏng.
  line   6714 | Medium      | id 1ded77d992f14b7f912fa85f98720eb4 | C -> Dịch nhày quánh, kiềm.

### Group 970 — topic: Endocrinology, Obstetrics and Gynecology
Q: Receptor tiếp nhận estrogen nằm ở:
Options (shared set): ['Trên màng tế bào đích.', 'Trong bào tương.', 'Trên màng nhân.', 'Trên chuỗi DNA.']
  line   6572 | Medium      | id 4b0a6e0e41f545f09f039db296da4833 | B -> Trong bào tương.
  line   6715 | Medium      | id 8751d5ba725f42aa9b94a2f863a563e3 | B -> Trong bào tương.

### Group 971 — topic: Endocrinology, Obstetrics and Gynecology
Q: Cơ chế tác dụng của estrogen tại tế bào đích là:
Options (shared set): ['Hoạt hoá adenylcyclase.', 'Hoạt hoá phospholipase C.', 'Hoạt hoá kênh Ca++.', 'Hoạt hoá sao chép RNAm.']
  line   6573 | Medium      | id 72a9090bc9e94f92a131e9bd2d386551 | D -> Hoạt hoá sao chép RNAm.
  line   6716 | Medium      | id 116914b3548c4278899822ce822c8cc0 | D -> Hoạt hoá sao chép RNAm.

### Group 972 — topic: Endocrinology, Obstetrics and Gynecology
Q: Progesteron có các tác dụng sau đây, trừ:
Options (shared set): ['Tăng thoái hoá protein.', 'Tăng thân nhiệt.', 'Tăng tổng hợp lipid.', 'Tăng tái hấp thu ion Na+ ở ống lượn xa khi nồng độ cao.']
  line   6574 | Medium      | id 1e5e47ef1a5742baa08c17e17b463634 | C -> Tăng tổng hợp lipid.
  line   6718 | Medium      | id 8e155cab17b04241984d30ee1ff5aec2 | C -> Tăng tổng hợp lipid.
  line   8617 | Easy        | id 5890fe4d054548b69c2cf422174774a7 | C -> Tăng tổng hợp lipid.

### Group 973 — topic: Endocrinology, Nephrology
Q: Đường huyết tăng và bài xuất ra nước tiểu trong:
Options (shared set): ['Ưu năng tuyến giáp.', 'Teo tiểu đảo Langerhans.', 'U tuyến tuỵ nội tiết.', 'U tuỷ thượng thận.']
  line   6578 | Medium      | id 41b8e0077e574458ac3c39148ec05b78 | B -> Teo tiểu đảo Langerhans.
  line   6698 | Medium      | id 2ee07888d80945b69e976232e40d875f | B -> Teo tiểu đảo Langerhans.

### Group 974 — topic: Endocrinology
Q: Tác dụng của T3-T4 làm tăng:
Options (shared set): ['Kích thước tuyến giáp.', 'Thời gian phản xạ gân xương.', 'Thoái hoá lipid.', 'AMP vòng ở tế bào đích.']
  line   6580 | Medium      | id 9f9435c90f8d4de691a52392329c79bd | C -> Thoái hoá lipid.
  line   6680 | Medium      | id c01905ae7b394a06807b671986bb1e85 | C -> Thoái hoá lipid.

### Group 975 — topic: Endocrinology
Q: Các yếu tố sau đây đều làm tăng bài tiết T3-T4, trừ:
Options (shared set): ['Nồng độ iod vô cơ trong tuyến giáp cao.', 'Nồng độ TSH trong máu cao.', 'Nồng độ iod hữu cơ trong máu giảm.', 'Khi bị lạnh hoặc stress.']
  line   6581 | Medium      | id c06671caa0a64e9c867ec75555bfb2cb | A -> Nồng độ iod vô cơ trong tuyến giáp cao.
  line   6681 | Medium      | id 7a89afcdd2b642e98137415abe523d49 | C -> Nồng độ iod hữu cơ trong máu giảm.

### Group 976 — topic: Endocrinology
Q: Tác dụng của T3 - T4:
Options (shared set): ['Làm phát triển sụn liên hợp.', 'Làm tăng tổng hợp ATP.', 'Làm tăng AMP vòng tại tế bào đích.', 'Làm tăng tốc độ phản ứng hoá học ở các tế bào.']
  line   6582 | Medium      | id 53b6409c9a274b868e4248ff69b06c7c | D -> Làm tăng tốc độ phản ứng hoá học ở các tế bào.
  line   6682 | Medium      | id 42418a719c4545c8b27eca8a4590eafb | D -> Làm tăng tốc độ phản ứng hoá học ở các tế bào.
  line   8701 | Medium      | id c85840c664cb44d89057c06875cf6ba8 | D -> Làm tăng tốc độ phản ứng hoá học ở các tế bào.

### Group 977 — topic: Endocrinology, Internal Medicine
Q: Cholesterrol được tổng hợp chủ yếu ở gan, ruột, ngoài ra là ở thượng thận, tinh hoàn, buồng trứng qua 4 giai đoạn, Nguyên liệu đầu tiên là
Options (shared set): ['AcetylcoA', 'Mevalovic', 'Squalen', 'Steroid']
  line   6596 | Medium      | id dc0e40ef358d4d029dae913e528cd0e0 | A -> AcetylcoA
  line  10935 | Medium      | id 7e3ce3c97b7b4b9a93c46f3ead566310 | A -> AcetylcoA

### Group 978 — topic: Nephrology, Endocrinology
Q: 3.74. Trong thí nghiệm về hiện tượng thẩm thấu, nếu nồng độ nước đường trong ống nhỏ hơn trong chậu thì mực nước đường trong ống sẽ cao hơn trong chậu. (Đúng/Sai)
Options (shared set): ['Đúng', 'Sai']
  line   6645 | Medium      | id a8d408dd91fb4b328a11581979a412a5 | B -> Sai
  line  12053 | Medium      | id 51adc5720299461e86a59b4ec8792f7e | A -> Đúng

### Group 979 — topic: Endocrinology, Obstetrics and Gynecology
Q: Tác dụng của FSH trên nữ giới:
Options (shared set): ['Kích thích noãn nang phát triển.', 'Kích thích sản xuất estrogen.', 'Kích thích sản xuất progesteron.', 'Kích thích tạo hoàng thể.']
  line   6670 | Medium      | id fb607a2553584c9380a13347d3086a43 | A -> Kích thích noãn nang phát triển.
  line   8699 | Medium      | id 37c69a23dbfc4a1a8e6a39c4aa7dc5d0 | A -> Kích thích noãn nang phát triển.

### Group 980 — topic: Endocrinology, Internal Medicine
Q: Cortisol làm tăng đường huyết chủ yếu nhờ tác dụng:
Options (shared set): ['Tăng tạo đường mới ở gan.', 'Giảm thoái hoá glucose ở mô.', 'Tăng phân giải glycogen thành glucose ở gan.', 'Tăng hấp thu glucose ở ruột.']
  line   6684 | Medium      | id 1e08ac2daf594c508a061a101870908e | A -> Tăng tạo đường mới ở gan.
  line  10977 | Medium      | id bf61c669fa174caa890a064800a5cc86 | A -> Tăng tạo đường mới ở gan.

### Group 981 — topic: Endocrinology, Obstetrics and Gynecology
Q: Tinh hoàn hoạt động từ:
Options (shared set): ['Thời kỳ bào thai cho đến hết đời.', 'Sau khi sinh cho đến hết đời.', 'Tuổi dậy thì cho đến hết đời.', 'Thời kỳ bào thai và tuổi dậy thì cho đến hết đời.']
  line   6705 | Medium      | id 84891f16c35a4a04aaadae79b4731df3 | D -> Thời kỳ bào thai và tuổi dậy thì cho đến hết đời.
  line   8873 | Easy        | id a3651425c991423282056b8b83068e83 | D -> Thời kỳ bào thai và tuổi dậy thì cho đến hết đời.

### Group 982 — topic: Endocrinology, Pathology
Q: Không bào hấp thụ hay gặp trong bệnh tuyến giáp
Options (shared set): ['Ung thư típ nhú', 'Bệnh Basedow', 'Bướu keo tuyến giáp giai đoạn tạo nốt', 'Viêm tuyến giáp']
  line   6736 | Medium      | id bd87c9f5d1934d3fb012cf68f187593f | B -> Bệnh Basedow
  line   6901 | Medium      | id 93dd1b54d0ec4c6e9e0216a433a7a891 | B -> Bệnh Basedow

### Group 983 — topic: Endocrinology, Oncology
Q: Ung thư tuyến giáp thường gặp:
Options (shared set): ['Nhiễm độc giáp', 'Ở nam giới', 'Tế bào nang tuyến typ nang', 'Bướu giáp bình giáp']
  line   6737 | Medium      | id 91df96b3271c425e913ffe0546bb7676 | D -> Bướu giáp bình giáp
  line   6902 | Medium      | id 35b3d1228ca549dbb564620840507fa1 | D -> Bướu giáp bình giáp

### Group 984 — topic: Endocrinology
Q: Basedow thuộc nhóm bệnh nào của tuyến giáp sau đây?
Options (shared set): ['Bình giáp, lan tỏa', 'Suy giáp, lan tỏa', 'Cường giáp, giả u', 'Cường giáp, giả nốt']
  line   6738 | Medium      | id 0555c36aff314277ad909dc04d12ec50 | C -> Cường giáp, giả u
  line   6903 | Medium      | id 32f877a2ba7c4889a58b04c53a707f4e | C -> Cường giáp, giả u

### Group 985 — topic: Endocrinology, Oncology
Q: Chọn ý đúng nhất cho Ung thư tuyến giáp thể nhú?
Options (shared set): ['Chiếm > 75% ung thư tuyến giáp', 'Tiên lượng nhìn chung không tốt', 'Thuộc nhóm bình giáp, dạng nốt, tiên lượng nhìn chung xấu', 'Thường gặp nhóm cường giáp']
  line   6739 | Medium      | id 665d1d4960814510b84dd1d1516930c4 | A -> Chiếm > 75% ung thư tuyến giáp
  line   7140 | Medium      | id 7c8fe32ad92a48799548f201127d2104 | A -> Chiểm > 75% ung thư tuyến giáp
  line   7141 | Medium      | id f97777b11be2458aa169dda8fab38099 | A -> Chiếm > 75% ung thư tuyến giáp

### Group 986 — topic: Endocrinology, Internal Medicine
Q: Hạ đường huyết không nhận biết xảy ra thường xuyên ở những bệnh nhân nào?
Options (shared set): ['Đái tháo đường lâu năm', 'Thường xuyên có nhiều đợt đường huyết thấp', 'Dùng thuốc ức chế beta', 'Tất cả đều đúng']
  line   6757 | Medium      | id 246bc21ac317452f8c3a549f6b5aba7f | D -> Tất cả đều đúng
  line   7124 | Medium      | id c0bf9dbc92e24fbe84b85cd4d34e5f33 | D -> Tất cả đều đúng
  line   7563 | Challenging | id ec80f0706c984587ab679a60afac958b | D -> Tất cả đều đúng

### Group 987 — topic: Endocrinology, Nephrology
Q: Nguyên nhân gây hạ đường huyết ở bệnh nhân không dùng thuốc tiểu đường:
Options (shared set): ['Suy giáp', 'Suy thượng thận', 'Suy gan nặng', 'Bệnh thận mạn']
  line   6758 | Medium      | id 7201d60966864ff7a23a9bdddd23aa36 | D -> Bệnh thận mạn
  line   6760 | Medium      | id df3426bc7eb0467690a76ee3e30b86da | D -> Bệnh thận mạn

### Group 988 — topic: Endocrinology, Internal Medicine
Q: Tác dụng phụ của thuốc kháng giáp, ngoại trừ:
Options (shared set): ['Rối loạn tiêu hoá', 'Vàng da, tắc mật, viêm gan', 'Tăng BC trung tính', 'Phát ban, nổi mề đay']
  line   6763 | Medium      | id 876b1d4929694d41ba787b55ee63c07a | C -> Tăng BC trung tính
  line   7126 | Medium      | id 3fcaefcae2a6417cac68acc65c9787e7 | C -> Tăng BC trung tính

### Group 989 — topic: Endocrinology, Nephrology
Q: Các giai đoạn của bệnh thận ĐTĐ theo Mogensen
Options (shared set): ['Có 4 giai đoạn', 'GĐ 1: Thận tăng mức lọc cầu thận', 'GĐ 2: Xuất hiện protein niệu', 'GĐ 3: Xuất hiện tăng huyết áp, suy thận']
  line   6765 | Medium      | id cea849ae5102491584be8a8823780823 | B -> GĐ 1: Thận tăng mức lọc cầu thận
  line   7125 | Medium      | id 7dc40609620142f3be6d27bd40bab5c4 | B -> GĐ 1: Thận tăng mức lọc cầu thận

### Group 990 — topic: Nephrology, Endocrinology
Q: Hạ Na máu kèm theo ứ muối và ứ nước toàn thể hạ Na máu do uống quá nhiều nước dùng gì?
Options (shared set): ['Demeclocycin.', 'Carbamazepin.', 'Furosemid.', 'Phenothiazin.']
  line   6769 | Medium      | id a028e874f7c448038e0d6b3d5c7cad70 | C -> Furosemid.
  line  12014 | Medium      | id e5ee51a1701f4a3c83986fd30b14d897 | A -> Demeclocycin.

### Group 991 — topic: Endocrinology
Q: Phát biểu nào sau đây về định nghĩa đái tháo đường là KHÔNG ĐÚNG
Options (shared set): ['Là một bệnh lý chuyển hóa, có cơ chế bệnh sinh phức tạp,', 'Đặc trưng bởi tăng đường huyết cấp tính,', 'Kèm theo các tình trạng rối loạn chuyển hóa G, L, P', 'Do các tình trạng khiếm khuyết tiết insulin, hoạt tính insulin, hoặc cả hai']
  line   6791 | Medium      | id 1d58c1219c844ab8bde96bb7541db906 | B -> Đặc trưng bởi tăng đường huyết cấp tính,
  line   6799 | Medium      | id bcabf7254de040fca5c5758b2f6c6f29 | B -> Đặc trưng bởi tăng đường huyết cấp tính

### Group 992 — topic: Endocrinology, Geriatrics
Q: Phát biểu đúng về lão hóa hệ nội tiết
Options (shared set): ['Chuyển hóa mỗi năm giảm 1% sau tuổi 30', 'Renin huyết thanh giảm nhưng không làm tăng Angiotensin II', 'Giảm đường huyết 2 giờ sau ăn nhanh hơn do giảm hấp thu và tăng thải glucose qua ống thận', 'A và C']
  line   6826 | Medium      | id d88ee9d97af745c689352e0e69d9aa7d | C -> Giảm đường huyết 2 giờ sau ăn nhanh hơn do giảm hấp thu và tăng thải glucose qua ống thận
  line  10808 | Medium      | id b5a90783bdd54780b7fdc2f49a70fd0b | C -> Giảm đường huyết 2 giờ sau ăn nhanh hơn do giảm hấp thu và tăng thải glucose qua ống thận

### Group 993 — topic: Endocrinology, Radiology, Nuclear Medicine
Q: Để thăm dò hình thái của tuyến nội tiết thường dựa vào, trừ?
Options (shared set): ['Chụp phóng xạ', 'Siêu âm', 'Khám lâm sàng', 'X Quang']
  line   6842 | Medium      | id cd635edcc7334a0eb8e0d44b41984313 | A -> Chụp phóng xạ
  line   8115 | Medium      | id 7a224da7fa374709b055f66289b56f56 | B -> Siêu âm

### Group 994 — topic: Endocrinology
Q: Nói về hoocmon ACTH tuyến yên câu nào đúng
Options (shared set): ['Kích thích tủy thượng thận tăng tiết cortisol', 'Bài tiết nhiều về ban đêm', 'Không bị ảnh hưởng bởi hóc môn vùng Hạ đồi', 'Điều hòa bài tiết do cơ chế điều hòa ngược (- ) và cả điều hòa ngược (+)']
  line   6862 | Medium      | id 1b02174d417441e6b867662467e38e22 | D -> Điều hòa bài tiết do cơ chế điều hòa ngược (- ) và cả điều hòa ngược (+)
  line   8546 | Medium      | id 4f44df5f96764d00beaf9d415165aa71 | D -> Điều hòa bài tiết do cơ chế điều hòa ngược (- ) và cả điều hòa ngược (+)

### Group 995 — topic: Endocrinology, Obstetrics and Gynecology
Q: Nói về hoóc môn prolactin của tuyến yên câu nào đúng
Options (shared set): ['Chỉ có ở người nữ', 'Làm tăng bài xuất sữa', 'Có tác dụng ức chế sự rụng trứng', 'Tăng 10 đến 20 lần khi bắt đầu có thai']
  line   6869 | Medium      | id 67f0d3d558be47d7bbbaee572b707cca | C -> Có tác dụng ức chế sự rụng trứng
  line   8545 | Medium      | id 4a581b94fc804820a5d8ae56fb681ce6 | C -> Có tác dụng ức chế sự rụng trứng

### Group 996 — topic: Endocrinology, Obstetrics and Gynecology
Q: HCG là hocmon hướng sinh dục nhau thai được tiết ra từ:
Options (shared set): ['Tbao langhans của nhau thai', 'Lớp nội bào của nhau', 'Tế bào hạt của hoàng thể', 'Tế bào vỏ trong của trứng']
  line   6949 | Medium      | id 11e2e656db6a4a0795516f5dbc4297bc | A -> Tbao langhans của nhau thai
  line  11937 | Easy        | id f223fe92bfb247cf93a7bfa2ceba5e53 | B -> Lớp nội bào của nhau

### Group 997 — topic: Endocrinology, Other(No Category)
Q: Bệnh viêm quanh răng ở người đái tháo đường
Options (shared set): ['Dễ tăng nặng', 'Do đường huyết cao làm xuất hiện túi quanh răng', 'Không khác biệt với người bình thường', 'Tất cả đúng']
  line   6952 | Medium      | id 4917783457ae4710bc6777376abf1c82 | A -> Dễ tăng nặng
  line  10708 | Medium      | id d60f032d666b48b692c3ce10b73b25e4 | A -> Dễ tăng nặng

### Group 998 — topic: Endocrinology, Nephrology
Q: Hormon tác động lên sự tái hấp thu Na+ và bài xuất K+ ở ống thận:
Options (shared set): ['ADH', 'Adrenalin', 'Aldosteron', 'Noradrenalin']
  line   6953 | Medium      | id 261d11e26f224ab5afd8a6a3fbc3bba4 | C -> Aldosteron
  line   8250 | Easy        | id e4dd103f16244dabb15008b306503eda | C -> Aldosteron

### Group 999 — topic: Endocrinology
Q: Tác dụng của nhóm hormon steroid lên tế bào nhận theo cơ chế:
Options (shared set): ['Tăng tổng hợp enzym phụ thuộc hormon', 'Giảm tổng hợp enzym phụ thuộc hormon', 'Ức chế hệ thống enzym phụ thuộc hormon', 'Tất cả đều sai']
  line   6955 | Medium      | id 15d4e53ee3c64694a98ca03f0679e830 | D -> Tất cả đều sai
  line   6990 | Medium      | id 7b2e6ab9c10741ab89cd7d7fe9359e4d | D -> Tất cả đều sai.

### Group 1000 — topic: Endocrinology
Q: Quá trình tổng hợp catecholamin lần lượt qua các phản ứng
Options (shared set): ['Phe→Tyr→DOPA→DOPAmin →Nor adrenalin→ Adrenalin', 'Phe→Tyr→DOPA→DOPAmin→ Adrenalin→ Nor Adrenalin', 'Phe→Tyr→DOPAmin→DOPA→Nor adrenalin→ Adrenalin', 'Phe→DOPA→Tyr→DOPAmin→Nor adrenalin→ Adrenalin']
  line   6958 | Medium      | id 353823e2e5bb4f15a2c128bf6a8b2d48 | A -> Phe→Tyr→DOPA→DOPAmin →Nor adrenalin→ Adrenalin
  line   8627 | Challenging | id 7ff347bdefed43f6b323299c7f2021be | A -> Phe→Tyr→DOPA→DOPAmin →Nor adrenalin→ Adrenalin

### Group 1001 — topic: Endocrinology
Q: Những hormon nào sau đây thuộc nhóm Androstan
Options (shared set): ['Testosteron, Glucocorticoid', 'Androsteron, Minerano corticoid', 'Glucocorticoid, Minerano corticoid', 'Testosteron, Androsteron']
  line   6959 | Medium      | id cdff19ef3e034d578c5069c80cea76f8 | D -> Testosteron, Androsteron
  line   6995 | Medium      | id da0496eb752f421782bcd7b243e1287c | D -> Testosteron, Androsteron

### Group 1002 — topic: Endocrinology
Q: Sự tạo iodua (I-) thành iod nguyên tố (I0) được thực hiện ở tế bào tuyến với sự tham gia của?
Options (shared set): ['H2O2, Enzym kinase, TSH', 'H2O2, Enzym peroxidase, TSH', 'H2O, Enzym kinase, TSH', 'H2O2, Enzym dehydrogenase, TSH']
  line   6962 | Medium      | id 892fd984e07c4562bd1b5f04f5251fda | B -> H2O2, Enzym peroxidase, TSH
  line   6998 | Medium      | id c8e5c1a29b204b57b71e3fec56c417e7 | B -> H2O2 , enzym peroxidase, TSH.

### Group 1003 — topic: Endocrinology
Q: Dùng phản ứng Felinh để phát hiện sự có mặt của fructose trong dung dịch, phản ứng này dựa trên tính chất nào của fructose?
Options (shared set): ['Tính khử của nhóm aldehyd', 'Tính khử của nhóm ceton', 'Tính oxy hóa của nhóm alcol', 'Tính khử của nhóm alcol']
  line   7025 | Medium      | id 0d3e661c788843f5a3cc7fd71e017ae1 | B -> Tính khử của nhóm ceton
  line   7029 | Medium      | id 933e525e0fe444ce91dd18f7df762515 | B -> Tính khử của nhóm ceton

### Group 1004 — topic: Endocrinology
Q: Sedoheptulose gặp ở?
Options (shared set): ['Dạng aldohexose', 'Dạng cetohexose', 'Dạng aldoheptose', 'Dạng cetoheptose']
  line   7026 | Medium      | id e67691062fce41b98676afdb8ba6f8bf | D -> Dạng cetoheptose
  line   7583 | Medium      | id 943f0543b22a4a9cb26ee4e2ed397cbf | D -> Dạng cetoheptose

### Group 1005 — topic: Endocrinology, Internal Medicine
Q: Acid béo no là loại acid béo:
Options (shared set): ['Có nhiều trong dầu thực vật', 'Có chức ít liên kết đôi trên mạch carbon', 'Không chứa liên kết đôi trên mạch carbon', 'Dễ bị thủy phân, hầu hết chúng là những acid béo có lợi cho sức khỏe']
  line   7048 | Medium      | id 1ca25879d7b5401ab0d122d75f5d5c8a | C -> Không chứa liên kết đôi trên mạch carbon
  line  11003 | Easy        | id 9227a9481f1b4ca9a2656f78c9244a69 | C -> Không chứa liên kết đôi trên mạch carbon

### Group 1006 — topic: Endocrinology
Q: Acid amin nào sau đây là tiền chất của hormon tuyến giáp:
Options (shared set): ['Cystein', 'Methionin', 'Tyrosin', 'Selenocystein']
  line   7057 | Medium      | id 21a6fd53e6514d128654c782ff92204a | C -> Tyrosin
  line   7328 | Medium      | id 1ab979a7f4ca43fcaa74f07fa52665af | C -> Tyrosin

### Group 1007 — topic: Obstetrics and Gynecology, Endocrinology, Pathology
Q: Để đánh giá hoạt động nội tiết của buồng trứng và sự đáp ứng nội tiết của nội mạc tử cung, cần thực hiện sinh thiết nội mạc để làm GPBL:
Options (shared set): ['Vào khoảng ngày thứ 7 đến 10 của chu kỳ kinh 28 ngày', 'Vào khoảng ngày thứ 13 đến 15 của chu kỳ kinh 28 ngày', 'Vào khoảng ngày thứ 17 đến 19 của chu kỳ kinh 28 ngày', 'Vào khoảng ngày thứ 21 đến 23 của chu kỳ kinh 28 ngày']
  line   7074 | Medium      | id 19f81c923d2a489f94373556eee9d8a4 | D -> Vào khoảng ngày thứ 21 đến 23 của chu kỳ kinh 28 ngày
  line   7116 | Medium      | id 89eb7ef4e1d34733a15a6ce6429867f9 | D -> Vào khoảng ngày thứ 21 đến 23 của chu kỳ kinh 28 ngày

### Group 1008 — topic: Endocrinology, Obstetrics and Gynecology
Q: Điều nào sau đây không đúng với đái đường trong khi có thai?
Options (shared set): ['Ảnh hưởng lớn của bệnh này là gây tử vong 2/3 số trẻ sơ sinh trong quá trình mang thai.', 'Tuy được phát hiện và điều trị, nhưng vẫn có khoảng 4 - 8% dị dạng bẩm sinh.', 'Phát hiện và điều trị sớm cho những thai phụ, nên đã làm giảm đáng kể tỷ lệ tử vong chu sinh.', 'Tuy được phát hiện và điều trị, nhưng vẫn còn thai chết trong tử cung.']
  line   7100 | Medium      | id b2c3c79e16cd48e6869530ad338c4ccd | A -> Ảnh hưởng lớn của bệnh này là gây tử vong 2/3 số trẻ sơ sinh trong quá trình mang thai.
  line   8127 | Challenging | id 8dcffa5cdca94180b71863f0ac76e6ae | A -> Ảnh hưởng lớn của bệnh này là gây tử vong 2/3 số trẻ sơ sinh trong quá trình mang thai.

### Group 1009 — topic: Endocrinology, Obstetrics and Gynecology, Pediatrics
Q: Yếu tố góp phần quyết định hệ sinh dục chưa biệt hoá ban đầu phát triển theo hướng nam:
Options (shared set): ['NST giới tính.', 'TDF (Testis Determining Factor).', 'Estrogen.', 'Progesteron.']
  line   7162 | Medium      | id 67f71c98341b4cdfbc80a88fdb166798 | B -> TDF (Testis Determining Factor).
  line   7164 | Medium      | id 721c824cf7eb4feab2350608108c2d6f | B -> TDF (Testis Determining Factor).

### Group 1010 — topic: Endocrinology, Obstetrics and Gynecology, Pediatrics
Q: Yếu tố ảnh hưởng đến sự phát triển của đường sinh dục và bộ phận sinh dục ngoài của nữ:
Options (shared set): ['AMH (Anti Mullerian Hormon).', 'Estrogen.', 'Progesteron.', 'Tất cả đêu đúng.']
  line   7163 | Medium      | id 1bbc2b3168b348ac8249f43bd979cbbb | A -> AMH (Anti Mullerian Hormon).
  line   7165 | Medium      | id fe5b806b8b0548b6b392e48aa4b5fb10 | A -> AMH (Anti Mullerian Hormon).

### Group 1011 — topic: Endocrinology
Q: Đái tháo đường (còn gọi là bệnh tiểu đường) là một nhóm bệnh rối loạn chuyển hóa cacbohydrat khi hocmon insulin của tụy bị thiếu hay giảm tác động trong cơ thể, biểu hiện bằng mức đường glucozo trong máu luôn cao. Em hãy cho biết nồng độ glucozo trong máu người bình thường khoảng bao nhiêu %?
Options (shared set): ['0,1%', '0.01', '0,5%', '1,5%']
  line   7175 | Medium      | id ee6a37e156bf4a95861c5d61dedc9619 | A -> 0,1%
  line   7181 | Medium      | id 09432651c93140309f778dec7298a4e4 | A -> 0,1%

### Group 1012 — topic: Radiology, Nuclear Medicine
Q: 9.277. Xác định phát biểu sai về hiệu ứng sinh học của tia phóng xạ đối với cơ thể sống:
Options (shared set): ['Tế bào có thể mất khả năng phân chia.', 'Cấu trúc của ADN có thể bị thay đổi tạo ADN dị thường.', 'Các phân tử protein bị đứt gãy làm giảm khả năng hoạt động chức năng một số mô.', 'Nhân tế bào bị tổn thương ít hơn so với màng.']
  line   7315 | Medium      | id 8c666ec42bc542d3b0150c22ebf1a088 | D -> Nhân tế bào bị tổn thương ít hơn so với màng.
  line   9159 | Easy        | id 8be2e4c608394cfabaa8f4db31e26560 | D -> Nhân tế bào bị tổn thương ít hơn so với màng.

### Group 1013 — topic: Endocrinology
Q: Androgen ngoài tác động phát triển các đặc tính sinh dục thứ phát ở nam còn có tác động nào sau đây:
Options (shared set): ['Trị bệnh gout ở nam', 'Trị loãng xương ở nam giới', 'Trị nhiễm trùng sau phẫu thuật 115', 'Trị suy tim']
  line   7338 | Medium      | id 2d5d2189d8f24831aaf3465f7f8dd49f | B -> Trị loãng xương ở nam giới
  line   9340 | Medium      | id 7c47fcb106c74430bb38ef0852ea036e | B -> Trị loãng xương ở nam giới

### Group 1014 — topic: Pediatrics, Neonatology
Q: Bé gái, con 2/2, sinh thường 39 tuần, cân nặng lúc sinh 3400 gram, khóc ngay sau sinh. Lúc 28 giờ tuổi, mẹ thấy bé vàng da ở mặt. Khám: tỉnh, sinh hiệu ổn, da vàng đến gối, rốn khô, các hệ cơ quan khác không có gì lạ. Bé bú mẹ hoàn toàn, tiểu ướt tã nhiều lần trong ngày, đã tiêu phân su từ 24 giờ tuổi. Tiền căn mẹ không sốt lúc sanh, không làm xét nghiệm tầm soát liên cầu khuẩn nhóm B, ối vỡ 4 giờ trước sinh, nhóm máu O+. Nguyên nhân gây ra vàng da phù hợp nhất là gì?
Options (shared set): ['Bất đồng nhóm máu ABO', 'Bú sữa mẹ thất bại', 'Thiếu men G6PD', 'Nhiễm khuẩn huyết']
  line   7366 | Hard        | id d7917c566b494f3fbe18cce2f813c4c8 | A -> Bất đồng nhóm máu ABO
  line   7367 | Hard        | id 60f4db87e3d34bcfa2319f418aedbb7e | A -> Bất đồng nhóm máu ABO

### Group 1015 — topic: Pediatrics, Neonatology
Q: Bé trai, con 1/1, sinh thường 40 tuần, cân nặng lúc sinh 3200 gram, khóc ngay sau sinh. Bé bú mẹ tốt, tiêu tiểu bình thường. Lúc 60 giờ tuổi, khám trước xuất viện: tỉnh tươi, da vàng đến gối, rốn khô, các hệ cơ quan khác không ghi nhận bất thường. Bé được đo bilirubin qua da, kết quả 12 mg/dL, mẹ nhóm máu B+. Xử trí nào tiếp theo phù hợp nhất là gì?
Options (shared set): ['Cho bé nhập khoa sơ sinh, che mắt và che bìu, chiếu đèn liên tục', 'Xét nghiệm công thức máu, nhóm máu ABO-Rh, Coombs test trực tiếp, bilirubin toàn phần, trực tiếp', 'Cho bé xuất viện và hẹn tái khám vàng da sau 2 ngày', 'Cho bé xuất viện và dặn mẹ phơi nắng cho bé mỗi ngày từ 6-8 giờ sáng']
  line   7369 | Hard        | id f42f7655c87b4bc083725e0b4b168088 | C -> Cho bé xuất viện và hẹn tái khám vàng da sau 2 ngày
  line   7370 | Medium      | id 7ec8f58154374261b36cf0708f05af7b | C -> Cho bé xuất viện và hẹn tái khám vàng da sau 2 ngày

### Group 1016 — topic: Infectious Diseases, Pulmonology, Veterinary Medicine
Q: Bệnh cúm gia cầm mắc ở các loài vật sau NGOẠI TRỪ:
Options (shared set): ['Gia cầm', 'Thủy cầm', 'Chim', 'Cá']
  line   7376 | Medium      | id 1426097b52a64cdead0df3cf6d83ea06 | D -> Cá
  line   9981 | Easy        | id 0177e6fec7f040f9b803e72f1e3fe2b6 | D -> Cá

### Group 1017 — topic: Cardiology, Infectious Diseases
Q: Bệnh hay nhầm với thấp tim nhất là:
Options (shared set): ['Suy tim do nguyên nhân ngoài tim', 'Viêm tim do siêu vi trùng', 'Tiếng thổi tâm thu cơ năng', 'Viêm nội tâm mạc nhiễm khuẩn']
  line   7382 | Challenging | id f98bc2fda1ba48ce98fa0b51d06f96d9 | D -> Viêm nội tâm mạc nhiễm khuẩn
  line   7383 | Challenging | id 088e2815ffb74997a4dfcbbf7d58e895 | A -> Viêm nội tâm mạc nhiễm khuẩn

### Group 1018 — topic: Radiology, Physics
Q: Bức xạ hồng ngoại:
Options (shared set): ['Được sản sinh từ dòng cao tầng và tạo ra phản ứng nhiệt khi được hấp thu', 'Được sản sinh bằng nhiệt và tạo ra phản ứng hóa học khi được hấp thu', 'Được sản sinh bằng nhiệt và tạo ra phản ứng nhiệt khi được hấp thu', 'Được sản sinh từ dòng cao tầng và tạo ra phản ứng hóa học khi được hấp thu']
  line   7450 | Medium      | id 3fb1d2ca20b5439aa58193e2b1412d0d | C -> Được sản sinh bằng nhiệt và tạo ra phản ứng nhiệt khi được hấp thu
  line   9739 | Easy        | id 21616621d0b0490da5625e4a178cfe5a | C -> Được sản sinh bằng nhiêt và tạo ra phản ứng nhiệt khi được hấp thu

### Group 1019 — topic: Nephrology, Pharmacology
Q: Cần lưu ý điều gì khi bệnh nhân dùng thuốc lợi tiểu hypothiazid lâu ngày:
Options (shared set): ['Giảm liều và bổ sung kali', 'Tăng liều và bổ sung kali', 'Giảm liều và bổ sung calci', 'Giảm liều và bổ sung các chất điện giải']
  line   7536 | Challenging | id e0a316dcc4aa46399d167c8fb0104ad4 | A -> Giảm liều và bổ sung kali
  line  12032 | Medium      | id 01658fa1d7b34d67861ee5bd450cd8d9 | A -> Giảm liều và bổ sung kali

### Group 1020 — topic: Allergy and Immunology
Q: Đáp ứng miễn dịch là
Options (shared set): ['Khả năng nhận biết,đáp ứng và loại bỏ các yếu tố lạ(kháng nguyên)', 'Phản ứng của cơ thể trước sự xâm nhập của các yếu tố lạ(kháng nguyên)', 'Khả năng tự vệ của cơ thể trước những yếu tố lạ(kháng nguyên)', 'Phản ứng bảo vệ của cơ thể trước những yếu tố lạ(kháng nguyên)']
  line   7544 | Easy        | id 7543d52bf6ea439fb5e39bc4720c5005 | A -> Khả năng nhận biết,đáp ứng và loại bỏ các yếu tố lạ(kháng nguyên)
  line  10337 | Easy        | id 8fed2d1814704d90b1151c631a35b4c3 | A -> Khả năng nhận biết,đáp ứng và loại bỏ các yếu tố lạ(kháng nguyên)

### Group 1021 — topic: Dermatology
Q: Tên đúng của bệnh viêm da cơ địa là
Options (shared set): ['Atopic dermatitis', 'Contact dermatitis', 'Mycosis', 'Scabies']
  line   7586 | Easy        | id 47d634aa8d174818b856b097d7de5b97 | A -> Atopic dermatitis
  line  10309 | Easy        | id 98f68fbaa87343baa6096cd734f4a7b3 | A -> Atopic dermatitis

### Group 1022 — topic: Dermatology, Allergy and Immunology
Q: Hội chứng DRESS là:
Options (shared set): ['Phản ứng do thuốc gây tăng bạch cầu ái toan và tổn thương nội tạng', 'Phản ứng do thuốc gây tăng bạch cầu ái kiềm và tổn thương nội tạng', 'Phản ứng do thuốc gây tăng bạch cầu đa nhân trung tính và tổn thương nội tạng', 'Phản ứng do thuốc gây tăng bạch cầu ái toan, không gây tổn thương nội tạng']
  line   7608 | Medium      | id 2819741d151e428393e3ec58142498ba | A -> Phản ứng do thuốc gây tăng bạch cầu ái toan và tổn thương nội tạng
  line  11882 | Easy        | id d341ec11830142dbae3dfc55859f2bae | A -> Phản ứng do thuốc gây tăng bạch cầu ái toan và tổn thương nội tạng

### Group 1023 — topic: Pulmonology, Geriatrics, Eastern Medicine
Q: Bệnh nhân nam 80 tuổi nghề nghiệp giáo viên cấp 3 về hưu, bị bệnh hơn 15 năm nay, hay phát bệnh mùa đông. Đợt 1/2016 vào viện điều trị với các triệu chứng khó thở đột ngột, tiếng rít, khó thở thì thở ra và đã được điều trị ổn định với chẩn đoán tây y là HPQ. Hiện tại bệnh nhân hết triệu chứng thở rít, đỡ khó thở nhiều, tuy nhiên còn nhiều biểu hiện triệu chứng sợ lạnh, sắc mặt trắng bệch, hồi hộp ù tai, hơi thở ngắn. Càng lao động càng tăng, khạc đờm có bọt, lưng gối mỏi yếu, nước tiểu trong dài, tiểu tiện nhiều lần, lưỡi đạm, rêu nhuận, mạch trầm tế vô lực. Bệnh nhân được chẩn đoán theo YHCT?
Options (shared set): ['Háo suyễn thể tỳ hư', 'Háo suyễn thể phế âm hư', 'Háo suyễn thể thận âm hư', 'Háo suyễn thể thận dương hư']
  line   7682 | Challenging | id 6d31f4d5839343a28759ae2386f15d93 | D -> Háo suyễn thể thận dương hư
  line  10773 | Hard        | id 1c86fd00e2dc407b94d6a638df57253e | D -> Háo suyễn thể thận dương hư

### Group 1024 — topic: Dermatology, Allergy and Immunology
Q: Kim lẩy da cắm vào giữa giọt dung dịch trên mặt da tạo thành một góc:
Options (shared set): ['150', '300', '450', '600']
  line   7702 | Medium      | id 055b420aaec746caa68a796d80cff0df | C -> 450
  line  10311 | Easy        | id fd7bd7c7680e4c62acac0cd7934da371 | C -> 450

### Group 1025 — topic: Pulmonology, Intensive Care
Q: Người bệnh thở máy được tiến hành cai máy thở khi:
Options (shared set): ['Hết rối loạn hô hấp', 'Tình trạng hô hấp đã ổn định', 'Hết khó thở', 'Hết suy hô hấp']
  line   7839 | Challenging | id 88e4514251c042b99c4f721123b7b3d0 | B -> Tình trạng hô hấp đã ổn định
  line   8487 | Challenging | id d361d5c3a40847c98b11d7c288d663ec | B -> Tình trạng hô hấp đã ổn định
  line  12203 | Medium      | id f800fd7457864dabba82ab90d89c086e | B -> Tình trạng hô hấp đã ổn định

### Group 1026 — topic: Dermatology, Allergy and Immunology
Q: Triệu chứng của bệnh mày đay là
Options (shared set): ['Sẩn phù, khi lặn không để lại dấu vết gì', 'Sẩn mụn nước', 'Sẩn chắc', 'Tổn thương hình bia bắn']
  line   7861 | Easy        | id e73847723da14df0b5f7467e32bdc6bf | A -> Sẩn phù, khi lặn không để lại dấu vết gì
  line  10365 | Medium      | id 0900d31dec294cb09551a25795abc1f5 | A -> Sẩn phù, khi lặn không để lại dấu vết gì

### Group 1027 — topic: Infectious Diseases, Virology
Q: Đặc điểm virus dại : nhân ARN vỏ lipid, yếu, bất hoạt bởi nhiệt độ và các chất hòa tan lipid, tia cực tím, cồn,. cồn iod?
Options (shared set): ['Đúng', 'Sai']
  line   8096 | Easy        | id 6d55ae38c41646a4816d5b124a01079f | A -> Đúng
  line   8098 | Medium      | id 18080111dc6d4ce1b3f649747bc87727 | A -> Đúng

### Group 1028 — topic: Otolaryngology, Radiology
Q: Hình ảnh viêm xoang hàm do răng trên phim Blondeau là:
Options (shared set): ['Mờ đặc xoang hàm một bên tương ứng răng bệnh', 'Dày niêm mạc một bên tương ứng răng bệnh', 'Mờ xoang bên tương ứng răng bệnh và mờ xoang trán hoặc sáng đối bên.', 'Mờ với hình ảnh mặt trời mọc bên răng.']
  line   8240 | Challenging | id 514259ff704a4443aec04376a2583916 | A -> Mờ đặc xoang hàm một bên tương ứng răng bệnh
  line   9899 | Medium      | id 1d04121ce0ee43068ac5eaa82124615d | A -> Mờ đặc xoang hàm một bên tương ứng răng bệnh

### Group 1029 — topic: Radiology, Physics
Q: Hồng ngoại là bức xạ điện từ có bước sóng:
Options (shared set): ['400.000nm-770nm', '200nm-390nm', '400nm-760nm', '400.000nm-77nm']
  line   8253 | Easy        | id e04aa85fba244ebeaa751b1b2eb9cdbd | A -> 400.000nm-770nm
  line   9738 | Easy        | id 863867445bff4a889b9c267b80a55ef3 | A -> 400.000nm-770nm

### Group 1030 — topic: Allergy and Immunology
Q: Kháng thể nào sau đây có thể tìm thấy trong dịch tiết
Options (shared set): ['IgG', 'IgA', 'IgE', 'IgM']
  line   8279 | Easy        | id e573d367c04f4a0a8f0924803a4a4bb9 | B -> IgA
  line   8280 | Easy        | id 0ff640c2865c48379b7a9b186d5a407a | C -> IgA.

### Group 1031 — topic: Psychiatry, Addiction Medicine
Q: Một bệnh nhân nam 55 tuổi, đến khám bệnh do bị mất ngủ kéo dài từ 12 tháng nay. Bệnh nhân than phiền rất khó vào giấc ngủ, buổi tối bệnh nhân lên giường nằm phải 2 tiếng mới ngủ được. Bệnh nhân ngủ rất kém chỉ được khoảng 4 giờ mỗi tối. Gia đình bệnh nhân cho biết, bệnh nhân nghiện rượu hơn 30 năm nay, mỗi ngày uống chừng 500ml rượu loại 40 độ cồn. Nếu không được uống rượu, bệnh nhân rất thèm, run tay, buồn nôn, vã mồ hôi… Và sau khi được uống rượu, các biểu hiện trên sẽ biến mất. Qua khai thác, bệnh nhân không có tiền sử chấn thương sọ não và không sử dụng ma túy. Chẩn đoán nào là phù hợp nhất với bệnh nhân này?
Options (shared set): ['Nghiện rượu', 'Giai đoạn trầm cảm', 'Giai đoạn hưng cảm', 'Tâm thần phân liệt']
  line   8393 | Hard        | id 11a501cb25f84d41a3554674f8414603 | A -> Nghiện rượu
  line   8394 | Hard        | id a206cb65e11445e294c63444f0f97b20 | B -> Nghiện rượu

### Group 1032 — topic: Allergy and Immunology, Oncology
Q: Một trong các chỉ định của thuốc kháng histamin H1 thế hệ 1 là:
Options (shared set): ['Cắt cơn hen phế quản', 'Điều trị chứng trào ngược dạ dày - thực quản', 'Chống nôn do dùng các thuốc chống ung thư', 'Loét dạ dày - tá tràng']
  line   8411 | Medium      | id 1cf71a1cc8d34811a6a8d4305e5b0dee | C -> Chống nôn do dùng các thuốc chống ung thư
  line  10299 | Medium      | id e8a76358f11546de921f8af38a75b49d | C -> Chống nôn do dùng các thuốc chống ung thư

### Group 1033 — topic: Anesthesiology, Pain Management
Q: Pethidin là thuốc thuộc nhóm:
Options (shared set): ['Gây tê, gây mê', 'Giảm đau trung ương', 'ức chế tâm than', 'Chống trầm cảm']
  line   8580 | Easy        | id 954fbe52dd964e11a4e0254031621bee | B -> Giảm đau trung ương
  line  10874 | Easy        | id ce819de69aef4267a96b582acb16982c | B -> Giảm đau trung ương

### Group 1034 — topic: Pharmacology, Pain Management
Q: Tác dụng Pethidin so với Morphin?
Options (shared set): ['Kém 5 lần', 'Kém 10 lần', 'Kém 20 lần', 'Kém 15 lần']
  line   8705 | Medium      | id d86517d0633e4e8390da6dc84966c38c | B -> Kém 10 lần
  line  11275 | Easy        | id b6d877178dc14b15829ec846948da018 | B -> Kém 10 lần

### Group 1035 — topic: Hematology, Emergency Medicine
Q: Tai biến truyền nhóm máu sẽ xảy ra khi: Kháng nguyên người cho bị ngưng kết với kháng thể người nhận?
Options (shared set): ['Đúng', 'Sai']
  line   8715 | Medium      | id 527d85bde5424644824cb84033c0604f | A -> Đúng
  line  11884 | Easy        | id 70fb1233a3a942f58810e6ed0194ba38 | A -> Đúng

### Group 1036 — topic: Endocrinology, Cell Biology
Q: Tế bào Leydig là tế bào:
Options (shared set): ['Nằm ở biểu mô tinh', 'Nằm trong mô kẽ tinh hoàn', 'Chế tiết Estradiol', 'Bảo vệ tinh trùng']
  line   8747 | Easy        | id fa74b282fcb94c61a7cf0b090be7b87e | B -> Nằm trong mô kẽ tinh hoàn
  line   8748 | Easy        | id acc7ee5fc46d48c3b54ae32c193babe5 | B -> Nằm trong mô kẽ tinh hoàn

### Group 1037 — topic: Psychiatry, Addiction Medicine
Q: Thuốc đối kháng với morphin thường dùng khi cai nghiện là:
Options (shared set): ['Methadon', 'Fentanyl', 'Naltrexon', 'Pentazocin']
  line   8820 | Medium      | id 08612e88fb1a4cc3927417a4dba4fa69 | C -> Naltrexon
  line  10857 | Medium      | id d3e9eef6981b4027902d4407320cca41 | C -> Naltrexon

### Group 1038 — topic: Neurology, General Medicine
Q: Thuốc kháng cholinesterase loại ức chế có hồi phục được dùng trong điều trị là:
Options (shared set): ['Chữa ngộ độc cura loại khử cực bản vận động cơ vân.', 'Tất cả các phương án đều sai.', 'Không làm hạ đường huyết tư thế đứng.', 'Ức chế men chuyển cholinesterase không hồi phục.']
  line   8832 | Hard        | id 2e079649322e4460b05b0bc3cc738a24 | B -> Tất cả các phương án đều sai.
  line  10863 | Medium      | id faeeaeedfaf14de5b24c62704624abeb | B -> Tất cả các phương án đều sai.

### Group 1039 — topic: Dermatology, Allergy and Immunology
Q: Trong bệnh viêm da tiếp xúc dị ứng, khi kháng nguyên thâm nhập vào thượng bì, tế bào nào tiếp nhận và xử lý kháng nguyên?
Options (shared set): ['Keratinocytes', 'Langerhans', 'Melanocytes', 'Lymphocytes']
  line   8922 | Medium      | id dfc751f55ff04d85b6d6123952b6fbe6 | B -> Langerhans
  line  10322 | Medium      | id b094d03b518c4c798ba866f96baf3046 | B -> Langerhans

### Group 1040 — topic: General Medicine, Dermatology
Q: Vị trí loét ép đầu tiên thường ở đâu?
Options (shared set): ['Mông', 'Gáy', 'Bả vai', 'Gót chân']
  line   9046 | Easy        | id deebb6bf20e147798299db540eecc6ff | C -> Bả vai
  line  10823 | Easy        | id 1bc7885b23524fe2abbdfcd2621948b4 | C -> Bả vai
  line  12321 | Easy        | id 3078a4909e6c45f299451b307dafc36c | C -> Bả vai

### Group 1041 — topic: Otolaryngology, Oncology, Radiology
Q: Hai phương pháp thường dùng nhất để điều trị ung thư vòm là:
Options (shared set): ['Phẫu thuật và Tia xạ', 'Phẫu thuật và Hóa chất', 'Tia xạ và Hóa chất', 'Tia xạ và Miễn dịch']
  line   9115 | Medium      | id 00aa5f2e53e84fd5b5545e96dbfd8243 | C -> Tia xạ và Hóa chất
  line   9952 | Medium      | id 6606e3653c484e528cd68539078e72e5 | C -> Tia xạ và Hóa chất

### Group 1042 — topic: Dentistry, Radiology
Q: Các triệu chứng có thể thấy trên XQ của sang chấn mô quanh răng do khớp cắn?
Options (shared set): ['Khoảng dây chằng quanh răng giãn rộng và tăng độ dày lá cứng', 'Khoảng dây chằng quanh răng giãn rộng và hình ảnh thấu quang vùng chóp chân răng', 'Tăng độ dày lá cứng và hình ảnh thấu quang vùng chóp chân răng', 'Hình ảnh thấu quang vùng chóp chân răng và khoảng dây chằng quanh răng thu hẹp']
  line   9130 | Medium      | id b3a10d148b574ddeacb632c1f15f8159 | D -> Hình ảnh thấu quang vùng chóp chân răng và khoảng dây chằng quanh răng thu hẹp
  line  10671 | Medium      | id bbec4600c1e745e0a4b06d4c05d4d772 | D -> Hình ảnh thấu quang vùng chóp chân răng và khoảng dây chằng quanh răng thu hẹp

### Group 1043 — topic: Cardiology, Radiology
Q: Chụp động mạch là một xét nghiệm cần thiết để chẩn đóan bệnh lý mạch máu, nhưng có thể gây nên những tai biến trầm trọng.
Options (shared set): ['Đúng .', 'Sai.']
  line   9141 | Medium      | id 1fe465fbc6bc4c73a6cdb007088085fd | B -> Sai.
  line  11029 | Medium      | id 95e4fe7b4cca4cd5ae4cb1311fbe4e07 | B -> Sai

### Group 1044 — topic: Molecular Biology
Q: Protein nào tham gia vào sự sao chép DNA ở Prokaryote có hoạt tính ATPase:
Options (shared set): ['Primase', 'DNA polymerase III', 'Helicase', 'SSB protein']
  line   9169 | Easy        | id 7424d2e90a4d4d76aea68a63244150fe | C -> Helicase
  line   9211 | Easy        | id d7ed8801b470448c95a8fe044740bbb2 | C -> Helicase

### Group 1045 — topic: Molecular Biology
Q: Liên kết và tương tác hóa học nào làm ổn định cấu trúc bậc 2 của DNA:
Options (shared set): ['Cộng hóa trị và hidro', 'Hydro và ion', 'Cộng hóa trị và ion', 'Hydro và kị nước']
  line   9171 | Easy        | id 211890bf7d6246fbb34b2679b4f6292e | D -> Hydro và kị nước
  line   9212 | Easy        | id d5b435e0aa1346a9b2f313b81f91a10c | D -> Hydro và kị nước

### Group 1046 — topic: Molecular Biology
Q: Enzyme nào tách mạch DNA trong quá trình sao chép:
Options (shared set): ['Helicase', 'Ligase', 'Topoisomerase II', 'Primase']
  line   9172 | Easy        | id b3a7b7562ab349a894dbe14f9c537908 | A -> Helicase
  line   9213 | Easy        | id 12ac52b5e6164f848254d23129f07881 | A -> Helicase

### Group 1047 — topic: Molecular Biology
Q: Enzyme nào có vai trò nối các đoạn DNA:
Options (shared set): ['Helicase', "3'-5' exonuclease", 'Ligase', 'Primase']
  line   9173 | Easy        | id 93e8d565b52a49a2bb30bcd2ccfbfdae | C -> Ligase
  line   9214 | Easy        | id 9100ab2dacef4315b532e23074f1269f | C -> Ligase

### Group 1048 — topic: Molecular Biology
Q: Enzyme nào tổng hợp các mồi RNA ngắn trong sao chép:
Options (shared set): ['RNA polymerase III', "3'-5' exonuclease", 'Ligase', 'Primase']
  line   9174 | Easy        | id 847c1959e61b4337a9bba08efe84347f | D -> Primase
  line   9215 | Easy        | id cc07a9881dbc4313883e3b5699ccef73 | D -> Primase

### Group 1049 — topic: Molecular Biology
Q: Enzyme nào tham gia tổng hợp mạch chậm DNA trong sao chép:
Options (shared set): ['DNA polymerase III', 'Ligase', 'Primase', 'Tất cả đều đúng']
  line   9175 | Easy        | id 1ae1080a6df7425e97f05ad153160ca9 | D -> Tất cả đều đúng
  line   9216 | Easy        | id 53ec114fe4b4441e8fe169441c1a39dc | A -> DNA polymerase III

### Group 1050 — topic: Molecular Biology
Q: Enzyme nào có chức năng phiên mã ngược:
Options (shared set): ['Primase', 'DNA polymerase', 'RNA polymerase', 'Tất cả đều sai']
  line   9176 | Easy        | id 3885a07dee0f45ec84411def21fd2cdb | D -> Tất cả đều sai
  line   9217 | Easy        | id bb8112276d374dbda4edf92abfc23caf | B -> DNA polymerase

### Group 1051 — topic: Molecular Biology
Q: Trong chủng E. coli đột biến, DNA polymerase I bị mất hoạt tính do đó sẽ không có vai trị:
Options (shared set): ['Phiên mã', 'Sửa sai bằng cách cắt bỏ', 'Tháo xoắn DNA', 'Tái tổ hợp DNA']
  line   9178 | Medium      | id 6ef4338237b04602a5f60b8f2908d2b6 | B -> Sửa sai bằng cách cắt bỏ
  line   9219 | Medium      | id f9a9c8dc331047a688685d101dd076c9 | B -> Sửa sai bằng cách cắt bỏ

### Group 1052 — topic: Molecular Biology
Q: DNA có thể tồn tại ở bào quan nào của tế bào:
Options (shared set): ['Nhân, bộ máy Golgi, ty thể', 'Nhân, ty thể, mạng lưới nội chất', 'Nhân, ty thể, lục lạp', 'Nhân, bộ máy Golgi, lục lạp']
  line   9184 | Easy        | id 0c1d1279558b4f47bb0662c201221de7 | C -> Nhân, ty thể, lục lạp
  line   9220 | Easy        | id 70076ceaa8114a53bc53afbb1c88954b | C -> Nhân, ty thể, lục lạp
  line   9242 | Easy        | id 6a7b3f1458ae48608bb9af6762fc2e86 | A -> Nhân, ty thể, lục lạp

### Group 1053 — topic: Molecular Biology
Q: Protein SSB trong sao chép DNA được viết tắt từ:
Options (shared set): ['Simple strand binding', 'Simple strandline binding', 'Single strandline bind', 'Single strand binding']
  line   9186 | Easy        | id cbdb77a8d2744472999cd82bec394ac7 | D -> Single strand binding
  line   9221 | Easy        | id c1b62473a6bd4adc8dd2ce406f7ed8b8 | D -> Single strand binding

### Group 1054 — topic: Molecular Biology
Q: Enzyme Topoisomerase có vai trò:
Options (shared set): ['Tách mạch tạo chẻ ba sao chép DNA.', 'Cắt một mạch DNA phía sau chẻ ba sao chép để tháo xoắn.', 'Sửa sai.', 'Làm mồi để tổng hợp các đoạn Okazaki.']
  line   9194 | Easy        | id 004756f0fc124700af61fe0f6528092d | D -> Làm mồi để tổng hợp các đoạn Okazaki.
  line   9224 | Easy        | id bb90ac026be9412b8c4daa7f413e87b7 | B -> Cắt một mạch DNA phía sau chẻ ba sao chép để tháo xoắn.

### Group 1055 — topic: Molecular Biology
Q: Acid nucleic là một chuỗi các nucleotide. Các nucleotide được tạo nên từ 3 thành phần. Thành phần nào trong số đó có thể tách ra khỏi nucleotide mà không làm mạch đứt rời:
Options (shared set): ['Đường', 'Phosphate', 'Base nitơ', 'Cả a và c']
  line   9196 | Easy        | id 90b58478cae54092928ed10c0c390112 | B -> Phosphate
  line   9225 | Easy        | id 7dab80ff0ee14206a11c2602db6d83d7 | B -> Phosphate

### Group 1056 — topic: Molecular Biology
Q: Nếu một trong những enzyme sau đây vắng mặt thì không có nucleotide nào được gắn vào chẻ ba sao chép. Enzyme nào trong số này:
Options (shared set): ['Polymerase I (có hoạt tính polymer hóa).', "Polymerase I (có hoạt tính exonucleose 5'--->3').", 'Polymerase III.', 'DNA- ligase.']
  line   9198 | Easy        | id 2a4e2ffb7470475f842f77a4a0c647c5 | D -> DNA- ligase.
  line   9226 | Easy        | id 97d364f3e9804f53bdffdd857c7e5515 | B -> Polymerase III.

### Group 1057 — topic: Orthopedics
Q: Trong trật khớp háng kiểu chậu, so với đường Nelaton-Rose, mẫu chuyển:
Options (shared set): ['Nằm cao hơn', 'Nằm thấp hơn', 'Ngang bằng', 'A và B đều đúng']
  line   9258 | Medium      | id 0f0d3b75ea624b459fa3f0ce204f8b4b | A -> Nằm cao hơn
  line   9275 | Medium      | id f62f18db66764accb0a94d2b62f9ce1e | A -> Nằm cao hơn

### Group 1058 — topic: Dentistry, Orthopedics
Q: Sang chấn mô quanh răng tiên phát?
Options (shared set): ['Xảy ra trên răng có mô quanh răng bị giảm thế tích (tiêu xương, tụt lợi) kèm theo lực khớp cắn quá mạnh', 'Xảy ra trên răng có mô quanh răng hoàn toàn khoẻ manh, tổn thương chỉ đơn thuần do lực quá mức', 'Xảy ra trên răng có mô quanh răng bị giảm thế tích (tiêu xương, tụt lợi) kèm theo lực khớp cắn bình thường', 'Xảy ra trên răng có mô quanh răng hoàn toàn khoẻ manh và lực khớp cắn bình thường']
  line   9329 | Medium      | id e82e2c2d152a483297a1176bb7e6131a | B -> Xảy ra trên răng có mô quanh răng hoàn toàn khoẻ manh, tổn thương chỉ đơn thuần do lực quá mức
  line  10713 | Medium      | id b2691783c50f40878f01f81622fbdca5 | B -> Xảy ra trên răng có mô quanh răng hoàn toàn khoẻ manh, tổn thương chỉ đơn thuần do lực quá mức

### Group 1059 — topic: Parasitology
Q: Ý nào sai với sán dây bò
Options (shared set): ['Không đẻ trứng trong ruột người', 'Lây truyền do tiêu hóa', 'Bò là ký chủ phụ', 'Trứng có nắp']
  line   9387 | Easy        | id 4df457288cc346e1845e2b66bccf6396 | D -> Trứng có nắp
  line   9388 | Easy        | id 0be7cc874b7f4e6e856a490f005324a4 | D -> Trứng có nắp

### Group 1060 — topic: Parasitology
Q: Ký chủ trung gian của sán dây chó
Options (shared set): ['Chó', 'Người', 'Bọ chét', 'Cá']
  line   9390 | Easy        | id d815b92e06994e37808d23ee64835ee9 | C -> Bọ chét
  line   9420 | Easy        | id 657e4f3df773465eb480ca84781f5808 | C -> Bọ chét

### Group 1061 — topic: Obstetrics and Gynecology, Genetics
Q: Nguyên nhân sảy thai nào sau đây không điều trị được?
Options (shared set): ['U xơ tử cung', 'Hở eo tử cung', 'Rối loạn nhiễm sắc thể', 'Nhiễm trùng cấp tính']
  line   9451 | Medium      | id 02a7011ed251473fb7f29d92e4c9af6b | C -> Rối loạn nhiễm sắc thể
  line   9452 | Medium      | id 14df1632daca441e99aefe7f5e00de9a | D -> Rối loạn nhiễm sắc thể
  line  11525 | Easy        | id ab38aae6072045c5a5a2c9dea92861fb | C -> Rối loạn nhiễm sắc thể

### Group 1062 — topic: Obstetrics and Gynecology, Genetics
Q: Sẩy thai liên tiếp nguyên nhân thường do:
Options (shared set): ['Đa thai', 'Mẹ bị lao phổi.', 'Bất thường nhiễm sắc thể ở thai.', 'Mẹ bị sang chấn']
  line   9476 | Medium      | id 0cfbd56b3f054f8eb493f8bea93d513e | C -> Bất thường nhiễm sắc thể ở thai.
  line   9485 | Medium      | id cb1c084234d64177b99cd78d1168c022 | D -> Bất thường nhiễm sắc thể ở thai.

### Group 1063 — topic: Obstetrics and Gynecology, Pediatrics, Genetics
Q: Double test được làm nhằm đánh giá nguy cơ:
Options (shared set): ['Khuyết tật ống thần kinh, trisomy 13, trisomy 18', 'Hội chứng Down, trisomy 13, trisomy 18', 'Hội chứng Down, khuyết tật ống thần kinh, trisomy 18', 'Hội chứng Down, khuyết tật ống thần kinh, trisomy 13']
  line   9496 | Medium      | id 454be956b8434e00bda52c8f3e1e3b6d | B -> Hội chứng Down, trisomy 13, trisomy 18
  line  11559 | Medium      | id 7ca4ba14794b4aef82d863c4bcbb75b9 | A -> Hội chứng Down, khuyết tật ống thần kinh, trisomy 18

### Group 1064 — topic: Allergy and Immunology, Genetics
Q: Gene mã cho các vùng thay đổi của chuỗi nặng phân tử kháng thể nằm trên nhiễm sắc thể nào:
Options (shared set): ['22', '7', 'c.2', '14']
  line   9515 | Easy        | id ff993481fa754313ac06889b341e074a | D -> 14
  line  11573 | Easy        | id 65d662fe687e48d1bf72170ee42bd986 | D -> 14

### Group 1065 — topic: Gastroenterology, Genetics
Q: Thiếu G6 Phosphatase gặp trong bệnh lý nào sau đây:
Options (shared set): ['Bệnh Wilson', 'Bệnh Von Gierke', 'Bệnh xơ gan nhiễm sắt', 'Bệnh thiểu α1 antitrypsin']
  line   9521 | Medium      | id ccfdd2e3b9d54ebdb00166d7c2a10759 | B -> Bệnh Von Gierke
  line  10582 | Medium      | id fb00bd01c1004f40996bd7d0a517d888 | B -> Bệnh Von Gierke

### Group 1066 — topic: Toxicology, Chemistry
Q: Chất nào không thể khử độc trong mặt nạ phòng độc khí CO ?
Options (shared set): ['Than hoạt tính', 'Ag2O', 'Oxide kim loại', 'MnO2']
  line   9584 | Medium      | id 8b58206cdbbf430b884c013c3f178919 | A -> Than hoạt tính
  line  11784 | Medium      | id 994178d299d04093931ce2aa696c4ae8 | A -> Than hoạt tính

### Group 1067 — topic: Toxicology, Chemistry
Q: Câu nào sau đây không đúng với Etanol:
Options (shared set): ['Chất lỏng không màu, không mùi, vị cay.', 'Khối lượng riêng 0,796g ở 15C, sôi ở 66 C', 'Phân bố tốt vào dịch cơ thể', 'Trường hợp ngộ độc thường sủ dụng quá nhiều bia rượu']
  line   9597 | Easy        | id 88d70f942ee34b42b7017a69e52b55f5 | B -> Khối lượng riêng 0,796g ở 15C, sôi ở 66 C
  line   9619 | Easy        | id 5d1f44d739314b89b07232a8c17600b0 | B -> Khối lượng riêng 0,796g ở 15C, sôi ở 66 C

### Group 1068 — topic: Surgery, General Medicine
Q: Trước khi đưa người bệnh đi phẫu thuật, điều dưỡng viên phải:
Options (shared set): ['Hoàn thiện thủ tục hành chính', 'Kiểm tra lại công tác chuẩn bị người bệnh', 'Đánh giá dấu hiệu sinh tồn, tình trạng người bệnh', 'Tất cả đều đúng.']
  line   9679 | Medium      | id 740ffee30fb7412d8cfd18185d4ff0ca | D -> Tất cả đều đúng.
  line  12218 | Easy        | id dd122f03b6f04f2bbc8e36d07f4fcf4b | D -> Tất cả đều đúng.
  line  12229 | Easy        | id 9daacb22442a4968b993ac81678e8d6c | D -> Tất cả đều đúng.

### Group 1069 — topic: Physical Medicine and Rehabilitation
Q: Vị trí chêm lót gối khi bệnh nhân nằm nghiêng bên liệt:
Options (shared set): ['Đầu, vai bên lành, chân và lưng bên liệt.', 'Đầu, chân bên lành, vai và lưng bên liệt.', 'Đầu, chân bên liệt, vai và lưng bên lành.', 'Đầu, lưng bên lành, chân và vai bên liệt.']
  line   9760 | Medium      | id dd30112ad5f3401185934c6b0ad88900 | B -> Đầu, chân bên lành, vai và lưng bên liệt.
  line   9791 | Easy        | id 30dde6f815144dd0bc70a956baf5126f | D -> Đầu, lưng bên lành, chân và vai bên liệt

### Group 1070 — topic: Physical Medicine and Rehabilitation
Q: Vai trò của tập vận động giúp:
Options (shared set): ['Phát hiện tổn thương co cứng, co rút cơ', 'Cải thiện tình trạng co cứng co rút', 'Phát hiện...', 'Cả 3']
  line   9761 | Medium      | id 825cf56b6be949309ec1e527e7fa382e | B -> Cải thiện tình trạng co cứng co rút
  line   9775 | Medium      | id a613721328ea46f3b1b0816893e64eb2 | C -> Cải thiện tình trạng co cứng co rút

### Group 1071 — topic: Neurology, Physical Medicine and Rehabilitation, Geriatrics
Q: Đối với bệnh nhân liệt toàn thân, cần xoay trở 2 giờ/lần để:
Options (shared set): ['Phòng ngừa loét ép, dễ vệ sinh, bệnh nhân đỡ mỏi...', 'Tránh teo cơ, cúng khớp', 'Phòng ngừa loét ép, tránh teo cơ, cứng khớp', 'A và B đúng']
  line   9805 | Medium      | id 94f47311b7d14f8fa7e6166a2bed1b9e | C -> Phòng ngừa loét ép, tránh teo cơ, cứng khớp
  line  10754 | Medium      | id 4b99684f73d14739b3f201d1d603b057 | C -> Phòng ngừa loét ép, tránh teo cơ, cứng khớp

### Group 1072 — topic: Neurology, Neurosurgery, Pathology
Q: U sợi thần kinh có đặc điểm gì?
Options (shared set): ['Xuất nguồn từ tế bào vỏ bao thần kinh.', 'Có thể có nhiều chỗ trên thân người.', 'Hiếm khi có vỏ bao.', 'Diễn tiến nhanh, khoảng 20% hóa ác nếu có kích thước to.']
  line   9824 | Medium      | id 3da46ee9529148cfa1e0f34e07654178 | B -> Có thể có nhiều chỗ trên thân người.
  line   9836 | Medium      | id 716738159bd3408682d716179d192593 | B -> Có thể có nhiều chỗ trên thân người.

### Group 1073 — topic: Neurology, Neurosurgery, Pathology
Q: U ống nội tủy thường có ở đâu?
Options (shared set): ['Chất xám của bán cầu đại não.', 'Não thất.', 'Thân não.', 'Tiểu não']
  line   9825 | Medium      | id cc5e591feb3443c9bcea811c44895fce | B -> Não thất.
  line   9831 | Medium      | id 6bd14ba1eb7649f88a3faa9212b7e154 | B -> Não thất.

### Group 1074 — topic: Neurology, Neurosurgery, Pathology
Q: U nguyên bào thần kinh đệm đa dạng có đặc điểm gì?
Options (shared set): ['Có xuất độ thấp nhất.', 'Tế bào u giống tế bào sao bình thường. nhưng tăng sản mạnh.', 'Là u tế bào sao độ 3 và độ 4.', 'Có tế bào sao và nguyên bào thần kinh']
  line   9826 | Medium      | id 9695a6fbe21c45418d159fe2ea3939fb | C -> Là u tế bào sao độ 3 và độ 4.
  line   9832 | Medium      | id 894ac604a14d49479724846577b5bc21 | C -> Là u tế bào sao độ 3 và độ 4.

### Group 1075 — topic: Neurology, Neurosurgery, Pathology
Q: U tế bào ít nhánh thường có ở đâu?
Options (shared set): ['Chất trắng bán cầu đại não', 'Chất xám bán cầu đại não', 'Cầu não', 'Nơi giao thoa của thần kinh thị giác']
  line   9827 | Medium      | id 3ae8aa7ee5b24ea5a1aab02ef949547b | A -> Chất trắng bán cầu đại não
  line   9833 | Medium      | id 8a53aec1003748ddb232853b82422271 | A -> Chất trắng bán cầu đại não

### Group 1076 — topic: Neurology, Neurosurgery, Pathology
Q: Loại u nào sau đây KHÔNG PHẢI là u của mô thần kinh đệm?
Options (shared set): ['U tế bào ít nhánh', 'U ống nội tủy.', 'U nguyên bào thần kinh đệm đa dạng.', 'U nguyên bào ống tủy.']
  line   9828 | Medium      | id 1f7799af360a4c499eb146e8603af2da | D -> U nguyên bào ống tủy.
  line   9834 | Medium      | id 59c00400f823460cad7ae532aade3266 | D -> U nguyên bào ống tủy.

### Group 1077 — topic: Neurology, Neurosurgery
Q: Bệnh nhân nam, 45 tuổi, bị đau đầu âm ỉ vài tháng nay, gần đây xuất hiện nghẹo cổ sang bên phải, khám thấy cơ thang và cơ ức đòn chũm bên trái bị liệt, được chụp cắt lớp vi tính sọ não thấy hình ảnh khối u tầng sọ giữa chèn ép rễ dây thần kinh số XI. Rễ dây thần kinh số XI thoát ra tại vị trí nào?
Options (shared set): ['Rãnh hành cầu', 'Rãnh cầu cuống', 'Rãnh trước trám hành', 'Rãnh sau trám hành']
  line   9838 | Challenging | id 3f5ba99278fe4b16b6285fa5b8e6cb65 | D -> Rãnh sau trám hành
  line   9845 | Challenging | id f60c82247f91405d9da7399637cbed39 | D -> Rãnh sau trám hành
  line   9846 | Challenging | id 945b8286e9964fbc955868636ef42307 | D -> Rãnh sau trám hành

### Group 1078 — topic: Neurology, Neurosurgery, Oncology
Q: BN nữ 50T, bị đau đầu khoảng 1 năm nay. Vào viện tỉnh táo, M 100 l/phút, HA 100/70 mmHg, T 0 370 C. Khám thấy liệt TW ½ mặt bên (P), nói ngọng, nuốt khó, CT Scan có hình ảnh U não. Tổn thương vị trí nào sau đây là phù hợp?
Options (shared set): ['Phần trên hồi đỉnh lên', 'Phần gối bao trong', 'Phần trên hồi trán lên', 'Phần sau bao trong']
  line   9839 | Hard        | id 31636562a2a3469694af43460309b593 | B -> Phần gối bao trong
  line   9847 | Challenging | id c4167cdbe8244b468707efcf1d88e2c0 | B -> Phần gối bao trong

### Group 1079 — topic: Neurology, Neurosurgery
Q: Bệnh nhân nam, 45 tuổi, bị đau đầu âm ỉ vài tháng nay, gần đây xuất hiện nuốt khó, được chụp cắt lớp vi tính sọ não thấy hình ảnh khối u tầng sọ giữa chèn ép rễ dây thần kinh sọ não số IX. Rễ dây thần kinh số IX thoát ra tại vị trí nào?
Options (shared set): ['Rãnh hành cầu', 'Rãnh cầu cuống', 'Rãnh trước trám hành', 'Rãnh sau trám hành']
  line   9840 | Challenging | id 63d6f205f6ca42f38e87a19cb62731c7 | D -> Rãnh sau trám hành
  line   9848 | Challenging | id 32ec4bdd48ef4382974bb9621a4e4a30 | D -> Rãnh sau trám hành

### Group 1080 — topic: Neurology, Neurosurgery
Q: Bệnh nhân nam, 45 tuổi, bị đau đầu âm ỉ vài tháng nay, gần đây xuất hiện lưỡi bị lệch sang bên phải khi thè, được chụp cắt lớp vi tính sọ não thấy hình ảnh khối u tầng sọ giữa chèn ép rễ dây thần kinh sọ não số XII. Rễ dây thần kinh số XII thoát ra tại vị trí nào?
Options (shared set): ['Rãnh hành cầu', 'Rãnh cầu cuống', 'Rãnh trước trám hành', 'Rãnh sau trám hành']
  line   9842 | Challenging | id 73664cc25b674ab6bf7dbd2c59cb3052 | C -> Rãnh trước trám hành
  line   9843 | Challenging | id de6537f3854a4feabae0808fb78422e2 | C -> Rãnh trước trám hành
  line   9850 | Challenging | id e9b7a580224349eaa432b0f750b52173 | C -> Rãnh trước trám hành

### Group 1081 — topic: Pediatrics, Otolaryngology
Q: Viêm VA mạn thường là nguyên nhân viêm tai giữa ở trẻ em đúng hay sai?
Options (shared set): ['Đúng', 'Sai']
  line   9874 | Medium      | id cb4a8ce702444222a08f7d15497aaf5d | A -> Đúng
  line   9924 | Medium      | id 2d1968158ef9423fb6aa0541cd1d69d8 | A -> Đúng

### Group 1082 — topic: Oncology, General Medicine
Q: Câu nào sau đây không đúng trong nguyên tắc phối hợp thuốc hóa chất điều trị ung thư?
Options (shared set): ['Dùng phối hợp các thuốc có cơ chế tác dụng khác nhau,', 'Không phối hợp nhiều thuốc có cùng độc tính trên một cơ quan.', 'Không dùng loại hoá chất mà bản thân nó ít hiệu quả khi dùng đơn độc.', 'Dùng liều cao, từng đợt ngắn, ngắt quãng có hiệu quả tương đương liều thấp kéo dài.']
  line  10168 | Medium      | id 955c8c3556d241c9a9cd1fdeda9e07b1 | D -> Dùng liều cao, từng đợt ngắn, ngắt quãng có hiệu quả tương đương liều thấp kéo dài.
  line  11317 | Easy        | id 6da9776cfc914f4d95d1a12d95f2c102 | D -> Dùng liều cao, từng đợt ngắn, ngắt quãng có hiệu quả tương đương liều thấp kéo dài.

### Group 1083 — topic: Pharmacology, Neurology
Q: Lựa chọn một đáp án đúng:
Options (shared set): ['Pilocarpin kích thích hệ N', 'Nicotin kích thích hệ N', 'Acetylcholin kích thích cả hệ M và N', 'Neostigmin ức chế hệ phó giao cảm']
  line  10177 | Easy        | id 2bdaa40139a74df0a5282a71b51c2c64 | C -> Acetylcholin kích thích cả hệ M và N
  line  11323 | Medium      | id 234faba8fb3f4cb4968a517bd94b4e2b | C -> Acetylcholin kích thích cả hệ M và N

### Group 1084 — topic: Gastroenterology, Hepatology
Q: Cơ chế khởi động chính của phù trong suy gan là:
Options (shared set): ['Tăng áp lực thẩm thấu', 'Giảm áp lực keo', 'Tăng tính thấm thành mạch', 'Cản trở tuần hoàn bạch huyết quanh gan']
  line  10284 | Medium      | id 97255125a2234f27972ae9192d2e6c0e | B -> Giảm áp lực keo
  line  10286 | Medium      | id 7ae4a1ab0e5941f8ab40dbdf43dcba86 | B -> Giảm áp lực keo

### Group 1085 — topic: Gastroenterology, Hepatology
Q: Xét nghiệm máu một bệnh nhân thây Bilirubin kết hợp tăng, phosphatase kiềm bình thường, bệnh nào sau đây là có thê:
Options (shared set): ['Sỏi mật hoặc ung thư mật quản', 'Bệnh Gilbert', 'Bệnh Crigler-Naljar', 'Hội chứng Dubin-Johnson']
  line  10285 | Challenging | id ac74babde3044ec282a4cc983c0a1426 | D -> Hội chứng Dubin-Johnson
  line  10287 | Challenging | id d74ab5f1f1ef4e268f7fc747106b0cb3 | D -> Hội chứng Dubin-Johnson

### Group 1086 — topic: Allergy and Immunology, Emergency Medicine
Q: theoThông tư số 51/2017/TT-BYT hướng dẫn phòng, chẩn đoán và xử trí phản vệ, khi xuất hiện phản vệ đối tượng nào sau đây sẽ xử trí cấp cứu đầu tiên:
Options (shared set): ['Bác sỹ', 'Điều dưỡng', 'Kỹ thuật viên', 'Bất kỳ nhân viên y tế nào phát hiện phản vệ']
  line  10308 | Easy        | id 1bac1137940f4cc8bcd955ec966d2a4b | D -> Bất kỳ nhân viên y tế nào phát hiện phản vệ
  line  10339 | Easy        | id 96151ca3cebe415eaa7a2909ccaefa33 | D -> Bất kỳ nhân viên y tế nào phát hiện phản vệ

### Group 1087 — topic: Gastroenterology, General Medicine
Q: MgSO4 là loại thuốc được dùng đối với bệnh nhân bị bệnh táo bón. Tính pH dung dịch MgSO4 có nồng độ 5.10-6 M?
Options (shared set): ['pH = 7.0', 'pH = 6.26', 'pH = 8.48', 'pH = 7.53']
  line  10574 | Medium      | id 31ff423043d44adfb902b2ba615473e2 | A -> pH = 7.0
  line  10603 | Medium      | id 2cc0baa933184b33ad5458408a287eff | A -> pH = 7.0

### Group 1088 — topic: Periodontology
Q: trong phân loại bệnh quanh răng năm 1999 của AAP, bệnh quanh răng khu trú khi:
Options (shared set): ['trên 20% số răng bị tổn thương', 'dưới 20% số răng bị tổn thương', 'trên 30% số răng bị tổn thương', 'dưới 30% số răng bị tổn thương']
  line  10656 | Easy        | id c5e2179a3f364412be67b894ec2fe247 | D -> dưới 30% số răng bị tổn thương
  line  10664 | Easy        | id 1999d850f16746acaadc569321bc23bd | D -> dưới 30% số răng bị tổn thương

### Group 1089 — topic: Periodontology, Endocrinology
Q: Trong phân loại bệnh quanh răng năm 1999 của AAP, bệnh lợi liên quan nội tiết là:
Options (shared set): ['viêm lợi do uống thuốc tránh thai', 'viêm lợi liên quan đến tuổi dậy thì', 'viêm lợi do thiếu vitamin C', 'viêm lợi do bệnh đái tháo đường']
  line  10657 | Easy        | id 5f69fc31e8c948e3bb46dece594b8df1 | B -> viêm lợi liên quan đến tuổi dậy thì
  line  10693 | Easy        | id 697961aef9dd472abc2cd5177182565c | B -> viêm lợi liên quan đến tuổi dậy thì

### Group 1090 — topic: Periodontology, Infectious Diseases
Q: Enzyme nào của vi khuẩn có khả năng phá huỷ chất nền của dây chằng quanh răng?
Options (shared set): ['Amylase', 'Mucinase', 'Hyaluronidase', 'Dextranase']
  line  10667 | Easy        | id 608b23217e5f4332ba5aef0ba7d40d0d | C -> Hyaluronidase
  line  10718 | Easy        | id f8beccca69ac4f33a6ad8111657af764 | A -> Hyaluronidase

### Group 1091 — topic: Periodontology
Q: Sự khác biệt quan trọng nhất giữa sang chấn mô quanh răng tiên phát và thứ phát là:
Options (shared set): ['Đặc điểm mòn men và ngà răng.', 'Đặc điểm khớp cắn', 'Đặc điểm tiến triển của tổn thương', 'Đặc điểm mô quanh răng']
  line  10686 | Medium      | id 4f4afc942d01484ea68ab165057f69fb | D -> Đặc điểm mô quanh răng
  line  10716 | Medium      | id 7debccf752094f6d8b8f3a9a5166b6c6 | D -> Đặc điểm mô quanh răng
  line  11372 | Medium      | id ea6c1d89e4554ad4a4a465399a777db5 | C -> Đặc điểm tiến triển của tổn thương
  line  11414 | Easy        | id c4717e1884a348ce806060b1a9f88c0e | D -> Đặc điểm mô quanh răng

### Group 1092 — topic: Periodontology
Q: Nguyên nhân có thể gây sang chấn mô quanh răng mạn tính:
Options (shared set): ['Mòn răng và cản trở cắn do phục hình', 'Cản trở cắn do phục hình và cắn phải vật cứng', 'Cản trở cắn do phục hình và di lệch răng thứ phát', 'Mòn răng và di lệch răng thứ phát.']
  line  10687 | Medium      | id 5833585188b84ff99b64eafdcb0572a4 | D -> Mòn răng và di lệch răng thứ phát.
  line  10699 | Medium      | id e8b24788b6264f35bc62a7179f75d7ed | D -> Mòn răng và di lệch răng thứ phát.

### Group 1093 — topic: Periodontology
Q: Nguyên nhân chính gây viêm quanh răng là:
Options (shared set): ['sang chấn khớp cắn', 'mảng bám vi khuẩn', 'thiếu hụt hormone', 'bệnh lý toàn thân']
  line  10690 | Medium      | id 9f78812cef1c4d73a9f90281c15a3b40 | B -> mảng bám vi khuẩn
  line  10709 | Medium      | id 6ff2cdf4be7d446ab7e2c49adc1fd696 | B -> mảng bám vi khuẩn

### Group 1094 — topic: Periodontology, Infectious Diseases
Q: Trong nhóm vi khuẩn bám sớm, loài vi khuẩn nào chiếm ưu thế hơn loài khác:
Options (shared set): ['Neisseria spp', 'Haemophilus spp', 'Streptococcus spp', 'Actinnomyces spp']
  line  10695 | Easy        | id 4e0dfc063a9344b58d26b431dbf3b836 | C -> Streptococcus spp
  line  11393 | Easy        | id 07ff738fdc5e40fb8cbd0f55e0583812 | C -> Streptococcus spp

### Group 1095 — topic: Periodontology
Q: Độ dày của xê măng răng thường có đặc điểm:
Options (shared set): ['dày nhất ở 1/3 chân răng phía chóp và vùng chẽ chân răng', 'dày nhất ở 1/3 chân răng phía cổ răng', 'dày nhất ở 1/3 chân răng phía chóp và mỏng nhất ở vùng chẽ chân răng', 'đồng đều giữa các vị trí']
  line  10703 | Easy        | id a110ea67b7a34aae8240a71bf7b4b264 | A -> dày nhất ở 1/3 chân răng phía chóp và vùng chẽ chân răng
  line  11410 | Easy        | id 3f45085304db4ac7a4aeeadcbc86117a | A -> Dày nhất ở 1/3 chân răng phía chóp và vùng chế chân răng

### Group 1096 — topic: Periodontology, Infectious Diseases
Q: Trong phân loại bệnh quanh răng năm 1999 của AAP, bệnh lợi do vi khuẩn đặc hiệu là:
Options (shared set): ['Viêm lợi liên quan đến rối loạn máu', 'Bệnh lợi chỉ do mảng bám không có yếu tố thuận lợi tại chỗ', 'Bệnh lợi liên quan đến nội tiết', 'Tổn thương lợi không do mảng bám']
  line  10720 | Easy        | id dd7ead92d1f149b1a8f65a869d3c54cd | D -> Tổn thương lợi không do mảng bám
  line  10723 | Easy        | id a18bf959cfdb4c55892fd5a09468f66f | C -> Tổn thương lợi không do mảng bám

### Group 1097 — topic: Periodontology, Pathology
Q: Đặc điểm khoảng gian bào của biểu mô nối trong vùng quanh răng?
Options (shared set): ['Khoảng gian bào chiếm khoảng 5% thể tích biểu mô', 'Khoảng gian bào chiếm khoảng 8% thể tích biểu mô', 'Khoảng gian bào chiếm khoảng 15% thể tích biểu mô', 'Khoảng gian bào chiếm khoảng 18% thể tích biểu mô']
  line  10726 | Easy        | id 097dfa27b2ec4f2f8ff90585732a93c0 | D -> Khoảng gian bào chiếm khoảng 18% thể tích biểu mô
  line  11441 | Easy        | id 026d27e6ae694ae29b2058a1fd21e161 | C -> khoảng gian bào chiếm khoảng 15% thể tích biểu mô

### Group 1098 — topic: Geriatrics, Obstetrics and Gynecology
Q: Tuổi trung bình của thời kỳ mãn kinh:
Options (shared set): ['Từ 40 – 45 tuổi.', 'Từ 45 – 50 tuổi.', 'Từ 40 – 50 tuổi.', 'Từ 45 – 55 tuổi.']
  line  10742 | Easy        | id a231788f365644af85fe42dcafcc8412 | D -> Từ 45 – 55 tuổi.
  line  10815 | Easy        | id 9a90b5beb016491d9e5aad0ba511c972 | D -> Từ 45 – 55 tuổi.

### Group 1099 — topic: Geriatrics, General Medicine
Q: Công ty dược A nhận định sản xuất sản phẩm của mình phục vụ đối tượng người cao tuổi, cách phân khúc thị trường này giúp doanh nghiệp nhận ra những cơ hội kinh doanh và lựa chọn được:
Options (shared set): ['Thị trường mục tiêu', 'Thị trường', 'Dự báo nhu cầu thị trường', 'Tập khách hàng của thị trường']
  line  10796 | Medium      | id bb65d1884c204714825e9c97628b3229 | A -> Thị trường mục tiêu
  line  10814 | Challenging | id d6c3e08d7e6345c6a4ed56c514436485 | A -> Thị trường mục tiêu

### Group 1100 — topic: Anesthesiology
Q: Thuốc gây mê đường tĩnh mạch là:
Options (shared set): ['Ether', 'Di nitrogen oxyd', 'Ketamin', 'Halothan']
  line  10837 | Easy        | id 003dbef5f4234478b92563e1bd52f211 | C -> Ketamin
  line  10902 | Easy        | id 0940a4a362a04a99bd0790e7ef8bf7c2 | C -> Ketamin

### Group 1101 — topic: Anesthesiology, Obstetrics and Gynecology
Q: Sau khi được chuyển từ phòng hồi sức về khoa, trong ngày hậu phẫu đầu tiên dấu hiệu sinh tồn của sản phụ được theo dõi mấy giờ 1 lần:
Options (shared set): ['Mỗi 1 giờ/lần', 'Mỗi 2 giờ/lần', 'Mỗi 4 giờ/lần', 'Mỗi 6 giờ/lần']
  line  10856 | Easy        | id 0be365a3754d4cd3934e9dcdc2f39ffe | C -> Mỗi 4 giờ/lần
  line  10885 | Easy        | id c9e9ed4cfcf64c3ebc87d6dd999a34bc | C -> Mỗi 4 giờ/lần

### Group 1102 — topic: Anesthesiology, Pharmacology, Pulmonology
Q: Trường hợp nào có thể dùng thuốc ketamin để gây mê là:
Options (shared set): ['Roi loạn tâm thần', 'Suy hô hấp', 'Tăng huyết áp', 'Phù não']
  line  10880 | Medium      | id 16cc211a279d43dc9761db18f84c23f7 | B -> Suy hô hấp
  line  10892 | Medium      | id 62bd3b8d5e5b4e168184562e87e1730d | B -> Suy hô hấp

### Group 1103 — topic: Vascular Surgery
Q: Vị trí giãn tĩnh mạch thường gặp nhất là tĩnh mạch hiển lớn?
Options (shared set): ['Đúng', 'Sai']
  line  11030 | Easy        | id f83bd4c503294e14a02eb47c5ac47697 | A -> Đúng
  line  11052 | Easy        | id 64d7c012990c43e6b3fc9803516ab475 | A -> Đúng

### Group 1104 — topic: Vascular Surgery
Q: Nguyên nhân chủ yếu của giãn tĩnh mạch chi dưới là do mất cơ năng của valve tĩnh mạch hiển lớn?
Options (shared set): ['Đúng', 'Sai']
  line  11031 | Medium      | id feed57b500de4355981f86ec34091d0b | B -> Sai
  line  11053 | Medium      | id 52032c872f514459acaaaf5f93eff115 | B -> Sai

### Group 1105 — topic: Dentistry
Q: tiêu xương ổ răng do sang chấn khớp cắn là tiêu xương
Options (shared set): ['ngang', 'chéo', 'tạo khuyết xương dạng nang', 'tạo khuyết xương trên bề mặt xương vỏ']
  line  11390 | Medium      | id f5866d8529014b2892bec9dfa19c6685 | D -> tạo khuyết xương trên bề mặt xương vỏ
  line  11407 | Easy        | id 11f7dea16a5542a093c469f41ab1eafe | B -> Chéo

### Group 1106 — topic: Nephrology, Vascular Medicine
Q: Bệnh nhân nam, 20 tuổi, đến khám vì đau chân phải. Tiền căn hội chứng thận hư lần đầu được chẩn đoán cách 1 tháng đang điều trị với prednisone 5mg, 10 viên/ngày. Huyết áp 120/70mmHg, mạch 80 lần/phút, nhiệt độ 370C, khám chân phải phù hơn chân trái, đỏ nhẹ từ ngón chân đến đùi, mềm, ấn đau, không nóng, không rỉ dịch, không mủ, không sốt. Biến chứng nào sau đây phù hợp nhất với bệnh cảnh lâm sàng?
Options (shared set): ['Viêm mô tế bào', 'Huyết khối tĩnh mạch sâu', 'Xơ vữa động mạch', 'Tắc mạch bạch huyết']
  line  11515 | Challenging | id 9e46723f44014a6e9483be63fee87d56 | B -> Huyết khối tĩnh mạch sâu
  line  11516 | Challenging | id eb3ea20464d54d54baa7ec7918a6c390 | B -> Huyết khối tĩnh mạch sâu

### Group 1107 — topic: Genetics
Q: Trong quá trình nhân đôi ADN, các đoạn Okazaki được nối lại với nhau thành mạch liên tục nhờ enzim nối, enzim nối đó là
Options (shared set): ['ADN giraza', 'ADN pôlimeraza', 'hêlicaza', 'ADN ligaza']
  line  11539 | Easy        | id 15cdb1e86579493b94b88e5c6733e529 | D -> ADN ligaza
  line  11585 | Easy        | id d46964f257ec4d0d8c2f2ef0c956172c | D -> ADN ligaza

### Group 1108 — topic: Ophthalmology
Q: Nguyên nhân gây nhãn viêm đồng cảm thường gặp nhất do:
Options (shared set): ['Xuất huyết tiền phòng.', 'Phòi tổ chức nội nhãn.', 'Vết thương xuyên thủng nhãn cầu.', 'Biến chứng thấm máu giác mạc .']
  line  11596 | Easy        | id bff73679f577476ca579fdc982056592 | C -> Vết thương xuyên thủng nhãn cầu.
  line  11630 | Easy        | id d8903654f7874994a4416e87f4e03a84 | C -> Vết thương xuyên thủng nhãn cầu.

### Group 1109 — topic: Pharmacology, Ophthalmology
Q: Corticoid chống chỉ định trong bệnh:
Options (shared set): ['Viêm loét giác mạc do herpes', 'Viêm màng bồ đào', 'Viêm tuyến lệ', 'Viêm giác mạc hình đĩa']
  line  11609 | Medium      | id 90180f110bae4c7dbee0d20ef1e5c1e6 | A -> Viêm loét giác mạc do herpes
  line  11622 | Easy        | id 416685cdc8e94ac0bbc28a1833ce2e0c | B -> Viêm loét giác mạc do herpes

### Group 1110 — topic: Toxicology, Forensic Medicine
Q: Khi ngộ độc nặng khí CO, nếu chết tử thi có biểu hiện nào sau đây ?
Options (shared set): ['Môi đỏ, Có những vết đỏ thắm ở đùi và bụng', 'Môi đỏ, Có những vết đỏ thắm ở cổ và cánh tay', 'Môi tím, Có những vết đỏ thắm ở cổ và cánh tay', 'Môi tím, Có những vết đỏ thắm ở đùi và bụng']
  line  11957 | Medium      | id b0b896a4b384451e85ee1622a8d24a61 | B -> Môi đỏ, Có những vết đỏ thắm ở cổ và cánh tay
  line  11960 | Medium      | id 3767da0163a44940965b74c1b59b6d11 | B -> Môi đỏ, Có những vết đỏ thắm ở cổ và cánh tay

### Group 1111 — topic: Analytical Chemistry
Q: Trong phản ứng Parris, Barbiturat tạo phức có màu gì với cobalt nitrat và
dietylamin trong methanol:
Options (shared set): ['Màu xanh ve', 'Màu hồng', 'Màu nâu nhạt', 'Màu trắng ngả sang xám']
  line  11962 | Easy        | id 747429d510ff432796a01833116d5d63 | A -> Màu xanh ve
  line  11988 | Medium      | id e4770533a10f4f0f838acfeb89cd46c1 | A -> Màu xanh ve

### Group 1112 — topic: Physical Medicine and Rehabilitation, Sports Medicine
Q: Vận động trị liệu gồm, Ngoại Trừ
Options (shared set): ['Tập kéo dãn', 'Tập kháng trở', 'Tập chống đẩy', 'Tập chủ động']
  line  12114 | Easy        | id 03f017be1a6443c6b619316378a57c13 | C -> Tập chống đẩy
  line  12141 | Easy        | id 4ca14084ffc8448fb6d6f0b9a3f3fc7d | C -> Tập chống đẩy

### Group 1113 — topic: Physical Medicine and Rehabilitation, Sports Medicine
Q: Tập mạnh cơ giai đoạn mạnh tính chấn thương mô mềm làm như thế nào?
Options (shared set): ['kháng trở', 'đẳng trương', 'tập vận động bình thường', 'hạn chế tập vận động']
  line  12144 | Medium      | id f84d37dca9ca4d828791e802d21f9d27 | A -> kháng trở
  line  12160 | Medium      | id b585c99d8bdf4e3fbf1e3900af925f83 | A -> Kháng trở

### Group 1114 — topic: Physical Medicine and Rehabilitation, Nursing
Q: Vai trò của điều dưỡng trong phục hồi chức năng, ngoại trừ:
Options (shared set): ['Chăm sóc toàn diện, giáo dục sức khỏe cho bệnh nhân.', 'Hướng dẫn bệnh nhân và người thân cách tập cho bệnh nhân đi lại', 'Hướng dẫn bệnh nhân cách tự chăm sóc', 'Hướng dẫn người thân, người chăm nuôi cách chăm sóc cho bệnh nhân']
  line  12217 | Medium      | id cb17edffc4e345f5abcba2f5a2ea637c | B -> Hướng dẫn bệnh nhân và người thân cách tập cho bệnh nhân đi lại
  line  12228 | Medium      | id 434bf55e376e46a3af7705a94368852d | B -> Hướng dẫn bệnh nhân và người thân cách tập cho bệnh nhân đi lại

### Group 1115 — topic: Nursing, General Medicine
Q: Khi dùng thuốc cho người bênh, điều dưỡng viên phải:
Options (shared set): ['Thực hiện theo “2 đúng”', 'Thực hiện theo “3 đúng”', 'Thực hiện theo “4 đúng”', 'Thực hiện theo “5 đúng”']
  line  12219 | Easy        | id edd0df47d94f41b189e2fb3934848bed | D -> Thực hiện theo “5 đúng”
  line  12230 | Easy        | id aa3b4a781f45458c99b5580f85d35a49 | D -> Thực hiện theo “5 đúng”

### Group 1116 — topic: Nursing, Psychiatry
Q: Để giao tiếp có hiệu quả, trước hết điều dưỡng viên cần phải xác định :
Options (shared set): ['Đối tượng giao tiếp', 'Thời gian giao tiếp', 'Địa điểm giao tiếp', 'Hình thức giao tiếp']
  line  12222 | Easy        | id d12e0d63f30a4cbca2efc24f4d8e5a54 | A -> Đối tượng giao tiếp
  line  12231 | Medium      | id ec7da25b538e4fc9aa95dfd1bca6c62d | A -> Đối tượng giao tiếp

### Group 1117 — topic: Nursing, General Medicine
Q: Trực tiếp thực hiện cho người bệnh ăn qua ống thông phải là:
Options (shared set): ['Điều dưỡng viên, hộ sinh viên', 'Bác sĩ điều trị', 'Người nhà người bệnh', 'Điều dưỡng viên']
  line  12227 | Easy        | id d8a40c53838a4740889a86d680c4dcdf | D -> Điều dưỡng viên
  line  12232 | Easy        | id 76333cb9b93d4d66b2156b8357cedc0e | D -> Điều dưỡng viên

### Group 1118 — topic: Toxicology, Diagnosis
Q: Lấy gì để xác định sự ngộ độc của NO và NO2
Options (shared set): ['Máu', 'Dịch tụy', 'Nước tiểu', 'Cả 3 ý trên']
  line  12235 | Medium      | id 05a93287fd8b45d494b0dec86bb0fef2 | D -> Cả 3 ý trên
  line  12470 | Easy        | id c158c470bb4140a9a59ac1458b467d26 | D -> Cả 3 ý trên

### Group 1119 — topic: Palliative Medicine
Q: Trên cùng một bệnh nhân có thể dùng đồng thời nhiều nhóm thuốc giảm đau
Options (shared set): ['Đúng', 'Sai']
  line  12241 | Easy        | id b2a4eb68598a456ab064344512ed2f24 | A -> Đúng
  line  12322 | Easy        | id b711b751abf640fa9faf2489d9a4f71d | A -> Đúng

### Group 1120 — topic: Oncology, Palliative Medicine
Q: Bệnh nhân ung thư cần được đánh giá đau và kiểm soát đau vào thời điểm nào là tốt nhất?
Options (shared set): ['Ngay từ khi được chẩn đoán bệnh.', 'Sau khi được điều trị bằng các biện pháp đặc hiệu,', 'Khi bệnh được chẩn đoán ở giai đoạn cuối.']
  line  12243 | Medium      | id b2f32ca9b1624f7985e0fa8c2c03c73f | A -> Ngay từ khi được chẩn đoán bệnh.
  line  12256 | Easy        | id 1fcb6a09eff34276acff662656bcea66 | A -> Ngay từ khi được chẩn đoán bệnh.

### Group 1121 — topic: Oncology, Palliative Medicine
Q: Đau trong ung thư xuất hiện do những yếu tố nào?
Options (shared set): ['Xâm lấn vào xương, thần kinh, phần mềm, tạng.', 'Viêm xung quanh u, loét da.', 'Biện pháp điều trị ung thư như mổ lổng ngực, xạ trị.', 'Tất cả các phương án đều đúng.']
  line  12247 | Medium      | id c357da0e98bc400aa1eea73648a9023f | D -> Tất cả các phương án đều đúng.
  line  12250 | Medium      | id 49ee8bc0e8064e6cbf321d3530aace62 | D -> Tất cả các phương án đều đúng.

### Group 1122 — topic: Neurology, Palliative Medicine
Q: Loại đau gọi là đau loạn cảm hay đau lạc đường dẫn truyền vào trung tâm thường gặp do yếu tố nào?
Options (shared set): ['Chấn thương các thần kinh ngoại vi.', 'Sự lo lắng, hoảng hốt và yếu tố xã hội.', 'Bị chèn ép hoặc bít tắc tạng.', 'Tất cả các phương án đều sai.']
  line  12253 | Medium      | id c6dacca358e74b39bf15fb803724ba36 | A -> Chấn thương các thần kinh ngoại vi.
  line  12335 | Medium      | id ac20b7b9e8dd4f64b7b213632952c9b4 | A -> Chấn thương các thần kinh ngoại vi.

### Group 1123 — topic: Palliative Medicine, General Medicine
Q: Thuốc nào sau đây có thời gian khống chế cơn đau cao nhất?
Options (shared set): ['Codein', 'Morphine (time-release) (MS Contin)', 'Methadone', 'Levorphanol']
  line  12273 | Medium      | id 35a827edd9f140c5894be547281942c3 | D -> Levorphanol
  line  12298 | Medium      | id 84a1834026294ee18659efb995b2d621 | C -> Methadone

### Group 1124 — topic: Palliative Medicine, General Medicine
Q: Thang điểm đau VAS có tối đa bao nhiêu điểm?
Options (shared set): ['5', '10', '7', '9']
  line  12277 | Easy        | id cb28ed0325fa4a96b18f9d293a3f26ce | B -> 10
  line  12304 | Easy        | id 0d01094e678d4d808b2417c3c0f63db3 | B -> 10

### Group 1125 — topic: Psychiatry, General Medicine
Q: Đối tượng nghiên cứu của tâm lý học y học bao gồm các nội dung sau, NGOẠI TRỪ:
Options (shared set): ['Nhân cách bệnh nhân', 'Hệ thống tổ chức bệnh viện', 'Nhân cách của người cán bộ y tế', 'Mối quan hệ giữa thầy thuốc và bệnh nhân']
  line  12382 | Easy        | id 6bdeac9f69744551966250fe313f448f | B -> Hệ thống tổ chức bệnh viện
  line  12401 | Easy        | id 7d370f400ee34626bf4713c26f24fd22 | B -> Hệ thống tổ chức bệnh viện


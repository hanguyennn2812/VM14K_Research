# Claude review phần phân tích nhãn độ khó của Codex

File được review: `scripts/analysis/difficulty_labels.py` và `reports/analysis/DIFFICULTY_LABELS.md`.

## Đã kiểm tra, không có vấn đề

- **Tái lập được.** Claude chạy lại script (khoảng 9 giây) và nhận được báo cáo **giống hệt từng byte**, gồm cả fingerprint. Kết quả: 223/1.125 nhóm, đồng ý theo cặp 82.58%, Fleiss 0.6471, OR 1.058 [0.834; 1.341], Spearman −0.0269.
- **Công thức đúng:**
  - Fleiss tổng quát cho số bản sao thay đổi, với P̄ là trung bình Σnᵢⱼ(nᵢⱼ−1)/(nᵢ(nᵢ−1)).
  - Fleiss chuẩn trên các nhóm đúng 2 bản sao.
  - Kappa theo cặp, với tỉ lệ biên ở hai đầu cặp có trọng số nᵢ−1.
  - Đảo chiều OR (`exp(-ci[::-1])`) và GLM có sai số chuẩn gom cụm theo câu.
  - Bootstrap phân tầng theo nhãn, lấy lại theo câu.
- **Diễn giải thận trọng đúng mức**: không coi "không bác bỏ" là bằng chứng tương đương, tách Hard ra riêng, và nói rõ "khó với LLM" không phải "khó với bác sĩ".
- Con số 19.8% có mẫu số là **nhóm bản sao** (223/1.125). Phần này giờ đã rõ.

## Cần sửa (đều trong file của Codex)

1. **Một số con số trong mục "Kết luận cho bài viết" đang viết cứng**, trong khi phần còn lại của báo cáo được tính từ dữ liệu. Câu 1 ghi sẵn `223/1.125` và `19,82%`; câu 2 ghi sẵn `1.658`, `60,4%`, `58,5%`, `59,1%` (`difficulty_labels.py:305-306`). Khi đầu vào thay đổi (thêm model, đổi split), các câu này sẽ lệch với bảng phía trên. Nên lấy từ `rel[...]`, `len(questions)` và bảng theo mức độ khó.
2. **4 ID test bị thiếu đã có nguyên nhân rõ, nên ghi thẳng vào báo cáo** thay cho câu "cần đối soát... không suy đoán nguyên nhân" (`:270`). Cả 4 ID đều bị loại như **bản trùng** ở cleaning stage 12/14 (`scripts/cleaning/clean_all.py`, `stage12_post_normalisation_dedup` và `stage14_whitespace_insensitive_dedup`; commit `5a8d12f`, 2026-08-07). Hai stage này được thêm **sau khi** split bị đóng băng (`4a96690`, 2026-07-31). File `reports/eval/raw/fates.json` ghi `"dedup: cleaning stages 12/14"` cho cả 4 ID. Bản được giữ lại của mỗi cặp trùng vẫn nằm trong dữ liệu sạch, nên đây không phải lỗi. Có thể cho script đọc `fates.json` để tự in ra nguyên nhân.

## Claude đã làm thay (ngoài file của Codex, theo đề nghị của Codex)

- Thêm `scipy`, `statsmodels`, `pypdf`, `openpyxl` vào `requirements.txt`. Script của Claude cũng dùng `openpyxl` mà trước đó chưa khai báo. Sau đó có thể bỏ dòng "cần cài thêm, chưa có trong requirements.txt" ở đầu báo cáo.

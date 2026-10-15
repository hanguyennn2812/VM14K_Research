# Jev và "System One models": là gì, ứng dụng gì cho AI và y tế

*Soạn 2026-10-15 cho việc số 5 của buổi họp 02/10 ("đọc tài liệu Jev"). Mọi con số đều có nguồn ở cuối
bài, đánh số [1]–[14]. Số liệu do nhà sản xuất tự công bố được ghi rõ là "theo TypeSafe". Mục 6 là phần
nhóm tự đo trên VM14K.*

---

## 0. Tóm tắt một phút

- **Jev** là model đầu tiên của TypeSafe AI, ra mắt tháng 9/2026, thuộc một lớp model mà họ gọi là
  **System One** [1]. Jev **không sinh văn bản**. Nó nhận một "state" (văn bản hoặc JSON) cùng một số câu
  hỏi có kiểu dữ liệu định sẵn, rồi trả về **quyết định kèm xác suất**: chọn một phương án (Choice),
  chấm điểm theo thang (Score), hoặc xác suất một mệnh đề là đúng (Noul) [1][3].
- Tên gọi lấy từ "Hệ thống 1" (nhanh, trực giác) trong *Thinking, Fast and Slow* của Kahneman [4].
  Trong ví von này, LLM có suy luận đóng vai "Hệ thống 2" (chậm, cân nhắc).
- **Theo TypeSafe:** độ trễ 70–500 ms, nhanh hơn LLM 40–200 lần trên các tác vụ dạng phân loại, giá
  input 0,042 USD/1 triệu token [1]. **Đánh giá độc lập** (ĐH Bonn, arXiv 2609.37647, 37 bộ dữ liệu) [5]:
  MMLU 91,8%, cao hơn Qwen3.8-27B (81,7%); xác suất **hiệu chỉnh tốt**, ECE 0,028 (Qwen 0,063);
  0,36 giây/request; chạy 346.009 request hết 9,15 USD. Tuy vậy, cả ba model đều yếu hơn với ngôn ngữ ít
  tài nguyên, nhãn nhiễu và chấm theo rubric. Bài này **không có bộ dữ liệu y khoa nào**.
- **"Harness"** là phần code bao quanh model: vòng lặp agent, quản lý state, gắn tool, middleware.
  LangChain dùng Jev làm hai middleware: chọn model cho từng yêu cầu (router) và chặn tool call nguy
  hiểm (guardrail) [2]. Browser Use dùng Jev để chọn thao tác cho agent trình duyệt [6].
- **Với y tế**, giá trị nằm ở các quyết định nhỏ, lặp nhiều và cần biết khi nào không chắc: phân loại và
  chuyển tuyến tin nhắn bệnh nhân, sàng lọc hồ sơ theo từng tiêu chí, chặn câu trả lời rủi ro, và
  **chuyển ca khó lên model lớn hoặc bác sĩ khi độ tin cậy thấp**. Jev không giải thích được lý do,
  là dịch vụ đóng ở nước ngoài, và chưa được kiểm chứng trên dữ liệu y khoa hay tiếng Việt.
- **Với VM14K:** một câu trắc nghiệm chính là một câu hỏi Choice. Mục 6 cho thấy ý tưởng "trả lời nhanh
  kèm xác suất, không chắc thì chuyển lên model mạnh" đo được ngay trên tập test của nhóm.

---

## 1. Jev là gì

### 1.1 Khác LLM ở đâu

| | LLM (GPT, Qwen, DeepSeek…) | System One model (Jev) |
|---|---|---|
| Đầu ra | Chuỗi văn bản, sinh từng token một | Giá trị có kiểu (lựa chọn, điểm, xác suất), sinh trong **một lượt** [1] |
| Lỗi định dạng | Có thể trả sai định dạng, phải parse | Theo TypeSafe là "never makes type errors", vì đầu ra bị ràng buộc bởi schema [1]. Đây là tính chất thiết kế, không phải số đo |
| Xác suất | Phải tự rút từ logit, thường hiệu chỉnh kém | Trả sẵn xác suất cho từng phương án kèm `confidence` [3][7] |
| Giải thích | Có | **Không.** Jev không viết câu trả lời và không giải thích lập luận [3] |
| Huấn luyện | RLHF, RLVR | **RLCD** (Reinforcement Learning for Calibrated Decisions): tối ưu cho quyết định có xác suất đúng mức, thay vì cho sở thích người chấm hay đáp án kiểm chứng được [1][8] |

### 1.2 Ba "primitive"

| Primitive | Câu hỏi | Trả về | Ví dụ |
|---|---|---|---|
| **Choice** | Chọn một trong các phương án | `choice`, `probabilities`, `confidence` | Ticket này chuyển cho bộ phận nào? |
| **Score** | Chấm theo thang có thứ tự | `score` (số thực), phân phối, `confidence` | Mức bực bội của khách từ 0 đến 2 → 1,4 |
| **Noul** | Mệnh đề này đúng không? | `noul` ∈ [0, 1] | Tin nhắn có yêu cầu hoàn tiền không → 0,95 |

Nguồn: tài liệu TypeSafe [3][19]. Nhiều câu hỏi được gửi chung một request và **chạy song song, độc lập
với nhau** trên cùng một state. Theo TypeSafe, thêm câu hỏi gần như không làm tăng thời gian phản hồi và
không gây "context rot" [3].

**Cách dùng được khuyến nghị:** tách một phán đoán phức tạp thành nhiều câu hỏi nhỏ, rồi ghép kết quả
bằng code thường. Khi ưu tiên thay đổi thì "change a coefficient in your code rather than rewriting a
prompt" [3].

### 1.3 Confidence và calibration

- **Calibration** (hiệu chỉnh) nghĩa là trong tất cả các câu model báo xác suất 0,8, khoảng 80% phải
  đúng. TypeSafe tự lưu ý rằng đây là tính chất **của cả nhóm dự đoán, không bảo đảm cho từng câu** [8].
- `confidence` là một con số từ 0 đến 1, tóm tắt mức tập trung của phân phối xác suất. TypeSafe đề xuất
  chia ba vùng: cao thì tự động làm, vừa thì xin xác nhận, thấp thì không làm mà **chuyển cho người hoặc
  hệ thống khác**. Ngưỡng do người dùng tự chỉnh theo lĩnh vực và theo mức rủi ro [7].
- Thước đo chuẩn là **ECE** (Expected Calibration Error) [10]. Bài toán "chỉ trả lời khi đủ chắc" gọi là
  **selective prediction** [11].

---

## 2. Số liệu: nhà sản xuất nói gì, đánh giá độc lập đo được gì

| Chỉ số | Theo TypeSafe [1] | Đánh giá độc lập, ĐH Bonn [5] |
|---|---|---|
| Độ trễ | 70–500 ms, so với 3–329 s của model frontier | 0,36 s/request, tính cả mạng |
| Chi phí | 0,042 USD/1M token input; output "too cheap to meter" | 346.009 request, 217,9M token: **9,15 USD** |
| Độ chính xác | "Similar levels of intelligence on System One tasks" | MMLU **91,8%** (Qwen3.8-27B 81,7%, Gemma-4-E4B 67,4%); IMDB, SST-2, HellaSwag, ARC 95–99%; Belebele 86,7% trên 122 ngôn ngữ (trung vị 91,1%) |
| So sánh | Nhanh hơn 193,6 lần, rẻ hơn 444,6 lần trên các workflow mẫu, mức "on the higher end" | Thắng Qwen3.8-27B ở 27/37 bộ, không lần thua nào vượt ngoài khoảng bootstrap; thắng Gemma-4-E4B cả 37/37 |
| Calibration | Có xác suất hiệu chỉnh | Choice ECE **0,028** (Qwen 0,063, Gemma 0,208); Noul ECE 0,052 (Qwen 0,113). Ví dụ selective prediction: SIB-200 từ 81,5% lên 98,2% khi chỉ trả lời 50% câu chắc nhất |
| Giới hạn | Choice tối đa 255 phương án; số phương án lớn phải chạy hai bước nên chậm hơn | Yếu với ngôn ngữ ít tài nguyên, nhãn chi tiết hoặc nhiễu, chấm theo rubric. Ngưỡng 0,5 cho câu nhị phân đặt sai chỗ: chỉnh ngưỡng nâng micro-F1 của UNFAIR-ToS từ 0,50 lên 0,75 |
| Kiểm tra học vẹt | | Đảo thứ tự phương án thì accuracy không đổi; bỏ câu hỏi thì về gần ngẫu nhiên. Chưa loại trừ được việc đã thuộc cặp câu hỏi–đáp án |

**Cần lưu ý:**
- Đáp án chuẩn trong benchmark workflow của TypeSafe là đáp án đồng thuận của GPT-6 Astra và Fable 5.1,
  tức "đồng ý với model khác" chứ không phải đúng theo chuyên gia. Chính TypeSafe ghi nhận điều này [1].
- Bài của Bonn [5] chỉ thử phiên bản jev-1.13.0, một prompt cho mỗi bộ dữ liệu, chạy một lần, và so với
  model mở ở chế độ không suy luận. **Không có bộ dữ liệu y khoa nào**, và văn bản không nêu riêng kết quả
  tiếng Việt (chỉ có trong hình của Belebele).

---

## 3. "Harness" và ba cách người ta đang dùng Jev

**Harness** là phần code quanh model: chạy vòng lặp agent, giữ state, gắn tool và middleware. LangChain
không định nghĩa từ này trong bài, nhưng hai ví dụ của họ đều là middleware chèn vào vòng lặp đó [2].

1. **Router chọn model** (`ModelRouterMiddleware`, LangChain [2]): Jev đọc tin nhắn mới nhất và chọn model
   theo tiêu chí do mình đặt, chẳng hạn câu tra cứu thì dùng model rẻ, câu thiết kế kiến trúc thì dùng
   model mạnh. Xác suất và confidence được giữ trong state của agent để code phía sau dùng tiếp.
2. **Guardrail cho tool call** (`AutoModeMiddleware` [2]): Jev phân loại một lệnh, ví dụ `bash`, là nguy
   hiểm hay không, và chặn trước khi chạy. Cả hai middleware còn nằm trong nhánh `experimental`.
3. **Agent trình duyệt** (Browser Use, `jev-ultrafast`, giấy phép MIT [6]): mỗi bước, trang web được biến
   thành bảng phần tử có đánh số. Jev chọn **thao tác và phần tử cùng lúc trong một request**, và chỉ khi
   phải gõ chữ mới gọi một LLM nhỏ. Kết quả từ chính repo: tác vụ đặt vé Google Flights giảm trung vị từ
   9,45 s xuống 7,09 s (−25%), số lệnh gọi trình duyệt từ 1.092 xuống 101. Repo nói rõ đây là "three
   repeats of one task on one browser profile, not a general reliability benchmark".
   Một nguyên tắc thiết kế đáng học: đầu ra của model **không bao giờ** trở thành selector, toạ độ, lệnh
   shell hay JavaScript. Mọi mục tiêu đều phải trỏ về một phần tử đã quan sát thấy, và lựa chọn `DONE`
   vẫn phải được kiểm tra độc lập [6].

**Điểm chung:** LLM lo phần cần sinh chữ và suy luận dài. Các quyết định nhỏ, lặp lại, cần nhanh và cần
biết mức chắc chắn thì giao cho System One. Ý tưởng chọn model theo từng câu hỏi để giảm chi phí đã có
trước Jev, ví dụ RouteLLM [13]. Cái mới của Jev là router được huấn luyện riêng cho việc ra quyết định có
xác suất hiệu chỉnh.

---

## 4. Ứng dụng trong AI nói chung

| Ứng dụng | Câu hỏi cho Jev | Vì sao hợp |
|---|---|---|
| "Smart if-statement" trong pipeline | Noul: "tài liệu này có phải hoá đơn không?" | Kiểu dữ liệu cố định, không cần parse |
| Router cho agent | Choice: model nào, tool nào | Một request, < 0,5 s, có confidence để quyết định leo thang |
| Guardrail và phát hiện jailbreak | Noul: "lệnh này có xoá dữ liệu không?" | Rẻ nên kiểm tra được mọi bước |
| Map-reduce trên kho dữ liệu lớn | Choice/Score cho hàng trăm nghìn bản ghi | Bonn chạy 346 nghìn request hết 9 USD [5] |
| Gán nhãn trước, người duyệt sau | Choice kèm confidence | Chỉ đưa câu confidence thấp cho người |

---

## 5. Ứng dụng trong y tế: có thể làm gì, và phải cẩn thận ở đâu

### 5.1 Các ứng dụng hợp lý

1. **Phân loại và chuyển tuyến tin nhắn bệnh nhân.** Đây là bài toán Choice và Noul điển hình: khẩn hay
   không, gửi cho khoa nào, cần bác sĩ hay điều dưỡng. Đã có nghiên cứu dùng LLM tinh chỉnh cho việc này,
   ví dụ GPT-4o tinh chỉnh đạt 97,5% accuracy khi phát hiện tin khẩn trong tin nhắn ngoại trú [14].
   Một System One model rẻ và nhanh hơn, và có xác suất để đặt ngưỡng **ưu tiên độ nhạy** (không bỏ sót
   ca khẩn).
2. **Sàng lọc hồ sơ theo từng tiêu chí.** TrialGPT (Nature Communications, 2024) chấm bệnh nhân theo từng
   tiêu chí tuyển chọn của thử nghiệm lâm sàng, đạt 87,3% trên 1.015 cặp bệnh nhân–tiêu chí, và giảm 42,6%
   thời gian sàng lọc [15]. Cách làm "mỗi tiêu chí là một câu hỏi Noul độc lập, ghép lại bằng code" trùng
   đúng với hướng dẫn thiết kế của Jev [3].
3. **Guardrail cho chatbot y tế.** Trước khi câu trả lời đến tay bệnh nhân, hỏi các câu Noul như "có nêu
   liều thuốc không?", "có dấu hiệu cấp cứu cần chuyển người không?". Lưu ý: guardrail này cũng có thể
   sai, nên cần đo độ nhạy trên dữ liệu thật.
4. **Biết khi nào không trả lời (abstention).** MedAbstain (2026) cho thấy nhiều LLM có accuracy cao vẫn
   **không biết bỏ qua** câu nên bỏ qua, và việc tăng kích thước model hay prompting tốt hơn cải thiện rất
   ít [16]. Xác suất hiệu chỉnh tốt là điều kiện cần cho một quy trình kiểu "chắc thì làm, không chắc thì
   chuyển bác sĩ".
5. **Chuyển ca khó lên model lớn hoặc lên người.** Model nhanh xử lý phần lớn câu hỏi, các câu có
   confidence thấp mới được gửi lên LLM suy luận hoặc bác sĩ. Mục 6 đo chính ý tưởng này trên VM14K.

### 5.2 Rủi ro và giới hạn

- **Chưa có bằng chứng trên dữ liệu y khoa.** Bài đánh giá độc lập duy nhất không có bộ y khoa nào [5].
  Benchmark của TypeSafe chấm theo đồng thuận của model khác, không theo chuyên gia [1].
- **Không giải thích được.** Lâm sàng thường cần biết *vì sao*, mà Jev không có lập luận để bác sĩ kiểm
  tra. Vì vậy chỉ nên dùng Jev cho bước lọc hoặc chuyển tuyến, không dùng cho kết luận.
- **Calibration không bảo đảm cho từng ca** [8]. Một ca sai với confidence 0,99 vẫn có thể xảy ra, nên
  phải đo độ nhạy và đặt ngưỡng trên dữ liệu của chính mình [7].
- **Quyền riêng tư.** Jev là API đóng ở nước ngoài. Ở Việt Nam, dữ liệu sức khoẻ là dữ liệu cá nhân nhạy
  cảm theo Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 (hiệu lực 01/01/2026) và Nghị định 356/2025/NĐ-CP
  [17]. Gửi hồ sơ bệnh nhân thật lên API cần cơ sở pháp lý và khử định danh.
- **Tiếng Việt chưa được kiểm chứng riêng.** Kết quả 122 ngôn ngữ chỉ là trung bình; bài Bonn ghi nhận độ
  chính xác giảm với ngôn ngữ ít tài nguyên [5].
- **Phụ thuộc nhà cung cấp:** phiên bản model có thể đổi, giá mới ở giai đoạn early access [1].

---

## 6. Bằng chứng trên VM14K: ý tưởng System One đo được ngay

Nhóm chưa có key Jev, nên đo ý tưởng của nó bằng model mở chạy local. Model nhỏ là Qwen3.5-2B, fine-tune
LoRA một epoch trên 7.313 câu train. Model lớn là DeepSeek-v4.1-flash, dùng kết quả zero-shot sẵn có.
Thí nghiệm đọc xác suất của model nhỏ ở chữ cái đáp án: câu nào model nhỏ ít chắc nhất thì lấy đáp án của
DeepSeek. Đo trên đủ 1.658 câu test. Số liệu và script nằm ở `reports/eval/FINETUNE.md` và
`scripts/training/`.

| Gửi lên DeepSeek | Chọn câu theo xác suất | Chọn câu ngẫu nhiên | Model nhỏ đúng trên phần tự giữ |
|---|---:|---:|---:|
| 0% | 51,0 | 51,0 | 51,0 |
| 25% | 59,1 | 56,1 | 57,2 |
| 50% | **65,6** | 61,2 | 65,7 |
| 75% | 69,7 | 66,3 | 74,6 |
| 100% | 71,4 | 71,4 | – |

- **Xác suất của model dùng được để chọn câu khó:** chuyển theo xác suất hơn chuyển ngẫu nhiên cùng số câu
  từ 3,0 đến 4,4 điểm.
- **Fine-tune làm xác suất đáng tin hơn hẳn:** ECE giảm từ 10,7% xuống 1,8%. Đây đúng là tính chất mà Jev
  quảng bá qua RLCD [1], và ở đây có được bằng LoRA thông thường trên dữ liệu trong miền.
- **Kết hợp này không vượt DeepSeek dùng một mình.** Trên 25% câu model nhỏ chắc nhất, model nhỏ đúng
  74,6%, nhưng DeepSeek đúng 81% trên chính những câu đó. Lợi ích nằm ở chỗ ít lệnh gọi model lớn hơn, dữ
  liệu xử lý tại chỗ không rời máy, và có một ngưỡng rõ ràng để chuyển ca khó lên người.

Thí nghiệm này không đo bản thân Jev, mà chỉ cho thấy hướng "trả lời nhanh kèm xác suất, không chắc thì
chuyển lên" kiểm chứng được trên VM14K. Nếu có key, Jev chạy được trên đúng bảng này (mục 7).

---

## 7. Đề xuất cho nhóm

1. **Xin early-access key của Jev** rồi chạy Choice trên đúng 1.658 câu test. Đặt cạnh 7 model đã có,
   báo cáo cả accuracy, ECE và accuracy theo mức coverage. Đây là đánh giá **y khoa tiếng Việt đầu tiên**
   cho System One model, vì bài của Bonn không có phần này.
2. **Dùng xác suất để ưu tiên câu cần bác sĩ duyệt** trong 238 câu bất đồng: câu nào model rất chắc mà
   khác đáp án chuẩn thì đưa lên trước. Cách này bổ sung cho cách đang dùng là "số model đồng thuận".
3. **Không** dùng Jev hay bất kỳ model đóng nào cho dữ liệu bệnh nhân thật khi chưa có khung pháp lý (mục 5.2).

---

## Tài liệu tham khảo

[1] D. Almeida (TypeSafe AI), "Introducing System One Models & Jev", blog TypeSafe, 15/09/2026.
https://typesafe.ai/blog/introducing-system-one-models-and-jev

[2] S. Runkle, H. Lovell, "Building a Harness with Jev", blog LangChain, 17/09/2026.
https://www.langchain.com/blog/building-a-harness-with-jev

[3] TypeSafe AI, "Introduction" (tài liệu kỹ thuật). https://docs.typesafe.ai/introduction

[4] D. Kahneman, *Thinking, Fast and Slow*. New York: Farrar, Straus and Giroux, 2011.

[5] T. Deußer, L. Sparrenberg, R. Sifa (University of Bonn; Lamarr Institute; Fraunhofer IAIS),
"Evaluating and Benchmarking the System One Model Jev", arXiv:2609.37647, 29/09/2026.
https://arxiv.org/abs/2609.37647

[6] Browser Use, "jev-ultrafast: Fastest and cheapest web agent", GitHub, giấy phép MIT.
https://github.com/browser-use/jev-ultrafast

[7] TypeSafe AI, "Confidence" (tài liệu kỹ thuật). https://docs.typesafe.ai/confidence

[8] TypeSafe AI, "AI Primer" (tài liệu kỹ thuật). https://docs.typesafe.ai/introduction/machine-learning-primer

[9] T. Nguyen et al., "VM14K: First Vietnamese Medical Benchmark", arXiv:2506.01305, 2025.
https://arxiv.org/abs/2506.01305

[10] C. Guo, G. Pleiss, Y. Sun, K. Q. Weinberger, "On Calibration of Modern Neural Networks", ICML 2017.
https://arxiv.org/abs/1706.04599

[11] Y. Geifman, R. El-Yaniv, "Selective Classification for Deep Neural Networks", NeurIPS 2017.
https://arxiv.org/abs/1705.08500

[12] E. J. Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", ICLR 2022.
https://arxiv.org/abs/2106.09685

[13] I. Ong et al., "RouteLLM: Learning to Route LLMs with Preference Data", arXiv:2406.18665, 2024
(ICLR 2025). https://arxiv.org/abs/2406.18665

[14] "Leveraging Large Language Models for Automating Outpatients' Message Classifications of Electronic
Medical Records", *Healthcare* (MDPI), 2025. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12691883/

[15] Q. Jin et al., "Matching patients to clinical trials with large language models", *Nature
Communications* 15, 9074 (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11574183

[16] S. Machcha et al., "Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty",
arXiv:2601.12471, 2026. https://arxiv.org/abs/2601.12471

[17] Quốc hội, Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 (thông qua 26/6/2025, hiệu lực 01/01/2026);
Chính phủ, Nghị định 356/2025/NĐ-CP (31/12/2025).
https://thuvienphapluat.vn/van-ban/Quyen-dan-su/Nghi-dinh-356-2025-ND-CP-huong-dan-Luat-Bao-ve-du-lieu-ca-nhan-687428.aspx

[18] Qwen Team, Qwen3.5-2B model card, Hugging Face, 2026. https://huggingface.co/Qwen/Qwen3.5-2B

[19] TypeSafe wiki, "System One" (bản sao tài liệu khái niệm). Link trong biên bản họp kết thúc bằng
`.mdm` và trả về 404; bản đúng là
https://github.com/chujianyun/typesafe-wiki/blob/main/references/docs/Concepts/System%20One.md

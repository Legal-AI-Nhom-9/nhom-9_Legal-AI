# THƯ VIỆN CÂU LỆNH — DỰ ÁN LEGAL AI

**Nhóm:** 9 (15 thành viên) · **Học phần:** AI ứng dụng (06050)
**Viện Công nghệ tiên tiến và Trí tuệ nhân tạo — Trường Đại học Hùng Vương TP. Hồ Chí Minh**
**Công cụ AI:** Claude (Anthropic)

> Mỗi câu lệnh dưới đây gắn với **một phần cụ thể trên trang web** (cột “Dùng ở”), để người chấm mở trang ra là đối chiếu được câu lệnh với kết quả.
> Mỗi câu lệnh ghi: **tên kỹ thuật**, **vì sao chọn**, **kết quả thật**. Phần “Tinh chỉnh” chỉ ghi những lần sửa đã thực sự xảy ra.
> Nguyên tắc chung cho mọi câu lệnh: **không đưa họ tên, MSSV, số điện thoại, hợp đồng thật hay dữ liệu cá nhân của bất kỳ ai vào AI.**

---

## Bảng tra nhanh

| # | Kỹ thuật | Dùng ở (trên trang) |
|---|---|---|
| 01 | Zero-shot | Chọn ý tưởng — nền của Mục 1 |
| 02 | Reverse prompting (AI hỏi lại) | Phạm vi ba việc: thuê trọ · lao động · mua bán online |
| 03 | Role prompting + R-T-C-F-E | Mục 1: ba cột Vấn đề · Giải pháp · Khách hàng |
| 04 | Few-shot | Phần mở đầu: dòng giới thiệu và ba ý dưới chữ LEGAL AI |
| 05 | Few-shot | Mục 2: thông điệp “Hỏi luật dễ như nhắn tin” |
| 06 | Image prompting tám lớp | Mục 2: hình chủ đề `imgs/chu-de.svg` |
| 07 | Image prompting tám lớp | Mục 2: infographic `imgs/poster.svg` |
| 08 | Image prompting tám lớp | Phần mở đầu: ảnh nền `imgs/hero.svg` |
| 09 | Image prompting tám lớp | Mục 1: điện thoại `imgs/frame.svg` |
| 10 | Reverse prompting (suy ngược) | Mục 3: ảnh `imgs/iris.svg`, đồng bộ phong cách |
| 11 | Prompt chaining | Mục 3: kịch bản video 10 cảnh |
| 12 | Video prompting bảy thành phần | Mục 3: video 88 giây |
| 13 | Role prompting + ràng buộc | Câu hỏi thường gặp |
| 14 | Role prompting cho mã nguồn | Toàn trang: bố cục, hiệu ứng cuộn, chế độ `#sua` |
| 15 | Role prompting cho mã nguồn | Mục 4: năm phần việc; mục Nguồn tham khảo |
| 16 | Generate Knowledge | Mục Nguồn tham khảo |
| 17 | Verification prompting | Rà soát toàn trang, lập `bang-xac-minh.md` |
| 18 | Role prompting + ràng buộc pháp lý | Nhãn nội dung AI ở chân trang |

---

## A. Ý TƯỞNG VÀ NỘI DUNG

### 01 · Zero-shot

**Dùng ở:** Chọn ý tưởng khởi nghiệp

```
Liệt kê 10 vấn đề pháp lý nhỏ mà sinh viên và người mới đi làm ở
TP. Hồ Chí Minh hay gặp: đủ phiền để mất ngủ nhưng không đủ lớn để
thuê luật sư. Với mỗi vấn đề, ghi một câu vì sao người trẻ hay gặp.
```

**Vì sao chọn:** Giai đoạn mở rộng ý, chưa cần ràng buộc.
**Kết quả:** Danh sách 10 vấn đề. Nhóm giữ ba vấn đề quen thuộc nhất với chính mình: giữ tiền cọc phòng trọ, công ty chậm lương hoặc kéo dài thử việc, shop online không hoàn tiền.

---

### 02 · Reverse prompting — AI đặt câu hỏi cho nhóm

**Dùng ở:** Chốt phạm vi “chỉ làm ba việc” ghi ở cột Giải pháp

```
Nhóm tôi muốn làm một trợ lý pháp lý bằng AI cho sinh viên.
Trước khi góp ý, hãy hỏi tôi 7 câu hỏi cần thiết nhất để hiểu đúng
bài toán (người dùng là ai, phạm vi, rủi ro pháp lý, cách thu tiền...).
Chỉ hỏi, chưa trả lời.
```

**Vì sao chọn:** Nhóm chưa rõ nên làm rộng hay hẹp.
**Kết quả:** Câu hỏi về rủi ro “trợ lý trả lời như luật sư” dẫn tới hai quyết định đang có trên trang: chỉ làm **ba việc** (thuê trọ, lao động, mua bán online) và **luôn chỉ tới luật sư hoặc Trung tâm trợ giúp pháp lý** khi có tranh chấp.

---

### 03 · Role prompting + khung R-T-C-F-E

**Dùng ở:** Mục 1 — ba cột Vấn đề · Giải pháp · Khách hàng

```
[Role]    Bạn là cố vấn khởi nghiệp cho sinh viên.
[Task]    Viết ba đoạn Vấn đề, Giải pháp, Khách hàng cho Legal AI.
[Context] Legal AI chỉ làm ba việc: thuê trọ, hợp đồng lao động, mua bán
          online. Người dùng hỏi bằng tiếng Việt như nhắn tin. Câu trả lời
          luôn ghi tên văn bản, số điều, đường dẫn tới văn bản gốc trên
          Cơ sở dữ liệu quốc gia về văn bản pháp luật. Không thay luật sư.
          Hỏi đáp miễn phí; soát hợp đồng thuê trọ và lao động có tính phí.
          Không hỏi họ tên hay số điện thoại người dùng.
[Format]  Ba đoạn, mỗi đoạn tối đa 110 từ, xưng "tụi mình", câu ngắn.
          Không đưa số liệu thị trường nếu không có nguồn.
[Example] Giọng mở đầu: "Bạn ký hợp đồng thuê trọ trong năm phút."
```

**Vì sao chọn:** Cần đủ ý kinh doanh (khách hàng, thu tiền, giới hạn trách nhiệm) nhưng vẫn giữ giọng người trẻ.
**Kết quả:** Bản nháp đầu dùng giọng “tụi mình”, mở đầu bằng “Bạn ký hợp đồng thuê trọ trong năm phút…”, tập trung sinh viên thuê trọ.
**Tinh chỉnh (đã xảy ra):** Nhóm viết lại Mục 1 theo giọng trang trọng hơn và mở rộng khách hàng mục tiêu sang nhà sáng lập, doanh nghiệp nhỏ và vừa (SMEs), startup chưa có bộ phận pháp chế; câu hỏi ví dụ đổi thành “Một sinh viên gặp tình huống chủ nhà không hoàn trả tiền đặt cọc sau khi kết thúc hợp đồng thuê phòng”. Bản đang ở Mục 1 là bản nhóm viết lại.

---

### 04 · Few-shot

**Dùng ở:** Phần mở đầu trang — dòng giới thiệu và ba ý dưới chữ LEGAL AI

```
Viết 1 dòng giới thiệu (tối đa 20 từ) và 3 ý ngắn (tối đa 6 từ mỗi ý)
cho phần mở đầu trang Legal AI, theo đúng nhịp các ví dụ:
- Giới thiệu: "Đặt câu hỏi như nhắn tin. Nhận câu trả lời có nguồn."
- Ý ngắn: "Luôn dẫn văn bản gốc"
```

**Vì sao chọn:** Phần mở đầu cần chữ rất ngắn để đọc được trên ảnh nền; mô tả “ngắn gọn” bằng lời thì AI vẫn viết dài.
**Kết quả:** Trên trang: “Hỏi luật bằng tiếng Việt đời thường. Mỗi câu trả lời kèm điều luật gốc để bạn tự kiểm tra.” và ba ý “Thuê trọ · lao động · mua bán online”, “Luôn dẫn văn bản gốc”, “Biết khi nào cần luật sư”.

---

## B. THÔNG ĐIỆP VÀ BỘ NHẬN DIỆN

### 05 · Few-shot

**Dùng ở:** Mục 2 — thông điệp chính

```
Viết 8 khẩu hiệu cho Legal AI, mỗi câu tối đa 7 tiếng, đời thường,
nói được thành tiếng, theo nhịp ba ví dụ:
- "Hỏi luật? Hỏi mình."
- "Đọc điều luật gốc, không tin suông."
- "Biết khi nào cần luật sư."
```

**Vì sao chọn:** Cần giữ nhịp ngắn, gần gũi.
**Kết quả:** Nhóm chọn **“Hỏi luật dễ như nhắn tin”** làm thông điệp chính (Mục 2, tiêu đề infographic, cảnh cuối video). Giữ “Hỏi luật? Hỏi mình.” cho hình chủ đề.

---

> **Tám lớp của câu lệnh sinh ảnh** dùng cho 06–09: ① Chủ thể · ② Hành động/nội dung · ③ Bối cảnh · ④ Phong cách · ⑤ Bố cục và góc nhìn · ⑥ Ánh sáng và màu · ⑦ Tỷ lệ khung · ⑧ Ràng buộc loại trừ.
> Các hình xuất ra dạng **SVG** (hình vector) để chữ tiếng Việt trên hình sắc nét và sửa được.

### 06 · Image prompting tám lớp — hình chủ đề

**Dùng ở:** Mục 2 — `imgs/chu-de.svg`

```
① Chủ thể:   Cán cân công lý màu cam.
② Nội dung:  Một bong bóng chat màu kem ghi "Hỏi luật? Hỏi mình."
             đặt cạnh đĩa cân bên phải; bên dưới là chữ LEGAL AI,
             chữ "AI" màu cam.
③ Bối cảnh:  Một hình tròn xanh dương lớn sau cán cân, nền xanh đậm.
④ Phong cách: Minh hoạ phẳng, nét đều, không đổ bóng, không chân thực.
⑤ Bố cục:    Cán cân chính giữa, nhìn thẳng; chữ LEGAL AI căn giữa phía dưới.
⑥ Màu:       Nền #12293F, tròn #1A3C6E, cam #F4831F, kem #F7F1E8.
⑦ Tỷ lệ:     4:3, xuất SVG 1200×900.
⑧ Loại trừ:  Không người, không búa thẩm phán, không biểu tượng tòa án
             hay quốc huy, không logo thương hiệu khác.
```

**Vì sao chọn:** Hình chủ đề phải nói được “pháp luật + trò chuyện” trong một cái nhìn.
**Kết quả:** Hình đang ở Mục 2. Lớp ⑧ loại bỏ biểu tượng cơ quan nhà nước, tránh gây hiểu nhầm Legal AI là dịch vụ chính thức.

---

### 07 · Image prompting tám lớp — infographic

**Dùng ở:** Mục 2 — `imgs/poster.svg`

```
① Chủ thể:   Infographic ba bước dùng Legal AI.
② Nội dung:  Tiêu đề "Hỏi luật dễ như nhắn tin", phụ đề "Ba bước dùng
             Legal AI". Ô 1 "Hỏi bằng tiếng Việt" — "Thuê trọ, lao động,
             mua bán online". Ô 2 "Đọc điều luật gốc" — "Có tên văn bản,
             số điều và link để tự kiểm tra". Ô 3 "Biết khi nào cần luật
             sư" — "Vụ việc phức tạp được chỉ tới nơi trợ giúp". Dòng cuối:
             "Hình minh hoạ có sử dụng AI tạo sinh · Không thay thế tư vấn
             của luật sư".
③ Bối cảnh:  Nền kem trơn.
④ Phong cách: Infographic phẳng, số thứ tự lớn, mũi tên cam nối các ô.
⑤ Bố cục:    Ba ô ngang hàng, đọc trái sang phải.
⑥ Màu:       Ô 1 xanh đậm #12293F, ô 2 xanh #1A3C6E, ô 3 cam #F4831F.
⑦ Tỷ lệ:     4:3, SVG 1200×900.
⑧ Loại trừ:  Không biểu tượng cảm xúc, không số liệu, không chữ nào
             vượt ra ngoài ô.
```

**Vì sao chọn:** Người xem cần hiểu cách dùng mà không phải đọc đoạn văn.
**Tinh chỉnh (đã xảy ra):** Bản đầu, dòng mô tả ô 2 và ô 3 **bị cắt ở mép ô** (“số điề…”). Nhóm bổ sung ràng buộc “không chữ nào vượt ra ngoài ô” và ngắt mỗi mô tả thành ba dòng.
Sau đó ô 1 đổi tiêu đề từ “Hỏi bằng tiếng Việt” thành **“Hỏi Legal AI”** cho rõ người dùng hỏi ai.
**Kết quả:** Infographic đang ở Mục 2, chữ đọc đủ.

---

### 08 · Image prompting tám lớp — ảnh nền mở đầu

**Dùng ở:** Phần mở đầu trang — `imgs/hero.svg`

```
① Chủ thể:   Cán cân công lý màu cam, nét mảnh.
② Nội dung:  Bong bóng chat người dùng "Chủ trọ giữ cọc có đúng?";
             bong bóng trả lời màu cam "Có 2 điều luật liên quan —
             Bấm để đọc văn bản gốc ↗".
③ Bối cảnh:  Góc trái mờ ba khối văn bản "ĐIỀU 1.", "ĐIỀU 2.", "ĐIỀU 3."
             như trang luật; nền chuyển từ xanh đen sang xanh dương.
④ Phong cách: Minh hoạ phẳng, có quầng sáng cam nhẹ sau cán cân.
⑤ Bố cục:    Cán cân và bong bóng lệch phải để chừa chỗ cho chữ
             LEGAL AI bên trái phía dưới.
⑥ Màu:       #0A1B2B → #1A3C6E, cam #F4831F.
⑦ Tỷ lệ:     16:10, SVG 1600×1000.
⑧ Loại trừ:  Không người, không số điều cụ thể chưa kiểm chứng.
```

**Vì sao chọn:** Ảnh nền phải kể đúng tình huống chính (giữ cọc) và chừa chỗ cho tiêu đề.
**Tinh chỉnh (đã xảy ra):** Chữ “ĐIỀU” trên ảnh dùng font Georgia nên trên máy Windows bị tách dấu (“ĐIÊ`U”); đổi sang Times New Roman / Tahoma có đủ dấu tiếng Việt.
**Kết quả:** Ảnh nền phần mở đầu. Bong bóng trả lời chỉ ghi “Có 2 điều luật liên quan”, không ghi số điều, vì lúc dựng hình nhóm chưa kiểm chứng.

---

### 09 · Image prompting tám lớp — giao diện điện thoại

**Dùng ở:** Mục 1 — phần “Cách dùng LegalAI · 4 bước”, `imgs/cach-dung.svg` (bản đầu: `imgs/frame.svg`, vẫn dùng trong video)

```
① Chủ thể:   Điện thoại đang mở ứng dụng Legal AI.
② Nội dung:  Thanh trên: logo tròn chữ "L", "Legal AI — Trợ lý pháp lý".
             Tin nhắn người dùng: "Mình báo chủ trọ trước 30 ngày mà vẫn
             bị giữ cọc, vậy có đúng không?". Câu trả lời dạng thẻ có hai
             nút "Văn bản gốc · Điều … ↗". Thẻ cuối: "Vụ việc đang tranh
             chấp? Gặp luật sư hoặc trợ giúp pháp lý →". Ô nhập: "Hỏi bằng
             tiếng Việt đời thường…".
③ Bối cảnh:  Nền xanh đậm, hai vòng tròn mờ ở góc.
④ Phong cách: Mô phỏng giao diện phẳng, câu trả lời vẽ bằng thanh xám
             thay vì chữ thật.
⑤ Bố cục:    Điện thoại chính giữa, nhìn thẳng.
⑥ Màu:       Xanh đậm, cam, kem như các hình khác.
⑦ Tỷ lệ:     16:10, SVG 1600×1000.
⑧ Loại trừ:  Không tay người, không thanh trạng thái giả (pin, sóng),
             không ghi số điều cụ thể.
```

**Vì sao chọn:** Cần cho thấy sản phẩm hoạt động thế nào mà không phải làm ứng dụng thật.
**Tinh chỉnh (đã xảy ra):** Bản đầu (`frame.svg`) để câu trả lời dạng thanh xám và nút “Điều …” vì lúc đó chưa kiểm chứng; trên trang, hình lại bị cắt dần khi cuộn nên người xem khó hiểu. Sau khi đối chiếu Điều 328 Bộ luật Dân sự 2015, nhóm vẽ lại thành `cach-dung.svg`: câu trả lời tóm tắt thật, nút “Điều 328 · Bộ luật Dân sự 2015”, đánh số 1–4 khớp với 4 bước ghi bên cạnh, hiện nguyên hình.
**Kết quả:** Phần “Cách dùng LegalAI · 4 bước” ở Mục 1.

---

### 10 · Reverse prompting — suy ngược từ kết quả

**Dùng ở:** Mục 3 — `imgs/iris.svg` (khung mở hình tròn khi cuộn)

```
Đây là mã của frame.svg và hero.svg mà nhóm đã chọn. Hãy suy ra câu lệnh
tám lớp có thể đã tạo ra hai hình này (bảng màu, phong cách, loại trừ).
Sau đó dùng đúng câu lệnh đó, chỉ thay lớp ① và ②, để vẽ: ba tờ giấy
nằm nghiêng — "HỢP ĐỒNG Thuê nhà trọ", "HỢP ĐỒNG Lao động",
"ĐƠN HÀNG Mua bán online" — mỗi tờ có một đoạn tô cam, phía dưới là
kính lúp màu cam. Tỷ lệ 16:10.
```

**Vì sao chọn:** Hình thứ năm phải cùng phong cách bốn hình trước mà không phải mô tả lại từ đầu.
**Kết quả:** Hình ba tờ giấy ở Mục 3 đồng bộ màu và nét với các hình còn lại. Hình này cũng dùng ở cảnh 8 của video.

---

## C. VIDEO

### 11 · Prompt chaining — kịch bản

**Dùng ở:** Mục 3 — bảng Kịch bản phân cảnh và `docs/kich-ban-video.md`

```
Bước 1 — Liệt kê 5 nhịp kể chuyện cho video 60–90 giây giới thiệu Legal AI:
         bối cảnh, vấn đề, giải pháp, kiểm chứng, kết thúc. Nhân vật là
         sinh viên hư cấu tên Lan, đã báo chủ trọ trước 30 ngày nhưng vẫn
         bị giữ ba triệu tiền cọc.
Bước 2 — Với 5 nhịp ở bước 1, viết lời dẫn cho từng cảnh, câu ngắn,
         tổng không quá 170 từ. Không khẳng định Lan chắc chắn thắng
         tranh chấp.
Bước 3 — Với lời dẫn ở bước 2, chia thành 10 cảnh; ghép mỗi cảnh với một
         hình có sẵn trong imgs/ (hero, frame, iris, poster, chu-de) hoặc
         một khung chữ; ghi thời lượng từng cảnh.
```

**Vì sao chọn:** Viết một lượt thì kịch bản dài và không bám hình có sẵn.
**Kết quả:** Kịch bản 10 cảnh. Ràng buộc “không khẳng định thắng tranh chấp” khiến cảnh 6–7 chuyển thành “tự đọc Điều 328 Bộ luật Dân sự 2015” và “còn tranh chấp thì gặp luật sư hoặc trợ giúp pháp lý”.

---

### 12 · Video prompting bảy thành phần

**Dùng ở:** Mục 3 — `video/legal-ai-video.mp4` (dựng bằng `docs/tao-video/make_video.py`)

```
① Mục tiêu:   Giới thiệu Legal AI: hỏi luật bằng tiếng Việt, câu trả lời
              kèm văn bản gốc, biết khi nào cần luật sư.
② Khán giả:   Sinh viên, người mới đi làm; xem trên điện thoại.
③ Thời lượng: 60–90 giây; khung 1280×720.
④ Cấu trúc:   10 cảnh theo kịch bản ở câu lệnh 11.
⑤ Lời dẫn và phụ đề: Phụ đề tiếng Việt gắn sẵn, chữ trắng trên dải xanh
              đậm, cỡ chữ đọc được trên điện thoại.
⑥ Hình ảnh và chuyển động: Dùng hình trong imgs/; mỗi cảnh phóng chậm 4%;
              chuyển cảnh mờ dần 0,6 giây; khung chữ nền xanh đậm hoặc kem.
⑦ Ràng buộc:  Dòng "Nội dung có sử dụng AI tạo sinh" ở góc phải trên suốt
              video; cảnh đầu ghi rõ nhân vật hư cấu; không hình, không giọng
              người thật; lời dẫn dùng giọng đọc tổng hợp có giấy phép; nhạc
              nền tự sinh, không dùng bản nhạc có bản quyền.
```

**Vì sao chọn:** Nhóm không có cảnh quay thật và không muốn dùng hình người.
**Tinh chỉnh (đã xảy ra):**
1. Lần dựng đầu dài **94 giây, vượt giới hạn 90 giây**. Nhóm rút mỗi cảnh giữa 1 giây, còn **88 giây**.
2. Bản đầu **không có tiếng**. Thử lồng tiếng bằng giọng espeak-ng thì nghe rất cứng, nhóm bỏ.
3. Đổi sang giọng nơ-ron Piper tiếng Việt (`vi_VN-vais1000-medium`, CC BY 4.0). Kiểm tra bằng mô hình nhận dạng giọng nói tiếng Việt thì thấy “Legal AI” bị nghe thành “Liver”, “online” thành “Imland”, chữ cuối câu trước dấu chấm bị nuốt. Nhóm viết lại lời dẫn theo âm Việt (“Lê gồ Ây Ai”, “trên mạng”), thay dấu chấm giữa câu bằng dấu phẩy, đọc chậm lại (length_scale 1,45). Lần kiểm tra sau, máy nghe ra đúng gần hết lời dẫn, kể cả khi có nhạc nền.

**Kết quả:** Video 88 giây đang nhúng ở Mục 3, có lời dẫn, nhạc nền và phụ đề.

---

## D. TRANG WEB

### 13 · Role prompting + ràng buộc — Câu hỏi thường gặp

**Dùng ở:** Mục Câu hỏi thường gặp

```
Bạn là người viết nội dung cho một dự án pháp lý của sinh viên.
Viết 5 câu hỏi thường gặp về Legal AI, mỗi câu trả lời tối đa 45 từ:
có thay luật sư không; trả lời sai thì sao; luật thay đổi thì cập nhật
thế nào; có thu thập thông tin cá nhân không; trang này có dùng AI không.
Ràng buộc: không hứa điều ứng dụng chưa làm được; dùng chữ "dự kiến"
cho những việc chưa vận hành; câu trả lời đầu tiên phải bắt đầu bằng "Không."
```

**Vì sao chọn:** FAQ là nơi dễ hứa quá mức nhất, cần ràng buộc rõ.
**Kết quả:** 5 câu trên trang. Câu về cập nhật luật dùng “Nhóm **dự kiến** đối chiếu định kỳ…”, đúng ràng buộc.

---

### 14 · Role prompting cho mã nguồn — dựng trang

**Dùng ở:** Toàn trang

```
Bạn là lập trình viên web. Từ trang mẫu của học phần, dựng index.html
một tệp (HTML, CSS, JavaScript, không thư viện ngoài trừ Google Fonts)
cho Legal AI, giữ đủ bốn mục: Ý tưởng · Nhận diện · Video · Nhóm.
- Phần mở đầu và Mục 1, Mục 3 có hiệu ứng khi cuộn: ảnh trôi chậm,
  khung ảnh mở dần, khung tròn mở rộng.
- Tôn trọng chế độ giảm chuyển động của hệ điều hành.
- Hiển thị tốt ở bề rộng 390 px, không cuộn ngang.
- Thêm chế độ chỉnh sửa: mở tệp trên máy hoặc thêm #sua vào địa chỉ thì
  hiện nút sửa chữ, nhúng YouTube, đổi ảnh, rồi tải về index.html.
- Không có biểu mẫu thu thập dữ liệu, không cookie theo dõi.
- Mọi ảnh có mô tả alt đúng nội dung.
```

**Vì sao chọn:** Nhóm cần tự sửa chữ được mà không phải biết lập trình.
**Kết quả:** Trang hiện tại. Chế độ `#sua` là cách nhóm điền họ tên, MSSV.

---

### 15 · Role prompting cho mã nguồn — hoàn thiện

**Dùng ở:** Mục 4 (năm phần việc), mục Nguồn tham khảo, khung video

```
Bạn là lập trình viên web. Sửa index.html hiện có:
(1) Mục Nhóm chia 5 phần việc; mỗi phần có tiêu đề, dòng "Họ và tên: …
    MSSV: …" để trống, và 3 gạch đầu dòng ghi rõ việc đã làm cho trang.
(2) Nhúng video/legal-ai-video.mp4 vào khung #videoBox; giữ nguyên chức
    năng nhúng YouTube của chế độ chỉnh sửa.
(3) Thêm mục Nguồn tham khảo trước chân trang, ghi số hiệu văn bản.
(4) Cho phép sửa các gạch đầu dòng trong chế độ #sua.
Không thêm biểu mẫu, không thêm thư viện, kiểm tra ở bề rộng 390 px.
```

**Vì sao chọn:** Trang đã có chế độ chỉnh sửa riêng, cần sửa mà không làm hỏng.
**Tinh chỉnh (đã xảy ra):** Khi kiểm tra ở bề rộng 390 px, dòng giáo viên hướng dẫn bị bóp hẹp thành cột chữ dọc; bổ sung quy tắc xếp dòng cho màn hình nhỏ.
**Kết quả:** Mục 4 và mục Nguồn tham khảo hiện tại; video phát được trên máy tính và điện thoại.

---

## E. KIỂM CHỨNG VÀ TRÁCH NHIỆM

### 16 · Generate Knowledge

**Dùng ở:** Mục Nguồn tham khảo

```
Trước khi trả lời, hãy liệt kê các văn bản pháp luật Việt Nam còn hiệu lực
liên quan đến: tiền đặt cọc khi thuê nhà; hợp đồng lao động và thử việc;
quyền của người mua hàng trực tuyến; trợ giúp pháp lý miễn phí; bảo vệ dữ
liệu cá nhân; gắn nhãn nội dung do AI tạo. Ghi số hiệu và năm. Sau đó mới
cho biết trang web nên dẫn văn bản nào cho từng nội dung.
```

**Vì sao chọn:** Hỏi thẳng “nên dẫn luật gì” thì AI trả lời chung chung.
**Kết quả:** Danh sách 7 văn bản. **Nhóm không dùng thẳng**: từng số hiệu được tra lại (Luật Trí tuệ nhân tạo 134/2025/QH15 và Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 tra trên thuvienphapluat.vn; các luật còn lại đối chiếu trên vbpl.vn — xem `bang-xac-minh.md`).

---

### 17 · Verification prompting

**Dùng ở:** Rà soát toàn trang trước khi nộp

```
Đây là toàn bộ chữ trên trang web của nhóm: [dán nội dung].
Chỉ dùng thông tin có trong văn bản trên. Liệt kê mọi khẳng định mang tính
sự kiện, số liệu hoặc pháp lý, kèm vị trí xuất hiện (mục nào, câu nào).
Không bổ sung kiến thức ngoài. Đánh dấu khẳng định nào chưa nêu nguồn.
```

**Vì sao chọn:** Cần tìm hết các chỗ phải kiểm chứng, tránh sót.
**Kết quả:** Danh sách được chuyển vào `docs/bang-xac-minh.md` để thành viên phần 04 đối chiếu và đánh dấu.

---

### 18 · Role prompting + ràng buộc pháp lý — nhãn AI

**Dùng ở:** Chân trang — khối “Nhãn nội dung do AI tạo sinh”

```
Bạn là người phụ trách tuân thủ của dự án. Viết nhãn công bố nội dung có
sử dụng AI tạo sinh cho trang web, tối đa 80 từ, ghi rõ: công cụ AI đã
dùng; từng khâu có dùng AI (nội dung, hình, video, mã trang); nhóm đã
làm gì với đầu ra của AI; có đưa dữ liệu cá nhân vào AI hay không; căn cứ
gắn nhãn là Luật Trí tuệ nhân tạo (Luật số 134/2025/QH15).
```

**Vì sao chọn:** Thiếu nhãn AI bị trừ 1,0 điểm; nhãn chung chung không cho biết AI làm phần nào.
**Kết quả:** Nhãn ở chân trang ghi từng khâu. Nhãn ngắn “Nội dung có sử dụng AI tạo sinh” còn có ở dưới video, trên infographic và suốt video.

---

## Tổng hợp kỹ thuật đã dùng

| Kỹ thuật | Câu lệnh | Số câu |
|---|---|---|
| Zero-shot | 01 | 1 |
| Reverse prompting | 02, 10 | 2 |
| Role prompting + R-T-C-F-E | 03 | 1 |
| Few-shot | 04, 05 | 2 |
| Image prompting tám lớp | 06, 07, 08, 09 | 4 |
| Prompt chaining | 11 | 1 |
| Video prompting bảy thành phần | 12 | 1 |
| Role prompting + ràng buộc (nội dung, mã, tuân thủ) | 13, 14, 15, 18 | 4 |
| Generate Knowledge | 16 | 1 |
| Verification prompting | 17 | 1 |
| **Tổng** | | **18 câu lệnh · 10 kỹ thuật** |

---

## Ba điều nhóm rút ra

1. **Lớp “loại trừ” quan trọng không kém lớp “chủ thể”.** Chính lớp ⑧ giữ cho hình không có người thật, không có biểu tượng cơ quan nhà nước và không có số điều chưa kiểm chứng — ba thứ có thể làm đồ án bị trừ điểm.
2. **Câu lệnh tốt vẫn phải đo lại kết quả.** Video vượt 90 giây và chữ trên infographic bị cắt chỉ phát hiện được khi xem thành phẩm, không phải khi đọc câu lệnh.
3. **Phần pháp lý không giao cho AI.** Generate Knowledge cho danh sách để tra, nhưng mọi số hiệu văn bản trên trang đều do nhóm tự tra lại.

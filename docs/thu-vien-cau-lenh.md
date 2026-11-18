# THƯ VIỆN CÂU LỆNH — DỰ ÁN LEGAL AI

**Nhóm:** ……………… · **Học phần:** AI ứng dụng (06050)
**Viện Công nghệ tiên tiến và Trí tuệ nhân tạo — Trường Đại học Hùng Vương TP. Hồ Chí Minh**
**Công cụ AI:** Claude (Anthropic)

> Ghi các câu lệnh đã dùng để tạo nội dung, hình, video và mã trang web. Mỗi câu lệnh ghi **tên kỹ thuật**, **lý do chọn** và **kết quả thật**, kể cả lần chưa đạt.
> Nguyên tắc chung: không đưa họ tên, MSSV, số điện thoại hay hợp đồng thật của ai vào AI.

---

## 01 · Zero-shot

**Kỹ thuật:** Zero-shot prompting
**Dùng ở:** Tìm ý tưởng khởi nghiệp

```
Liệt kê 10 vấn đề pháp lý nhỏ mà sinh viên và người mới đi làm ở
TP. Hồ Chí Minh hay gặp, đủ phiền để mất ngủ nhưng không đủ lớn để
thuê luật sư.
```

**Vì sao chọn:** Giai đoạn mở rộng, chưa cần ràng buộc.
**Kết quả:** Ra 10 vấn đề. Nhóm giữ ba nhóm việc gặp nhiều nhất quanh mình: thuê trọ (giữ cọc), hợp đồng lao động (chậm lương, thử việc), mua bán online (không hoàn tiền).

---

## 02 · Role prompting kèm khung R-T-C-F-E

**Kỹ thuật:** Role prompting + Role–Task–Context–Format–Example
**Dùng ở:** Viết Mục 1 (Vấn đề · Giải pháp · Khách hàng)

```
Bạn là cố vấn khởi nghiệp cho sinh viên.
Nhiệm vụ: viết ba đoạn Vấn đề, Giải pháp, Khách hàng cho Legal AI, trợ lý
pháp lý chỉ làm ba việc: thuê trọ, hợp đồng lao động, mua bán online.
Bối cảnh: người đọc là sinh viên, đọc trên điện thoại. Legal AI không
thay luật sư; mỗi câu trả lời phải kèm tên văn bản, số điều, đường dẫn
văn bản gốc.
Định dạng: mỗi đoạn tối đa 110 từ, xưng "tụi mình", không dùng số liệu
thị trường nếu không có nguồn.
Ví dụ giọng điệu: "Bạn ký hợp đồng thuê trọ trong năm phút."
```

**Vì sao chọn:** Bản viết đầu quá trang trọng, đọc như văn bản hành chính.
**Kết quả:** Ba đoạn đang nằm ở Mục 1 trên trang, nhóm đã đọc lại và biên tập. *(Nhóm ghi thêm số lần chỉnh và chỗ đã sửa.)*

---

## 03 · Few-shot

**Kỹ thuật:** Few-shot prompting
**Dùng ở:** Chọn thông điệp chính (Mục 2)

```
Viết 8 khẩu hiệu cho Legal AI theo đúng nhịp ngắn, đời thường của ba
ví dụ sau:
- "Hỏi luật? Hỏi mình."
- "Đọc điều luật gốc, không tin suông."
- "Biết khi nào cần luật sư."
```

**Vì sao chọn:** Cần giữ giọng gần gũi, mô tả bằng lời không ra được.
**Kết quả:** Nhóm chọn “Hỏi luật dễ như nhắn tin” làm thông điệp chính và giữ “Hỏi luật? Hỏi mình.” cho hình chủ đề.

---

## 04 · Câu lệnh sinh ảnh — đủ tám lớp

**Kỹ thuật:** Image prompting tám lớp: chủ thể · hành động · bối cảnh · phong cách · bố cục/góc nhìn · ánh sáng và màu · tỷ lệ khung · ràng buộc loại trừ
**Dùng ở:** Hình giao diện điện thoại `imgs/frame.svg`

```
[Chủ thể]   Một chiếc điện thoại đang mở ứng dụng Legal AI.
[Hành động] Người dùng nhắn: "Mình báo chủ trọ trước 30 ngày mà vẫn bị
            giữ cọc, vậy có đúng không?"; ứng dụng trả lời kèm hai nút
            "Văn bản gốc · Điều …" và một thẻ "Vụ việc đang tranh chấp?
            Gặp luật sư hoặc trợ giúp pháp lý".
[Bối cảnh]  Nền xanh đậm có hai vòng tròn mờ.
[Phong cách] Minh hoạ phẳng dạng vector, không chân thực.
[Bố cục]    Điện thoại đặt chính giữa, nhìn thẳng.
[Ánh sáng/màu] Xanh đậm #0A1B2B, cam #F4831F, kem #F7F1E8.
[Tỷ lệ]     Khung ngang 16:10.
[Loại trừ]  Không có người, không có khuôn mặt hay bàn tay thật,
            không có logo thương hiệu khác, không ghi số điều cụ thể
            chưa kiểm chứng.
```

**Vì sao chọn:** Lần đầu chỉ ghi “giao diện app pháp lý” nên ra hình chung chung, có điều luật đánh số tuỳ tiện.
**Kết quả:** Đủ tám lớp thì ra hình đúng câu chuyện. Nút văn bản gốc để “Điều …” vì nhóm chưa muốn ghi số điều lên hình trước khi kiểm chứng.

---

## 05 · Reverse prompting — suy ngược từ kết quả

**Kỹ thuật:** Reverse prompting, suy câu lệnh từ đầu ra mẫu
**Dùng ở:** Đồng bộ phong cách các hình `hero`, `iris`, `chu-de`, `poster`

```
Đây là hình frame.svg nhóm đã chọn. Hãy suy ra câu lệnh tám lớp có thể
đã tạo ra hình này, rồi dùng đúng câu lệnh đó (giữ bảng màu, phong cách,
loại trừ) viết lại cho: (1) cán cân và bong bóng chat "Chủ trọ giữ cọc
có đúng?"; (2) ba tờ giấy thuê trọ, lao động, mua bán online có kính lúp;
(3) infographic ba bước "Hỏi luật dễ như nhắn tin".
```

**Vì sao chọn:** Cần năm hình cùng một phong cách mà không mô tả lại từ đầu.
**Kết quả:** Năm hình đồng bộ. Lỗi phát hiện sau: trên infographic, dòng “số điều” và “chỉ tới nơi trợ giúp” bị cắt ở mép ô; nhóm đã sửa bằng cách xuống dòng.

---

## 06 · Prompt chaining — kịch bản video

**Kỹ thuật:** Prompt chaining
**Dùng ở:** Kịch bản video Mục 3

```
Bước 1 — Liệt kê 5 nhịp kể chuyện cho video 60–90 giây: bối cảnh, vấn đề,
         giải pháp, kiểm chứng, kết thúc. Nhân vật là sinh viên hư cấu
         bị giữ tiền cọc.
Bước 2 — Với 5 nhịp ở bước 1, viết lời dẫn cho từng cảnh, tổng không
         quá 170 từ, câu ngắn.
Bước 3 — Với lời dẫn ở bước 2, ghép mỗi cảnh với một hình có sẵn
         trong imgs/ hoặc một khung chữ, ghi thời lượng từng cảnh.
```

**Vì sao chọn:** Làm một lượt thì kịch bản dài, không khớp thời lượng.
**Kết quả:** Ra 10 cảnh. **Lần dựng đầu dài 94 giây, vượt giới hạn**; nhóm rút mỗi cảnh giữa một giây, còn 88 giây.

---

## 07 · Câu lệnh tạo video — đủ bảy thành phần

**Kỹ thuật:** Video prompting bảy thành phần: mục tiêu · khán giả · thời lượng · cấu trúc cảnh · lời dẫn và phụ đề · hình ảnh và chuyển động · ràng buộc pháp lý, đạo đức
**Dùng ở:** Dựng video bằng mã (`docs/tao-video/make_video.py`)

```
[Mục tiêu]   Video giới thiệu Legal AI: hỏi luật bằng tiếng Việt, câu trả
             lời kèm văn bản gốc, biết khi nào cần luật sư.
[Khán giả]   Sinh viên, người mới đi làm.
[Thời lượng] 60–90 giây, khung 1280×720.
[Cấu trúc]   10 cảnh theo kịch bản ở câu lệnh 06.
[Lời dẫn/phụ đề] Phụ đề tiếng Việt gắn sẵn, chữ trắng trên dải xanh đậm,
             cỡ chữ đọc được trên điện thoại.
[Hình ảnh/chuyển động] Dùng các hình trong imgs/, mỗi cảnh phóng chậm
             4%, chuyển cảnh mờ dần 0,6 giây.
[Ràng buộc]  Nhãn "Nội dung có sử dụng AI tạo sinh" suốt video; không hình,
             giọng người thật; công bố nhân vật hư cấu ở cảnh đầu; không
             khẳng định kết quả tranh chấp.
```

**Vì sao chọn:** Nhóm không có tư liệu quay thật và không muốn dùng hình người.
**Kết quả:** Video 88 giây dùng được. Hạn chế: chưa có giọng đọc.

---

## 08 · Generate Knowledge

**Kỹ thuật:** Generate Knowledge prompting
**Dùng ở:** Chuẩn bị mục Nguồn tham khảo

```
Trước khi trả lời, hãy liệt kê các văn bản pháp luật Việt Nam liên quan
đến: tiền đặt cọc khi thuê nhà; hợp đồng lao động và thử việc; quyền của
người mua hàng online; trợ giúp pháp lý miễn phí; dữ liệu cá nhân; gắn
nhãn nội dung do AI tạo. Ghi số hiệu văn bản. Sau đó mới cho biết trang
web của nhóm nên dẫn văn bản nào.
```

**Vì sao chọn:** Hỏi thẳng thì AI trả lời chung chung.
**Kết quả:** Có danh sách để tra. **Nhóm không dùng thẳng**: từng số hiệu được tra lại trên vbpl.vn và thuvienphapluat.vn (xem `bang-xac-minh.md`).

---

## 09 · Verification prompting

**Kỹ thuật:** Verification prompting — khoá nguồn, buộc dẫn vị trí
**Dùng ở:** Rà soát toàn trang trước khi nộp

```
Đây là toàn bộ chữ trên trang web của nhóm: [dán nội dung].
Chỉ dùng thông tin có trong văn bản trên, liệt kê mọi khẳng định mang
tính sự kiện, số liệu hoặc pháp lý, kèm vị trí xuất hiện. Không bổ sung
kiến thức ngoài. Đánh dấu khẳng định nào chưa nêu nguồn.
```

**Vì sao chọn:** Cần tìm hết các chỗ phải kiểm chứng.
**Kết quả:** Danh sách khẳng định được chuyển vào `bang-xac-minh.md` để thành viên phần 04 đối chiếu.

---

## 10 · Role prompting cho mã nguồn

**Kỹ thuật:** Role prompting + ràng buộc rõ
**Dùng ở:** Mục Thông tin nhóm, mục Nguồn tham khảo, nhúng video

```
Bạn là lập trình viên web. Sửa index.html của nhóm: (1) mục Nhóm chia 5
phần việc, mỗi phần ghi rõ việc đã làm, để trống họ tên và MSSV;
(2) nhúng video/legal-ai-video.mp4 vào khung #videoBox, giữ nguyên chức
năng nhúng YouTube của chế độ chỉnh sửa; (3) thêm mục Nguồn tham khảo
trước chân trang. Không thêm biểu mẫu, không thêm thư viện ngoài, hiển
thị tốt ở bề rộng 390 px.
```

**Vì sao chọn:** Trang đã có chế độ chỉnh sửa riêng, cần sửa mà không làm hỏng.
**Kết quả:** Chạy đúng trên máy tính và điện thoại; chế độ `#sua` vẫn sửa được chữ trong mục Nhóm.

---

## Tổng hợp kỹ thuật đã dùng

| Kỹ thuật | Số câu lệnh |
|---|---|
| Zero-shot | 1 |
| Role prompting + R-T-C-F-E | 2 |
| Few-shot | 1 |
| Image prompting tám lớp | 1 |
| Reverse prompting | 1 |
| Prompt chaining | 1 |
| Video prompting bảy thành phần | 1 |
| Generate Knowledge | 1 |
| Verification prompting | 1 |
| **Tổng** | **10 câu lệnh · 9 kỹ thuật** |

---

## Ba điều nhóm rút ra

1. **Hình đủ tám lớp mới bám đúng câu chuyện.** Câu lệnh ngắn cho ra hình đẹp nhưng sai nội dung, có cả điều luật đánh số tuỳ tiện.
2. **Tách kịch bản thành chuỗi bước giúp kiểm soát thời lượng**, nhưng vẫn phải đo lại: bản dựng đầu vượt 90 giây.
3. **Phần pháp lý không giao cho AI.** Mọi số hiệu văn bản trên trang đều được nhóm tự tra lại.

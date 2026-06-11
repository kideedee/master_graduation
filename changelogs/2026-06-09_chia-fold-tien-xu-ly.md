# Nhật ký thay đổi — Session 2026-06-09 (chia fold & tiền xử lý)

## Mục tiêu
Làm rõ trật tự xử lý dữ liệu trong phần **Thu thập dữ liệu và tiền xử lý** ([chapters/c3/chapter_3.tex](../chapters/c3/chapter_3.tex#L20)): việc **chia 5-fold ở mức hệ gen** phải xảy ra **trước** các bước tạo contig, tăng cường dữ liệu và lấy mẫu giảm ngẫu nhiên. Bản gốc nhắc kiểm định chéo như một câu rời về "độ tin cậy", khiến người đọc dễ hiểu nhầm contig được cắt trước rồi mới chia fold.

> Quy ước: **(N)** = nội dung mới/thực chất (nên rà soát kỹ).

---

## Quyết định cuối cùng về cấu trúc
Đưa bước chia fold **vào trong pipeline** và đặt làm **Bước 1**, biến pipeline tiền xử lý từ 4 bước thành **5 bước**:

| Bước | Nội dung | Phạm vi chạy |
|---|---|---|
| 1 | Chia dữ liệu ở mức hệ gen (5-fold phân tầng, 8:2) | một lần |
| 2 | Tạo contig (cửa sổ trượt) | mỗi fold |
| 3 | Tăng cường dữ liệu (bổ sung đảo ngược) | mỗi fold |
| 4 | Lấy mẫu giảm ngẫu nhiên (chỉ trên train) | mỗi fold |
| 5 | Mã hóa BPE | mỗi fold |

Diễn đạt rõ: Bước 1 chạy một lần tạo ra 5 phần; Bước 2–5 lặp độc lập trong mỗi phần, riêng cho tập huấn luyện và tập kiểm định.

## Lý do bắt buộc của trật tự
Contig sinh từ cửa sổ trượt **chồng lấn**, nên contig cùng một hệ gen chia sẻ đoạn DNA trùng. Nếu chia phần ở mức contig (sau khi cắt), các contig gần giống hệt từ cùng hệ gen lọt cả train lẫn val, gây **rò rỉ thông tin giữa train/val** và làm kết quả thổi phồng. Chia ở mức hệ gen, đặt làm bước đầu, loại bỏ nguy cơ này. Lập luận này được đặt trọn trong phần mô tả Bước 1.

Bằng chứng mã nguồn đang làm đúng: bảng `tab:dataset_statistics` cho thấy cột Huấn luyện cân bằng 1:1 còn cột Kiểm định giữ mất cân bằng gốc, tức undersampling chỉ trên train sau khi đã chia fold.

---

## Chi tiết thay đổi — `chapters/c3/chapter_3.tex`

### (N) Đoạn thu thập dữ liệu ([dòng 23](../chapters/c3/chapter_3.tex#L23))
Rút gọn: bỏ phần mô tả chi tiết chia fold ở đây (đã chuyển vào Bước 1), kết đoạn bằng một câu chuyển ngắn trỏ xuống quy trình bên dưới.

### (N) Câu mở pipeline ([dòng 25](../chapters/c3/chapter_3.tex#L25))
Mô tả pipeline gồm **năm bước**; nêu rõ Bước 1 chạy một lần, bốn bước còn lại lặp độc lập trong mỗi fold cho cả train và val.

### (N) Bước 1 mới: Chia dữ liệu ở mức hệ gen ([dòng 35](../chapters/c3/chapter_3.tex#L35))
`\textbf{Bước 1: Chia dữ liệu ở mức hệ gen.}` chứa toàn bộ mô tả chia phần (5-fold phân tầng, 8:2, mỗi hệ gen chỉ thuộc một tập) cùng lập luận chống rò rỉ train/val, có tham chiếu "Như trình bày ở Bước 2".

### (N) Đánh số lại các bước
- Bước 1 cũ (tạo contig) → **Bước 2**.
- Bước 2 cũ (tăng cường) → **Bước 3**.
- Bước 3 cũ (undersampling) → **Bước 4**; sửa tham chiếu nội bộ "sau bước 1 và bước 2" → "sau bước 2 và bước 3".
- Bước 4 cũ (BPE) → **Bước 5**.

### (N) Đồng bộ mục Tổng quan ([dòng 16](../chapters/c3/chapter_3.tex#L16))
Câu mô tả hình: "bốn bước: tạo contig…" → "năm bước: chia dữ liệu ở mức hệ gen, tạo contig…".

### (N) Caption + comment hình `fig:data_preparation` ([dòng 30–31](../chapters/c3/chapter_3.tex#L30))
Caption liệt kê đủ 5 bước, mở đầu bằng "chia dữ liệu ở mức hệ gen (5-fold phân tầng)". Comment LaTeX nhắc vẽ lại ảnh để khối chia fold là bước đầu của pipeline, bốn bước còn lại nằm trong mỗi fold.

---

## KHÔNG đụng tới
- Số liệu hai bảng (`tab:sliding_window_params`, `tab:dataset_statistics`).
- Công thức cửa sổ trượt; nội dung sinh học Bước 3 (tăng cường) và Bước 5 (BPE).
- Không thêm in đậm/nghiêng/viết hoa nhấn mạnh trong câu; không dùng gạch ngang "—" để ngắt câu.

## Việc cần làm thủ công
- [ ] Vẽ lại ảnh `figures/data_preparation.png`: khối "chia 5-fold mức hệ gen" là bước đầu pipeline, bốn bước còn lại nằm trong mỗi fold (đã đặt comment nhắc trong file `.tex`).

## Kiểm tra sau khi sửa
- [ ] Biên dịch lại: `pdflatex thesis.tex` (không đổi `.bib` nên không cần bibtex) để xác nhận không lỗi cú pháp và `\ref{fig:data_preparation}` hiển thị đúng.

# Nhật ký thay đổi — Session 2026-06-09 (chia fold & tiền xử lý)

## Mục tiêu
Làm rõ trật tự xử lý dữ liệu trong phần **Thu thập dữ liệu và tiền xử lý** ([chapters/c3/chapter_3.tex](../chapters/c3/chapter_3.tex#L20)): việc **chia 5-fold ở mức hệ gen** phải xảy ra **trước** ba bước tạo contig, tăng cường dữ liệu và lấy mẫu giảm ngẫu nhiên. Bản cũ nhắc kiểm định chéo như một câu rời về "độ tin cậy", khiến người đọc dễ hiểu nhầm contig được cắt trước rồi mới chia fold.

> Quy ước: **(N)** = nội dung mới/thực chất (nên rà soát kỹ).

---

## Vấn đề được sửa
Tái cấu trúc phần thành hai giai đoạn rõ ràng:
1. **Chia dữ liệu ở mức hệ gen** — 5-fold phân tầng, 8:2, trước mọi bước tiền xử lý; mỗi hệ gen chỉ thuộc train hoặc val của một fold.
2. **Pipeline tiền xử lý cho từng fold** — 4 bước (contig → tăng cường → undersampling chỉ trên train → BPE) lặp độc lập cho cả 5 phần.

Lý do bắt buộc của trật tự: contig sinh từ cửa sổ trượt **chồng lấn**, nên contig cùng một hệ gen chia sẻ đoạn DNA trùng. Nếu chia ở mức contig, các contig gần giống hệt từ cùng hệ gen lọt cả train lẫn val → **rò rỉ thông tin giữa train/val** → kết quả thổi phồng. Chia ở mức hệ gen loại bỏ nguy cơ này.

Bằng chứng mã nguồn đang làm đúng: bảng `tab:dataset_statistics` cho thấy cột Huấn luyện cân bằng 1:1 còn cột Kiểm định giữ mất cân bằng gốc → undersampling chỉ trên train, sau khi đã chia fold.

---

## Chi tiết thay đổi — `chapters/c3/chapter_3.tex`

### (N) Đoạn thu thập dữ liệu ([dòng 23](../chapters/c3/chapter_3.tex#L23))
Thay câu kiểm định chéo cũ bằng **hai đoạn**:
- Đoạn 1: nêu rõ chia phần ở **mức hệ gen** và **trước toàn bộ tiền xử lý**; phân tầng theo nhãn; mỗi hệ gen chỉ thuộc một tập trong một fold.
- Đoạn 2: lập luận chống **rò rỉ thông tin giữa tập huấn luyện và kiểm định** (phân biệt với "rò rỉ k-mer" đã bàn ở Chương 2 — khái niệm khác).

### (N) Câu mở pipeline ([dòng ~26](../chapters/c3/chapter_3.tex#L25))
Đổi đoạn "Quy trình tiền xử lý gồm bốn bước liên tiếp…" thành câu mở giai đoạn 2: 4 bước áp dụng riêng cho train/val của **từng fold**, lặp độc lập cho cả 5 phần; undersampling chỉ trên train.

### (N) Nhấn lại trật tự ở các bước
- **Bước 1** (tạo contig): thêm cụm "trên tập hệ gen đã chia của mỗi fold" vào câu mô tả cửa sổ trượt.
- **Bước 3** (undersampling): thêm "trong từng fold" vào câu khẳng định chỉ áp dụng trên tập huấn luyện.

### (N) Caption hình `fig:data_preparation` ([dòng ~30](../chapters/c3/chapter_3.tex#L30))
Caption mới nêu rõ pipeline chạy **sau khi chia dữ liệu ở mức hệ gen** và undersampling **chỉ trên tập huấn luyện**. Thêm comment LaTeX ghi chú **cần vẽ lại ảnh** `data_preparation.png` để bổ sung khối "chia 5-fold ở mức hệ gen" ở đầu pipeline.

---

## KHÔNG đụng tới
- Số liệu hai bảng (`tab:sliding_window_params`, `tab:dataset_statistics`).
- Công thức cửa sổ trượt; nội dung Bước 2 (tăng cường) và Bước 4 (BPE).
- Không thêm in đậm/in nghiêng/viết hoa nhấn mạnh trong câu văn (theo yêu cầu hình thức).

## Việc cần làm thủ công (ngoài phạm vi sửa text)
- [ ] Vẽ lại ảnh `figures/data_preparation.png` thêm khối "chia 5-fold mức hệ gen" ở đầu, thể hiện 4 bước nằm trong mỗi fold (đã đặt comment nhắc trong file `.tex`).

## Kiểm tra sau khi sửa
- [ ] Biên dịch lại: `pdflatex thesis.tex` (không đổi `.bib` nên không cần bibtex) để xác nhận không lỗi cú pháp và `\ref{fig:data_preparation}` hiển thị đúng.

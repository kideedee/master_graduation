# Nhật ký thay đổi — Session 2026-06-09

## Mục tiêu
Bổ sung phần **phân tích lỗi** của PhaBERT vào luận văn (từ kết quả trong `error_analysis/`), kèm một số chỉnh sửa hình thức (dấu câu, in đậm/nghiêng) cho nhất quán.

> Quy ước: **(N)** = nội dung mới / thực chất (nên rà soát kỹ) · **(H)** = chỉnh hình thức (không đổi nội dung).

---

## 1. Chương 4 — `chapters/c4/chapter_4.tex`

### (N) Thêm Section 4.4 "Phân tích lỗi"
Section mới đặt sau *Kết quả thực nghiệm*, trước *Thảo luận*. Số liệu lấy từ `error_analysis/tables/` (tập kiểm định 5-fold, gộp/pooled — đóng khung là *mô tả hành vi*, không phải ước lượng tổng quát hóa).

- [\section{Phân tích lỗi}](chapters/c4/chapter_4.tex#L124) — đoạn mở giải thích phương pháp gộp.
- [\subsection{Phân tích lỗi theo lớp nhãn}](chapters/c4/chapter_4.tex#L129) — FPR/FNR theo 4 nhóm độ dài:
  - Bảng `tab:error_by_class` (FPR/FNR + cỡ mẫu).
  - Hình `fig:error_confusion_matrix` (ma trận nhầm lẫn).
  - Bình luận: temperate (lớp thiểu số) bị phân loại sai nhiều hơn; khoảng cách FPR−FNR nới rộng theo độ dài (Nhóm D: 12,43% vs 7,62%).
- [\subsection{Phân tích lỗi theo thành phần GC}](chapters/c4/chapter_4.tex#L159) — quan hệ hình chữ U theo GC:
  - Hình `fig:error_heatmap_gc` (bản đồ nhiệt độ dài × GC).
  - Bình luận: mạnh ở GC 35–55%, yếu ở 2 cực (GC>55%: 24,83% toàn cục); phát hiện chưa được công cụ trước báo cáo.
  - **Lưu ý:** bảng GC `tab:error_by_gc` đã được **comment-out** (heatmap đã thể hiện đủ số liệu); câu văn đã chỉnh để trỏ tới hình thay vì bảng.

### (N) Kết luận chương
- [Dòng 223](chapters/c4/chapter_4.tex#L223) — thêm 1 câu tổng kết phân tích lỗi, trỏ tới `\ref{sec:phan_tich_loi}` (hai điểm yếu: thiên lệch lớp đa số + lỗi cao ở GC cực trị).

### (H) Chỉnh hình thức
- Bỏ in đậm/in nghiêng nhấn mạnh tùy tiện chữ tiếng Việt trong mục mới; header bảng để chữ thường (đồng bộ các bảng cũ).
- Đổi em-dash `---` → dấu phẩy ở các chỗ ngắt/chèn mệnh đề (mục Thảo luận & Phân tích kiến trúc).

---

## 2. Chương 5 — `chapters/c5/chapter_5.tex`

### (N) Bổ sung mục *Hạn chế và hướng phát triển*
- [Dòng 27](chapters/c5/chapter_5.tex#L27) — thêm dẫn chứng số liệu FPR/FNR vào **Hạn chế #1** (undersampling), trỏ `\ref{sec:loi_theo_lop}`: FPR > FNR ở mọi nhóm, chênh ~1,6 lần ở Nhóm D.
- [Dòng 31](chapters/c5/chapter_5.tex#L31) — thêm **Hạn chế #3 (mới)**: yếu ở GC cực trị, trỏ `\ref{sec:loi_theo_gc}`; hướng khắc phục: tăng cường dữ liệu vùng GC cực trị + đặc trưng thành phần nucleotide.

### (H) Chỉnh hình thức
- Đổi em-dash `---` → dấu phẩy / "gồm …" (đoạn liệt kê 7 cấu hình).

---

## 3. Chương 2 — `chapters/c2/chapter_2.tex` *(H)*
Đổi em-dash `---` → dấu phẩy tại các vị trí:
- 6 định nghĩa viết tắt: `(Stochastic Gradient Descent, SGD)`, `(Convolutional Neural Network, CNN)`, `(Masked Language Modeling, MLM)`, `(Global Average Pooling, GAP)`, `(Global Max Pooling, GMP)`, `(Local Context-Aware, LCA)`.
- 4 chỗ ngắt/chèn câu (BPE token, PHACTS, PhaTYP–Prodigal, rò rỉ thông tin k-mer).

---

## 4. Abstract tiếng Anh — `chapters/abtract_en.tex` *(H)*
- Đổi `--- virulent or temperate ---` → `, virulent or temperate,`.

---

## 5. Hình ảnh — `figures/` *(N — tài nguyên)*
Thêm 2 file mới, copy từ `error_analysis/figures/` (đã đồng bộ lại nhiều lần theo bản ảnh người dùng cập nhật):

| File | Nguồn |
|---|---|
| [figures/error_confusion_matrix.png](figures/error_confusion_matrix.png) | `error_analysis/figures/confusion_matrix_by_group.png` |
| [figures/error_heatmap_length_gc.png](figures/error_heatmap_length_gc.png) | `error_analysis/figures/heatmap_lengthxGC.png` |

> Bản ảnh mới nhất: bố cục lưới 2×2 (confusion matrix), heatmap dạng phần trăm, số có dấu chấm phân tách hàng nghìn.

---

## Kiểm tra & nguồn số liệu
- ✅ Mọi con số trong bảng/đoạn mới khớp chính xác CSV trong `error_analysis/tables/` (`slice_by_group_class.csv`, `slice_by_gc_bin.csv`).
- ✅ CSV chạy lại nhiều lần trong session nhưng **giá trị không đổi** → bảng giữ nguyên.
- ✅ Citation dùng (`wu2021deephage`, `shang2023phatyp`, `feiner2015new`, `lin2017focal`) đều có trong `references.bib`; không thêm entry mới.
- ✅ Mọi `\label` mới có `\ref`; không còn undefined reference.
- ✅ Full 4-command compile sạch — `thesis.pdf` 74 trang.

## Lưu ý biên dịch
- Có `\label`/`\ref` mới → cần **full compile**: `pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex`.

## Ghi chú khác
- Không đụng tới `chapters/c1` và `chapters/c3` trong session này.
- Các `---` còn lại trong `chapters/c3/chapter_3.tex` (dòng 229/231/237) là ô bảng nghĩa "không áp dụng" — **cố ý giữ nguyên**, không phải ngắt câu.

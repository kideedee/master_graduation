# Nhật ký thay đổi — Session 2026-06-07

## Mục tiêu
Thống nhất tên mô hình trong luận văn: đổi các chỗ còn sót `PhaBERT-CNN` thành `PhaBERT`.

## Lý do
- Glossary ([chapters/glossary.tex:49](chapters/glossary.tex#L49)) định nghĩa tên chính thức của mô hình là **`PhaBERT`** (tên đầy đủ: "Phage BERT"), **không** chứa "CNN" trong acronym.
- "CNN" chỉ là một thành phần kiến trúc (mô-đun MKC — Multi-Kernel Convolution), đã có entry riêng trong glossary (dòng 12 `CNN`, dòng 45 `MKC`).
- Phần lớn luận văn đã dùng `PhaBERT`; chỉ còn 4 chỗ sót lại dùng `PhaBERT-CNN` → gây không nhất quán.

## Thay đổi đã thực hiện
Đổi `PhaBERT-CNN` → `PhaBERT` tại 4 vị trí:

| File | Dòng | Số chỗ |
|---|---|---|
| [chapters/c1/chapter_1.tex](chapters/c1/chapter_1.tex#L49) | 49 | 2 |
| [chapters/c3/chapter_3.tex](chapters/c3/chapter_3.tex#L16) | 16 | 1 |
| [chapters/c4/chapter_4.tex](chapters/c4/chapter_4.tex#L153) | 153 | 1 |

**Tổng:** 4 occurrence trong nội dung luận văn (`chapters/`).

## Kiểm tra sau thay đổi
- ✅ `chapters/*.tex` không còn `PhaBERT-CNN` nào.
- ✅ Nhất quán với glossary.
- Các occurrence còn lại nằm **ngoài** nội dung luận văn (không vào PDF): `CLAUDE.md` (metadata dự án), `implementation/phabert_cnn_model.py` (tên class code), `claude_old/` (config cũ) — không cần đổi.

## Lưu ý biên dịch
- Chỉ sửa text thuần, không thay đổi `references.bib` hay `\label`/`\ref`.
- Chỉ cần **quick compile**: `pdflatex thesis.tex` (1 lần) để cập nhật PDF.

## Ghi chú khác
- Thư mục `temp/` (bản nháp cũ chương 2) đã được người dùng xóa sạch file — chỉ còn thư mục rỗng, không ảnh hưởng PDF.

# Plan: Chương 4 — Chỉnh sửa văn phong và nội dung

## Tổng quan

Chương 4 có nội dung phân tích kỹ thuật tốt và cấu trúc logic rõ ràng. Tuy nhiên có một số vấn đề cần sửa: lỗi chính tả, inconsistency định dạng số, đoạn mở đầu liệt kê section máy móc, và không thống nhất thuật ngữ cross-chapter.

## Các vấn đề và giải pháp

### Vấn đề 1: Lỗi chính tả "hương pháp" → "phương pháp"
**Vị trí:** 
- Dòng 65: "sử dụng hương pháp kiểm chứng chéo"
- Dòng 69-70: caption bảng "theo hương pháp kiểm chứng chéo"

**Giải pháp:** Sửa thành "phương pháp" ở cả 2 chỗ.

### Vấn đề 2: Inconsistency dấu phân cách thập phân — dấu chấm vs dấu phẩy
**Hiện tại:**
- Bảng ablation (tab:ablation_results): dùng dấu PHẨY (82,54 / 87,38 / ...) — đúng chuẩn tiếng Việt
- Bảng main (tab:main_results): dùng dấu CHẤM (82.54 / 87.38 / ...) — sai chuẩn tiếng Việt
- Body text: phần lớn dùng dấu PHẨY, riêng dòng 109 dùng dấu CHẤM ("78.07\% đến 89.09\%")

**Giải pháp:** Thống nhất dấu PHẨY theo chuẩn tiếng Việt:
- Sửa tất cả số trong bảng tab:main_results: dấu chấm → dấu phẩy
- Sửa dòng 109: "78.07\%" → "78,07\%" và "89.09\%" → "89,09\%"

### Vấn đề 3: Inconsistency metric labels giữa 2 bảng
**Hiện tại:**
- Bảng ablation (tab:ablation_results): viết hoa "Sn", "Sp", "Acc"
- Bảng main (tab:main_results): viết thường "sn", "sp", "acc"

**Giải pháp:** Thống nhất viết hoa "Sn", "Sp", "Acc" (nhất quán với bảng ablation).

### Vấn đề 4: Inconsistency format dải bp trong header bảng
**Hiện tại:**
- Bảng ablation: "100--400 bp", "1.200--1.800 bp" (có dấu chấm phân nhóm)
- Bảng main: "100--400 bp", "1200--1800 bp" (KHÔNG dấu chấm phân nhóm)

**Giải pháp:** Thống nhất có dấu chấm phân nhóm: "1.200--1.800 bp", "800--1.200 bp" ở bảng main. Chuẩn tiếng Việt dùng dấu chấm cho phân nhóm hàng nghìn.

### Vấn đề 5: Đoạn mở đầu chương — liệt kê section máy móc  
**Hiện tại (dòng 4):** Câu đầu OK, nhưng sau đó liệt kê "Phần~\ref{sec:thiet_lap_thuc_nghiem} mô tả...; Phần~\ref{sec:tai_nguyen_tinh_toan} trình bày...; Phần~\ref{sec:ket_qua} trình bày...; Cuối cùng, Phần~\ref{sec:ket_luan_c4} tổng kết..."

Giống y hệt kiểu đã sửa ở Chương 3 — cần viết lại thành narrative.

**Giải pháp:** Viết lại thành narrative ngắn gọn, mô tả mạch logic thay vì liệt kê section references. Giữ câu đầu, thay phần liệt kê section bằng mô tả tuần tự logic.

### Vấn đề 6: Lỗi chính tả "gene" → "gen"
**Vị trí:** Dòng 121: "công cụ dự đoán gene"
**Giải pháp:** Sửa thành "gen" — đúng chuẩn tiếng Việt (tương tự Chương 3).

### Vấn đề 7: Thuật ngữ không nhất quán "kiểm chứng chéo" vs "kiểm định chéo"
**Hiện tại:**
- Chương 1, 3: dùng "kiểm định chéo"
- Chương 4 (dòng 9, 65, 69, 140): dùng "kiểm chứng chéo"
- Chương 5 (dòng 9): dùng "kiểm chứng chéo"
- vietnamese-terms.md: "Kiểm định chéo" là canonical

**Giải pháp:** Sửa tất cả "kiểm chứng chéo" → "kiểm định chéo" trong Chương 4 (4 chỗ). [Chương 5 sẽ sửa khi review C5.]

### Vấn đề 8: Thuật ngữ "dữ liệu siêu hệ gen" vs "dữ liệu metagenomic"
**Vị trí:** 
- Dòng 9: "phân tích dữ liệu siêu hệ gen"
- Dòng 135: "phân tích siêu hệ gen"

**Phân tích:** Chương 1, 2 dùng "dữ liệu metagenomic" hoặc "metagenomics" — không dùng "siêu hệ gen". Chương 5 dùng "dữ liệu siêu hệ gen". Glossary: "Metagenomics → Hệ metagenomics".

**Giải pháp:** Giữ nguyên. "Siêu hệ gen" là từ Việt hóa hợp lệ cho metagenomics, tương đương "dữ liệu metagenomic". Không có inconsistency nghiêm trọng.

### Vấn đề 9: Câu kết luận chương cuối — transition sang Chương 5
**Hiện tại (dòng cuối):** "Chương tiếp theo tổng kết các đóng góp của nghiên cứu, thảo luận các hạn chế và đề xuất hướng phát triển trong tương lai." — OK, đủ cụ thể.

**Giải pháp:** Giữ nguyên. Câu chuyển tiếp đủ cụ thể, không cần sửa.

## Tóm tắt thay đổi

| # | Section | Thay đổi |
|---|---------|----------|
| 1 | Bảng main + dòng 109 | Sửa lỗi chính tả "hương pháp" → "phương pháp" |
| 2 | Bảng main (tab:main_results) + dòng 109 | Thống nhất dấu phẩy thập phân |
| 3 | Bảng main | Thống nhất "sn"→"Sn", "sp"→"Sp", "acc"→"Acc" |
| 4 | Bảng main header | Thống nhất "1200"→"1.200", "800--1200"→"800--1.200" |
| 5 | Đoạn mở đầu chương | Viết lại thành narrative |
| 6 | Thảo luận (dòng 121) | Sửa "gene" → "gen" |
| 7 | Toàn chương | Sửa "kiểm chứng chéo" → "kiểm định chéo" (4 chỗ) |

## Citation keys (đã xác minh — 15/15 OK)
- `wu2021deephage` — ✓ EXISTS
- `ghurye2016metagenomic` — ✓ EXISTS
- `shang2023phatyp` — ✓ EXISTS
- `hyatt2010prodigal` — ✓ EXISTS
- `zhou2023dnabert` — ✓ EXISTS
- `zhang2024deeppl` — ✓ EXISTS
- `kim2014convolutional` — ✓ EXISTS
- `azimi2019phage` — ✓ EXISTS
- `feiner2015new` — ✓ EXISTS
- `ligeti2024prokbert` — ✓ EXISTS
- `sennrich2015neural` — ✓ EXISTS
- `howard2018universal` — ✓ EXISTS
- `devlin2019bert` — ✓ EXISTS
- `trimble2012short` — ✓ EXISTS
- `raffel2020exploring` — ✓ EXISTS

## File cần sửa
- `chapters/c4/chapter_4.tex` — toàn bộ chỉnh sửa trong file duy nhất này

## Lưu ý
- KHÔNG thêm citation mới
- KHÔNG thay đổi \label{} hay section structure
- KHÔNG thay đổi nội dung kỹ thuật, số liệu kết quả, công thức, hình
- Giữ nguyên tên section, chỉ sửa nội dung/văn phong bên trong

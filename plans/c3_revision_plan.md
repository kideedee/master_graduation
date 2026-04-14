# Plan: Chương 3 — Chỉnh sửa văn phong và nội dung

## Tổng quan

Chương 3 có nội dung kỹ thuật tốt và đầy đủ. Các vấn đề chính cần sửa thuộc về **văn phong**: cross-reference máy móc, đoạn mở đầu chương liệt kê section kiểu danh sách, thiếu chuyển tiếp giữa các mục, lỗi chính tả, và inconsistency định dạng tiêu đề.

## Các vấn đề và giải pháp

### Vấn đề 1: Đoạn mở đầu chương (dòng 4) — liệt kê section máy móc
**Hiện tại:** "Chương được tổ chức thành các phần chính: Phần~\ref{sec:overview} giới thiệu...; Phần~\ref{sec:data_preprocessing} mô tả...; Phần~\ref{sec:architecture} trình bày..."
- Kiểu danh sách section với dấu chấm phẩy, không phải narrative
- Thiếu section `\ref{sec:training_strategy}` trong danh sách
- Câu cuối chỉ liệt kê, không cho thấy mạch logic

**Giải pháp:** Viết lại thành đoạn narrative ngắn gọn, mô tả mạch logic của chương thay vì liệt kê từng section. Tương tự cách Chapter 1 mô tả bố cục — nêu vai trò/câu hỏi mỗi phần giải quyết, không phải nội dung chi tiết.

**Đề xuất nội dung mới:** Giữ 2 câu đầu (mô tả phương pháp), viết lại câu 3 thành: "Chương trình bày tuần tự từ tổng quan phương pháp, qua quy trình xây dựng dữ liệu, đến kiến trúc mô hình và chiến lược huấn luyện."

### Vấn đề 2: Cross-reference máy móc "Chi tiết X được trình bày trong Phần Y"
**Vị trí:**
- Dòng 16: "Chi tiết kiến trúc của PhaBERT-CNN được trình bày trong Phần~\ref{sec:architecture}."
- Dòng 18: "Chi tiết chiến lược huấn luyện được trình bày trong Phần~\ref{sec:training_strategy}."

**Giải pháp:** Bỏ cả hai câu. Đoạn trước mỗi câu đã đủ nội dung; reader sẽ đọc tiếp theo thứ tự chương mà không cần chỉ dẫn.

### Vấn đề 3: Lỗi chính tả "cửa số" → "cửa sổ"
**Vị trí:** Dòng 137 — xuất hiện 2 lần "cửa số tích chập" thay vì "cửa sổ tích chập"
**Giải pháp:** Sửa cả 2 lần thành "cửa sổ"

### Vấn đề 4: Inconsistency Title Case trong tiêu đề subsection
**Hiện tại:**
- Dòng 162: `\subsection{Kết Hợp Đặc Trưng và Đầu Phân Loại}` — Title Case
- Dòng 193: `\subsection{Giai Đoạn 1: Khởi Động}` — Title Case
- Dòng 197: `\subsection{Giai Đoạn 2: Tinh Chỉnh Đầy Đủ}` — Title Case
- Dòng 201: `\subsection{Hàm mục tiêu và kỹ thuật Regularization}` — Mixed
- Các subsection khác: "Mạng nền DNABERT-2", "Mô-đun MKC" — sentence case

**Giải pháp:** Thống nhất sentence case cho tất cả subsection (chuẩn tiếng Việt):
- "Kết hợp đặc trưng và đầu phân loại"
- "Giai đoạn 1: Khởi động"
- "Giai đoạn 2: Tinh chỉnh đầy đủ"
- "Hàm mục tiêu và kỹ thuật regularization"

### Vấn đề 5: "gene" vs "gen"
**Vị trí:** Dòng 9, 12 — "công cụ dự đoán gene"
**Giải pháp:** Sửa thành "gen" — đúng chính tả tiếng Việt. Thuật ngữ canonical trong vietnamese-terms.md là "gen đánh dấu" (không phải "gene").

### Vấn đề 6: Thiếu chuyển tiếp giữa các section
**Vị trí:**
- Cuối sec:overview (trước sec:data_preprocessing): Không có câu nối → sec:data_preprocessing bắt đầu đột ngột
- Cuối sec:data_preprocessing (trước sec:architecture): Không có câu nối
- Cuối sec:architecture (trước sec:training_strategy): Không có câu nối

**Giải pháp:** Thêm câu chuyển tiếp cuối mỗi section:
- Cuối overview: "Trước khi đi vào kiến trúc mô hình, phần tiếp theo trình bày quy trình xây dựng dữ liệu huấn luyện và kiểm định." → KHÔNG, kiểu này vẫn máy móc. Tốt hơn: thêm ý nối logic tự nhiên.
- Cuối data_preprocessing: Bảng thống kê đã kết thúc tốt, section architecture bắt đầu bằng tổng quan 3 thành phần — flow OK.
- Cuối architecture: Câu cuối subsection softmax/argmax kết thúc gọn, cần nối sang training.

**Quyết định:** Chỉ thêm transition ở 2 chỗ thực sự cần:
1. Cuối sec:overview (sau khi bỏ "Chi tiết chiến lược...") — cần câu kết nối sang data
2. Cuối sec:architecture (sau dòng 186) — cần câu kết nối sang training strategy

### Vấn đề 7: Kết luận chương quá ngắn gọn
**Hiện tại (dòng 241-243):** 3 câu tóm tắt + 1 câu chuyển tiếp. Nội dung ổn nhưng câu cuối "Chương tiếp theo trình bày thiết kế thực nghiệm..." hơi generic.

**Giải pháp:** Sửa nhẹ câu cuối để cụ thể hơn: nêu rõ sẽ so sánh với phương pháp nào, trên loại dữ liệu nào.

### Vấn đề 8: Dòng 34 — câu quá dài về cửa sổ trượt
**Hiện tại:** Câu bắt đầu "Để mô phỏng kịch bản này..." chứa cả mô tả phương pháp, công thức, và giải thích tham số — hơn 80 từ.

**Giải pháp:** Chia thành 2-3 câu ngắn hơn.

## Tóm tắt thay đổi theo section

| Section | Thay đổi |
|---------|----------|
| Đoạn mở đầu chương | Viết lại câu 3 thành narrative |
| Tổng quan phương pháp | Bỏ 2 câu cross-ref máy móc, sửa "gene"→"gen", thêm transition cuối |
| Thu thập dữ liệu | Chia câu dài dòng 34 |
| Kiến trúc PhaBERT-CNN | Sửa "cửa số"→"cửa sổ", sửa Title Case subsection, thêm transition cuối |
| Chiến lược huấn luyện | Sửa Title Case subsection |
| Kết luận | Cụ thể hóa câu chuyển tiếp cuối |

## Citation keys (đã xác minh)
- `zhou2023dnabert` — ✓ EXISTS
- `kim2014convolutional` — ✓ EXISTS
- `wu2021deephage` — ✓ EXISTS
- `mavrich2017bacteriophage` — ✓ EXISTS
- `zhang2024deeppl` — ✓ EXISTS
- `sennrich2015neural` — ✓ EXISTS
- `press2021train` — ✓ EXISTS
- `johnson2017deep` — ✓ EXISTS
- `howard2018universal` — ✓ EXISTS
- `loshchilov2017decoupled` — ✓ EXISTS
- `smith2019super` — ✓ EXISTS

## File cần sửa
- `chapters/c3/chapter_3.tex` — toàn bộ chỉnh sửa trong file duy nhất này

## Lưu ý
- KHÔNG thêm citation mới
- KHÔNG thay đổi \label{} hay section structure
- KHÔNG thay đổi nội dung kỹ thuật, công thức, bảng, hình
- Giữ nguyên tên section, chỉ sửa nội dung/văn phong bên trong

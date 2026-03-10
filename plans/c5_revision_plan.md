# Plan: Sửa đổi Chương 5 (Kết luận)

## I. Mục tiêu
Sửa các vấn đề trong chương 5:
1. Bổ sung trích dẫn cho các số liệu
2. Cải thiện cấu trúc câu (chia câu dài thành câu ngắn hơn)
3. Đảm bảo tính nhất quán với các chương trước

## II. Các thay đổi cụ thể

### 1. Section 5.1 (Tóm tắt đóng góp)
**Vấn đề:** Câu đầu tiên quá dài (dòng 8-9), thiếu trích dẫn cho các số liệu

**Sửa:**
- Chia câu dài thành 2-3 câu ngắn hơn
- Thêm trích dẫn cho các số liệu: 81.59%, 87.91%, 90.01%, 0.91-5.98%, 90.69%
- Các số liệu này đến từ chương 4 (kết quả thực nghiệm), cần tham chiếu đến bảng/hình trong chương 4

**Trích dẫn cần thêm:**
- Tham chiếu đến Bảng kết quả trong chương 4 (cần kiểm tra label chính xác)
- Có thể cần thêm \ref{tab:...} hoặc \ref{fig:...}

### 2. Section 5.2 (Phân tích kết quả)
**Vấn đề:**
- Dòng 14: Câu quá dài với nhiều mệnh đề phụ
- Dòng 16: Thiếu trích dẫn cho số liệu "0.07%", "3.43%", "6.90%"

**Sửa:**
- Chia câu dài thành câu ngắn hơn
- Thêm trích dẫn cho các số liệu từ chương 4
- Đảm bảo các trích dẫn \cite{hyatt2010prodigal}, \cite{trimble2012short} đã có trong references.bib

### 3. Section 5.3 (Hướng nghiên cứu tương lai)
**Vấn đề:** Nội dung tốt nhưng có thể cải thiện cấu trúc

**Sửa:**
- Giữ nguyên nội dung chính
- Có thể thêm bullet points để dễ đọc hơn (tùy chọn)

### 4. Section 5.4 (Kết luận)
**Vấn đề:** Câu cuối hơi dài

**Sửa:**
- Chia thành 2 câu để dễ đọc hơn
- Nhấn mạnh ý nghĩa thực tiễn

## III. Danh sách trích dẫn cần kiểm tra

Các trích dẫn đã có trong chapter_5.tex:
- \cite{hyatt2010prodigal} - dòng 14
- \cite{trimble2012short} - dòng 14

Cần thêm:
- Tham chiếu đến bảng/hình kết quả trong chương 4 (sử dụng \ref{})

## IV. Số liệu cần verify

Tất cả các số liệu trong chương 5 đều đến từ kết quả thực nghiệm trong chương 4:
- 81.59% (Nhóm A accuracy)
- 87.91% (Nhóm B accuracy)
- 90.01% (Nhóm C accuracy)
- 90.69% (Nhóm D accuracy)
- 0.91-5.98% (cải thiện so với baseline)
- 0.07% (cải thiện ở Nhóm A)
- 3.43% (cải thiện ở Nhóm D)
- 6.90% (cải thiện specificity ở Nhóm A)

Cần kiểm tra xem các số này có khớp với chương 4 không.

## V. Terminology check

Các thuật ngữ cần kiểm tra với vietnamese-terms.md:
- Thực khuẩn thể / Phage ✓
- Contig ✓
- BPE tokenization ✓
- Attention pooling ✓
- CNN đa tỷ lệ / Multi-scale CNN ✓
- Nhánh song song kép / Dual parallel branches ✓
- Stratified k-fold cross-validation ✓
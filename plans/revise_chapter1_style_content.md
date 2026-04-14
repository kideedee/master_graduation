# Plan: Chỉnh sửa nội dung và văn phong Chương 1

## Bối cảnh
Chương 1 cần chỉnh sửa dựa trên: (a) nội dung thực tế từ Chương 3, 4, 5; (b) best practices về viết Introduction cho luận văn thạc sĩ. Yêu cầu cụ thể của người dùng: bỏ kiểu "xem Mục x để biết thêm chi tiết", cải thiện văn phong tổng thể.

## Các vấn đề phát hiện và giải pháp

### Vấn đề 1: Cross-reference máy móc — "xem Mục X để biết thêm chi tiết"
**Vị trí:** Dòng 7, 9, 18
- Dòng 7: `(xem Mục~\ref{subsec:bacteriophage} để biết thêm chi tiết)` — ngoặc đơn + "để biết thêm chi tiết"
- Dòng 9: `(xem Mục~\ref{subsec:metagenomics} để biết thêm chi tiết)` — tương tự
- Dòng 18: `Tổng quan chi tiết về từng phương pháp và phân tích khoảng trống nghiên cứu được trình bày tại Mục~\ref{sec:phage_classification_methods} và Mục~\ref{subsec:comparison_gaps}.`

**Giải pháp:** Lồng cross-reference tự nhiên vào nội dung. Thay vì dùng ngoặc đơn chú thích, viết dạng narrative: "Sinh học của thực khuẩn thể và metagenomics được trình bày chi tiết trong Chương~\ref{chap:theory}" chỉ ở phần bố cục luận văn, hoặc bỏ hẳn cross-reference nếu không cần thiết (Chapter 1 nên tự đủ, chỉ forward-ref ở phần bố cục).

**Hành động cụ thể:**
- Dòng 7: Bỏ `(xem Mục~\ref{subsec:bacteriophage} để biết thêm chi tiết)` hoàn toàn — thông tin về sinh học phage đã đủ ngay trong câu
- Dòng 9: Bỏ `(xem Mục~\ref{subsec:metagenomics} để biết thêm chi tiết)` — thông tin metagenomics đã đủ
- Dòng 18: Viết lại câu cuối mục Thách thức, lồng tham chiếu tự nhiên thay vì liệt kê Mục

### Vấn đề 2: Mục "Bố cục luận văn" (sec:organization) quá máy móc
**Vị trí:** Dòng 54-64
- Hiện tại: Liệt kê từng chương bằng **bold Chương X** rồi mô tả nội dung — kiểu "Chapter 1 does X, Chapter 2 does Y"
- Không cho thấy mạch logic xuyên suốt, chỉ là danh sách

**Giải pháp:** Viết lại thành đoạn văn narrative, mỗi chương được mô tả bằng vai trò trong chuỗi logic nghiên cứu, không bold tên chương riêng từng dòng. Dùng `\ref{}` tự nhiên.

### Vấn đề 3: Mục "Phạm vi nghiên cứu" (sec:scope) — đoạn hạn chế dài dòng, kiểu liệt kê thủ thế
**Vị trí:** Dòng 49
- "Thứ nhất, luận văn không xem xét...", "Thứ hai...", "Thứ ba...", "Thứ tư..." — 4 hạn chế liên tiếp, giọng phòng thủ
- Quá chi tiết cho Introduction — một số hạn chế phù hợp hơn ở Chương 5

**Giải pháp:** Giữ phạm vi (scope) ngắn gọn 1 đoạn. Gộp các hạn chế thành 2-3 ý chính viết bằng prose tự tin, thay vì liệt kê phòng thủ. Bỏ hạn chế về contig mô phỏng vs thực tế (đã thảo luận đầy đủ ở Chương 5).

### Vấn đề 4: Mục "Đóng góp" (sec:contributions) — con số chưa khớp hoàn toàn
**Vị trí:** Dòng 40
- `82,26--91,34\%` và `0,32--6,61\%` — cần verify lại với Chương 4
- Từ Chương 4: PhaBERT-CNN đạt 82,26%, 87,38%, 90,01%, 91,34% → OK
- Cải thiện vs PhaTYP 0,32-3,34%, vs DeePhage 2,25-4,19%, vs ProkBERT 1,58-6,61% → "cải thiện 0,32--6,61% so với các phương pháp tiên tiến" là đúng

**Giải pháp:** Con số OK, nhưng đóng góp 3 và 4 cần chỉnh văn phong: đóng góp 3 dùng "(chi tiết tại Chương~\ref{chap:thuc_nghiem_danh_gia})" — nên bỏ cross-ref trong danh sách đóng góp, chỉ nêu kết quả gọn.

### Vấn đề 5: Văn phong — một số câu quá dài, lặp ý
**Vị trí:** Nhiều nơi
- Dòng 7: Câu dài 6 dòng, chứa quá nhiều thông tin
- Dòng 16: Mục thách thức câu quá dài "Bên cạnh các thách thức sinh học..."
- Dòng 47: "Phương pháp sử dụng DNABERT-2 làm mô hình nền tảng hệ gen và được đánh giá thông qua kiểm định chéo 5 phần phân tầng với các chỉ số độ nhạy, độ đặc hiệu và độ chính xác." — chi tiết quá cho phần phạm vi ở Chapter 1

**Giải pháp:** Chia câu dài, bỏ chi tiết kỹ thuật không cần thiết ở Introduction.

### Vấn đề 6: Transition giữa các mục
- Không có câu chuyển tiếp giữa "Đặt vấn đề" → "Thách thức nghiên cứu" → "Mục tiêu"
- Mỗi section bắt đầu đột ngột

**Giải pháp:** Thêm câu nối cuối mỗi mục, tạo mạch logic: bối cảnh → thách thức → mục tiêu → đóng góp → phạm vi → bố cục.

## Tóm tắt thay đổi theo section

| Section | Thay đổi |
|---------|----------|
| Đặt vấn đề | Bỏ 2 "(xem Mục X để biết thêm chi tiết)", chia câu dài, thêm transition |
| Thách thức | Viết lại câu cuối (bỏ cross-ref máy móc), thêm transition |
| Mục tiêu | Giữ nguyên cơ bản, chỉnh nhẹ văn phong |
| Đóng góp | Bỏ "(chi tiết tại Chương~\ref{...})" trong mục 3, giữ con số |
| Phạm vi | Gộp hạn chế, viết prose tự tin thay vì liệt kê Thứ nhất/Thứ hai/..., bỏ hạn chế thứ 4 (contig mô phỏng — để Chương 5) |
| Bố cục | Viết lại thành narrative paragraph thay vì bold từng chương |

## File cần sửa
- `chapters/c1/chapter_1.tex` — toàn bộ chỉnh sửa trong file duy nhất này

## Lưu ý
- KHÔNG thêm citation mới — chỉ dùng citation đã có
- KHÔNG thay đổi \label{} hay section structure
- Giữ nguyên tên section, chỉ sửa nội dung bên trong
- Vietnamese terminology phải nhất quán với vietnamese-terms.md
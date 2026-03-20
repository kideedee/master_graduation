# Plan: Chương 3 — Chỉnh sửa toàn diện theo chuẩn văn phong khoa học

## Phân tích hiện trạng

Chương 3 hiện tại đã có nội dung kỹ thuật tốt, nhưng cần chỉnh sửa để đạt chuẩn văn phong luận văn thạc sĩ/bài báo khoa học. Các vấn đề chính:

1. **Trùng lặp nội dung với Chương 2**: Phần 3.1 (Tổng quan phương pháp) lặp lại đánh giá các phương pháp PHACTS, PhageAI, DeePhage, PhaTYP, DeepPL — đã trình bày chi tiết ở C2 Mục 2.4
2. **Trùng lặp nội dung với Chương 4**: Phần 3.1 trích dẫn số liệu kết quả (accuracy 78.07--89.09%, 91.02%, 94.65%) — thuộc về chương thực nghiệm
3. **Bảng dữ liệu chưa hoàn thiện**: Bảng `tab:dataset_statistics` còn TODO, bảng `tab:sliding_window_params` bị comment out
4. **Phần chiến lược huấn luyện quá ngắn**: Thiếu chi tiết hyperparameters, hàm mất mát, regularization (đã bị comment out)
5. **Thiếu hình minh họa quy trình tiền xử lý dữ liệu**: Hình `data_preparation.png` tồn tại nhưng chưa được sử dụng
6. **Văn phong chưa đồng nhất**: Một số chỗ dùng "học viên", một số chỗ dùng câu bị động — cần thống nhất
7. **Phần kết luận chương lặp lại quá nhiều chi tiết kỹ thuật** thay vì tóm tắt đóng góp

## Outline chỉnh sửa

<!-- PLACEHOLDER_OUTLINE_DETAILS -->

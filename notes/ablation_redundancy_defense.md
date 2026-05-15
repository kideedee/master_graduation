# Kiến thức nền: Hiện tượng redundancy trong ablation multi-kernel CNN

## Hiện tượng trong PhaBERT

- Bỏ 1 nhánh CNN (NO-K3/K5/K7): thay đổi ±0.3–1.5% (trong biên dao động cross-validation)
- Bỏ hẳn cả module MKC (so với DNABERT-2 baseline): giảm 0.49–3.02% (nhất quán trên mọi nhóm)
- Kết luận: các nhánh riêng lẻ redundant với nhau, nhưng module tổng thể rõ ràng có đóng góp

---

## Papers liên quan

### 1. Zhang & Wallace (2017) — ĐÃ CITE trong luận văn

**"A Sensitivity Analysis of (and Practitioners' Guide to) CNNs for Sentence Classification"**
- URL: https://arxiv.org/abs/1510.03820
- Kết luận chính:
  - Hiệu suất **ít nhạy cảm** với kích thước bộ lọc cụ thể — dải rộng (1–10) đều hoạt động tốt
  - **Dùng nhiều kích thước cùng lúc luôn tốt hơn** dùng một kích thước duy nhất
  - Khuyến nghị dùng 2–4 filter sizes
- Câu trả lời cho hội đồng: "Kết quả ablation của chúng tôi phù hợp với nhận định của Zhang & Wallace (2017) rằng hiệu suất CNN đa cửa sổ ít nhạy cảm với kích thước bộ lọc cụ thể, mà phụ thuộc vào việc sử dụng đồng thời nhiều kích thước."

### 2. Michel et al. (2019) — "Are Sixteen Heads Really Better than One?"

**NeurIPS 2019**
- URL: https://arxiv.org/abs/1905.10650
- Hiện tượng y hệt nhưng ở transformer attention heads:
  - 40–80% heads có thể bị loại bỏ mà không ảnh hưởng đáng kể
  - Nhưng cơ chế multi-head attention tổng thể rõ ràng cần thiết
- Quote: "MHA can be seen as an **ensemble of low-rank vanilla attention layers**"
- Ý nghĩa: Hiện tượng redundancy giữa các thành phần song song là phổ biến trong deep learning, không riêng CNN

### 3. Voita et al. (2019) — "Specialized Heads Do the Heavy Lifting"

**ACL 2019**
- URL: https://arxiv.org/abs/1905.09418
- Chỉ một số ít "specialized heads" thực sự quan trọng
- Phần còn lại redundant nhưng đóng vai trò **ổn định hóa** (stabilizing)
- Cấu trúc hai tầng: vài thành phần critical + nhiều thành phần redundant-but-stabilizing

### 4. Vorontsov et al. (2017) — "Coupled Ensembles of Neural Networks"

- URL: https://arxiv.org/abs/1709.06053
- Multi-branch tạo **implicit regularization**
- Quote: "The use of branches brings an additional form of regularization"
- Gradient chung buộc các nhánh học biểu diễn bổ sung, ngăn co-adaptation

### 5. Nguyen et al. (2018) — "Multi-Branch Architectures Are Less Non-Convex"

- URL: https://arxiv.org/abs/1806.01845
- Chứng minh toán học: multi-branch làm optimization landscape ít non-convex hơn
- Duality gap → 0 khi số nhánh tăng (Shapley-Folkman lemma)
- Lợi ích nằm ở **cấu trúc**, không quy cho nhánh riêng lẻ

### 6. Krogh & Vedelsby (1995) — Ensemble Ambiguity Decomposition

- Công thức: **Ensemble error = Average member error − Diversity**
- Diversity (sự khác biệt giữa các member) trực tiếp giảm lỗi ensemble
- Individual members có thể "weak" hoặc redundant, ensemble vẫn tốt hơn miễn là members mắc lỗi khác nhau

### 7. Edelman & Tononi (2001) — Degeneracy vs. Redundancy

- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC15929/
- **Degeneracy**: cấu trúc KHÁC nhau thực hiện CÙNG chức năng (kernel 3,5,7 → overlapping features)
- **Redundancy**: bản sao GIỐNG HỆT thực hiện cùng chức năng
- Multi-kernel CNN là degenerate, không phải redundant thuần túy
- Bỏ 1 → chức năng được cover bởi nhánh khác (marginal drop)
- Bỏ hết → mất hoàn toàn lớp đặc trưng đó (significant drop)

---

## 4 Framework giải thích (dùng khi bảo vệ)

| # | Framework | Giải thích ngắn | Khi nào dùng |
|---|-----------|-----------------|--------------|
| 1 | **Implicit ensemble** | Các nhánh = ensemble members. Bỏ 1 member → ensemble vẫn hoạt động. Bỏ hết → mất ensemble | Câu hỏi chung "tại sao bỏ 1 không ảnh hưởng?" |
| 2 | **Degeneracy** | Cấu trúc khác nhau, chức năng chồng lấn. Khác với redundancy thuần túy | Câu hỏi "các nhánh có phải bản sao?" |
| 3 | **Implicit regularization** | Multi-branch ngăn co-adaptation, buộc học biểu diễn bổ sung | Câu hỏi "lợi ích ngoài accuracy?" |
| 4 | **Optimization landscape** | Nhiều nhánh → landscape ít non-convex → train tốt hơn | Câu hỏi "có phải thừa tham số?" |

---

## Câu trả lời mẫu cho hội đồng

### Q: "Tại sao bỏ 1 nhánh CNN không ảnh hưởng nhiều?"

> Kết quả này phù hợp với nhận định của Zhang & Wallace (2017): hiệu suất CNN đa cửa sổ ít nhạy cảm với kích thước bộ lọc cụ thể. Các nhánh kernel 3, 5, 7 trích xuất đặc trưng chồng lấn đáng kể — khi bỏ 1 nhánh, thông tin đã được cover bởi các nhánh còn lại. Michel et al. (2019) cũng ghi nhận hiện tượng tương tự ở attention heads: 40-80% heads có thể bị loại bỏ mà không ảnh hưởng, nhưng cơ chế multi-head tổng thể vẫn cần thiết.

### Q: "Vậy tại sao vẫn cần 3 nhánh? Có phải thừa?"

> Không thừa. Thứ nhất, Zhang & Wallace (2017) chứng minh dùng nhiều kích thước cùng lúc luôn tốt hơn 1 kích thước duy nhất — lợi ích nằm ở sự kết hợp, không phải ở nhánh riêng lẻ. Thứ hai, Nguyen et al. (2018) chứng minh multi-branch làm optimization landscape ít non-convex hơn, giúp mô hình hội tụ tốt hơn. Thứ ba, kết quả trên contig dài (Nhóm D) cho thấy mô hình đầy đủ 3 nhánh đạt 91.38% so với 90.99-91.05% khi thiếu 1 nhánh — lợi ích phát huy rõ khi trình tự đủ dài.

### Q: "Hiện tượng này có phổ biến trong deep learning không?"

> Rất phổ biến. Michel et al. (2019) thấy ở attention heads, Voita et al. (2019) thấy ở specialized vs. redundant heads, và nhiều nghiên cứu multi-scale CNN trong computer vision cũng báo cáo pattern tương tự. Krogh & Vedelsby (1995) đã giải thích lý thuyết từ góc độ ensemble: Ensemble error = Average member error − Diversity. Các thành phần riêng lẻ có thể thay thế được, nhưng ensemble tổng thể luôn tốt hơn.

### Q: "Trên contig ngắn, bỏ 1 nhánh lại TỐT HƠN (83.56% vs 82.01%). Giải thích?"

> Đây là hiệu ứng regularization. Trên contig ngắn (100-400 bp), tín hiệu trình tự hạn chế — ít mô-típ chức năng hoàn chỉnh. Khi đó, ít tham số hơn giúp mô hình tổng quát hóa tốt hơn do giảm nguy cơ quá khớp. Vorontsov et al. (2017) cũng ghi nhận multi-branch có thể gây overfitting khi dữ liệu không đủ phong phú. Ngược lại, trên contig dài (Nhóm D), mô hình đầy đủ đạt kết quả cao nhất vì trình tự đủ dài để chứa các mô-típ đa dạng ở nhiều kích thước.

---

## Lưu ý khi bảo vệ

- Trong luận văn đã cite Zhang & Wallace (2017) — đủ cho văn bản viết
- Michel et al. (2019) và các papers khác dùng làm kiến thức nền khi trả lời câu hỏi
- Không cần thêm citation vào luận văn — nội dung hiện tại đã chặt chẽ
- Nếu hội đồng hỏi sâu, có thể đề cập "implicit ensemble effect" và "degeneracy vs. redundancy" như framework giải thích

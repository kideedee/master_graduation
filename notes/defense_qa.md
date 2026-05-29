# Câu hỏi dự kiến từ hội đồng bảo vệ

Luận văn: PhaBERT — Phân loại hệ gen thực khuẩn dựa trên phương pháp học sâu
Học viên: Vũ Quang Sơn | GVHD: TS. Điệp Thị Hoàng | VNU-UET 2025

---

## 1. Kiến trúc và thiết kế

### Q1.1: Tại sao chọn DNABERT-2 mà không phải các mô hình nền tảng hệ gen khác (Hyena-DNA, Evo, Nucleotide Transformer)?

> **Trả lời:** DNABERT-2 được chọn vì ba lý do:
> 1. **BPE tokenization** — tạo token không chồng lấn, loại bỏ rò rỉ thông tin (vấn đề chính của ProkBERT dùng k-mer chồng lấn)
> 2. **ALiBi positional encoding** — cho phép ngoại suy độ dài tốt, không bị giới hạn bởi positional embedding cố định như DNABERT gốc (512bp)
> 3. **Tiền huấn luyện đa loài** — đã được kiểm chứng trên nhiều tác vụ hạ nguồn trong sinh tin học
>
> Hyena-DNA và Evo là các mô hình mới hơn, chủ yếu tập trung vào trình tự rất dài (>10K bp). Bài toán của chúng tôi xử lý contig 100-1800bp — DNABERT-2 phù hợp hơn về mặt quy mô.

### Q1.2: MKC có 3 kernel sizes (3, 5, 7). Tại sao chọn các giá trị này? Đã thử các giá trị khác chưa?

> **Trả lời:** Bộ kernel (3, 5, 7) kế thừa từ TextCNN (Kim, 2014) — kiến trúc đã được kiểm chứng rộng rãi cho phân loại văn bản. Zhang & Wallace (2017) chứng minh rằng hiệu suất CNN đa cửa sổ ít nhạy cảm với kích thước bộ lọc cụ thể, mà phụ thuộc vào việc sử dụng đồng thời nhiều kích thước. Kết quả ablation của chúng tôi cũng xác nhận điều này: bỏ bất kỳ 1 nhánh nào chỉ thay đổi ±0.3-1.5%, nằm trong biên dao động cross-validation.
>
> Chúng tôi không thử các bộ kernel khác (ví dụ 5, 7, 9) vì mục tiêu chính là đánh giá đóng góp của module MKC tổng thể so với baseline, không phải tối ưu hóa hyperparameter cho kernel size.

### Q1.3: Masked average pooling có gì khác so với attention pooling thông thường?

> **Trả lời:** Masked average pooling tính trung bình trên tất cả token positions, nhưng loại trừ các padding tokens thông qua attention mask. Khác với attention pooling (DNABERT-2-P trong ablation) vốn học trọng số cho từng position, masked average pooling coi mọi token thực đều quan trọng như nhau.
>
> Kết quả ablation cho thấy: attention pooling (DNABERT-2-P) tốt hơn trên contig ngắn (nhóm A: 83,54% vs 82,18%) vì tập trung vào vùng thông tin cao khi tín hiệu hạn chế. CNN đa cửa sổ (DNABERT-2-CNN) tốt hơn trên contig dài (nhóm C: 90,16% vs 89,88%). PhaBERT kết hợp cả hai → cân bằng nhất trên toàn phổ độ dài.

---

## 2. Dữ liệu và phương pháp đánh giá

### Q2.1: Làm sao đảm bảo không có rò rỉ dữ liệu giữa train và validation?

> **Trả lời:** Chúng tôi chia tách ở **mức genome**, không phải mức contig. Tất cả contig được tạo từ cùng 1 genome chỉ xuất hiện trong 1 fold duy nhất. Điều này đảm bảo mô hình không thể "nhớ" các đoạn trình tự từ cùng genome trong tập train để dự đoán trên tập validation.
>
> Ngoài ra, BPE tokenization tạo token không chồng lấn — khác với k-mer chồng lấn (ProkBERT) vốn gây rò rỉ thông tin giữa các token liền kề trong quá trình tiền huấn luyện.

### Q2.2: Random undersampling loại bỏ dữ liệu lớp đa số. Tại sao không dùng class weighting hoặc focal loss?

> **Trả lời:** Chúng tôi đã nhận diện đây là hạn chế trong luận văn. Lý do chọn undersampling:
> 1. **Đơn giản và hiệu quả** — giảm thời gian train đáng kể (ít mẫu hơn)
> 2. **Phù hợp với quy mô dữ liệu** — sau bước cửa sổ trượt + RC, số contig rất lớn (460K cho nhóm A). Undersampling vẫn giữ 230K mẫu/lớp — đủ lớn
> 3. **Tập validation giữ nguyên phân bố gốc** — đánh giá trên phân bố thực tế
>
> Class weighting và focal loss đã được thử nghiệm sơ bộ nhưng không cải thiện đáng kể trên tập dữ liệu này, có thể do kích thước tập train sau undersampling đã đủ lớn. Đây là hướng nghiên cứu tiếp theo cần đánh giá có hệ thống.

### Q2.3: Tại sao dùng 5-fold CV thay vì train/val/test split cố định?

> **Trả lời:** 5-fold stratified cross-validation được chọn vì:
> 1. **Nhất quán với các nghiên cứu trước** (DeePhage, PhaTYP) — cho phép so sánh công bằng
> 2. **Tận dụng tối đa dữ liệu** — với 2.241 genomes, mỗi fold vẫn có đủ mẫu
> 3. **Đánh giá ổn định** — kết quả trung bình 5 fold giảm phương sai do chia ngẫu nhiên
>
> Phân tầng (stratified) đảm bảo tỷ lệ ôn hòa/độc lực nhất quán qua các fold.

### Q2.4: Tại sao không đưa DeepPL vào so sánh?

> **Trả lời:** DeepPL sử dụng DNABERT gốc (không phải DNABERT-2) với learned positional embedding giới hạn tối đa 512bp. Thực nghiệm của chúng tôi đánh giá contig đến 1.800bp (nhóm C và D vượt 512bp). DeepPL không thể xử lý các nhóm này, nên không đưa vào so sánh để đảm bảo công bằng trên cùng thiết kế thực nghiệm.

---

## 3. Kết quả và phân tích

### Q3.1: PhaTYP có Specificity cao hơn trên contig dài. Tại sao PhaBERT vẫn tốt hơn?

> **Trả lời:** Đúng, PhaTYP đạt Sp cao hơn ở nhóm C (87,65% vs 86,92%) và D (89,75% vs 87,63%) nhờ khai thác đặc trưng protein — thông tin ở cấp độ cao hơn nucleotide. Tuy nhiên:
> 1. PhaBERT đạt **Accuracy tổng thể cao hơn** trên mọi nhóm (91,38% vs 91,02% nhóm D)
> 2. PhaBERT đạt **Sensitivity cao hơn** (92,38% vs 92,29% nhóm D) — quan trọng cho liệu pháp phage vì cần phát hiện đầy đủ phage độc lực
> 3. PhaBERT **không phụ thuộc Prodigal** — trên contig ngắn (nhóm A), PhaTYP giảm mạnh (78,92%) vì Prodigal không phát hiện được protein trên đoạn ngắn
>
> Trade-off: PhaBERT ưu tiên Sensitivity (an toàn cho liệu pháp), PhaTYP ưu tiên Specificity trên contig dài.

### Q3.2: Cải thiện 0,36% (nhóm D vs PhaTYP) có ý nghĩa thống kê không?

> **Trả lời:** Trên quy mô dữ liệu hệ gen môi trường hiện đại (IMG/VR chứa >15 triệu trình tự), cải thiện 1% tương đương giảm ~150.000 phân loại sai. Với 0,36%, con số này vẫn là hàng chục nghìn contig.
>
> Quan trọng hơn, PhaBERT đạt accuracy cao nhất **nhất quán trên tất cả 4 nhóm** — không có phương pháp nào khác làm được điều này. PhaTYP yếu ở nhóm A, DeePhage luôn thấp hơn, ProkBERT bão hòa từ nhóm B. Tính nhất quán này có giá trị thực tiễn cao hơn mức cải thiện tuyệt đối ở 1 nhóm.

### Q3.3: Ablation cho thấy bỏ 1 nhánh CNN không ảnh hưởng nhiều. Vậy 3 nhánh có thừa không?

> **Trả lời:** (Xem chi tiết tại `notes/ablation_redundancy_defense.md`)
>
> Không thừa. Đây là hiện tượng phổ biến trong deep learning:
> 1. **Zhang & Wallace (2017)**: hiệu suất CNN đa cửa sổ ít nhạy cảm với kích thước cụ thể, nhưng dùng nhiều kích thước cùng lúc luôn tốt hơn 1 kích thước
> 2. **Michel et al. (2019)**: 40-80% attention heads có thể bỏ mà không ảnh hưởng, nhưng multi-head tổng thể vẫn cần thiết
> 3. **Kết quả trên contig dài (nhóm D)**: mô hình đầy đủ đạt 91,38% vs 90,99-91,05% khi thiếu 1 nhánh — lợi ích phát huy rõ khi trình tự đủ dài
>
> Các nhánh tạo "implicit ensemble" — thông tin chồng lấn nhưng ensemble tổng thể ổn định hơn từng thành phần.

### Q3.4: Trên contig ngắn (nhóm A), bỏ 1 nhánh lại TỐT HƠN. Giải thích?

> **Trả lời:** Đây là hiệu ứng regularization. Trên contig ngắn (100-400bp), tín hiệu trình tự hạn chế — ít mô-típ chức năng hoàn chỉnh. Khi đó, ít tham số hơn giúp mô hình tổng quát hóa tốt hơn do giảm nguy cơ quá khớp.
>
> Ngược lại, trên contig dài (nhóm D), trình tự đủ dài để chứa các mô-típ đa dạng → mô hình đầy đủ khai thác tốt hơn → đạt kết quả cao nhất.

---

## 4. Ý nghĩa thực tiễn

### Q4.0: Tại sao phân loại lối sống phage trên contig (phân mảnh) lại có ích? Liệu pháp phage cần phage đầy đủ cơ mà?

> **Trả lời:** Câu hỏi rất đúng — liệu pháp phage cần hạt phage sống, không phải file trình tự. Nhưng phân loại trên contig có giá trị ở **3 tầng**:
>
> **Tầng 1: Contig là thực tế duy nhất của metagenomics.**
> Phần lớn phage trong tự nhiên nhiễm vi khuẩn không thể nuôi cấy → không bao giờ phân lập được. IMG/VR v4 chứa >15 triệu trình tự virus, trong đó ~91% không đầy đủ (chỉ ~8.9% đạt ≥90% completeness). Nếu công cụ chỉ hoạt động trên genome đầy đủ, ta bỏ qua >90% đa dạng sinh học phage đã biết.
>
> **Tầng 2: Bước lọc BẮT BUỘC trước phân lập cho liệu pháp.**
> Workflow thực tế: hàng nghìn contig từ metagenome → dự đoán lối sống → loại temperate → ưu tiên virulent cho phân lập thực nghiệm. Không có bước lọc này, nhà nghiên cứu lãng phí hàng tuần phân lập phage temperate — vô dụng và nguy hiểm cho trị liệu (lysogenic conversion, truyền gen kháng kháng sinh).
>
> **Tầng 3: Giá trị độc lập không cần phân lập.**
> - *Sinh thái*: tỷ lệ temperate/virulent thay đổi tương quan với IBD, ung thư đại trực tràng
> - *Giám sát AMR*: prophage (temperate) mang gen kháng kháng sinh → xác định temperate = xác định vector truyền AMR
> - *An toàn sinh học*: tỷ lệ lytic/lysogenic trong nước thải, đất cho biết mức độ rủi ro lan truyền gen
>
> **Từ contig virulent → phage therapy bằng cách nào?**
> Contig là dữ liệu (chuỗi ATCG trong máy tính), không phải vật chất sinh học. Có 2 con đường:
> 1. **Phân lập có hướng dẫn (sequence-guided isolation)** — phổ biến nhất: dùng trình tự contig thiết kế primer/probe → quay lại mẫu gốc → nuôi cấy host → plaque assay → PCR xác nhận đúng phage cần tìm. Contig = bản đồ chỉ đường thay vì mò mẫm ngẫu nhiên.
> 2. **Sinh học tổng hợp** — mới nổi: tổng hợp hóa học toàn bộ genome → biến nạp vào host → "boot up" phage sống. Cần genome đầy đủ, chưa phổ biến lâm sàng.
>
> **Tóm lại:** Phân loại trên contig không thay thế phân lập — nó là bước tiền đề giúp (1) lọc ứng viên ở quy mô metagenomics, (2) hướng dẫn phân lập có mục tiêu, và (3) phục vụ các ứng dụng sinh thái/AMR không cần phân lập.

### Q4.1: PhaBERT có thể triển khai thực tế như thế nào?

> **Trả lời:** PhaBERT có ưu thế triển khai so với PhaTYP:
> - **Không cần pipeline phụ trợ** — PhaTYP cần chạy Prodigal trước để dự đoán protein, PhaBERT nhận trực tiếp chuỗi DNA
> - **Inference nhanh** — <10ms/contig trên GPU
> - **Đầu vào đơn giản** — chỉ cần chuỗi nucleotide ATGC
>
> Quy trình triển khai: contig từ metagenomic assembly → phân nhóm theo độ dài → chạy mô hình tương ứng → output: virulent/temperate + confidence score.

### Q4.2: Tại sao phân loại phage quan trọng cho liệu pháp phage?

> **Trả lời:** Liệu pháp phage chỉ sử dụng phage **độc lực** (lytic). Nếu phage ôn hòa (temperate) bị phân loại sai thành độc lực và được dùng trong điều trị:
> 1. Phage có thể tích hợp vào genome vi khuẩn (lysogeny)
> 2. Chuyển gen độc lực cho vi khuẩn qua biến đổi tiềm tan (lysogenic conversion)
> 3. Ví dụ: độc tố tả (CTXphi), độc tố Shiga (stx1/stx2), độc tố bạch hầu
>
> → Sensitivity cao (phát hiện đúng phage độc lực) quan trọng cho sàng lọc ứng viên liệu pháp. PhaBERT đạt Sn 82-92% — cao nhất trong các phương pháp so sánh.

---

## 5. Phương pháp luận

### Q5.1: Chiến lược huấn luyện 2 giai đoạn có cần thiết không? Tại sao không fine-tune toàn bộ từ đầu?

> **Trả lời:** Huấn luyện 2 giai đoạn nhằm:
> 1. **GĐ1 (freeze backbone)**: Khởi tạo ổn định MKC + classifier trước. Nếu unfreeze ngay từ đầu, gradient từ các lớp mới (random init) có thể phá hỏng biểu diễn đã học của DNABERT-2 (catastrophic forgetting)
> 2. **GĐ2 (unfreeze + discriminative LR)**: LR thấp cho backbone (2×10⁻⁵) bảo toàn tri thức tiền huấn luyện, LR cao cho MKC (1×10⁻³) cho phép thích nghi nhanh với tác vụ
>
> Đây là chiến lược phổ biến trong fine-tuning mô hình tiền huấn luyện (Howard & Ruder, 2018 — ULMFiT).

### Q5.2: BPE tokenization giảm 5× độ dài chuỗi. Có mất thông tin không?

> **Trả lời:** Không mất thông tin — BPE là mã hóa **lossless** (có thể decode ngược lại chuỗi gốc). Giảm 5× độ dài nghĩa là mỗi token BPE đại diện cho ~5 nucleotides trung bình. Lợi ích:
> 1. Giảm chi phí tính toán (attention là O(n²))
> 2. Mỗi token mang nhiều thông tin ngữ cảnh hơn 1 nucleotide đơn lẻ
> 3. Loại bỏ rò rỉ thông tin (token không chồng lấn)
>
> DNABERT-2 đã được tiền huấn luyện với BPE → biểu diễn đã tối ưu cho tokenization này.

### Q5.3: Cửa sổ trượt tạo contig có overlap. Có gây data leakage không?

> **Trả lời:** Overlap giữa contig từ **cùng 1 genome** không gây leakage vì tất cả contig từ cùng genome chỉ nằm trong 1 fold. Leakage chỉ xảy ra nếu contig từ cùng genome xuất hiện ở cả train và validation — điều này được ngăn chặn bởi genome-level split.
>
> Overlap có mục đích: tăng số lượng mẫu huấn luyện và mô phỏng thực tế (trong metagenomic assembly, các contig thường chồng lấn).

---

## 6. So sánh và vị trí trong lĩnh vực

### Q6.1: So với các mô hình mới hơn (2024-2025) thì PhaBERT đứng ở đâu?

> **Trả lời:** PhaBERT tập trung vào bài toán cụ thể (phage lifestyle prediction trên contig ngắn) với đóng góp chính là kiến trúc MKC chuyên biệt. Các mô hình mới hơn (Evo, Caduceus) là foundation models tổng quát — chúng có thể được dùng thay DNABERT-2 làm backbone trong tương lai, nhưng vẫn cần kiến trúc chuyên biệt cho tác vụ (MKC) để đạt hiệu suất tối ưu.
>
> Đóng góp của luận văn không phải backbone mới, mà là cách kết hợp backbone + task-specific architecture hiệu quả cho bài toán phân loại phage.

### Q6.2: ProkBERT cũng dùng BERT tiền huấn luyện trên genome. Tại sao kém hơn?

> **Trả lời:** ProkBERT dùng LCA k-mer chồng lấn (overlapping k-mers) để tokenize. Vấn đề:
> 1. **Rò rỉ thông tin**: token liền kề chia sẻ (k-1) nucleotides → trong masked language modeling, mô hình có thể "nhìn" token bị mask qua các token lân cận
> 2. **Dư thừa token**: chuỗi dài hơn nhiều so với BPE → tốn tài nguyên tính toán
> 3. **Bão hòa trên contig dài**: accuracy đạt đỉnh ở nhóm B (85,35%) rồi giảm ở C (84,03%) và D (84,73%) — phản ánh hạn chế cơ bản của tokenization
>
> PhaBERT dùng BPE (DNABERT-2) loại bỏ hoàn toàn các vấn đề trên.

---

## 7. Hạn chế và hướng phát triển

### Q7.1: Nếu mở rộng sang đa phương thức (DNA + protein), kiến trúc sẽ như thế nào?

> **Trả lời:** Hướng đề xuất:
> - Nhánh DNA: DNABERT-2 + MKC (giữ nguyên PhaBERT)
> - Nhánh protein: ESM-2 hoặc ProtBERT xử lý protein sequences (từ Prodigal khi khả dụng)
> - Tích hợp: cross-attention hoặc late fusion
> - Quan trọng: cần cơ chế **conditional computation** — khi contig ngắn không có protein features (Prodigal fail), chỉ dùng nhánh DNA. Khi contig dài có protein, dùng cả hai.
>
> Điều này giải quyết trade-off hiện tại: PhaBERT mạnh trên contig ngắn, PhaTYP mạnh về Sp trên contig dài.

### Q7.2: Luận văn chỉ đánh giá trên 1 dataset. Tính tổng quát hóa thế nào?

> **Trả lời:** Dataset 2.241 genomes được tổng hợp từ DeePhage và DeepPL — đây là benchmark chuẩn trong lĩnh vực, được nhiều nghiên cứu sử dụng. 5-fold CV giúp đánh giá ổn định trên nhiều cách chia khác nhau.
>
> Hạn chế: chưa đánh giá trên independent test set từ nguồn khác (ví dụ: NCBI mới, IMG/VR). Đây là hướng phát triển — cần thu thập thêm dữ liệu từ các nguồn độc lập để đánh giá generalization.

---

## Lưu ý khi trả lời

- Trả lời ngắn gọn, đi thẳng vào vấn đề (30-60 giây/câu)
- Nếu không chắc → thừa nhận là hạn chế, đề xuất hướng giải quyết
- Dùng số liệu cụ thể từ luận văn để minh họa
- Không defensive — coi câu hỏi là cơ hội thể hiện hiểu biết sâu
- Nếu hội đồng hỏi ngoài scope → "Đây là hướng nghiên cứu tiếp theo rất thú vị, chúng tôi đã đề cập trong phần hạn chế..."

---

## 8. Tính mới và vị trí đóng góp

### Q8.1: Đóng góp lớn nhất của đề tài là gì?

> **Trả lời:** Đóng góp lớn nhất là chứng minh rằng mô hình nền tảng hệ gen (DNABERT-2) cần kiến trúc chuyên biệt cho tác vụ (MKC) để đạt hiệu suất tối ưu — chứ không phải chỉ gắn thêm đầu phân loại tuyến tính.
>
> Cụ thể: DNABERT-2 với linear head đạt 81,52–88,36%. Khi thêm MKC, cải thiện lên 82,01–91,38% — tăng 0,49–3,02% tùy nhóm, với Specificity tăng đặc biệt đáng kể (+8,61% ở contig ngắn). Nghiên cứu ablation 7 cấu hình cho thấy sự kết hợp nhánh CNN đa cửa sổ + gộp trung bình có mặt nạ mang lại hiệu suất cân bằng nhất trên toàn phổ độ dài.
>
> Foundation model cung cấp biểu diễn tốt, nhưng **cách khai thác biểu diễn đó cho tác vụ cụ thể** mới quyết định hiệu suất cuối cùng. Insight này có thể mở rộng sang các bài toán tin sinh học hạ nguồn khác.

### Q8.2: Đã có công bố nào kết hợp foundation model + kiến trúc chuyên biệt cho bài toán phân loại phage chưa?

> **Trả lời:** Chưa. Qua khảo sát toàn diện, trong bài toán phân loại phage lifestyle, chưa có nghiên cứu nào kết hợp mô hình nền tảng hệ gen tiền huấn luyện với kiến trúc tích chập đa tỷ lệ chuyên biệt cho tác vụ.
>
> Các phương pháp hiện có đều thiếu ít nhất 1 yếu tố:
> - **DeepPL (2024)**: dùng DNABERT gốc + fine-tuning head chuẩn (không CNN, giới hạn 512bp)
> - **ProkBERT PhaStyle (2024)**: dùng ProkBERT + weighted pooling (1 linear layer, không multi-scale)
> - **DeePhafier (2024)**: có multi-scale self-attention nhưng train từ đầu, không dùng foundation model, cần protein features
>
> Pattern kiến trúc DNABERT-2 + CNN đã được áp dụng cho bài toán KHÁC: DNABERT2-CAMP (Genes, 2025) kết hợp DNABERT-2 + 4-layer CNN cho nhận diện promoter E. coli. Điều này xác nhận pattern hợp lệ, nhưng chưa ai áp dụng cho phage lifestyle.
>
> PhaBERT nằm ở giao điểm: foundation model (DNABERT-2) + multi-scale CNN (MKC) + end-to-end trên DNA thô — kết hợp mà chưa có nghiên cứu trước nào thực hiện cho bài toán này.

---

## 9. Rò rỉ thông tin

### Q9.1: Em khẳng định BPE loại bỏ hoàn toàn rò rỉ thông tin. Liệu điều này có đúng? Có rủi ro rò rỉ nào khác không?

> **Trả lời:** Khẳng định "loại bỏ hoàn toàn" đề cập cụ thể đến rò rỉ **ở mức tokenization** — hiện tượng token liền kề chia sẻ nucleotides trong k-mer chồng lấn, khiến mô hình suy ra token bị mask từ token lân cận trong tiền huấn luyện. BPE tạo token không chồng lấn nên loại bỏ hoàn toàn loại rò rỉ này.
>
> Tuy nhiên, có các nguồn rò rỉ tiềm ẩn khác mà BPE không giải quyết:
>
> **Thứ nhất**, sliding window tạo contig với overlap 10-40% → contig trong cùng tập train chia sẻ đoạn trình tự. Giảm thiểu bằng genome-level split — contig từ cùng genome chỉ nằm trong 1 fold.
>
> **Thứ hai**, DNABERT-2 tiền huấn luyện trên dữ liệu đa loài từ NCBI, có thể bao gồm genome phage trong dataset đánh giá. Đây là rủi ro chung của mọi phương pháp dùng foundation model (PhaTYP, ProkBERT cũng chịu) — so sánh vẫn công bằng.
>
> **Thứ ba**, tương đồng sinh học giữa genome khác fold (conserved regions, horizontal gene transfer). Phương pháp nghiêm ngặt hơn là sequence-similarity-based split, nhưng chưa được áp dụng trong các nghiên cứu trước (DeePhage, PhaTYP) và sẽ giảm đáng kể kích thước dataset.
>
> Tóm lại, "loại bỏ hoàn toàn" nên hiểu trong phạm vi tokenization-level leakage. Các nguồn khác được giảm thiểu bằng genome-level split nhưng không loại bỏ 100%.

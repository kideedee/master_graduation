# Plan: Viết lại Chương 5 (Kết luận)

## Cấu trúc mới

- 5.1: Kết luận
- 5.2: Thảo luận về kết quả chính
  - 5.2.1: Phân tích kết quả
  - 5.2.2: Đóng góp của nghiên cứu
  - 5.2.3: Hạn chế và hướng phát triển tương lai

**Lưu ý:** Viết liền mạch trong mỗi section, không chia nhỏ thêm.

---

## I. Section 5.1: Kết luận

### Mục tiêu
Tóm tắt toàn bộ nghiên cứu: phương pháp đã đề xuất, kết quả đạt được, và ý nghĩa của công trình.

### Outline (3 đoạn văn)

**Đoạn 1: Giới thiệu bài toán và phương pháp đề xuất**
- Bối cảnh: Phân loại lối sống thực khuẩn thể từ dữ liệu metagenomic
- Thách thức: Contig ngắn, thiếu protein hoàn chỉnh
- Phương pháp đề xuất: PhaBERT-CNN kết hợp DNABERT-2 với Modified TextCNN
- Đặc điểm: Hoạt động trực tiếp trên chuỗi DNA thô, không phụ thuộc gene prediction

**Đoạn 2: Kết quả chính**
- Đánh giá trên 4 nhóm độ dài contig (100-1800 bp) qua 5-fold cross-validation
- Accuracy đạt được: 81.59% (A), 87.91% (B), 90.01% (C), 90.69% (D)
- So sánh với baseline: Vượt trội PhaTYP, DeePhage, ProkBERT trên nhóm A, B, C
- Cạnh tranh với PhaTYP trên nhóm D (chỉ kém 0.34%)

**Đoạn 3: Ý nghĩa và đóng góp**
- Chứng minh hiệu quả của việc kết hợp genomic foundation model với kiến trúc task-specific
- Giải quyết hạn chế của các phương pháp hiện có (gene prediction dependency, limited generalization)
- Mở ra hướng tiếp cận mới cho các bài toán phân loại genome downstream

---

## II. Section 5.2: Thảo luận về kết quả chính

### 5.2.1: Phân tích kết quả

**Mục tiêu:** Giải thích tại sao PhaBERT-CNN đạt kết quả như vậy, phân tích ưu nhược điểm.

**Outline (4 đoạn văn liền mạch)**

**Đoạn 1: Hiệu suất vượt trội trên contig ngắn và trung bình**
- PhaBERT-CNN tốt nhất trên nhóm A, B, C
- Nguyên nhân 1: Không phụ thuộc gene prediction (Prodigal thất bại trên contig <400 bp)
- Nguyên nhân 2: DNABERT-2 tiền huấn luyện tổng quát hóa tốt hơn DeePhage
- Nguyên nhân 3: Kiến trúc nhánh song song (multi-scale CNN + attention pooling) nắm bắt motif cục bộ và ngữ cảnh toàn cục

**Đoạn 2: Đánh giá đóng góp của kiến trúc task-specific**
- So sánh DNABERT-2 baseline vs PhaBERT-CNN (Hình \ref{fig:dnabert2_vs_phabertcnn})
- Cải thiện accuracy tăng dần theo độ dài: 0.07% (A) → 3.43% (D)
- Cải thiện specificity đáng kể ở nhóm A: 6.90% (73.25% → 80.15%)
- Giải thích: CNN khai thác motif chức năng hiệu quả hơn khi chuỗi dài; attention pooling giúp tập trung vào vùng thông tin quan trọng

**Đoạn 3: Hiệu suất trên contig dài**
- PhaTYP vượt trội trên nhóm D (91.02% vs 90.69%)
- Nguyên nhân: PhaTYP tận dụng protein features từ ORF hoàn chỉnh
- PhaBERT-CNN vẫn đạt specificity cao nhất (90.95%), tốt hơn PhaTYP (89.75%)
- Gợi ý: Kết hợp thêm protein features theo kiến trúc multi-modal có thể cải thiện

**Đoạn 4: So sánh với các phương pháp khác**
- DeePhage: Hiệu suất trung bình, hạn chế bởi one-hot encoding và thiếu pre-training
- ProkBERT: Stagnation trên contig dài, gợi ý hạn chế của LCA tokenization chồng lấn
- PhaBERT-CNN: Cân bằng giữa sensitivity và specificity, hiệu suất ổn định trên tất cả nhóm

### 5.2.2: Đóng góp của nghiên cứu

**Mục tiêu:** Nêu rõ các đóng góp khoa học và thực tiễn.

**Outline (3 đoạn văn liền mạch)**

**Đoạn 1: Đóng góp về phương pháp**
- Đề xuất PhaBERT-CNN: Kiến trúc lai kết hợp genomic foundation model với CNN chuyên biệt
- Kiến trúc nhánh song song kép: Multi-scale CNN (kernel 3, 5, 7) + attention pooling
- Chiến lược huấn luyện hai giai đoạn với discriminative learning rates

**Đoạn 2: Đóng góp về kết quả thực nghiệm**
- Đánh giá toàn diện trên 4 nhóm độ dài contig (100-1800 bp)
- Cải thiện state-of-the-art trên contig ngắn và trung bình
- Chứng minh hiệu quả của việc kết hợp pre-trained embeddings với task-specific architecture

**Đoạn 3: Đóng góp về ứng dụng thực tiễn**
- Giải quyết bài toán thực tế: Phân loại phage từ metagenomic assemblies phân mảnh
- Không phụ thuộc gene prediction, hoạt động trên chuỗi DNA thô
- Mở ra hướng tiếp cận mới cho các bài toán sinh tin học downstream

### 5.2.3: Hạn chế và hướng phát triển tương lai

**Mục tiêu:** Thừa nhận hạn chế và đề xuất hướng nghiên cứu tiếp theo.

**Outline (5 đoạn văn liền mạch)**

**Đoạn 1: Hạn chế về xử lý class imbalance**
- Random undersampling có thể mất thông tin từ lớp đa số
- Đề xuất: Class weighting, focal loss, oversampling tổng hợp

**Đoạn 2: Hạn chế về hiệu suất trên contig dài**
- PhaBERT-CNN kém PhaTYP trên nhóm D
- Nguyên nhân: Chưa tận dụng protein features
- Đề xuất: Mở rộng kiến trúc multi-modal kết hợp nucleotide + protein features

**Đoạn 3: Hạn chế về đánh giá**
- Chỉ đánh giá trên simulated contigs từ complete genomes
- Đề xuất: Kiểm tra trên real metagenomic datasets từ môi trường đa dạng

**Đoạn 4: Hướng phát triển về interpretability**
- Phân tích attention weights để xác định vùng genomic quan trọng
- Trực quan hóa các motif được CNN học được
- Hiểu rõ hơn cơ chế phân loại của mô hình

**Đoạn 5: Hướng phát triển về ứng dụng mở rộng**
- Chuyển giao sang các tác vụ liên quan: Host prediction, prophage detection
- Tích hợp vào pipeline phân tích metagenomic tự động
- Tối ưu hóa inference speed cho ứng dụng quy mô lớn

---

## III. Danh sách trích dẫn cần sử dụng

### Từ references.bib:

1. **zhou2023dnabert** - DNABERT-2 foundation model
2. **wu2021deephage** - DeePhage baseline
3. **shang2023phatyp** - PhaTYP baseline
4. **ligeti2024prokbert** - ProkBERT baseline
5. **hyatt2010prodigal** - Prodigal gene prediction tool
6. **trimble2012short** - Prodigal limitations on short contigs

### Tham chiếu nội bộ (\\ref{}):

1. **\\ref{tab:main_results}** - Bảng kết quả chính (Chapter 4)
2. **\\ref{fig:dnabert2_vs_phabertcnn}** - So sánh DNABERT-2 vs PhaBERT-CNN
3. **\\ref{fig:primary_contig_exp}** - Hiệu suất trên 4 nhóm contig
4. **\\ref{chap:method}** - Chương 3 (Phương pháp đề xuất)
5. **\\ref{chap:thuc_nghiem_danh_gia}** - Chương 4 (Thực nghiệm)

---

## IV. Số liệu cần verify

### Từ Chapter 4 (tab:main_results):

**PhaBERT-CNN:**
- Nhóm A: sn=82.00%, sp=80.15%, acc=81.59%
- Nhóm B: sn=89.91%, sp=80.44%, acc=87.91%
- Nhóm C: sn=91.12%, sp=85.93%, acc=90.01%
- Nhóm D: sn=88.47%, sp=90.95%, acc=90.69%

**PhaTYP:**
- Nhóm A: acc=78.92%
- Nhóm B: acc=85.90%
- Nhóm C: acc=88.87%
- Nhóm D: sn=92.29%, sp=89.75%, acc=91.02%

**DeePhage:**
- Nhóm A: acc=78.07%
- Nhóm B: acc=84.17%
- Nhóm C: acc=87.40%
- Nhóm D: acc=89.09%

**ProkBERT:**
- Nhóm A: acc=80.68%
- Nhóm B: acc=85.35%
- Nhóm C: acc=84.03%
- Nhóm D: acc=84.73%

**DNABERT-2 baseline (fig:dnabert2_vs_phabertcnn):**
- Nhóm A: acc=81.52%, sp=73.25%
- Nhóm D: acc=87.26%

**Cải thiện PhaBERT-CNN vs baselines:**
- vs PhaTYP: 0.91-2.67% (nhóm A, B, C)
- vs DeePhage: 2.17-3.24% (nhóm A, B, C)
- vs ProkBERT: 0.91-5.98% (nhóm A, B, C)
- vs PhaTYP nhóm D: -0.34% (90.69% vs 91.02%)

**Cải thiện PhaBERT-CNN vs DNABERT-2:**
- Nhóm A: +0.07% acc, +6.90% sp (73.25% → 80.15%)
- Nhóm D: +3.43% acc (87.26% → 90.69%)

---

## V. Terminology check

Các thuật ngữ sẽ sử dụng (theo vietnamese-terms.md):

- Thực khuẩn thể / Phage ✓
- Lối sống (lifestyle) ✓
- Contig ✓
- Metagenomic ✓
- Học sâu (deep learning) ✓
- Mô hình nền tảng genome (genomic foundation model) ✓
- Tiền huấn luyện (pre-training) ✓
- Tinh chỉnh (fine-tuning) ✓
- BPE tokenization ✓
- Attention pooling ✓
- Multi-scale CNN / CNN đa tỷ lệ ✓
- Nhánh song song kép (dual parallel branches) ✓
- Gene prediction / Dự đoán gene ✓
- Sensitivity / Độ nhạy ✓
- Specificity / Độ đặc hiệu ✓
- Accuracy / Độ chính xác ✓

Giữ nguyên tiếng Anh:
- DNABERT-2, PhaBERT-CNN, PhaTYP, DeePhage, ProkBERT
- Embedding, tokenization, attention, pooling, backbone
- Kernel, batch, dropout
- k-mer, contig, metagenomic
- ORF (Open Reading Frame)
- Prodigal

---

## VI. Ghi chú về văn phong

- Viết liền mạch trong mỗi section, không chia nhỏ subsection
- Sử dụng câu ngắn, rõ ràng
- Mỗi đoạn văn tập trung vào một ý chính
- Kết nối các đoạn văn bằng từ nối logic
- Trích dẫn đầy đủ cho mọi số liệu và khẳng định
- Tham chiếu chéo đến các bảng/hình trong chương 4

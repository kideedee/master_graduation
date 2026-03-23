# Plan: Chương 1 - Chỉnh sửa thuật ngữ tiếng Việt và bổ sung bảng thuật ngữ/viết tắt

## Tổng quan

Rà soát toàn bộ Chương 1 (`chapters/c1/chapter_1.tex`) để: (A) chỉnh sửa các thuật ngữ tiếng Việt chưa nhất quán hoặc chưa chuẩn xác, (B) bổ sung thuật ngữ/viết tắt còn thiếu vào bảng glossary (`chapters/glossary.tex`), và (C) cập nhật bảng thuật ngữ nội bộ (`vietnamese-terms.md`).

---

## I. Các vấn đề thuật ngữ phát hiện trong Chương 1

### A. Thuật ngữ tiếng Anh chưa được Việt hóa hoặc giải thích lần đầu xuất hiện

| Dòng | Thuật ngữ EN trong bản gốc | Vấn đề | Đề xuất chỉnh sửa |
|------|---------------------------|--------|-------------------|
| 7 | "chu trình phân giải" | Dùng "chu trình phân giải" thay vì "chu trình tan" (lytic cycle) -- không nhất quán với chương 2 (dòng 22 c2 dùng "chu trình tan") và glossary (dòng 32: "Lytic cycle = Chu trình tan") | Thay "chu trình phân giải" --> "chu trình tan (lytic cycle)" lần đầu xuất hiện; sau đó dùng "chu trình tan" |
| 7 | "prophage" | Thuật ngữ EN, cần giải thích tiếng Việt lần đầu xuất hiện | Thêm "(tiền thực khuẩn thể)" sau prophage lần đầu |
| 7 | "biến đổi tiềm tan" | Dịch "lysogenic conversion" -- nhất quán với c2 (dòng 24). OK nhưng cần chú thích EN lần đầu | Thêm "(lysogenic conversion)" lần đầu xuất hiện |
| 9 | "contig" | Đã giải thích inline bằng em-dash. OK |  |
| 16 | "gen đánh dấu phổ quát" / "gen 16S rRNA" | OK -- thuật ngữ chính xác | Bổ sung "gen đánh dấu" vào glossary |
| 16 | "chuyển gen ngang" | OK -- thuật ngữ đúng nhưng chưa có trong glossary | Bổ sung "(horizontal gene transfer)" vào glossary |
| 18 | "tokenization chồng lấp" | Cần rõ hơn: "chiến lược tokenization dựa trên k-mer chồng lấp" | Sửa thành "các chiến lược tokenization dựa trên k-mer chồng lấp" |
| 23 | "mô hình nền tảng genome" | Chưa nhất quán: c2 dùng "mô hình nền tảng hệ gen (genomic foundation models)" | Thay "mô hình nền tảng genome" --> "mô hình nền tảng hệ gen (genome foundation model)" |
| 28 | "discriminative learning rates" | Thuật ngữ EN không giải thích | Thay bằng "tốc độ học phân biệt (discriminative learning rates)" |
| 29 | "stratified 5-fold cross-validation" | Thuật ngữ EN không giải thích | Thay bằng "kiểm định chéo 5 phần phân tầng (stratified 5-fold cross-validation)" |
| 40 | "accuracy 81.59--90.69\%" | Số liệu cần verify -- OK, đã có nguồn document/phabert_cnn.tex |  |
| 41 | "ablation study" | Thuật ngữ EN không giải thích | Thay bằng "nghiên cứu loại bỏ thành phần (ablation study)" |
| 41 | "baseline" | Thuật ngữ EN, cần Việt hóa | Thay bằng "mô hình cơ sở (baseline)" |
| 47 | "sensitivity, specificity, và accuracy" | Sensitivity/specificity chưa Việt hóa | Thay bằng "độ nhạy (sensitivity), độ đặc hiệu (specificity), và độ chính xác (accuracy)" |
| 47 | "mô hình nền tảng genome" | Lặp lại vấn đề ở dòng 23 | Dùng "mô hình nền tảng hệ gen" cho nhất quán |
| 49 | "chronic infection" | Thuật ngữ EN không giải thích | Thay bằng "nhiễm mãn tính (chronic infection)" |
| 49 | "sliding window" | Thuật ngữ EN không giải thích | Thay bằng "cửa sổ trượt (sliding window)" |

### B. Thuật ngữ nhất quán cần kiểm tra xuyên suốt chương

| Thuật ngữ | Cách dùng trong c1 | Cách dùng chuẩn (theo c2/glossary) | Cần sửa? |
|-----------|--------------------|------------------------------------|----------|
| Chu trình tan / Chu trình phân giải | "chu trình phân giải" (dòng 7) | "chu trình tan" (c2, glossary) | CO -- thống nhất thành "chu trình tan" |
| Mô hình nền tảng genome / hệ gen | "nền tảng genome" (dòng 23, 47) | "nền tảng hệ gen" (c2 dòng 146, 149) | CO -- thống nhất thành "nền tảng hệ gen" |
| Thực khuẩn thể / thực khuẩn | Dùng "thực khuẩn thể" nhất quán | OK | Khong |
| metagenomics / metagenomic | Dùng cả hai dạng | c2 dùng "metagenomics" cho danh từ, "metagenomic" cho tính từ | OK -- đúng ngữ pháp EN |

---

## II. Bổ sung vào bảng glossary (`chapters/glossary.tex`)

Bảng hiện có 33 mục (STT 1-33). Cần bổ sung các thuật ngữ sau xuất hiện trong Chương 1 nhưng chưa có trong glossary:

| STT mới | Từ viết tắt/thuật ngữ | Cụm từ đầy đủ | Cụm từ tiếng Việt |
|---------|----------------------|---------------|-------------------|
| 34 | Prophage | Prophage | Tiền thực khuẩn thể |
| 35 | HGT | Horizontal Gene Transfer | Chuyển gen ngang |
| 36 | Metagenomics | Metagenomics | Siêu hệ gen học |
| 37 | NGS | Next-Generation Sequencing | (da co -- STT 7) |
| 38 | MKCA | Multi-Kernel Convolutional Attention | Mô đun tích chập đa kernel kết hợp cơ chế chú ý |
| 39 | Ablation study | Ablation study | Nghiên cứu loại bỏ thành phần |
| 40 | Cross-validation | Cross-validation | Kiểm định chéo |
| 41 | Phage therapy | Phage therapy | Liệu pháp phage |
| 42 | Lysogenic conversion | Lysogenic conversion | Biến đổi tiềm tan |
| 43 | Foundation model | Foundation model | Mô hình nền tảng |
| 44 | PhaBERT-CNN | Phage BERT - Convolutional Neural Network | Mô hình PhaBERT-CNN |

Luu y: NGS (STT 7) da co trong glossary, khong can bo sung.

---

## III. Bổ sung vào `vietnamese-terms.md`

Thêm vào bảng "Key Technical Terms":

| Vietnamese | English |
|---|---|
| Tiền thực khuẩn thể | Prophage |
| Chuyển gen ngang | Horizontal gene transfer |
| Siêu hệ gen học | Metagenomics |
| Kiểm định chéo | Cross-validation |
| Phân tầng | Stratified |
| Tốc độ học phân biệt | Discriminative learning rate |
| Nghiên cứu loại bỏ thành phần | Ablation study |
| Mô hình cơ sở | Baseline |
| Cửa sổ trượt | Sliding window |
| Nhiễm mãn tính | Chronic infection |
| Mô hình nền tảng | Foundation model |
| Mô hình nền tảng hệ gen | Genome foundation model |
| Liệu pháp phage | Phage therapy |
| Biến đổi tiềm tan | Lysogenic conversion |
| Gen đánh dấu | Marker gene |

Thêm vào bảng "Forbidden Substitutions (Keep in English)":

| Keep as-is (English) | Reason |
|---|---|
| MKCA | Specific module name (Multi-Kernel Convolutional Attention) |
| prophage | Standard bioinformatics term, widely used in Vietnamese literature |
| cross-validation | Widely used as-is in Vietnamese ML literature (alongside "kiem dinh cheo") |
| ablation study | Widely used as-is in Vietnamese ML literature |
| baseline | Widely used as-is in Vietnamese ML literature |

---

## IV. Danh sach chinh sua cu the trong `chapters/c1/chapter_1.tex`

### Dong 7 (Dat van de, doan 1):
1. "chỉ thực hiện chu trình phân giải" --> "chỉ thực hiện chu trình tan (lytic cycle)"
2. "ở trạng thái prophage" --> "ở trạng thái prophage (tiền thực khuẩn thể)"
3. "thông qua biến đổi tiềm tan" --> "thông qua biến đổi tiềm tan (lysogenic conversion)"

### Dong 18 (Thach thuc, doan 2):
4. "các chiến lược tokenization chồng lấp" --> "các chiến lược tokenization dựa trên k-mer chồng lấp"

### Dong 23 (Muc tieu):
5. "mô hình nền tảng genome DNABERT-2" --> "mô hình nền tảng hệ gen (genome foundation model) DNABERT-2"

### Dong 28 (Muc tieu, item 3):
6. "với discriminative learning rates" --> "với tốc độ học phân biệt (discriminative learning rates)"

### Dong 29 (Muc tieu, item 4):
7. "thông qua stratified 5-fold cross-validation" --> "thông qua kiểm định chéo 5 phần phân tầng (stratified 5-fold cross-validation)"

### Dong 41 (Dong gop, item 4):
8. "Cung cấp ablation study" --> "Cung cấp nghiên cứu loại bỏ thành phần (ablation study)"
9. "với DNABERT-2 baseline" --> "với mô hình cơ sở DNABERT-2 (baseline)"

### Dong 47 (Pham vi):
10. "mô hình nền tảng genome" --> "mô hình nền tảng hệ gen"
11. "sensitivity, specificity, và accuracy" --> "độ nhạy (sensitivity), độ đặc hiệu (specificity) và độ chính xác (accuracy)"

### Dong 49 (Pham vi, gioi han):
12. "chronic infection" --> "nhiễm mãn tính (chronic infection)"
13. "sliding window" --> "cửa sổ trượt (sliding window)"

---

## V. Citations

Tat ca citation keys trong Chuong 1 da duoc kiem tra va TON TAI trong references.bib:

- `\cite{suttle2007marine}` -- so luong phage tren Trai Dat -- ✓ EXISTS
- `\cite{koskella2014bacteria}` -- dieu hoa quan the vi khuan -- ✓ EXISTS
- `\cite{howard2017lysogeny}` -- lysogeny -- ✓ EXISTS
- `\cite{gorski2016phage}` -- lieu phap phage -- ✓ EXISTS
- `\cite{cobian2016viruses}` -- nguy co truyen gen -- ✓ EXISTS
- `\cite{shang2023phatyp}` -- phuong phap thuc nghiem truyen thong -- ✓ EXISTS
- `\cite{mokili2012metagenomics}` -- metagenomics -- ✓ EXISTS
- `\cite{hayes2017metagenomic}` -- co so du lieu han che -- ✓ EXISTS
- `\cite{zhou2023dnabert}` -- DNABERT-2 -- ✓ EXISTS

---

## VI. Numbers to Verify

- "accuracy 81.59--90.69%" (dong 40) -- Source: document/phabert_cnn.tex -- CAN VERIFY
- "cải thiện 0.91--5.98%" (dong 40) -- Source: document/phabert_cnn.tex -- CAN VERIFY
- "$10^{30}$" (dong 7) -- Source: \cite{suttle2007marine} -- standard estimate, OK
- "2.241 hệ gen phage" (dong 49) -- Source: document/phabert_cnn.tex -- CAN VERIFY
- "100--1800 bp" (dong 47, 29) -- Source: document/phabert_cnn.tex -- CAN VERIFY

---

## VII. Tong ket

### Phan A: Chinh sua trong `chapters/c1/chapter_1.tex` -- 13 thay doi
- 3 thay doi nhat quan thuat ngu ("chu trinh phan giai" -> "chu trinh tan", "nen tang genome" -> "nen tang he gen")
- 10 thay doi bo sung giai thich tieng Viet cho thuat ngu EN

### Phan B: Bo sung vao `chapters/glossary.tex` -- ~10 muc moi (STT 34-44)

### Phan C: Bo sung vao `.claude/rules/vietnamese-terms.md` -- ~15 thuat ngu moi + ~5 forbidden substitutions

### Thu tu thuc hien
1. Chinh sua `chapters/c1/chapter_1.tex` (13 thay doi)
2. Bo sung `chapters/glossary.tex` (10 muc moi)
3. Cap nhat `.claude/rules/vietnamese-terms.md` (20 muc moi)
4. Compile de kiem tra: `pdflatex thesis.tex`

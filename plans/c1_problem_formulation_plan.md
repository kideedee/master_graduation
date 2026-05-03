# Plan: Chương 1 - Phát biểu bài toán (sec:problem_formulation)

**Vị trí chèn:** Sau `\section{Thách thức nghiên cứu}` (sec:challenges), trước `\section{Mục tiêu nghiên cứu}` (sec:objectives).
**Label:** `\label{sec:problem_formulation}`

---

## Outline

I. Đặt khung bài toán: phân loại nhị phân là quy ước chung của tất cả công trình liên quan
   1. Nhận xét rằng tất cả phương pháp (DeePhage, PhaTYP, BACPHLIP, DeepPL, PhageAI, PhaBERT-CNN) đều đặt bài toán là phân loại nhị phân
   2. Lý do lựa chọn binary: hai chu trình sinh học rõ ràng (lytic vs lysogenic), đủ dữ liệu có nhãn, ứng dụng thực tiễn trực tiếp (liệu pháp phage)

II. Định nghĩa hình thức không gian đầu vào
   1. Định nghĩa chuỗi DNA s ∈ {A, T, G, C}^L với ràng buộc L ∈ [100, 1800]
   2. Giải thích ý nghĩa thực tiễn: contig phân mảnh trong dữ liệu metagenomic, không phải hệ gen hoàn chỉnh

III. Định nghĩa hình thức không gian nhãn và hàm phân loại
   1. Nhãn y ∈ {0, 1}: 0 = thực khuẩn thể ôn hòa (temperate), 1 = thực khuẩn thể độc lực (virulent)
   2. Hàm phân loại tổng quát f: S → {0, 1}
   3. Phát biểu bài toán tối ưu hóa: tìm f* tối đa hóa P(f(s) = y) theo phân phối dữ liệu thực

IV. Công thức hóa theo xác suất (probabilistic formulation)
   1. Mô hình hóa P(y | s) qua softmax hai lớp đầu ra
   2. Quyết định phân loại: ŷ = argmax P(y | s)
   3. Hàm mất mát binary cross-entropy đặt bài toán huấn luyện là tối thiểu hóa L_BCE

V. So sánh ngắn gọn cách các phương pháp tiên tiến biểu diễn đầu vào — để dẫn đến lý do chọn BPE
   1. One-hot (DeePhage): mã hóa vị trí-từng-nucleotide, thưa, không ngữ nghĩa
   2. Vector hiện diện miền protein 206 chiều (BACPHLIP): chỉ khả thi trên hệ gen hoàn chỉnh
   3. Protein cluster token (PhaTYP): phụ thuộc Prodigal, thất bại trên contig ngắn
   4. k-mer chồng lấp (DeepPL): gây rò rỉ thông tin, giới hạn độ dài 512 token
   5. BPE trực tiếp trên DNA thô (PhaBERT-CNN): không chồng lấp, không phụ thuộc dự đoán gen, xử lý độ dài tùy ý

VI. Ràng buộc thực tiễn của bài toán — nhắc lại bối cảnh metagenomic
   1. Đầu vào là contig phân mảnh, không thể giả định có gen hoàn chỉnh
   2. Độ dài biến thiên lớn (100–1800 bp), không có gen đánh dấu phổ quát
   3. Mô hình phải hoạt động trực tiếp trên chuỗi DNA thô để ứng dụng được trên dữ liệu thực

---

## Paragraph Descriptions

1. **Đoạn mở đầu — Khung quy ước:** Phát biểu rằng tất cả nghiên cứu liên quan đều đồng thuận đặt dự đoán lối sống thực khuẩn thể như một bài toán phân loại nhị phân, và giải thích cơ sở sinh học của sự lựa chọn đó (hai chu trình ti sinh học rõ ràng về mặt sinh học và ứng dụng).

2. **Đoạn định nghĩa toán học - Đầu vào:** Định nghĩa hình thức không gian đầu vào S = {A, T, G, C}^L với L ∈ [100, 1800], đặt trong ngữ cảnh thực tiễn metagenomic (contig có thể là đoạn ngắn từ một hệ gen dài hơn, không cần hệ gen hoàn chỉnh).

3. **Đoạn định nghĩa toán học - Nhãn và hàm phân loại:** Định nghĩa Y = {0, 1}, hàm f: S → Y, và bài toán học f* = argmin E[L(f(s), y)] — đặt rõ mục tiêu học máy.

4. **Đoạn công thức hóa xác suất:** Triển khai P(y | s) qua softmax, quyết định phân loại bằng argmax, và hàm binary cross-entropy L_BCE — liên kết trực tiếp đến cách PhaBERT-CNN được tối ưu hóa (đã có ở Chương 3, lần này trình bày ở mức khái niệm chung của bài toán).

5. **Đoạn so sánh biểu diễn đầu vào:** Bảng ngắn hoặc danh sách so sánh năm cách biểu diễn đầu vào của các phương pháp chính, chỉ rõ hạn chế của từng cách — kết thúc bằng câu dẫn: BPE trực tiếp trên DNA thô giải quyết đồng thời các hạn chế này.

6. **Đoạn kết — Ràng buộc thực tiễn:** Đặt lại bài toán trong bối cảnh metagenomic cụ thể: contig phân mảnh, không có gen đánh dấu, độ dài biến thiên, và kết luận rằng đây chính là không gian bài toán mà PhaBERT-CNN được thiết kế để giải quyết — dẫn sang phần mục tiêu nghiên cứu.

---

## Citations

- `\cite{wu2021deephage}` — Mô tả biểu diễn one-hot L×4 của DeePhage — ✓ EXISTS in references.bib
- `\cite{shang2023phatyp}` — Mô tả biểu diễn protein cluster token của PhaTYP và phát biểu bài toán dưới dạng xác suất (Equations 1-3 trong paper, là căn cứ cho cách PhaTYP formalizes nhất) — ✓ EXISTS in references.bib
- `\cite{hockenberry2021bacphlip}` — Mô tả vector hiện diện 206-chiều domain của BACPHLIP — ✓ EXISTS in references.bib
- `\cite{zhang2024deeppl}` — Mô tả k-mer 6 chồng lấp + giới hạn 512 token của DeepPL — ✓ EXISTS in references.bib
- `\cite{tynecki2020phageai}` — Đề cập PhageAI trong so sánh (Word2Vec k-mer + SVM) — ✓ EXISTS in references.bib
- `\cite{mcnair2012phacts}` — PHACTS như tiền thân phương pháp dựa trên protein — ✓ EXISTS in references.bib
- `\cite{zhou2023dnabert}` — BPE tokenization của DNABERT-2, giải thích tại sao BPE loại bỏ rò rỉ thông tin — ✓ EXISTS in references.bib

**Lưu ý:** Không có citation key nào bị thiếu. Không cần thêm citation mới vào references.bib.

---

## Numbers to Verify

- `L ∈ [100, 1800]` — Phạm vi độ dài contig trong bộ chuẩn — Source: `\cite{wu2021deephage}` (DeePhage định nghĩa bộ chuẩn 4 nhóm A-D từ 100-1800 bp); cũng xác nhận trong `chapters/c1/chapter_1.tex` dòng 51 ("100--1800 bp") và `chapters/c3/chapter_3.tex` dòng 24.
- Vector 206 chiều của BACPHLIP — Source: `\cite{hockenberry2021bacphlip}` — **Cần verify** qua paper (paper title: "BACPHLIP: predicting bacteriophage lifestyle from conserved protein domains", PeerJ 2021). DOI không có trong bib, tìm trên PeerJ để xác nhận "206-dim binary domain presence vector".
- Vocab size 45k protein cluster của PhaTYP — Source: `\cite{shang2023phatyp}` — **Cần verify** trong paper (Briefings in Bioinformatics, bbac487); nếu không xác nhận được con số cụ thể, bỏ con số này và chỉ mô tả "protein cluster token với vocabulary lớn".
- k = 6 cho DeepPL k-mer tokenization — Source: `\cite{zhang2024deeppl}` — Đã xác nhận trong `chapters/c2/chapter_2.tex` dòng 174 ("k-mer 6").

---

## Vietnamese Terminology

| English term | Vietnamese (từ vietnamese-terms.md) |
|---|---|
| Binary classification | Phân loại nhị phân |
| DNA Sequence | Chuỗi DNA |
| Virulent phage | Thực khuẩn thể độc lực |
| Temperate phage | Thực khuẩn thể ôn hòa |
| Lifestyle | Lối sống |
| Input space | Không gian đầu vào |
| Output space | Không gian đầu ra |
| Classification function | Hàm phân loại |
| Raw DNA sequence | Chuỗi DNA thô |
| Contig | contig (giữ nguyên tiếng Anh — bioinformatics term) |
| Marker gene | Gen đánh dấu |
| Information leakage | Rò rỉ thông tin |
| BPE (Byte Pair Encoding) | Mã hóa cặp byte (BPE) — giữ BPE |
| Metagenomic | metagenomic (giữ nguyên tiếng Anh) |
| Lytic cycle | Chu trình tan |
| Lysogenic cycle | Chu trình tiềm tan |
| Attention mechanism | Cơ chế chú ý |
| Softmax | softmax (giữ nguyên) |
| Loss function | Hàm mất mát |
| Training | Huấn luyện |
| Pre-training | pre-training (giữ nguyên) |

**Các thuật ngữ phải giữ nguyên tiếng Anh:** embedding, tokenization, token, k-mer, contig, metagenomic, BPE, softmax, dropout, pooling, baseline, BACPHLIP, DeePhage, PhaTYP, DeepPL, PhageAI, DNABERT-2, PhaBERT-CNN, one-hot.

---

## Equations Needed

Tất cả phương trình cần có `\label{}`. Đề xuất các label sau (kiểm tra không trùng với Chapter 3):

```latex
% Eq 1: Định nghĩa không gian đầu vào
s \in \{A, T, G, C\}^L, \quad L \in [100, 1800]
\label{eq:input_space}

% Eq 2: Định nghĩa không gian nhãn và hàm phân loại
f: \mathcal{S} \rightarrow \{0, 1\}, \quad y \in \{0, 1\}
\label{eq:classification_func}

% Eq 3: Xác suất softmax
P(y \mid s) = \text{softmax}(\mathbf{W} \cdot \phi(s))_y
\label{eq:prob_formulation}

% Eq 4: Binary cross-entropy (định nghĩa bài toán học — phiên bản ngắn gọn ở mức khái niệm)
\mathcal{L}_{\text{BCE}} = -\frac{1}{N}\sum_{i=1}^{N}
    \bigl[y_i \log P(1 \mid s_i) + (1-y_i)\log P(0 \mid s_i)\bigr]
\label{eq:bce_c1}
```

**Lưu ý tránh trùng label:** Chapter 3 đã dùng `\label{eq:softmax}` (dòng 183), `\label{eq:bce_loss}` (dòng 207), `\label{eq:cnn_layer1}`, `\label{eq:cnn_layer2}`, `\label{eq:cnn_pool}`. Các label đề xuất ở trên (`eq:input_space`, `eq:classification_func`, `eq:prob_formulation`, `eq:bce_c1`) đều mới, không trùng.

---

## Figures/Tables Needed

**Bảng so sánh biểu diễn đầu vào (tùy chọn — có thể viết dưới dạng danh sách thay vì bảng):**

Nếu dùng bảng:
- Label: `\label{tab:input_representation_comparison}`
- Caption: "So sánh chiến lược biểu diễn đầu vào của các phương pháp phân loại lối sống thực khuẩn"
- Cột: Phương pháp | Biểu diễn đầu vào | Hạn chế chính
- Nội dung: DeePhage (one-hot), BACPHLIP (domain vector), PhaTYP (protein cluster), DeepPL (k-mer), PhaBERT-CNN (BPE)

**Khuyến nghị:** Vì Chapter 2 đã có `\label{tab:comprehensive_method_comparison}` với các cột tương tự, **nên dùng danh sách trong văn bản thay vì bảng** để tránh trùng lặp cấu trúc. Nếu dùng bảng, phải có cột khác biệt rõ ràng (tập trung vào "biểu diễn đầu vào" và "hạn chế tương ứng với bài toán", không phải so sánh hiệu năng).

**Không cần hình ảnh mới** cho phần này. Có thể tham chiếu `\ref{fig:architecture_detail}` từ Chapter 3 nếu cần minh họa pipeline, nhưng không nên forward-reference quá sớm tới chương sau trong Chương 1.

---

## Critical Warnings

1. **Tránh trùng lặp với Chapter 3:** Hàm BCE và softmax đã được định nghĩa chi tiết tại `chapters/c3/chapter_3.tex` (dòng 179-210). Trong mục này, chỉ trình bày ở mức **khái niệm bài toán** — không lặp lại chi tiết kiến trúc như `\mathbf{W}_1`, `\mathbf{W}_2`, các chiều cụ thể. Dùng câu như "Chi tiết kiến trúc được trình bày tại Chương~\ref{chap:method}."

2. **Tránh trùng lặp với Chapter 2:** Chapter 2 (dòng 154-221) đã mô tả chi tiết từng phương pháp. Phần so sánh biểu diễn đầu vào trong mục này phải cô đọng (2-3 dòng mỗi phương pháp) và tập trung vào góc độ **hình thức toán học** của bài toán, không phải mô tả kỹ thuật đầy đủ.

3. **Tránh trùng lặp với sec:scope (dòng 51):** Section `sec:scope` đã nêu "phân loại nhị phân lối sống thực khuẩn thể (virulent/temperate) từ các contig DNA trong phạm vi độ dài 100--1800 bp". Mục `sec:problem_formulation` phải đi sâu hơn vào **định nghĩa toán học hình thức** (không gian đầu vào, hàm phân loại, xác suất, hàm mất mát), không chỉ nhắc lại thông tin đó.

4. **Số liệu BACPHLIP (206 chiều):** Verify trước khi dùng. Nếu không xác nhận được, dùng "vector đặc trưng nhị phân dựa trên sự hiện diện của các miền protein bảo tồn" thay vì "206 chiều".

5. **Số liệu vocab PhaTYP (45k):** Verify trước khi dùng. Paper PhaTYP (shang2023phatyp) có thể không công bố con số này chi tiết — nếu không có, bỏ con số.

---

## Style and Length Guidance

- **Độ dài mục tiêu:** 400-600 từ (tiếng Việt), tương đương 6 đoạn văn ngắn — phù hợp với độ dài các section khác trong Chapter 1 (sec:background ~3 đoạn, sec:challenges ~2 đoạn).
- **Tone:** Hình thức, học thuật — sử dụng định nghĩa và ký hiệu toán học nhưng luôn đi kèm diễn giải bằng ngôn ngữ tự nhiên.
- **Phương trình:** Đặt trong `\begin{equation}...\end{equation}`, không dùng `$$`. Mỗi phương trình phải có label.
- **Kết nối với các section khác:** Mở đầu bằng câu chuyển tiếp từ `sec:challenges`, kết thúc bằng câu dẫn sang `sec:objectives`.
- **Ký hiệu nhất quán với Chapter 3:** Dùng $y \in \{0, 1\}$ (0 = temperate, 1 = virulent), $s$ cho chuỗi DNA, $\mathcal{L}_{\text{BCE}}$ cho hàm mất mát — tất cả đã dùng trong `chapters/c3/chapter_3.tex`.

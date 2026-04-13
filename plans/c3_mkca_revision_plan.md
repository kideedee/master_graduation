# Plan: Chương 3 — Đổi tên MKCA → MKC và bỏ Attention Pooling, thay bằng Masked Mean Pooling

## Bối cảnh thay đổi

Model `phabert_cnn_model.py` đã được sửa lại thành class `Dnabert2CnnModelNoAttention`. Thay đổi cốt lõi: **nhánh Attention Pooling bị xóa hoàn toàn**, thay bằng **masked mean pooling** đơn giản và xác định. Luận văn phải phản ánh đúng kiến trúc thực tế đã cài đặt.

## Đổi tên module: MKCA → MKC

- **MKCA** = Multi-Kernel Convolutional **Attention** — không còn chính xác vì đã bỏ Attention
- **MKC** = Multi-Kernel Convolution — đơn giản, phản ánh đúng thành phần chính

**Tất cả** vị trí "MKCA" và "Multi-Kernel Convolutional Attention" trong chương 3 phải đổi thành "MKC" và "Multi-Kernel Convolution".

**Đổi tên MKCA → MKC và cập nhật "attention pooling" → "masked mean pooling" tại TẤT CẢ files:**
- `chapters/c3/chapter_3.tex` — chi tiết bên dưới
- `chapters/glossary.tex` (dòng 45)
- `chapters/c1/chapter_1.tex` (dòng 23, 38, 60)
- `chapters/c4/chapter_4.tex` (dòng 11, 23, 25, 34, 95, 100, 111, 116)
- `chapters/c5/chapter_5.tex` (dòng 7, 11, 16)

## Các vị trí cần sửa trong `chapters/c3/chapter_3.tex`

### 1. Đoạn mở đầu chương (dòng 4) — sửa mô tả kiến trúc

**Hiện tại:** "kiến trúc chuyên biệt bao gồm mạng nơ-ron tích chập đa cửa sổ kết hợp với lớp gộp chú ý"

**Sửa thành:** bỏ "lớp gộp chú ý", thay bằng "nhánh CNN đa kernel kết hợp với pooling trung bình có mặt nạ toàn cục"

---

### 2. Phần 3.1 — Tổng quan phương pháp (dòng 11–15)

**Hiện tại (dòng 11–12):** Mô tả PhaBERT-CNN với "kiến trúc MKCA" có "bốn ưu điểm chính", liệt kê 3 ưu điểm (điểm 4 bị thiếu trong nhánh).

**Hiện tại (dòng 15):** "nhánh Attention Pooling~\cite{lin2017structured} tổng hợp thông tin toàn cục có trọng số"

**Sửa dòng 15:** Thay "nhánh Attention Pooling~\cite{lin2017structured} tổng hợp thông tin toàn cục có trọng số" bằng "masked mean pooling tổng hợp thông tin toàn cục từ tất cả vị trí chuỗi"

**Xóa `\cite{lin2017structured}`** khỏi câu này (không còn dùng attention pooling tại đây).

---

### 3. Subsection `\subsection{Mô-đun MKC}` (dòng 114–116)

**Hiện tại:** "mô-đun MKCA được thiết kế với hai nhánh song song có chức năng bổ trợ nhau: nhánh CNN đa kernel thực hiện trích xuất đặc trưng cục bộ đa kernel, trong khi nhánh Attention Pooling tổng hợp thông tin ngữ cảnh toàn cục thông qua cơ chế gán trọng số thích nghi theo tầm quan trọng của từng vị trí chuỗi."

**Sửa thành:** Đổi tiêu đề subsection `\subsection{Mô-đun MKCA}` → `\subsection{Mô-đun MKC}`. Mô tả mô-đun MKC có hai nhánh song song: (1) nhánh CNN đa kernel trích xuất đặc trưng cục bộ đa tỷ lệ, (2) nhánh masked mean pooling tổng hợp thông tin toàn cục bằng cách tính trung bình có trọng số theo attention mask — loại bỏ các token padding.

---

### 4. Xóa toàn bộ subsubsection `Nhánh Attention Pooling toàn cục` (dòng 139–163)

Xóa toàn bộ khối từ `\subsubsection{Nhánh Attention Pooling toàn cục}` đến hết phương trình `\label{eq:attn_proj}`, bao gồm:
- eq:attn_hidden, eq:attn_score, eq:attn_weights, eq:attn_aggregate, eq:attn_proj
- Đoạn giải thích ưu điểm của attention pooling so với max/average pooling

---

### 5. Thêm subsubsection mới: `Nhánh Masked Mean Pooling toàn cục`

Thay thế subsubsection bị xóa bằng mô tả masked mean pooling theo đúng code trong `phabert_cnn_model.py` (forward(), dòng 122–134).

**Nội dung subsubsection mới:**

Nhánh thứ hai áp dụng masked mean pooling để tổng hợp thông tin mức chuỗi từ các hidden states của DNABERT-2. Không giống attention pooling học trọng số thích nghi, masked mean pooling tính trung bình đơn giản trên tất cả token không phải padding, đảm bảo tính xác định và tránh quá khớp với tập huấn luyện nhỏ.

Cho hidden states $\mathbf{H} = \{\mathbf{h}_1, \ldots, \mathbf{h}_n\} \in \mathbb{R}^{n \times 768}$ và attention mask $\mathbf{m} \in \{0, 1\}^n$ (1 = token thực, 0 = padding):

**Phương trình mean pooling:**
$$\mathbf{g} = \frac{\sum_{t=1}^{n} m_t \cdot \mathbf{h}_t}{\sum_{t=1}^{n} m_t} \in \mathbb{R}^{768}$$

Label: `\label{eq:mean_pooling}`

**Phương trình chiếu tuyến tính:**
$$\mathbf{f}_{\text{global}} = \text{Dropout}\!\left(\text{ReLU}(\mathbf{W}_g \mathbf{g} + \mathbf{b}_g)\right) \in \mathbb{R}^{128}$$

Label: `\label{eq:global_proj}`

trong đó $\mathbf{W}_g \in \mathbb{R}^{128 \times 768}$, $\mathbf{b}_g \in \mathbb{R}^{128}$, dropout rate = 0.1.

Giải thích ngắn: Masked mean pooling bỏ qua các token padding (do các chuỗi trong batch có độ dài khác nhau và được đệm về cùng độ dài), đảm bảo chỉ các token thực sự mang thông tin sinh học mới đóng góp vào biểu diễn toàn cục.

---

### 6. Sửa subsection `Kết Hợp Đặc Trưng và Đầu Phân Loại` (dòng 165–189)

**Sửa phương trình eq:feature_fusion (dòng 170–171):**

Hiện tại:
$$\mathbf{f}_{\text{combined}} = [\mathbf{f}_{\text{attn}}; \mathbf{f}_{\text{CNN}}] = [\mathbf{f}_{\text{attn}}; \mathbf{f}^{(3)}; \mathbf{f}^{(5)}; \mathbf{f}^{(7)}] \in \mathbb{R}^{512}$$

Sửa thành:
$$\mathbf{f}_{\text{combined}} = [\mathbf{f}_{\text{global}}; \mathbf{f}_{\text{CNN}}] = [\mathbf{f}_{\text{global}}; \mathbf{f}^{(3)}; \mathbf{f}^{(5)}; \mathbf{f}^{(7)}] \in \mathbb{R}^{512}$$

**Sửa câu giải thích (dòng 174):**

Hiện tại: "kết hợp cả ngữ cảnh toàn cục từ nhánh attention (128 chiều) và đặc trưng cục bộ đa kernel từ các nhánh CNN (384 chiều)"

Sửa thành: "kết hợp biểu diễn toàn cục từ masked mean pooling (128 chiều) và đặc trưng cục bộ đa kernel từ các nhánh CNN (384 chiều)"

---

### 7. Sửa phần Regularization trong Chiến lược huấn luyện (dòng 213)

**Hiện tại:** "Dropout với rate = 0.1 được áp dụng sau attention pooling và trong đầu phân loại"

**Sửa thành:** "Dropout với rate = 0.1 được áp dụng sau global pooling và trong đầu phân loại"

---

### 8. Sửa kết luận chương (dòng 246)

**Hiện tại:** "Phương pháp kết hợp mô hình nền tảng DNABERT-2 với mô-đun MKCA gồm nhánh CNN đa kernel và nhánh attention pooling"

**Sửa thành:** "Phương pháp kết hợp mô hình nền tảng DNABERT-2 với mô-đun MKC gồm nhánh CNN đa kernel và nhánh masked mean pooling toàn cục"

---

## Outline tổng hợp các thay đổi

```
=== Chương 3 ===
I.   Đoạn mở đầu chương (dòng 4): bỏ "lớp gộp chú ý"
II.  Phần 3.1 (dòng 11): đổi MKCA → MKC, Multi-Kernel Convolutional Attention → Multi-Kernel Convolution
III. Phần 3.1 (dòng 15): thay "Attention Pooling\cite{lin2017structured}" → "masked mean pooling"
IV.  Phần 3.2 (dòng 87): đổi "Mô đun MKCA" → "Mô đun MKC"
V.   Đổi tiêu đề subsec (dòng 114): "Mô-đun MKCA" → "Mô-đun MKC"
VI.  Mở đầu subsec MKC (dòng 116): cập nhật mô tả hai nhánh, MKCA → MKC
VII. Xóa subsubsec "Nhánh Attention Pooling toàn cục" (dòng 139–163)
VIII.Thêm subsubsec mới "Nhánh Masked Mean Pooling toàn cục"
IX.  Sửa eq:feature_fusion: f_attn → f_global
X.   Sửa câu giải thích feature fusion (dòng 174)
XI.  Sửa dòng 194, 198: MKCA → MKC
XII. Sửa regularization (dòng 213): "attention pooling" → "global pooling"
XIII.Sửa kết luận chương (dòng 246): MKCA → MKC, attention pooling → masked mean pooling

=== Chương 1 ===
XIV. Dòng 23: MKCA → MKC, Multi-Kernel Convolutional Attention → Multi-Kernel Convolution
XV.  Dòng 38: MKCA → MKC, attention pooling → masked mean pooling
XVI. Dòng 60: MKCA → MKC

=== Chương 4 ===
XVII.  Dòng 11, 23, 25, 34, 95, 100, 102, 111, 116: MKCA → MKC, attention pooling → masked mean pooling, xóa \cite{lin2017structured}

=== Chương 5 ===
XVIII. Dòng 7, 11, 16: MKCA → MKC, attention pooling → masked mean pooling

=== Glossary ===
XIX.   Dòng 45: MKCA → MKC, Multi-Kernel Convolutional Attention → Multi-Kernel Convolution
```

---

## Paragraph Descriptions

1. **Subsec MKC intro (sửa):** Mô tả MKC (Multi-Kernel Convolution) có hai nhánh song song: CNN đa kernel và masked mean pooling toàn cục — bỏ hoàn toàn đề cập attention pooling.

2. **Subsubsec Masked Mean Pooling — mở đầu:** Giới thiệu masked mean pooling là phương án tổng hợp toàn cục xác định, tính trung bình trên các token không phải padding, đơn giản và hiệu quả cho chuỗi có độ dài biến đổi.

3. **Subsubsec Masked Mean Pooling — phương trình:** Trình bày eq:mean_pooling (tính trung bình có mặt nạ) và eq:global_proj (chiếu tuyến tính 768→128).

4. **Subsubsec Masked Mean Pooling — giải thích:** Giải thích tại sao cần attention mask (loại bỏ padding token), tính xác định của phép tính, và lý do lựa chọn masked mean pooling thay vì attention pooling.

---

## Citations

- `\cite{lin2017structured}` — Dùng cho attention pooling — **CHỈ XÓA** khỏi dòng 15 (tổng quan) và toàn bộ subsubsec bị xóa. Không thêm vào đâu mới. — ✓ EXISTS in references.bib (nhưng không còn cần thiết sau khi sửa)
- `\cite{kim2014convolutional}` — Vẫn giữ cho nhánh CNN đa kernel — ✓ EXISTS
- `\cite{johnson2017deep}` — Vẫn giữ cho hai lớp Conv1d xếp chồng — ✓ EXISTS
- `\cite{zhou2023dnabert}` — Vẫn giữ cho DNABERT-2 backbone — ✓ EXISTS

---

## Numbers to Verify

- `128` chiều f_global — Source: `implementation/phabert_cnn_model.py` dòng 76–79 (`nn.Linear(768, 128)`) — CONFIRMED
- `384` chiều f_CNN — Source: `implementation/phabert_cnn_model.py` dòng 86 (`128 * 3`) — CONFIRMED
- `512` chiều f_combined — Source: `implementation/phabert_cnn_model.py` dòng 86 (`128 * 3 + 128 = 512`) — CONFIRMED
- Dropout rate `0.1` — Source: `implementation/phabert_cnn_model.py` dòng 79 (`nn.Dropout(0.1)`) — CONFIRMED
- `768` → `128` linear projection — Source: `implementation/phabert_cnn_model.py` dòng 77 (`nn.Linear(768, 128)`) — CONFIRMED

---

## Vietnamese Terminology

- Masked mean pooling → masked mean pooling (giữ tiếng Anh, thuật ngữ kỹ thuật)
- Attention pooling → attention pooling (giữ tiếng Anh — "Forbidden Substitutions" list)
- pooling → pooling (giữ tiếng Anh — "Forbidden Substitutions" list)
- attention mask → attention mask (giữ tiếng Anh — "Forbidden Substitutions" list)
- Nhánh song song → nhánh song song (Vietnamese)
- Biểu diễn toàn cục → biểu diễn toàn cục (Vietnamese for "global representation")
- Token padding → token padding (giữ tiếng Anh — token trong "Forbidden Substitutions")
- Trung bình có mặt nạ → trung bình có mặt nạ (Vietnamese for "masked mean")

---

## Figures/Tables Needed

Không cần hình/bảng mới. Kiến trúc tổng thể `fig:architecture_detail` cần được cập nhật nếu hình hiện tại vẽ nhánh Attention Pooling — nhưng đây là file ảnh nằm ngoài phạm vi kế hoạch viết này.

---

## Lưu ý quan trọng cho implementation

1. Khi xóa subsubsec Attention Pooling, **không xóa label** nào đang được `\ref{}` ở nơi khác trong chương. Kiểm tra: `grep -n "eq:attn" chapters/c3/chapter_3.tex` — tất cả các label eq:attn_hidden, eq:attn_score, eq:attn_weights, eq:attn_aggregate, eq:attn_proj chỉ xuất hiện trong nội bộ subsubsec đó, không bị `\ref{}` từ nơi khác.

2. Tên subsubsec mới gợi ý: `\subsubsection{Nhánh Masked Mean Pooling toàn cục}`

3. Câu mô tả `\mathbf{f}_{\text{combined}}` tại dòng 174 cần đổi `\mathbf{f}_{\text{attn}}` → `\mathbf{f}_{\text{global}}` đồng bộ với phương trình eq:feature_fusion.

4. Kiểm tra dòng 213 (regularization): câu "Dropout ... sau attention pooling" phải đổi thành "sau global pooling".

---

## Thay đổi ngoài Chương 3: Đổi MKCA → MKC và attention pooling → masked mean pooling

### A. `chapters/glossary.tex` (dòng 45)

**Hiện tại:** `37 & MKCA & Multi-Kernel Convolutional Attention & Mô đun tích chập đa nhân kết hợp cơ chế chú ý`

**Sửa thành:** `37 & MKC & Multi-Kernel Convolution & Mô đun tích chập đa nhân`

---

### B. `chapters/c1/chapter_1.tex`

**Dòng 23:** Đổi `mô đun MKCA (Multi-Kernel Convolutional Attention)` → `mô đun MKC (Multi-Kernel Convolution)`

**Dòng 38:** Đổi `mô đun MKCA gồm nhánh CNN đa kernel (kích thước 3, 5, 7) kết hợp nhánh attention pooling, cho phép đồng thời trích xuất đặc trưng cục bộ đa tỷ lệ và biểu diễn ngữ cảnh toàn cục có trọng số` → `mô đun MKC gồm nhánh CNN đa kernel (kích thước 3, 5, 7) kết hợp masked mean pooling toàn cục, cho phép đồng thời trích xuất đặc trưng cục bộ đa tỷ lệ và biểu diễn toàn cục từ tất cả vị trí chuỗi`

**Dòng 60:** Đổi `mô đun MKCA` → `mô đun MKC`

---

### C. `chapters/c4/chapter_4.tex`

**Dòng 11:** Đổi `kiến trúc MKCA` → `kiến trúc MKC`

**Dòng 23:** Đổi `Đánh giá đóng góp của MKCA` → `Đánh giá đóng góp của MKC`

**Dòng 25:** Đổi `không có MKCA` → `không có MKC`. Đổi `đóng góp của mô đun MKCA (bao gồm nhánh CNN đa kernel và attention pooling)` → `đóng góp của mô đun MKC (bao gồm nhánh CNN đa kernel và masked mean pooling)`

**Dòng 34:** Đổi `MKCA mang lại cải thiện có ý nghĩa` → `MKC mang lại cải thiện có ý nghĩa`. Đổi `cơ chế attention pooling~\cite{lin2017structured} giúp tổng hợp thông tin có trọng số từ các vị trí quan trọng trong chuỗi` → `masked mean pooling giúp tổng hợp thông tin toàn cục từ tất cả vị trí chuỗi`. Xóa `\cite{lin2017structured}`.

**Dòng 95:** Đổi `kiến trúc MKCA với ba nhánh tích chập song song (kernel sizes 3, 5, 7)~\cite{kim2014convolutional} và attention pooling~\cite{lin2017structured} cho phép mô hình đồng thời nắm bắt các đặc trưng cục bộ ở nhiều tỷ lệ không gian và tổng hợp ngữ cảnh toàn cục có trọng số` → `kiến trúc MKC với ba nhánh tích chập song song (kernel sizes 3, 5, 7)~\cite{kim2014convolutional} và masked mean pooling cho phép mô hình đồng thời nắm bắt các đặc trưng cục bộ ở nhiều tỷ lệ không gian và tổng hợp thông tin toàn cục`. Xóa `\cite{lin2017structured}`.

**Dòng 100:** Đổi `đóng góp của MKCA tăng dần` → `đóng góp của MKC tăng dần`

**Dòng 102:** Đổi `cơ chế attention pooling~\cite{lin2017structured} đóng vai trò quan trọng trong việc phát hiện phage ôn hòa` → `kiến trúc MKC đóng vai trò quan trọng trong việc phát hiện phage ôn hòa`. Xóa `\cite{lin2017structured}`. Đổi câu tiếp `Cơ chế chú ý cho phép mô hình gán trọng số cao hơn cho các vị trí mang tín hiệu đặc trưng` → `Nhánh CNN đa kernel cho phép mô hình nắm bắt các motif cục bộ ở nhiều tỷ lệ không gian mang tín hiệu đặc trưng`

**Dòng 111:** Đổi `(MKCA)` → `(MKC)`

**Dòng 116:** Đổi `MKCA` → `MKC` (2 lần), đổi `các thành phần CNN và attention pooling đóng góp` → `các thành phần CNN và masked mean pooling đóng góp`

---

### D. `chapters/c5/chapter_5.tex`

**Dòng 7:** Đổi `mô đun MKCA gồm nhánh CNN đa kernel và nhánh attention pooling` → `mô đun MKC gồm nhánh CNN đa kernel và masked mean pooling toàn cục`

**Dòng 11:** Đổi `kiến trúc chuyên biệt MKCA` → `kiến trúc chuyên biệt MKC`

**Dòng 16:** Đổi `mô đun MKCA chuyên biệt` → `mô đun MKC chuyên biệt`. Đổi `nhánh attention pooling để tổng hợp biểu diễn toàn cục có trọng số từ các token embeddings` → `masked mean pooling để tổng hợp biểu diễn toàn cục từ tất cả token embeddings`

---

### E. Kiểm tra `\cite{lin2017structured}` sau khi sửa

Sau khi sửa, `\cite{lin2017structured}` có thể không còn được dùng ở đâu. Cần kiểm tra: `grep -rn "lin2017structured" chapters/` — nếu không còn citation nào, giữ entry trong `references.bib` nhưng ghi chú là không còn dùng (hoặc có thể xuất hiện ở chương 2 nên cần kiểm tra).

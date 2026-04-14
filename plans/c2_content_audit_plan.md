# Plan: Chương 2 — Rà soát nội dung toàn chương

## Bối cảnh

Đây là kế hoạch rà soát (content audit) toàn bộ `chapters/c2/chapter_2.tex`. Chương 2 hiện có 219 dòng, bao gồm 4 section chính. Tất cả citation key đã được xác minh tồn tại trong `references.bib`. Mục tiêu: phát hiện lỗi cấu trúc, số liệu sai format, số liệu cần xác minh, và nội dung cần bổ sung hoặc chỉnh sửa.

---

## Các vấn đề đã xác định

### VẤN ĐỀ 1 — Cấu trúc: `\label` bị đặt sai vị trí (NGHIÊM TRỌNG)

**Vị trí:** Dòng 47 và dòng 70

`\section{Nền tảng học sâu}` (dòng 47) **không có `\label{}`** ngay sau nó. Label `\label{sec:deep_learning_foundation}` bị đặt lạc ở dòng 70 — sau `\subsection{Mạng nơ-ron nhân tạo}`, giữa đoạn văn cuối của subsection đó và `\subsection{Mạng nơ-ron tích chập}`.

Hậu quả: `\ref{sec:deep_learning_foundation}` trỏ đến vị trí sai trong PDF (trỏ đến giữa Mục 2.2.1 thay vì đầu Section 2.2).

**Sửa:**
- Dòng 47–48: thêm `\label{sec:deep_learning_foundation}` ngay sau `\section{Nền tảng học sâu}`
- Dòng 70: xóa dòng `\label{sec:deep_learning_foundation}` đứng lạc

---

### VẤN ĐỀ 2 — Số liệu cần xác minh: DNABERT-2 so với DNABERT (dòng 123)

**Vị trí:** Dòng 123

Câu hiện tại:
> "...giúp mô hình hiệu quả hơn 3 lần so với DNABERT trong khi chỉ sử dụng một phần ba số FLOPs mặc dù có nhiều hơn 30\% tham số."

Ba con số ở đây — "3 lần", "một phần ba FLOPs", "30% tham số" — so sánh **DNABERT-2 với DNABERT gốc**. Tuy nhiên câu viết hơi mâu thuẫn: nếu dùng "1/3 FLOPs" thì tức là hiệu quả hơn 3 lần, hai vế tương đương nhau. Nên chọn một cách diễn đạt duy nhất.

**Sửa đề xuất:** Xóa "3 lần" (hoặc "một phần ba") để tránh lặp, ví dụ:
> "...giúp mô hình chỉ sử dụng khoảng một phần ba số FLOPs so với DNABERT trong quá trình huấn luyện, mặc dù có nhiều hơn 30\% tham số."

**Cần xác minh:** Con số "30% tham số nhiều hơn" cần đối chiếu với bài báo `zhou2023dnabert` (arXiv:2306.15006). DNABERT-2 có ~117M tham số, DNABERT gốc có ~86M — chênh lệch ~36%, không phải 30%. Cần WebFetch để xác nhận con số chính xác từ bài báo.

---

### VẤN ĐỀ 3 — Số liệu cần xác minh: "21 lần nhỏ hơn" và "92 lần GPU" (dòng 125)

**Vị trí:** Dòng 125

Câu hiện tại:
> "...DNABERT-2 đạt hiệu năng tương đương mô hình Nucleotide Transformer 2,5 tỉ tham số~\cite{dalla2025nucleotide} trong khi nhỏ hơn 21 lần và yêu cầu ít hơn khoảng 92 lần thời gian GPU trong quá trình huấn luyện trước."

Hai con số "21 lần" và "92 lần" cần được xác minh qua WebFetch bài báo DNABERT-2 (`https://arxiv.org/abs/2306.15006`). Đây là con số định lượng mạnh, nếu sai sẽ bị phản biện khi bảo vệ.

**Cần xác minh:** WebFetch `https://arxiv.org/abs/2306.15006`

---

### VẤN ĐỀ 4 — Số liệu cần xác minh: "10 lần ngắn hơn hoặc 15 lần dài hơn" (dòng 125)

**Vị trí:** Dòng 125 (cuối)

Câu:
> "...xử lý hiệu quả các đầu vào ngắn hơn 10 lần hoặc dài hơn 15 lần so với dữ liệu huấn luyện trước."

Nếu độ dài huấn luyện trước trung bình là 700 bp:
- Ngắn hơn 10 lần = ~70 bp — khớp với "chuỗi có độ dài từ 70 đến 10.000 bp" trong câu trước
- Dài hơn 15 lần = ~10.500 bp — khớp với con số 10.000 bp

Về logic các con số có nhất quán, nhưng cần xác minh nguồn gốc "10 lần" và "15 lần" là từ bài báo hay là suy luận của người viết. Nếu là suy luận, nên đổi thành nêu trực tiếp phạm vi (70–10.000 bp) thay vì dùng bội số.

**Đề xuất sửa:** Đổi thành phạm vi tuyệt đối:
> "...xử lý hiệu quả các đầu vào có độ dài từ 70 đến trên 10.000~bp, tương ứng phạm vi rộng hơn nhiều so với độ dài huấn luyện trước trung bình."

---

### VẤN ĐỀ 5 — Format số thập phân dùng dấu chấm thay vì dấu phẩy (dòng 121)

**Vị trí:** Dòng 121

> "BPE xây dựng từ điển gồm **4.096** token..."

Trong tiếng Việt, dấu chấm (.) trong số nguyên lớn là dấu phân cách hàng nghìn — đây là format **đúng** cho số nguyên 4096. Không phải số thập phân, không cần sửa.

Tuy nhiên, cần đảm bảo nhất quán: số "4.096" dùng dấu chấm làm phân cách hàng nghìn — đây là chuẩn tiếng Việt cho số nguyên lớn, nhưng trong LaTeX toán học thường dùng `\,` (thin space) thay vì dấu chấm. Xem xét đổi sang `4~096` hoặc `4.096` tùy quy ước nhất quán trong toàn thesis.

**Cần kiểm tra:** Xem các chương khác dùng format nào cho số nguyên 4 chữ số (vd: 1.200 hay 1200 hay 1~200).

---

### VẤN ĐỀ 6 — Thiếu chú giải về "4.096" trong từ điển BPE (dòng 121)

**Vị trí:** Dòng 121

Câu nêu "BPE xây dựng từ điển gồm 4.096 token" — đây là con số cụ thể của DNABERT-2, nhưng không có citation ngay sau. Citation `\cite{zhou2023dnabert,raffel2020exploring}` ở cuối đoạn bao phủ claim về "span prediction" chứ không trực tiếp cho con số 4.096. Nên thêm `\cite{zhou2023dnabert}` ngay sau "4.096 token".

**Sửa:** Đổi "từ điển gồm 4.096 token" → "từ điển gồm 4.096 token~\cite{zhou2023dnabert}"

---

### VẤN ĐỀ 7 — DeePhage: "vượt trội ~30%" cần xác minh (dòng 167)

**Vị trí:** Dòng 167

Câu:
> "DeePhage...đạt độ chính xác kiểm định chéo 5 lần lên đến 89\%, vượt trội so với PHACTS khoảng 30\% trên cùng bộ dữ liệu~\cite{wu2021deephage}."

PHACTS đạt "xấp xỉ 90% trên bộ gen hoàn chỉnh" (dòng 156) nhưng "chỉ đạt khoảng 50% trên các đoạn 100--1800~bp" (dòng 156). Vậy "vượt trội 30%" so với 50% → DeePhage đạt ~80%? Nhưng câu nói DeePhage đạt 89%. 89% - 50% = 39%, không phải 30%.

Nếu "~30%" là so trên tập dữ liệu cụ thể nào đó (không phải tổng hợp), cần ghi rõ. Nếu là xấp xỉ chung thì cần xem lại số liệu từ bài báo `wu2021deephage`.

**Cần xác minh:** WebFetch bài báo DeePhage để xác nhận con số so sánh với PHACTS.

---

### VẤN ĐỀ 8 — PhaTYP: "92,29% độ nhạy và 91,02% độ chính xác" cần xác minh (dòng 169)

**Vị trí:** Dòng 169

Các số liệu cụ thể này cần đối chiếu với bài báo `shang2023phatyp`. Format dấu phẩy đã đúng chuẩn tiếng Việt.

**Cần xác minh:** Xác nhận đây là sensitivity và precision (hay accuracy và sensitivity?) trên Nhóm D từ bài báo PhaTYP.

---

### VẤN ĐỀ 9 — ProkBERT: "80,68% đến 85,35%" — nguồn và ngữ cảnh (dòng 173)

**Vị trí:** Dòng 173

Phạm vi "80,68%--85,35%" được nêu nhưng không rõ đây là trên bộ chuẩn nào hay tập con nào. Câu cần thêm ngữ cảnh: "trên bộ chuẩn phân loại phage" đã có nhưng chưa rõ nhóm độ dài nào.

**Sửa đề xuất:** Thêm ngữ cảnh: "...đạt độ chính xác dao động từ 80,68\% đến 85,35\% trên các nhóm contig A--D trong bộ chuẩn phân loại phage~\cite{ligeti2024prokbert}."

---

### VẤN ĐỀ 10 — Thiếu section giới thiệu tổng quan cho Section 2.2 (dòng 47)

**Vị trí:** Dòng 47–49

Section `\section{Nền tảng học sâu}` bắt đầu ngay vào `\subsection{Mạng nơ-ron nhân tạo}` mà không có đoạn giới thiệu tổng quan cho section (như Section 2.1 và 2.4 đều có). Nên thêm 1--2 câu giới thiệu nêu section này trình bày gì và tại sao liên quan đến bài toán.

**Sửa đề xuất:** Thêm 2 câu sau `\section{Nền tảng học sâu}` và label:
> "Phần này trình bày các kiến trúc học sâu cơ bản được sử dụng trong nghiên cứu: mạng nơ-ron nhân tạo, mạng nơ-ron tích chập (CNN), kiến trúc Transformer, BERT, và mô hình nền tảng hệ gen DNABERT-2. Các kiến trúc này tạo thành nền tảng lý thuyết trực tiếp cho mô hình PhaBERT-CNN được đề xuất ở Chương~\ref{chap:method}."

---

### VẤN ĐỀ 11 — Thiếu section giới thiệu cho Section 2.3 (dòng 128)

**Vị trí:** Dòng 128–132

`\section{Học chuyển giao trong tin sinh học}` cũng bắt đầu thẳng vào subsection. Nên thêm 1 câu giới thiệu ngắn.

**Sửa đề xuất:** Thêm sau label:
> "Phần này trình bày paradigm huấn luyện trước--tinh chỉnh và các chiến lược tinh chỉnh phù hợp cho bài toán phân loại lối sống phage, bao gồm tinh chỉnh phân biệt và kỹ thuật mở khóa dần dần."

---

### VẤN ĐỀ 12 — "Bảng~\ref" không có số thực tế, chỉ có label (dòng 185)

**Vị trí:** Dòng 185

> "Bảng~\ref{tab:comprehensive_method_comparison} tổng hợp..."

Đây là đúng chuẩn LaTeX cross-reference. Không cần sửa.

---

### VẤN ĐỀ 13 — PhageAI: thiếu citation \cite{tynecki2020phageai} cho con số hiệu năng (dòng 158)

**Vị trí:** Dòng 158

Câu "PhageAI đạt hiệu năng tốt trên bộ gen hoàn chỉnh, tuy nhiên bị hạn chế trên contig ngắn" — claim về hiệu năng không có citation trực tiếp (citation `\cite{tynecki2020phageai}` chỉ ở đầu câu giới thiệu PhageAI). Đây có thể OK vì claim này mang tính tổng hợp, nhưng nếu muốn mạnh hơn nên thêm citation.

---

## Outline các sửa đổi theo mức độ ưu tiên

### Ưu tiên cao (lỗi cấu trúc hoặc số liệu có thể sai)

1. **Sửa `\label` bị đặt sai** (Vấn đề 1)
   - Dòng 47: thêm `\label{sec:deep_learning_foundation}` sau `\section{Nền tảng học sâu}`
   - Dòng 70: xóa dòng `\label{sec:deep_learning_foundation}` lạc chỗ

2. **Xác minh và sửa câu dòng 123** (Vấn đề 2)
   - WebFetch bài báo DNABERT-2 để xác nhận "30% tham số"
   - Viết lại câu tránh lặp "3 lần" / "một phần ba"

3. **Xác minh "21 lần" và "92 lần GPU"** (Vấn đề 3)
   - WebFetch `https://arxiv.org/abs/2306.15006`

4. **Xác minh "vượt trội ~30%" DeePhage vs PHACTS** (Vấn đề 7)

### Ưu tiên trung bình (cải thiện rõ ràng)

5. **Thêm citation cho "4.096 token"** (Vấn đề 6) — sửa nhanh

6. **Sửa câu dòng 125 về "10 lần/15 lần"** (Vấn đề 4) — dùng số tuyệt đối

7. **Thêm ngữ cảnh cho ProkBERT "80,68%--85,35%"** (Vấn đề 9) — thêm "nhóm A--D"

8. **Xác minh PhaTYP 92,29% và 91,02%** (Vấn đề 8)

### Ưu tiên thấp (cải thiện chất lượng viết)

9. **Thêm đoạn giới thiệu Section 2.2** (Vấn đề 10)

10. **Thêm đoạn giới thiệu Section 2.3** (Vấn đề 11)

---

## Mô tả từng thay đổi cụ thể

### Thay đổi A: Sửa label (Vấn đề 1)

**Vị trí trong file:** Dòng 47 và dòng 70

Dòng 47–48 hiện tại:
```latex
\section{Nền tảng học sâu}

\subsection{Mạng nơ-ron nhân tạo}
```

Sau khi sửa:
```latex
\section{Nền tảng học sâu}
\label{sec:deep_learning_foundation}

\subsection{Mạng nơ-ron nhân tạo}
```

Dòng 70 hiện tại (xóa):
```latex
\label{sec:deep_learning_foundation}
```

---

### Thay đổi B: Thêm citation cho "4.096 token" (Vấn đề 6)

**Vị trí:** Dòng 121

Hiện tại: `BPE xây dựng từ điển gồm 4.096 token bằng cách`

Sau sửa: `BPE xây dựng từ điển gồm 4.096 token~\cite{zhou2023dnabert} bằng cách`

---

### Thay đổi C: Sửa câu dòng 123 tránh lặp (Vấn đề 2 — sau khi xác minh)

**Vị trí:** Dòng 123

Hiện tại:
```
giúp mô hình hiệu quả hơn 3 lần so với DNABERT trong khi chỉ sử dụng một phần ba số FLOPs mặc dù có nhiều hơn 30\% tham số.
```

Sau sửa (phụ thuộc vào kết quả xác minh WebFetch):
```
giúp mô hình chỉ yêu cầu khoảng một phần ba số FLOPs so với DNABERT trong quá trình tiền huấn luyện, mặc dù có nhiều hơn [X]\% tham số~\cite{zhou2023dnabert}.
```

---

### Thay đổi D: Sửa dòng 125 từ bội số sang phạm vi tuyệt đối (Vấn đề 4)

**Vị trí:** Cuối dòng 125

Hiện tại:
```
xử lý hiệu quả các đầu vào ngắn hơn 10 lần hoặc dài hơn 15 lần so với dữ liệu huấn luyện trước.
```

Sau sửa:
```
xử lý hiệu quả các đầu vào có độ dài từ 70~bp đến trên 10.000~bp --- rộng hơn đáng kể so với độ dài huấn luyện trước trung bình~\cite{zhou2023dnabert}.
```

---

### Thay đổi E: Thêm ngữ cảnh cho ProkBERT (Vấn đề 9)

**Vị trí:** Dòng 173

Hiện tại:
```
ProkBERT đạt độ chính xác dao động từ 80,68\% đến 85,35\% trên bộ chuẩn phân loại phage.
```

Sau sửa:
```
ProkBERT đạt độ chính xác dao động từ 80,68\% đến 85,35\% trên các nhóm contig A--D trong bộ chuẩn phân loại phage~\cite{ligeti2024prokbert}.
```

---

### Thay đổi F: Thêm đoạn giới thiệu Section 2.2 (Vấn đề 10)

**Vị trí:** Sau dòng 47–48 (sau `\section` + `\label` mới)

Nội dung thêm:
```latex
Phần này trình bày các kiến trúc học sâu nền tảng được kế thừa trong nghiên cứu: mạng nơ-ron nhân tạo, mạng nơ-ron tích chập (CNN), kiến trúc Transformer, mô hình BERT, và mô hình nền tảng hệ gen DNABERT-2. Mỗi thành phần cung cấp cơ sở lý thuyết trực tiếp cho một phần của kiến trúc PhaBERT-CNN được đề xuất tại Chương~\ref{chap:method}.
```

---

### Thay đổi G: Thêm đoạn giới thiệu Section 2.3 (Vấn đề 11)

**Vị trí:** Sau dòng 129 (`\label{sec:transfer_learning}`)

Nội dung thêm:
```latex
Phần này trình bày cơ sở lý thuyết của học chuyển giao trong bối cảnh phân tích hệ gen, bao gồm paradigm huấn luyện trước--tinh chỉnh và các chiến lược tinh chỉnh phù hợp cho dữ liệu sinh học có nhãn hạn chế.
```

---

## Citations

- `\cite{zhou2023dnabert}` — DNABERT-2: nguồn gốc các số liệu 4.096 token, FLOPs, tham số, GUE — ✓ EXISTS
- `\cite{wu2021deephage}` — DeePhage: nguồn số liệu 89%, so sánh với PHACTS — ✓ EXISTS
- `\cite{shang2023phatyp}` — PhaTYP: số liệu 92,29% và 91,02% — ✓ EXISTS
- `\cite{ligeti2024prokbert}` — ProkBERT: số liệu 80,68%–85,35% — ✓ EXISTS
- `\cite{dalla2025nucleotide}` — Nucleotide Transformer: cơ sở so sánh "21 lần" — ✓ EXISTS

## Kết quả xác minh số liệu (WebFetch + Full PDF 2026-04-14)

| Số liệu | Kết quả | Chi tiết (nguồn trong paper) |
|---------|---------|------------------------------|
| "4.096 token" | ✓ VERIFIED | Trang 5: "vocabulary size of 2^12 = 4096" |
| "3 lần hiệu quả" | ✓ VERIFIED | Trang 1 (Abstract): "while being 3× more efficient" |
| "một phần ba FLOPs" | ✓ VERIFIED | Trang 9: "requires only one-third the number of FLOPs" |
| "30% tham số nhiều hơn" | ✓ VERIFIED | Trang 9: "Despite having 30% more parameters than DNABERT" |
| "nhỏ hơn 21 lần" (vs NT) | ✓ VERIFIED | Trang 1: "21× fewer parameters" |
| "92 lần thời gian GPU" | ✓ VERIFIED | Trang 1: "approximately 92× less GPU time" |
| "~5 lần giảm độ dài chuỗi" | ✓ VERIFIED | Trang 4: "reduces the sequence length by approximately 5 times" |
| "700bp huấn luyện trước" | ✓ VERIFIED | Trang 10: "pre-trained purely on 700bp-len sequences" |
| "vượt trội ~30% so với PHACTS" | ✓ VERIFIED | DeePhage paper: "nearly 30% higher than PHACTS" |
| **"92,29% độ nhạy, 91,02% độ chính xác" (PhaTYP)** | **✗ MISMATCH** | Bài báo ghi: **sensitivity = 93%, accuracy = 94%** |

### Thay đổi bắt buộc dựa trên kết quả xác minh

**Thay đổi H: Sửa số liệu PhaTYP (Dòng 169) — BẮT BUỘC**

Hiện tại (SAI):
```
PhaTYP đạt hiệu năng mạnh trên contig dài, đặc biệt Nhóm~D (1200--1800~bp) với 92,29\% độ nhạy và 91,02\% độ chính xác.
```

Sau sửa (ĐÚNG theo bài báo):
```
PhaTYP đạt hiệu năng mạnh trên contig dài, đặc biệt Nhóm~D (1200--1800~bp) với 93\% độ nhạy và 94\% độ chính xác.
```

**Thay đổi I: KHÔNG CẦN — Các số liệu DNABERT-2 đã được xác minh ĐÚNG**

Câu dòng 123 giữ nguyên:
```
giúp mô hình hiệu quả hơn 3 lần so với DNABERT trong khi chỉ sử dụng một phần ba số FLOPs mặc dù có nhiều hơn 30\% tham số.

## Thuật ngữ tiếng Việt

- Feature map → bản đồ đặc trưng ✓ (đã dùng đúng dòng 75)
- Kernel → cửa sổ tích chập / kích thước cửa sổ tích chập ✓
- Backbone → mạng nền ✓
- Span prediction → dự đoán đoạn ✓
- Catastrophic forgetting → quên thảm khốc ✓
- Gradual unfreezing → mở khóa dần dần ✓

## Hình/Bảng

Tất cả hình trong chương 2 đã được xác nhận tồn tại trong `figures/`:
- `figures/hierachy_contig.png` — EXISTS
- `figures/neural_network.png` — EXISTS
- `figures/transformer.png` — EXISTS

Bảng `tab:comprehensive_method_comparison` (dòng 190) — cấu trúc đúng, label đúng.

## Ghi chú triển khai

Thứ tự thực hiện đề xuất:
1. **Trước tiên** thực hiện các thay đổi không cần xác minh: A, B, E, F, G (dòng 47/70, 121, 173, thêm intro paragraphs)
2. **Sau đó** WebFetch xác minh các số liệu: dòng 123 ("30% tham số"), dòng 125 ("21 lần", "92 lần"), dòng 167 ("30% DeePhage vs PHACTS"), dòng 169 (PhaTYP nhóm D)
3. **Cuối cùng** thực hiện thay đổi C và D sau khi có kết quả xác minh

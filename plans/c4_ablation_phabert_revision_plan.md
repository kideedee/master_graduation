# Plan: Đổi tên PhaBERT-CNN → PhaBERT + Cập nhật Ablation Study (4 cấu hình)

## Tóm tắt thay đổi

1. **Đổi tên**: PhaBERT-CNN → PhaBERT (toàn bộ thesis)
2. **Ablation study mới**: 4 cấu hình (thay vì 3 cũ), thêm DNABERT-2-CNN và DNABERT-2-AP
3. **PhaBERT giữ nguyên số liệu PhaBERT-CNN gốc** — không thay đổi số
4. **DNABERT-2 Group D sửa**: 88,75/86,99/88,36 (trước: giống Group C 87,68/85,75/87,25)
5. **Kiến trúc**: Giữ nguyên Masked Mean Pooling — Chapter 3 chỉ đổi tên

**ĐƠN GIẢN HÓA**: Section 4.3.2 (main results) và tất cả phân tích so sánh với PhaTYP/DeePhage/ProkBERT CHỈ CẦN ĐỔI TÊN, không sửa số liệu.

---

## Dữ liệu Ablation (CUỐI CÙNG)

| Model | Group A (Sn,Sp,Acc) | Group B (Sn,Sp,Acc) | Group C (Sn,Sp,Acc) | Group D (Sn,Sp,Acc) |
|---|---|---|---|---|
| DNABERT-2 | 83,68 / 73,25 / 81,52 | 87,24 / 79,27 / 85,56 | 87,68 / 85,75 / 87,25 | **88,75 / 86,99 / 88,36** |
| PhaBERT | 82,54 / 81,30 / 82,26 | 88,20 / 84,39 / 87,38 | 90,92 / 86,58 / 90,01 | 92,31 / 87,71 / 91,34 |
| DNABERT-2-CNN | 82,68 / 80,44 / 82,18 | 88,11 / 84,63 / 87,36 | 91,21 / 86,25 / 90,16 | 91,75 / 88,58 / 91,07 |
| DNABERT-2-AP | 85,12 / 77,65 / 83,54 | 89,04 / 84,49 / 87,63 | 90,84 / 86,30 / 89,88 | 91,72 / 88,74 / 91,08 |

> PhaBERT = số liệu PhaBERT-CNN gốc (không thay đổi)
> DNABERT-2 Groups A-C: giữ nguyên; Group D: ĐÃ SỬA
> DNABERT-2-CNN và DNABERT-2-AP: MỚI

---

## Bold Values — Bảng Ablation

| Metric | Group A | Group B | Group C | Group D |
|---|---|---|---|---|
| Sn | **D2-AP** 85,12 | **D2-AP** 89,04 | **D2-CNN** 91,21 | **PhaBERT** 92,31 |
| Sp | **PhaBERT** 81,30 | **D2-CNN** 84,63 | **PhaBERT** 86,58 | **D2-AP** 88,74 |
| Acc | **D2-AP** 83,54 | **D2-AP** 87,63 | **D2-CNN** 90,16 | **PhaBERT** 91,34 |

## Bold Values — Bảng Main Results (KHÔNG ĐỔI, chỉ đổi tên)

PhaBERT-CNN → PhaBERT. Tất cả bold values giữ nguyên.

---

## Số Liệu Tính Toán — CHỈ ABLATION THAY ĐỔI

### PhaBERT vs DNABERT-2 (Acc) — Group D thay đổi do DNABERT-2 sửa
- Nhóm A: 82,26 − 81,52 = **+0,74%** (không đổi)
- Nhóm B: 87,38 − 85,56 = **+1,82%** (không đổi)
- Nhóm C: 90,01 − 87,25 = **+2,76%** (không đổi)
- Nhóm D: 91,34 − 88,36 = **+2,98%** (CŨ: 91,34 − 87,25 = 4,09%)
- Range: **0,74% đến 2,98%** (CŨ: 0,74% đến 4,09%)

### PhaBERT vs DNABERT-2 (Sp)
- Nhóm A: 81,30 − 73,25 = **+8,05%** (không đổi)
- Nhóm B: 84,39 − 79,27 = **+5,12%** (không đổi)
- Nhóm C: 86,58 − 85,75 = **+0,83%** (không đổi)
- Nhóm D: 87,71 − 86,99 = **+0,72%** (CŨ: 87,71 − 85,75 = 1,96%)
- Max: **8,05%** (Nhóm A — không đổi)

### DNABERT-2-CNN vs DNABERT-2 (Acc)
- A: 82,18 − 81,52 = +0,66%
- B: 87,36 − 85,56 = +1,80%
- C: 90,16 − 87,25 = +2,91%
- D: 91,07 − 88,36 = +2,71%

### DNABERT-2-AP vs DNABERT-2 (Acc)
- A: 83,54 − 81,52 = +2,02%
- B: 87,63 − 85,56 = +2,07%
- C: 89,88 − 87,25 = +2,63%
- D: 91,08 − 88,36 = +2,72%

### So sánh với phương pháp tiên tiến — KHÔNG ĐỔI
PhaBERT numbers = old PhaBERT-CNN → tất cả comparisons giữ nguyên:
- vs PhaTYP: 0,32--3,34%
- vs DeePhage: 2,25--4,19%
- vs ProkBERT: 1,58--6,61%
- Tổng: 0,32--6,61%

---

## Thay Đổi Chi Tiết Theo File

### 1. chapters/c3/chapter_3.tex — CHỈ ĐỔI TÊN

Replace all "PhaBERT-CNN" → "PhaBERT" ở dòng: 4, 11, 16, 18, 89, 92, 97, 243

### 2. chapters/c4/chapter_4.tex

#### 2a. Đổi tên toàn file
- "PhaBERT-CNN" → "PhaBERT" (tất cả occurrences)

#### 2b. Section 4.3.1 — VIẾT LẠI ABLATION STUDY

**Đoạn mô tả (thay dòng 25):**
4 cấu hình mới:
1. DNABERT-2: baseline — đầu phân loại tuyến tính đơn giản
2. PhaBERT: mô hình đề xuất đầy đủ (DNABERT-2 + CNN đa kernel + masked mean pooling)
3. DNABERT-2-CNN: chỉ nhánh CNN đa kernel, không có nhánh gộp toàn cục
4. DNABERT-2-AP: attention pooling thay thế mô-đun MKC

Logic so sánh: giống plan cũ

**Bảng tab:ablation_results (thay dòng 27-49):**
4 models × 4 groups × 3 metrics. DNABERT-2 Group D = 88,75/86,99/88,36. Bold theo bảng ở trên.

**Caption bảng:** "Nghiên cứu loại bỏ thành phần: so sánh DNABERT-2, PhaBERT, DNABERT-2-CNN và DNABERT-2-AP trên bốn nhóm độ dài contig"

**Caption hình (dòng 55):** "So sánh hiệu suất của DNABERT-2, PhaBERT, DNABERT-2-CNN và DNABERT-2-AP trên bốn nhóm độ dài contig"

**Đoạn phân tích 1 (thay dòng 59):**
- Cả ba biến thể vượt DNABERT-2 nhất quán
- PhaBERT cải thiện Acc: +0,74% (A), +1,82% (B), +2,76% (C), +2,98% (D) — tăng dần theo độ dài
- Sp cải thiện: +8,05% Nhóm A (73,25→81,30), +5,12% Nhóm B (79,27→84,39)
- Giải thích CNN đa cửa sổ + TextCNN cite

**Đoạn phân tích 2 (thay dòng 61) — VIẾT LẠI:**
So sánh thành phần riêng lẻ:
- D2-AP: Acc cao nhất ở Nhóm A (83,54) và B (87,63) → mạnh trên contig ngắn
- D2-CNN: Acc cao nhất ở Nhóm C (90,16) → mạnh trên contig trung
- PhaBERT: Acc cao nhất ở Nhóm D (91,34), Sp cao nhất ở Nhóm A (81,30) và C (86,58) → cân bằng, mạnh trên contig dài
- Kết hợp hai nhánh (CNN + masked mean pooling) mang lại khả năng tổng quát hóa tốt hơn, đặc biệt trên contig dài
- PhaBERT đạt Sn vượt trội ở Nhóm D (92,31) so với D2-CNN (91,75) và D2-AP (91,72)

#### 2c. Section 4.3.2 — CHỈ ĐỔI TÊN
- "PhaBERT-CNN" → "PhaBERT" (tất cả)
- Tất cả số liệu GIỮ NGUYÊN

#### 2d. Section 4.4 (Thảo luận)

**4.4.1 (dòng 121):** "PhaBERT-CNN" → "PhaBERT"

**4.4.2 (dòng 126):**
Cũ: "cải thiện từ 0,74% ở Nhóm A (từ 81,52% lên 82,26%) đến 4,09% ở Nhóm D (từ 87,25% lên 91,34%)"
Mới: "cải thiện từ 0,74% ở Nhóm A (từ 81,52% lên 82,26%) đến 2,98% ở Nhóm D (từ 88,36% lên 91,34%)"
"PhaBERT-CNN" → "PhaBERT"

**4.4.3 (dòng 133):** "PhaBERT-CNN" → "PhaBERT"

#### 2e. Section 4.5 (Kết luận chapter 4) — Cập nhật

- "PhaBERT-CNN" → "PhaBERT"
- "ba cấu hình" → "bốn cấu hình"
- "biến thể PhaBERT-CNN-AP" → "DNABERT-2-CNN và DNABERT-2-AP"
- "0,74% đến 4,09%" → "0,74% đến 2,98%"
- "8,05%" → giữ nguyên (Group A không đổi)
- Viết lại kết luận ablation: không còn so sánh masked mean vs attention pooling
- "82,26% đến 91,34%" → giữ nguyên
- "0,32 đến 6,61%" → giữ nguyên

### 3. chapters/c1/chapter_1.tex — CHỈ ĐỔI TÊN

- Tất cả "PhaBERT-CNN" → "PhaBERT"
- Số liệu 82,26--91,34% và 0,32--6,61%: GIỮ NGUYÊN

### 4. chapters/c5/chapter_5.tex

- Tất cả "PhaBERT-CNN" → "PhaBERT"
- Dòng 11: số liệu Acc và so sánh: GIỮ NGUYÊN
- Dòng 20:
  - "ba cấu hình" → "bốn cấu hình"
  - "đường cơ sở DNABERT-2, PhaBERT-CNN-AP (gộp chú ý) và PhaBERT-CNN (gộp trung bình có mặt nạ)" → "DNABERT-2, PhaBERT, DNABERT-2-CNN và DNABERT-2-AP"
  - "0,74% đến 4,09%" → "0,74% đến 2,98%"
  - "8,05%" → giữ nguyên
  - Viết lại câu so sánh chiến lược gộp → mô tả kết quả ablation mới
  - "0,32--6,61%" → giữ nguyên
- Dòng 29: "87,71%" → giữ nguyên (PhaBERT Sp Nhóm D không đổi)

### 5. chapters/abtract_vi.tex — SỬA ĐOẠN 2 + 3

**Đoạn 2 (dòng 10):**
Cũ: "PhaBERT-CNN... mạng nơ-ron tích chập đa kernel và cơ chế attention pooling"
Mới: "PhaBERT... mô-đun MKC gồm nhánh CNN đa kernel và gộp trung bình có mặt nạ toàn cục"
Bỏ "áp dụng self-attention để tập trung vào các vùng genome có tính thông tin cao"

**Đoạn 3 (dòng 12):**
Cũ: "accuracy 81.59%, 87.91%, 90.01%, và 90.69%... cải thiện 0.91-5.98%"
Mới: "accuracy 82,26%, 87,38%, 90,01% và 91,34%... cải thiện 0,32--6,61%"
Cũ: "sensitivity (82.00%-91.12%) và specificity (80.15%-90.95%)"
Mới: "sensitivity (82,54%--92,31%) và specificity (81,30%--87,71%)"

> LƯU Ý: Abstract hiện có SỐ SAI (dùng PhaBERT-CNN-AP numbers). Sửa thành PhaBERT-CNN gốc = PhaBERT.

### 6. chapters/abtract_en.tex — SỬA ĐOẠN 2 + 3

**Đoạn 2 (dòng 10):**
Cũ: "PhaBERT-CNN... multi-scale CNNs and attention pooling mechanism"
Mới: "PhaBERT... multi-kernel CNNs and masked mean pooling"
Bỏ "applies self-attention mechanism..."

**Đoạn 3 (dòng 12):**
Cũ: "accuracies of 81.59%, 87.91%, 90.01%, and 90.69%... improving 0.91-5.98%"
Mới: "accuracies of 82.26%, 87.38%, 90.01%, and 91.34%... improving 0.32--6.61%"
Cũ: "sensitivity (82.00%-91.12%) and specificity (80.15%-90.95%)"
Mới: "sensitivity (82.54%--92.31%) and specificity (81.30%--87.71%)"

### 7. chapters/glossary.tex

Dòng 49: `PhaBERT-CNN | Phage BERT - Convolutional Neural Network | Mô hình PhaBERT-CNN`
→ `PhaBERT | Phage BERT | Mô hình PhaBERT`

---

## Mô Tả Ablation Study Mới (Section 4.3.1)

### 4 cấu hình:
1. **DNABERT-2**: Baseline
2. **PhaBERT**: Đầy đủ = DNABERT-2 + CNN đa kernel + masked mean pooling
3. **DNABERT-2-CNN**: Chỉ CNN đa kernel
4. **DNABERT-2-AP**: Chỉ attention pooling

### Phát hiện chính:
1. **MKC tổng thể**: PhaBERT vượt DNABERT-2 Acc +0,74% đến +2,98%, tăng dần theo độ dài
2. **Sp cải thiện đặc biệt**: +8,05% Nhóm A
3. **Từng thành phần riêng**: D2-AP mạnh trên contig ngắn (A, B); D2-CNN mạnh trên contig trung (C); PhaBERT mạnh nhất trên contig dài (D)
4. **Giá trị kết hợp**: PhaBERT đạt Sp cao nhất (ablation) ở A và C → kết hợp hai nhánh cải thiện nhận diện phage ôn hòa

---

## Citations — Không cần thêm mới

---

## Thứ Tự Thực Hiện

1. chapters/c3/chapter_3.tex — Đổi tên
2. chapters/c4/chapter_4.tex — Ablation mới + đổi tên
3. chapters/c5/chapter_5.tex — Đổi tên + ablation summary
4. chapters/c1/chapter_1.tex — Đổi tên
5. chapters/abtract_vi.tex — Sửa đoạn 2+3
6. chapters/abtract_en.tex — Sửa đoạn 2+3
7. chapters/glossary.tex — Entry 41

---

## LƯU Ý

1. **Hình cần tạo lại**: `figures/dnabert2_vs_phabertcnn.png` (4 models) và `figures/primary_contig_exp.png` (tên PhaBERT)
2. **Section 4.3.2**: CHỈ đổi tên, KHÔNG sửa số
3. **Abstracts**: Sửa cả tên LẪN số (đang có số sai từ PhaBERT-CNN-AP)
4. **DNABERT-2 ablation**: Only Group D changes (88,75/86,99/88,36)

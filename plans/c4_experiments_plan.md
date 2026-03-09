# Plan: Chapter 4 — Thực nghiệm và Đánh giá

## Yêu cầu viết lại
- Văn phong tương tự Chương 3: đoạn văn xuôi liền mạch, ít subsection
- Không lặp lại nội dung đã có ở Chương 3 (xây dựng dữ liệu, kiến trúc, chiến lược huấn luyện)
- Tham chiếu về Chương 3 thay vì mô tả lại

---

## Outline

### I. Mở đầu chương (1 đoạn)
- Giới thiệu mục tiêu chương: đánh giá PhaBERT-CNN trên 4 nhóm độ dài contig
- Tham chiếu Chương 3 cho chi tiết phương pháp và dữ liệu
- Nêu cấu trúc chương

### II. Môi trường thực nghiệm (1 section, không chia subsection)
**Đoạn 1 — Phần cứng và phần mềm:**
- GPU NVIDIA RTX 5070Ti, CPU Intel i5 13500, 64GB RAM (từ Chapter 3)
- Python, PyTorch, Transformers

**Đoạn 2 — Các phương pháp so sánh:**
- DNABERT-2 baseline (dense head đơn giản)
- PhaTYP: BERT + protein features, phụ thuộc Prodigal
- DeePhage: CNN trên one-hot encoding
- ProkBERT: BERT tiền huấn luyện trên prokaryotic genomes
- Lý do loại DeepPL: giới hạn 512 bp của DNABERT

**Đoạn 3 — Chỉ số đánh giá:**
- Sensitivity (sn), Specificity (sp), Accuracy (acc)
- Công thức và ý nghĩa từng chỉ số
- Lý do dùng 3 chỉ số này (nhất quán với các nghiên cứu trước)

### III. Kết quả thực nghiệm (1 section)
**Đoạn 1 — So sánh PhaBERT-CNN vs DNABERT-2:**
- Bảng/hình dnabert2_vs_phabertcnn.png
- Phân tích: Group A (accuracy tương đương nhưng specificity cải thiện 6.90%), Groups B-C (cải thiện 2.35-2.76%), Group D (cải thiện 3.43%)
- Kết luận: CNN component bổ sung hiệu quả cho transformer

**Đoạn 2 — Bảng so sánh tổng thể (Table chính):**
- Bảng 3 chỉ số (sn, sp, acc) × 4 phương pháp × 4 nhóm
- Dùng số liệu từ paper gốc

**Đoạn 3 — Phân tích kết quả:**
- PhaBERT-CNN tốt nhất Groups A, B, C (acc 81.59%, 87.91%, 90.01%)
- PhaTYP tốt nhất Group D (acc 91.02%), PhaBERT-CNN đạt 90.69% (kém 0.34%)
- DeePhage: moderate, 78.07%-89.09%
- ProkBERT: stagnation ở Group C-D (84.03%-84.73%)
- Hình primary_contig_exp.png

### IV. Phân tích và thảo luận (1 section)
**Đoạn 1 — Ưu điểm PhaBERT-CNN:**
- Không phụ thuộc gene prediction → hiệu quả trên contig ngắn
- Pre-trained genomic knowledge → tổng quát hóa tốt hơn DeePhage
- Multi-scale CNN → nắm bắt đặc trưng đa tỷ lệ

**Đoạn 2 — Hạn chế:**
- Group D: PhaTYP tốt hơn nhờ protein features từ ORF hoàn chỉnh
- Thời gian inference chậm hơn DeePhage (117M parameters)
- Random undersampling có thể mất thông tin

**Đoạn 3 — Ablation study (DNABERT-2 baseline vs PhaBERT-CNN):**
- Bảng so sánh DNABERT-2 vs PhaBERT-CNN chi tiết (sn, sp, acc)
- Phân tích đóng góp của CNN + attention pooling

### V. Kết luận chương (1 đoạn)
- Tóm tắt kết quả chính
- Dẫn sang Chương 5

---

## Citation List

| Key | Lý do |
|-----|-------|
| wu2021deephage | Baseline DeePhage, nguồn dữ liệu |
| shang2023phatyp | Baseline PhaTYP |
| ligeti2024prokbert | Baseline ProkBERT |
| zhou2023dnabert | DNABERT-2 baseline |
| zhang2024deeppl | Nguồn dữ liệu, lý do loại DeepPL |
| hyatt2010prodigal | Prodigal dependency của PhaTYP |

---

## Numbers to Verify (từ phabert_cnn.tex)

### PhaBERT-CNN
| Group | sn | sp | acc |
|-------|----|----|-----|
| A (100-400 bp) | 82.00% | 80.15% | 81.59% |
| B (400-800 bp) | 89.91% | 80.44% | 87.91% |
| C (800-1200 bp) | 91.12% | 85.93% | 90.01% |
| D (1200-1800 bp) | 88.47% | 90.95% | 90.69% |

### PhaTYP
| Group | sn | sp | acc |
|-------|----|----|-----|
| A | 79.07% | 78.77% | 78.92% |
| B | 86.74% | 85.06% | 85.90% |
| C | 90.09% | 87.65% | 88.87% |
| D | 92.29% | 89.75% | 91.02% |

### DeePhage
| Group | sn | sp | acc |
|-------|----|----|-----|
| A | 80.09% | 71.79% | 78.07% |
| B | 86.46% | 77.18% | 84.17% |
| C | 89.17% | 80.13% | 87.40% |
| D | 91.17% | 80.84% | 89.09% |

### ProkBERT
| Group | sn | sp | acc |
|-------|----|----|-----|
| A | 80.65% | 80.80% | 80.68% |
| B | 85.67% | 84.15% | 85.35% |
| C | 83.61% | 85.72% | 84.03% |
| D | 85.00% | 83.68% | 84.73% |

### DNABERT-2 (từ phân tích trong paper)
| Group | acc | sp (nếu có) |
|-------|-----|-------------|
| A | 81.52% | 73.25% |
| B | 85.56% (87.91-2.35) | — |
| C | 87.25% (90.01-2.76) | — |
| D | 87.26% (90.69-3.43) | 85.75% (90.95-5.20) |

### Cải thiện PhaBERT-CNN so với các baseline
- vs PhaTYP: 0.91-2.67% (Groups A-C)
- vs DeePhage: 2.17-3.24% (Groups A-C) — từ abstract: "2.17-3.24%"
- vs ProkBERT: 0.91-5.98% (Groups A-C) — từ abstract: "0.91-5.98%"
- Group D: PhaBERT-CNN kém PhaTYP 0.34% (91.02-90.69)
- Group D: PhaBERT-CNN hơn DeePhage 1.60% (90.69-89.09)
- Group D: PhaBERT-CNN hơn ProkBERT 5.96% (90.69-84.73)

---

## Nội dung KHÔNG viết lại (đã có ở Chương 3)
- Xây dựng tập dữ liệu (nguồn, số lượng genome, sliding window, augmentation, undersampling)
- Kiến trúc PhaBERT-CNN
- Chiến lược huấn luyện hai giai đoạn
- Bảng tham số sliding window
- Bảng siêu tham số
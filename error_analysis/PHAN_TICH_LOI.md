# Phân tích lỗi mô hình PhaBERT (Transfer Learning) — Giải thích chỉ số & Bình luận số liệu

> Tài liệu này giải thích **ý nghĩa từng chỉ số** trong bộ kết quả phân tích lỗi (`error_analysis/`) và **bình luận trên
số liệu thực tế** đã chạy được.
> Mô hình: DNABERT‑2 + CNN (lớp `PhaBERT`), phân loại **nhãn lối sống của thực khuẩn thể (phage)** từ contig DNA.
> Dữ liệu: 20 mô hình (5‑fold CV × 4 nhóm độ dài), inference lại trên tập validation của từng fold.

---

## 0. Bối cảnh & quy ước

| Khái niệm                     | Giá trị                                                                | Ghi chú                                               |
|-------------------------------|------------------------------------------------------------------------|-------------------------------------------------------|
| **Nhãn lớp**                  | `0 = temperate` (ôn hòa / lysogenic), `1 = virulent` (độc lực / lytic) | Xác minh tại `embedding_sequence/create_contig.py:39` |
| **Lớp dương tính (positive)** | `1 = virulent`                                                         | precision/recall/F1 tính cho lớp này                  |
| **Nhóm độ dài (bp)**          | `100_400`, `400_800`, `800_1200`, `1200_1800`                          | Đúng convention DeePhage/PhaTYP                       |
| **id bản ghi**                | chỉ số dòng trong tập val (thứ tự cố định, `shuffle=False`)            | Dùng để truy ngược về chuỗi gốc                       |
| **GC%**                       | `100 × (G+C) / (A+C+G+T)`                                              | Loại base mơ hồ (N…) khỏi mẫu số                      |

### Hai cách gộp 5 fold (rất quan trọng khi đọc số)

```
┌─ HEADLINE (báo cáo hiệu năng) ──────────────────────────────┐
│ Tính metric RIÊNG từng fold → lấy mean ± std qua 5 fold.    │
│ → file: headline_per_group_meanstd.csv                      │
│ → ít bị lệch do kích thước fold, dùng để "báo cáo con số".  │
├─ SLICING (phân tích lỗi) ───────────────────────────────────┤
│ GỘP (pool) toàn bộ prediction trong nhóm rồi mới cắt lát.   │
│ → mọi file slice_*, calibration_*, threshold_*, confidence_*│
│ → mỗi mẫu cần 1 prediction để gán vào lát cắt GC/length.    │
│ ⚠️ Đây là số MÔ TẢ hành vi model, KHÔNG phải ước lượng      │
│    sai số tổng quát (generalization).                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 1. Các chỉ số nền tảng (định nghĩa)

Với mỗi lát cắt, từ ma trận nhầm lẫn (confusion matrix):

```
                 Dự đoán
               temperate(0)   virulent(1)
Thực temperate(0)   TN            FP
Thực virulent(1)    FN            TP
```

| Chỉ số                                | Công thức                       | Ý nghĩa                                                                                 |
|---------------------------------------|---------------------------------|-----------------------------------------------------------------------------------------|
| **error_rate**                        | `(FP+FN) / n`                   | Tỉ lệ đoán sai. = `1 − accuracy`. **Trục chính của phân tích lỗi.**                     |
| **accuracy**                          | `(TP+TN) / n`                   | Tỉ lệ đoán đúng                                                                         |
| **FPR** (False Positive Rate)         | `FP / (FP+TN)`                  | Tỉ lệ **temperate bị nhầm thành virulent** = lỗi trên lớp temperate                     |
| **FNR** (False Negative Rate)         | `FN / (FN+TP)`                  | Tỉ lệ **virulent bị nhầm thành temperate** = lỗi trên lớp virulent                      |
| **precision**                         | `TP / (TP+FP)`                  | Trong các ca đoán "virulent", bao nhiêu % đúng                                          |
| **recall** (= sensitivity)            | `TP / (TP+FN)`                  | Trong các virulent thật, bắt được bao nhiêu %                                           |
| **specificity**                       | `TN / (TN+FP)` = `1 − FPR`      | Recall của lớp temperate                                                                |
| **F1**                                | `2·P·R / (P+R)`                 | Trung bình điều hòa precision & recall (lớp virulent)                                   |
| **ROC‑AUC**                           | diện tích dưới đường ROC        | Khả năng phân tách 2 lớp theo xác suất, **độc lập ngưỡng** (0.5=ngẫu nhiên, 1=hoàn hảo) |
| **Wilson 95% CI** (`err_ci_low/high`) | khoảng tin cậy Wilson cho tỉ lệ | Sai số của `error_rate`; bin càng ít mẫu → khoảng càng rộng                             |
| **suppressed**                        | `n < 30`                        | Cờ cảnh báo bin quá ít mẫu, số liệu không đáng tin                                      |

> **Vì sao cần cả FPR và FNR?** Một mô hình có thể "giỏi tổng thể" nhưng lệch: sai chủ yếu ở 1 lớp. Tách FPR/FNR cho
> thấy lỗi rơi vào temperate hay virulent.

---

## 2. Hiệu năng theo nhóm độ dài — `headline_per_group_meanstd.csv` & `slice_overall_by_group.csv`

| group     | accuracy (mean±std) | error_rate (pooled) | ROC‑AUC |
|-----------|---------------------|---------------------|---------|
| 100_400   | 0.820 ± 0.012       | **0.180**           | 0.894   |
| 400_800   | 0.873 ± 0.010       | 0.127               | 0.931   |
| 800_1200  | 0.899 ± 0.008       | 0.101               | 0.945   |
| 1200_1800 | 0.914 ± 0.008       | **0.086**           | 0.951   |

**Bình luận:**

- **Quan hệ đơn điệu rõ ràng**: contig càng dài → lỗi càng giảm (0.180 → 0.086, tức giảm hơn **một nửa**). Hợp với sinh
  học: chuỗi dài chứa nhiều "tín hiệu" (gene tích hợp, motif…) để model bám vào.
- **std giữa 5 fold rất nhỏ (~0.01)** → kết quả ổn định, không phải may rủi do chia fold. Đây là tín hiệu tốt về độ tin
  cậy.
- Khớp xu hướng của các công cụ cùng loại (DeePhage, PhaTYP): nhóm 100–400 bp luôn là điểm yếu cố hữu.

---

## 3. Lỗi theo lớp nhãn — `slice_by_group_class.csv`

Với mỗi nhóm, tách theo nhãn thật. Vì các dòng chỉ thuộc 1 lớp nên `error_rate` của:

- hàng `temperate(0)` = **FPR** (temperate bị nhầm thành virulent)
- hàng `virulent(1)` = **FNR** (virulent bị nhầm thành temperate)

| group     | err temperate (FPR) | err virulent (FNR) | n temperate | n virulent |
|-----------|---------------------|--------------------|-------------|------------|
| 100_400   | 0.182               | 0.179              | 291k        | 1,101k     |
| 400_800   | 0.156               | 0.119              | 121k        | 458k       |
| 800_1200  | 0.131               | 0.093              | 81k         | 308k       |
| 1200_1800 | **0.124**           | **0.076**          | 61k         | 234k       |

**Bình luận:**

- **Mất cân bằng lớp nặng**: virulent chiếm ~79% (100_400). Model học thiên về lớp đa số → **temperate (thiểu số) luôn
  là lớp yếu hơn**.
- Khoảng cách 2 lớp **nới rộng theo độ dài**: ở 1200_1800, lỗi temperate (0.124) gần **gấp đôi** lỗi virulent (0.076).
  Nghĩa là khi có contig dài, lỗi còn lại **dồn vào việc nhầm temperate → virulent**.
- Hệ quả thực tế: nếu bài toán quan tâm phát hiện **temperate**, cần lưu ý mô hình đang bỏ sót nhóm này nhiều hơn.

---

## 4. Lỗi theo GC content — `slice_by_gc_bin.csv` (phát hiện mới)

Bin GC cố định theo sinh học: `<35 / 35–45 / 45–55 / >55` (%).

| GC bin | error_rate (ALL) | error_rate 100_400 |
|--------|------------------|--------------------|
| <35    | 0.192            | 0.230              |
| 35–45  | 0.109            | 0.139              |
| 45–55  | **0.106**        | **0.132**          |
| >55    | **0.248**        | **0.289**          |

**Bình luận:**

- **Quan hệ hình chữ U**: model mạnh ở **GC trung bình (35–55%)**, yếu hẳn ở **2 cực**, đặc biệt **GC cao (>55%)** — lỗi
  tới 24.8% (toàn cục) và 28.9% ở contig ngắn.
- Mẫu hình này **đúng ở cả 4 nhóm độ dài** → là đặc tính của model, không phải nhiễu.
- **Ý nghĩa đóng góp**: các công cụ phage hiện hành (DeePhage/PhaTYP/PhaMer…) **chưa báo cáo lỗi theo GC** → đây là một
  góc phân tích mới, có thể đưa vào luận văn như một hạn chế chưa từng được chỉ ra.
- *Lưu ý kỹ thuật*: ở contig ngắn (100–400 bp), ước lượng GC có sai số lấy mẫu lớn (±5% ở 100 bp) → bin GC cực trị ở
  nhóm ngắn cần diễn giải thận trọng.

---

## 5. Lỗi theo độ dài chi tiết — `slice_by_length_bin.csv`

Bin phụ rộng 100 bp trong từng nhóm. Ví dụ nhóm 100_400:

| bin (bp) | error_rate |
|----------|------------|
| 100      | 0.213      |
| 200      | 0.177      |
| 300      | 0.158      |
| 400      | 0.154      |

**Bình luận:** đơn điệu giảm ngay cả trong nội bộ một nhóm → khẳng định lại "ngắn = khó". Các bin biên (vd 400, 800,
1200, 1800) thường ít mẫu (xem cột `n`/`suppressed`) nên độ rộng CI lớn, đọc cẩn thận.

---

## 6. Hiệu chuẩn xác suất (Calibration) — `calibration_metrics.csv`

| Chỉ số                               | Công thức / ý nghĩa                                                                                                                        |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| **ECE** (Expected Calibration Error) | Trung bình có trọng số `\|độ chính xác thực tế − độ tự tin\|` trên 10 bin xác suất. **0 = hiệu chuẩn hoàn hảo**; >0.05–0.10 = lệch đáng kể |
| **Brier**                            | MSE giữa xác suất dự đoán và nhãn 0/1. Càng thấp càng tốt                                                                                  |
| **Brier baseline**                   | `p(1−p)` với `p` = tỉ lệ lớp dương. Mốc của model "đoán bừa theo tần suất"                                                                 |
| **Brier skill score**                | `1 − Brier/baseline`. >0 = tốt hơn đoán bừa; càng gần 1 càng tốt                                                                           |

| group     | ECE       | Brier skill |
|-----------|-----------|-------------|
| 100_400   | **0.138** | 0.10        |
| 400_800   | 0.108     | 0.31        |
| 800_1200  | 0.092     | 0.42        |
| 1200_1800 | **0.082** | 0.50        |

**Bình luận:**

- ECE > 0.08 ở **mọi** nhóm → mô hình **tự tin quá mức (overconfident)**, tệ nhất ở contig ngắn (0.138).
- Brier skill chỉ 0.10 ở nhóm 100_400 → trên contig ngắn, lợi thế so với baseline "đoán theo tần suất" rất mỏng.
- Xem chi tiết overconfidence ở mục 8 (gây bất ngờ).

---

## 7. Quét ngưỡng quyết định — `threshold_sweep.csv` & `youden_optimal_threshold.csv`

- **threshold_sweep**: với mỗi ngưỡng 0.30→0.70, tính FPR/FNR/F1/balanced_accuracy. Cho thấy đánh đổi: nâng ngưỡng →
  giảm FPR nhưng tăng FNR.
- **Youden‑J** = `sensitivity + specificity − 1`, tìm ngưỡng cân bằng nhất 2 loại lỗi.

| group     | ngưỡng tối ưu (Youden) | sensitivity | specificity |
|-----------|------------------------|-------------|-------------|
| 100_400   | 0.579                  | 0.808       | 0.831       |
| 400_800   | 0.766                  | 0.864       | 0.865       |
| 800_1200  | 0.924                  | 0.891       | 0.890       |
| 1200_1800 | **0.994**              | 0.902       | 0.904       |

**Bình luận:**

- Ngưỡng tối ưu **trôi từ 0.58 lên 0.99** theo độ dài — bất thường. Nguyên nhân: với contig dài, điểm số của model **bão
  hòa sát 1** (đa số đẩy về virulent), nên muốn cân bằng phải cắt ở ngưỡng rất cao.
- Gợi ý: nếu triển khai thực tế, **không nên dùng cứng ngưỡng 0.5**; nên hiệu chỉnh ngưỡng theo từng nhóm độ dài.

---

## 8. Mức độ "sai mà tự tin" — `confidence_summary.csv` & `confidence_by_group_gc.csv`

`confidence` của một dự đoán = `max(prob_class_0, prob_class_1)`. **confident‑wrong** = dự đoán sai **và** confidence >
0.85.

| group     | % lỗi là confident‑wrong | conf khi SAI | conf khi ĐÚNG |
|-----------|--------------------------|--------------|---------------|
| 100_400   | 64.7%                    | 0.866        | 0.950         |
| 400_800   | 81.0%                    | 0.925        | 0.984         |
| 800_1200  | 89.9%                    | 0.958        | 0.994         |
| 1200_1800 | **92.8%**                | **0.970**    | 0.997         |
| **ALL**   | **72.2%**                | 0.893        | 0.970         |

**Bình luận (điểm cảnh báo quan trọng nhất):**

- **Nghịch lý overconfidence**: nhóm dài tuy **ít lỗi nhất** nhưng khi sai thì **92.8% là sai với độ tự tin > 0.85** (
  trung bình 0.97 — gần như "chắc chắn mà sai").
- Toàn cục: **72% mọi lỗi đều là lỗi tự tin** → **không thể dùng ngưỡng xác suất cao để lọc bỏ ca sai**. Đây là hạn chế
  nghiêm trọng cho ứng dụng thực tế (người dùng dễ tin nhầm các dự đoán "chắc nịch").
- Theo GC (`confidence_by_group_gc.csv`): tỉ lệ confident‑wrong trên tổng (`frac_confwrong_of_all`) cao nhất ở **2 cực
  GC** — vd 100_400: GC>55 = 17.4%, GC<35 = 15.6% so với ~8.5–9.2% ở giữa. GC cực trị **vừa nhiều lỗi, vừa sai tự tin**.
- `confident_wrong.csv` liệt kê từng ca (kèm `true_class`, `pred_class`, `length`, `gc`) để soi tay — nhiều ca có
  `prob_wrong = 1.0`.

---

## 9. Bảng tra file đầu ra

### `tables/`

| File                             | Nội dung                                                |
|----------------------------------|---------------------------------------------------------|
| `headline_per_group_meanstd.csv` | Hiệu năng mean±std qua 5 fold, theo nhóm                |
| `slice_overall_by_group.csv`     | Metric đầy đủ theo nhóm (pooled) + dòng `ALL`           |
| `slice_by_group_class.csv`       | Tách theo lớp temperate/virulent                        |
| `slice_by_gc_bin.csv`            | Theo nhóm × GC bin (chính là lưới 2D length×GC dạng số) |
| `slice_by_gc_bin_class.csv`      | Theo nhóm × GC bin × lớp                                |
| `slice_by_length_bin.csv`        | Theo nhóm × bin độ dài 100 bp                           |
| `calibration_metrics.csv`        | ECE, Brier, Brier skill theo nhóm                       |
| `threshold_sweep.csv`            | FPR/FNR/F1/balanced_acc theo ngưỡng 0.3→0.7             |
| `youden_optimal_threshold.csv`   | Ngưỡng tối ưu Youden‑J theo nhóm                        |
| `confidence_summary.csv`         | Mức overconfidence theo nhóm                            |
| `confidence_by_group_gc.csv`     | Overconfidence theo nhóm × GC bin                       |
| `confident_wrong.csv`            | Danh sách ca sai mà tự tin (prob>0.85)                  |

### `figures/`

| File                            | Đọc gì                                                                               |
|---------------------------------|--------------------------------------------------------------------------------------|
| `error_rate_by_group.png`       | Cột error rate ± Wilson CI theo nhóm độ dài                                          |
| `error_rate_by_gc_bin.png`      | Error rate theo GC bin, tách temperate/virulent (4 nhóm)                             |
| `confusion_matrix_by_group.png` | 4 ma trận nhầm lẫn (nhãn temperate/virulent)                                         |
| `heatmap_lengthxGC.png`         | Heatmap 2D error rate (nhóm × GC); ô gạch chéo = <30 mẫu                             |
| `scatter_lengthxGC.png`         | Phân bố từng contig (length×GC), tô màu đúng/sai — lỗi tụ ở GC cực trị & contig ngắn |
| `reliability_by_group.png`      | Đường tin cậy (calibration) + histogram xác suất, kèm ECE                            |

### gốc

| File                         | Nội dung                                                               |
|------------------------------|------------------------------------------------------------------------|
| `master_predictions.parquet` | Toàn bộ bản ghi đã ghép length/GC/bin — tái dùng cho phân tích sâu hơn |

---

## 10. Kết luận tổng hợp & lưu ý

**Bức tranh tổng thể về model PhaBERT:**

1. ✅ **Mạnh** ở contig **dài** + GC **trung bình (35–55%)**.
2. ⚠️ **Yếu** ở contig **ngắn (100–400 bp)** và GC **cực trị** (đặc biệt >55%).
3. ⚠️ **Thiên về virulent** (lớp đa số) → **temperate là lớp yếu hơn**, nhất là ở contig dài.
4. 🚨 **Tự tin quá mức**: 72% lỗi là lỗi "chắc nịch" (prob>0.85), càng tệ ở contig dài → **không dùng được prob để lọc
   lỗi**.

**Lưu ý khi trích dẫn số liệu:**

- Số "slicing" là **mô tả hành vi** trên dữ liệu hiện có, không phải ước lượng generalization (xem mục 0). Dùng
  `headline_*` (mean±std) khi cần báo cáo con số hiệu năng.
- Bin có `suppressed = True` (n<30) → bỏ qua hoặc gộp khi diễn giải.
- GC ở contig ngắn có sai số ước lượng lớn → thận trọng với các bin GC cực trị ở nhóm 100–400.

**Hướng đề xuất (nếu cải thiện model):** xử lý mất cân bằng lớp (class weight / focal loss), hiệu chỉnh xác suất hậu
kỳ (Platt/temperature scaling — vì ECE cao), và tăng cường dữ liệu ở vùng GC cực trị.

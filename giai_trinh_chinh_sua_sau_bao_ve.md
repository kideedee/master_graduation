# Giải trình chỉnh sửa luận văn sau bảo vệ

**Đề tài:** Phân loại hệ gen thực khuẩn dựa trên phương pháp học sâu
**Học viên:** Vũ Quang Sơn · Ngành: Khoa học máy tính, mã số 8480101
**Đơn vị:** Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội (VNU-UET)
**Cán bộ hướng dẫn:** TS. Diệp Thị Hoàng

**Hội đồng chấm luận văn** (QĐ thành lập số 1086/QĐ-ĐHCN ngày 22/5/2026):
- Chủ tịch: TS. Nguyễn Việt Anh
- Phản biện 1 (PB1): TS. Trần Quốc Long
- Phản biện 2 (PB2): TS. Hà Mạnh Hùng
- Thư ký: ThS. Nghiêm Nguyễn Việt Dung

**Buổi bảo vệ:** 8h00 ngày 30/05/2026, phòng 210-E3, Trường ĐHCN-ĐHQGHN.

---

## Chú thích trạng thái

| Ký hiệu | Ý nghĩa |
|---|---|
| ✅ | Đã chỉnh sửa trong luận văn |
| 🔄 | Đã chỉnh sửa một phần trong luận văn, phần còn lại đưa vào hướng phát triển |
| 📝 | Đã nêu thành hạn chế trong luận văn / giải trình bằng văn bản (hướng phát triển) |

---

## Bảng tổng hợp trạng thái

| # | Nguồn | Nội dung góp ý | Trạng thái |
|---|---|---|---|
| A1 | PB1 | Làm rõ chia 5-fold ở mức hệ gen hay contig; chống rò rỉ thông tin train/val | ✅ |
| A2 | PB1 | Báo cáo độ lệch chuẩn / khoảng tin cậy / kiểm định thống kê sau 5-fold | ✅ |
| A3 | PB1 | Làm rõ baseline nào chạy lại, baseline nào lấy từ công bố | ✅ |
| A4 | PB1 | Đánh giá trên dữ liệu độc lập / chia theo cụm tương đồng | 📝 |
| A5 | PB1 | Phân tích lỗi theo độ dài / lớp nhãn / họ phage / vật chủ / GC | 🔄 |
| A6 | PB1 | Sửa lỗi trình bày, trích dẫn, thống nhất tên mô hình | ✅ |
| A7 | PB1 | Làm rõ "phân loại hệ gen thực khuẩn" là phân loại lối sống, không phải taxonomy | ✅ |
| B2 | PB2 | Chưa giải thích ý nghĩa sinh học của kết quả | 🔄 |
| B3 | PB2 | Chưa chứng minh khả năng tổng quát hóa trên dữ liệu độc lập | 📝 |
| B4 | PB2 | Chưa so sánh với các mô hình lớn (Nucleotide Transformer, DNA Transformer) | 📝 |
| C1 | Quyết nghị HĐ | Cập nhật/hạn chế trích dẫn tài liệu cũ | ✅ |

---

## Phần A — Phản biện 1: TS. Trần Quốc Long

### A1. Làm rõ cách chia 5-fold (mức hệ gen vs mức contig) ✅

**Góp ý:** Cần làm rõ việc chia 5-fold thực hiện ở mức hệ gen hay mức contig, vì các contig sinh từ cửa sổ trượt chồng lấn (kể cả reverse complement) có thể lọt vào cả tập huấn luyện lẫn tập kiểm định, gây rò rỉ thông tin và thổi phồng kết quả.

**Cách xử lý:** Tái cấu trúc phần *Thu thập dữ liệu và tiền xử lý* thành hai giai đoạn rõ ràng: (1) chia dữ liệu 5-fold phân tầng ở mức hệ gen, thực hiện trước toàn bộ bước tiền xử lý, mỗi hệ gen chỉ thuộc tập huấn luyện hoặc kiểm định của một fold; (2) pipeline tiền xử lý (tạo contig → tăng cường → undersampling chỉ trên tập huấn luyện → BPE) áp dụng độc lập cho từng fold. Bổ sung lập luận chống rò rỉ thông tin giữa train/val, phân biệt với khái niệm rò rỉ k-mer đã bàn ở Chương 2.

**Vị trí:** Chương 3 (mục Thu thập dữ liệu và tiền xử lý); Hình `fig:data_preparation`; Bảng `tab:dataset_statistics` (cột Huấn luyện cân bằng 1:1, cột Kiểm định giữ phân bố gốc — minh chứng undersampling chỉ trên train, sau khi đã chia fold).

> Lưu ý: ảnh `figures/data_preparation.png` cần vẽ lại để bổ sung khối "chia 5-fold mức hệ gen" ở đầu pipeline (đã đặt comment nhắc trong file `.tex`).

---

### A2. Độ lệch chuẩn / khoảng tin cậy / kiểm định thống kê ✅

**Góp ý:** Sau kiểm định chéo 5-fold cần báo cáo độ lệch chuẩn, khoảng tin cậy hoặc kiểm định thống kê để thể hiện độ tin cậy của kết quả.

**Cách xử lý:** Bổ sung **độ lệch chuẩn** giữa 5 phần vào toàn bộ bảng kết quả: mỗi ô số liệu (Sn, Sp, Acc) được trình bày dạng *trung bình ± độ lệch chuẩn* (ví dụ độ chính xác PhaBERT Nhóm D: 91,38 ± 0,89). Phần thảo luận nghiên cứu loại bỏ thành phần cũng diễn giải biên dao động này (chênh lệch ±0,3–1,5% giữa các biến thể nằm trong biên dao động của kiểm định chéo 5 phần), nhằm tránh kết luận quá mức từ những khác biệt nhỏ.

Góp ý đề xuất một trong ba phương án (độ lệch chuẩn, khoảng tin cậy hoặc kiểm định thống kê); luận văn chọn báo cáo độ lệch chuẩn qua 5 fold cho toàn bộ chỉ số. Do số fold nhỏ (n=5) làm hạn chế lực của kiểm định ý nghĩa thống kê, việc báo cáo độ biến thiên qua độ lệch chuẩn là phương án phù hợp và đầy đủ trong ba phương án mà phản biện đề xuất.

**Vị trí:** Chương 4, Bảng `tab:ablation_results` (nghiên cứu loại bỏ thành phần) và Bảng `tab:main_results` (so sánh với PhaTYP, DeePhage, ProkBERT); đoạn thảo luận nghiên cứu loại bỏ thành phần.

---

### A3. Phân biệt baseline chạy lại vs lấy từ công bố ✅

**Góp ý:** Cần nói rõ baseline nào được học viên chạy lại trên cùng tập dữ liệu, baseline nào trích số liệu từ công bố gốc, để đảm bảo so sánh công bằng.

**Cách xử lý:** Toàn bộ các phương pháp đối chứng (DNABERT-2, DeePhage, PhaTYP, ProkBERT) đều được học viên huấn luyện và đánh giá lại trên chính tập dữ liệu của luận văn, theo cùng cách chia kiểm định chéo phân tầng 5 phần như PhaBERT; không có số liệu nào được trích lại từ công bố gốc. Bổ sung một câu khẳng định tường minh điều này vào phần thiết lập thực nghiệm để người đọc thấy rõ tính công bằng của so sánh.

**Vị trí:** Chương 4, mục `sec:thiet_lap_thuc_nghiem` (Thiết lập thực nghiệm), ngay sau đoạn liệt kê bốn phương pháp đối chứng.

---

### A4. Đánh giá trên dữ liệu độc lập / chia theo cụm tương đồng 📝

**Góp ý:** Cần đánh giá mô hình trên tập dữ liệu độc lập, hoặc chia dữ liệu theo cụm tương đồng trình tự, để chứng minh khả năng tổng quát hóa thực sự (thí nghiệm mới).

**Cách xử lý (giải trình + hướng phát triển):** Do hạn chế về thời gian sau bảo vệ, học viên chưa tiến hành thí nghiệm mới trên dữ liệu độc lập hay chia theo cụm tương đồng. Tuy nhiên, luận văn đã có biện pháp chống rò rỉ thông tin ở mức hệ gen (xem A1): mỗi hệ gen chỉ thuộc một tập trong một fold, tránh việc các contig chồng lấn từ cùng hệ gen lọt cả train lẫn val. Luận văn cũng bổ sung hạn chế về phạm vi đánh giá vào mục Hạn chế và hướng phát triển, thừa nhận chưa kiểm chứng trên một tập dữ liệu độc lập hoàn toàn. Học viên cam kết các hướng phát triển: kiểm chứng PhaBERT trên dữ liệu hệ gen môi trường độc lập, và khảo sát phương án chia dữ liệu theo cụm tương đồng trình tự (CD-HIT / MMseqs2). Đồng thời điều chỉnh một câu ở phần Kết luận để tránh tuyên bố quá mức về khả năng tổng quát hóa.

**Vị trí:** Chương 5, mục `sec:limitations_future` (đoạn về phạm vi đánh giá); Chương 5 phần Kết luận (điều chỉnh câu về tổng quát hóa).

> Ghi chú: phần giải trình này đồng thời đáp ứng góp ý **B3** của PB2 (chưa chứng minh tổng quát hóa trên dữ liệu độc lập) — xem chéo [[B3]].

---

### A5. Phân tích lỗi đa chiều 🔄

**Góp ý:** Cần phân tích lỗi của mô hình theo nhiều chiều: độ dài contig, lớp nhãn, họ phage, vật chủ, và thành phần GC.

**Cách xử lý (phần đã làm):** Bổ sung mục *Phân tích lỗi* (Section 4.4) với:
- Phân tích lỗi theo lớp nhãn: FPR/FNR theo 4 nhóm độ dài (lớp thiểu số temperate bị phân loại sai nhiều hơn; khoảng cách FPR−FNR nới rộng theo độ dài, Nhóm D: 12,43% vs 7,62%).
- Phân tích lỗi theo thành phần GC: quan hệ hình chữ U (mô hình mạnh ở GC 35–55%, yếu ở hai cực, GC>55% lỗi 24,83% toàn cục).

**Phần còn thiếu (giải trình):** Hai chiều phân tích theo **họ phage** và theo **vật chủ** chưa được thực hiện do bộ dữ liệu hiện tại chưa thu thập được chú giải họ phage và vật chủ đầy đủ, nhất quán cho từng hệ gen. Khi không có nhãn đáng tin cho hai chiều này, việc cắt lát lỗi theo họ phage/vật chủ sẽ không bảo đảm độ chính xác. Đây được ghi nhận là hướng phát triển: bổ sung chú giải họ phage và vật chủ cho tập dữ liệu, sau đó phân tích lỗi theo hai chiều này để đánh giá đầy đủ hơn các yếu tố ảnh hưởng đến sai số của mô hình.

**Vị trí:** Chương 4, mục `sec:phan_tich_loi` (Phân tích lỗi), `sec:loi_theo_lop`, `sec:loi_theo_gc`; Bảng `tab:error_by_class`; Hình `fig:error_confusion_matrix`, `fig:error_heatmap_gc`; Chương 5 (mục Hạn chế, bổ sung Hạn chế #3 về GC cực trị).

---

### A6. Lỗi trình bày, trích dẫn, thống nhất tên mô hình ✅

**Góp ý:** Còn lỗi trình bày, lỗi trích dẫn; tên mô hình chưa thống nhất giữa PhaBERT và PhaBERT-CNN.

**Cách xử lý:**
- Thống nhất tên mô hình thành **PhaBERT** (theo glossary; "CNN" chỉ là một thành phần kiến trúc trong mô-đun MKC), đổi 4 chỗ còn sót ở Chương 1, 3, 4.
- Sửa lỗi trích dẫn hỏng hiển thị `[?]` (ví dụ `cobian2016viruses`); nâng 8 entry preprint lên bản xuất bản chính thức ở venue uy tín; chuẩn hóa tiêu đề DNABERT-2.
- Chỉnh hình thức: bỏ in đậm/in nghiêng nhấn mạnh tùy tiện, thay em-dash bằng dấu phẩy ở các vị trí ngắt câu.

**Vị trí:** Chương 1, 3, 4 (đổi tên mô hình); `references.bib` + Chương 1 (sửa trích dẫn); Chương 2, 4, 5 (chỉnh hình thức).

---

### A7. "Phân loại hệ gen thực khuẩn" = phân loại lối sống, không phải taxonomy ✅

**Góp ý:** Cụm từ "phân loại hệ gen thực khuẩn" dễ gây hiểu nhầm là phân loại theo bậc phân loại học (taxonomy), trong khi luận văn thực chất phân loại lối sống (độc lực / ôn hòa).

**Cách xử lý:** Viết lại phần tóm tắt (tiếng Việt và tiếng Anh) nêu rõ bài toán là phân loại lối sống của thực khuẩn thể (độc lực hay ôn hòa); đổi từ khóa thành "Phân loại lối sống" / "Lifestyle classification".

**Vị trí:** `chapters/abtract_vi.tex`, `chapters/abtract_en.tex` (nội dung tóm tắt + từ khóa).

---

## Phần B — Phản biện 2: TS. Hà Mạnh Hùng

### B2. Chưa giải thích ý nghĩa sinh học của kết quả 🔄

**Góp ý:** Luận văn chưa giải thích ý nghĩa sinh học đằng sau kết quả mô hình.

**Cách xử lý (giải trình + hướng phát triển):** Luận văn đã có một số liên hệ sinh học bước đầu: phân tích lỗi theo thành phần GC (mục `sec:loi_theo_gc`) liên hệ sai số của mô hình với đặc trưng thành phần trình tự và gợi ý các nhóm vi khuẩn chủ có GC cực trị; phần ý nghĩa thực tiễn (mục `sec:practical_significance`) bàn về cơ chế sinh học của lối sống thực khuẩn thể (biến đổi tiềm tan, chuyển gen ngang, các gen độc lực điển hình như CTXφ và độc tố Shiga). Tuy nhiên, luận văn chưa giải thích sâu cơ chế sinh học mà mô hình thực sự khai thác để phân biệt lối sống, chẳng hạn các mô-típ hay gen đánh dấu cụ thể mà mô hình dựa vào để ra quyết định.

Học viên xác định đây là một hạn chế và đưa vào hướng phát triển: kết hợp các kỹ thuật phân tích khả diễn giải (interpretability) nhằm xác định các vùng trình tự hoặc gen mà mô hình chú trọng, đối chiếu với tri thức sinh học về các gen điều hòa chu trình tan và chu trình tiềm tan, qua đó làm rõ ý nghĩa sinh học đằng sau kết quả phân loại.

**Vị trí:** Chương 4, mục `sec:loi_theo_gc` và `sec:practical_significance` (phần liên hệ sinh học đã có).

---

### B3. Chưa chứng minh khả năng tổng quát hóa trên dữ liệu độc lập 📝

**Góp ý:** Chưa có bằng chứng tổng quát hóa trên tập dữ liệu độc lập (trùng với góp ý A4 của PB1).

**Giải trình / hướng phát triển:** Xử lý chung với góp ý [[A4]] của PB1. Luận văn đã bổ sung hạn chế về phạm vi đánh giá vào mục Hạn chế và hướng phát triển (Chương 5, `sec:limitations_future`): thừa nhận chưa đánh giá trên dữ liệu độc lập, nêu rõ biện pháp chống rò rỉ ở mức hệ gen đã áp dụng, và cam kết hướng phát triển là kiểm chứng trên dữ liệu hệ gen môi trường độc lập kèm khảo sát chia dữ liệu theo cụm tương đồng. Câu tuyên bố quá mức về tổng quát hóa ở phần Kết luận cũng đã được điều chỉnh lại cho phù hợp.

**Vị trí:** Chương 5, mục `sec:limitations_future` (đoạn về phạm vi đánh giá) và phần Kết luận.

---

### B4. Chưa so sánh với các mô hình nền tảng lớn 📝

**Góp ý:** Chưa so sánh với các mô hình lớn như Nucleotide Transformer hoặc các DNA Transformer quy mô lớn khác.

**Giải trình / hướng phát triển:** Đây là hạn chế của luận văn. Luận văn đã bổ sung hạn chế này vào mục Hạn chế và hướng phát triển (Chương 5, `sec:limitations_future`): nêu rõ nghiên cứu mới chỉ dùng DNABERT-2 làm mạng nền, chưa so sánh với các mô hình nền tảng quy mô lớn hơn như Nucleotide Transformer do chi phí tính toán cao. Học viên cam kết hướng phát triển là đánh giá mô-đun MKC trên nhiều mạng nền khác nhau, bao gồm các mô hình nền tảng hệ gen quy mô lớn.

**Vị trí:** Chương 5, mục `sec:limitations_future` (đoạn về phạm vi đánh giá).

---

## Phần C — Quyết nghị Hội đồng

### C1. Cập nhật trích dẫn tài liệu cũ ✅

**Quyết nghị:** Cập nhật / hạn chế việc trích dẫn các tài liệu đã cũ.

**Cách xử lý:**
- Nâng 8 entry preprint (arXiv) lên bản xuất bản chính thức (ICLR/ACL/EMNLP), bổ sung 3 entry mới cho các luận điểm nhạy thời gian, sửa trích dẫn hỏng.
- Trẻ hóa 6 trích dẫn cũ (>5 năm) ở Chương 1 bằng tài liệu 2021–2026 khớp đúng luận điểm (theo chiến lược lai: giữ nguồn kinh điển + thêm nguồn mới), bổ sung 5 entry mới đã WebFetch xác minh độc lập trên trang gốc.
- Mở rộng rà soát sang **Chương 2**: thay 4 trích dẫn ở venue yếu (preprint chưa bình duyệt + tạp chí cấp thấp) bằng tài liệu cấp cao khớp luận điểm. Cụ thể:

| Luận điểm | Trước (venue yếu) | Sau (venue cấp cao) |
|---|---|---|
| Viral metagenomics qua các hệ sinh thái | `hayes2017metagenomic` (Viruses, MDPI) | `sommers2021integrating` (Annual Review of Virology) |
| reads → contig | `ghurye2016metagenomic` (Yale J. Biol. Med.) | `ayling2020metagenome` (Briefings in Bioinformatics) |
| contig → scaffold | `setubal2021metagenome` (Biophysical Reviews) | `ayling2020metagenome` (Briefings in Bioinformatics) |
| Gộp chú ý (attention pooling) | `santos2016attentive` (arXiv preprint) | `lin2017structured` (ICLR 2017) |

  Kèm theo: thêm 1 entry mới (`ayling2020metagenome`), sửa venue `lin2017structured` (arXiv → ICLR 2017), xóa 3 entry mồ côi (`santos2016attentive`, `setubal2021metagenome`, `hayes2017metagenomic`). Mọi nguồn mới đã WebFetch xác minh độc lập. Giữ nguyên các trích dẫn nền tảng/nguồn gốc phương pháp.

**Vị trí:** `references.bib`, Chương 1 và Chương 2.

---

## Phụ lục — Tham chiếu nhật ký thay đổi

Chi tiết kỹ thuật của từng đợt chỉnh sửa được lưu trong thư mục `changelogs/`:

| File | Nội dung |
|---|---|
| `2026-06-07_rename-phabert.md` | Thống nhất tên mô hình PhaBERT (A6) |
| `2026-06-07_CITATION_UPDATES.md` | Nâng cấp 8 preprint, sửa cite hỏng, +3 entry (A6, C1) |
| `2026-06-09_chia-fold-tien-xu-ly.md` | Làm rõ chia 5-fold mức hệ gen, chống rò rỉ (A1) |
| `2026-06-09_phan-tich-loi.md` | Bổ sung Section 4.4 Phân tích lỗi (A5, B2) |
| `2026-06-09_tre-hoa-trich-dan-c1.md` | Trẻ hóa 6 trích dẫn Chương 1, +5 entry (C1) |
| `2026-06-10_nang-cap-trich-dan-c2.md` | Nâng cấp 4 trích dẫn Chương 2, +1 entry, sửa venue lin2017, xóa 3 mồ côi (C1) |

# Nhật ký cập nhật trích dẫn — 2026-06-07

Ghi lại toàn bộ thay đổi về tài liệu tham khảo thực hiện trong phiên làm việc này.
Mục tiêu: cập nhật trích dẫn cũ lên bản xuất bản chính thức ở venue uy tín, sửa lỗi
citation, và bổ sung nguồn mới cho các luận điểm nhạy thời gian.

**Nguyên tắc xuyên suốt:** giữ nguyên citation key (không phá `\cite` cũ), chỉ đổi
metadata; mọi metadata đều được **WebFetch xác minh độc lập** trên trang nguồn gốc
(ACL Anthology / OpenReview / DBLP / PMC / PubMed); không đổi nội dung/số liệu trong
câu, chỉ đổi lệnh `\cite`.

---

## Phần 1 — Nâng cấp 8 entry preprint → bản xuất bản chính thức

File: `references.bib`. Citation key giữ nguyên; chỉ đổi type/venue/năm/metadata.
Tất cả đã WebFetch xác minh khớp chính xác nguồn gốc.

| Key | Trước | Sau (đã verify) | Nguồn xác minh |
|---|---|---|---|
| `zhou2023dnabert` | arXiv 2306.15006, 2023 | `@inproceedings` ICLR 2024 | OpenReview oMLQB4EZE1 |
| `sennrich2015neural` | arXiv 1508.07909, 2015 | `@inproceedings` ACL 2016, pp.1715–1725, DOI 10.18653/v1/P16-1162 | ACL Anthology P16-1162 |
| `kudo2018sentencepiece` | arXiv 1808.06226, 2018 | `@inproceedings` EMNLP 2018 Demos, pp.66–71, DOI 10.18653/v1/D18-2012 | ACL Anthology D18-2012 |
| `press2021train` | arXiv 2108.12409, 2021 | `@inproceedings` ICLR 2022, url OpenReview R8sQPpGCv0 | OpenReview R8sQPpGCv0 |
| `loshchilov2017decoupled` | arXiv 1711.05101, 2017 | `@inproceedings` ICLR 2019, url OpenReview Bkg6RiCqY7 | OpenReview Bkg6RiCqY7 |
| `howard2018universal` | `@article` (sai type) ACL 2018 | `@inproceedings` ACL 2018, pp.328–339, DOI 10.18653/v1/P18-1031 | ACL Anthology P18-1031 |
| `kingma2015adam` | arXiv 1412.6980, 2015 | `@inproceedings` ICLR 2015 | DBLP (ICLR Poster 2015) |
| `santos2016attentive` | `@inproceedings` ghi "arXiv" (lỗi cấu trúc) | `@misc` arXiv 1602.03609 (chưa từng xuất bản) | arXiv 1602.03609 |

Ghi chú:
- Các bài ICLR không có DOI truyền thống → dùng `url` OpenReview, không bịa DOI.
- `DNABERT-2` là model trung tâm của luận văn: nâng từ "preprint 2023" lên "ICLR 2024".

## Phần 2 — Sửa lỗi citation hỏng

File: `chapters/c1/chapter_1.tex` (dòng 7).

- **Trước:** `\cite{cobian2016vi-rútes}` (từ "viruses" bị tự động dịch thành "vi-rútes"
  bên trong lệnh `\cite` → hiện `[?]` trong PDF)
- **Sau:** `\cite{cobian2016viruses}` (khớp đúng key trong `references.bib`)

## Phần 3 — Chuẩn hóa tiêu đề DNABERT-2

File: `references.bib` (`zhou2023dnabert`).

- **Trước:** "...Benchmark for Multi-Species Genome" (số ít)
- **Sau:** "...Benchmark for Multi-Species Genomes" (số nhiều, khớp tiêu đề chính thức
  trên OpenReview ICLR 2024)

## Phần 4 — Bổ sung nguồn mới cho luận điểm nhạy thời gian (Chương 1)

Chỉ áp dụng cho trích dẫn "Loại 3" (tuyên bố bối cảnh hiện tại). Không đổi nội dung/
số liệu trong câu — chỉ đổi `\cite`. Thêm 3 entry mới vào `references.bib`, tất cả đã
WebFetch xác minh.

### 4.1 — Luận điểm "AMR ngày càng gia tăng → liệu pháp phage hứa hẹn" (dòng 7)

- **Trước:** `...gia tăng, liệu pháp phage...hứa hẹn~\cite{gorski2016phage};`
- **Sau:** `...gia tăng~\cite{murray2022amr}, liệu pháp phage...hứa hẹn~\cite{gorski2016phage,strathdee2023phage};`
- Mỗi citation chống đỡ đúng một vế: Murray 2022 (quy mô AMR) + Strathdee 2023 (phage therapy).

### 4.2 — Luận điểm "CSDL hệ gen phage vẫn còn rất hạn chế" (dòng 16)

- **Trước:** `...trong tự nhiên~\cite{hayes2017metagenomic}.`
- **Sau:** `...trong tự nhiên~\cite{rolland2024phagedive}.`
- Thay (không ghép): Rolland 2024 khớp gần nguyên văn ("only a very limited fraction...
  maintained in public collections") và mới hơn. `hayes2017metagenomic` vẫn được trích
  ở `chapters/c2/chapter_2.tex` nên không tạo entry mồ côi.

### Entry mới thêm vào `references.bib`

| Key | Venue | Metadata (đã verify) | Nguồn |
|---|---|---|---|
| `murray2022amr` | The Lancet | 399(10325):629–655, 2022, DOI 10.1016/S0140-6736(21)02724-0 | PubMed 35065702 |
| `strathdee2023phage` | Cell | 186(1):17–31, 2023, DOI 10.1016/j.cell.2022.11.017 | PMC9827498 |
| `rolland2024phagedive` | Nucleic Acids Research | 53(D1):D819–D825, 2024, DOI 10.1093/nar/gkae878 | PMC11701545 |

---

## Kiểm tra (sau mỗi phần đều compile full 4 lệnh)

```
pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex
```

Kết quả lần compile cuối:
- 4/4 pass exit 0
- 0 undefined citation · 0 undefined reference
- 3 key mới (`murray2022amr`, `strathdee2023phage`, `rolland2024phagedive`) resolve đúng trong `.bbl`
- Không còn `[?]` (lỗi cobian đã sửa)

## Phạm vi KHÔNG đụng tới (ghi nhận để tham khảo sau)

- **Nhóm C (SOTA mới):** ProkBERT PhaStyle 2025, Evo/Evo2, Caduceus, GROVER... đã research
  nhưng người dùng chọn **không bổ sung** trong phiên này. Dữ liệu research vẫn sẵn nếu
  cần dùng sau.
- **Trích dẫn Loại 1 & 2 ở Chương 1** (tên công cụ + khái niệm nền tảng như suttle2007,
  koskella2014, howard2017, mokili2012...): giữ nguyên — trích nguồn gốc là đúng chuẩn,
  không phải lỗi thời.

---

## Tổng hợp file đã thay đổi

- `references.bib` — cập nhật 8 entry (Phần 1) + chuẩn hóa 1 tiêu đề (Phần 3) + thêm 3 entry (Phần 4)
- `chapters/c1/chapter_1.tex` — sửa 1 cite hỏng (Phần 2) + cập nhật cite ở dòng 7 và 16 (Phần 4)

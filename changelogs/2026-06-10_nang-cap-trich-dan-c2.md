# Nhật ký nâng cấp trích dẫn cũ — Chương 2 — 2026-06-10

Ghi lại thay đổi thực hiện trong phiên: thay các trích dẫn cũ ở venue yếu (preprint
chưa bình duyệt + tạp chí cấp thấp) trong Chương 2 bằng tài liệu ở hội nghị/tạp chí
cấp cao hơn, khớp đúng luận điểm.

**Nguyên tắc xuyên suốt:** chỉ thay các trích dẫn **hỗ trợ luận điểm chung**; tuyệt
đối giữ nguyên trích dẫn **nền tảng/kinh điển** (Transformer, BERT, ReLU, Adam, BPE,
GAP, SPP...) và **nguồn gốc phương pháp** (DeePhage, PhaTYP, DNABERT, ProkBERT...).
Mọi nguồn mới đều **WebFetch/xác minh độc lập** trên trang gốc trước khi áp dụng.
Không đổi nội dung/số liệu trong câu, chỉ đổi lệnh `\cite`.

**Lưu ý:** hội nghị hàng đầu ML (NeurIPS/ICLR/ICML/ACL/EMNLP/NAACL) là venue cấp CAO
— không bị coi là "cấp thấp"; không đụng tới.

---

## Phần 1 — Thay trích dẫn trong `chapters/c2/chapter_2.tex`

| Dòng | Luận điểm | Trước | Sau | Hành động |
|---|---|---|---|---|
| 31 | Viral metagenomics: đa dạng phage qua các hệ sinh thái (đại dương/đất/ruột) | `emerson2012dynamic,hayes2017metagenomic` | `emerson2012dynamic,sommers2021integrating` | THAY hayes2017 |
| 33 | reads → contig (qua vùng chồng lấp) | `ghurye2016metagenomic` | `ayling2020metagenome` | THAY |
| 33 | contig → scaffold (điền ký tự N) | `setubal2021metagenome` | `ayling2020metagenome` | THAY |
| 182 | Gộp chú ý = trọng số học thay vì cố định | `santos2016attentive` | `lin2017structured` | THAY |
| 189 | Gộp chú ý tốn thêm tham số + chi phí tính toán | `santos2016attentive` | `lin2017structured` | THAY |

Ghi chú:
- **hayes2017 → sommers2021:** từ *Viruses* (MDPI) lên *Annual Review of Virology*; cùng
  chủ đề viral metagenomics, mới hơn. (`sommers2021integrating` đã có sẵn trong bib, dùng ở c1.)
- **ghurye2016 + setubal2021 → ayling2020:** một review Q1 (*Briefings in Bioinformatics*)
  bao trùm CẢ contig lẫn scaffold → gộp 2 nguồn yếu thành 1 nguồn mạnh.
- **santos2016 → lin2017:** từ arXiv preprint lên ICLR 2017 (peer-reviewed). `lin2017structured`
  đã có trong bib nhưng entry ghi SAI venue = "arXiv preprint" → đã sửa (xem Phần 3).

## Phần 2 — Trích dẫn GIỮ NGUYÊN (không phải lỗi thời / là nguồn gốc)

- Toàn bộ trích dẫn nền tảng/kinh điển: `vaswani2017attention`, `devlin2019bert`,
  `nair2010rectified`, `kingma2015adam`, `sennrich2015neural`, `kim2014convolutional`,
  `lin2014network`, `he2015spatial`, `watson1953molecular`, `rumelhart1986learning`...
- Trích dẫn nguồn gốc phương pháp/công cụ: `wu2021deephage`, `shang2023phatyp`,
  `ji2021dnabert`, `zhou2023dnabert`, `zhang2024deeppl`, `ligeti2024prokbert`,
  `mcnair2012phacts`, `hockenberry2021bacphlip`, `hyatt2010prodigal`.
- `tynecki2020phageai` (BioRxiv 2020): GIỮ preprint — PhageAI chưa từng có bản
  peer-reviewed, đây là nguồn gốc duy nhất của tool.
- `yang2016hierarchical` (NAACL 2016): đã peer-reviewed, giữ nguyên ở §2.4.4.

## Phần 3 — Thay đổi `references.bib`

**Thêm mới (1 entry, đã verify):**

| Key | Venue | Metadata (đã verify) | Nguồn xác minh |
|---|---|---|---|
| `ayling2020metagenome` | Briefings in Bioinformatics | 21(2):584–594, 2020, DOI 10.1093/bib/bbz020 | Semantic Scholar PDF / PubMed 30815668 |

**Sửa entry (1 entry):**

- `lin2017structured`: `@article ... journal={arXiv preprint arXiv:1703.03130}` →
  `@inproceedings ... booktitle={The Fifth International Conference on Learning
  Representations (ICLR)}, year={2017}, url={openreview.net/forum?id=BJC_jUqxe}`.
  (Định danh ICLR 2017 xác nhận qua dblp conf/iclr/LinFSYXZB17 + OpenReview.)

**Xóa entry mồ côi (3 entry — sau khi thay không còn nơi nào trích trong toàn luận văn):**

- `santos2016attentive` (arXiv) · `setubal2021metagenome` (Biophys. Reviews) ·
  `hayes2017metagenomic` (MDPI Viruses).

Luận điểm đã xác minh khớp (WebFetch/perplexity):
- **Ayling 2020:** "overlaps are computed by comparing all reads to all other reads,
  overlaps are grouped together to form contigs"; "link contigs together in 'scaffolds'".
  → khớp cả contig lẫn scaffold.
- **Lin 2017:** "self-attention mechanism... to replace the max pooling or averaging step";
  cần ma trận trọng số học Ws1, ws2. → khớp gộp chú ý = trọng số học + tốn tham số.
- **Sommers 2021:** "viral metagenomics has expanded our knowledge of the ecology of
  uncultured viruses" trong cả môi trường (đại dương, đất) lẫn host-associated (ruột người).

---

## Kiểm tra (compile full 4 lệnh)

```
pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex
```

Kết quả:
- 4/4 pass exit 0 · PDF 75 trang
- 0 cảnh báo bibtex · 0 undefined citation · 0 undefined reference
- `ayling2020metagenome`, `lin2017structured` (ICLR 2017), `sommers2021integrating`
  resolve đúng trong `thesis.bbl`; 3 entry mồ côi đã biến mất khỏi bibliography.

## Phạm vi KHÔNG đụng tới

- **`ghurye2016metagenomic`:** chỉ thay trong c2; entry GIỮ trong `references.bib` vì
  `chapters/c4/chapter_4.tex` vẫn trích → tránh hỏng cite ở Chương 4.
- **Chương 2 chỉ đụng `\cite`** (+ bib), không sửa nội dung/số liệu câu.

---

## Tổng hợp file đã thay đổi

- `references.bib` — thêm 1 entry (`ayling2020metagenome`), sửa venue
  `lin2017structured` (→ICLR 2017), xóa 3 entry mồ côi.
- `chapters/c2/chapter_2.tex` — cập nhật `\cite` ở dòng 31, 33 (×2), 182, 189.

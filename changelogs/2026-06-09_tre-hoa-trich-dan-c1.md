# Nhật ký trẻ hóa trích dẫn cũ — Chương 1 — 2026-06-09

Ghi lại thay đổi thực hiện trong phiên: thay/bổ sung các trích dẫn cũ (>5 năm) trong
Chương 1 bằng tài liệu mới hơn (2021–2026) khớp đúng luận điểm.

**Nguyên tắc xuyên suốt:** chiến lược **lai** — giữ nguồn kinh điển + thêm nguồn mới
song song; thay hẳn các review thường. Ưu tiên **mới + uy tín cân bằng**, khớp chính
xác luận điểm. Mọi nguồn mới đều **WebFetch xác minh độc lập** trên trang gốc
(PMC/PubMed/Frontiers/Nature) trước khi áp dụng. Không đổi nội dung/số liệu trong câu,
chỉ đổi lệnh `\cite`.

---

## Phần 1 — Thay/bổ sung trích dẫn trong `chapters/c1/chapter_1.tex`

| Dòng | Luận điểm | Trước | Sau | Hành động |
|---|---|---|---|---|
| 7 | Đồng tiến hóa VK–phage + chuyển gen ngang | `koskella2014bacteria` | `chevallereau2022interactions` | THAY |
| 7 | Phân loại tan/tiềm tan, prophage | `howard2017lysogeny` | `howard2017lysogeny,rostol2026revisiting` | GIỮ + THÊM |
| 7 | AMR → liệu pháp phage hứa hẹn | `gorski2016phage,strathdee2023phage` | `strathdee2023phage` | BỎ gorski2016 |
| 7 | Nguy cơ truyền gen AMR (tiềm tan) | `cobian2016viruses` | `gummalla2023temperate,strathdee2023phage` | THAY + THÊM |
| 9 | Metagenomics nghiên cứu phage không cần nuôi cấy | `mokili2012metagenomics` | `sommers2021integrating` | THAY |
| 16 | Phage không có gen đánh dấu phổ quát như 16S rRNA | `mokili2012metagenomics` | `schackart2023evaluation` | THAY |

Ghi chú:
- **#4 (gorski2016):** dòng 7 vốn đã đồng trích `strathdee2023phage` (Cell 2023) → chỉ
  cần bỏ `gorski2016phage`, luận điểm vẫn được nguồn mới + uy tín chống đỡ.
- **#5 (venue):** `gummalla2023temperate` khớp luận điểm chính xác nhất nhưng ở
  *Microorganisms* (MDPI) → ghép thêm `strathdee2023phage` (Cell) để cân bằng uy tín.
- **#6:** `mokili2012metagenomics` được tách thành 2 nguồn đúng domain hơn — Sommers 2021
  cho vế "không cần nuôi cấy" (dòng 9), Schackart 2023 cho vế "không có 16S" (dòng 16).

## Phần 2 — Trích dẫn cũ GIỮ NGUYÊN (không phải lỗi thời)

- `suttle2007marine` (2007): con số 10³⁰ là nguồn kinh điển → giữ.
- `howard2017lysogeny` (2017): chuẩn vàng cơ chế lysogeny → giữ, chỉ thêm nguồn mới
  song song (rostol2026revisiting).
- `strathdee2023phage` (2023), `murray2022amr` (2022): đã đủ mới → giữ.
- Toàn bộ trích dẫn tên phương pháp/công cụ (`mcnair2012phacts`, `hockenberry2021bacphlip`,
  `wu2021deephage`, `shang2023phatyp`, `zhang2024deeppl`, `zhou2023dnabert`,
  `rolland2024phagedive`): giữ — năm xuất bản gắn liền với chính phương pháp.

## Phần 3 — Entry mới thêm vào `references.bib` (5 entry, đã verify)

| Key | Venue | Metadata (đã verify) | Nguồn xác minh |
|---|---|---|---|
| `chevallereau2022interactions` | Nature Reviews Microbiology | 20(1):49–62, 2022, DOI 10.1038/s41579-021-00602-y | PMID 34373631 / Nature |
| `gummalla2023temperate` | Microorganisms | 11(3):541, 2023, DOI 10.3390/microorganisms11030541 | PMC10052878 |
| `sommers2021integrating` | Annual Review of Virology | 8(1):133–158, 2021, DOI 10.1146/annurev-virology-010421-053015 | PubMed 34033501 |
| `schackart2023evaluation` | Frontiers in Microbiology | 14:1078760, 2023, DOI 10.3389/fmicb.2023.1078760 | Frontiers (full text) |
| `rostol2026revisiting` | Nature Reviews Microbiology | 2026, DOI 10.1038/s41579-026-01318-7 (online ahead of print — chưa có volume/pages) | Nature |

Luận điểm đã WebFetch xác minh khớp:
- Chevallereau 2022: "phages shape the composition and evolution of bacterial communities";
  bàn transduction (HGT). → khớp đồng tiến hóa + chuyển gen ngang.
- Gummalla 2023: "temperate phage can collect ARGs... by generalized or specialized
  transduction"; "could be a potential risk jeopardizing... antimicrobial intervention". → khớp nguy cơ AMR.
- Sommers 2021: "viral metagenomics has expanded our knowledge of the ecology of
  uncultured viruses". → khớp vế không cần nuôi cấy.
- Schackart 2023: "Since viruses lack a universal gene marker (e.g., 16S rRNA in
  prokaryotes)...". → khớp vế không có gen đánh dấu phổ quát.
- Rostøl 2026: bàn chu trình tan/tiềm tan, prophage trong host. → khớp phân loại tiềm tan.

---

## Kiểm tra (compile full 4 lệnh)

```
pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex
```

Kết quả:
- 4/4 pass exit 0
- 0 cảnh báo bibtex · 0 undefined citation · 0 undefined reference
- 5 key mới resolve đúng trong `thesis.bbl`

## Phạm vi KHÔNG đụng tới (ghi nhận để tham khảo sau)

- **Entry bib cũ không xóa:** `koskella2014bacteria`, `mokili2012metagenomics`,
  `howard2017lysogeny` vẫn được `chapters/c2/chapter_2.tex` trích → giữ trong
  `references.bib` để tránh entry mồ côi / hỏng cite ở Chương 2.
- **Chương 1 chỉ đụng `\cite`,** không sửa nội dung/số liệu câu.

## Việc cần làm sau (theo dõi)

- `rostol2026revisiting` mới đăng (online ahead of print) → khi Nature gán volume/pages
  chính thức thì cập nhật lại entry; đối chiếu lại danh sách tác giả đầy đủ (hiện ghi
  "Rost{\o}l, Chmielowska, Marina, et al.").

---

## Tổng hợp file đã thay đổi

- `references.bib` — thêm 5 entry mới (Phần 3)
- `chapters/c1/chapter_1.tex` — cập nhật `\cite` ở dòng 7 (×4), 9, 16 (Phần 1)

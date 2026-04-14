# Plan: Chapter 5 — Kết luận (Revision)

Source file: `chapters/c5/chapter_5.tex` (27 lines)

---

## Summary of Issues

| # | Severity | Location | Issue |
|---|----------|----------|-------|
| 1 | CRITICAL | Line 14 | Duplicate `\label{sec:contributions}` — also in C1 line 35 |
| 2 | CRITICAL | Lines 9, 18 | "kiểm chứng chéo" must be "kiểm định chéo" |
| 3 | WARNING | Between lines 3–4 | Missing chapter intro paragraph |
| 4 | WARNING | Lines 7, 20 | Inconsistent metagenomic term: "siêu hệ gen" vs "hệ metagenome" |
| 5 | SUGGESTION | Lines 16–20, 27 | Dense paragraphs — consider splitting |

---

## Issue 1 — CRITICAL: Duplicate `\label{sec:contributions}`

**Location:** Line 14  
**Problem:** `\label{sec:contributions}` at C5 line 14 duplicates the same label defined at `chapters/c1/chapter_1.tex:35`. LaTeX will silently use whichever it processes last, potentially breaking any `\ref{}` targeting C1's section.  
**Verification:** `sec:contributions` is not `\ref{}`'d anywhere in the codebase, so no cross-references need updating.

**Fix:**

```latex
% Before (line 14):
\label{sec:contributions}

% After:
\label{sec:contributions_c5}
```

No other lines in C5 need to change. No other files need to change.

---

## Issue 2 — CRITICAL: "kiểm chứng chéo" → "kiểm định chéo"

**Location:** Lines 9 and 18  
**Problem:** "kiểm chứng chéo" is a non-canonical rendering. The canonical term per `.claude/rules/vietnamese-terms.md` is "kiểm định chéo". C1–C4 have already been corrected.

**Fix (line 9):**

```latex
% Before:
thông qua kiểm chứng chéo phân tầng 5 phần

% After:
thông qua kiểm định chéo phân tầng 5 phần
```

**Fix (line 18):**

```latex
% Before:
luận văn cung cấp đánh giá trên bốn nhóm độ dài contig từ 100 đến 1.800 bp thông qua kiểm chứng chéo phân tầng 5 phần

% After:
luận văn cung cấp đánh giá trên bốn nhóm độ dài contig từ 100 đến 1.800 bp thông qua kiểm định chéo phân tầng 5 phần
```

---

## Issue 3 — WARNING: Missing chapter intro paragraph

**Location:** Between line 2 (`\label{chap:conclusion}`) and line 4 (`\section{Kết luận}`)  
**Problem:** C5 jumps directly from `\chapter{Kết luận}` to `\section{Kết luận}` without a narrative bridge paragraph. Chapters 3 and 4 both open with a 3–4 sentence paragraph that (a) states what the chapter covers, (b) references prior chapters for context, and (c) previews the section sequence — all in flowing prose, not a bullet list.

**Style reference:** C3 opens with "Chương này trình bày chi tiết phương pháp... Chương trình bày tuần tự từ..." C4 opens with "Chương này trình bày các thực nghiệm... chương này tập trung vào... Chương trình bày tuần tự từ..."

**Fix:** Insert a 2–3 sentence paragraph after `\label{chap:conclusion}` and before `\section{Kết luận}`. The paragraph must:
- State that the chapter summarizes findings and situates the contribution
- Reference C3 (method) and C4 (experiments) in flowing prose
- Preview the three sections (kết luận, đóng góp, hạn chế) without mechanical enumeration

**Draft text:**

```latex
Chương này tổng kết các kết quả nghiên cứu của luận văn và đánh giá ý nghĩa của phương pháp PhaBERT-CNN được đề xuất trong Chương~\ref{chap:method} và kiểm chứng tại Chương~\ref{chap:thuc_nghiem_danh_gia}. Nội dung được tổ chức theo ba phần: tóm tắt kết quả và nhận định chính, tổng hợp các đóng góp của nghiên cứu, và thảo luận về hạn chế cùng hướng phát triển trong tương lai.
```

Note: This uses `\ref{chap:method}` and `\ref{chap:thuc_nghiem_danh_gia}` — both labels exist and are correct. No new citations needed.

---

## Issue 4 — WARNING: Inconsistent metagenomic terminology

**Location:** Line 7 ("dữ liệu siêu hệ gen") and line 20 ("hệ metagenome" — appears 3 times)  
**Problem:** Two different Vietnamese renderings of the same concept are used within the same chapter.

**Analysis of usage across the thesis:**
- C1: uses "metagenomic" (English, kept as-is per forbidden-substitution rules)
- C3: uses "hệ metagenome" (intro paragraph line 3) and "siêu hệ gen" (line 9 of C4)
- C4 line 9: "siêu hệ gen" — used directly in a key experimental sentence
- C5 line 7: "siêu hệ gen" — already uses the preferred form
- C5 line 20: "hệ metagenome" — three occurrences, inconsistent with line 7

**Decision:** Standardize to "siêu hệ gen" throughout C5, consistent with C4 and C5 line 7.

**Fix (line 20) — three substitutions:**

```latex
% Before (occurrence 1):
PhaBERT-CNN giải quyết một thách thức quan trọng trong phân tích dữ liệu hệ metagenome:

% After:
PhaBERT-CNN giải quyết một thách thức quan trọng trong phân tích dữ liệu siêu hệ gen:

% Before (occurrence 2):
phân loại lối sống thực khuẩn thể từ các contig phân mảnh thu được qua quá trình lắp ráp hệ metagenome.

% After:
phân loại lối sống thực khuẩn thể từ các contig phân mảnh thu được qua quá trình lắp ráp siêu hệ gen.

% Before (occurrence 3):
PhaBERT-CNN có tiềm năng tích hợp vào các quy trình phân tích hệ metagenome tự động,

% After:
PhaBERT-CNN có tiềm năng tích hợp vào các quy trình phân tích siêu hệ gen tự động,
```

---

## Issue 5 — SUGGESTION: Dense paragraphs

**Location:** Section 5.2 (lines 16–18, single paragraph ~290 words) and Section 5.3 (line 27, single paragraph ~200 words)

**Assessment:** These are genuinely dense but the content is logically organized within each paragraph (methodological contribution → training strategy → distinction; experimental results → ablation → comparison). Splitting would require finding natural topical breaks.

**Recommended split points (optional, not required for correctness):**

For Section 5.2 (Đóng góp), the paragraph on lines 16–18 covers three contributions across three sentences but the third sentence on training strategy could begin a new paragraph starting with "Chiến lược huấn luyện hai giai đoạn..."

For Section 5.3 (Hạn chế), line 27 covers nucleotide-only limitation and multi-modal extension — the sentence beginning "Hướng phát triển tự nhiên là mở rộng..." could open a new paragraph.

**Decision for this revision:** Leave Issue 5 as a low-priority suggestion. Fix Issues 1–4 first; revisit paragraph splitting only if the supervisor requests improved readability.

---

## Ordered Fix Sequence

Execute in this order to minimize re-reading:

1. **Issue 3** — Insert intro paragraph (after line 2, before line 4)
2. **Issue 1** — Rename label on line 14 (line numbers shift by +3 after Issue 3 insert, so this becomes line 17)
3. **Issue 2** — Fix "kiểm chứng chéo" on original lines 9 and 18 (now lines 12 and 21)
4. **Issue 4** — Fix "hệ metagenome" on original line 20 (now line 23)

After all edits, re-verify that:
- `\label{sec:contributions_c5}` appears exactly once in the file
- "kiểm chứng" does not appear anywhere in `chapters/c5/chapter_5.tex`
- "hệ metagenome" does not appear anywhere in `chapters/c5/chapter_5.tex`
- The intro paragraph uses `\ref{chap:method}` and `\ref{chap:thuc_nghiem_danh_gia}` (not `\cite{}`)

---

## Constraints Confirmed

- No new `\cite{}` keys added
- Section titles unchanged: "Kết luận", "Đóng góp của nghiên cứu", "Hạn chế và hướng phát triển tương lai"
- No `\label{}` names changed except `sec:contributions` → `sec:contributions_c5`
- No technical content, numbers, or performance figures modified
- No structural changes to sections

---

## Vietnamese Terminology Used

| English | Vietnamese (canonical) |
|---------|----------------------|
| Cross-validation | kiểm định chéo |
| Metagenomic data | dữ liệu siêu hệ gen |
| Metagenomic assembly | lắp ráp siêu hệ gen |
| Metagenomic analysis pipeline | quy trình phân tích siêu hệ gen |

---

## Citation Keys in C5 (all pre-verified — no changes needed)

| Key | Status |
|-----|--------|
| `hyatt2010prodigal` | ✓ EXISTS |
| `trimble2012short` | ✓ EXISTS |
| `zhou2023dnabert` | ✓ EXISTS |
| `shang2023phatyp` | ✓ EXISTS |
| `wu2021deephage` | ✓ EXISTS |
| `ligeti2024prokbert` | ✓ EXISTS |
| `lin2017focal` | ✓ EXISTS |
| `lin2023esm2` | ✓ EXISTS |
| `elnaggar2021prottrans` | ✓ EXISTS |

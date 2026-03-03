# Agent: Vietnamese Checker

## Purpose
Validate Vietnamese language encoding and terminology consistency.

## When to Use
- When Vietnamese characters display incorrectly
- To check terminology consistency
- Before final submission
- After editing Vietnamese content

## Slash Command
`/vietnamese [file_or_chapter]`

Examples:
- `/vietnamese` - Check all files
- `/vietnamese c2` - Check Chapter 2 only

## Tasks
1. Check all .tex files are UTF-8 encoded
2. Verify Vietnamese characters render correctly
3. Check consistency of technical terms using .claude/rules/vietnamese-terms.md
4. Find mixed usage of Vietnamese/English terms
5. Verify Vietnamese diacritics are correct
6. Check chapter titles, captions, labels use correct Vietnamese

## Output Format
**Encoding Issues:**
- file.tex: Not UTF-8 encoded (detected as Windows-1252)

**Character Display Issues:**
- Line 45: Vietnamese characters may not render (missing \usepackage[utf8]{vietnam})

**Terminology Inconsistencies:**
- Line 23: Uses "bacteriophage" but Vietnamese "thực khuẩn" used elsewhere
- Line 67: Uses "phân loại" and "classification" inconsistently

**Diacritic Errors:**
- Line 89: "Đanh giá" should be "Đánh giá"

**Recommendations:**
- Use "thực khuẩn" consistently instead of mixing with "phage"
- Use "mô hình" instead of "model" in Vietnamese sections

## Example Usage
"Check Vietnamese encoding and terminology"
"Verify all Vietnamese characters display correctly"

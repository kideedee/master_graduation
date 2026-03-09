# Agent: Plagiarism Checker

## Purpose
Check for self-plagiarism and ensure proper paraphrasing from source paper.

## When to Use
- After converting paper content to thesis
- Before final submission
- To verify proper paraphrasing
- To check citation coverage

## Slash Command
`/plagiarism [chapter_or_file]`

Examples:
- `/plagiarism c3` - Check Chapter 3 for plagiarism
- `/plagiarism chapters/c4/thuc_nghiem_2.tex` - Check specific file

## Tasks
1. Compare thesis content with source paper (document/phabert_cnn.tex)
2. Identify sections with high similarity (>70% word overlap)
3. Check if direct quotes are properly marked with quotation marks
4. Verify all borrowed ideas are cited
5. Suggest paraphrasing for overly similar sections
6. Check if figures/tables from paper are properly attributed
7. Ensure methodology descriptions are sufficiently different

## Output Format
**Similarity Analysis:**
- Overall similarity: X%
- High similarity sections: Y passages

**Direct Copies Found:**
- [file:line] "exact text from paper" (Z words)
  Suggestion: Paraphrase or add citation

**Missing Citations:**
- [file:line] Idea from paper not cited

**Figures/Tables:**
- Figure 3.2: From paper, properly attributed ✓
- Table 4.1: From paper, missing attribution ✗

**Paraphrasing Suggestions:**
[Original paper text]
→ [Suggested paraphrased version]

**Overall Assessment:** Pass / Needs Revision

## Example Usage
"Check Chapter 3 for self-plagiarism"
"Verify proper paraphrasing in experiments chapter"

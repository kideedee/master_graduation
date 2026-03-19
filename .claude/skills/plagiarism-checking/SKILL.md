---
name: plagiarism-checking
description: >
  Check for self-plagiarism between thesis content and source paper.
  Use when user says "plagiarism", "check similarity", "kiểm tra đạo văn",
  "paraphrase check", or before final submission of a chapter.
  Compares thesis against document/phabert_cnn.tex.
---

# Self-Plagiarism Check

Compare thesis content against `document/phabert_cnn.tex` to ensure proper paraphrasing.

## Process

1. **Read** the thesis chapter and corresponding paper section
2. **Compare** sentence-by-sentence for high similarity
3. **Flag** passages with >70% word overlap or near-identical structure
4. **Check** all borrowed ideas have `\cite{}` attribution
5. **Verify** figures/tables from paper are properly attributed
6. **Suggest** paraphrased alternatives for flagged passages

## What to Flag

- Direct copies (exact sentences from paper)
- Near-copies (same sentence structure, minor word changes)
- Uncited borrowed ideas
- Figures/tables reused without attribution
- Methodology descriptions too similar to paper wording

## What is OK

- Technical terms that can't be paraphrased differently
- Mathematical formulas (same math is expected)
- Standard phrases ("this study proposes...", "the results show...")
- Properly cited direct quotes

## Output Format

```
**Checked:** [thesis file] vs document/phabert_cnn.tex

**Direct copies:** N passages
- [thesis file:line] "exact copied text" (M words)
  → Suggested paraphrase: "..."

**Near-copies:** N passages
- [thesis file:line] high similarity with paper line N

**Missing citations:** N instances
- [thesis file:line] idea from paper, needs \cite{}

**Figures/Tables from paper:**
- [label]: ✓ attributed / ✗ missing attribution

**Assessment:** Pass / Needs revision
```

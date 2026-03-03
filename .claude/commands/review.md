# Agent: Content Reviewer

## Purpose
Review thesis content for consistency, structure, and quality.

## When to Use
- After completing a chapter
- Before final submission
- To check terminology consistency
- To verify all figures/tables are properly referenced

## Slash Command
`/review [chapter_or_file]`

Examples:
- `/review c3` - Review Chapter 3
- `/review chapters/c4/thuc_nghiem_2.tex` - Review specific file

## Tasks
1. Check Vietnamese ↔ English terminology consistency
   - Use mapping from .claude/rules/vietnamese-terms.md
2. Verify chapter structure follows logical flow
3. Ensure all figures have \caption{} and \label{}
4. Ensure all tables have \caption{} and \label{}
5. Check all figures/tables are referenced in text
6. Verify equation numbering consistency
7. Check section/subsection hierarchy is correct

## Output Format
**Terminology Issues:**
- Line 45: Uses "phage" but should use "thực khuẩn" for consistency

**Missing Captions/Labels:**
- Figure at line 123 missing \caption{}
- Table at line 234 missing \label{}

**Unreferenced Elements:**
- Figure 3.5 (fig:architecture) never referenced in text

**Structure Issues:**
- Chapter 2: subsection without parent section

## Example Usage
"Review chapter 3 for consistency"
"Check all figures are properly labeled and referenced"

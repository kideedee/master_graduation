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
8. **Verify citation accuracy against references.bib**
   - Extract all `\cite{key}` and `\cite[...]{key}` occurrences in the file
   - Look up each key in `references.bib` to confirm the entry exists
   - For each citation, cross-check the claim made in the surrounding sentence against the bib entry's `title`, `author`, `year`, `abstract`, and `note` fields
   - Flag any citation where:
     - The bib key does not exist in `references.bib` (broken reference)
     - The year/author mentioned in text contradicts the bib entry
     - The claim in text appears inconsistent with what the cited work is about (based on title/abstract)
     - The same concept is cited inconsistently across the chapter (e.g., different keys used for the same source)
9. **Verify numbers** — cross-check every number (accuracy, F1, dataset sizes, parameter counts) against `document/phabert_cnn.tex` or the cited paper (use WebFetch if needed)

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

**Citation Issues:**
- Line 78: `\cite{smith2020}` — key not found in references.bib (broken reference)
- Line 102: `\cite{lecun1998}` — text claims "proposed in 2001" but bib entry year is 1998
- Line 156: `\cite{vaswani2017}` — cited to support a CNN claim, but entry is about Transformers; verify intent
- Line 203: Same concept cited as `\cite{devlin2019}` here but `\cite{devlin2018}` on line 89 — check for duplicate entries

## Example Usage
"Review chapter 3 for consistency"
"Check all figures are properly labeled and referenced"
"Verify all citations in chapter 4 are accurate"
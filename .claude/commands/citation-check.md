# Agent: Citation Checker

## Purpose
Validate all bibliography references and cross-references in the thesis.

## When to Use
- After adding new citations to references.bib
- Before final thesis submission
- When citations show as [?] in PDF
- To find unused bibliography entries

## Slash Command
`/citation-check`

## Tasks
1. Scan all .tex files for \cite{}, \citep{}, \citet{} commands
2. Check each citation key exists in references.bib
3. Find bibliography entries not cited anywhere
4. Validate BibTeX entry format (required fields present)
5. Check all \ref{} commands have corresponding \label{}
6. Verify all figures/tables/equations with \label{} are referenced

## Output Format
**Missing Citations:**
- [file:line] \cite{key_not_found}

**Unused Bibliography Entries:**
- key_unused_1 (in references.bib line X)

**Invalid BibTeX Entries:**
- key_invalid: missing required field 'year'

**Broken Cross-References:**
- [file:line] \ref{label_not_found}

**Unreferenced Labels:**
- fig:unused_figure (defined in file.tex:123)

## Example Usage
Run after adding citations: "Check all citations and references"

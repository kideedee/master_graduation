---
name: latex-compiling
description: >
  Compile LaTeX thesis and auto-debug compilation errors.
  Use when user says "compile", "build", "pdflatex", "debug error",
  "fix compilation", "tạo PDF", or when any LaTeX compilation is needed.
  Also use after writing new content to verify it compiles.
---

# LaTeX Compilation & Debug

## Quick Compile (no bib changes)

```bash
pdflatex thesis.tex
```

## Full Compile (after bib/citation changes)

```bash
pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex
```

## Compilation Workflow

1. Run the appropriate compile command
2. Parse stdout/stderr for errors and warnings
3. For each error:
   - Identify the file and line number
   - Diagnose root cause
   - Apply fix
   - Re-compile to verify
4. Report results

## Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `! Undefined control sequence` | Typo or missing package | Check spelling; add `\usepackage{}` |
| `! Missing $ inserted` | Math symbol outside math mode | Wrap in `$...$` or use `\%`, `\_` |
| `Citation 'key' undefined` | Missing bib entry or no bibtex run | Check references.bib; run full compile |
| `! File not found` | Wrong path in `\input{}` or `\includegraphics{}` | Verify file exists at specified path |
| `! LaTeX Error: \begin{...} ended by \end{...}` | Mismatched environments | Find and fix the mismatch |
| Vietnamese chars broken | Encoding issue | Verify UTF-8 + `\usepackage[utf8]{vietnam}` |

## Debug Strategy

If error is unclear:
1. Check the .log file for detailed context: `tail -50 thesis.log`
2. Isolate the chapter: use `\includeonly{chapters/cN/...}` in thesis.tex
3. Binary search: comment out half the content to locate the error

## Output Format

```
**Status:** ✓ Success / ✗ Failed

**Errors:** (if any)
- [file:line] Error description → Fix applied

**Warnings:** (if any)
- Citation warnings, overfull hbox, etc.

**Result:** thesis.pdf (N pages, N references)
```

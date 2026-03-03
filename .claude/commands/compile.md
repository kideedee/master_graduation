# Agent: LaTeX Compiler

## Purpose
Compile LaTeX thesis and debug compilation errors.

## When to Use
- To compile thesis with full bibliography
- When compilation fails with errors
- To debug missing packages or file paths
- Before viewing updated PDF

## Slash Command
`/compile`

## Tasks
1. Run full compile sequence:
   - pdflatex thesis.tex
   - bibtex thesis
   - pdflatex thesis.tex (2nd pass)
   - pdflatex thesis.tex (3rd pass)
2. Parse error messages and identify root cause
3. Check for missing LaTeX packages
4. Validate file paths in \input{}, \includegraphics{}
5. Suggest fixes for common errors
6. Clean auxiliary files if needed

## Output Format
**Compilation Status:** Success / Failed

**Errors Found:**
- Line 123: ! Undefined control sequence \unknowncommand
  Fix: Add \usepackage{packagename} or check spelling

**Warnings:**
- Citation 'key' undefined (run bibtex)
- Reference 'fig:missing' undefined

**Files Generated:**
- thesis.pdf (X pages)
- thesis.bbl (Y references)

## Example Usage
"Compile thesis with bibliography"
"Debug compilation error in chapter 3"

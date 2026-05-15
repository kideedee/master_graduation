# Troubleshooting

This file contains solutions to common LaTeX compilation and formatting issues.

## Bibliography Issues

**Problem:** Citations showing as `[?]` or not appearing

**Solution:**
```bash
pdflatex thesis.tex
bibtex thesis
pdflatex thesis.tex
pdflatex thesis.tex
```

**Problem:** Bibliography not showing at all

**Solution:**
- Check that `references.bib` has entries
- Ensure you have at least one `\cite{}` command in your document
- Verify the bibliography style is set: `\bibliographystyle{unsrt}`

## Vietnamese Characters

**Problem:** Vietnamese characters not displaying correctly

**Solution:**
- Ensure file is saved with UTF-8 encoding
- Check that `\usepackage[utf8]{vietnam}` and `\usepackage[utf8]{inputenc}` are in preamble
- Use a text editor that supports UTF-8 (VS Code, TeXstudio, etc.)

## Figures Not Appearing

**Problem:** Figures not showing in PDF

**Solution:**
- Verify image file exists in `imgs/` directory
- Check file path is correct (case-sensitive on some systems)
- Ensure image format is supported (PNG, JPG, PDF)
- Try using full path: `\includegraphics{imgs/filename.png}`

## Table of Contents Not Updating

**Problem:** TOC shows old chapter titles or page numbers

**Solution:**
- Run `pdflatex thesis.tex` at least twice
- Delete `.toc` file and recompile: `rm thesis.toc && pdflatex thesis.tex`

## Compilation Errors

**Problem:** `! Undefined control sequence`

**Solution:**
- Check for typos in command names
- Ensure required packages are loaded
- Look at the line number in error message

**Problem:** `! Missing $ inserted`

**Solution:**
- Math symbols must be in math mode: `$\alpha$` not `\alpha`
- Use `\%` for percent sign outside math mode

**Problem:** `! File not found`

**Solution:**
- Check file paths are correct
- Ensure files exist in specified locations
- Use forward slashes `/` even on Windows

## Long Compilation Times

**Solution:**
- Use quick compile (`pdflatex thesis.tex` once) during writing
- Only run full compile with bibtex when needed
- Comment out `\listoffigures` and `\listoftables` during drafting
- Use `\includeonly{chapters/c3/de_xuat}` to compile only specific chapters

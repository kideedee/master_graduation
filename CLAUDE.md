# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Vietnamese master's thesis (Luận văn Thạc sĩ) about deep learning models for wireless device management ("Nghiên cứu các mô hình học sâu cho bài toán quản lý thiết bị vô tuyến"). The thesis is written in LaTeX with Vietnamese language support.

**Author**: Lê Thế Nam
**Institution**: Vietnam National University, Hanoi - University of Engineering and Technology (UET)
**Supervisors**: Dr. Nguyen The Hoang Anh, Assoc. Prof. Le Thanh Ha
**Year**: 2025

## Building the Thesis

### Compile Main Thesis
```bash
pdflatex thesis.tex
bibtex thesis
pdflatex thesis.tex
pdflatex thesis.tex
```

The output will be `thesis.pdf`. You may need to run pdflatex multiple times to resolve all references and generate the table of contents correctly.

### Compile Presentation Slides
```bash
pdflatex slide.tex
```

### Compile Other Documents
```bash
pdflatex cover.tex      # Cover pages only
pdflatex outline.tex    # Thesis outline
pdflatex tomtat.tex     # Summary (tóm tắt)
```

## Project Structure

### Main Files
- `thesis.tex` - Main thesis document that includes all chapters and front matter
- `cover.tex` - Three cover pages (Vietnamese, Vietnamese with author, English)
- `slide.tex` - Beamer presentation template
- `outline.tex` - Thesis outline
- `tomtat.tex` - Vietnamese summary
- `references.bib` - Bibliography database (currently empty)

### Chapter Organization
Chapters are organized in subdirectories under `chapters/`:

- **c1/** - Chapter 1: Introduction (Giới thiệu)
  - `gioi_thieu.tex` - Main chapter file
  - `li_cho_chon_de_tai.tex` - Motivation for topic selection
  - `bo_cuc_luan_van.tex` - Thesis structure

- **c2/** - Chapter 2: Theoretical Background (Cơ sở lý thuyết)
  - `co_so_ly_thuyet.tex` - Main chapter file
  - `gioi_thieu_3d.tex` - 3D reconstruction introduction
  - `nerf.tex` - Neural Radiance Fields
  - `nerf_variants.tex` - NeRF variants
  - `sfm.tex` - Structure from Motion
  - `mvs.tex` - Multi-View Stereo
  - `triangulation.tex` - Triangulation methods
  - `volume_rendering.tex` - Volume rendering
  - `feature_extraction.tex` - Feature extraction overview
  - `sift.tex` - SIFT algorithm
  - `aliked.tex` - ALIKED feature detector
  - `lightglue.tex` - LightGlue feature matching
  - `related.tex` - Related work

- **c3/** - Chapter 3: Proposed Methods (Đề xuất)
  - `de_xuat.tex` - Main chapter file
  - `neus.tex` - NeuS method
  - `neus2.tex` - NeuS2 method
  - `instant_ngp.tex` - Instant Neural Graphics Primitives
  - `neuralangelo.tex` - Neuralangelo method
  - `geo_neus.tex` - Geo-NeuS method

- **c4/** - Chapter 4: Experiments (Thực nghiệm)
  - `thuc_nghiem_2.tex` - Main chapter file
  - `thuc_nghiem.tex` - Detailed experiments

- **c5/** - Chapter 5: Conclusion (Kết luận)
  - `ket luan.tex` - Main chapter file

### Front Matter
Located in `chapters/`:
- `acknowledgement.tex` - Acknowledgements (Lời cảm ơn)
- `assurance.tex` - Assurance statement (Lời cam đoan)
- `abtract_vi.tex` - Vietnamese abstract (Tóm tắt)
- `abtract_en.tex` - English abstract
- `glossary.tex` - Glossary of terms

### Supporting Directories
- `imgs/` - Images and figures used in the thesis
- `snipet/` - Python code snippets for ML frameworks:
  - `tensorflow.py` - TensorFlow examples
  - `keras.py` - Keras examples
  - `sklearn.py.py` - Scikit-learn examples
  - `grayscale.py` - Image processing utilities
- `document/` - Additional documentation
  - `example/` - Example documents
  - `my_work/` - Working documents

## LaTeX Configuration

### Document Class and Formatting
- Document class: `report` with A4 paper, 13pt font
- Margins: left=3cm, right=2cm, top=2.5cm, bottom=3cm
- Line spacing: 1.3
- Vietnamese language support via `vietnam` and `inputenc` packages

### Key Packages Used
- **Math**: `amsmath`, `amsfonts`, `amssymb`, `physics`, `bm`
- **Graphics**: `graphicx`, `tikz`, `float`, `subcaption`
- **Tables**: `longtable`, `booktabs`, `multirow`, `makecell`
- **Code listings**: `listings`
- **Algorithms**: `algorithm` (displayed as "Thuật toán")
- **Bibliography**: `natbib` with `unsrt` style, numbers, sort&compress
- **Formatting**: `titlesec`, `sectsty`, `tocloft`

### Custom Commands
- `\argmax` - Defined as `\arg\!\max`
- Chapter prefix: "Chương" (Vietnamese for "Chapter")

## Working with This Thesis

### Adding New Content
- Each chapter has a main file that includes subsection files
- Add new sections by creating `.tex` files in the appropriate chapter directory
- Include new sections in the chapter's main file using `\input{chapters/cX/filename}`

### Adding References
- Add bibliography entries to `references.bib`
- Cite using `\cite{key}` or `\citep{key}` for parenthetical citations
- Rebuild with bibtex after adding new references

### Adding Figures
- Place images in `imgs/` directory
- Reference with `\includegraphics[options]{imgs/filename}`
- Use `\caption{}` and `\label{}` for cross-referencing

### Vietnamese Language Notes
- The thesis uses UTF-8 encoding with Vietnamese language support
- Chapter titles, figure/table captions, and algorithm names are in Vietnamese
- Maintain consistent Vietnamese terminology throughout

## Git Workflow

- Main branch: `master`
- Development branch: `develop` (current)
- LaTeX auxiliary files are gitignored (see `.gitignore`)
- The compiled PDF (`thesis.pdf`) is tracked in the repository

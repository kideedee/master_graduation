# Agent: Figure Manager

## Purpose
Manage figures and images in the thesis.

## When to Use
- To audit which figures are used/unused
- When figures don't appear in PDF
- To validate figure paths
- Before final submission cleanup

## Slash Command
`/figures`

## Tasks
1. List all image files in imgs/ directory
2. Scan all .tex files for \includegraphics{} commands
3. Match used figures with available files
4. Find unused figure files
5. Find missing figure files (referenced but not exist)
6. Validate figure paths are correct
7. Check all figures have \label{} and \caption{}
8. Verify figure formats are supported (PNG, JPG, PDF)

## Output Format
**Figure Inventory:**
- Total figures in imgs/: X files
- Figures used in thesis: Y files
- Unused figures: Z files

**Used Figures:**
- ✓ imgs/phabert_cnn_architecture.png (used in c3/de_xuat.tex:45)
- ✓ imgs/training_curves.png (used in c4/thuc_nghiem_2.tex:123)

**Unused Figures:**
- imgs/old_diagram.png (not referenced anywhere)

**Missing Figures:**
- imgs/confusion_matrix.png (referenced in c4/thuc_nghiem_2.tex:234 but file not found)

**Issues:**
- Figure at c3/de_xuat.tex:45 missing \caption{}

## Example Usage
"List all figures and check which are used"
"Find missing figure files"

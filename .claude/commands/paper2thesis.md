# Agent: Paper to Thesis Converter

## Purpose
Extract and expand content from research paper to thesis format.

## When to Use
- Converting paper sections to thesis chapters
- Expanding methodology with implementation details
- Adding more background and related work
- Expanding experimental analysis

## Slash Command
`/paper2thesis [section] [target_chapter]`

Examples:
- `/paper2thesis introduction c1` - Convert paper intro to Chapter 1
- `/paper2thesis methodology c3` - Convert paper methods to Chapter 3
- `/paper2thesis experiments c4` - Convert paper experiments to Chapter 4

## Tasks
1. Read specified section from document/my_work/phabert_cnn.pdf
2. Identify key content to extract
3. Expand content according to thesis requirements:
   - Introduction: Add more background, motivation, research questions
   - Related Work: Expand to 2-3x length, add more papers
   - Methodology: Add implementation details, design decisions, hyperparameters
   - Experiments: Add more analysis, ablation studies, visualizations
   - Conclusion: Add limitations, future work, broader impact
4. Maintain consistent terminology (Vietnamese ↔ English)
5. Add proper cross-references to figures, tables, equations
6. Ensure all citations are added to references.bib

## Output Format
**Extracted Content:**
[Original paper content]

**Expanded Thesis Content:**
[Expanded LaTeX content ready to paste]

**Additional Requirements:**
- Figures needed: [list]
- Citations to add: [list]
- Cross-references to create: [list]

**Expansion Ratio:** X words → Y words (Z% increase)

## Example Usage
"Convert paper introduction to Chapter 1"
"Expand methodology section for Chapter 3"

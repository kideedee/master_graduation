# Agent: Paper to Thesis Converter

Convert and expand content from the research paper to thesis format, following the mandatory 3-step workflow.

## Slash Command

`/paper2thesis [section] [target_chapter]`

Examples:
- `/paper2thesis introduction c1` - Convert paper intro to Chapter 1
- `/paper2thesis methodology c3` - Convert paper methods to Chapter 3
- `/paper2thesis experiments c4` - Convert paper experiments to Chapter 4

## Process

### Step 1 — Plan

1. Read the specified section from `document/phabert_cnn.tex`
2. Identify content to extract and expand
3. Create a plan file at `plans/<chapter>_paper2thesis_plan.md` containing:
   - **Expanded outline**: hierarchical structure for the thesis version (2-3x longer than the paper)
   - **Paragraph descriptions**: one sentence per paragraph describing what it conveys
   - **Content to add**: implementation details, design decisions, additional analysis
   - **Citation list**: citation keys you intend to use + short reason
   - **Numbers to verify**: every number that will appear
4. Present the plan to the user and wait for confirmation

### Step 2 — Write

Write expanded LaTeX content following the plan:
- Write entirely in Vietnamese (see Critical Rule #6 in CLAUDE.md for exceptions)
- Expand according to each chapter's requirements:
  - Introduction: add more background, motivation, research questions
  - Related Work: expand 2-3x, add more related papers
  - Methodology: add implementation details, design decisions, hyperparameters
  - Experiments: add more analysis, ablation studies, visualizations
  - Conclusion: add limitations, future work, broader impact
- Use terminology from `.claude/rules/vietnamese-terms.md`
- Every figure, table, and equation must have `\label{}` and be referenced

### Step 3 — Verify

1. **Citation keys**: confirm every `\cite{key}` exists in `references.bib`
2. **Claim verification**: use WebFetch to retrieve cited papers and confirm claims are accurate
3. **Number verification**: cross-check every number against `document/phabert_cnn.tex` — this is the ground truth for this work's results
4. **Consistency**: ensure expanded content does not contradict the source paper
5. **Terminology**: check against `.claude/rules/vietnamese-terms.md`

## Output Format

```
**Plan saved at:** plans/<chapter>_paper2thesis_plan.md

**Verification report:**
- Citation keys: [OK / MISSING: list]
- Numbers verified against source paper: [OK / MISMATCH: list]
- Terminology: [OK / INCONSISTENT: list]

**Expanded LaTeX content:**
[content]
```
---
name: paper-converting
description: >
  Convert and expand content from the research paper (document/phabert_cnn.tex)
  into thesis format. Use when user says "convert paper", "paper to thesis",
  "chuyển đổi bài báo", "expand from paper", or references converting
  specific paper sections into thesis chapters.
---

# Paper → Thesis Conversion

Convert sections from `document/phabert_cnn.tex` into expanded thesis chapters.
Uses the same Plan→Write→Verify workflow as `/thesis-writing` but with paper-specific guidance.

## Expansion Guidelines

| Paper section | Target chapter | Expansion ratio |
|---------------|---------------|-----------------|
| Introduction | c1 | 2-3x: add background, motivation, research questions, scope |
| Related Work | c2 | 2-3x: add more related papers, deeper comparisons |
| Material & Methods | c3 | 2-3x: add design decisions, rationale, math formulations |
| Experiments | c4 | 2-3x: add ablation studies, deeper analysis, more visualizations |
| Conclusion | c5 | 2x: add limitations, future work, broader impact |

## Process

### Step 1 — Plan (`thesis-planner`)
1. Read the target section from `document/phabert_cnn.tex`
2. Create `plans/<chapter>_paper2thesis_plan.md`:
   - **Expanded outline**: thesis structure (2-3x paper length)
   - **Content to ADD**: what doesn't exist in paper but thesis needs
   - **Content to EXPAND**: what exists but needs more detail
   - **Citation keys**: verify all with `grep` against references.bib
   - **Numbers to verify**: every number, cross-checked against paper
3. Present plan → wait for user confirmation

### Step 2 — Write (`thesis-writer`)

Delegate to the `thesis-writer` agent:
> "Use the thesis-writer agent to write content from the plan [plan file path]"

The agent follows the same writing rules automatically (Vietnamese-first, no copy-paste from paper, expand and rewrite).

### Step 3 — Verify (`citation-verifier`)

Delegate to the `citation-verifier` agent:
> "Use the citation-verifier agent to verify claims in [file]"

Additional checks for paper conversion:
- **Consistency check**: expanded content must not contradict source paper
- **Paraphrasing check**: no sentences directly copied from paper (flag for `/plagiarism-checking`)

## Key Principle

The paper is the GROUND TRUTH for this work's results and methods.
When expanding, you may add explanation and context, but NEVER change
the numbers, claims, or technical descriptions from the paper.

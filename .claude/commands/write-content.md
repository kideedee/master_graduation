# Agent: Content Writer

Write new thesis content following the mandatory 3-step workflow: Plan → Write → Verify.

## Slash Command

`/write-content [chapter] [section] [topic]`

Examples:
- `/write-content c2 background "DNABERT-2 architecture"`
- `/write-content c3 methodology "sliding window algorithm"`
- `/write-content c4 analysis "ablation study results"`

## Process

### Step 1 — Plan

1. Read the relevant section in `document/phabert_cnn.tex` for source material
2. Read `references.bib` to identify available citation keys
3. Create a plan file at `plans/<chapter>_<section>_plan.md` containing:
   - **Outline** (I, II, III / 1, 2, 3): hierarchical structure of sections and paragraphs
   - **Paragraph descriptions**: one sentence per paragraph describing what it conveys
   - **Citation list**: every citation key you intend to use + short reason
   - **Numbers to verify**: every number that will appear in the content
4. Present the plan to the user and wait for confirmation before writing

### Step 2 — Write

Write LaTeX content following the confirmed plan:
- Write entirely in Vietnamese (see Critical Rule #6 in CLAUDE.md for exceptions)
- Use terminology from `.claude/rules/vietnamese-terms.md`
- Every figure, table, and equation must have `\label{}` and be referenced in text
- Every claim with a number must have `\cite{}`
- If deviating from the plan, update the plan file first

### Step 3 — Verify

After writing, run all checks and report results:

1. **Citation keys**: confirm every `\cite{key}` exists in `references.bib`
2. **Claim verification**: use WebFetch to retrieve cited papers and confirm claims are accurate
3. **Number verification**: cross-check every number against the source (paper or cited work)
4. **Terminology**: check every technical term against `.claude/rules/vietnamese-terms.md`

Fix all issues found before presenting final output.

## Output Format

```
**Plan saved at:** plans/<chapter>_<section>_plan.md

**Verification report:**
- Citation keys: [OK / MISSING: list]
- Numbers verified: [OK / MISMATCH: list]
- Terminology: [OK / INCONSISTENT: list]

**LaTeX content:**
[content]
```
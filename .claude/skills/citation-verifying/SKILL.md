---
name: citation-verifying
description: >
  Verify that all citation keys exist in references.bib and that claims match
  the actual papers. Use when user says "verify citations", "check references",
  "kiểm tra trích dẫn", "are my citations correct", or after writing new content.
  Also use proactively before finalizing any chapter.
---

# Citation Verification

This skill addresses the most critical recurring issue: Claude hallucinating citation keys and getting paper claims wrong.

## Phase 1 — Key Existence Check

### Current citation keys used in thesis
!`grep -rohP '\\cite[tp]?\{[^}]+\}' chapters/*/chapter_*.tex 2>/dev/null | grep -oP '\{[^}]+\}' | tr ',' '\n' | sed 's/[{}]//g;s/^ *//;s/ *$//' | sort -u | head -50`

### Available bibliography keys
!`grep -oP '@\w+\{([^,]+)' references.bib | sed 's/@\w\+{//' | sort | head -50`

For the target file(s), extract all `\cite{...}` keys and verify each exists:

```bash
# Extract all citation keys from a chapter
grep -oP '\\cite[tp]?\{[^}]+\}' chapters/cN/*.tex | grep -oP '\{[^}]+\}' | tr ',' '\n' | sed 's/[{}]//g' | sort -u

# Check each key against references.bib
grep -c "KEY" references.bib
```

Report: list of ✓ found / ✗ missing keys.

## Phase 2 — Claim Accuracy Check (`citation-verifier`)

Delegate to the `citation-verifier` agent:
> "Use the citation-verifier agent to verify claims in [file(s)]"

The agent runs in isolated context with WebFetch/WebSearch access and follows a **multi-step fallback chain**:

1. **Landing page** — fetch abstract/DOI page for quick verification
2. **Full paper** — if abstract lacks detail, fetch arXiv HTML (`arxiv.org/html/ID`) or PMC full text with targeted prompts to find exact numbers in Results/Tables
3. **Broad search** — WebSearch for secondary sources (Semantic Scholar, PapersWithCode, reviews), then WebFetch the best result
4. **Final determination** — only mark `⚠ UNABLE TO VERIFY` after exhausting all steps

The agent also handles arXiv IDs embedded in `journal` fields (e.g., `journal={arXiv preprint arXiv:2306.15006}`) which are common in this bibliography.

Cross-checks our results against `document/phabert_cnn.tex` (ground truth).

## Phase 3 — Cross-Reference Consistency

- Same source cited with different keys? → flag duplicate
- Same claim cited differently in different chapters? → flag inconsistency
- Year/author in text contradicts bib entry? → flag mismatch

## Verification Labels

- `✓ VERIFIED` — claim matches paper exactly (from landing page)
- `✓ VERIFIED (via full paper)` — verified by reading full paper content, not just abstract
- `✓ VERIFIED (via secondary source)` — verified through Semantic Scholar, review article, etc.
- `✗ MISMATCH` — specific discrepancy described (e.g., "thesis says 94.2% but paper reports 93.8%")
- `⚠ UNABLE TO VERIFY` — exhausted all steps (landing page → full paper → search); must list what was attempted

## Output Format

```
**File(s) checked:** [list]
**Total citations:** N keys, M unique

**Key existence:**
- ✓ N keys found in references.bib
- ✗ M keys MISSING: [list]

**Claim verification:**
- ✓ VERIFIED: [key] — [brief summary]
- ✗ MISMATCH: [key] — thesis says X, paper says Y
- ⚠ UNABLE TO VERIFY: [key] — [reason]

**Consistency issues:**
- [any cross-reference problems]

**Recommended fixes:**
1. [specific fix for each issue]
```

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

The agent runs in isolated context with WebFetch/WebSearch access, verifies numerical claims against actual papers, cross-checks our results against `document/phabert_cnn.tex`, and returns a structured verification report.

## Phase 3 — Cross-Reference Consistency

- Same source cited with different keys? → flag duplicate
- Same claim cited differently in different chapters? → flag inconsistency
- Year/author in text contradicts bib entry? → flag mismatch

## Verification Labels

- `✓ VERIFIED` — claim matches paper exactly
- `✗ MISMATCH` — specific discrepancy described (e.g., "thesis says 94.2% but paper reports 93.8%")
- `⚠ UNABLE TO VERIFY` — paper not accessible; note what partial info was found

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

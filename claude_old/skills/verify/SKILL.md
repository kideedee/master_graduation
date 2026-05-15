---
name: verify
description: >
  Verify citation keys and claims in thesis files. Use when user says
  "/verify", "check citations", "kiểm tra trích dẫn".
  Example: /verify chapters/c3/chapter_3.tex
argument-hint: "<file-path>"
context: fork
agent: citation-verifier
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch
---

# /verify — Invoke Citation Verifier

Delegate directly to the `citation-verifier` agent.

## Usage

```
/verify [file path]
```

## Behavior

1. If a file path is provided, pass it to the `citation-verifier` agent:
   > "Use the citation-verifier agent to verify claims in [path]"

2. If no path is provided, ask the user which file to verify.

3. The agent will:
   - Find all `\cite{}` keys and verify they exist in `references.bib`
   - WebFetch cited papers to confirm numerical claims
   - Cross-check our results against `document/phabert_cnn.tex`
   - Report: ✓ VERIFIED / ✗ MISMATCH / ⚠ UNABLE TO VERIFY

## After Verification

If mismatches are found, suggest specific fixes with correct numbers from the source papers.
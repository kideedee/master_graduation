---
name: thesis-writing
description: >
  Write new thesis content using the mandatory Plan→Write→Verify workflow.
  Use whenever user asks to write, expand, draft, or add new content to any thesis chapter.
  Also triggers for: "viết nội dung", "thêm phần", "mở rộng", "draft section",
  "write about", or any request to produce LaTeX thesis content.
---

# Thesis Writing — Plan → Write → Verify

Every piece of thesis content MUST go through all 3 steps. Do not skip any step.
Each step delegates to a specialized agent.

## Step 1 — Plan (`thesis-planner`)

Delegate to the `thesis-planner` agent:
> "Use the thesis-planner agent to create a plan for [chapter] [section]: [description]"

The agent reads existing content, references, terminology, and creates a plan in `plans/`.

Present the plan to user. **Wait for confirmation before Step 2.**

## Step 2 — Write (`thesis-writer`)

Delegate to the `thesis-writer` agent:
> "Use the thesis-writer agent to write content from the plan [plan file path]"

The agent reads the confirmed plan, checks terminology, matches existing chapter style, and writes LaTeX directly into the target file.

## Step 3 — Verify (`citation-verifier`)

Delegate to the `citation-verifier` agent:
> "Use the citation-verifier agent to verify claims in [file]"

The agent checks citation keys, verifies numerical claims via WebFetch, and cross-checks our results against `document/phabert_cnn.tex`.

Fix ALL reported issues before presenting final output.

## Validation Loop
After Step 3, ALWAYS verify:
1. `grep -oP '\\cite[tp]?\{[^}]+\}' <file> | sort -u` → check all keys exist in references.bib
2. `pdflatex thesis.tex` → verify compilable without errors
3. If issues found: fix and re-validate. Do NOT report success until both pass.

## Gotchas

- Do NOT invent citation keys — only use keys that exist in `references.bib`.
- When describing other papers' methods, keep descriptions general unless verified via WebFetch.
- Vietnamese terms must be consistent across chapters — agents check `.claude/rules/vietnamese-terms.md` automatically.

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

For the target file(s), extract all `\cite{...}` keys and verify each exists in `references.bib`:

```bash
# Extract all citation keys from a chapter
grep -oP '\\cite[tp]?\{[^}]+\}' chapters/cN/*.tex | grep -oP '\{[^}]+\}' | tr ',' '\n' | sed 's/[{}]//g' | sort -u

# Check each key against references.bib
grep -c "KEY" references.bib
```

Report: list of ✓ found / ✗ missing keys.

## Phase 2 — NotebookLM-based Claim Verification (`citation-verifier`)

Delegate to the `citation-verifier` agent:
> "Use the citation-verifier agent to verify claims in [file(s)]"

The agent uses **NotebookLM** as the verification engine:

### Step A — Locate PDF URL

For each cited key, find a downloadable PDF URL using this priority:

1. **bib `doi` field** → `https://doi.org/<doi_value>`
2. **bib `eprint` field** → `https://arxiv.org/pdf/<eprint_value>`
3. **bib `url` field** → use directly
4. **arXiv ID in `journal`** (regex `arXiv:(\d{4}\.\d{4,5})`) → `https://arxiv.org/pdf/<id>`
5. **No URL in bib → WebSearch** (see below — this is the common case)

#### WebSearch for papers without URL in bib

Search using paper title + first author + year:
```
"<paper title>" <first_author> <year> pdf arxiv pmc
```

From results, prefer in this order:
- **PMC PDF**: `https://www.ncbi.nlm.nih.gov/pmc/articles/<PMCID>/pdf/<filename>.pdf`
- **arXiv PDF**: `https://arxiv.org/pdf/<id>`
- **PMC full text**: `https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/`
- **Open-access publisher**: direct PDF link from journal site

### Step B — Download PDF to local

```bash
# Download paper PDF to /tmp/
curl -L --max-time 60 "<pdf_url>" -o "/tmp/<cite_key>.pdf"
# Verify it's a real PDF (not an HTML error page)
file /tmp/<cite_key>.pdf
```

If `file` reports HTML instead of PDF, the URL redirected to a paywall — try next URL from WebSearch results.

### Step C — Upload PDF to NotebookLM

Upload to notebook ID: `c6a1c52e-4f16-449a-9100-985e8b8b6a9c`

Use `source_add` with:
- `notebook_id`: `c6a1c52e-4f16-449a-9100-985e8b8b6a9c`
- `source_type`: `file`
- `file_path`: `/tmp/<cite_key>.pdf`
- `wait`: `true`

**Before uploading**: check if source already exists in notebook (via `notebook_get`) to avoid duplicates.

### Step D — Query notebook to verify claim

Use `notebook_query` on the notebook:
- `notebook_id`: `c6a1c52e-4f16-449a-9100-985e8b8b6a9c`
- `source_ids`: [just the uploaded source's ID]
- `query`: "Find the exact value of [specific metric/claim]. Quote the exact numbers and the section/table they appear in."

### Step E — Fallback if PDF download fails

If PDF is not downloadable (paywalled, redirect fails):
1. Try `source_add` with `source_type=url` using the arXiv abstract URL
2. If that fails, use WebFetch on arXiv HTML: `https://arxiv.org/html/<id>`
3. Last resort: WebSearch and fetch secondary sources (Semantic Scholar, PapersWithCode)

### For our work (PhaBERT-CNN)

Always verify against `document/phabert_cnn.tex` first — this is the ground truth for all numbers from this research. Do NOT upload our own paper to NotebookLM.

## Phase 3 — Cross-Reference Consistency

- Same source cited with different keys? → flag duplicate
- Same claim cited differently in different chapters? → flag inconsistency
- Year/author in text contradicts bib entry? → flag mismatch

## Verification Labels

- `✓ VERIFIED` — claim matches paper exactly (from NotebookLM query)
- `✓ VERIFIED (via URL source)` — verified via URL source in NotebookLM (no PDF)
- `✓ VERIFIED (via secondary source)` — verified through WebSearch fallback
- `✗ MISMATCH` — specific discrepancy described (e.g., "thesis says 94.2% but paper reports 93.8%")
- `⚠ UNABLE TO VERIFY` — exhausted all steps; must list what was attempted

## Output Format

```
**File(s) checked:** [list]
**Total citations:** N keys, M unique
**NotebookLM notebook:** c6a1c52e-4f16-449a-9100-985e8b8b6a9c

**Key existence:**
- ✓ N keys found in references.bib
- ✗ M keys MISSING: [list]

**Claim verification:**
- ✓ VERIFIED: [key] — [brief summary] (source: NotebookLM query)
- ✗ MISMATCH: [key] — thesis says X, paper says Y
- ⚠ UNABLE TO VERIFY: [key] — [reason; what was attempted]

**Consistency issues:**
- [any cross-reference problems]

**Recommended fixes:**
1. [specific fix for each issue]
```

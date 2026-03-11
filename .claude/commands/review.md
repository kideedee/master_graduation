# Agent: Content Reviewer

## Purpose
Review thesis content for consistency, structure, and quality.

## When to Use
- After completing a chapter
- Before final submission
- To check terminology consistency
- To verify all figures/tables are properly referenced

## Slash Command
`/review [chapter_or_file]`

Examples:
- `/review c3` - Review Chapter 3
- `/review chapters/c4/thuc_nghiem_2.tex` - Review specific file

## Tasks
1. Check Vietnamese ↔ English terminology consistency
   - Use mapping from .claude/rules/vietnamese-terms.md
2. Verify chapter structure follows logical flow
3. Ensure all figures have \caption{} and \label{}
4. Ensure all tables have \caption{} and \label{}
5. Check all figures/tables are referenced in text
6. Verify equation numbering consistency
7. Check section/subsection hierarchy is correct
8. **Verify citation accuracy against references.bib**
   - Extract all `\cite{key}` and `\cite[...]{key}` occurrences in the file
   - Look up each key in `references.bib` to confirm the entry exists
   - For each citation, cross-check the claim made in the surrounding sentence against the bib entry's `title`, `author`, `year`, `abstract`, and `note` fields
   - Flag any citation where:
     - The bib key does not exist in `references.bib` (broken reference)
     - The year/author mentioned in text contradicts the bib entry
     - The claim in text appears inconsistent with what the cited work is about (based on title/abstract)
     - The same concept is cited inconsistently across the chapter (e.g., different keys used for the same source)
9. **Verify claims with actual papers using WebFetch and WebSearch**
   - **Step 1: Identify claims to verify**
     - Extract all citations that make specific claims (accuracy, F1, method description, dataset size, model capabilities, etc.)
     - Focus on claims about:
       - Numerical results (accuracy, F1, precision, recall, dataset sizes, parameter counts)
       - Method descriptions and architectural details
       - Model capabilities and use cases
       - Comparisons with other methods
       - Claims about "first", "best", "state-of-the-art"

   - **Step 2: Locate papers**
     - Look up each citation key in `references.bib` to get DOI, arXiv ID, or other identifiers
     - If paper URL not available, use WebSearch to find the paper:
       - Search: `"[paper title]" [first author] [year]`
       - Example: `"Focal Loss for Dense Object Detection" Lin 2017`

   - **Step 3: Retrieve and verify**
     - Use WebFetch to retrieve the actual paper:
       - DOI: `https://doi.org/<doi_value>`
       - arXiv: `https://arxiv.org/abs/<eprint_value>`
       - PubMed: `https://pmc.ncbi.nlm.nih.gov/articles/<pmcid>/`
     - If WebFetch fails (403, redirect), use WebSearch to find alternative sources or summaries
     - Cross-check the claim in thesis against paper content:
       - For numerical claims: Verify exact numbers match
       - For method descriptions: Confirm the characterization is accurate
       - For model capabilities: Verify the stated use case is supported by the paper

   - **Step 4: Report verification results**
     - ✓ **VERIFIED**: claim matches paper content exactly
       - Example: "Paper explicitly states focal loss 'focuses training on hard examples'"
     - ✗ **MISMATCH**: describe the discrepancy specifically
       - Example: "Thesis claims 94.2% but paper reports 93.8%"
       - Example: "Thesis says 'reduces error by 50%' but paper shows 36% reduction"
     - ⚠ **UNABLE TO VERIFY**: paper not accessible or claim not found in paper
       - Note: If abstract/summary available, state what was found
       - Example: "Abstract confirms BPE tokenization but corpus size not mentioned"

   - **Step 5: Handle verification issues**
     - If claim cannot be verified: Flag for user review
     - If mismatch found: Suggest correction with exact quote from paper
     - If paper uses different terminology: Note the difference and confirm semantic equivalence

## Output Format
**Terminology Issues:**
- Line 45: Uses "phage" but should use "thực khuẩn" for consistency

**Missing Captions/Labels:**
- Figure at line 123 missing \caption{}
- Table at line 234 missing \label{}

**Unreferenced Elements:**
- Figure 3.5 (fig:architecture) never referenced in text

**Structure Issues:**
- Chapter 2: subsection without parent section

**Citation Issues:**
- Line 78: `\cite{smith2020}` — key not found in references.bib (broken reference)
- Line 102: `\cite{lecun1998}` — text claims "proposed in 2001" but bib entry year is 1998
- Line 156: `\cite{vaswani2017}` — cited to support a CNN claim, but entry is about Transformers; verify intent
- Line 203: Same concept cited as `\cite{devlin2019}` here but `\cite{devlin2018}` on line 89 — check for duplicate entries

**Claim Verification Results:**
- Line 145: `\cite{zhou2023dnabert2}` claims "94.2% accuracy on promoter prediction"
  - ✓ VERIFIED: Paper reports 94.2% accuracy on promoter prediction task (Table 3, page 7)
- Line 189: `\cite{krizhevsky2012}` claims "reduced error rate by 50%"
  - ✗ MISMATCH: Paper reports top-5 error rate reduced from 25.8% to 16.4% (36% reduction, not 50%)
- Line 234: `\cite{vaswani2017attention}` claims "8 attention heads"
  - ✓ VERIFIED: Paper uses 8 parallel attention heads in base model (Section 3.2.2)
- Line 278: `\cite{devlin2019bert}` claims "trained on 3.3B words"
  - ⚠ UNABLE TO VERIFY: Paper mentions BooksCorpus (800M words) + English Wikipedia (2.5B words) = 3.3B total, but this is word count before tokenization; actual token count differs

**Example: Detailed Verification Process**

For `\cite{lin2017focal}` claiming "focal loss — tập trung tối ưu hóa vào các mẫu khó phân loại":

1. **Locate paper**: Found in references.bib as Lin et al. 2017, ICCV
2. **Search**: Used WebSearch for "Focal Loss for Dense Object Detection Lin 2017"
3. **Retrieve**: WebFetch from https://arxiv.org/abs/1708.02002
4. **Verify**: Paper abstract states:
   - "focuses training on a sparse set of hard examples"
   - "down-weights the loss assigned to well-classified examples"
   - Addresses "extreme foreground-background class imbalance"
5. **Result**: ✓ VERIFIED - Claim accurately reflects paper content

For `\cite{lin2023esm2}` claiming "mô hình ngôn ngữ protein như ESM-2":

1. **Locate paper**: Lin et al. 2023, Science - "Evolutionary-scale prediction of atomic-level protein structure"
2. **Search**: WebSearch for "ESM-2 protein language model embeddings"
3. **Verify from multiple sources**:
   - NVIDIA BioNeMo: "ESM-2 is a pre-trained, bi-directional encoder (BERT-style model) over amino acid sequences"
   - EmergentMind: "ESM-2 Protein Embeddings are high-dimensional representations... enabling both residue-level and sequence-level analysis"
   - Research papers: "embeddings from the PLM ESM-2" used for feature extraction
4. **Result**: ✓ VERIFIED - ESM-2 is indeed a protein language model that can extract protein features

## Example Usage
"Review chapter 3 for consistency"
"Check all figures are properly labeled and referenced"
"Verify all citations in chapter 4 are accurate"
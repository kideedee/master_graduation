---
name: chapter_1.tex citation verification
description: Full verification record for all 14 citation claims in chapters/c1/chapter_1.tex — two mismatches found
type: reference
---

## Verification Date
2026-05-03

## File Verified
`chapters/c1/chapter_1.tex`

## Results Summary
- Verified: 12
- Mismatch: 2 (suttle2007marine, zhang2024deeppl)
- Unable to verify: 0

---

## Mismatches — Action Required

### MISMATCH 1: suttle2007marine — Wrong population estimate (line 7)
- Thesis claims: `$10^{30}$` individuals
- Paper reports: `$10^{31}$` virus-like particles (Suttle 2007, Nature Reviews Microbiology 5:801-812)
- Fix: Change `$10^{30}$` → `$10^{31}$`
- Source: https://www.nature.com/articles/nrmicro1750

### MISMATCH 2: zhang2024deeppl — Does NOT inherit 4-group length convention (line 37)
- Thesis claims: DeepPL inherited DeePhage's 4-group scheme [100-400, 400-800, 800-1200, 1200-1800 bp]
- Paper reports: DeepPL uses a unified sliding window of 100 bp; does NOT partition sequences into the 4 DeePhage groups. Reports results by sequencer type, not length group.
- Exact quote from paper: "The sequence sizes between 100 to 512 bp were compared in the fine-tuning process. The comparison of different parameters indicated that the sequence size of 100 bp yielded reasonably balanced results with less computing requirements and was further used in the current study."
- Fix: Remove `zhang2024deeppl` from `\cite{shang2023phatyp,zhang2024deeppl}` on line 37. Keep citation on line 23 (list of methods) unchanged.
- Source: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012525

---

## Verified Claims

| cite_key | Claim | Verdict | Source |
|---|---|---|---|
| koskella2014bacteria | phages drive bacterial population regulation and HGT | VERIFIED | academic.oup.com femsre |
| howard2017lysogeny | temperate phages integrate genome as prophage | VERIFIED | academic.oup.com ismej |
| gorski2016phage | phage therapy promising alternative vs antibiotic resistance | VERIFIED | frontiersin.org |
| cobian2016viruses | temperate phages risk transferring ARGs via lysogenic conversion | VERIFIED (secondary source) | WebSearch DOI 10.1146/annurev-virology-100114-054952 |
| shang2023phatyp (claim 6) | traditional methods require lab culture, time-consuming, not for uncultured phages | VERIFIED | academic.oup.com bib bbac487 |
| mokili2012metagenomics | NGS/metagenomics for phage diversity; phages lack 16S rRNA equivalent | VERIFIED (secondary source) | WebSearch DOI 10.1016/j.coviro.2011.12.004 |
| hayes2017metagenomic | existing phage databases limited vs natural diversity | VERIFIED (secondary source) | mdpi.com/1999-4915/9/6/127 (403 direct); bib metadata |
| mcnair2012phacts | PHACTS is feature-based (protein similarity + Random Forest) | VERIFIED | academic.oup.com bioinformatics 28/5/614 |
| hockenberry2021bacphlip | BACPHLIP is feature-based (Pfam domains + Random Forest) | VERIFIED (secondary source) | WebSearch DOI 10.7717/peerj.11396 |
| wu2021deephage | DeePhage deep learning; 4 groups [100-400,400-800,800-1200,1200-1800]; perf depends on length | VERIFIED | gigascience giab056 |
| shang2023phatyp (claim 12) | PhaTYP inherited 4-group convention | VERIFIED | academic.oup.com bib bbac487 |
| zhou2023dnabert | DNABERT-2 is genome foundation model | VERIFIED | arxiv.org/abs/2306.15006 |

---

## Notes on DeepPL for Future Reference
DeepPL (zhang2024deeppl) uses sliding-window 100 bp input, reports by sequencer/assembly type.
It can legitimately be cited in chapter_1.tex line 23 (list of existing methods).
It must NOT be cited for inheriting the 4-group length convention — that claim applies to PhaTYP only.

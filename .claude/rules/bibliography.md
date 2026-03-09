# Bibliography Management

This file contains guidance for managing bibliography and citations in the thesis.

## Adding Bibliography Entries

Add entries to `references.bib` file:

### Journal Article
```bibtex
@article{author2024phage,
  title={Bacteriophage Classification Using Deep Learning},
  author={Author, First and Author, Second},
  journal={Bioinformatics},
  year={2024},
  volume={40},
  number={5},
  pages={1234--1245},
  doi={10.1093/bioinformatics/xyz123}
}
```

### Conference Paper
```bibtex
@inproceedings{author2023bert,
  title={BERT for Genomic Sequences},
  author={Author, First},
  booktitle={Proceedings of NeurIPS},
  year={2023},
  pages={1--10}
}
```

### arXiv Preprint
```bibtex
@misc{author2024arxiv,
  title={Novel Approaches to Phage Classification},
  author={Author, First and Author, Second},
  year={2024},
  eprint={2401.12345},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}
```

### Dataset
```bibtex
@misc{dataset2023,
  title={PhageDB: A Comprehensive Bacteriophage Database},
  author={{PhageDB Consortium}},
  year={2023},
  howpublished={\url{https://phagedb.org}},
  note={Accessed: 2025-01-15}
}
```

### Software/Tool
```bibtex
@misc{pytorch2023,
  title={PyTorch: An Imperative Style, High-Performance Deep Learning Library},
  author={Paszke, Adam and others},
  year={2023},
  howpublished={\url{https://pytorch.org}}
}
```

## Citing in Text

```latex
\cite{author2024phage}              % [1]
\citep{author2024phage}             % (Author et al., 2024)
\citet{author2024phage}             % Author et al. (2024)
\cite{ref1,ref2,ref3}               % [1-3] (with sort&compress)

% Multiple citations with text
As shown in previous studies \cite{ref1,ref2}, ...
```

## After Adding References

1. Run `bibtex thesis` to process bibliography
2. Run `pdflatex thesis.tex` twice to update citations
3. Check that citations appear correctly in PDF

## Verifying Claims Before Citing (Step 3)

Before writing a claim about another paper's results, verify it using WebFetch:

### Verification procedure

1. **Find the paper URL** from the `doi` or `eprint` field in `references.bib`:
   - DOI: `https://doi.org/<doi_value>`
   - arXiv: `https://arxiv.org/abs/<eprint_value>`
   - PubMed: `https://pmc.ncbi.nlm.nih.gov/articles/<pmcid>/`

2. **Use WebFetch** to retrieve the paper and confirm:
   - Does the cited number (accuracy, F1, dataset size...) actually appear in the paper?
   - Does the described method match the claim in the thesis?
   - Do the publication year and authors match the `.bib` entry?

3. **Report results**:
   - OK: claim verified
   - MISMATCH: describe the discrepancy specifically and fix the content

### Example

```
Claim in thesis: "DNABERT-2 achieves 94.2% accuracy on dataset X \cite{zhou2023dnabert2}"
→ WebFetch https://arxiv.org/abs/2306.15006
→ Found: paper reports 94.2% on benchmark Y, not X
→ Fix: correct the dataset name or the number
```


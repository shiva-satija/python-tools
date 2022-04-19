# python-tools
Command line Python Scripts for Bioinformatics Analysis
[![DOI](https://zenodo.org/badge/469747269.svg)](https://zenodo.org/badge/latestdoi/469747269)
# cpgoe.py
GC Content and CpG Dinucleotide ratio calculator:
Calculates GC content and CpG Dinucleotide Observed/Expected ratio of sequences in fasta or multifasta file.(required libraries: Biopython and pandas)

 ``` bash    
$ python cpgoe.py <file.fasta>
```
# rseq.py
Random Sequence Generation tool:
Generates DNA or RNA sequence of user specified length.

Arguments

sequence length= any integer number (example: 100)

molecule type= type 1 for DNA or type 2 for RNA

```bash
$ python rseq.py <sequence length> <molecule type>



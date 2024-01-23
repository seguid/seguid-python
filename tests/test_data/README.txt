This directory contains test data for functions in the test_chksum.py file.

 - README.txt (This file)
 - M13.txt
 - M13_minimal_rotation.txt
 - pUC19.txt
 - pUC19_minimal_rotation_watson_linebreak_crick.txt

---
The M13.txt file contain the 6407 nucleotides circular single stranded DNA genome of the
M13 bacteriophage. The M13 genome sequence is available from the GenBank accession numbers
NC_003287.2 or V00604.2

https://www.ncbi.nlm.nih.gov/nuccore/NC_003287.2
https://www.ncbi.nlm.nih.gov/nucleotide/V00604.2
---
The M13_minimal_rotation.txt contain the DNA 6407 nt M13 ssDNA sequence rotated to its minimum.
This represents the data that is fed into the SHA1 algorithm by the scSEGUID function for the pUC19 sequence.
---
The pUC19.txt file contain the DNA seqence of the pUC19 cloning vector, 2686 bp circular
double stranded DNA. The pUC19 sequence is avaliable from the GenBank accession numbers
M77789.2 or L09130.1.

https://www.ncbi.nlm.nih.gov/nucleotide/M77789.2
https://www.ncbi.nlm.nih.gov/nucleotide/L09130.1
---
The pUC19_minimal_rotation_watson_linebreak_crick.txt contain the smallest of the minimal rotations
of the watson and crick strands, a linebreak and the complementary strand. This represents the
data that is fed into the SHA1 algorithm by the dcSEGUID function for the pUC19 sequence.
---

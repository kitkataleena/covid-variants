from Bio import Align
from Bio import SeqIO
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

seq1_file = "sequences/QHU36824.1.fasta"
seq2_file = "seqeuence/YP_009724390.1(refseq).fasta"

seq1 = str(SeqIO.read(seq1_file, "fasta").seq)
seq2 = str(SeqIO.read(seq2_file, "fasta").seq)

print(seq1)
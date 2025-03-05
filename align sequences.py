from Bio import Align
from Bio import SeqIO
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sequences = list(SeqIO.parse("sequences.fasta"))
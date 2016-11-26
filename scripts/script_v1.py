#author Bartosz Nitkiewicz e-mail: bartosz_at_nitkiewicz_dot_me
from Bio import SeqIO
for seq_record in SeqIO.parse("seq.fasta", "fasta"):
    x = raw_input('--> ')
    if x in seq_record.seq:
        print 'JEST'

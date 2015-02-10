#author Bartosz Nitkiewicz e-mail: bartosz_at_gmail_dot_com
from Bio import SeqIO
for seq_record in SeqIO.parse("seq.fasta", "fasta"):
    x = raw_input('--> ')
    if x in seq_record.seq:
        print 'JEST'

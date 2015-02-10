#author Bartosz Nitkiewicz e-mail: bartosz_at_gmail_dot_com
from Bio import SeqIO
for seq_record in SeqIO.parse("seq.fasta", "fasta"):
    x = raw_input('--> ')
    data = seq_record.seq
    position = data.find(x)
    if position != -1:
        print("Found at position", position)
    else:
        print("Not found")
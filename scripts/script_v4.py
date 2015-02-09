import readline, glob
def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
seq_file = raw_input('Enter file path... ')
sq = open(seq_file)

from Bio import SeqIO
from Bio.Seq import Seq
for seq_record in SeqIO.parse(sq, "fasta"):
    x = raw_input('--> ')
    seq = Seq(x)
    seq_rev = seq.reverse_complement()
    data = seq_record.seq
    position = data.find(seq)
    if position != -1:
        print("Found at position", position)
    else:
        print("Not found")
    position_rev = data.find(seq_rev)
    if position_rev != -1:
        print("Reverse found at position", position_rev)
    else:
        print("Reverse not found")

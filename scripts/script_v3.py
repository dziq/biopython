import readline, glob
def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
seq_file = raw_input('Enter file path... ')
sq = open(seq_file)

from Bio import SeqIO
for seq_record in SeqIO.parse(sq, "fasta"):
    x = raw_input('--> ')
    data = seq_record.seq
    position = data.find(x)
    if position != -1:
        print("Found at position", position)
    else:
        print("Not found")
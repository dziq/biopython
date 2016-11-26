#author Bartosz Nitkiewicz e-mail: bartosz_at_nitkiewicz_dot_me

import string
import re
import sgmllib

from Bio import File
from Bio.WWW import NCBI
result_handle = NCBI.query(search_command, search_database, term = search_term,doptcmdl = return_format)
search_command = 'Search'
search_database = 'Nucleotide'
return_format = 'FASTA'
search_term = 'Cypripedioideae'
my_browser = 'lynx'
import os

result_file_name = os.path.join(os.getcwd(), 'results.html')
result_file = open(result_file_name, 'w')
result_file.write(result_handle.read())
result_file.close()

if my_browser == 'lynx':
    os.system('lynx -force_html ' + result_file_name)
elif my_browser == 'netscape':
    os.system('netscape file:' + result_file_name)

from Bio import SeqIO
for seq_record in SeqIO.parse("seq.fasta", "fasta"):
#    print(seq_record.seq)
    x = raw_input('--> ')
    if x in seq_record.seq:
        print 'JEST'
    #statement(s) = "AAACATGAAGG" in seq_record.seq:
#    if expression:
#        statement(s)
#    else:
#        statement(s)


import sys
Sequence_Length = int(sys.argv[1])#add seq length
molecule= int(sys.argv[2])# DNA or RNA
import random
bases_dna = ['A','T','C','G']
bases_rna = ['A','U','C','G']
if molecule== 1 :
    bases = bases_dna
elif molecule ==2 :
    bases = bases_rna
seq_list= []
for i in range(0,Sequence_Length):
  seq_list.append(random.choice(bases))
chromosome =">"+'seq_random \n'+"".join(seq_list)
print(chromosome)

from string import maketrans
from sys import stdin

if __name__ == '__main__':
    dna_rna_transform = maketrans('T', 'U')
    for line in stdin:
        print(line.translate(dna_rna_transform))

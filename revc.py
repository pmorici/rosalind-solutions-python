from string import maketrans
from sys import stdin

if __name__ == '__main__':
    dna_comp_transform = maketrans('ATCG', 'TAGC')
    for line in stdin:
        print(line[::-1].translate(dna_comp_transform))

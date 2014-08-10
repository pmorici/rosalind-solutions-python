from sys import stdin
from itertools import izip

CODON_TABLE = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V',
               'GUU': 'V', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W',
               'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N',
               'AGU': 'S', 'ACU': 'T', 'CAC': 'H', 'ACG': 'T',
               'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P',
               'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A',
               'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y',
               'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G',
               'UCC': 'S', 'UCA': 'S', 'UAA': '', 'GGA': 'G',
               'UAC': 'Y', 'GAC': 'D', 'GAA': 'E', 'AUA': 'I',
               'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M',
               'UGA': '', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L',
               'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K',
               'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R',
               'CGA': 'R', 'GCU': 'A', 'UAG': '', 'AUU': 'I',
               'UUG': 'L', 'UUA': 'L', 'CGC': 'R', 'UUC': 'F'}

def ianticodon(rna_str):
    """return iterator of anticodons in an ran string"""
    return map(''.join, izip(*[iter(rna_str)]*3))

def codon_transform(anticodons):
    """given an iterable of anticodons return the encoded protein string"""
    return ''.join(map(CODON_TABLE.get, anticodons))

if __name__ == '__main__':
    rna_str = stdin.readline().strip()
    print(codon_transform(ianticodon(rna_str)))

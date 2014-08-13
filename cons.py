from __future__ import print_function
import operator
from sys import stdin
from itertools import izip
from collections import Counter

from gen import parse_fasta

if __name__ == '__main__':
    dna = parse_fasta(stdin)
    profile = []

    for bp in izip(*dna.values()):
        profile.append(Counter(bp))

    consensus = ''.join([ max(p.iteritems(), key=operator.itemgetter(1))[0]
                        for p in profile])

    print(consensus)
    keys = ['A', 'C', 'G', 'T']
    for k in keys:
        print("{0}: ".format(k), end="")
        for p in profile:
            print("{0} ".format(p[k]), end="")
        print("")

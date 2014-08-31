from sys import stdin
import numpy
import operator
from itertools import izip

from gen import parse_fasta

def tuple_math(t1, t2, op):
    """apply the operator to the given tuples t1 and t2 term by term"""
    return tuple(op(a,b) for a,b in izip(t1, t2))

def LCSubstring_dyn(strs):
    """Dynamic programming method of finding the longest common substring.
       This implementation is limited to 32 input strings and uses memory
       on the order of the product of the lengths of the input strings.
    """
    dim = [len(s) for s in strs]
    a = numpy.zeros(dim, numpy.uint16)
    z = 0
    lcs = set()
    ONE = (1,)* len(dim)
    
    for p, x in numpy.ndenumerate(a):
        chrs = [strs[i][p[i]] for i in xrange(len(p))]
        if all([chrs[0] == x for x in chrs]):
            if 0 in p:
                a[p] = 1
            else:
                p1 = tuple_math(p, ONE, operator.sub)
                a[p] = a[p1] + 1
            if a[p] > z:
                z = a[p]
                lcs.clear()
                lcs.add(strs[0][p[0]-z+1:p[0]+1])
            elif a[p] == z:
                lcs.add(strs[0][p[0]-z+1:p[0]+1])
        else:
            a[p] = 0

    return lcs

def LCSubstring_simple(strs):
    """Simple iteration method of finding the longest common substring"""
    short = min(strs)
    strs.remove(short)

    for n in xrange(len(short), 1, -1):
        for i in xrange(0, len(short)-n):
            m_cnt = 0
            sub_str = short[i:i+n]
            for s in strs:
                if sub_str not in s:
                    break
                m_cnt += 1
            if len(strs) == m_cnt:
                return sub_str

    return None
                

if __name__ == '__main__':
    db = parse_fasta(stdin)

    #print LCSubstring_dyn(db.values()).pop()
    print LCSubstring_simple(db.values())

    

    

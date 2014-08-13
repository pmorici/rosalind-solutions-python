from sys import stdin
from itertools import izip

def kmp_table(sub):
    """Compute the kmp table for sub"""
    t = [-1, 0]
    pos = 2
    cnd = 0

    while pos < len(sub):
        if sub[pos-1] == sub[cnd]:
            cnd += 1
            t.append(cnd)
            pos += 1
        elif cnd > 0:
            cnd = t[cnd]
        else:
            t.append(0)
            pos += 1

    return t[:len(sub)]

def kmp_overlap(sub):
    """Find the longest suffix of sub[1:] that is a prefix of sub"""
    overlap = len(sub)
    for i in xrange(len(sub)-1):
        if sub[1+i:] == sub[:-1-i]:
            return len(sub) - (i+1)
    return len(sub) - 1
            

def kmp_search(s, sub, allow_overlap=False):
    """Return a list of all occurances of sub in s.
       Use KMP algorithem as described on Wikipedia;
       http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
       modified to find all sub sequence matches.
    """
    tbl = kmp_table(sub)
    print "table=", tbl
    if allow_overlap:
        sub_overlap = kmp_overlap(sub)
        print "overlap=", sub_overlap

    m = 0
    i = 0
    r = []

    while m+i < len(s):
        if sub[i] == s[m+i]:
            if i == len(sub) - 1:
                r.append(m)
                if allow_overlap:
                    m += len(sub) - sub_overlap
                    i = sub_overlap
                else:
                    i = 0
                    m += len(sub)
            else:
                i += 1
        else:
            if tbl[i] > -1:
                m = m+i-tbl[i]
                i = tbl[i]
            else:
                i = 0
                m = m+1
    return r

def search(s, sub, allow_overlap=False):
    """naieve search of s for sub"""
    r = []
    i = 0;
    
    try:
        while(i+len(sub) < len(s)):
            r.append(s.index(sub, i))
            if allow_overlap:
                i = r[-1] + 1
            else:
                i = r[-1] + len(sub)
    except ValueError:
        pass
    
    return r

if __name__ == '__main__':
    dna_s = stdin.readline().strip()
    dna_t = stdin.readline().strip()

    idx = kmp_search(dna_s, dna_t, True)

    idx = map(lambda x: str(x+1), idx)
    print(' '.join(idx))

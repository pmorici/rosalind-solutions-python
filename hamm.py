from sys import stdin
from itertools import imap
from collections import Counter

if __name__ == '__main__':
    
    s = stdin.readline().strip()
    t = stdin.readline().strip()

    # Counter difference between two strings
    dh = Counter(imap(lambda a, b:a!=b, s, t))[True]
    print(dh)

from sys import stdin
from itertools import imap
import operator

if __name__ == '__main__':
    Pr = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    c = [int(x) for x in stdin.readline().split()]

    Ex = sum(imap(operator.mul, Pr, c)) * 2

    print Ex
    

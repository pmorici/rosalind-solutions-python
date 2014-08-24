from sys import stdin

def rabbit_mpop(n, m):
    """return rabbits alive after n months if they live for m months.
         Fn = Fn-1 + Fn-2 - Fn-m-1
    """
    h = [0] * (m-2) + [1,1,1]

    if n < 2:
        return 1
    if m < 2:
        return 0

    for g in xrange(2, n):
        h.append(h[-1] + h[-2] - h[-(m+1)])
        h.pop(0)

    return h[-1]
        
if __name__ == '__main__':
    n, m = [int(x) for x in stdin.readline().split()]

    print rabbit_mpop(n, m)

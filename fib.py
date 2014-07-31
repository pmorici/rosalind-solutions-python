from sys import stdin

def rabbit_pop(n, k):
    """Return rabbit pairs after n month with k rabbits per litter"""
    f1 = 1
    f2 = 1
    if n <= 2:
        return 1
    while n > 2:
        g = (f1*k)+f2
        f1 = f2
        f2 = g
        n -= 1
    return f2

if __name__ == '__main__':
    argv = [int(arg) for arg in stdin.read().split()]
    print("{0}".format(rabbit_pop(*argv)))

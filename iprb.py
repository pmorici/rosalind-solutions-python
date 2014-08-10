from sys import stdin

def phenotype_probability(k,m,n):

    p = k+m+n

    b1 = k/p
    b2 = m/p
    b3 = n/p

    p -= 1
    t = {}
    t['b1_1'] = (k-1)/p * b1
    t['b1_2'] = m/p * b1
    t['b1_3'] = n/p * b1

    t['b2_1'] = k/p * b2
    t['b2_2'] = (m-1)/p * b2 * .75
    t['b2_3'] = n/p * b2 * .5

    t['b3_1'] = k/p * b3
    t['b3_2'] = m/p * b3 *.5
    t['b3_3'] = (n-1)/p* b3 * 0

    return sum(t.values())

if __name__ == '__main__':
    p = phenotype_probability(*[float(x) for x in stdin.readline().split()])
    
    print(p)

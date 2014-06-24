from collections import Counter
import sys

if __name__ == '__main__':
    c = Counter()

    for line in sys.stdin:
        c.update(line.strip())

    print("{A} {C} {G} {T}".format(**c))

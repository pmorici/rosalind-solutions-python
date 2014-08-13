from collections import Counter
from sys import stdin
from gen import parse_fasta

def gc_content(dna_str):
    """return the gc content expressed as a %"""
    c = Counter(dna_str)
    return (c['G'] + c['C']) / float(sum(c.values())) * 100

if __name__ == '__main__':

    dna_db = parse_fasta(stdin)
    gc_db = {dna_id:gc_content(dna) for dna_id, dna in dna_db.iteritems()}

    max_gc = max(gc_db.iteritems(), key=lambda x:x[1])

    print("{0}\n{1}".format(*max_gc))
        

    
        

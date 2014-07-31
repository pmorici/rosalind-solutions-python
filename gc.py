from collections import Counter
from sys import stdin

def gc_content(dna_str):
    """return the gc content expressed as a %"""
    c = Counter(dna_str)
    return (c['G'] + c['C']) / float(sum(c.values())) * 100

def parse_fasta(filein):
    """given a file stream return a dictionary of id:dna mappings"""
    dna_id = None
    dna_strs = ''
    dna_db = {}

    for line in stdin:
        if line.startswith('>'):
            if dna_id is not None:
                dna_db[dna_id] = ''.join(dna_strs)
            dna_id = line[1:].strip()
            dna_strs = []
        else:
            dna_strs.append(line.strip())
    if dna_id is not None:
        dna_db[dna_id] = ''.join(dna_strs)

    return dna_db

if __name__ == '__main__':

    dna_db = parse_fasta(stdin)
    gc_db = {dna_id:gc_content(dna) for dna_id, dna in dna_db.iteritems()}

    max_gc = max(gc_db.iteritems(), key=lambda x:x[1])

    print("{0}\n{1}".format(*max_gc))
        

    
        

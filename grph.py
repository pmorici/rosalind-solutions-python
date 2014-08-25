from sys import stdin
from gen import parse_fasta

def o3_adj(dna_db):
    """return the O3 Adjacency List"""
    o3 = []
    
    for s_id, s in dna_db.iteritems():
        suffix = s[-3:]
        
        for t_id, t in dna_db.iteritems():
            if t.startswith(suffix) and s_id != t_id:
                o3.append((s_id, t_id,))

    return o3
    

if __name__ == '__main__':
    dna = parse_fasta(stdin)
    o3 = o3_adj(dna)

    for e in o3:
        print e[0], e[1]

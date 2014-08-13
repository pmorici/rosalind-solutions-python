"""Common functions"""

def parse_fasta(filein):
    """given a file stream return a dictionary of id:dna mappings"""
    dna_id = None
    dna_strs = ''
    dna_db = {}

    for line in filein:
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
    pass

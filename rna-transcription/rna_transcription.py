import re
def to_rna(dna_strand):
    length_passed = len(dna_strand)
    dna_strand = re.sub(r'[^ACGT]', r'', dna_strand)
    length_trimmed = len(dna_strand)
    if not length_trimmed == length_passed:
        return ''
    dna_strand = re.sub(r'[G]', r'C', dna_strand)
    dna_strand = re.sub(r'[C]', r'G', dna_strand)     
    dna_strand = re.sub(r'[T]', r'A', dna_strand)
    dna_strand = re.sub(r'[A]', r'U', dna_strand) 
    return dna_strand
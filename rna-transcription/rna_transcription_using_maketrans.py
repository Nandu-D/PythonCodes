import re
def to_rna(dna_strand):
    length_passed = len(dna_strand)
    dna_strand = re.sub(r'[^ACGT]', r'', dna_strand)
    length_trimmed = len(dna_strand)
    if not length_trimmed == length_passed:
        return ''
    translation_mapping = str.maketrans('GCTA','CGAU')   
    dna_strand = dna_strand.translate(translation_mapping)
    return dna_strand
    
if __name__ =='__main__':
    dna = input('Enter DNA : ')
    print('RNA : {0}'.format(to_rna(dna)))

    import re
    def to_rna(dna_strand):
        length_passed = len(dna_strand)
        dna_strand = re.sub(r'[^ACGT]', r'', dna_strand)
        length_trimmed = len(dna_strand)
        if not length_trimmed == length_passed:
            return ''
        list_dna_strand = list(dna_strand)
        for i in range(length_passed):
            if list_dna_strand[i] == 'G':
                list_dna_strand[i] = 'C'
            elif list_dna_strand[i] == 'C':
                list_dna_strand[i] = 'G'   
            elif list_dna_strand[i] == 'T':
                list_dna_strand[i] = 'A'
            else:
                list_dna_strand[i] = 'U'
        dna_strand = ''.join(list_dna_strand)      
        return dna_strand
    
    if __name__ =='__main__':
        dna = input('Enter DNA : ')
        print('RNA : {0}'.format(to_rna(dna)))

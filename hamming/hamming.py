def distance(str1,str2):
    if len(str1) == len(str2):
        count = 0
        for i in range(len(str1)):
            if not str1[i] == str2[i]:
                count = count + 1
        return count
    else:
        raise ValueError()
         
    
if __name__ =='__main__':
    dna1 = input('Enter DNA-1 : ')
    dna2 = input('Enter DNA-2 : ')
    print(distance(dna1, dna2))

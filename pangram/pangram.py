import re
from string import ascii_lowercase

def is_pangram(sentence):
    sentence = re.sub(r'[^a-zA-Z]',r'', sentence)
    sentence = sentence.lower()
    for a_z in ascii_lowercase:
        if not a_z in sentence:
            return False
    return True   
    
if __name__ == '__main__' :
    line = input('Enter the sentence : ')
    print(is_pangram(line)) 
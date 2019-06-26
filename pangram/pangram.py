import string
import re

def is_pangram(sentence):
    #declare abecedary
    abecedary = string.ascii_lowercase
    #clean sentence(quit whiteaspaces and converts string to lowercase)
    cleanit = sentence.strip(string.punctuation).replace(" ","").lower()
    #clean sentence step 2 I use set and regular expression (quit numbers and underscores)
    unique = set(re.sub('[0-9_-]+', '', cleanit))
    #compare length between unique and abecedary
    if len(unique) == len(abecedary):
        return True
    else:
        return False




import re
def abbreviate(words):
    # re.sub matches with non alphabetical character, after clean, split
    clean = re.sub('[^A-Za-z0-9\']+', ' ', words).split()
    return("".join(word[0].upper() for word in clean))
    

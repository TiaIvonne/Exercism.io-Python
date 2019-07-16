def is_isogram(string):
    clean = [string.lower() for string in string if string.isalpha()]
    if len(clean) == len(set(clean)):
        return True
    else:
        return False

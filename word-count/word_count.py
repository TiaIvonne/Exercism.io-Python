from collections import Counter
import re
def count_words(sentence):
    # clean sentence, converts sentence to lowercase, find d+ digits w+ for letters and ''
    words = re.findall(r"\d+|\w+'?\w+", sentence.lower().replace('_',' '))
    return Counter(words)

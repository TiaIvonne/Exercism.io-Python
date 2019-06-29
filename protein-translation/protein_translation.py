## map all values
## codon -> protein
## import regular expression module
import re
proto = {
    'AUG':['Methionine'],
    'UUU':['Phenylalanine'],
    'UUC':['Phenylalanine'],
    'UUA':['Leucine'],
    'UUG':['Leucine'],
    'UCU':['Serine'],
    'UCC':['Serine'],
    'UCA':['Serine'],
    'UCG':['Serine'],
    'UAU':['Tyrosine'],
    'UAC':['Tyrosine'],
    'UGU':['Cysteine'],
    'UGC':['Cysteine'],
    'UGG':['Tryptophan'],
    }


def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x


def proteins(strand):
    """
    ask proto dictionary which protein matches a given codon/strand
    """
    matches = []
    # take a strans and divides in 3 sub-strands
    identify_strand = re.findall(r'\w{3}', strand)
    # code stop if strand UAA UAG or UGA appears
    stop = ['UAA','UAG','UGA']
    # looping dictionary
    for strand in identify_strand:
        try:
            if strand in stop:
                break
            extract_protein = "".join(proto[strand])
            matches.append(extract_protein)
        except KeyError:
            pass
    return unique_list(matches)

def distance(strand_a, strand_b):
    # start count
    count = 0
    # compare len a and b, if is not coincidence, raise an error
    if len(strand_a) == len(strand_b):
        # with zip compares strands(both) and then evaluate differences
        for i, j in zip(strand_a, strand_b):
            if i != j:
                count +=1
    else:
        # value error
        raise ValueError (strand_a + "does not match" + strand_b)
    return count 
def distance(strand_a, strand_b):
    dist = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Error strings need to be the same length")

    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            dist += 1
    return dist






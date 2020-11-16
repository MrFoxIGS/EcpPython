def to_comp(dna_strand):
    new_strand = ""
    for letter in dna_strand:
        if letter == "G":
            new_strand = new_strand + "C"
        elif letter == "C":
            new_strand = new_strand + "G"
        elif letter == "T":
            new_strand = new_strand + "A"
        elif letter == "A":
            new_strand = new_strand + "T"
    return new_strand

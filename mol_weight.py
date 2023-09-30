def protein_mass(seq: str):
    "Counts molecular weight of the protein"
    count = 0
    for amino in seq:
        if amino == "A":
            count += 89
        elif amino == "R":
            count += 174
        elif amino == "N":
            count += 132
        elif amino == "V":
            count += 117
        elif amino == "H":
            count += 155
        elif amino == "G":
            count += 75
        elif amino == "Q":
            count += 146
        elif amino == "E":
            count += 147
        elif amino == "I":
            count += 131
        elif amino == "L":
            count += 131
        elif amino == "K":
            count += 146
        elif amino == "M":
            count += 149
        elif amino == "P":
            count += 115
        elif amino == "S":
            count += 105
        elif amino == "Y":
            count += 181
        elif amino == "T":
            count += 119
        elif amino == "W":
            count += 204
        elif amino == "F":
            count += 165
        else:
            count += 133
    return count
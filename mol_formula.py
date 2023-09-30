def protein_formula(seq: str):
    "Returns molecular formula of the protein"
    fС = 0
    fH = 0
    fN = 0
    fO = 0
    fS = 0
    for amino in seq:
        if amino == "A":
            fС += 3
            fH += 7
            fN += 1
            fO += 2
            fS += 0
        elif amino == "R":
            fС += 6
            fH += 14
            fN += 4
            fO += 2
            fS += 0
        elif amino == "N":
            fС += 4
            fH += 8
            fN += 2
            fO += 3
            fS += 0
        elif amino == "V":
            fС += 5
            fH += 11
            fN += 1
            fO += 2
            fS += 0
        elif amino == "H":
            fС += 6
            fH += 9
            fN += 3
            fO += 2
            fS += 0
        elif amino == "G":
            fС += 2
            fH += 5
            fN += 1
            fO += 2
            fS += 0
        elif amino == "Q":
            fС += 5
            fH += 10
            fN += 2
            fO += 3
            fS += 0
        elif amino == "E":
            fС += 5
            fH += 9
            fN += 1
            fO += 4
            fS += 0
        elif amino == "I":
            fС += 6
            fH += 13
            fN += 1
            fO += 2
            fS += 0
        elif amino == "L":
            fС += 6
            fH += 13
            fN += 1
            fO += 2
            fS += 0
        elif amino == "K":
            fС += 6
            fH += 14
            fN += 2
            fO += 2
            fS += 0
        elif amino == "M":
            fС += 5
            fH += 11
            fN += 1
            fO += 2
            fS += 1
        elif amino == "P":
            fС += 5
            fH += 9
            fN += 1
            fO += 2
            fS += 0
        elif amino == "S":
            fС += 3
            fH += 7
            fN += 1
            fO += 3
            fS += 0
        elif amino == "Y":
            fС += 9
            fH += 11
            fN += 1
            fO += 3
            fS += 0
        elif amino == "T":
            fС += 4
            fH += 9
            fN += 1
            fO += 3
            fS += 0
        elif amino == "W":
            fС += 11
            fH += 12
            fN += 2
            fO += 2
            fS += 0
        elif amino == "F":
            fС += 9
            fH += 11
            fN += 1
            fO += 2
            fS += 0
        else:
            fС += 4
            fH += 7
            fN += 1
            fO += 4
            fS += 0
    if fS == 0:
        aa_formula = f'С: {fС}, H: {fH}, N: {fN}, O:{fO}'
    else:
        aa_formula = f'С: {fС}, H: {fH}, N: {fN}, O:{fO}, S: {fS}'
    return aa_formula
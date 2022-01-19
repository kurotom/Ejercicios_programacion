"""
Encontrar diferencias entre dos cadenas de ADN, demarcando las diferencias en B.

We read DNA using the letters C,A,G and T. Two strands might look like this:
    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    ^ ^ ^  ^ ^    ^^
"""


def distance(strand_a, strand_b):
    faltantes = 0
    if strand_a == "" or strand_b == "":
        assert ValueError("No contienen datos")
    if len(strand_a) != len(strand_b):
        raise ValueError("No tienen la misma longitud")

    for a in enumerate(strand_a):
        if a[1] != strand_b[a[0]]:
            faltantes += 1
    return faltantes


print(distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
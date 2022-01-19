"""
Given a DNA strand, return its RNA complement (per RNA transcription).
Both DNA and RNA strands are a sequence of nucleotides.
The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
    G -> C
    C -> G
    T -> A
    A -> U
"""


def to_rna(dna_strand):
    transcription_dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    result = ""
    for dna in dna_strand:
        for dna_nucleo in transcription_dna_to_rna.keys():
            if dna == dna_nucleo:
                result += transcription_dna_to_rna.get(dna_nucleo)
    return result


print(to_rna("GCTAATCG")) # CGAUUAGC


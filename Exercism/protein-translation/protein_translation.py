"""
Translate:

RNA: "AUGUUUUCU" =>
Codons: "AUG", "UUU", "UCU" =>
Protein: "Methionine", "Phenylalanine", "Serine"

RNA: "AUGUUUUCUUAAAUG" =>
Codons: "AUG", "UUU", "UCU", "UAA", "AUG" =>
Protein: "Methionine", "Phenylalanine", "Serine"

    "UAA" => terminates the translation
"""


def proteins(strand):
    std_gen_code = {'Alanine': ('GCU', 'GCC', 'GCA', 'GCG'), 'Arginine': ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
     'Asparagine': ('AAU', 'AAC'), 'Aspartic acid': ('GAU', 'GAC'), 'Cysteine': ('UGU', 'UGC'),
     'Glutamic acid': ('GAA', 'GAG'), 'Glutamine': ('CAA', 'CAG'), 'Glycine': ('GGU', 'GGC', 'GGA', 'GGG'),
     'Histidine': ('CAU', 'CAC'), 'Isoleucine': ('AUU', 'AUC', 'AUA'),
     'Leucine': ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'), 'Lysine': ('AAA', 'AAG'), 'Methionine': 'AUG',
     'Phenylalanine': ('UUU', 'UUC'), 'Proline': ('CCU', 'CCC', 'CCA', 'CCG'),
     'Serine': ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'), 'Threonine': ('ACU', 'ACC', 'ACA', 'ACG'),
     'Tryptophan': 'UGG', 'Tyrosine': ('UAU', 'UAC'), 'Valine': ('GUU', 'GUC', 'GUA', 'GUG')}

    divide_cod_gen = []
    result_translation = []

    for i in range(0, len(strand), 3):
        if strand[i:i+3] == "UAA" or strand[i:i+3] == "UAG" or strand[i:i+3] == "UGA":
            break
#        print(strand[i:i+3])
        if strand[i:i + 3] not in divide_cod_gen:
            divide_cod_gen.append(strand[i:i + 3])
#    print(divide_cod_gen)

    for cod_amino in divide_cod_gen:
        for name_amino, cod_std_amino in list(std_gen_code.items()):
            if cod_amino in cod_std_amino:
                result_translation.append(name_amino)
#                print(name_amino, cod_std_amino, cod_amino)
    return result_translation


print(proteins("AUGUUUUCU")) # "AUG", "UUU", "UCU" => ["Methionine", "Phenylalanine", "Serine"]
print(proteins("AUGUUUUCUUAAAUG")) # "AUG", "UUU", "UCU", "UAA", "AUG" => ["Methionine", "Phenylalanine", "Serine"]
print(proteins("UGGUAG")) # ['Tryptophan']
print(proteins("UGGUGUUAUUAAUGGUUU")) # ["Tryptophan", "Cysteine", "Tyrosine"]
# UGG UGU UAU UAA UGG UUU

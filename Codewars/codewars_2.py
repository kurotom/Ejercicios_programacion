# -*- coding: utf-8 -*-
"""
El objetivo de este ejercicio es convertir una cadena en una nueva cadena donde cada carácter de la nueva cadena es
"(" si ese carácter aparece solo una vez en la cadena original, o ")" si ese carácter aparece más de una vez en el
original cuerda. Ignora las mayúsculas al determinar si un personaje es un duplicado.
"""

"""
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""

pal = "lGeFxH(S"
final = []


def duplicate_encode(word):
    final = []
    word = word.lower()
    for x in word:
        if word.count(x) == 1:
            final.append("(")
        elif word.count(x) > 1:
            final.append(")")
    return "".join(final)




print(duplicate_encode(pal))

print(len(duplicate_encode(pal)))
print(len(pal))

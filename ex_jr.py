# Invertir cadena

cadena = 'abcd'
print(cadena[::-1])
print()
print()
print()

# contar repeticiones carácter

repeticiones = 'abcdeeeab'
dict_rep = dict()
for i in repeticiones:
    if i not in dict_rep:
        dict_rep[i] = repeticiones.count(i)
print(dict_rep)
print()
print()
print()


# distancia hamming

def hamming(a,b):
    a1 = str(a)
    b1 = str(b)
    x = 0
    index = []
    for i in range(len(a1)):
        if a1[i] != b1[i]:
            x += 1
            index.append(i)
    return 'totalDiff', x, 'location', index

print(hamming(1011101, 1001001))
print(hamming(2143896, 2233796))
print(hamming("tener", "reses"))
print(hamming(1111111, 1111111))
print()
print()
print()


# contador de palabras

def countWord(texto):
    excluded = '!"#$%&\'()*+,-./:;<=>?@[\]^_\`{|}~'
    txt = texto.split()
    count = dict()
    x = 0
    for i in txt:
        if i not in excluded:
            x += 1
            count[i.lower()] = count.get(i.lower(), 0) + 1

    return count


text = """
La noche estrellada es un óleo sobre lienzo del pintor postimpresionista neerlandés Vincent van Gogh . Pintado en junio de 1889, representa la vista desde la ventana orientada al este de su habitación de asilo en Saint-Rémy-de-Provence, justo antes del amanecer, con la adición de un pueblo imaginario. Ha estado en la colección permanente del Museo de Arte Moderno de la ciudad de Nueva York desde 1941, adquirida a través de Lillie P. Bliss Bequest . Ampliamente considerada como la obra maestra de Van Gogh, La noche estrellada es una de las pinturas más reconocidas en la historia de la cultura occidental.
"""

print(countWord(text))
print()
print()
print()

# contar carácteres por tipo numero en una cadena

def cnt(item):
    it = item.split()
    total = 0
    for i in it:
        if i.isnumeric():
            for x in i:
                total += 1
    return f'Numbers total: {total}'

itm = '20 de septiembre de 1889'
print(cnt(itm))


# encontrar prefijos comunes en el array
# 'none' en caso de no encontrar

def profijos(array):
    resultado = 'none'
    p = array[0]
    i = 1
    l = False
    while i < len(p):
        if l == True:
            break
        else:
            i += 1
        h = 1
        for x in array:
            if p[:i] in x:
                if h == 3:
                    resultado = p[:i]

                h += 1
            else:
                l = True
                break
    return resultado


lista = ['flower', 'car', 'dog']
print(profijos(lista))

lista = ['flower', 'flow', 'flac']
print(profijos(lista))

lista = ['car', 'card', 'catridge']
print(profijos(lista))

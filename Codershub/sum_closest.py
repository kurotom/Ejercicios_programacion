"""
Escribe una función que, dada una lista ordenada de números y un número adicional x, devuelva una lista de dos números
cuya suma sea la más cercana al número x.
Por ejemplo:
    find_closest([10, 22, 28, 29, 30, 40], 54) = (22,30) porque su suma es 52 y es lo más cercano a 54.

Nota:
la solución debe estar en tiempo lineal.
"""


def findClosest(list , x):
    print(list, x)
    l = 0
    for i in range(len(list)):
        for x in list:
            print(list[l])
            l += 1
    return ''


l = [10, 22, 28, 29, 30, 40]
print(findClosest(l, 54))
# (22,30) porque su suma es 52 y es lo más cercano a 54.
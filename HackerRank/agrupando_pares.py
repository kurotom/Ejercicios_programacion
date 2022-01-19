# -*- coding: utf-8 -*-
"""
John trabaja en una tienda de ropa. Tiene una gran pila de calcetines que debe combinar por color para la venta. Dada
una serie de enteros que representan el color de cada calcetín, determine cuántos pares de calcetines con colores
coincidentes hay.
Por ejemplo, hay "n = 7" calcetines con colores "ar = [1, 2, 1, 2, 3, 2]. Hay un par de color "1" y uno de color "2".
Quedan tres calcetines impares, uno de cada color. El número de pares es "2".

La función "sockMerchant" tiene los siguientes parámetros:
     n: el número de calcetines en la pila
     ar: los colores de cada calcetín

Entrada:
La primera línea contiene un número entero "n", el número de calcetines.
La segunda línea contiene enteros "n" separados por espacios que describen los colores "ci" de los calcetines en la pila.

Salida:
Imprime el número total de pares de calcetines que John puede vender.

"""

"""
Entrada:
15

Entrada
6 5 2 3 5 2 2 1 1 5 1 3 3 3 5

Salida:
6
"""


def sockMerchant(n, ar):
    repite = []
    sorted(ar)
    for i in sorted(ar):
        c = sorted(ar).count(i)
        if (i, c) not in repite:
            repite.append((i, c))
    a = 0
    for x in repite:
        a += (x[1] // 2)
    return a


n = 15
ar = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]

result = sockMerchant(n, ar)

print(result)

# -*- coding: utf-8 -*-
"""
Cuenta las cantidades de ocurrencias de "1" de la conversion base 10 a binario (2).
"""

# Numero entero natural.
n = int(input())
# rango permitido.
if 1 <= n <= 1000000:
    # Convierte base 10 a binario, excluyendo el inicio, formato str.
    x = (bin(n)[2:])
    # Cuenta ocurrencias de 1 excluyendo los 0.
    i = 0
    for a in x:
        if a != "0":
            i += 1
    print("Ocurrencias de 1: {}".format(i))

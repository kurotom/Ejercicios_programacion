# -*- coding: utf-8 -*-

s = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

lista = []
mn = []
final = []

for x in s:
    lista.append([x[0], x[1]])

for x in lista:
    mn.append(x[1])

for x in lista:
    if x[1] != min(mn):
        final.append(x[1])

for x in sorted(lista):
    if x[1] == min(final):
        print(x[0])



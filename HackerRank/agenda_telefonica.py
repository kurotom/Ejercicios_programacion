# -*- coding: utf-8 -*-
#3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry


n = int(input())
contactos = {}
if 1 <= n <= 100000:
    for _ in range(n):
        numero = input().split()
        contactos[numero[0]] = numero[1]

for x in range(n):
    nombre = input()
    if nombre not in contactos:
        print("Contacto no existe")
    else:
        print("{}={}".format(nombre, contactos[nombre]))









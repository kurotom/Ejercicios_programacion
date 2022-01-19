# -*- coding: utf-8 -*-
"""
Intento Juego
"""

import random


def enemigo(x):
    posibilidad = (50 * x) / 100
    if x == aleatorio(posibilidad):
        print("Te encontraste a un enemigo!")
        if input("Escapar? s/n: ") == "s":
            print("Sales corriendo en sentido opuesto de tu enemigo")
        else:
            print("Intentas pelear con todo, pero el enemigo es muy fuerte y mueres")


aleatorio = random.randrange

w = 0
s = 0
a = 0
d = 0

while True:
    sel = input(">>>: ")
    if sel == "*":
        break
    if sel == "w":
        w += 1
        print("Avanzas un espacio hacia adelante", w)
        enemigo(w)
    elif sel == "s":
        s += 1
        print("Avanzas un espacio hacia atras", s)
        enemigo(s)
    elif sel == "a":
        a += 1
        print("Avanzas un espacio hacia la izquierda", a)
        enemigo(a)
    elif sel == "d":
        d += 1
        print("Avanzas un espacio hacia la derecha", d)
        enemigo(d)
    else:
        pass


# -*- coding: utf-8 -*-
"""
Un cuadrado de cuadrados

Te gustan los bloques de construcción. Te gustan especialmente los bloques de construcción que son cuadrados. Y lo que
más te gusta es ¡organízalos en un cuadrado de bloques de construcción cuadrados!

Sin embargo, a veces, no puede organizarlos en un cuadrado. ¡En cambio, terminas con un rectángulo ordinario! Los
malditos ¡cosas! Si solo tuvieras una manera de saber, si actualmente estás trabajando en vano ... ¡Espera! ¡Eso es!
Solo tienes que comprobar si tu número de bloques de construcción es un cuadrado perfecto.

####    Tarea   ####
Dado un número integral, determine si es un número cuadrado:
    En matemáticas, un número cuadrado o cuadrado perfecto es un número entero que es el cuadrado de un número entero;
    en otras palabras, Es el producto de algún número entero consigo mismo.

Las pruebas siempre usarán algún número integral, así que no se preocupe por eso en los lenguajes dinámicos.

Examples

isSquare(-1) returns  false
isSquare(0) returns   true
isSquare(3) returns   false
isSquare(4) returns   true
isSquare(25) returns  true
isSquare(26) returns  false
"""

import math


def isSquare(n):
    if len(str(math.sqrt(n))) == 3:
        return True
    return False


#print(isSquare(-1))
#print(isSquare(0))
print(isSquare(25))
#print(isSquare(26))

# -*- coding: utf-8 -*-
"""
¡Tu biblioteca local necesita tu ayuda! Dadas las fechas de devolución esperadas y reales para un libro de la
biblioteca, cree un programa que calcule la multa (si corresponde). La estructura de tarifas es la siguiente:

1)  Si el libro se devuelve en la fecha de devolución prevista o antes, no se aplicará ninguna multa.
    Multa = 0

2)  Si el libro se devuelve después del día de devolución esperado pero aún dentro del mismo mes calendario y año que
la fecha de devolución esperada.
    Multa = 15 Hackos x (dias de retraso)

3)  Si el libro se devuelve después del mes de devolución esperado pero aún dentro del mismo año calendario que la fecha
de devolución esperada.
    Multa = 500 Hackos x (meses de retraso)

4)  Si el libro se devuelve después del año calendario en el que se esperaba, hay una multa fija.
    10000 Hackos

Input:
    Formato dia entregado:  "dia" "mes" "año"
    Formato dia entrega:    "dia" "mes" "año"

Output:
    Imprimir un entero unico entregado costo de multa.

Ejemplo:
    Input:
            9 6 2015
            6 6 2015
    Output:
            45
"""

import datetime
import calendar


def fecharetraso(devuelto, vencimiento):
    #                   AÑO             MES         DIA
    dvt = datetime.date(devuelto[0], devuelto[1], devuelto[2])
    lmt = datetime.date(vencimiento[0], vencimiento[1], vencimiento[2])
    diasanual = datetime.date(vencimiento[0], 12, 31).timetuple().tm_yday
    mesdia = calendar.monthrange(devuelto[0], devuelto[1])[1]
    dias = (dvt - lmt).days
    if calendar.isleap(devuelto[0]) is True:
        if dias <= 0:
            #   1
            print("Modulo 1")
            print(0)
        elif dias < mesdia and dias < diasanual:
            #   2
            print("Modulo 2")
            print(15 * dias)
        elif mesdia < dias < 366:
            #   3
            print("Modulo 3")
            print(500 * (dias//30))
        else:
            print(10000)
    else:
        if dias <= 0:
            #   1
            print("Modulo 1-1")
            print(0)
        elif dias < mesdia and dias < diasanual:
            #   2
            print("Modulo 2-1")
            print(15 * dias)
        elif mesdia < dias < 365:
            #   3
            print("Modulo 3-1")
            print(500 * (dias//30))
        else:
            print(10000)

#    print("-----------------------")
#    print(dias, mesdia, dias, diasanual, datetime.date(devuelto[2], 12, 31).timetuple().tm_yday)
#    print(calendar.isleap(devuelto[2]))
#    print(devuelto[1], dias, mesdia)
#    print(dvt - lmt)


def comprobar(fecha):
    dia, mes, anio = fecha
    if 1 <= int(dia) <= 31:
        if 1 <= int(mes) <= 12:
            if 1 <= int(anio) <= 3000:
                return [int(anio), int(mes), int(dia)]
    else:
        return "Maximos:\nDias: 31\nMes: 12\nAño: 3000"


entregado = input().split()
limite = input().split()
fecharetraso(comprobar(entregado), comprobar(limite))


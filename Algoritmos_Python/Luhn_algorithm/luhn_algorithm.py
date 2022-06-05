#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def algoritmo(m):
    resultado = []
    digito = m[::-1]
    for i in range(1, len(digito) + 1):
        if i % 2 == 0:
            num = int(digito[i - 1]) * 2
            x = list(str(num))
            if len(x) > 1:
                res = int(x[0]) + int(x[1])
                resultado.append(res)
            else:
                resultado.append(int(x[0]))
        else:
            resultado.append(int(digito[i - 1]))
    return resultado

def verificacion(n):
    if str(n).isnumeric():
        res = sum(algoritmo(str(n))) % 10
        return res == 0
    else:
        return False



if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        print(verificacion(args[1]))
    else:
        print('Enter integers.')

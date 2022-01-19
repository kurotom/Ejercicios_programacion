# -*- coding: utf-8 -*-
"""
Task:

Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

Rules:

    You need to round the answer to 2 decimal places and return it as String.

    If the given value is 0 then it should return 0.00

    You will only be given Natural Numbers as arguments.

Examples:

SeriesSum(1) => 1 = "1.00"
SeriesSum(3) => 1 + 1/4 + 1/7 = "1.39"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"

NOTE: In PHP the function is called series_sum().
"""


def series_sum(n):
    l1 = []
    if type(n) == int:
        if n == 0:
            return "0.00"
        if n == 1:
            return "1.00"
        else:
            for x in range(1, n):
                l1.append(float("{}".format(1 / (1 + (3 * x)))))
        return "{:.2f}".format(1 + sum(l1))
    else:
        raise TypeError("Solos numeros naturales")


print(series_sum(5))

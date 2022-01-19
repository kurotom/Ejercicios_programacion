# -*- coding: utf-8 -*-
"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.

"""

def getCount(inputStr):
    total = []
    vocales = ["a", "e", "i", "o", "u"]
    for x in vocales:
        total.append(inputStr.count(x))
    return sum(total)


print(getCount("abracadabra"))
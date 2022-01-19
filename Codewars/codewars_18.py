# -*- coding: utf-8 -*-
"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing
distinct letters, each taken only once - coming from s1 or s2.

Examples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""


def longest(s1, s2):
    l1 = "".join(sorted(s1 + s2))
    m1 = []
    for x in l1:
        if x not in m1:
            m1.append(x)
    return "".join(m1)




a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))

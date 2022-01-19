# -*- coding: utf-8 -*-
"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the
result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""


def array_diff(a, b):
    l1 = []
    if not a:
        return []
    elif not b:
        return a
    for x in a:
        i = x in b
        if i is False:
            l1.append(x)
    return l1


#print(array_diff([1, 2], [1]))
print(array_diff([1, 2, 2, 2, 3], [1, 2]))
#print(array_diff([], [1, 2]))
#print(array_diff([1, 2], []))

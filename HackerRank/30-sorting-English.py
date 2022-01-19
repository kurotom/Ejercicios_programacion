# -*- coding: utf-8 -*-
"""
Given an array, , of size distinct elements, sort the array in ascending order using the Bubble Sort algorithm above.
Once sorted, print the following 3 lines:

1) Array is sorted in numSwaps swaps.
    where "numSwaps" is the number of swaps that took place.
2) First Element: firstElement
    where "firstElement" is the first element in the sorted array.
3) Last Element: lastElement
    where "lastElement" is the last element in the sorted array.

Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur
during execution.

Constraints

2 <= n <= 600
1 <= ai <= 2 x 10^6, where 0 <= i < n.
"""

# import sys

n = int("3".strip())
a = list(map(int, ("1 2 3".strip().split())))


def funcion(arrai):
    pasos = 0
    for num in range(len(arrai)-1, 0, -1):
        for i in range(num):
            if arrai[i] > arrai[i+1]:
                arrai[i], arrai[i+1] = arrai[i+1], arrai[i]
                pasos += 1
    return pasos


print("Array is sorted in {} swaps.".format(funcion(a)))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))



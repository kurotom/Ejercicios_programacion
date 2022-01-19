# -*- coding: utf-8 -*-

"""
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given a number, "n",
determine and print whether it's "Prime" or "Not prime".

Note: If possible, try to come up with a "O(sqrt(n))" primality algorithm, or see what sort of optimizations
you come up with for an algorithm "O(n)". Be sure to check out the Editorial after submitting your code!

Input Format:
    The first line contains an integer, "T" , the number of test cases.
    Each of the "T" subsequent lines contains an integer, "n", to be tested for primality.

Constraints:
    1 <= T <= 30
    1 <= n <= 2 x 10^9

Output Format:
    For each test case, print whether "n" is "Prime" or "Not a prime" on a new line.
"""
import math


def primo(numero):
    if numero < 2:
        return "Not prime"
    for x in range(2, math.ceil(math.sqrt(n)) + 1):
        if numero % x == 0:
            return "Not prime"
    return "Prime"


T = int(input())
if 1 <= T <= 30:
    for i in range(T):
        n = int(input())
        if 1 <= n <= 2*(10**9):
            print(primo(n))
        continue


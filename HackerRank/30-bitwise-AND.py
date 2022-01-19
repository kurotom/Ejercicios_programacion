# -*- coding: utf-8 -*-
"""
Given set "S = {1,2,3,...N}". Find two integers, "A" and "B" (where "A" < "B"), from set "S" such that the value "A & B"
of is the maximum possible and also less than a given integer,"K". In this case,"&" represents the bitwise AND operator.

Input Format:
    The first line contains an integer, "T", the number of test cases.
    Each of the "T" subsequent lines defines a test case as "2" space-separated integers, "N" and "K", respectively.

Constraints:
    1 <= T <= 20^3
    2 <= N <= 10^3
    2 <= K <= N

Output Format:
    For each test case, print the maximum possible value of "A & B" on a new line.

Sample Input:
    3
    5 2
    8 5
    2 2

Sample Output:
    1
    4
    0
"""

import math
import os
import random
import re
import sys


def FindMaxAB(n, k):
    max_ab = 0
    for i in range(k - 2, n):
        for j in range(i + 1, n + 1):
            ab = i & j
            if ab == k - 1:
                return ab
            if max_ab < ab < k:
                max_ab = ab
    return max_ab


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        print(FindMaxAB(n, k))






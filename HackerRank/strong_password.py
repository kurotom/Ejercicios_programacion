#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Password to be strong if it satisfies the following criteria:
*   Its length is at least 6.
*   It contains at least one digit.
*   It contains at least one lowercase English character.
*   It contains at least one uppercase English character.
*   It contains at least one special character. The special characters are: !@#$%^&*()-+

Input Format:
*    The first line contains an integer "n" denoting the length of the string.
*    The second line contains a string consisting of "n" characters, the password typed by Louise. Each character is
     either a lowercase/uppercase English alphabet, a digit, or a special character.

Constraints:
*    1 <= n <= 100

Output Format:
*    Print a single line containing a single integer denoting the answer to the problem.
"""

import sys
from random import randrange

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

todo = numbers + lower_case + upper_case + special_characters


#   print(todo[random.randrange(0, len(numbers + lower_case + upper_case + special_characters))])

def numes(password):
    for n in password:
        if n in numbers:
            return password
    return -1

def lower(password):
    for l in password:
        if l in lower_case:
            return password
    return -1

def upper(password):
    for u in password:
        if u in upper_case:
            return password
    return -1

def special(password):
    for s in password:
        if s in special_characters:
            return password
    return -1


def minimumNumber(n, password):
    if len(password) < 6:
        if numes(password) == -1:
            password = password + numbers[randrange(0, len(numbers))]
        if lower(password) == -1:
            password = password + lower_case[randrange(0, len(lower_case))]
        if upper(password) == -1:
            password = password + upper_case[randrange(0, len(upper_case))]
        if special(password) == -1:
            password = password + special_characters[randrange(0, len(special_characters))]
        for i in range(6 - len(password)):
            password += todo[randrange(0, len(todo))]
        return password
    else:
        if numes(password) == -1:
            password = password + numbers[randrange(0, len(numbers))]
        if lower(password) == -1:
            password = password + lower_case[randrange(0, len(lower_case))]
        if upper(password) == -1:
            password = password + upper_case[randrange(0, len(upper_case))]
        if special(password) == -1:
            password = password + special_characters[randrange(0, len(special_characters))]
        return password




for variable in sys.argv[1].split("|"):
    n = len(variable)
    print(len(minimumNumber(n, variable)) - len(variable))
    print(minimumNumber(n, variable))



#   Original
#n = int(input())
#if 1 <= n <= 100:
#    contra = input()
#    contra = "lpo"         #   test
#    contra = "#HackeRank"  #   test
#    print(len(minimumNumber(n, contra)) - len(contra))
#    print(minimumNumber(n, contra))




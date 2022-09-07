"""
In this task, you should check whether a sequence of characters can be divided into strings of a given array. If it can
be divided, the function should return 1. Otherwise, it should return 0

Example:
    Array of strings: "New", "Quiz", "Test", "Exam"
    Sequence of characters: "TestQuiz"

The function should return 1, since both "Test" and "Quiz" can be found in the array.

Example:
    Array of strings: "100", "200", "300"
    Sequence of characters: "400"

The function should return 0, since the string can not be found in the array
Note: string matched should not be case sensitive.
"""

import re
def canSeparateString(str, words):
    yes = 0
    for x in words:
        regex = re.compile(f'{x}', re.IGNORECASE)
        a = re.findall(regex, str)
        if a != []:
            yes = 1
    return yes

str1 = "TestQuiz"
arr1 = ["New", "Quiz", "Test", "Exam"]
str2 = "400"
arr2 = ["100", "200", "300"]
print(canSeparateString(str1, arr1))
print(canSeparateString(str2, arr2))


def canSeparateString(str, words):
    yes = 0
    for i in words:
        if i in str:
            yes = 1
    return yes

str1 = "TestQuiz"
arr1 = ["New", "Quiz", "Test", "Exam"]
str2 = "400"
arr2 = ["100", "200", "300"]
print(canSeparateString(str1, arr1))
print(canSeparateString(str2, arr2))
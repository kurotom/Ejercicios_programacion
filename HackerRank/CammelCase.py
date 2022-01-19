# -*- coding: utf-8 -*-
"""
Alice wrote a sequence of words in CamelCase as a string of letters, "s", having the following properties:
    It is a concatenation of one or more words consisting of English letters.

    All letters in the first word are lowercase.

    For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given "s", print the number of words in "s" on a new line.

For example, s = oneTwoThree. There are "3" words in the string.


Input Format:
    A single line containing string "s".

Constraints:
    1 <= s <= 10^5

Output Format:
    Print the number of words in string "s".
"""
import re


def camelcase(s):
    return len(re.sub("([a-z])([A-Z])", r"\1 \2", s).split())


s = "saveChangesInTheEditor"
print(camelcase(s))

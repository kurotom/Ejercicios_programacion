# -*- coding: utf-8 -*-
"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence, "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters
A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

pangram = "The quick, brown fox jumps over the lazy dog!"
pangram(pangram)
"""


def is_pangram(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for x in abc:
        valor = x in s.lower()
        if valor is False:
            return False
    return True


#pangram = "The quick, brown fox jumps over the lazy dog!"
pangram = "The quick, brown fox jumps"
print(is_pangram(pangram))

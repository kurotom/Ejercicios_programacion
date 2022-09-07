"""
Write an effective function that given two strings s1, s2 returns the minimal numbers of characters needed to be
changed in s2 so s1 would be a sequence substring of s2.

Changes allowed are just switching one character with the other ( not deleting or adding new characters).
for example:
min_chars("cdef","abzdef") will return 1
min_chars("abc","azbzc") will return 2

You can assume that s2 is longer than s1.
"""


def min_chars(s1, s2):
    def uno():
        r = 0
        for i in s1:
            if i not in s2:
                r += 1
        return r

    def dos():
        r = 0
        for x in s2:
            if x not in s1:
                r += 1
        return r

    if uno() != 0:
        return uno()
    else:
        return dos()

print(min_chars("cdef", "abzdef"))
# will return 1
print(min_chars("abc", "azbzc"))
# will return 2
"""
Write a function that, given a non-negative integer, return its digits in descending order. In other words, Rearrange
the digits to create the highest possible number.

For example:
    num = 42145 will return 54421
"""


def CreateHighestNumber(num):
    x = str(num)
    a = "".join(sorted(x, reverse=True))
    return int(a)


print(CreateHighestNumber(42145))


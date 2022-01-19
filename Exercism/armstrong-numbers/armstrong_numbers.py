"""
Numbers armstrong
    9 is an Armstrong number, because 9 = 9^1 = 9
    10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
    153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
"""


def is_armstrong_number(number):
    size = len(str(number))
    init = 0
    for i in range(0, size):
        init += int(str(number)[i]) ** size
    if number == init:
        return True
    return False


print(is_armstrong_number(9))   # True
print(is_armstrong_number(10))  # False
print(is_armstrong_number(153)) # True
print(is_armstrong_number(154)) # False

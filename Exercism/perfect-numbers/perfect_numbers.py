"""
aliquot sum of 15 is (1 + 3 + 5) = 9

    Perfect: aliquot sum = number
        6 is a perfect number because (1 + 2 + 3) = 6
        28 is a perfect number because (1 + 2 + 4 + 7 + 14) = 28
    Abundant: aliquot sum > number
        12 is an abundant number because (1 + 2 + 3 + 4 + 6) = 16
        24 is an abundant number because (1 + 2 + 3 + 4 + 6 + 8 + 12) = 36
    Deficient: aliquot sum < number
        8 is a deficient number because (1 + 2 + 4) = 7
        Prime numbers are deficient
"""


def classify(number):
    aliquot_sum = 0
    for n in range(1, number + 1):
        if number % n == 0 and number != n:
            aliquot_sum += n
    if number > 0:
        if aliquot_sum == number:
            return "perfect"
        elif aliquot_sum > number:
            return "abundant"
        elif aliquot_sum < number:
            return "deficient"
    else:
        raise ValueError("Not zero or negative numbers")


print(classify(6))
print(classify(12))
print(classify(8))

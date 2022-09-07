"""
A binary string is a string containing only the digits '1' and '0'.
A legal binary string is a binary string that doesn't have two '1' next to each other.

Write a recursive function gen_str(k) that returns the number of all the possible legal binary strings that the number
of their characters equals k.

For example: gen_str(3) will return 5 because [000,001,010,100,101]
"""


def gen_str(k):
    a = []
    n = 0
    while True:
        inicio = str(bin(n))[2:]
        if len(inicio) <= k:
#            print(inicio, len(inicio), k, inicio)
            if len(inicio) == 1:
                a.append(f'00{inicio}')
            elif len(inicio) == 2:
                if inicio[0] != inicio[1]:
                    a.append(f'0{inicio}')
            elif len(inicio) > 2:
                if inicio[0] != inicio[1]:
                    a.append(f'{inicio}')
            n += 1
        else:
            break

    return len(a)


print(gen_str(3))
# return 5 ,because [000,001,010,100,101]
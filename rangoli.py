# Rangoli
#
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
#
# e d c b a  = 5

def rangoli(numero):
    N = numero
    MEDIO = N - 1

    abc = 'abcdefghijklmnopqrstuvwxyz'
    abcR = 'zyxwvutsrqponmlkjihgfedcba'

    superString = ''
    # Medio
    medioString = "-".join(list(abcR[-N:] + abc[1:N])) + '\n'

    inferString = ''

    a = 0
    # Superior
    while a < MEDIO:
        x = N * -1
        y = ((N - 1) - a) * -1
        w = N
        z = ((N - 1) - a) - 1

        if y == 0 or z < 0:
            superString += "-".join(list(abcR[N * -1 : ] + abc[ 1 : w])) + '\n'
        else:
            l1 = "-".join(list(abcR[N * -1 : ((N - 1) - a) * -1] + abc[ z + 2 : w ]))
            slash = ((len(medioString) - len(l1)) // 2)
            lf1 = '-' * slash + l1 + '-' * slash + '\n'
            superString += lf1

        a += 1

    # Inferior
    b = 0

    while MEDIO >= 0:
        y = b * -1
        x = (MEDIO ) * -1
        if b != 0:
            l2 = "-".join(list(abcR[N * -1 : y] + abc[b + 1 : N]  ))
            slash2 = ((len(medioString) - len(l2)) // 2)
            lf2 = '-' * slash2 + l2 + '-' * slash2 + '\n'
            inferString += lf2
        b += 1
        MEDIO -= 1

    return superString + medioString + inferString

n = int(input('>:  '))
print(rangoli(n))

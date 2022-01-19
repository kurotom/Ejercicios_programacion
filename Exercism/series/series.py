"""
Given a string of digits, output all the contiguous substrings of length n in that string in the order that they appear.

For example, the string "49142" has the following 3-digit series:
    "491"
    "914"
    "142"
And the following 4-digit series:
    "4914"
    "9142"
And if you ask for a 6-digit series from a 5-digit string, you deserve whatever you get.
Note that these series are only required to occupy adjacent positions in the input; the digits need not be numerically
consecutive.
"""


def slices(series, length):
    res = []
    if length > len(series):
        raise ValueError("Numero mayor que lista")
    if series == "":
        raise ValueError("Lista vacia")
    if length <= 0:
        raise ValueError("Numero es menor o igual a 0")
    for i in range(len(series)):
        if len(series[i:i + length]) < length:
            break
    #        print(i, series[i:i + lenght])
        res.append(series[i:i + length])
        i -= 1
    return res


#slices("49142", 3) # "491" "914" "142"
#slices("49142", 4) # "4914" "9142"
#slices("9142", 2) # "91" "14" "42"
#slices("", 1) # raise error
#slices("123", -1) # raise error
#slices("123", 4) # raise error
#slices("918493904243", 5) # ["91849", "18493", "84939", "49390", "93904", "39042", "90424", "04243"]


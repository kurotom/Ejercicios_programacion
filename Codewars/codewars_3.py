# -*- coding: utf-8 -*-
"""
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an
application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club,
handicaps range from -2 to +26; the better the player the lower the handicap.

###        Input      ####
Input will consist of a list of lists containing two items each. Each list contains information for a single potential
member. Information consists ofb an integer for the person's age and an integer for the person's handicap.

Note for F#: The input will be of (int list list) which is a List<List>

###        Example Input    ###
[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

###        Output   ###
Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to
be placed in the senior or open category.

###        Example Output   ###
["Open", "Open", "Senior", "Open", "Open", "Senior"]
"""


def openOrSenior(data):
    resultado = []
    for persona in data:
        if persona[0] >= 55:
            if persona[1] > 7:
                resultado.append("Senior")
            elif persona[1] <= 7:
                resultado.append("Open")
            elif persona[1] < 0:
                resultado.append("Open")
        elif persona[0] < 55:
            resultado.append("Open")
    return resultado


print(openOrSenior([[57, 7], [58, 10], [35, 9], [24, 3], [61, 23], [28, 20], [32, 22], [72, 13]]))


"""
It should work for random tests too:
[[57, 7], [58, 10], [35, 9], [24, 3], [61, 23], [28, 20], [32, 22], [72, 13]]
should equal:
['Open', 'Senior', 'Open', 'Open', 'Senior', 'Open', 'Open', 'Senior']
"""

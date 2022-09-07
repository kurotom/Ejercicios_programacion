"""
Given a 2D cube of integers (Two-dimensional lists), you are required to rotate the cube by 90 degrees.

Example:
    Give the following cube:
        1 2 3
        4 5 6
        7 8 9

The function should return:
        7 4 1
        8 5 2
        9 6 3
"""


def rotateCube(arr):
    a = []
    i = 0
    for x in range(3):
        b = []
        for y in range(3):
            if x == i:
                b.append(arr[y][x])
        b.reverse()
        a.append(b)
        i += 1
    return a


cube = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotateCube(cube))

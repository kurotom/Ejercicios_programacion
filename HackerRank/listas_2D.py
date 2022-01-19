# -*- coding: utf-8 -*-
#matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]

matrix = [[1, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 2, 4, 4, 0],
          [0, 0, 0, 2, 0, 0],
          [0, 0, 1, 2, 4, 0]]

"""
a = []
for i in range(6):
    b = []
    for fila in matrix:
        b.append(fila[i])
    a.append(b)

for x in a:
    print(x)
"""

max = -100
for i in range(4):
    for j in range(4):
        sum = matrix[i+1][j+1]
        for x in range(3):
            sum += matrix[i][j+x] + matrix[i+2][j+x]
        if sum > max:
            max = sum
print(max)

"""
Dado un triángulo (creado a partir de una matriz), devuelve la suma mínima de la ruta de arriba a abajo.
Puede pasar a uno de los dos números de la fila siguiente para cada paso. lo que significa que si está en el índice i
en la fila actual, puede pasar al índice i o al índice i + 1 en la siguiente fila.

For example:
triangle = [[8],[5,6],[1,2,3]] ---> 17
    8
    5,6
    1,2,3
the function will return 8+6+3= 17

Nota:
Intente resolver el problema utilizando solo O(n) espacio extra.
Donde n es el número total de filas en el triángulo
"""
import copy


def MinSumTriangle(arr):
    triangle = []
    for i in arr:
        triangle.append(list(i))
    dp = list(copy.deepcopy(triangle[-1]))
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(0, row + 1):
            dp[col] = triangle[row][col] + max(dp[col], dp[col + 1])
    return dp[0]




array = [set([8]), set([5, 6]), set([1, 2, 3])]
print(MinSumTriangle(array))
# 17
#print(MinSumTriangle([set([2]), set([-11, -10])]))
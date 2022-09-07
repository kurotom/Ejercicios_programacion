
def diagonalDifference(arr):
    # Write your code here
    l1 = []
    l2 = []
    inicio = 0
    final = len(arr[0]) - 1
    for x in arr:
        # print(x[inicio], x[final])
        l1.append(x[inicio])
        l2.append(x[final])
        inicio += 1
        final -= 1
    print(abs(sum(l1) - sum(l2)))
    return abs(sum(l1) - sum(l2))



matrix = [
    [11,2,4],
    [4,5,6],
    [10,8,-12],
]
print(diagonalDifference(matrix))

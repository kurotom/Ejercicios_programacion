"""
Given an array of numbers (integers) and a certain sum, check how many unique ways can any of the array numbers match
the given sum.

Example:
    result: 10
    array: 1,2,3,4,5

The function should return: 3
    1+2+3+4 = 10
    1+4+5 = 10
    2+3+5 = 10

Example:

    result: 17
    array: 1,2,4,7,5

The function should return: 1
    1, 4, 5, 7 = 17
"""


def getUniqueMatches(arr, result):
    print(arr, result)
    r = 0
    l = 0
    k = 0
    for i in range(len(arr)):
        for a in arr:
            print(arr[l], arr[k])
            k+=1
#            k += arr[l]
#            if k == 10:
#                print(k)
#                k = 0
        l += 1
    return ""


total = 10
array = [1,2,3,4,5]
print(getUniqueMatches(array, total))
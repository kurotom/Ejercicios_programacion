# -*- coding: utf-8 -*

arr = "2 3 6 6 5"
n = 5

esta = []

if 2 <= n <= 10:
    arr = map(int, arr.split())
    a = list(arr)
    for x in a:
        if x != max(a):
            esta.append(x)
    print(max(esta))


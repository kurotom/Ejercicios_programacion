"""
Gold is traded in a Commodities Exchange; the closing prices of gold are changing every day and given in an array. Find
the best profit that you can make by buying and selling gold.

For example, if the daily closing prices are:
    20, 70, 140, 90,180, 20, 20

The best profit will be 210, buying on the first day, selling on the third day. Again buy on the fourth day and sell on
the fifth day. If there can be no profit return 0.
"""


def findBestProfit(arr):
    length = len(arr)
#    print(arr)
#    print((140-20) + (180-90))
    inicio = 0
    fin = len(arr) - 1

    if fin <= inicio:
        return 0

    ganancia = 0
    for i in range(inicio, fin, 1):
        for j in range(i + 1, fin + 1):
            if arr[j] > arr[i]:
                profit = arr[j] - arr[i]
                if profit > ganancia:
                    ganancia = arr[j] - arr[i]
                else:
                    break
#                current_profit = arr[j] - arr[i] + findBestProfit([arr[j], arr[i]])
#                print(findBestProfit(arr))
#                print(current_profit)
    print(ganancia)





array = [20, 70, 140, 90, 180, 20, 20]
findBestProfit(array)

"""
Write a program that prints the numbers from 1 to 100, not including 100. But
for multiples of four print “Fizz” instead of the number and for the multiples
of six print “Buzz”. For numbers which are multiples of both four and six print
nothing, not even a number.
"""

def fizzbuzz():
    x = []
    for i in range(1, 100):
        if i % 4 == 0 and i % 6 != 0:
            print('Fizz')
            x.append(i)
        if i % 6 == 0 and i % 4 != 0:
            print('Buzz')
            x.append(i)
    print(x)


if __name__ == '__main__':
    fizzbuzz()

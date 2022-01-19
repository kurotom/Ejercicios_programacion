# -*- coding: utf-8 -*-

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        c = 0
        for x in range(n):
            if x > 0:
                if n % x == 0:
                    c += x
        #print(c + n, c, n)
        return c + n


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

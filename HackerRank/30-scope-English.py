# -*- coding: utf-8 -*-

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = self.computeDifference()

    # Add your code here
    def computeDifference(self):
        ld = {}
        if len(self.__elements) == 1:
            return "{}".format(str(self.__elements[0]))
        for x in self.__elements:
            for y in self.__elements:
                if x - y > 0:
                    ld[(x, y)] = x - y
                elif x - y == 0:
                    ld[(x, y)] = x - y
        return max(list(ld.values()))

# End of Difference class



_ = input()
if 1 <= int(_) <= 10:
    a = [int(e) for e in input().split(' ')]
    d = Difference(a)
    d.computeDifference()
    print(d.maximumDifference)


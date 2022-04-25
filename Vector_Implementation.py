"""
Create a Python class that represents any n_dimentional vector, where n is a
finite natural number. The vectors are always represented as vertical vectors.
You should be able to natively add, subtract, and find the dot product of the
two vector objects (for dot product, use the multiplication symbol *). If the
vector dimensions don't match up, the program should raise an exception.
Additionally, the vectors should be printable, with the output being the vector
as it would be written.
"""

import numpy as np

class Vector():
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'{self.x}'

    def __add__(self, sum):
        if isinstance(sum, Vector):
            if len(self.x) != len(sum.x):
                raise Exception('Vectors must be same length!')
            else:
                res = []
                for i in range(len(self.x)):
                    res.append(self.x[i] + sum.x[i])
                return f'{res}'
        else:
            raise Exception('Vectors must be "Vector" instance')

    def __sub__(self, rest):
        if isinstance(rest, Vector):
            if len(self.x) != len(rest.x):
                raise Exception('Vectors must be same length!')
            else:
                res = []
                for i in range(len(self.x)):
                    res.append(self.x[i] - rest.x[i])
                return f'{res}'
        else:
            raise Exception('Vectors must be "Vector" instance')

    def __mul__(self, mult):
        if isinstance(mult, Vector):
            if len(self.x) != len(mult.x):
                raise Exception('Vectors must be same length!')
            else:
                res = []
                for i in range(len(self.x)):
                    res.append(self.x[i] * mult.x[i])
                return Vector(res)
        else:
            raise Exception('Vectors must be "Vector" instance')

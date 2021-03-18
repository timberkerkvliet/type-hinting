from math import sqrt


class Vector(object):
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.x + other.x)

    def __sub__(self, other):
        return self + other*-1

    def __mul__(self, scalar):
        return Vector(x=self.x*scalar, y=self.y*scalar)

    def __len__(self):
        return sqrt(self.x**2 + self.y**2)

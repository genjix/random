from math import sqrt

class Vector2D(object):
    def __init__(self, x=0.0, y=0.0):
        object.__init__(self)
        self.x = x
        self.y = y

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        return Vector2D(self.x, self.y) / self.magnitude()
    
    def __iadd__(self, op):
        self.x += op.x
        self.y += op.y
        return self

    def __add__(self, op):
        return Vector2D(self.x + op.x, self.y + op.y)

    def __isub__(self, op):
        self.x -= op.x
        self.y -= op.y
        return self

    def __sub__(self, op):
        return Vector2D(self.x - op.x, self.y - op.y)

    def __imul__(self, op):
        self.x *= op
        self.y *= op
        return self
    
    def __mul__(self, op):
        return Vector2D(self.x * op, self.y * op)

    def __idiv__(self, op):
        if op < 0.00001:
            op = 0.00001
        self.x /= op
        self.y /= op
        return self

    def __div__(self, op):
        if op < 0.00001:
            op = 0.00001
        return Vector2D(self.x / op, self.y / op)


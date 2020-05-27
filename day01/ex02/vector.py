import sys


class Vector:
    def __init__(self, *args, **kwargs):
        if (len(args) == 1):
            one_arg = True
            a1 = args[0]
        else:
            one_arg = False
            a1 = None
        if one_arg and isinstance(a1, list):
            self.values = a1
            self.size = len(a1)
        elif one_arg and isinstance(a1, int):
            self.size = a1
            self.values = {}
            v = 0.0
            i = 0
            while i < a1:
                self.values[i] = v
                i += 1
                v += 1.0
        else:
            self.size = a1[1] - a1[0]
            self.values = {}
            v = float(a1[0])
            i = 0
            while i < self.size:
                self.values[i] = v
                i += 1
                v += 1.0

    def __add__(self, other):
        i = 0
        len = self.size if self.size < other.size else other.size
        res = []
        for i in range(len):
            res.append(0)
        while i < len:
            res[i] = self.values[i] + other.values[i]
            i += 1
        return Vector(res)

    def __radd__(self, other):
        if other.size == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        i = 0
        len = self.size if self.size < other.size else other.size
        res = []
        for i in range(len):
            res.append(0)
        while i < len:
            res[i] = self.values[i] - other.values[i]
            i += 1
        return Vector(res)

    def __rsub__(self, other):
        if other.size == 0:
            return self
        else:
            return self.__sub__(other)

    def __truediv__(self, other):
        i = 0
        len = self.size if self.size < other.size else other.size
        res = []
        for i in range(len):
            res.append(0)
        while i < len:
            res[i] = self.values[i] / other.values[i]
            i += 1
        return Vector(res)

    def __rtruediv__(self, other):
        if other.size == 0:
            return self
        else:
            return self.__truediv__(other)

    def __mul__(self, other):
        i = 0
        len = self.size if self.size < other.size else other.size
        res = []
        for i in range(len):
            res.append(0.0)
        while i < len:
            res[i] = self.values[i] * other.values[i]
            i += 1
        return Vector(res)

    def __rmul__(self, other):
        if self.size == 0:
            return self
        else:
            return self.__mul__(other)

    def __str__(self):
        return "Values: %s, Size %i" % (self.values, self.size)

    def __repr__(self):
        return {'values': self.values, 'size': self.size}


x = Vector((3))
y = Vector((3))
z = x.__add__(y)
print(z.values)
print(z.size)

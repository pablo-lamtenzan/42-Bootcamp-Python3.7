import sys


class Matrix:
    def __init__(self, *args, **kwargs):
        if (len(args) == 1):
            one_arg = True
            a1 = args[0]
        else:
            one_arg = False
            a1 = None
        if one_arg and isinstance(a1, list):
            # have to check if all elems has the same shapes
            self.data = a1
            y = 0
            for i in range(len(a1)):
                while y < len(a1[i]):
                    y += 1
                break
            self.shape = (len(a1), y)
        elif one_arg and isinstance(a1, tuple):
            self.shape = a1
            self.data = []
            for i in range(a1[0]):
                self.data.append([])
                for y in range(a1[1]):
                    self.data[i].append(0.0)
        elif isinstance(args[0], list) and isinstance(args[1], tuple):
            self.data = args[0]
            self.shape = args[1]
    
    def __add__(self, other):
        new = Matrix(self.data, self.shape)
        # check if other object is Matrix too
        if isinstance(other, Matrix):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] + other.data[i][j]
        # check if other object is scalar
        elif isinstance(other, (int, float)):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] + other
        return new
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        new = Matrix(self.data, self.shape)
        # check if other object is Matrix too
        if isinstance(other, Matrix):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] - other.data[i][j]
        # check if other object is scalar
        elif isinstance(other, (int, float)):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] - other
        return new

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        new = Matrix(self.data, self.shape)
        # check if other object is Matrix too
        if isinstance(other, Matrix):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] * other.data[i][j]
        # check if other object is scalar
        elif isinstance(other, (int, float)):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] * other
        return new

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        new = Matrix(self.data, self.shape)
        # check if other object is Matrix too
        if isinstance(other, Matrix):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] / other.data[i][j]
        # check if other object is scalar
        elif isinstance(other, (int, float)):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.data[i][j] = self.data[i][j] / other
        return new

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    # not work
    def __str__(self):
        return f"(Matrix {x for x in self.data})"

    def __repr__(self):
        return {}


x = Matrix((2, 3))
y = Matrix((2, 3))
z = x.__add__(2.0)
z.__str__()
#print(z.data)
#print(z.shape)

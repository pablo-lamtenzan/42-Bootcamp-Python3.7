import numpy as np


class ScrapBooker:
    def _init__(self):
        pass

    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        if not isinstance(position, tuple) and len(position) != 2:
            return "ERROR"
        if not isinstance(dimensions, tuple) and len(dimensions) != 2:
            return "ERROR"
        y, x = dimensions
        startx = x
        starty = 0
        return array[starty:starty + position[0], startx:startx + position[1]]

    @staticmethod
    def thin(array, n, axis=0):
        if axis == 1:
            axis = 0
        else:
            axis = 1
        return np.delete(array, slice(n - 1, None, n), axis=axis)

    @staticmethod
    def juxtapose(array, n, axis=0):
        return np.concatenate([array] * n, axis=axis)

    @staticmethod  # dim == tupple
    def mosaic(array, dimensions):
        return np.tile(array, dimensions)


array = np.array([list("ABCDEFGHIJKL") for i in range(10)])
Sc = ScrapBooker()
ret = Sc.crop(array, (3, 3), position=(3, 3))
print(ret)
print(array)

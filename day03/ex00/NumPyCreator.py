import numpy as np


class NumPyCreator:
    def __init__(self):
        pass

    @staticmethod
    def from_list(lst, type=None):
        return np.array(lst, dtype=type)

    @staticmethod
    def from_tuple(tpl, type=None):
        return np.array(tpl, dtype=type)

    @staticmethod
    def from_iterable(itr, type=None):
        return np.fromiter(itr, dtype=type)

    @staticmethod
    def from_shape(shape, value=0, type=None):
        return np.full(shape, value, dtype=type)

    @staticmethod
    def random(shape):
        return np.random.random_sample(shape)

    @staticmethod
    def identity(n):
        return np.identity(n)


npc = NumPyCreator()
ret = npc.from_list([[1, 2, 3], [6, 3, 4]], type="float")
print(ret)
ret = npc.from_tuple((1, 2, 3), type="int")
print(ret)
ret = npc.from_iterable(iter([1, 2, 3]), type="int")
print(ret)
ret = npc.from_shape(3, type="int")
print(ret)
ret = npc.random((3))
print(ret)
ret = npc.identity(3)
print(ret)

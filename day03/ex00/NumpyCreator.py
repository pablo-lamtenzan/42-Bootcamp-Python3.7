import numpy as np


class NumPyCreator:
    def __init__(self):
        pass

    @staticmethod
    def from_list(lst, type=None):
        return np.array(lst, dtype=srt(type))

    @staticmethod
    def from_tuple(tpl, type=None):
        return np.array(tpl, dtype=srt(type))

    @staticmethod
    def from_iterable(itr, type=None):
        return np.fromiter(itr, dtype=type)
    
    @staticmethod
    def from_shape(shape, value=0):
        return np.full(shape, value, dtype=type)
    
    @staticmethod
    def random(shape, type=None):
        return np.random.random_sample(shape, dtype=type)

    @staticmethod
    def identity(n):
        return np.identity(n, dtype=type)

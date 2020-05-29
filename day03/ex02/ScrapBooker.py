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
        return array[starty:starty + pos[0], startx:startx + pos[1]]
        # check it

    @staticmethod
    def thin(array, n, axis):
        np.delete(array, n, axis=axis)
        # all to test n is a slice

    @staticmethod
    def juxtapose(array, n, axis):
        return np.repeat(array, n, axis=axis)
        # np.concatenate

    @staticmethod
    def mosaic(array, dimensions):
        return np.repeat(array[:, :, np.newaxis], dimensions, axis=2)
        # np.tile

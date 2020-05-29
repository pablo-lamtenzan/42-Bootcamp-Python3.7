import numpy as np
from ImageProcessor import ImageProcessor as im


class ColorFilter:
    def __init__(self):
        pass

    @staticmethod
    def invert(array):
        filter = [1, 1, 1]
        new = np.copy(array)
        for raw in range(len(array)):
            for pixel in range(raw):
                new[raw][pixel] = filter - new[raw][pixel]
        return new

    @staticmethod
    def to_blue(array):
        new = np.zeros(array.shape)
        for raw in range(array.shape[0]):
            for pixel in range(array.shape[1]):
                new[raw][pixel][2] = array[raw][pixel][2]
        return new

    @staticmethod
    def to_green(array):
        new = np.zeros(array.shape)
        for raw in range(array.shape[0]):
            for pixel in range(array.shape[1]):
                new[raw][pixel][1] = array[raw][pixel][1]
        return new

    @staticmethod
    def to_red(array):
        new = np.zeros(array.shape)
        for raw in range(array.shape[0]):
            for pixel in range(array.shape[1]):
                new[raw][pixel][0] = array[raw][pixel][0]
        return new

    @staticmethod
    def celluloid(array):
        filter = [1, 1, 1]
        new = np.copy(array)
        for raw in range(array.shape[0]):
            for pixel in range(array.shape[1]):
                for i in range(3):
                    if array[raw][pixel][i] < 0.5:
                        dist = 0.5 - array[raw][pixel][i]
                        if dist > 0.25:
                            new[raw][pixel][i] = 0.33
                        else:
                            new[raw][pixel][i] = 0.0
                    else:
                        dis = 1.0 - array[raw][pixel][i]
                        if dist < 0.75:
                            new[raw][pixel][i] = 0.66
                        else:
                            res[raw][pixel][i] = 1.0
        return new

    @staticmethod
    def to_grayscale(array, filter=None):
        ret = np.array(array)
        if filter == 'm':
            for raw in range(array.shape[0]):
                for pixel in range(array.shape[1]):
                    amean = 0
                    for i in range(3):
                        amean += array[raw][pixel][i]
                    for j in range(3):
                        ret[raw][pixel][j] = amean / 3
        elif filter == 'w':
            tfilter = [0.299, 0.587, 0.114]
            for raw in range(array.shape[0]):
                for pixel in range(array.shape[1]):
                    ret[raw][pixel] = array[raw][pixel] * tfilter
        else:
            return "ERROR"
        return ret


C = ColorFilter()
array = im.load("42AI.png")
ret = C.invert(array)
im.display(ret)

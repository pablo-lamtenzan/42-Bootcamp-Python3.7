import numpy as np


class ColorFilter:
    def __init__(self):
        pass

    @staticmethod
    def invert(array):
        filter = [1, 1, 1]
        new = np.coy(array)
        for raw in range(len(array)):
            for pixel in range(len(raw)):
                new[raw][pixel] = filter - new[raw][pixel]
        return new

    @staticmethod
    def to_blue(array):
        new = np.zeros(array)
        for raw in range(len(array)):
            for pixel in range(len(raw)):
                new[raw][pixel][2] = array[raw][pixel][2]
        return new

    @staticmethod
    def to_green(array):
        new = np.zeros(array)
        for raw in range(len(array)):
            for pixel in range(len(raw)):
                new[raw][pixel][1] = array[raw][pixel][1]
        return new

    def to_red(array):
        new = np.zeros(array)
        for raw in range(len(array)):
            for pixel in range(len(raw)):
                new[raw][pixel][0] = array[raw][pixel][0]
        return new

    @staticmethod
    def celluloid(array):
        filter = [1, 1, 1]
        new = np.coy(array)
        for raw in range(len(array)):
            for pixel in range(len(raw)):
                for i in range(3):
                    if array[raw][pixel][i] < 0.5:
                        dist = 0.5 - array[raw][pixel][i]
                        if dist > 0.25:
                            res[raw][pixel][i] = 0.33
                        else:
                            res[raw][pixel][i] = 0.0
                    else:
                        dis = 1.0 - array[raw][pixel][i]
                        if dist < 0.75:
                            res[raw][pixel][i] = 0.66
                        else:
                            res[raw][pixel][i] = 1.0
        return new

    @staticmethod
    def to_grayscale(array, filter):
        ret = np.array(array)
        if filter == 'm':
            for raw in range(len(array)):
                for pixel in ran(len(raw)):
                    amean = 0
                    for i in range(3):
                        amean += array[raw][pixel][i]
                    for j in range(3):
                        ret[raw][pixel][j] = amean / 3
        elif filter == 'w':
            tfilter = [0.299, 0.587 0.114]
            for raw in range(len(raw)):
                for pixel in range(len(raw)):
                    new[raw][pixel] = array[raw][pixel] * tfilter
        else:
            return "ERROR"
        return ret

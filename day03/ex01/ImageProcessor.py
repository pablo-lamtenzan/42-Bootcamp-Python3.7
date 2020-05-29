import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:
    def __init__(self):
        pass

    @staticmethod
    def load(path):
        ret = np.array(mpimg.imread(path))
        print(ret.shape)
        return ret

    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()

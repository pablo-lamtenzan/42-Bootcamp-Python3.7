import pandas as pd



class FileLoader:
    def __init__(self):
        pass

    @staticmethod
    def load(path):
        data = pd.read_csv(path)
        print("Loading dataset of dimensions %i x %i" % (data.shape[0],
              data.shape[1]))
        # data.head(5)
        return data

    @staticmethod
    def display(df, n):
        if n > 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))



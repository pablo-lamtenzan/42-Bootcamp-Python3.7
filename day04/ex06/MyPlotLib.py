import pandas as pd
from matplotlib import pyplot as plt
from FileLoader import FileLoader
import scipy


class MyPlotLib:
    def __init__(self, df, features):
        self.data = df
        self.features = features
        pass

    @staticmethod
    def histogram(data, features):
        data[features].hist()
        plt.show()

    @staticmethod
    def density(data, features):
        data[features].plot.kde()
        plt.show()

    @staticmethod
    def pair_plot(data, features):
        pd.plotting.scatter_matrix(data[features])
        plt.show()

    @staticmethod
    def box_plot(data, features):
        data[features].plot.box()
        plt.show()


f = FileLoader()
r = f.load("athlete_events.csv")
features = ['Year', 'Team']
m = MyPlotLib(r, features)
m.box_plot(r, features)

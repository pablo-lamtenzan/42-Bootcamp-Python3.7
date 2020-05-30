import pandas as pd
from matplotlib import pyplot as plt
from FileLoader import FileLoader


class Komparator:
    def __init__(self, df):
        self.data = df
        pass

    def compare_box_plots(self, categorical_var, numerical_var):
        self.data[categorical_var].plot.box(colunm=numerical_var)
        plt.show()

    def density(self, categorical_var, numerical_var):
        pass

    def compare_histograms(categorical_var, numerical_var):
        pass

# to end

f = FileLoader()
r = f.load("athlete_events.csv")
k = Komparator(r)
k.compare_box_plots(["Team", "Year"], [1, 2, 3])

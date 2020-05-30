import pandas as pd
from FileLoader import FileLoader


def youngestFellah(df, year):
    w = df.loc[(df["Sex"] == "F") & (df["Year"] == year)]
    m = df.loc[(df["Sex"] == "M") & (df["Year"] == year)]
    min_w = w['Age'].min()
    min_m = m['Age'].min()
    print("The lowest women's age in %i was %i." % (year, min_w))
    print("The lowest men's age in %i was %i." % (year, min_m))


F = FileLoader()
df = F.load("athlete_events.csv")
youngestFellah(df, 2000)

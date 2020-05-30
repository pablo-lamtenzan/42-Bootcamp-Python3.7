import pandas as pd
from FileLoader import FileLoader


def proportionBySport(df, year, sport, gender):
    sport_data = df.loc[(df["Sex"] == gender) & (df["Year"] == year) &
                        (df["Sport"] == sport)]
    gender_data = df.loc[(df['Sex'] == gender) & (df['Year'] == year)]
    return sport_data.size / gender_data.size


F = FileLoader()
df = F.load("athlete_events.csv")
ret = proportionBySport(df, 2004, "Tennis", "F")
print(ret)

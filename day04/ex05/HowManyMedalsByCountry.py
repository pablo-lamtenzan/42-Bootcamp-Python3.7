import pandas as pd
from FileLoader import FileLoader


def howManyMedalsByCountry(df, country_name):
    data = df[df['Team'] == country_name]
    ret = {}
    for i, rows in data.iterrows():
        # create
        if rows['Year'] not in ret:
            ret[rows['Year']] = {'G': 0, 'S': 0, 'B': 0}
            if pd.notna(rows['Medal']):
                ret[rows['Year']][rows['Medal'][0]] += 1
        # append
        elif pd.notna(rows['Medal']):
            ret[rows['Year']][rows['Medal'][0]] += 1
    return ret


F = FileLoader()
ret = F.load("athlete_events.csv")
m = howManyMedalsByCountry(ret, "United States")
print(m)

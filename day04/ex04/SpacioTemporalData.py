import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, data):
        self.data = data
        pass

    def when(self, location):
        data = self.data[self.data['City'] == location]
        ret = []
        for i, rows in data.iterrows():
            if rows['Year'] not in ret:
                ret.append(rows['Year'])
        return ret

    def where(self, date):
        data = self.data[self.data['Year'] == date]
        ret = []
        for i, rows in data.iterrows():
            if rows['City'] not in ret:
                ret.append(rows['City'])
        return ret


f = FileLoader()
r = f.load("athlete_events.csv")
s = SpatioTemporalData(r)
print("Test for when(Paris) -> %s" % s.when("Paris"))
print("Test for where(2016) -> %s" % s.where(2016))

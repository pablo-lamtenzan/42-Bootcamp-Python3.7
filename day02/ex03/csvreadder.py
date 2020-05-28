import csv


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0,
                 skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.header_data = []
        self.data = []

    def __enter__(self):
        # open the file and tail
        f = open(self.filename, mode='r')
        f.readline()[self.skip_top:-self.skip_bottom]
        csv_reader = csv.reader(f, delimiter=self.sep)
        self.f = f
        # get data and header
        first = True
        for row in csv_reader:
            if first and self.header is True:
                first = False
                self.header_data.append(row)
            else:
                self.data.append(row)
        # check corruption
        cont = 0
        for i in self.data:
            for y in i:
                cont += 1
            break
        for i in self.data:
            if len(i) != cont:
                return "ERROR"
        if self.header is True:
            for y in self.header_data:
                if len(y) != cont:
                    return "ERROR"
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.f.close()

    def getdata(self):
        return self.data

    def getheader(self):
        if len(self.header_data) == 0:
            return "No header"
        return self.header_data


if __name__ == "__main__":
    with CsvReader('test.csv') as file:
        if file is None:
            print("File is corrupted")
        data = file.getdata()
        header = file.getheader()
        print(data)
        print(header)

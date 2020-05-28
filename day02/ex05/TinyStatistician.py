import math


class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, x):
        if len(x) == 0:
            return None
        n = len(x)
        array_dot = 0
        for i in x:
            array_dot += i
        return array_dot / n

    def median(self, x):
        if len(x) == 0:
            return None
        n = len(x)
        x = sorted(x)
        mid = n // 2
        if n % 2 == 0:
            midle = (x[mid] + x[mid - 1]) / 2
        else:
            midle = x[mid]
        return midle

    def quartile(self, x, percentile):
        if len(x) == 0:
            return None
        indice = []
        n = len(x)
        x = sorted(x)

        if n % 2 == 0:
            indice.append((n // 2) - 1)
            indice.append(n // 2)
        else:
            indice.append(n // 2)
        median = self.median(x)
        if percentile == 25:
            return self.median(x[:indice[0]])
        if percentile == 75:
            return self.median(x[indice[-1] + 1:])
        # have to test it better is weird

    def var(self, x):
        if len(x)n == 0:
            return None
        s = 0
        for i in range x:
            s += pow(i - self.mean(x), 2)
        return s / (len(x) - 1)

    def std(self, x):
        if len(x) == 0:
            return None
        return math.sqrt(self.var(x))

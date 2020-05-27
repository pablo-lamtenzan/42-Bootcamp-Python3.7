

class Evaluator:
    def __init__(self):
        pass

    def zip_evaluate(self, coefs, words):
        if len(coefs) != len(words):
            print("-1")
            return -1
        ret = 0
        for a, b in zip(coefs, words):
            ret += len(b) * a
        print(ret)
        return ret

    def enumerate_evaluate(self, coefs, words):
        if len(coefs) != len(words):
            print("-1")
            return -1
        ret = 0
        for a, b in enumerate(words):
            ret += len(b) * coefs[a]
        print(ret)
        return (ret)


x = Evaluator()
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
x.enumerate_evaluate(coefs, words)

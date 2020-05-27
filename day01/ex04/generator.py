import time
import random


def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        return "ERROR"
    if option is not None:
        if option != "ordered" and option != "shuffle" and \
           option != "unique":
            return "ERROR"
    text = str(text)
    res = text.split(sep)
    if option == "ordered":
        res.sort()
    elif option == "shuffle":
        random.shuffle(res)
    elif option == "unique":
        res = list(dict.fromkeys(res))
    for i in res:
        yield i


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

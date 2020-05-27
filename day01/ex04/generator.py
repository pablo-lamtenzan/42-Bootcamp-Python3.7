import time


def rand_numb(n):
    digit = int(str(time.time()).split('.')[-1][-1])
    if digit <= len(n):
        return n[digit - 1]
    else:
        new_digit = digit - len(n)
        return n[new_digit]


def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        return "ERROR"
    if option and (option != "shuffle" or option != "unique" or option != "ordered"):
        return "ERROR"
    text = str(text)
    res = text.split(sep)
    if not option or option == "ordered":
        if option == "ordered":
            res = res.sort()
        for i in res:
            yield i
    elif option == "shuffle":
        pass  # do to
    elif option == "unique":
        check = []
        for i in res:
            check.append(i)
            if i not in check:
                yield i

# check the 3 options

            




text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
    print(word)

import string


def text_analyser(str):
    upper = 0
    lower = 0
    ponct = 0
    esp = 0
    for ch in str:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
        if ch in string.punctuation:
            ponct += 1
        if ch == ' ':
            esp += 1
    print("Uppercases: ", upper)
    print("Lowercases: ", lower)
    print("Ponctuation: ", ponct)
    print("Espace: ", esp)

import string


def text_analyser(array=''):
    upper = 0
    lower = 0
    ponct = 0
    esp = 0
    if not array == '':
        for ch in array:
            if ch.isupper():
                upper += 1
            if ch.islower():
                lower += 1
            if ch in string.punctuation:
                ponct += 1
            if ch == ' ':
                esp += 1
    else:
        print("This function only is useful with a param")
    print("Uppercases: ", upper)
    print("Lowercases: ", lower)
    print("Ponctuation: ", ponct)
    print("Espace: ", esp)


text_analyser()

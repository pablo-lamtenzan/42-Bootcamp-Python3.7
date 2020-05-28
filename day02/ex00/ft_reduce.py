

def ft_reduce(function_to_apply, list_of_inputs):
    res = list_of_inputs[0]
    for inputs in list_of_inputs[1:]:
        res = function_to_apply(res, inputs)
    return res


def add(x, y):
    return x + y


nb = [1, 2, 3, 4, 5]
print(ft_reduce(add, nb))

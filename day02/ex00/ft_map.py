

# works well but hae to see what it returns
def ft_map(function_to_apply, list_of_inputs):
    return [function_to_apply(inputs) for inputs in list_of_inputs]


listof = [1, 2, 3, 4, 5]


def sum(x):
    return x + x


def prod(x):
    return x * x


print(ft_map(sum, listof))

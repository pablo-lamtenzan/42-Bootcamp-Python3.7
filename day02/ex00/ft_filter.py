

def ft_filter(function_to_apply, list_of_inputs):
    res = []
    for inputs in list_of_inputs:
        if function_to_apply(inputs):
            res.append(inputs)
    return res


numb_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = ft_filter(lambda x: x % 2, numb_list)
print(odd)

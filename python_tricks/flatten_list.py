# Example to flatten the list of lists using recursion.

def flatten_list(nested_list):
    flattened_list = []
    for element in nested_list:
        if isinstance(element, list):
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)
    return flattened_list


nested_list = [1, 2, [2, 2, 3, 4, [5, 4, 3, 2]], 1, 3, 7, 9]

result = flatten_list(nested_list=nested_list)
print(result)
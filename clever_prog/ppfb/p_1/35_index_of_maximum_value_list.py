def maximum(x):
    maximum_index = 0
    current_index = 1
    while current_index < len(x):
        if x[maximum_index] > x[current_index]:
            maximum_index = current_index
        current_index += 1
    return maximum_index


a = [23, 76, 45, 98, 78, 9, 24]
print(maximum(a))

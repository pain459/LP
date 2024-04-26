# Using sorted and zip functions to sort 2 different lists based on the index

x = ['a', 'b', 'c', 'd']
y = [3, 2, 4, 1]

# sort elements based on numeric values
sorted_elements = [element for _, element in sorted(zip(y, x))]

print(sorted_elements)
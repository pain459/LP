# using set operator to delete the duplicate elements from a list.

x = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]

# Remove duplicated while preserving order.
unique_elements = list(set(i for i in x))
print(unique_elements)
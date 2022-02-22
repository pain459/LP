# demonstration of different lists.

list1 = []
print("This is an empty list:")
print(list1)

list2 = [1, 2, 3, 4, 5]
print("\nThis is a list of integers:")
print(list2)

list3 = ['a', 'b', 'c', 'd']
print("\nThis is a list of alphabets:")
print(list3)

# Accessing the list of items.
print(f"First element in the list3 is {list3[0]}")

# Multidimensional lists.
list_mdim = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_mdim[1][2]) # should print 6

# Mixed lists
list_mixed = [1, 2, 'a', 'b', 3, 4, 'abc']
print(list_mixed)

# Getting the length of the list
print(len(list_mixed))
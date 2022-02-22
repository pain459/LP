# list append demo

list1 = []
print('empty' if len(list1) == 0 else 'Not empty')

list1.append(0)
list1.append(1)

print(list1)

# Adding tuples to the list
list1.append((2, 3))
print(list1)

# adding another list to the list.
list2 = [4, 5]
list1.append(list2)
print(list1)

# reading second item from a tuple.
print(list1[2][1])  # Should print 3
# lambda function with map to five the squares for the numbers in a list.
list1 = [i for i in range(1, 11)]
list2 = list(map(lambda x: x ** 2, list1))
print(list2)
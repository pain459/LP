# lambda that returns products of elements of two lists
list1 = [i for i in range(1, 11)]
list2 = [i for i in range(11, 21)]

# if len(list1) == len(list2):
#     print("This shall execute.")

list3 = list(map(lambda x, y: x*y, list1, list2))

print(list3)
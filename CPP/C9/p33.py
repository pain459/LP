# Using map to give the squares of numbers
def square(n):
    return n ** 2


list1 = [i for i in range(1, 11)]
list2 = list(map(square, list1))

print(list2)
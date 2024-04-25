# using zip to unzip a list of tuples.

pairs = [('a', 1), ('b', 2), ('c', 3)]

letters, numbers = zip(*pairs)
print(letters)
print(numbers)
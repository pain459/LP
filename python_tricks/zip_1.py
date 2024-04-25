# Using zip to iterate over multiple iterables simultaneously

names = ['a', 'b', 'c']
numbers = [1, 2, 3]

for i, j in zip(names, numbers):
    print(f'{i} {j}')
from itertools import chain

x = [1, 2, 3, 4]
y = ['a', 'b', 'c', 'd']
z = [5, 6, 7, 8]

# chain the iterables together
chained_iterable = chain(x, y, z)

for i in chained_iterable:
    print(i, end=' ')
print('\n')
# using itertools to compute Cartesian product
from itertools import product

x = ['a', 'b', 'c', 'd']
y = [1, 2, 3, 4]

for i, j in product(x, y):
    print(f'{i} {j}')
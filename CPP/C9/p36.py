# Lambda that returns the product of elements of the list
from functools import reduce

x = [i for i in range(1, 11)]
result = reduce(lambda x, y: x*y, x)
print(result)


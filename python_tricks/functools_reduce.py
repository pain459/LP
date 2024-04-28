# To apply function to an iterable and accumulate the result.

import functools
import operator

# Example list of numbers:

numbers = [1, 2, 3, 4, 5, 6]

# Calculate the product of all numbers using functools.mul and operator.mul
product = functools.reduce(operator.mul, numbers)

print(product)
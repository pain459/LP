# Using where function
import numpy as np
a = np.array([1, 2, 3, 4, 5], int)
b = np.array([5, 4, 3, 2, 1], int)
# if a>b take element from a else from b
c = np.where(a > b, a, b)
print(c)
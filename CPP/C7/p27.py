# Using logical_and(), logical_or(), logical_not()
import numpy as np

a = np.array([1, 2, 3])
b = np.array([0, 2, 3])

c = np.logical_and(a > 0, a < 4)
print(c)
c = np.logical_or(b >= 0, b == 1)
print(c)
c = np.logical_not(b)
print(c)
# Comparing arrays
import numpy as np

a = np.array([1, 2, 3, 0])
b = np.array([0, 2, 3, 1])
d = np.array(['a', 'b', 'c'])
e = np.array(['a', 'd', 'f'])

c = a == b
print("Result of a = b:", c)
c = a > b
print("Result of a > b:", c)
c = a <= b
print("Result of a <= b:", c)

f = d == e
print("Result of d = e:", f)
f = d >= e
print("Result of d > e:", f)
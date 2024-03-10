# Slicing an array
import numpy as np

# Create array with elements 10 to 15
a = np.arange(10, 16)
print(a)

print(a.size)

print(a[1:6:3])

# not actual copy but same as
b = a[::]
print(b)
a[0] = 100
print(b)

b = a[:-2:]
print(b)
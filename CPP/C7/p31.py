# using view method for copying an array.
import numpy as np

a = np.arange(1, 6)
b = a.view()
print(a)
print(b)

b[0] = 99
print(a)
print(b)
# Using nonzero() function
import numpy as np
a = np.array([1, 2, 3, 4, -1, 0, 6, 0, 5], int)
# retrieve indices of non zero elements from a
b = np.nonzero(a)
print(b)

# display indices
for i in b:
    print(a[i])

# Print elements
print(a[b])
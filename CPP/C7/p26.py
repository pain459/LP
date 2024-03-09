# Using any() and all() functions.

import numpy as np

a1 = np.array([1, 2, 3, 4])
a2 = np.array([1, 2, 4, 5])

a3 = a1 < a2
print("Result of a1 > a2:", a3)

print("Check if any one element is true:", np.any(a3))
print("Check is all elements are true:", np.all(a3))

# Using any() in if statement.
if (np.any(a1>a2)):
    print("At least one element in a1 is greater than those in a2.")
# aliasing an array
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = a

print("Original array a:", a)
print("Copied array b:", b)

# modifying the array b
b[0] = 99

print("After modification.")
print("Original array:", a)
print("Modified array:", b)
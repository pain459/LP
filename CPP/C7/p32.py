# Copying an array
import numpy as np

a = np.arange(0, 10)
b = np.copy(a)

# Edit the array a
a[-1] = 100

# Print to see the changes to array a only.
print(a)
print(b)
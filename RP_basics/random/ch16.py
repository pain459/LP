# Scientific computing and graphing

# Use NumPy for matrix manipulation
# Classical way to do this.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for i in range(len(row)):
        row[i] = row[i] * 2

print(matrix)

# now we will touch matrix with numpy
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(2 * matrix)

second_matrix = np.array([[5, 4, 3], [7, 6, 5], [9, 8, 7]])
print(second_matrix - matrix)
print(second_matrix * matrix)
print(second_matrix @ matrix)

# Playing with numpy
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix.shape)
print(matrix.diagonal())
print(matrix.flatten())
print(matrix.transpose())
print(matrix.min())
print(matrix.max())
print(matrix.mean())
print(matrix.sum())

# Stacking and shaping arrays
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(np.hstack([A, B]))
print(np.vstack([A, B]))
print(A.reshape(9, 1))

# creating matrices on the fly
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix = matrix.reshape(3, 3)
print(matrix)
print(np.arange(11, 20).reshape(3, 3))
print(np.arange(1, 13).reshape(3, 2, 2))

# Using matplotlib for plotting graphs
from matplotlib import pyplot as plt
plt.plot([1, 2, 3, 4, 5])
plt.show()

xs = [1, 2, 3, 4, 5]
ys = [2, 4, 6, 8, 10]
plt.plot(xs, ys)
plt.show()

xs = [1, 2, 3, 4, 5]
ys = [3, -1, 4, 0, 6]
plt.plot(xs, ys)
plt.show()

plt.plot([2, 4, 6, 8, 10], "g-o")

# Plot multiple graphs on the same window.
from matplotlib import pyplot as plt
xs = [0, 1, 2, 3, 4]
y1 = [1, 2, 3, 4, 5]
y2 = [1, 2, 4, 8, 16]
plt.plot(xs, y1, "g-o", xs, y2, "b-^")

# Plot data from numpy arrays
from matplotlib import pyplot as plt
import numpy as np

array = np.arange(1, 6)
plt.plot(array)

# some matrices

from matplotlib import pyplot as plt
import numpy as np

data = np.arange(1, 21).reshape(5, 4)
plt.plot(data)

# Formats your plots to perfection.

from matplotlib import pyplot as plt
import numpy as np

days = np.arange(0, 21)
other_site = np.arange(0, 21)
real_python = other_site ** 2

plt.plot(days, other_site)
plt.plot(days, real_python)
plt.xticks([0, 5, 10, 15, 20])
plt.xlabel("Days of Reading")
plt.ylabel("Amount of python learned")
plt.title("Python learned reading real python vs other site")
plt.legend(["other site", "Real Python"])

# Some other types of plots

from matplotlib import pyplot as plt

xs = [1, 2, 3, 4, 5]
tops = [2, 4, 6, 8, 10]

plt.bar(xs, tops)

# bar chart with custom data.

from matplotlib import pyplot as plt

fruits = {
    "apples": 10,
    "oranges": 16,
    "bananas": 9,
    "pears": 4
}

plt.bar(fruits.keys(), fruits.values())

# Histograms
from matplotlib import pyplot as plt
from numpy import random

plt.hist(random.randn(100000000), 20)
# plt.savefig('hist.png')



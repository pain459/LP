# Operations on arrays

from array import *
from math import log

# Create an array with int values
# arr = array('f', [round(log(i, 2) ** 2, 2) for i in range(1, 10)])
# arr = array('f', [float("{:.2f}".format(log(i, 2) ** 2)) for i in range(1, 10)])
arr = array('f', [float(format(log(i, 2) ** 2, '.2f')) for i in range(1, 10)])
print(arr)
arr.append(30)
arr.insert(0, 143)
print(arr)
n = arr.index(9)
print(n)
# Convert array to list
list1 = arr.tolist()
print(list1)
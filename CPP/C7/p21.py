# Creating an array using logspace.
from numpy import *

arr = logspace(1, 4, 5)
# print('arr =', arr)

# Finding number of elements
n = len(arr)

# Repeat from 0 to n-1 times
for i in range(n):
    print('%.1f' % arr[i], end=' ')
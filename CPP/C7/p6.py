# Program to retrieve the elements via while loop

from array import *

x = array('i', [10, 20, 30, 40, 50])
# Find number of elements
n = len(x)
# display array using indexing
i = 0
while i < n:
    print(x[i], end=' ')
    i += 1

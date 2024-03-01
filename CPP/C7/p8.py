# Slicing the elements of an array
from array import *

# Creating an array of given range
x = array('i', [i for i in range(10)])

# slicing elements in certain range
for i in x[2:5]:
    print(i, end=' ')
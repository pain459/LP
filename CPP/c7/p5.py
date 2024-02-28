# accessing elements of an array using index

from array import *

a = array('i', [10, 20, 30, 40, 50])

# number of elements
n = len(a)

# Display array elements using indexing
for i in range(n):
    print(a[i], end=' ')

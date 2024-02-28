# Create one array from another array
import array
from array import *

a = array('i', [1, 2, 3, 4])
b = array(a.typecode, (i**2 for i in a))

print("The elements in array b squared are: ")
for i in b:
    print(i)
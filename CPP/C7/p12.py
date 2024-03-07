# Searching array for an element
from array import *
# Creating an empty array to store integers
x = array('i', [])
# Store elements into the array x
print("How many elements? ", end='')
n = int(input()) # accept input into n

for i in range(n):
    print("Enter element: ", end='')
    x.append(int(input())) # carrying the input from above line.

print("Original array: ", x)
# linear search or sequential search


#
# searching an array for an element - v2.0
from array import *
# create an empty array to store integers
x = array('i', [])
# Store elements into array x
print("Enter number of elements in an array: ", end='')
n = int(input())

for i in range(n):
    print('Enter the element: ', end='')
    x.append(int(input()))

print("Original array: ", x)

print("Enter element to be searched: ", end='')
s = int(input())
# Use index() method to give location of the element in the array
# We use try except statement here.

try:
    pos = x.index(s)
    print("Found at position: ", pos + 1)
except ValueError:
    print("Not found in an array.")
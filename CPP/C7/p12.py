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
print("Enter element to search: ", end='')
s = int(input()) # accept the element to be searched.
# linear search or sequential search
flag = False # This becomes true if element is found

for i in range(len(x)):
    if s == x[i]:
        print('Found at the position= ', i+1)
        flag =- True
    else:
        print("Not found in an array.")


#
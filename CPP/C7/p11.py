# Sorting using bubble sort technique
from array import *

# Create an empty array to store integers
x = array('i', [])

# Store elements into array x
print("Enter how many elements: ", end='')
n = int(input())  # accept the input into n

for i in range(n):
    print("Enter element: ", end='')
    x.append(int(input()))
print("Original array: ", x)

# bubble sort
flag = False  # When swapping is done, flag will be come true.
for i in range(n - 1):
    for j in range(n - 1 - i):
        if x[j] > x[j + 1]:
            t = x[j]
            x[j] = x[j + 1]
            x[j + 1] = t
            flag = True
    if flag == False:
        break
    else:
        flag = False
print('Sorted array = ', x)

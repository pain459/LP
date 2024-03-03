# percentage calculator program which will discard invalid entries into an array.
from array import *


def check_int(a):
    try:
        return int(a)
    except (TypeError, ValueError):
        pass


# lst = [int(i) for i in input("Enter the marks: ").split(',')]
lst = [check_int(i) for i in input("Enter the marks: ").split(',') if check_int(i) is not None]

# Create an array with given inputs
arr1 = array('i', lst)
# make the sum of values.
sum = 0
for i in arr1:
    sum += i
# display percentage
n = len(arr1)
percent = sum / n
print("Percentage: ", percent)
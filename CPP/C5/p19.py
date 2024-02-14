# Find the sum of even numbers

import sys

args = sys.argv[1:]
print(args)

sum = 0
for a in args:
    x = int(a)
    if x > 1 and x % 2 == 0:
        sum += x

print("Total sum is:", sum)
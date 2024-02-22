# To display even numbers between m and n
import sys

m, n = [int(i) for i in input("Enter minimum and maximum range separated by comma: ").split(',')]

if m < n:
    x = m
elif m == n:
    print("Found equal numbers. Exiting the program.")
    sys.exit(0)
else:
    x = n

'''Writing ternary operators is a pain.'''
# x = (m if m < n else (print("exiting"), sys.exit(0)) if m == n else n) if m < n else n

if x % 2 != 0:
    x += 1

while m <= x <= n:
    print(x)
    x += 2

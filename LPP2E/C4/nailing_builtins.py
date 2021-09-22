# To see the list command is dir(__builtins__)
# abs(x)
# Return the absolute value of a number. The argument may be an integer or a floating
# point number. If the argument is a complex number, its magnitude is returned.
from math import sqrt

abs(12)  # returns 12
abs(-125.5)  # returns 125.5
abs(12+4j)  # abs will return the median of the complex numbers.
# returns 12.649110640673518
# abs of complex numbers can be calculated as below traditionally.
sqrt((12 ** 2) + (4 ** 2))  # returns 12.649110640673518
# Doc at https://en.wikipedia.org/wiki/Complex_number#Polar_complex_plane


# all(iterable) & any(iterable)
# Return True if all elements of the iterable are true (or if the iterable is empty).
print(all([True, True, False, True]))
print(all([True, True, True]))
print(all([False, True, True, False]))
# Practical example.
list1 = []
list2 = []
for i in range(1, 21):
    list1.append(4 * i - 3)

for i in range(0, 20):
    list2.append(list1[i] % 2 == 1)

print("See whether all numbers in list1 are odd =>")
print(all(list2))

list3 = []
list4 = []
for i in range(1, 21):
    if i % 2 == 1:
        list3.append(i)

print(all(list3))  # our above logic is correct to calculate the odd number. Result is true.

# any(iterable)
# Return True if any element of the iterable is true. If the iterable is empty, return False.

print(any([True, True, False, True]))
print(any([True, True, True]))
print(any([False, True, True, False]))

# We can do a list comparison, but moving on.


# ascii(object)
# returns the printable string if ascii is provided.
ascii("Pythön")  # returns "'Pyth\\xf6n'"

# bin(x)
# Converts an integer number to a binary string prefixed with "0b"
bin(125)  # Returns a string with 0b prefix.
# returns '0b1111101'
# if we don't want the 0b suffix, here is the method.
# first with 0b
print(f'{14:#b}')  # returns 0b1110
print(f'{14:b}')  # returns 1110


# class bool([x])
bool(0)  # returns False
bool(1)  # returns True


# breakpoint(*args, **kws)

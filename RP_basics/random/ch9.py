# Tuples
#
# >>> first_tuple = (1, 2, 3, 4)
# >>> type(first_tuple)
# <class 'tuple'>
# >>> empty_tuple = ()
# >>> type(empty_tuple)
# <class 'tuple'>
# >>>

# Adding , will change the type.
# >>> x = (1)
# >>> type(x)
# <class 'int'>
# >>> x = (1,)
# >>> type(x)
# <class 'tuple'>
# >>>
# Work of the inbuilt function tuple.
# >>> tuple("Python")
# ('P', 'y', 't', 'h', 'o', 'n')
# >>> tuple(1, 2, 3)
# Traceback (most recent call last):
#   File "<pyshell#93>", line 1, in <module>
#     tuple(1, 2, 3)
# TypeError: tuple expected at most 1 arguments, got 3
# >>>
# >>> tuple(1)
# Traceback (most recent call last):
#   File "<pyshell#94>", line 1, in <module>
#     tuple(1)
# TypeError: 'int' object is not iterable
# >>>
# Working with assignments
# >>> x = tuple()
# >>> type(x)
# <class 'tuple'>
# >>> x
# ()
# >>>
# Other operations on tuples
# >>> numbers = (1, 2, 3)
# >>> len(numbers)
# 3
# >>> numbers[1]
# 2
# >>> word = tuple("university")
# >>> word
# ('u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')
# They support slicing.
# >>> word[2:5]
# ('i', 'v', 'e')
# Immutability
# >>> word[0] = "i"
# Traceback (most recent call last):
#   File "<pyshell#108>", line 1, in <module>
#     word[0] = "i"
# TypeError: 'tuple' object does not support item assignment
# >>>

# Tuples are iterable.
text = tuple("university")
print(text)
for i in text:
    print(i.upper())

# Third way of creating a tuple.
data = 1.25, 5.2, 7
print(type(data))  # This should return tuple.
x, y, z = data  # packed values should be equal to unpacked ones. Else we will observe ValueError
print(x)  # This should print 1.25

# Checking existence of values with in.
name = tuple("university")
if "e" in name:
    print("Found it!")
else:
    print("Letter not found!")


# Returning multiple values from a function.
def adder_sub(x, y):
    return (x + y, x - y)


adder_sub(3, 2)  # output is (5, 1)

# Review
cardinal_numbers = ("first", "second", "third")
print(cardinal_numbers[1])
position1, position2, position3 = cardinal_numbers
print(position1)  # This should print "first"
my_name = tuple("rkp")
print(my_name)
if "x" in my_name:
    print("Yes")
else:
    print("No")
my_name_2 = my_name[1:]
print(my_name_2)

# Diving into lists.
# Lists are mutable. Meaning we can edit the value in the list at given position.
colors = ["red", "yellow", "green", "blue"]
print(type(colors))

# Creating list from a string. list keyword to the rescue.
new_list = list("red")
print(new_list)

# Creating list from a tuple.
colors_tuple = ("red", "yellow", "green", "blue")
colors_list = list(colors_tuple)
print(colors_list)  # ['red', 'yellow', 'green', 'blue']

# Creating a list on the fly
groceries = "eggs, milk, cheese"
print(type(groceries))  # Expecting string and it is.
groceries_list = groceries.split(",")
print(groceries_list)
# Split is weird. We can split a string with any letter and create a list out of it.
name1 = "Pneumonoultramicroscopicsilicovolcanoconiosis"
# print(name1.split("o"))  # Lets save this to a new variable.

name2 = name1.split("o")
print(name2)
# Trying to split with something that don't exist.
list1 = "milk, cheddar, slime"
list1.split('x')

# Basic list operations
numbers = [1, 2, 3, 4]
print(numbers[1])  # returns 2 as it is in the index position 1
print(numbers[1:3])  # prints [2, 3] per index positions.
# pulling boolean response out of lists
print("x" in numbers)  # False
# Iterating over the list
numbers = [1, 2, 3, 4]
for i in numbers:
    if i % 2 == 0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")

# Changing elements in the list.
colors = ["red", "yellow", "green", "blue"]
colors[0] = "brown"
print(colors)  # returns ['brown', 'yellow', 'green', 'blue']
# Slicing the list.
print(colors[1:3])  # should print ["yellow", "green"]
print(colors)  # Actual list will stay as it is.

# List methods, adding and removing elements.
colors = ["red", "yellow", "green", "blue"]
colors.insert(1, "orange")  # insert orange in the index place 1 and rest will move towards the right.
print(colors)
colors.insert(10, "violet")  # if the index is out of range, it will insert at the end.
print(colors)
colors.insert(-1, "indigo")  # insert at the end.
print(colors)
colors.insert(-2, "purple")  # Actually inserted at -3.
print(colors)
# using pop
colors = colors.pop()  # pop and save the last one from the list.
print(colors)
# Some more testing.
colors = ["red", "yellow", "green", "blue"]
print(colors.pop())  # pop blue but the list is unchanged.
colors_2 = colors.pop()
print(colors_2)  # should print green as blue is popped earlier.

chars = ["a", "b", "c", "d"]
chars.append("e")
print(chars)
chars.extend(["f", "g"])
print(chars)

# Sum, max, min
n = [1, 2, 3, 4]
t = 0
for i in n:
    t += i
print(t)

n = [1, 2, 3, 4]
print(max(n))
print(min(n))
print(sum(n))

# Nesting lists and tuples.

two_by_two = [[1, 2], [3, 4]]
print(two_by_two[0])
print(two_by_two[0][1])  # should return 2

# Copying a list. quirk of OOP
list1 = ["a", "b", "c", "d"]
list2 = list1
list2.append("e")
# As both list1 and list2 are pointing to same object (list in this case).
# This is possible. This is not a clean copy.
print(list1)
print(list2)

# Clean copy
list1 = ["a", "b", "c", "d"]
list2 = list1[:]
list2.append("e")
print(list1)  # returns ['a', 'b', 'c', 'd']
print(list2)  # returns ['a', 'b', 'c', 'd', 'e']

# Sorting lists
list1 = ["b", "c", "a", "d"]
print(list1.sort())
print(list1)  # permanent change in the list

list1 = ["b", "c", "a", "d"]
print(sorted(list1))  # temporary sort.
print(list1)  # list1 unaffected.

# Dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = (("a", 1), ("b", 2), ("c", 3))
print(type(dict1))  # <class 'dict'>
print(type(dict2))  # <class 'tuple'>
dict3 = dict(dict2)
print(type(dict3))  # <class 'dict'>

# Accessing dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1['a'])  # returns 1

# Adding or removing values in a list.
dict1 = {"a": 1, "b": 2, "c": 3}
dict1["d"] = 4
print(dict1)

del dict1["d"]
print(dict1)  # removed 'd':4

# Checking the existence of keys.
dict1 = {"a": 1, "b": 2, "c": 3}
print("a" in dict1)  # returns true
print("d" in dict1)  # returns false

# Iterating over dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
for i in dict1:
    print(i)  # returns keys.
# Accessing values.
dict1 = {"a": 1, "b": 2, "c": 3}
for i in dict1:
    print(f"{i} value for key {dict1[i]}")



print('Today is a good day to learn python')
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')

#string concatenation
print("string1" + "string2")

# It works
print("""trying to connect these""" + " " + "two strings")

# storing in variables
greeting = "Hello!"
name = "Bruce Banner"
print(greeting + " " + "I'm " + name)

# Getting inputs
name = input("Please enter your name: ")
greeting = "Hello"
print(greeting + ", " + name + '!')

# Using input as a return
name = input("Please enter your name: ")
print('Hello, ' + name + '!')

# Assigning the variables directly and printing the return.
name = "Batman"
age = 24
print(name, age)

# this will give the type of datatype it is storing.
print(type(name))
print(type(age))

#rebinding
age = "2 years"
print(type(age))  # <class 'str'>

# Strongly typed language
a = 2
b = '2'
print(a + b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Doing this a bit more interactive.
a = 2
b = '2'
try:
    print(a + b)
except TypeError:
    print("Looks like you are doing something naughty. Python don't like this")
else:
    print("error occured!")
finally:
    print("Python is a strongly typed language")

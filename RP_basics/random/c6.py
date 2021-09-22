# In [15]: len = "I'm string now"
#
# In [16]: type(len)
# Out[16]: str
#
# In [17]: del len
#
# In [18]: type(len)
# Out[18]: builtin_function_or_method
#
# In [19]:

# Above we've done something with del keyword. Check later.

# Now we will observe one side effect of the function.

# In [19]: value = print("printing the value from function print")
# printing the value from function print
#
# In [20]: value
#
# In [21]: type(value)
# Out[21]: NoneType
#
# In [22]: print(value)
# None

def multiply(x, y):  # function signature
    # Function body begins
    product = x * y
    return product


# This is how we call a function.
print(multiply(10, 20))


# Function with no return statements.
def greet(name):
    # print(f"Hello {name}!")  # With this, we will observe the functional side effect.
    return f"Hello {name}"


print(greet("RRR"))


# Documenting what does the functions do is important.
def multiply(x, y):
    """Return the product of entered x and y"""
    result = x * y
    return result


print(help(multiply))


#  Challenges
def convert_cel_to_far(f):
    return f * (9 / 5) + 32


temp_c = eval(input("Enter the temperature in C: "))
print(f"{temp_c} degrees C = {convert_cel_to_far(temp_c)} degrees F")

# While loops
n = 1
while n < 5:  # test condition
    # loop body
    print(n)
    n = n + 1  # This will print 1 2 3 4 in line.

# Testing infinite loops.
num = float(input("Enter a positive number: "))
while num <= 0:
    print(f"{num} is not a positive number.")
    num = float(input("Enter a positive number: "))

#  For loops
for i in "python":  # membership expression
    # loop body
    print(i)

#  Above example in while loop.
word = "python"
index = 0
while index < len(word):
    print(word[index])
    index = index + 1

# Some more examples
for i in range(10):
    print("Python")  # prints Python word 10 times.

for n in range(10, 20):
    print(n * n)

# practical example of money sharing between 2, 3, 4, 5 people.
amount = eval(input("Enter the amount to be shared: "))
for i in range(2, 6):
    print(f"{i} people: ${amount / i:.2f} each")

# Nested loops.
for i in range(1, 4):
    for j in range(4, 7):
        print(f"i = {i} and j = {j}")

# Review exercises
for i in range(2, 10):
    print(i)

i = 2
while i < 11:
    print(i)
    i += 1


def doubles(x):
    return x * 2


n = eval(input("Please enter a number to print doubles of it: "))
for i in range(3):
    y = doubles(n)
    print(y)
    n = y


# Challenge: Track your investments
def invest(a, r, y):
    for i in range(1, y + 1):
        y_i = a + round((r * a), 2)
        print(f"year {i}: ${round(y_i, 2):.2f}")
        a = y_i


# def valuate(x, y):
#     if x <= 0:
#         print("Invalid entry. Please enter a positive number")
#         print(y)
#     else:
#         pass
# invest(100, 0.05, 10)
a = eval(input("Enter the amount of amount to be invested: "))
r = eval(input("Enter the annual interest offered by bank. ex 5% = 0.05 : "))
y = eval(input("Enter the number of years you are planning to invest: "))

invest(a, r, y)

# scopes
x = "Hello World!"  # Global scope


def func():
    x = 2  # Local scope
    print(f"Inside 'func', x has a value of {x}")


func()
print(f"outside 'func', x has a value of {x}")

# Scope resolution
x = 5


def outer_func():
    y = 3

    def inner_func():
        z = x + y
        return z

    return inner_func()


outer_func()  # This should return 8
# Breaking the rules
# This is a bad practice. But we can use to fix simple bugs.
total = 0
def add_to_total(n):
    global total
    total = total + n

add_to_total(5)
print(total)

# learning debugging
for i in range(1, 4):
    j = i * 2
    print(f"i is {i} and j is {j}")
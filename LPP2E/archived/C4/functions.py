# Fnctions
# Improve readibility.
# Matric multiplications
import sys


def matrix_mul(a, b):
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)]
            for r in a]


a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]
c = matrix_mul(a, b)


# Improve traceability
def calculate_price_with_vat(price, vat):
    return price * (100 + vat) / 100


calculate_price_with_vat(1950, 2)


# Scoped and name resolution
# Scoping level 1
def my_function():
    test = 1
    print('my_function:', test)


test = 0
my_function()  # prints 1
print('global:', test)  # prints 0, as test = 0 is declared at global scope.


# Scoping level 2
# Remember LEGB rule: local, enclosing, global, built-in
def outer():
    test = 1

    def inner():
        test = 2
        print('Inner:', test)

    inner()
    print('Outer:', test)


test = 9
outer()
print('global:', test)


# The global and nonlocal statements.
# Testing nonlocal

def outer():
    # nonlocal test
    test = 1  # outer scope

    def inner():
        # nonlocal test
        test = 2  # nearest enclosing scope. Which is outer.
        print('Inner:', test)

    inner()
    print('Outer:', test)


test = 0  # global scope
outer()
print('global:', test)


# Testing global
def outer():
    # nonlocal test
    test = 1  # outer scope

    def inner():
        global test
        test = 2  # nearest enclosing scope. Which is outer.
        print('Inner:', test)

    inner()
    print('Outer:', test)


test = 0  # global scope
outer()
print('global:', test)

# A bit deep into functions.

# Input parameters
# Argument-passing.
# Argument-passing is nothing more than assigning an object to a local variable
# name
x = 3


def func(y):
    print(y)


func(x)  # should return 3

# Assignment to argument names doesn't affect the caller
x = 3


def func(x):
    x = 7  # defining a local x, not changing the global one.


func(x)
print(x)  # prints 3

# Changing the mutable affects the caller.

x = [1, 2, 3]


def func(x):
    x[1] = 42  # This affects the caller.
    x = "This is a new string object!"  # Won't be printed as this creates new string object.


func(x)
print(x)  # returns [1, 42, 3]


# Specifying input parameters. We will see all 5 ways below.
# Positional arguments

def func(a, b, c):
    print(a, b, c)


func(1, 2, 3)  # prints 1 2 3


# keyword arguments and default values

def func(a, b, c):
    print(a, b, c)


func(a=1, c=2, b=3)  # Returns 1 3 2


# We are declaring the input arguments based on position.

# Now the defaults.
# Ordering is important. Defalult cannot be declared on the left side.
# positional arguments not honoured when arguments are scrambled.
def func(a, b=12, c=85):
    print(a, b, c)


func(1)  # Returns 1 12 85
func(1, 5)  # returns 1 5. Postion is also honoured.
func(2, c=5)  # returns 2 12 5. Honoruring position and the assignment.


# Variable positional arguments.
# This line will accept the list/tuple. But logic works only for tuple.
def minimum(*n):
    print(type(n))  # print the input type. In this case tuple.
    if n:  # Collection of objects returns true. Empty one returns false.
        mn = n[0]  # assigning the first value of tuple to variable mn
        for value in n[1:]:  # cycling a loop across the rest the tuple.
            if value < mn:  # comparing if first value from the loop is less than mn
                mn = value  # If less, update value at mn
        print(mn)  # at the end, print the value mn. Which is the minimum.


minimum(1, 8, 9, -7)

x = (1, 8, 9, -7)
min(x)  # the entire program can be written in a single line min(x), where x is a tuple.


# Unpacking a tuple.
def func(*args):
    print(args)


values = (1, 8, 9, -7)
func(values)  # returns ((1, 8, 9, -7),)
func(*values)  # returns (1, 8, 9, -7). This method is called unpacking.


# Variable keyword arguments.
# Variable keyword arguments are very similar to variable positional arguments. The only
# difference is the syntax (** instead of *) and that they are collected in a dictionary.
# Collection and unpacking work in the same way.

def func(**kwargs):
    print(kwargs)


# All calls equivalent. They print: {'a': 1, 'b': 42}
func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))


# Importance of variable keyword arguments.
# Fictional program.
def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', 'username'),
        'pwd': options.get('pwd', 'password'),
    }
    print(conn_params)


connect()
connect(host='10.0.0.11', port=1452)
connect(user='kumarrav')


# Last way:  Keyword only argument
# Rarely used in Python 3.
def kwo(*a, c):
    print(a, c)


kwo(1, 2, 3, 4, c=100)
kwo(c=4)


# multikeyword arguments
def kwo2(a, b=42, *, c):
    print(a, b, c)


kwo2(12, b=12, c=1)


# Combining input parameters
# pattern(name positional arguments, default arguments, variable positional arguments \
# , keyword only arguments, variable keyword arguments.

# When defining a function, normal positional arguments come first (name), then
# any default arguments (name=value), then the variable positional arguments
# (*name or simply *), then any keyword-only arguments (either name or
# name=value form is good), and then any variable keyword arguments (**name).
def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)


# Above example:
# a, b  are positional arguments.
# c is a default argument
# *args is a variable position argument
# **kwargs is a variable keywords argument.
func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
func(1, 2, 3, 5, 7, 9, A='a', B='b')  # same output as above.


# Including keyword arguments.
def func(a, b, c=7, *args, d, e=256, **kwargs):
    print('positional arguments a, b, c: ', a, b, c)
    print('variable position argument args: ', args)
    print('keyword only arguments d, e: ', d, e)
    print('variable keyword arguments kwargs: ', kwargs)


func(1, 2, 3, *(5, 7, 9), d=10, e=11, **{'A': 'a', 'B': 'b'})
func(1, 2, 3, 5, 6, 7, d=10, e=11, A='a', B='b')  # same as above.


# Additional unpacking generalizations
def additional(*args, **kwargs):
    print(args)
    print(kwargs)


args1 = (1, 2, 3)
args2 = [4, 5]
kwargs1 = dict(option1=10, option2=20)
kwargs2 = {'option3': 30}
additional(*args1, *args2, **kwargs1, **kwargs2)


# Avoid the trap! Mutable defaults
def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))
    b[len(a)] = len(a)


func()
func()
func()


# defaults retained after calling functions with other values.
def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))
    b[len(a)] = len(a)


func()
func(a=[1, 2, 3], b={'B': 1})
func()


# Return values

# defining factorial with return values
def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(2, n):
        result *= k
    return result


factorial(12)

# function to return factorial
from functools import reduce
from operator import mul


def factorial(n):
    # similar to declaring a variable equals 1 and then iterating across.
    return reduce(mul, range(1, n + 1), 1)


factorial(5)

# Simple factorial math.
j = 1
for i in range(1, 3):
    j = j * (i + 1)
print(j)

# introducing mul
from operator import mul

j = 1
for i in range(1, 6):
    j = mul(j, i + 1)
print(j)

# Now using reduce and mul together.

from functools import reduce
from operator import mul

n = 5
print(reduce(mul, range(1, 1 + n), 1))


# returning multiple values

def moddiv(a, b):
    """This function will return the values"""
    return a % b, a // b


# can be returned as tuple
j = moddiv(12, 2)
# can call individual objects if needed.
help(moddiv)


# recursive functions
# This function will feed in the n-1 into function and multiply until 1 is returned after decrementing.

def factorial(n):
    if n in (0, 1):
        return 1
    return factorial(n - 1) * n


factorial(5)


# One more example. Sum of n numbers.
def sum_of_n(n):
    if n == 0:
        return 0
    return sum_of_n(n - 1) + n


sum_of_n(25)

# recursion limit.
sys.getrecursionlimit()  # 3000 default
sys.setrecursionlimit(4000)  # we can set the recursion limit.


# Anonymous functions
# Also called as lambdas in python
def is_multiple_of_five(n):
    return not n % 5  # this statement will return True if n % 5 is 0.


#                       Cashing on the not keyword. Not false = true
# Get multiples of 5
def get_multiples_of_five(n):
    # The filter function below is interesting.
    return list(filter(is_multiple_of_five, range(n)))


get_multiples_of_five(100)


# Using lambda to reduce the bool deciding function.
def get_multiples_of_five(n):
    # defining a lambda
    # func_name = lambda [parameter_list]: expression
    # def func_name([parameter_list]): return expression
    return list(filter(lambda k: not k % 5, range(1, n)))


get_multiples_of_five(50)


# One more example.
def adder(a, b):
    return a + b


adder_lambda = lambda a, b: a + b
adder_lambda(10, 20)


# One more example.
def to_upper(a):
    return a.upper()


to_upper_lambda = lambda a: a.upper()


# Function attributes.
#  I didn't understand this yet.
def multiplication(a, b=1):
    """Return a multiplied by b. """
    return a * b


special_attributes = ["__doc__", "__name__", "__qualname__", "__module__",
                      "__defaults__", "__code__", "__globals__", "__dict__",
                      "__closure__", "__annotations__", "__kwdefaults__",
                      ]

for i in special_attributes:
    print(i, '=>', getattr(multiplication, i))

# get all builtin modules
dir(__builtins__)

# One final example

from math import sqrt, ceil

def get_primes(n):
    """Calculate a list of primes up to n (included)"""
    primelist = []
    for candidate in range(2, n + 1):
        is_prime = True
        root = ceil(sqrt(candidate))  # division limit

        for prime in primelist:  # we try the primes
            if prime > root:  # no need to check any further
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
    return primelist

get_primes(152)
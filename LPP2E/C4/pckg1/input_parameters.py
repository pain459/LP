# Positional arguments
def func(a, b, c):
    print(a, b, c)


func(1, 2, 3)  # Prints: 1 2 3


# keyword arguments and default values
# assignment while using function.
def func(a, b, c):
    print(a, b, c)


func(1, c=3, b=2)  # returns: 1 2 3


# assignment while declaring function.
def func(a, b=1, c=2):
    print(a, b, c)


func(1)  # prints 1 1 2
func(1, 2)  # prints 1 2 2
func(1, 2, 3)  # prints 1 2 3


# def func(a, b=2, c):
#     print(a, b, c)
# non-default argument follows default argument. Hence this declaration is invalid.

# def func(b=1, c=2, 43):
#     print(b, c, 43)
# Invalid syntax. Positional argument follows after keyword one.

# Variable position arguments
def minimum(*n):
    print(type(n))  # expected to be tuple
    if n:
        mn = n[0]  # declaring a new variable with value of first from input tuple
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)


minimum(1, 9, -2, -8)
minimum()

n = (1, 2, 3, 4)
bool(n)


# Variable keyword arguments.
def func(**kwargs):
    print(kwargs)


func(a=1, b=2)
func(**{'a': 1, 'b': 2})
func(**dict(a=1, b=2))


# One more example

def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)


connect()
connect(host='127.0.0.42', port=5000)


# Keyword-only arguments
def kwo(*a, c):
    print(a, c)


kwo(1, 2, 3, c=7)
kwo(c=4)


# kwo(1, 2)  # Returns error.4


# One more example
def kwo2(a, b=42, *, c):
    print(a, b, c)


kwo2(3, b=7, c=99)  # prints 3 7 99
kwo2(3, c=10)  # prints 3 42 10
kwo2(3, 23, c=10)  # 3 23 10


# Combining input params.
# order to define in a single line.

def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})


# One more example with keyword arguments this time.
def func_with_kwonly(a, b=42, *args, c, d=256, **kwargs):
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('args:', args)
    print('kwargs:', kwargs)


func_with_kwonly(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F')
func_with_kwonly(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F')


# Additional unpacking generalizations
def additional(*args, **kwargs):
    print(args)
    print(kwargs)


args1 = (1, 2, 3)
args2 = [4, 5]
kwargs1 = {'a': 6, 'b': 7}
kwargs2 = dict(c=8, d=9)

additional(*args1, *args2, **kwargs1, **kwargs2)


# returning multiple values
def mod_div(a, b):
    return a // b, a % b


mod_div(22, 7)


# Recursive functions.
def factorial(n):
    if n in (0, 1):
        return 1
    return factorial(n - 1) * n


factorial(100)


# Anonymous functions
# filter.regular.py
def is_multiple_of_five(n):
    return not n % 5


def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))


# Using lambda
def get_multiples_of_five2(n):
    return list(filter(lambda k: not k % 5, range(n)))

get_multiples_of_five2(100)
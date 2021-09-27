# We will be covering
# 1. The map, zip, and filter functions
# 2. Comprehensions
# 3. Generators

# Wrapping code of list constructor. Using aliases.
# traditional
import math

range(7)  # Will return range(0, 7)
list(range(7))  # [0, 1, 2, 3, 4, 5, 6]
# Using aliases
_ = list
_(range(7))  # [0, 1, 2, 3, 4, 5, 6]


# The map, zip and filter functions.
# Refresher for lambda
# example 1: adder
def adder(a, b):
    return a + b


# is equivalent to:
adder_lambda = lambda a, b: a + b


# example 2: to uppercase
def to_upper(s):
    return s.upper()


# is equivalent to:
to_upper_lambda = lambda s: s.upper()

# map_example
_ = list
_(map(lambda *a: a, range(3)))
_(map(lambda *a: a, range(3), 'abc'))
_(map(lambda *a: a, range(3), 'abc', range(4, 7)))
# Map stops at the shortest iterator
_(map(lambda *a: a, (), range(3), 'abc'))  # returns [] as () is the shortest iterator.
# It stops at the shortest. Which means 'def' is the max length it can go.
_(map(lambda *a: a, range(5), 'abcde', range(5, 10), 'def'))

# decorate.sort.undecorate.py
# Need to read it somewhere else.

# Zip
# Zip.grades.py
_ = list
grades = [18, 23, 43, 56]
avgs = [22, 21, 34, 23]
_(zip(avgs, grades))
# I can write this as lambda too.
_(map(lambda *a: a, avgs, grades))

# maxims.py
a = [5, 9, 2, 4, 7]
b = [1, 4, 5, 3, 2]
c = [6, 8, 9, 3, 4]
_ = list
maxs = map(lambda n: max(*n), zip(a, b, c))
_(maxs)

# Filter
# filter.py
test = [2, 5, 6, 0, 0, 3, 5, 0, 8]
_ = list
_(filter(None, test))
_(filter(lambda x: x, test))  # equivalent of the above
_(filter(lambda x: x > 4, test))  # returns the values greater than 4.

# Comprehensions
# squares.map.py
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

# Doing this in lambda way
_ = list
squares = map(lambda i: i ** 2, range(10))
_(squares)

# squares.comprehension.py
__ = [i ** 2 for i in range(10)]
print(__)

# Even squares
_ = list
even_squares = map(lambda n: n ** 2, filter(lambda n: n % 2, range(10)))
# Filter gives the values and Map gives the pattern.
print(_(even_squares))

# Using list comprehensions
sq2 = [i ** 2 for i in range(10) if not i % 2]
print(sq2)

# Nested comprehensions
# pairs.for.loop.py
items = 'ABCD'
pairs = []
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))
print(pairs)

# pairs.list.comprehensions.py
items = 'ABCD'
pairs = [(items[i], items[j])
         for i in range(len(items)) for j in range(i, len(items))]
print(pairs)


# Skipping some other types of comprehensions for future reference.

# Starting with generator functions.
# first.n.squares.py
# traditional approach
def get_squares(n):
    return [i ** 2 for i in range(n)]


print(get_squares(10))


# generator approach
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2  # we yield, we don't return in generators.


print(list(get_squares_gen(10)))


# first.n.squares.manual.py
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2


squares = get_squares_gen(4)
print(squares)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


# gen.yield.return.py
def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q ** k
        if result <= 1000000:
            yield result
        else:
            return
        k += 1


for i in geometric_progression(2, 5):
    print(i)


# first.n.squares.manual.method.py
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2


squares = get_squares_gen(3)
print(squares.__next__())
print(squares.__next__())
print(squares.__next__())
print(squares.__next__())


# gen.send.preparation.py
def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))

# gen.send.preparation.stop.py
stop = False


def counter(start=0):
    n = start
    while not stop:
        yield n
        n += 1


c = counter()
print(next(c))
print(next(c))
print(next(c))
stop = True
print(next(c))


# gen.send.py
def counter(start=0):
    n = start
    while True:
        result = yield n
        print(type(result), result)
        if result == 'Q':
            break
        n += 1


c = counter()
print(next(c))
print(c.send('Wow!'))
print(next(c))
print(c.send('Q'))


# gen.yield.for.py
def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2


for n in print_squares(2, 5):
    print(n)


# gen.yield.from.py  Using the yield from expression.
def print_squares(start, end):
    yield from (n ** 2 for n in range(start, end))


for n in print_squares(2, 5):
    print(n)

# Generator expression.
# We will see some difference between generator expressions and normal iterations.
cubes = [i ** 3 for i in range(10)]
print(cubes)  # will receive [0, 1, 8, 27, 64, 125, 216, 343, 512, 729] as a list.
type(cubes)  # <class 'list'>

# Using generator.
_ = list
cubes_gen = (i ** 3 for i in range(10))
print(cubes_gen)  # prints memory location <generator object <genexpr> at 0x000001A932CBB448>
print(_(cubes_gen))  # prints [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print(_(cubes_gen))  # returns empty list as the o/p is now exhausted.

# gen.map.py
def adder(*n):
    return sum(n)


s1 = sum(map(lambda *n: adder(*n), range(100), range(1, 101)))
print(s1)

# Using a filter
_ = list
cubes = [x ** 3 for x in range(10)]

odd_cubes1 = filter(lambda cube: cube % 2, cubes)
print(_(odd_cubes1))

odd_cubes2 = (cube for cube in cubes if cube % 2)
print(_(odd_cubes2))


# Dealing with some memory intensive calculations.
# sum.example.2.py
s = sum([i**2 for i in range(10**8)])  # This might kill some small machines.
print(s)

# Optimised way with generators.
s1 = sum(i**2 for i in range(10**8))  # This succeeds. Oh generator you beauty.
print(s1)  #prints 333333328333333350000000

# Performance considerations.
# performances.py
from time import time
mx = 5000

t = time()  # start time for the for loop
floop = []
for a in range(1, mx):
    for b in range(a, mx):
        floop.append(divmod(a, b))
print('for loop: {:.4f} s'.format(time() - t))  # elapsed time

t = time()  # Start time for list comprehension.
compr = [
    divmod(a, b) for a in range(1, mx) for b in range(a, mx)]
print('list comprehension: {:.4f} s'.format(time() - t))

t = time()
gener = list(
    divmod(a, b) for a in range(1, mx) for b in range(a, mx))
print('generator expression: {:.4f} s'.format(time() - t))

# Examples comparing for loop and a map call
# performances.map.py
from time import time
mx = 2 * 10 ** 7

t = time()
absloop = []
for n in range(mx):
    absloop.append(abs(n))
print('for loop: {:.4f} s'.format(time() - t))

t = time()
abslist = [abs(n) for n in range(mx)]
print('list comprehension {:.4f} s'.format(time() - t))

t = time()
_ = list
absmap = _(map(abs, range(mx)))
print('map: {:.4f} s'.format(time() - t))

# pythagorean.triple.generation.for.py
import math
from time import time

def gen_triples(N):
    for m in range(1, int(N**.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 and math.gcd(m, n) == 1:
                c = m**2 + n**2
                if c <= N:
                    a = m**2 - n **2
                    b = 2 * m * n
                    yield (a, b, c)

t = time()
triples = sorted(
    gen_triples(500), key=lambda *triple: sum(*triple))
print('time taken for execution {:.4f} s'.format(time() - t))
print(triples)


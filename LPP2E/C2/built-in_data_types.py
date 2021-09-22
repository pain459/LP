# doing the full chapter.
# Topics
# Python objects' structures
# Mutability and immutability
# Built-in data types: numbers, strings, sequences, collections, and mapping types
# The collections module
# Enumerations

# Mutable of immutable?
# Observe the ID changes for both assignments.
import collections

age = 42
print(age)
print(id(age))
age = 43
print(age)
print(id(age))

# Checking this with class.

class Person():
    def __init__(self, age):
        self.age = age

fab = Person(age = 42)
fab.age
id(fab)
id(fab.age)
fab.age = 25
id(fab)
id(fab.age)

# Numbers
a = 14
b = 3
a + b
a - b
a * b
a / b  # Tree division
a // b  # integer division
a % b  # modulo operation (remainder of division)
a ** b  # power operation

int(1.75)  # returns 1. Rounding towards 0.
int(-1.75)  # returns -1. Truncation done towards 0.

# feature. we can add underscores between numbers.
n = 1_024
n  # returns 1024
hex_n = 0x_4_0_0
hex_n  # 1024. As 0x400 == 1024 in hex.

# Booleans
int(True)  # returns 1, as True behaves like 1
int(False)  # returns 0
bool(1)  # returns True
bool(-42)  # returns True. And so every non-zero number
bool(0)  # returns false.
not True  # False
not False  # true
True and True  # true
False or True  # true
# Upcasting.
1 + True  # Returns 2. As True = 1
False + 42  # returns 42 as False = 0

# Real numbers
# Python supports only double format.
pi = 3.1415926536
radius = 4.5
area = pi * (radius ** 2)
area

# Verify how floating point behaves in your system.
import sys
sys.float_info

# Approximation issues of double precision number.
0.3 - 0.1 * 3  # Returns -5.551115123125783e-17

# Complex numbers
c = 3.14 + 2.73j
c.real
c.imag
c.conjugate()
c * 2
# c ** 2d
d = 1 + 1j
c - d
c * d
c / d

# Fractions and decimals.
# Fractions
from fractions import Fraction
Fraction(10, 6)
Fraction(1, 3) + Fraction(2, 3)
f = Fraction(10, 6)
f.numerator
f.denominator

# decimals
# Decimal numbers come at a price in performance. The amount of data
# stored for each number is far greater than fractions or floats.
from decimal import Decimal as D
D(3.14)
print(D('3.14'))
D(0.1) * D(3) - D(0.3)  # returns the number with double precision issue.
print(D('0.1') * D(3) - D('0.3'))  # only decimal points to be under ' '. Result returns 0.0
D('1.4').as_integer_ratio()  # provides result 7/5 as (7, 5)

# Immutable sequences

# Strings and bytes
# 4 ways to make a string.
str1 = 'This is a string. We built it with single quotes.'
str2 = "This s also a string, but built with double quotes."
str3 = '''This is a string suing triple quotes,
... so it can span multiple lines.'''
str4 = """This too is a multiline one
... but using a triple double quotes."""
str4  # this is auto formatted with required /n and etc.
print(str4)  # output is formatted.
len(str1)  # returns the length of the string.

# Encoding and decoding strings.
s = "This is üŋíc0de"
type(s)
encoded_s = s.encode('utf-8')  #  utf-8 encoded version of s
print(encoded_s)  # results in byte object.
encoded_s.decode('utf-8')  # reverting back to original.
# Creating a bytes class object.
bytes_obj = b"A bytes object"
type(bytes_obj)  #return bytes

# Indexing and slicing strings.
s = "The trouble is you think you have time."
s[0]  # return T. String index at 0
s[5]  # return r
s[:4].strip()  # return 'The '. Using strip to chop off the white space.
s[4:]  # return 'trouble is you think you have time.'. We will specify only the stop position.
s[2:14]  # return 'e trouble is'
s[2:14:3]  # slicing, start, stop and step (evey 3 chars)
s[:]  # quick method to make a copy of a string.

# String formatting. All 4 possibilities
greet_old = 'Hello %s!'  # deprecated method.
greet_old % 'Fabrizio'  # returns 'Hello Fabrizio!'

greet_positional = 'Hello {} {}!'
greet_positional.format('Fabrizio', 'Romano')  # return 'Hello Fabrizio Romano!'

greet_positional_idx = 'This is {0}! {1} loves {0}!'
greet_positional_idx.format('Python', 'Fabrizio')
# Above statement returns 'This is Python! Fabrizio loves Python!'
greet_positional_idx.format('Coffee', 'Ravi')
# Above statement returns 'This is Coffee! Ravi loves Coffee!'
keyword = 'Hello, my name is {name} {last_name}'
keyword.format(name='Fabrizio', last_name='Romano')
# Above statement returns 'Hello, my name is Fabrizio Romano'

# new feature in python 3.6
# formatted string literals.
name = 'Fab'
age = 42
print(f"Hello! My name is {name} and I'm {age}")

from math import pi
print(f"No arguing with {pi}, it's irrational..")


# Tuples
t = ()  # empty tuple
one_element_tuple = (42, )  # comma , is mandatory.
three_elements_tuple = (1, 2, 3)
a, b, c = 1, 2, 3  # Tuple for multiple assignments.
a, b, c  # returns the tuple of (1, 2, 3)
3 in three_elements_tuple  # returns True bool response.
# Testing one line swaps with tuples
# traditional
a, b = 1, 2
c = a
a = b
b = c
a, b
# with tuples in python
a, b = 1, 2
a, b = b, a
a, b  # returns (2, 1)


# Mutable sequences.
a = [] # empty list
a = list() # same as above. Empty list.
a = [1, 2, 3]  # declaring a list.
a = [i + 5 for i in a]  # list comprehension.
print(a)  # returns [6, 7, 8]
# Above can also be return as below.
a = [1, 2, 3]  # for representation.
[i + 5 for i in [1, 2, 3]]  # returns the same [6, 7, 8]
# Creating a list from tuple.
a = (1, 2, 3)
list(a)  # returns [1, 2, 3]
# list from a string.
a = "hello"
list(a)  # returns ['h', 'e', 'l', 'l', 'o']

# playing with lists.
a = [1, 2, 3, 4]
a.append(13)
print(a)  # [1, 2, 3, 4, 13]
a.count(1)  # 1, there is only 1 one in the list.
a.extend([5, 7])  # extending the list by 2 other values again in a list.
print(a)  # [1, 2, 3, 4, 13, 5, 7]
a.insert(0, 17)  # insert value 17 at position 0
print(a)  # [17, 1, 2, 3, 4, 13, 5, 7]
a.pop()  # pop the last value from the list.
print(a)  # [17, 1, 2, 3, 4, 13, 5]
a.pop(3)  # pop the element at position 3.
print(a)  # [17, 1, 2, 4, 13, 5]
a.remove(17)  # remove the element with value 17
print(a)  # [1, 2, 4, 13, 5]
a.reverse()  # reverse the list.
print(a)  # [5, 13, 4, 2, 1]
a.sort()  # sort the elements per value. Low to high.
print(a)  # [1, 2, 4, 5, 13]
a.clear()  # Remove all values from the list.
print(a)  # []
# power of lists main methods.
a = list('hello')  # makes a list from a string.
print(a)  # ['h', 'e', 'l', 'l', 'o']
a.append(100)  # append 100, heterogeneous type
print(a)  # ['h', 'e', 'l', 'l', 'o', 100]
a.extend((1, 2, 3))  # Extending using a tuple
print(a)  # ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3]
a.extend('...')  # Extending using a string.
print(a)  # ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3, '.', '.', '.']
# common operations to do in a list.
a = [1, 3, 5, 7]
min(a)  # 1
max(a)  # 7
sum(a)  # 16
len(a)  # 4
b = [6, 7, 8]
# Operator overloading.
a + b  # [1, 3, 5, 7, 6, 7, 8]
a * 2  # [1, 3, 5, 7, 1, 3, 5, 7]

# Power of sorted.
from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]  # list of tuples
sorted(a)  # temporary sort. Sort based on the first value at a tuple in ascending order.
# Sorting with the position 0
sorted(a, key=itemgetter(0))  # [(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]
# Sorting with position 0 and 1 in a tuple
sorted(a, key=itemgetter(0, 1))  # [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
# Sorting with position 1 in tuple.
sorted(a, key=itemgetter(1))  # [(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
# reversing the elements after sorting with position 1
sorted(a, key=itemgetter(1), reverse=True)  #[(4, 9), (5, 3), (1, 3), (1, 2), (2, -1)]
# Timsort is a stable sorting
# algorithm, which means that when multiple records have the same key, their original order
# is preserved.

# Byte arrays
# empty byte array object.
bytearray()  # bytearray(b'')
# zero filled instances with given length
bytearray(10)  # bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
# bytearray of iterable integers
bytearray(range(5))  # bytearray(b'\x00\x01\x02\x03\x04')
name = bytearray(b'Lina')  # Byte array from bytes
name.replace(b'L', b'l')  # bytearray(b'lina')
name.endswith(b'na')  # True
name.upper()  # bytearray(b'LINA')
name.count(b'L')  # 1


# Set types
# These are basic mathematical sets only.
small_primes = set()  # empty set
small_primes.add(2)  # adding value to the set.
small_primes.add(3)
small_primes.add(5)
small_primes  # {2, 3, 5}
small_primes.add(1)  # will be removed using remove
small_primes  # {1, 2, 3, 5}
small_primes.remove(1)
small_primes  # {2, 3, 5}
3 in small_primes  # True. membership test.
4 in small_primes  # False
4 not in small_primes  # True
small_primes  # {2, 3, 5}
small_primes.add(3)
small_primes  # {2, 3, 5} remains same. Duplication not allowed.
bigger_primes = set([5, 7, 11, 13])  # quick set creation.
small_primes | bigger_primes  # {2, 3, 5, 7, 11, 13} Using union operator
small_primes & bigger_primes  # {5}. Intersection operator.
small_primes - bigger_primes  # {2, 3} difference operator
bigger_primes - small_primes  # {7, 11, 13} reversing above.
# set creation. Notice the elimination of duplicates.
small_primes = {2, 3, 3, 5, 5, 7, 11}
small_primes  # {2, 3, 5, 7, 11}

# now the frozen sets.
small_primes = frozenset([2, 3, 5])
small_primes.add(7)  # will throw an attribute error as we are trying to add object to frozen set.
bigger_primes = frozenset([5, 7, 11])
small_primes | bigger_primes  # frozenset({2, 3, 5, 7, 11})
# All set operations are allowed here.

# Mapping types - Dictionaries

# 5 ways of creating dictionaries
a = dict(A=1, Z=-1)
print(a)  # {'A': 1, 'Z': -1}
b = {'A': 1, 'Z': -1}
c = dict([('A', 1), ('Z', -1)])
d = dict(zip(['A', 'Z'], [1, -1]))
e = dict({'Z': -1, 'A': 1})
print(a == b == c == d == e)  # returns True

# one more example on zip
a = list('abcde')
print(a)
b = [i for i in range(1, 6)]
print(b)
c = dict(zip(a, b))
print(c)
# one more

list(zip('hello', range(1, 6)))
# Returns [('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]

# Basic operations with dict
d.clear()  # cleared as there are some stale values from earlier example.
d = {}  # empty dictionary
d['a'] = 1  # added 'a':1 to dict
d['b'] = 2
print(d)   # returns {'a': 1, 'b': 2}
len(d)  # of course 2 values.
del d['a']  # removes a
print(d)  # remaining {'b': 2}
d['c'] = 3
d  # returns {'b': 2, 'c': 3}
'c' in d  # membership check. Returns True
2 in d  # Returns False. As we cannot check the membership of values.
d.clear()  # removing stale data.

# Using .keys, .values, .items in dict
d = dict(zip('hello', range(5)))  # notice that keys are unique. So, one l in hello will be eliminated.
print(d)  # returns {'h': 0, 'e': 1, 'l': 3, 'o': 4}. Clever!
d.keys()  # dict_keys(['h', 'e', 'l', 'o'])
d.values() # dict_values([0, 1, 3, 4])
d.items()  # dict_items([('h', 0), ('e', 1), ('l', 3), ('o', 4)])
3 in d.values()  # Returns true
('o', 4) in d.items()  # Returns True
d.clear()  # cleanup
# Playing with pop on dictionary
d = dict(zip('hello', range(5)))
print(d)  # {'h': 0, 'e': 1, 'l': 3, 'o': 4}
d.popitem()
print(d)  # {'h': 0, 'e': 1, 'l': 3}
d.pop('l')  # Popped the key l and its value.
print(d)  # {'h': 0, 'e': 1}
d.pop('z', 100)  # returns 100. No changes done but I will see this as a side effect.
d.update({'Z': 5})
print(d)
d.get('e')  # returns 1 which is the key for 'e'
d.get('b', 100)  # we will get 100 that is default. Neither the key exist at the dict nor the value.
# set default method on dictionary.
d.clear()
d = {}
d.setdefault('a', 1)
d
d.setdefault('a', 5) # Statement completes but no override expected. It will return 1 only.
d  # returned {'a': 1}. No override expected.
# Knowledge test
d.clear()
d = {}
d.setdefault('a', {}).setdefault('b', []).append(1)
d

# Collections module
# namedtuple
from collections import namedtuple
Vision = namedtuple('Vision', ['left', 'right'])
Vision = Vision(9.5, 8.8)
Vision[0]
Vision.left
Vision.right
 # We can easily update the tuple and proceed with calls.
 # With this approach, we can easily call the required values from tuple and avoid the overhead of positional arguments.
Vision = namedtuple('Vision', ['left', 'center', 'right'])
Vision = Vision(9.5, 9.2, 8.8)
Vision.left  # 9.5
Vision.right  # 9.2
Vision.center  # 8.8

# defaultdict
# Update the existing values or create the value if it don't exist starting from 0.
# Classical approach
d.clear()
d = {}
d['age'] = d.get('age', 0) + 1
d  # we will get reply as {'age': 1}
d.clear()
d = {'age': 39}
d['age'] = d.get('age', 0) + 1
d  # {'age': 40}  # As there is a value of 39 already, 1 will be added.

# using defaultdict
from collections import defaultdict
dd = defaultdict(int)  # Int is the default type. 0 is the value.
dd['age'] += 1
dd  # returns defaultdict(int, {'age': 1})

# ChainMap
from collections import ChainMap
default_connection = {'host': 'localhost', 'port': 4567}
connection = {'port':5678}
conn = ChainMap(connection, default_connection)
print(conn)  # ChainMap({'port': 5678}, {'host': 'localhost', 'port': 4567})
conn['host']  # returns 'localhost'
conn.maps  # we can see the mapping objects.
# returns [{'port': 5678}, {'host': 'localhost', 'port': 4567}]
conn['host'] = 'packtpub.com'  # adding a host
conn.maps  # returns [{'port': 5678, 'host': 'packtpub.com'}, {'host': 'localhost', 'port': 4567}]
# conn['host'] = 'localhost'
del conn['port']  # removing post information.
conn.maps  # returns [{'host': 'packtpub.com'}, {'host': 'localhost', 'port': 4567}]
conn['port']  # returns 4567
dict(conn)  # returns {'host': 'packtpub.com', 'port': 4567}
# moral: didn't understand.


# Enums

# Traditional
GREEN = 1
YELLOW = 2
RED = 4
TRAFFIC_LIGHTS = (GREEN, YELLOW, RED)  # or as below.
traffic_lights = {'GREEN': 1, 'YELLOW': 2, 'RED': 4}
# Nothing special about this code. Lets use enum.

# using enum
from enum import Enum
class TrafficLight(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 4

TrafficLight.GREEN  # returns <TrafficLight.GREEN: 1>
TrafficLight.GREEN.name  # returns 'GREEN'
TrafficLight.GREEN.value  # returns 1
TrafficLight(1)  # returns <TrafficLight.GREEN: 1>
TrafficLight(2)  # returns <TrafficLight.YELLOW: 2>
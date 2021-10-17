# Numbers
print(123 + 123)
print(1.5 * 4)
print(2 ** 100)
print(len(str(2 ** 100)))

import math

math.pi
math.sqrt(85)

import random

random.random()
random.choice([1, 2, 3, 4])

# Strings
# sequence operations
S = 'spam'
len(S)
S[0]
S[-1]
S[len(S) - 1]  # Negative indexing, hardway.
S[1:3]
S[1:]
S[2:]
S[:3]
S[::-1]
S[::2]
S + 'xyz'  # on the fly representation, nothing changes here.
S  # actual string won't be effected due to this.
# Strings are immutable
s = 'spam'
s[0] = 'z'  # Thrown an error "TypeError"
s = 'z' + s[1:]
s  # zpam
# another way of editing texts
s = 'shruberry'
l = list(s)
l[1] = 'c'
l = ''.join(l)
l  # scruberry

B = bytearray(b'spam')
B.extend(b'eggs')
B  # bytearray(b'spameggs')
B.decode()  # 'spameggs'
type(B.decode())  # <class 'str'>

# Type specific methods
S = 'Spam'
S.find('pa')  # This will give the offset 1.
S.replace('pa', 'XYZ')  # SXYZm
S  # Spam

line = 'aaa,bbb,ccc,ddd'
line.split(',')  # ['aaa', 'bbb', 'ccc', 'ddd']
S.upper()
S.lower()
S.isalpha()

line = 'aaa,bbb,ccccc,dd\n'
line.rstrip()  # Remove whitespace characters on the right side
# rstrip the empty space and then split the string.
line.rstrip().split(',')  # ['aaa', 'bbb', 'ccccc', 'dd']

x = '%s, eggs, and %s' % ('spam', 'SPAM')
x  # 'spam, eggs, and SPAM'
y = '{0}, eggs, and {1}'.format('spam', 'SPAM')
y  # 'spam, eggs, and SPAM'
z = '{}, eggs, and {}'.format('spam', 'SPAM')
z  # 'spam, eggs, and SPAM'
a = '{f} and {s}'.format(s='YOU', f='ME')
a  # 'ME and YOU'
# Some examples of formatting.
# separators, decimal digits
print('{:,.2f}'.format(269998.2567))  # 269,998.26
# Digits, padding, signs
print('%.2f | %+05d' % (3.14159, -42))  # 3.14 | -0042

# Pattern Matching
import re
match = re.match('Hello[ \t]*(.*)world', 'Hello     Python world')
match.group(1)
# one more example
match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match.groups())  # ('usr', 'home', 'lumberjack')

print(re.split('[/:]', '/usr/home/lumberjack'))  # ['', 'usr', 'home', 'lumberjack']
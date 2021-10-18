nudge = 1
wink = 2
A, B = nudge, wink
A, B  # (1, 2)

[C, D] = [nudge, wink]
C, D  # (1, 2)

# Swapping
nudge = 1
wink = 2
nudge, wink = wink, nudge
nudge, wink  # (2, 1)

# more assignments
[a, b, c] = (1, 2, 3)
a, c  # (1, 3)
[a, b, c] = [1, 2, 3]
a, c  # (1, 3)
(a, b, c) = 'ABC'
a, c  # ('A', 'C')

# Advanced sequence assignment patterns
string = 'SPAM'
a, b, c, d = string
a, d  # ('S', 'M')

a, b, c, = 'SPAM'  # ValueError
# fixing the ValueError, quick hacks...
a, b, c = string[0], string[1], string[2:]
a, b, c  # ('S', 'P', 'AM')

a, b = string[:2]
c = string[2:]
a, b, c  # ('S', 'P', 'AM')

a, b, c = list(string[:2]) + [string[2:]]
a, b, c  # ('S', 'P', 'AM')

(a, b), c = string[:2], string[2:]
a, b, c  # ('S', 'P', 'AM')

((a, b), c) = ('SP', 'AM')
a, b, c  # ('S', 'P', 'AM')

red, green, blue = range(3)
red, blue  # (0, 2)

# Spitting the sequence into front and rest in loops
L = [1, 2, 3, 4]
while True:
    front, L = L[0], L[1:]
    print(front, L)
# The loop breaks due to self.locals issue after providing the o/p


# Extended unpacking.

seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)  # 1 2 3 4
a, b = seq  # ValueError
a, *b = seq  # introduction of args
a  # 1
b  # [2, 3, 4]

*a, b = seq
a  # [1, 2, 3]
b  # 4

a, *b, c = seq
a  # 1
b  # [2, 3]
c  # 4

a, b, *c = seq
a  # 1
b  # 2
c  # [3, 4]

# some more experiments with strings and args.
a, *b = 'spam'
a  # 's'
b  # ['p', 'a', 'm']

a, *b, c = 'spam'
a  # 's'
b  # ['p', 'a']
c  # 'm'

a, *b, c  = range(4)
a  # 0
b  # [1, 2]
c  # 3

# Same while example again
L = [1, 2, 3, 4]
while L:
    front, *L = L
    print(front, L)
'''
1 [2, 3, 4]
2 [3, 4]
3 [4]
4 []
'''

# Boundary cases
seq = [1, 2, 3, 4]
a, b, c, *d = seq
print(a, b, c, d)  # 1 2 3 [4]
# * could be assigned to single item but still a list.

a, b, c, d, *e = seq
print(a, b, c, d, e)  # 1 2 3 4 []
# * could be empty list if there is no assignment.

a, *b, c, *d = seq  # SyntaxError: two starred expressions in assignment

a, b = seq  # ValueError: too many values to unpack (expected 2)

# *a = seq  # SyntaxError: starred assignment target must be in a list or tuple

*a, = seq
print(a)  # [1, 2, 3, 4]

# A useful convenience
seq = [1, 2, 3, 4]

a, *b = seq  # # First, rest
print(a, b)  # 1 [2, 3, 4]

a, b = seq[0], seq[1:]  # First, rest:traditional
print(a, b)  # 1 [2, 3, 4]

*a, b = seq  # Rest, last
print(a, b)  # [1, 2, 3] 4

a, b = seq[:-1], seq[-1]  # rest, last:traditional
print(a, b)  # [1, 2, 3] 4


# Multiple target assignments

a = b = c = 'spam'
print(a, b, c)  # spam spam spam
a, b, c  # ('spam', 'spam', 'spam')

a = b = 0
b = b + 1
a, b  # (0, 1)

# Careful while initializing variables to an empty mutable object.
a = b = []
b.append(42)
a, b  # ([42], [42])

# a and be do not share the same object
a = []
b = []
b.append(42)
a, b  # ([], [42])

# a and be does not share the same object
a, b = [], []


# Augmented Assignments
'''
X += Y X &= Y X −= Y X |= Y
X *= Y X ^= Y X /= Y X >>= Y
X %= Y X <<= Y X **= Y X //= Y
'''
x = 1
x = x + 1
x  # 2

S = 'spam'
S += "SPAM"
S  # 'spamSPAM'

L = [1, 2]
L = L + [3]  # concatenate: slower
L  # [1, 2, 3]
L.append(4)  # Faster, but in place.
L  # [1, 2, 3, 4]
L = L + [5, 6]  # Concatenate: slower
L  # [1, 2, 3, 4, 5, 6]
L.extend([7, 8])  # Faster, but in place.
L  # [1, 2, 3, 4, 5, 6, 7, 8]
L += [9, 10]  # Mapped to L.extend([9, 10])
L  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L = []
L += 'spam' # += and extend allow any sequence, but + does not.
L  # ['s', 'p', 'a', 'm']
L = L + 'spam'  # TypeError: can only concatenate list (not "str") to list
L += 'spam'
L  # ['s', 'p', 'a', 'm', 's', 'p', 'a', 'm']


# Augmented assignment and shared references
L = [1, 2]
M = L  # L & M reference the same object
L = L + [3, 4]  # concatenation makes a new object
L, M  # ([1, 2, 3, 4], [1, 2])  # Changes L but not M

L = [1, 2]
M = L
L += [3, 4]  # But += really means extend
L , M  # M see the the in-place change too.
# ([1, 2, 3, 4], [1, 2, 3, 4])
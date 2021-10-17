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

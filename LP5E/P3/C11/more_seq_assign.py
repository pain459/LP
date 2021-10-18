# Variable Name Rules
# Reserved keyword list
'''
False class finally is return
None continue for lambda try
True def from nonlocal while
and del global not with
as elif if or yield
assert else import pass break except in raise
'''

# Expression statements
'''
Operation Interpretation
spam(eggs, ham) Function calls
spam.ham(eggs) Method calls
spam Printing variables in the interactive interpreter
print(a, b, c, sep='') Printing operations in Python 3.X
yield x ** 2 Yielding expression statements
'''

# Automatic print stream redirection
import sys
temp = sys.stdout  # Save for restoring later
sys.stdout = open('log.txt', 'a')  # redirect prints to a file
print('spam')  # prints go to file directly
print(1, 2, 3)  # same
sys.stdout.close()  # Flush output to disk.
sys.stdout = temp  # restoring original stream
print('back here')  # prints locally
print(open('log.txt').read())  # results of earlier prints
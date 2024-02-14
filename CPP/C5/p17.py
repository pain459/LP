# Python program to display command line arguments

import sys

n = len(sys.argv)
args = sys.argv

print('No. of command line args = ', n)
print('The args are ', args)
print('the args one by one.\n')
for i in args:
    print(i)

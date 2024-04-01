# program to find if file exists or not.
import os, sys

# open the file to reading data
fname = input('Enter file name: ')

if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(f'{fname} file doesnt exist')
    sys.exit(1)

# Read strings from the file
print('Reading the file...')
str = f.read()
print(str)

# Close the file after reading it
f.close()
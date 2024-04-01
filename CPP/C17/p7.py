# Counting number of lines, words and characters in a file
import os, sys

# Open the file for reading
fname = input('Enter the file name: ')

if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(f'{fname} doesnt exist')
    sys.exit(1)

# initialize the counters
cl = cw = cc = 0
for line in f:
    words = line.split()
    cl += 1
    cw += len(words)
    cc += len(line)

print(f'No. of lines: {cl}')
print(f'No. of words: {cw}')
print(f'No. of characters: {cc}')

# Close the file
f.close()
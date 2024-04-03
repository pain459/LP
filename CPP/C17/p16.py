# Searching the binary file based on the record name
import os

# take the record length as 20
reclen = 20

# find the size of the file
size = os.path.getsize('cities.bin')
print(f'Size of the file is {size} bytes.')

# Find the number of records in the file.
n = int(size / reclen)
print(f'No. of records = {n}')

# open the file in binary mode forreading
with open('cities.bin', 'rb') as f:
    name= input('Enter the city name: ')
    # Convert name into binary string
    name = name.encode()
    # Position represents the position of the file pointer
    position = 0
    # found becomes true if city is found in the file.
    found = False

    # Repeat for n records in the file
    for i in range(n):
        # place the file pointer at position
        f.seek(position)
        # Read 20 characters
        str = f.read(20)
        # if found
        if name in str:
            print(f'Found a record no. {i+1}')
            found = True
        # go to the next round
        position += reclen
    if not found:
        print('City not found.')
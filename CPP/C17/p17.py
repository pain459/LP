# Updating the city name in the file
import os

# take the record length as 20 characters
reclen = 20

# Find size of the file
size = os.path.getsize('cities.bin')
print(f'Size of file = {size} bytes.')

# Find the number of records in the file.
n = int(size / reclen)
print(f'No. of records = {n}')

# Open the file in binary mode for reading.
with open('cities.bin', 'rb') as f:
    name = input('Enter city name: ')
    # Convert name into binary string
    name = name.encode()

    newname = input('Enter new name: ')
    # Find the length of newname
    ln = len(newname)
    # add spaces to make its length to be 20
    newname = newname.encode()

    # position represents the position of file pointer
    position = 0

    # Found becomes true if city is found in the file
    found = False

    # Repeat for n records in the file
    for i in range(n):
        # place the file pointer at position
        f.seek(position)
        # read 20 characters
        str = f.read(20)
        # if found
        if name in str:
            print(f'Updated record no {i+1}')
            found = True
            # go back 20 bytes from current position
            f.seek(-20, 1)
            # update the record
            f.write(newname)

        # go to next record
        position += reclen
    if not found:
        print('city not found.')
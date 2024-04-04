# Deleting a record from the file
import os

# Take record length as 20 characters
reclen = 20

# Find size of the file
size = os.path.getsize('cities.bin')

# Find the number of records
n = int(size/reclen)

# open the cities.bin for reading
f1 = open('cities.bin', 'rb')

# Open file2.bin for writing
f2 = open('file2.bin', 'wb')

# accept city name from keyboard
city = input('Enter city name to delete: ')

# add spaces so that it will have 20 characters length
ln = len(city)
city = city + (reclen - ln)*' '

# Convert the city name to binary string
city = city.encode()

# Repeat for all n records
for i in range(n):
    # Read one record from f1 file
    str = f1.read(reclen)
    # if it is not the city name, store into f2 file
    if(str != city):
        f2.write(str)
print('Record deleted...')

# close the files
f1.close()
f2.close()

# Delete the cities.bin file
os.remove('cities.bin')

# Rename file2.bin as cities.bin
os.rename('file2.bin', 'cities.bin')
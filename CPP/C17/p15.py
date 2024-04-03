# Reading city name based on the record number
# Take record length as 20 characters
reclen = 20

# Open the fine in binary mode for reading
with open('cities.bin', 'rb') as f:
    n = int(input('Enter the record number: '))
    # Move file pointer to the end of n-1 th record
    f.seek(reclen * (n - 1))
    # get nth record with 20 chars
    str = f.read(reclen)
    # Convert the byte string into ordinary string
    print(str.decode())
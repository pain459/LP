# reading city name based on record number
# take record length as 20
reclen = 20

# Open the file in binary mode for reading
with open('cities.bin', 'rb') as f:
    n = int(input('Enter record number: '))
    # Move file pointer to the end of n-1 th record
    f.seek(reclen * (n - 1))
    # Get the nth record with 20 chars
    str = f.read(reclen)
    # Convert the byte string to ordinary string
    print(str.decode())
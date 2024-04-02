# Create cities.bin with cities names
# take the record size as 20 bytes
reclen = 20

# Open the file in wb mode as binary file
with open('cities.bin', 'wb') as f:
    # Write data into the file
    n = int(input('How many entries? '))

    for i in range(n):
        city = input('Enter city name: ')
        # find the length of the city
        ln = len(city)
        # Increase the city name to 20 chars
        # By adding remaining spaces
        city = city + (reclen - ln)*' '
        # Convert city name to byte string
        city = city.encode()
        # Write the city name into a file
        f.write(city)
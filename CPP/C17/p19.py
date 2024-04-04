# mmap demos
# create phonebook.dat file
# Open the file in wb mode as binary file
with open('phonebook.dat', 'wb') as f:
    # Write data into the file
    n = int(input('How many entries: '))

    for i in range(n):
        name = input('Enter name: ')
        phone = input('Enter phone number: ')
        # convert name and phone from strings to bytes
        name = name.encode()
        phone = phone.encode()
        # Write the data into the file
        f.write(name+phone)
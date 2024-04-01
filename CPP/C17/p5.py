# Appending and then reading strings
# open the file for reading data
f = open('myfile.txt', 'a+')

print('Enter text to append (@ at end): ')
while str != '@':
    str = input() # accepting string into str
    # Writing the string into file
    if str != '@':
        f.write(str + '\n')

# put the file pointer to the beginning of the file
f.seek(0, 0)

# print strings from the file
print('The file contents are: ')
str = f.read()
print(str)

# Closing the file
f.close()
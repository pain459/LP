# Creating a file to store characters
# Open file for writing data
f = open('myfile.txt', 'w')

# Enter characters to write
x = input('Enter data to to load in the file: ')

# write the data into the file
f.write(x)

# closing the file
f.close()
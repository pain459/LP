# Reading from a file
# Open the file for reading data
f = open('myfile.txt', 'r')

# Read strings from the file
print("The contents from the file are: ")
str = f.read()
print(str)

# Closing the file
f.close()
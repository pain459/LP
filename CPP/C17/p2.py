# Reading characters from file
# Open file for reading data
f = open('myfile.txt', 'r')

# read all characters from the file
str = f.read()

# Display them on the screen
print(str)

# Close the file
f.close()

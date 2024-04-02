# Copying an image into a file
# Open the files in binary mode
f1 = open('img.png', 'rb')
f2 = open('copy.png', 'wb')

# Read bytes from f1 and write to f2
bytes = f1.read()
f2.write(bytes)

# Close the files
f1.close()
f2.close()
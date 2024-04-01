# Creating a file with strings
# open the file for writing data
f = open('myfile.txt', 'w')
# enter strings from the keyboard
print('Enter text (@ at end): ')
while str != '@':
    str = input()
    # write the string to the file
    if str != '@':
        f.write(str + '\n')
# Closing the file
f.close()
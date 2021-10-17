f = open('data.txt', 'w')  # open/create if dont exist in write mode.
f.write('Hello\n')
f.write('world\n')
f.close()  # Close to flush output buffers to disk

# reading the file
f = open('data.txt')  # r is default mode.
text = f.read()
text  # 'Hello\nworld\n'
print(text)  # \n will be processed by print statement.
text.split()  # ['Hello', 'world'] now we can play around the data.
# Using for in this case.
for line in open('data.txt'): print(line)
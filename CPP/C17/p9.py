# With statement to open a file
# this will automatically close the file after operation.
with open('myfile.txt', 'r') as f:
    for line in f:
        print(line)
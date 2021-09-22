# reading and writing simple files.
output_file = open("hello.txt", "w")
output_file.writelines("This is my first line")
output_file.close()

output_file = open("hello.txt", "w")
lines_to_write = [
    "This is my file.",
    "\nThere are many like it.",
    "\nBut this one is mine"
]

output_file.writelines(lines_to_write)
output_file.close()

# Appending text
output_file = open("hello.txt", "a")
output_file.writelines("\nNON SEQUITUR")
output_file.close()

# Reading a file.
input_file = open("hello.txt", "r")
print(input_file.readlines()[0])  # [0] is mentioned assuming we are reading the list line. Since the returned type
# is a list.
input_file.close()

#  For loop to print the lines
input_file = open("hello.txt", "r")
for i in input_file.readlines():
    print(i, end="")
input_file.close()

# Using while loop to print the lines.

input_file = open("hello.txt", "r")

line = input_file.readline()
while line != "":
    print(line, end="")
    line = input_file.readline()
input_file.close()

#  using with method to print the contents of the file.
with open("hello.txt", "r") as input_file:
    for i in input_file.readlines():
        print(i)

# Copying the contents of one file to another.
with open("hello.txt", "r") as source, open("hello2.txt", "w") as dest:
    for i in source.readlines():
        dest.writelines(line)


# Traversing a file with .seek()
input_file = open("hello.txt", "r")
print("Line 0 (first line):", input_file.readline())

input_file = open("hello.txt", "r")
input_file.seek(0)
print("Line 0 again:", input_file.readline())
print("Line 1:", input_file.readline())

input_file = open("hello.txt", "r")
input_file.seek(8)
print("Line 0 (starting at 9th character):", input_file.readline())

input_file.close()

# Finally using import modules..

import os
path = r'C:\Users\kumarrav\Desktop\prog_mat'
os.listdir(path)
# os.mkdir(os.path.join(path, 'test'))
# os.mkdir(path + "/test")
os.mkdir(os.path.join(path, 'test'))

# Removing the directory.

import os
path = r'C:\Users\kumarrav\Desktop\prog_mat'
os.rmdir(os.path.join(path, 'test'))

# Renaming the files with some extension.
import os
path = r'C:\Users\kumarrav\Desktop\prog_mat'

for file_name in os.listdir(path):
    # Converting the filename to lower case and checking the files ending with .png
    if file_name.lower().endswith(".png"):
        # Creating a variable for full path.
        full_path = os.path.join(path, file_name)
        # Creating a variable new path by eliminating last 4 letters
        # Technically removing extension and adding a new one using concatenation.
        new_file_name = full_path[:-4] + "_backup.png"
        # Using the rename module.
        os.rename(full_path, new_file_name)


# The glob module.

import glob
# path = r'C:\Users\kumarrav\Desktop\prog_mat'
# Searching the files with certain extensions in the current working directory.
glob.glob("*.txt")

# Improvising the file rename program.
import os
import glob
path = r'C:\Users\kumarrav\Desktop\prog_mat'

possible_files = os.path.join(path, "*.png")
print(possible_files)  # returns the directory + *.png extension.
print(glob.glob(possible_files))  # greps through the directory for possible matches.

for file_name in glob.glob(possible_files):
    full_path = os.path.join(path, file_name)
    print(full_path)  # Just checking the full path. Python will auto set the path and slashes
    new_file_name = full_path[:-4] + "_backup.png"
    print(new_file_name)  # This will decide the new file name.
    os.rename(full_path, new_file_name)  # rename will execute the code to rename the files.


# Searching through the sub folders.

import os
import glob

path = r"C:\local"

possible_files = os.path.join(path, "*/*.pdf")

for i in glob.glob(possible_files):
    print(i)

# Checking the existence of files and folders.

import os
path = r"C:\local"

files_and_folders = os.listdir(path)
print(files_and_folders)  # returns the data in a list.

for i in files_and_folders:
    full_path = os.path.join(path, i)
    # print(os.path.isdir(full_path))
    if os.path.isdir(full_path):
        # Using the rename function to rename the files.
        os.rename(full_path, full_path + "_folder")
        # Execute the below to undo the rename.
        # os.rename(full_path, full_path[:-7])

# Using os.walk() to traverse across the directories.

import os

path = r'C:\local'
print(type(os.walk(path)))  # Return generator
# for current_folder, sub_folders, file_names
for i, j, k in os.walk(path):
    for l in k:
        print(os.path.join(i, l))


# Read and write CSV data.
import os
import csv

path = os.getcwd()

with open(os.path.join(path, "wonka.csv"), "r") as my_file:
    reader = csv.reader(my_file)
    for row in reader:
        print(row)

# To get a single row of data and skip the headers of csv file.
# We will implement next function.

import os
import csv

path = os.getcwd()

with open(os.path.join(path, "wonka.csv"), "r") as my_file:
    reader = csv.reader(my_file)
    next(reader)
    for first_name, last_name, reward in reader:
        print(f"{first_name} {last_name} got: {reward}")


# Using delimiter to read the data dn display.
import os
import csv

path = os.getcwd()

with open(os.path.join(path, "tabbed_wonka.csv"), "r") as my_file:
    reader = csv.reader(my_file, delimiter="\t")
    next(reader)
    for row in reader:
        print(row)

# Writing data to a CSV file
# Using write row.
import os
import csv

path = os.getcwd()

with open(os.path.join(path, "movies.csv"), "w") as my_file:
    writer = csv.writer(my_file)
    writer.writerow(["Movie", "Rating"])
    writer.writerow(["Interstellar", "10"])
    writer.writerow(["Joker", "9"])
    writer.writerow(["Inception", "9.5"])

# Using writerows method which takes the list of rows, to write all rows in a single line.

import os
import csv

path = os.getcwd()

ratings = [["Movies", "Rating"],
           ["Interstellar", 9],
           ["Joker", 9],
           ["Inception", 9.5]]

with open(os.path.join(path, "movies_list2.csv"), "w") as my_file:
    writer = csv.writer(my_file)
    writer.writerows(ratings)
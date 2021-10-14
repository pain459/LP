# \n will start a new line.

splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# Using \t
tabbedString = "1\t2\t3\t4\t5\t6"
print(tabbedString)

# using \ to escape.
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting')
print("The pet shop owner said 'No, no, \"e\"s uh,...he\"s resting")

# Using """ """ quotes to escape everything.
print("""The pet shop owner said "No, no, 'e's uh,...he's resting""")

# """ """ will include line breaks by default.
anotherSplitString = """This string has been 
split over 
several 
lines"""

print(anotherSplitString)

# Using \ to eliminate the line breaks.
# Now the output will be in the same line.
anotherSplitString = """This string has been \
split over \
several \
lines"""

print(anotherSplitString)

# Exercises
print("Number 1\tThe Larch")
print("Number 2\tThe Horse Chestnut")

# testing \ char
print("""The pet shop owner said \
"No, no, 'e's uh,...he's resting""")

# The last \ will do the trick
print("The pet shop owner said 'No, "\
      "no, \"e\"s uh,...he\"s resting")

# including \ in the string.
# Failed case
print("C:\Users\local\treats\noobs")
# Passed case escaping \ with \
print("C:\\Users\local\\treats\\noobs")
# using raw string. r at the start. Prefer escaping with \ instead.
print(r"C:\Users\local\treats\noobs")


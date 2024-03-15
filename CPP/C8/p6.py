# Program to find all occurrences of substring in a main string.
str1 = input("Enter main string: ")
sub1 = input("Enter sub string: ")

i = 0
flag = False
n = len(str1)
while i < n:
    pos = str1.find(sub1, i, n)
    if pos != -1:
        print("Found at position: ", pos + 1)
        i = pos + 1
        flag = True
    else:
        i += 1
if flag == False:
    print("Substring not found!")

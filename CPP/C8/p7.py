# Find all occurrences of substring in the main string v2.0
str1 = input("Enter main string: ")
sub1 = input("Enter sub string: ")

flag = False
pos = -1
n = len(str1)

while True:
    pos = str1.find(sub1, pos+1, n)
    if pos == -1:
        break
    print("Found at position: ", pos+1)

if not flag:
    print("Not found!")
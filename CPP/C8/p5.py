# Try to find the first occurrence of substring in a main string.
str1 = input("Enter main string: ")
sub1 = input("Enter sub string: ")

# Find position of sub in str
# search from zeroth to last character in str1
try:
    n = str1.index(sub1, 0, len(str1))
except ValueError:
    print("Substring not found.")
else:
    print("Sub string found at position: ", n+1)
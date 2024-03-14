# Find position on substring

str1 = input("Enter the main string: ")
str2 = input("Enter the sub string: ")

# Find position of str2 in str1
# We will use the find method.
n = str1.find(str2, 0, len(str1))
if n == -1:
    print(str2 + " is not found in main string.")
else:
    print(f"{str2} is found at position, {n+1}")
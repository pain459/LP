# To know whether substring is in main string or not.

str1 = input("Enter main string: ")
str2 = input("Enter substring: ")

if str2 in str1:
    print(str2 + " is found in main string.")
else:
    print(str2 + " is not found in main string.")
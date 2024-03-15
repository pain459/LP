# To accept a group of numbers and display them

str1 = input("Enter numbers separated by space: ")

lst1 = str1.split(' ')
for i in lst1:
    print(i)
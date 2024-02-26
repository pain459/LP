# Find element in the list

x = [1, 2, 3, 4, 5]
search = int(input("Please enter the integer to search: "))
for i in x:
    if i == search:
        print("Found!")
        break
else:
    print("Not found!")
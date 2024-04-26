# List of tuples to unpack
data = [('Alice', 25, 'New York'), ('Bob', 30, 'Los Angeles'), ('Charlie', 28, 'Chicago')]

# unzip the data into seperate lists
names, age, city = zip(*data)

print(list(names)) # to convert to list
print(age)
print(city)
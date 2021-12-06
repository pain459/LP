programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary['Bug'])
print(programming_dictionary['Function'])
print(programming_dictionary)

# Adding new key items to dictionary.

programming_dictionary['Loop'] = "The action of doing something over and over again."
print(programming_dictionary)

# empty dictionary.
empty_dictionary = {}

# Wiping an existing dictionary
programming_dictionary = {}

print(programming_dictionary)

# looping through the dictionary.

dict1 = {'A': 1, 'B': 2, 'C': 3}
for i in dict1:
    print(i)
    print(dict1[i])

for i,j in dict1.items():
    print(i)
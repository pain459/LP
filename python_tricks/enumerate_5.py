# creating a dictionary of a list of items using enumerate

x = ['a', 'b', 'c']

indexed_dict = {index: item for index, item in enumerate(x)}

print(indexed_dict)
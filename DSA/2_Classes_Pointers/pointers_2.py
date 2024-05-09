# lets perform pointers demo with dictionaries

dict1 = {'item': 10}

dict2 = dict1

# checking the memory values of dict1 and dict2

print(f'Location if dict1 is {id(dict1)}')
print(f'Location if dict2 is {id(dict2)}')

# lets change the value for item from dict2

dict2['item'] = 20

# lets verify the values now.

print('Memory locations after dict data change.')
print(f'Location if dict1 is {id(dict1)}')
print(f'Location if dict2 is {id(dict2)}')

print(dict1.values())
print(dict2.values())

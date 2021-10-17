# Mapping Operations
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
D['food']  # 'Spam'
D['quantity'] += 1
D  # {'food': 'Spam', 'quantity': 5, 'color': 'pink'}

# Building a dictionary
D = {}
D['name'] = 'Bob'
D['age'] = 40
D['job'] = 'Dev'
print(D)  # {'name': 'Bob', 'age': 40, 'job': 'Dev'}

# Building dictionary from dict.
bob1 = dict(name='Bob', age=40, job='dev')
print(bob1)  # {'name': 'Bob', 'age': 40, 'job': 'dev'}

# Creating dictionary with zip
bob1 = dict(zip(['name', 'age', 'job'], ['Bob', 40, 'dev']))
print(bob1)  # {'name': 'Bob', 'age': 40, 'job': 'dev'}

# Nesting revisited
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
rec['name']
rec['name']['first']
rec['jobs'].append('janitor')
rec['jobs']
rec['jobs'][-1]
rec = 0

# Missing keys : if tests
D = {'a': 1, 'b': 2, 'c': 3}
D
D['e'] = 99
D
D['f']  # returns KeyError
# simplifying with if
D = {'a': 1, 'b': 2, 'c': 3}
if 'f' not in D:
    print('Missing')
# using get and assigning default values.
value = D.get('x', 0)
value  # 0 as that key doesn't exist.
value = D['x'] if 'x' in D else 0
value  # 0


# Sorting keys: for loops
D = {'a': 1, 'b': 2, 'c': 3}
Ks = list(D.keys())
Ks.sort()
Ks  # ['a', 'b', 'c']

for key in list(D.keys()):
       print(key, '=>', D[key])
'''
a => 1
b => 2
c => 3
'''

for i in 'spam':
    print(i.upper())

# decrement counter
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

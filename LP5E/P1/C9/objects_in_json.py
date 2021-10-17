name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
rec  # {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}

import json
json.dumps(rec)

# Storing a json object. It stores as a string.
S = json.dumps(rec)
S  # '{"name": {"first": "Bob", "last": "Smith"}, "job": ["dev", "mgr"], "age": 40.5}'

# Loading a json object.
O = json.loads(S)
O  # {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}


O == rec  # True

# Testing with example json.
json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())  # reads JSON.

# loading into object.
P = json.load(open('testjson.txt'))
P  # {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}


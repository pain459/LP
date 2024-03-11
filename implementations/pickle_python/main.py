import pickle as p

# Data to serialize
data = {'a': 1, 'b': 2, 'c': 3}
print(data)

# serialise the data now.
with open('data.pickle', 'wb') as f:
    p.dump(data, f)


# Deserialize the data
with open('data.pickle', 'rb') as f:
    restored_data = p.load(f)

print(restored_data)
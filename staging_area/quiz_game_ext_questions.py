import json

# Open JSON file
with open('DB.json', 'r') as file:
    data = json.load(file)

# Access data
print(data)
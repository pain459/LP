import pandas as pd

# JSON-like data (dictionary)
json_data = {
    "id": [101, 102, 103, 104],
    "name": ["John", "Alice", "Bob", "Emily"],
    "age": [30, 25, 35, 28],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"],
    "gender": ["Male", "Female", "Male", "Female"]
}

# Create DataFrame from JSON data
df = pd.DataFrame.from_dict(json_data)

# Display the DataFrame
print(df)

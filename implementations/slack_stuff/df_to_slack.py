import pandas as pd

# Create a DataFrame with complex data
data = {
    'id': [101, 102, 103, 104],
    'name': ['John', 'Alice', 'Bob', 'Emily'],
    'age': [30, 25, 35, 28],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'gender': ['Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

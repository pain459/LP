import pandas as pd
import random
import string

# Function to generate unique alphanumeric IDs
def generate_unique_id(length=20):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Generate a list of unique IDs
def generate_unique_ids(num_ids, length=20):
    unique_ids = set()
    while len(unique_ids) < num_ids:
        unique_ids.add(generate_unique_id(length))
    return list(unique_ids)

# Number of IDs to generate
num_ids = 100  # Change this number to the desired number of IDs

# Generate the IDs
center_ids = generate_unique_ids(num_ids)

# Create a DataFrame
df_center_ids = pd.DataFrame(center_ids, columns=["CenterID"])

# Save to CSV
df_center_ids.to_csv('voting_centers.csv', index=False)

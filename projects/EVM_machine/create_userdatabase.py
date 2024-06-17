import pandas as pd
import random
import string

# Generate random alphanumeric unique IDs
def generate_unique_id(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Generate random first and last names
def generate_name():
    first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "David", "Laura", "Robert", "Linda"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return random.choice(first_names), random.choice(last_names)

# Generate random phone numbers
def generate_phone_number():
    return f"+1{random.randint(1000000000, 9999999999)}"

# Generate random addresses
def generate_address():
    streets = ["Main St", "High St", "Broadway", "Maple St", "Oak St", "Pine St", "Elm St", "Washington St", "Lake St", "Hill St"]
    return f"{random.randint(100, 999)} {random.choice(streets)}"

# Generate random sex
def generate_sex():
    return random.choice(["Male", "Female", "Other"])

# Generate random religion
def generate_religion():
    religions = ["Christianity", "Islam", "Hinduism", "Buddhism", "Judaism", "Other"]
    return random.choice(religions)

# Create user list
users = []
for _ in range(1000):
    user_id = generate_unique_id()
    first_name, last_name = generate_name()
    phone_number = generate_phone_number()
    address = generate_address()
    sex = generate_sex()
    religion = generate_religion()
    users.append([user_id, first_name, last_name, phone_number, address, sex, religion])

# Convert to DataFrame
df_users = pd.DataFrame(users, columns=["UniqueID", "FirstName", "LastName", "PhoneNumber", "Address", "Sex", "Religion"])

# Export to CSV
df_users.to_csv('user_list.csv', index=False)

print("User list generated and exported to 'user_list.csv'.")

import csv
from faker import Faker

# Initialize the Faker library
fake = Faker()

# Define the CSV file columns
columns = [
    "CustomerID", "FirstName", "LastName", "Email", "PhoneNumber", "Address", 
    "City", "State", "PostalCode", "RegistrationDate"
]

# Function to generate a single row of fake customer data
def generate_customer_data(customer_id):
    return [
        customer_id,
        fake.first_name(),
        fake.last_name(),
        fake.email(),
        fake.phone_number(),
        fake.address().replace("\n", ", "),
        fake.city(),
        fake.state(),
        fake.zipcode(),
        fake.date_this_decade()
    ]

# Create and write the CSV file
with open("customer_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(columns)

    # Generate and write 100 rows of customer data
    for i in range(1, 101):
        writer.writerow(generate_customer_data(i))

print("customer_data.csv has been created with 100 rows of customer data.")

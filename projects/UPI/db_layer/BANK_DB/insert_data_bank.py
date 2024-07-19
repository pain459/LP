import psycopg2
from faker import Faker
import random
import time

# Initialize Faker
faker = Faker()

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="bankdb",
    user="postgres",
    password="mysecretpassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Function to generate unique_id
def generate_unique_id(bank_shortcode, branch_shortcode):
    epoch_ist = int(time.time())  # current epoch timestamp IST
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    unique_id = f"{bank_shortcode}{branch_shortcode}{epoch_ist}{random_string}"
    return unique_id

# Insert data into bank_mapping table
bank_data = []
for _ in range(100):
    bank_name = faker.company()
    bank_short_code = faker.unique.bothify(text='??????').upper()
    created_on = int(time.time())
    bank_data.append((bank_name, bank_short_code, created_on))

cur.executemany("INSERT INTO bank.bank_mapping (bank_name, bank_short_code, created_on) VALUES (%s, %s, %s)", bank_data)
conn.commit()

# Insert data into bank_branch_mapping table
branch_data = []
for bank_name, bank_short_code, _ in bank_data:
    for _ in range(100):
        branch_name = faker.company_suffix()
        branch_shortcode = faker.unique.bothify(text='??????').upper()
        created_on = int(time.time())
        unique_id = generate_unique_id(bank_short_code, branch_shortcode)
        branch_data.append((bank_name, bank_short_code, branch_name, branch_shortcode, created_on, unique_id))

cur.executemany("INSERT INTO bank.bank_branch_mapping (bank_name, bank_name_shortcode, branch_name, branch_shortcode, created_on, unique_id) VALUES (%s, %s, %s, %s, %s, %s)", branch_data)
conn.commit()

# Close the connection
cur.close()
conn.close()

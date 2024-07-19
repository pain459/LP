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

# Function to generate unique_id for bank_branch_mapping
def generate_branch_unique_id(bank_shortcode, branch_shortcode):
    epoch_ist = int(time.time())  # current epoch timestamp IST
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    unique_id = f"{bank_shortcode}{branch_shortcode}{epoch_ist}{random_string}"
    return unique_id

# Function to generate unique_id for user_details
def generate_user_unique_id(bank_shortcode, branch_shortcode, first_name, last_name, social_security_number):
    epoch_ist = int(time.time())  # current epoch timestamp IST
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    ssn_clean = social_security_number.replace("-", "")  # Remove hyphens from SSN
    unique_id = f"{bank_shortcode}{branch_shortcode}{epoch_ist}{first_name.lower()}{last_name.lower()}{ssn_clean}{random_string}"
    return unique_id

# Insert data into bank_mapping table
bank_data = []
for _ in range(100):
    bank_name = faker.unique.company()
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
        unique_id = generate_branch_unique_id(bank_short_code, branch_shortcode)
        branch_data.append((bank_name, bank_short_code, branch_name, branch_shortcode, created_on, unique_id))

cur.executemany("INSERT INTO bank.bank_branch_mapping (bank_name, bank_name_shortcode, branch_name, branch_shortcode, created_on, unique_id) VALUES (%s, %s, %s, %s, %s, %s)", branch_data)
conn.commit()

# Fetch all branch_shortcodes with their respective bank_shortcodes
cur.execute("SELECT bank_name_shortcode, branch_shortcode FROM bank.bank_branch_mapping")
branch_shortcodes = cur.fetchall()

# Insert data into user_details table
user_data = []
for _ in range(1000):  # Generating 1000 user records as an example
    first_name = faker.first_name()
    last_name = faker.last_name()
    social_security_number = faker.unique.ssn()
    address = faker.address()
    pin_code = faker.zipcode()
    created_on_epoch_ist = int(time.time())
    bank_shortcode, branch_shortcode = random.choice(branch_shortcodes)
    unique_id = generate_user_unique_id(bank_shortcode, branch_shortcode, first_name, last_name, social_security_number)
    user_data.append((first_name, last_name, social_security_number, address, pin_code, created_on_epoch_ist, branch_shortcode, unique_id))

cur.executemany("INSERT INTO bank.user_details (first_name, last_name, social_security_number, address, pin_code, created_on_epoch_ist, branch_shortcode, unique_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", user_data)
conn.commit()

# Close the connection
cur.close()
conn.close()

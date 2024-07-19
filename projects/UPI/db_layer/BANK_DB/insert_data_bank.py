import psycopg2
from faker import Faker
import random
import time
import argparse
import concurrent.futures

# Initialize Faker
faker = Faker()

# Database connection parameters
db_params = {
    'dbname': 'bankdb',
    'user': 'postgres',
    'password': 'mysecretpassword',
    'host': 'localhost',
    'port': '5432'
}

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

# Function to insert data with retry on unique constraint violation
def insert_with_retry(conn, insert_query, data_tuple, generate_unique_id_func, max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            with conn.cursor() as cur:
                cur.execute(insert_query, data_tuple)
                conn.commit()
            return
        except psycopg2.errors.UniqueViolation:
            conn.rollback()
            retries += 1
            data_tuple = generate_unique_id_func(data_tuple)
    raise Exception("Max retries exceeded for inserting data with unique constraint")

# Function to generate records for bank_mapping
def generate_bank_mapping_records(num_records):
    conn = psycopg2.connect(**db_params)
    bank_data = []
    for _ in range(num_records):
        bank_name = faker.unique.company()
        bank_short_code = faker.unique.bothify(text='??????').upper()
        created_on = int(time.time())
        bank_data.append((bank_name, bank_short_code, created_on))

    with conn.cursor() as cur:
        cur.executemany("INSERT INTO bank.bank_mapping (bank_name, bank_short_code, created_on) VALUES (%s, %s, %s)", bank_data)
        conn.commit()
    conn.close()

# Function to generate records for bank_branch_mapping
def generate_bank_branch_mapping_records(num_records_per_bank):
    conn = psycopg2.connect(**db_params)
    with conn.cursor() as cur:
        cur.execute("SELECT bank_name, bank_short_code FROM bank.bank_mapping")
        bank_data = cur.fetchall()

    branch_data = []
    for bank_name, bank_short_code in bank_data:
        for _ in range(num_records_per_bank):
            branch_name = faker.company_suffix()
            branch_shortcode = faker.unique.bothify(text='??????').upper()
            created_on = int(time.time())
            unique_id = generate_branch_unique_id(bank_short_code, branch_shortcode)
            branch_data.append((bank_name, bank_short_code, branch_name, branch_shortcode, created_on, unique_id))

    insert_query = "INSERT INTO bank.bank_branch_mapping (bank_name, bank_name_shortcode, branch_name, branch_shortcode, created_on, unique_id) VALUES (%s, %s, %s, %s, %s, %s)"
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(insert_with_retry, conn, insert_query, data, lambda d: (d[0], d[1], d[2], d[3], d[4], generate_branch_unique_id(d[1], d[3]))) for data in branch_data]
        for future in concurrent.futures.as_completed(futures):
            future.result()
    conn.close()

# Function to generate records for user_details
def generate_user_details_records(num_records):
    conn = psycopg2.connect(**db_params)
    with conn.cursor() as cur:
        cur.execute("SELECT bank_name_shortcode, branch_shortcode FROM bank.bank_branch_mapping")
        branch_shortcodes = cur.fetchall()

    user_data = []
    for _ in range(num_records):  # Generating specified user records
        first_name = faker.first_name()
        last_name = faker.last_name()
        social_security_number = faker.unique.ssn()
        address = faker.address()
        pin_code = faker.zipcode()
        created_on_epoch_ist = int(time.time())
        bank_shortcode, branch_shortcode = random.choice(branch_shortcodes)
        unique_id = generate_user_unique_id(bank_shortcode, branch_shortcode, first_name, last_name, social_security_number)
        user_data.append((first_name, last_name, social_security_number, address, pin_code, created_on_epoch_ist, branch_shortcode, unique_id))

    insert_query = "INSERT INTO bank.user_details (first_name, last_name, social_security_number, address, pin_code, created_on_epoch_ist, branch_shortcode, unique_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(insert_with_retry, conn, insert_query, data, lambda d: (d[0], d[1], d[2], d[3], d[4], d[5], d[6], generate_user_unique_id(d[6], d[7], d[0], d[1], d[2]))) for data in user_data]
        for future in concurrent.futures.as_completed(futures):
            future.result()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate records for bank database.')
    parser.add_argument('--banks', type=int, help='Number of bank records to generate')
    parser.add_argument('--branches', type=int, help='Number of branch records per bank to generate')
    parser.add_argument('--users', type=int, help='Number of user records to generate')

    args = parser.parse_args()

    if args.banks:
        generate_bank_mapping_records(args.banks)
    if args.branches:
        generate_bank_branch_mapping_records(args.branches)
    if args.users:
        generate_user_details_records(args.users)

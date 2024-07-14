import psycopg2
from psycopg2 import sql
from faker import Faker
import random
import string
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib

# Initialize Faker
fake = Faker()

# Database connection details
db_params = {
    'dbname': 'rankings_board',
    'user': 'admin',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}

# Function to generate a unique_id
# def generate_unique_id(country_code):
#     current_date = datetime.now().strftime("%Y%m%d")
#     epoch_time = int(time.time() * 1000)  # Current time in milliseconds
#     random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
#     return f"{country_code}{current_date}{epoch_time}{random_string}"

def generate_unique_id(country_code):
    current_date = datetime.now().strftime("%Y%m%d")
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    raw_id = f"{country_code}{current_date}{random_string}"
    return hashlib.sha1(raw_id.encode()).hexdigest()[:24]

# Function to read country codes from the database
def read_country_codes():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute("SELECT country_name, country_code FROM rankings_board.country_codes")
    country_codes = cursor.fetchall()
    cursor.close()
    conn.close()
    return country_codes

# Function to insert a single player's data
def insert_player_data(country_codes):
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    country_code = random.choice(country_codes)[1]
    dob = fake.date_of_birth(minimum_age=18, maximum_age=40)
    sex = random.choice(['M', 'F'])
    unique_id = generate_unique_id(country_code)

    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Insert into player_names
    cursor.execute(
        sql.SQL("""
            INSERT INTO rankings_board.player_names (unique_id, first_name, middle_name, last_name, country_code, DOB, Sex)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """),
        [unique_id, first_name, middle_name, last_name, country_code, dob, sex]
    )

    # Generate random stats
    matches = random.randint(0, 300)
    goals = random.randint(0, 100)
    assists = random.randint(0, 100)
    fouls = random.randint(0, 50)
    injuries = random.randint(0, 20)

    # Insert into player_stats
    cursor.execute(
        sql.SQL("""
            INSERT INTO rankings_board.player_stats (unique_id, matches, goals, assists, fouls, injuries)
            VALUES (%s, %s, %s, %s, %s, %s)
        """),
        [unique_id, matches, goals, assists, fouls, injuries]
    )

    conn.commit()
    cursor.close()
    conn.close()

# Number of players to insert
num_players = 1000000

# Read country codes from the database
country_codes = read_country_codes()

# Function to handle the insertion using multiple threads
def main():
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(insert_player_data, country_codes) for _ in range(num_players)]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()

print("Additional player data and stats inserted successfully!")

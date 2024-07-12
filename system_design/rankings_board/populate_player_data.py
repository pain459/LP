import psycopg2
from psycopg2 import sql
from faker import Faker
import random
import string
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

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

# List of countries and their codes (assuming this is already populated)
football_playing_countries = [
    ('Afghanistan', 'AF'),
    ('Albania', 'AL'),
    ('Algeria', 'DZ'),
    ('American Samoa', 'AS'),
    ('Andorra', 'AD'),
    ('Angola', 'AO'),
    ('Anguilla', 'AI'),
    ('Antigua and Barbuda', 'AG'),
    ('Argentina', 'AR'),
    ('Armenia', 'AM'),
    ('Aruba', 'AW'),
    ('Australia', 'AU'),
    ('Austria', 'AT'),
    ('Azerbaijan', 'AZ'),
    ('Bahamas', 'BS'),
    ('Bahrain', 'BH'),
    ('Bangladesh', 'BD'),
    ('Barbados', 'BB'),
    ('Belarus', 'BY'),
    ('Belgium', 'BE'),
    ('Belize', 'BZ'),
    ('Benin', 'BJ'),
    ('Bermuda', 'BM'),
    ('Bhutan', 'BT'),
    ('Bolivia', 'BO'),
    ('Bosnia and Herzegovina', 'BA'),
    ('Botswana', 'BW'),
    ('Brazil', 'BR'),
    ('British Virgin Islands', 'VG'),
    ('Brunei', 'BN'),
    ('Bulgaria', 'BG'),
    ('Burkina Faso', 'BF'),
    ('Burundi', 'BI'),
    ('Cabo Verde', 'CV'),
    ('Cambodia', 'KH'),
    ('Cameroon', 'CM'),
    ('Canada', 'CA'),
    ('Cayman Islands', 'KY'),
    ('Central African Republic', 'CF'),
    ('Chad', 'TD'),
    ('Chile', 'CL'),
    ('China PR', 'CN'),
    ('Chinese Taipei', 'TW'),
    ('Colombia', 'CO'),
    ('Comoros', 'KM'),
    ('Congo', 'CG'),
    ('Cook Islands', 'CK'),
    ('Costa Rica', 'CR'),
    ('Croatia', 'HR'),
    ('Cuba', 'CU'),
    ('Curaçao', 'CW'),
    ('Cyprus', 'CY'),
    ('Czech Republic', 'CZ'),
    ('Denmark', 'DK'),
    ('Djibouti', 'DJ'),
    ('Dominica', 'DM'),
    ('Dominican Republic', 'DO'),
    ('DR Congo', 'CD'),
    ('Ecuador', 'EC'),
    ('Egypt', 'EG'),
    ('El Salvador', 'SV'),
    ('England', 'GB'),
    ('Equatorial Guinea', 'GQ'),
    ('Eritrea', 'ER'),
    ('Estonia', 'EE'),
    ('Eswatini', 'SZ'),
    ('Ethiopia', 'ET'),
    ('Faroe Islands', 'FO'),
    ('Fiji', 'FJ'),
    ('Finland', 'FI'),
    ('France', 'FR'),
    ('Gabon', 'GA'),
    ('Gambia', 'GM'),
    ('Georgia', 'GE'),
    ('Germany', 'DE'),
    ('Ghana', 'GH'),
    ('Gibraltar', 'GI'),
    ('Greece', 'GR'),
    ('Grenada', 'GD'),
    ('Guam', 'GU'),
    ('Guatemala', 'GT'),
    ('Guinea', 'GN'),
    ('Guinea-Bissau', 'GW'),
    ('Guyana', 'GY'),
    ('Haiti', 'HT'),
    ('Honduras', 'HN'),
    ('Hong Kong', 'HK'),
    ('Hungary', 'HU'),
    ('Iceland', 'IS'),
    ('India', 'IN'),
    ('Indonesia', 'ID'),
    ('Iran', 'IR'),
    ('Iraq', 'IQ'),
    ('Israel', 'IL'),
    ('Italy', 'IT'),
    ('Ivory Coast', 'CI'),
    ('Jamaica', 'JM'),
    ('Japan', 'JP'),
    ('Jordan', 'JO'),
    ('Kazakhstan', 'KZ'),
    ('Kenya', 'KE'),
    ('Kiribati', 'KI'),
    ('Korea Republic', 'KR'),
    ('Kosovo', 'XK'),
    ('Kuwait', 'KW'),
    ('Kyrgyz Republic', 'KG'),
    ('Lao PDR', 'LA'),
    ('Latvia', 'LV'),
    ('Lebanon', 'LB'),
    ('Lesotho', 'LS'),
    ('Liberia', 'LR'),
    ('Libya', 'LY'),
    ('Liechtenstein', 'LI'),
    ('Lithuania', 'LT'),
    ('Luxembourg', 'LU'),
    ('Macao', 'MO'),
    ('Madagascar', 'MG'),
    ('Malawi', 'MW'),
    ('Malaysia', 'MY'),
    ('Maldives', 'MV'),
    ('Mali', 'ML'),
    ('Malta', 'MT'),
    ('Mauritania', 'MR'),
    ('Mauritius', 'MU'),
    ('Mexico', 'MX'),
    ('Micronesia', 'FM'),
    ('Moldova', 'MD'),
    ('Monaco', 'MC'),
    ('Mongolia', 'MN'),
    ('Montenegro', 'ME'),
    ('Montserrat', 'MS'),
    ('Morocco', 'MA'),
    ('Mozambique', 'MZ'),
    ('Myanmar', 'MM'),
    ('Namibia', 'NA'),
    ('Nauru', 'NR'),
    ('Nepal', 'NP'),
    ('Netherlands', 'NL'),
    ('New Caledonia', 'NC'),
    ('New Zealand', 'NZ'),
    ('Nicaragua', 'NI'),
    ('Niger', 'NE'),
    ('Nigeria', 'NG'),
    ('North Macedonia', 'MK'),
    ('Northern Ireland', 'GB'),
    ('Norway', 'NO'),
    ('Oman', 'OM'),
    ('Pakistan', 'PK'),
    ('Palestine', 'PS'),
    ('Panama', 'PA'),
    ('Papua New Guinea', 'PG'),
    ('Paraguay', 'PY'),
    ('Peru', 'PE'),
    ('Philippines', 'PH'),
    ('Poland', 'PL'),
    ('Portugal', 'PT'),
    ('Puerto Rico', 'PR'),
    ('Qatar', 'QA'),
    ('Republic of Ireland', 'IE'),
    ('Romania', 'RO'),
    ('Russia', 'RU'),
    ('Rwanda', 'RW'),
    ('Saint Kitts and Nevis', 'KN'),
    ('Saint Lucia', 'LC'),
    ('Saint Vincent and the Grenadines', 'VC'),
    ('Samoa', 'WS'),
    ('San Marino', 'SM'),
    ('Sao Tome and Principe', 'ST'),
    ('Saudi Arabia', 'SA'),
    ('Scotland', 'GB'),
    ('Senegal', 'SN'),
    ('Serbia', 'RS'),
    ('Seychelles', 'SC'),
    ('Sierra Leone', 'SL'),
    ('Singapore', 'SG'),
    ('Sint Maarten', 'SX'),
    ('Slovakia', 'SK'),
    ('Slovenia', 'SI'),
    ('Solomon Islands', 'SB'),
    ('Somalia', 'SO'),
    ('South Africa', 'ZA'),
    ('South Sudan', 'SS'),
    ('Spain', 'ES'),
    ('Sri Lanka', 'LK'),
    ('Sudan', 'SD'),
    ('Suriname', 'SR'),
    ('Sweden', 'SE'),
    ('Switzerland', 'CH'),
    ('Syria', 'SY'),
    ('Tajikistan', 'TJ'),
    ('Tanzania', 'TZ'),
    ('Thailand', 'TH'),
    ('Timor-Leste', 'TL'),
    ('Togo', 'TG'),
    ('Tonga', 'TO'),
    ('Trinidad and Tobago', 'TT'),
    ('Tunisia', 'TN'),
    ('Turkey', 'TR'),
    ('Turkmenistan', 'TM'),
    ('Turks and Caicos Islands', 'TC'),
    ('Tuvalu', 'TV'),
    ('Uganda', 'UG'),
    ('Ukraine', 'UA'),
    ('United Arab Emirates', 'AE'),
    ('United States of America', 'US'),
    ('Uruguay', 'UY'),
    ('Uzbekistan', 'UZ'),
    ('Vanuatu', 'VU'),
    ('Venezuela', 'VE'),
    ('Vietnam', 'VN'),
    ('Wales', 'GB'),
    ('Yemen', 'YE'),
    ('Zambia', 'ZM'),
    ('Zimbabwe', 'ZW')
]

# Function to generate a unique_id
def generate_unique_id(country_code):
    current_date = datetime.now().strftime("%Y%m%d")
    epoch_time = int(time.time() * 1000)  # Current time in milliseconds
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{country_code}{current_date}{epoch_time}{random_string}"

# Function to insert a single player's data
def insert_player_data():
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    country_code = random.choice(football_playing_countries)[1]
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
num_players = 10000000

# Use ThreadPoolExecutor to insert data concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(insert_player_data) for _ in range(num_players)]
    for future in as_completed(futures):
        try:
            future.result()
        except Exception as e:
            print(f"Error: {e}")

print("Additional player data and stats inserted successfully!")

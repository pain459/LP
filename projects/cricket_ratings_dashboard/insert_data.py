import random
import string
from faker import Faker
from app import create_app, get_redis_client
from app.models import CountryRanking, Player, db

app = create_app()
app.app_context().push()
redis_client = get_redis_client()
fake = Faker()

# List of country codes (example)
country_codes = {
    'Afghanistan': 'AF',
    'Australia': 'AU',
    'Bangladesh': 'BD',
    'England': 'GB',
    'India': 'IN',
    'Ireland': 'IE',
    'New Zealand': 'NZ',
    'Pakistan': 'PK',
    'South Africa': 'ZA',
    'Sri Lanka': 'LK',
    'West Indies': 'WI',
    'Zimbabwe': 'ZW',
    'Nepal': 'NP',
    'Netherlands': 'NL',
    'Scotland': 'SC',
    'UAE': 'AE',
    'USA': 'US',
    'Canada': 'CA'
}

def generate_points():
    return random.randint(0, 2500)

def generate_unique_id(base_id):
    return f"{base_id}_{''.join(random.choices(string.ascii_letters + string.digits, k=6))}"

def insert_countries():
    for country, code in country_codes.items():
        unique_id = f"{code}_0001"
        points = generate_points()
        ranking = CountryRanking(unique_id=unique_id, country=country, points=points)
        db.session.add(ranking)
        redis_client.zadd('country_rankings', {country: points})
    db.session.commit()

def insert_players():
    countries = CountryRanking.query.all()
    for country in countries:
        for _ in range(1000):  # Insert 1000 players per country
            unique_id = generate_unique_id(country.unique_id)
            name = fake.name()
            points = generate_points()
            player = Player(unique_id=unique_id, name=name, country_unique_id=country.unique_id)
            db.session.add(player)
            redis_client.zadd('player_rankings', {unique_id: points})
    db.session.commit()

if __name__ == "__main__":
    insert_countries()
    insert_players()
    print("Data inserted successfully!")

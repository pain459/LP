import random
from app import create_app, db, get_redis_client
from app.models import CountryRanking

app = create_app()
app.app_context().push()
redis_client = get_redis_client()

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

def insert_countries():
    for country, code in country_codes.items():
        unique_id = f"{code}_0001"
        points = generate_points()
        ranking = CountryRanking(unique_id=unique_id, country=country, points=points)
        db.session.add(ranking)
        redis_client.zadd('country_rankings', {country: points})
    db.session.commit()

if __name__ == "__main__":
    insert_countries()
    print("Data inserted successfully!")

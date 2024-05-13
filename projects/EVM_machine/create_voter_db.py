import sqlite3
from faker import Faker

def create_database():
    conn = sqlite3.connect('voters.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE voters
                 (name text, age integer, voter_id_number text, polling_booth_id text, voted boolean)''')

    fake = Faker()
    for _ in range(100):  # Generate 100 fake voters
        name = fake.name()
        age = fake.random_int(min=18, max=90)
        voter_id_number = fake.uuid4()
        polling_booth_id = fake.random_int(min=1, max=10)
        voted = False
        c.execute("INSERT INTO voters VALUES (?, ?, ?, ?, ?)", (name, age, voter_id_number, polling_booth_id, voted))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()

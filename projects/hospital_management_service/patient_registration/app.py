import time
import psycopg2
from . import create_app

def wait_for_db():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                dbname='hospital_data',
                user='hospital_admin',
                password='admin_password',
                host='db'
            )
            conn.close()
            print("Database connection established.")
            return True
        except psycopg2.OperationalError:
            retries -= 1
            print(f"Database connection failed. Retrying in 5 seconds... ({retries} retries left)")
            time.sleep(5)
    return False

def check_and_create_table():
    conn = psycopg2.connect(
        dbname='hospital_data',
        user='hospital_admin',
        password='admin_password',
        host='db'
    )
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        gender VARCHAR(10),
        address TEXT,
        contact VARCHAR(15)
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    if wait_for_db():
        check_and_create_table()
        app = create_app()
        app.run(host='0.0.0.0')
    else:
        print("Error: Unable to connect to the database after several retries.")

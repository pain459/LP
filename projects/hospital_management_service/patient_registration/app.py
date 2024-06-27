import logging
import time
import psycopg2
from flask import Flask
from sqlalchemy.exc import IntegrityError
from . import create_app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
            logger.info("Database connection established.")
            return True
        except psycopg2.OperationalError:
            retries -= 1
            logger.warning(f"Database connection failed. Retrying in 5 seconds... ({retries} retries left)")
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
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        gender VARCHAR(10) NOT NULL,
        address TEXT,
        contact VARCHAR(15) UNIQUE NOT NULL,
        unique_id VARCHAR(64) UNIQUE NOT NULL
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
        logger.error("Error: Unable to connect to the database after several retries.")

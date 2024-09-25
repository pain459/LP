import pandas as pd
import psycopg2
from datetime import datetime

# Configurations (Database credentials)
DB_HOST = 'db'
DB_NAME = 'etl_db'
DB_USER = 'user'
DB_PASS = 'password'

# Extract: Read data from a CSV file
def extract(file_path):
    print(f"{datetime.now()} - Extracting data from {file_path}")
    return pd.read_csv(file_path)

# Transform: Clean the data
def transform(data):
    print(f"{datetime.now()} - Transforming data")
    data['cleaned_column'] = data['column_name'].apply(lambda x: x.strip().lower())
    return data

# Load: Load data into PostgreSQL database
def load(data):
    print(f"{datetime.now()} - Loading data into database")
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
    cursor = conn.cursor()
    for _, row in data.iterrows():
        cursor.execute("INSERT INTO target_table (column_name) VALUES (%s)", (row['cleaned_column'],))
    conn.commit()
    cursor.close()
    conn.close()

# ETL pipeline
def etl_pipeline(file_path):
    data = extract(file_path)
    cleaned_data = transform(data)
    load(cleaned_data)
    print(f"{datetime.now()} - ETL pipeline completed")

if __name__ == "__main__":
    etl_pipeline("/data/source_file.csv")

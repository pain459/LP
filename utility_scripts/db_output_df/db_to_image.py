import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
DB_TYPE = 'postgresql'
DB_DRIVER = 'psycopg2'
DB_USER = 'your_username'
DB_PASS = 'your_password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'your_database'

# Create the connection string
DATABASE_URI = f"{DB_TYPE}+{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create a database engine
engine = create_engine(DATABASE_URI)

# Define the query to retrieve data
query = "SELECT * FROM your_table"

# Fetch data from the database into a DataFrame
df = pd.read_sql(query, engine)

# Display the DataFrame without the index column
print(df.to_string(index=False))

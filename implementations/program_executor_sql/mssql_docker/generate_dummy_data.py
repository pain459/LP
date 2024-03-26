from faker import Faker
import pyodbc

# Connection parameters
server = 'mssql'  # Service name of the MSSQL Server container
database = 'master'  # You can specify your database name here
username = 'sa'
password = 'YourStrong!Passw0rd'  # Use the password you set in the docker-compose file
port = '1433'

# Connection string
conn_str = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'

# Function to check if the table exists
def table_exists(table_name):
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = ?", table_name)
        row = cursor.fetchone()
        exists = row is not None
        cursor.close()
        conn.close()
        return exists
    except pyodbc.Error as e:
        print("Error checking table existence:", e)
        return False

# Function to create the dummy table if it doesn't exist
def create_dummy_table():
    try:
        if not table_exists('DummyTable'):
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE DummyTable (Id INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(100), Email NVARCHAR(100))")
            conn.commit()
            cursor.close()
            conn.close()
            print("Dummy table created successfully.")
        else:
            print("Dummy table already exists.")
    except pyodbc.Error as e:
        print("Error creating dummy table:", e)

# Function to generate dummy data
def generate_dummy_data():
    fake = Faker()
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        for _ in range(10):  # Generating 10 dummy records as an example
            name = fake.name()
            email = fake.email()
            cursor.execute("INSERT INTO DummyTable (Name, Email) VALUES (?, ?)", name, email)
        conn.commit()
        cursor.close()
        conn.close()
        print("Dummy data generated successfully.")
    except pyodbc.Error as e:
        print("Error connecting to the database or executing query:", e)

if __name__ == "__main__":
    create_dummy_table()  # Create the table if it doesn't exist
    generate_dummy_data()  # Generate dummy data

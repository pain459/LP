import psycopg2

# Database connection parameters
dbname = "postgres"
user = "postgres"
password = "mysecretpassword"
host = "localhost"
port = "5432"

try:
    # Establish a connection to the database
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a simple SQL query to verify the connection
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Connected to PostgreSQL server, version: {db_version}")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except (Exception, psycopg2.Error) as error:
    print(f"Error connecting to PostgreSQL database: {error}")

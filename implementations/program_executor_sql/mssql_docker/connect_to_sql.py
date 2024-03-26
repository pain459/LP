import pyodbc

# Connection parameters
server = 'mssql'  # Service name of the MSSQL Server container
database = 'master'  # You can specify your database name here
username = 'sa'
password = 'YourStrong!Passw0rd'  # Use the password you set in the docker-compose file
port = '1433'

# Connection string
conn_str = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'

try:
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Execute a sample query
    cursor.execute("SELECT @@version")
    row = cursor.fetchone()

    # Print query result
    print("SQL Server version:", row[0])

    # Close the cursor and connection
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print("Error connecting to the database:", e)

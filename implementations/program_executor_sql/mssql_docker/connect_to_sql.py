import pyodbc
import time

# Connection parameters
server = 'mssql'  # Service name of the MSSQL Server container
database = 'master'  # You can specify your database name here
username = 'sa'
password = 'YourStrong!Passw0rd'  # Use the password you set in the docker-compose file
port = '1433'

# Connection string
conn_str = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'

# Function to connect to the database and check if the connection is successful
def check_connection():
    try:
        conn = pyodbc.connect(conn_str, timeout=5)  # Adjust timeout as needed
        conn.close()
        return True
    except pyodbc.Error:
        return False

# Main function
def main():
    while True:
        if check_connection():
            print("Connectivity to SQL Server established.")
            # Here you can call other functions or scripts
            break  # Exit loop if connectivity is established
        else:
            print("Connection failed. Retrying in 1 minute...")
            time.sleep(60)  # Wait for 1 minute before trying again

if __name__ == "__main__":
    main()

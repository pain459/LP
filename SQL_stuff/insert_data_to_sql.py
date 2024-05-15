import pyodbc

# Database connection details
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'

# Connect to the database
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Batch size
batch_size = 1000

# Fetch and insert data in batches
last_mod_counter = 0
while True:
    # Fetch a batch of rows from the source table
    cursor.execute("""
        SELECT TOP (?) Column1, Column2, ModCounter
        FROM SourceTable
        WHERE ModCounter > ?
        ORDER BY ModCounter
    """, batch_size, last_mod_counter)

    rows = cursor.fetchall()

    # If no rows are returned, break the loop
    if not rows:
        break

    # Insert the batch of rows into the destination table
    for row in rows:
        cursor.execute("""
            INSERT INTO DestinationTable (Column1, Column2, ModCounter)
            VALUES (?, ?, ?)
        """, row.Column1, row.Column2, row.ModCounter)

    # Commit the transaction
    conn.commit()

    # Update the last modification counter
    last_mod_counter = rows[-1].ModCounter

# Close the cursor and connection
cursor.close()
conn.close()

print("Data inserted successfully in batches.")

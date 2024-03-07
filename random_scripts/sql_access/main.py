import pyodbc


def query_sql_server(server, database, query):
    # Connect to sql server
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')

    # Create cursor from the application
    cursor = conn.cursor()

    try:
        # Execute the query
        cursor.execute(query)
        # Fetch all results
        rows = cursor.fetchall()
        # Print the results
        for i in rows:
            print(i)

    except Exception as e:
        print("Error executing SQL: ", e)

    finally:
        cursor.close()
        conn.close()


# Example usage
server = 'WATER'
database = 'AdventureWorks2022'
query = """
        select ProductID,Name, ProductNumber, DaysToManufacture from Production.Product 
        where DaysToManufacture > 1
        and DaysToManufacture < 4
        """

query_sql_server(server=server, database=database, query=query)

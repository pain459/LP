import pyodbc
import argparse


# Constants
SERVER = 'WATER'
DATABASE = 'AdventureWorks2022'


def query_sql_server(server, database, query):
    # Connect to sql server
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')

    # Create cursor from the application
    cursor = conn.cursor()

    try:
        query_results = []
        # Execute the query
        cursor.execute(query)
        # Fetch all results
        rows = cursor.fetchall()
        # Print the results
        for i in rows:
            query_results.append(list(i))
        return query_results

    except Exception as e:
        print("Error executing SQL: ", e)

    finally:
        cursor.close()
        conn.close()


def parse_arguments():
    # create argument parser
    parser = argparse.ArgumentParser(description='Query SQL server.')

    # Add arguments
    parser.add_argument('--server', default=SERVER, help='SQL Server hostname or IP address')
    parser.add_argument('--database', default=DATABASE, help='Database name')
    parser.add_argument('--query_part', required=True, help='Part of your query')

    # Return Parse arguments object
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Construct full query
    query = f"select ProductID,Name, ProductNumber, DaysToManufacture from Production.Product where {args.query_part}"

    # Execute query
    # result = query_sql_server(server=server, database=database, query=query)
    result = query_sql_server(args.server, args.database, query)

    print(result)


if __name__ == "__main__":
    main()

# Sample invocation
# $ python main.py --server 'WATER' --database 'AdventureWorks2022' --query_part 'DaysToManufacture > 1 and DaysToManufacture < 4'
# Execution using default arguments
# $ python main.py --query_part 'DaysToManufacture > 1 and DaysToManufacture < 4'

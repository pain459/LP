import psycopg2
from datetime import datetime, timedelta

def populate_team_calendar(db_config, start_date, end_date):
    """
    Populate the team_calendar table in PostgreSQL with default values for 2025.

    Args:
    - db_config (dict): Dictionary with database connection parameters.
    - start_date (str): Start date in 'YYYYMMDD' format.
    - end_date (str): End date in 'YYYYMMDD' format.
    """
    # Convert start_date and end_date to datetime objects
    start_date = datetime.strptime(start_date, "%Y%m%d")
    end_date = datetime.strptime(end_date, "%Y%m%d")

    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"]
        )
        cursor = conn.cursor()

        # Create the team_calendar table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS team_calendar (
                date DATE PRIMARY KEY,
                day VARCHAR(10) NOT NULL,
                member1 INTEGER NOT NULL,
                member2 INTEGER NOT NULL,
                member3 INTEGER NOT NULL
            );
        """)
        conn.commit()
        print("Table 'team_calendar' is ready.")

        # Generate data for the table
        current_date = start_date
        while current_date <= end_date:
            day_name = current_date.strftime("%A")
            is_working = 0 if day_name in ["Saturday", "Sunday"] else 1
            
            # Insert data into the table
            cursor.execute("""
                INSERT INTO team_calendar (date, day, member1, member2, member3)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (date) DO NOTHING;
            """, (current_date.strftime("%Y%m%d"), day_name, is_working, is_working, is_working))

            current_date += timedelta(days=1)

        conn.commit()
        print(f"Team calendar populated from {start_date.strftime('%Y%m%d')} to {end_date.strftime('%Y%m%d')}.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # PostgreSQL connection configuration
    db_config = {
        "dbname": "holidays_db",   # Replace with your database name
        "user": "postgres",        # Replace with your username
        "password": "password",    # Replace with your password
        "host": "localhost",       # Replace with your host
        "port": "5432"             # Replace with your port
    }

    # Populate the team_calendar table for 2025
    populate_team_calendar(db_config, "20250101", "20251231")

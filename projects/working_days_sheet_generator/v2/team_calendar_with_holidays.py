import psycopg2

def mark_holidays_in_team_calendar(db_config):
    """
    Mark holidays in the team_calendar table based on fixed_holidays data.

    Args:
    - db_config (dict): Dictionary with database connection parameters.
    """
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"]
        )
        cursor = conn.cursor()

        # Fetch all holidays from fixed_holidays table
        cursor.execute("SELECT holiday_date FROM fixed_holidays;")
        holidays = cursor.fetchall()
        holiday_dates = [row[0] for row in holidays]

        print(f"Fetched {len(holiday_dates)} holidays from fixed_holidays.")

        # Update team_calendar to mark holidays as off (0) for all members
        for holiday_date in holiday_dates:
            cursor.execute("""
                UPDATE team_calendar
                SET member1 = 0, member2 = 0, member3 = 0
                WHERE date = %s;
            """, (holiday_date,))
        
        conn.commit()
        print(f"Marked {len(holiday_dates)} holidays in the team_calendar table.")
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

    # Mark holidays in the team_calendar table
    mark_holidays_in_team_calendar(db_config)

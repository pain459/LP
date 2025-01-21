import psycopg2
import argparse

def modify_working_day(db_config, date, member, status, allow_weekend_override):
    """
    Modify the working status of a specific member for a given date in the team_calendar table.

    Args:
    - db_config (dict): Database connection parameters.
    - date (str): The date to modify in 'YYYYMMDD' format.
    - member (str): The member to modify (e.g., 'member1', 'member2', 'member3').
    - status (int): The status to set (1 = working, 0 = off).
    - allow_weekend_override (bool): Allow marking weekends as working days if True.
    """
    try:
        # Validate member input
        if member not in ["member1", "member2", "member3"]:
            raise ValueError(f"Invalid member: {member}. Allowed values are 'member1', 'member2', 'member3'.")

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"]
        )
        cursor = conn.cursor()

        # Check if the date exists and fetch the day
        cursor.execute("SELECT day FROM team_calendar WHERE date = %s;", (date,))
        result = cursor.fetchone()
        if not result:
            raise ValueError(f"Date {date} not found in team_calendar.")

        day_name = result[0]

        # Prevent marking weekends as working days if not allowed
        if not allow_weekend_override and status == 1 and day_name in ["Saturday", "Sunday"]:
            raise ValueError(f"Cannot mark a weekend ({day_name}) as a working day without override enabled.")

        # Update the working status of the member for the given date
        cursor.execute(f"""
            UPDATE team_calendar
            SET {member} = %s
            WHERE date = %s;
        """, (status, date))
        conn.commit()
        print(f"Successfully updated {member} on {date} to {'working' if status == 1 else 'off'}.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Modify a team member's working day status in the team_calendar table.")
    parser.add_argument("date", type=str, help="Date to modify in 'YYYYMMDD' format.")
    parser.add_argument("member", type=str, help="Team member to modify (e.g., 'member1', 'member2', 'member3').")
    parser.add_argument("status", type=int, choices=[0, 1], help="Status to set (1 = working, 0 = off).")
    parser.add_argument("--allow_weekend_override", action="store_true", help="Allow marking weekends as working days.")

    # Parse arguments
    args = parser.parse_args()

    # PostgreSQL connection configuration
    db_config = {
        "dbname": "holidays_db",   # Replace with your database name
        "user": "postgres",        # Replace with your username
        "password": "password",    # Replace with your password
        "host": "localhost",       # Replace with your host
        "port": "5432"             # Replace with your port
    }

    # Call the function with parsed arguments
    modify_working_day(db_config, args.date, args.member, args.status, args.allow_weekend_override)

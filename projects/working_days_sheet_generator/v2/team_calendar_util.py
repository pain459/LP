import psycopg2
import argparse

def get_active_members(db_config):
    """
    Fetch the list of active members from the active_members table.
    """
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT member_name FROM active_members;")
        members = [row[0] for row in cursor.fetchall()]
        return members
    finally:
        cursor.close()
        conn.close()

def get_total_working_days(db_config, start_date, end_date, member=None):
    """
    Fetch total working days for all active members or a specific member.
    """
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        if member:
            # Specific member
            query = f"SELECT SUM({member}) FROM team_calendar WHERE date BETWEEN %s AND %s;"
            cursor.execute(query, (start_date, end_date))
            result = cursor.fetchone()[0] or 0
            return result
        else:
            # Dynamically fetch active members and calculate total
            active_members = get_active_members(db_config)
            query = f"""
                SELECT {', '.join([f'SUM({m})' for m in active_members])}
                FROM team_calendar
                WHERE date BETWEEN %s AND %s;
            """
            cursor.execute(query, (start_date, end_date))
            result = cursor.fetchone()
            return {active_members[i]: result[i] or 0 for i in range(len(active_members))}
    finally:
        cursor.close()
        conn.close()

def get_total_non_working_days(db_config, start_date, end_date, include_weekends=True):
    """
    Fetch total non-working days in a given date range for active members.
    """
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Dynamically fetch active members
        active_members = get_active_members(db_config)
        member_conditions = " OR ".join([f"{m} = 0" for m in active_members])

        if include_weekends:
            # Include weekends
            query = f"""
                SELECT COUNT(*)
                FROM team_calendar
                WHERE date BETWEEN %s AND %s
                  AND ({member_conditions});
            """
        else:
            # Exclude weekends
            query = f"""
                SELECT COUNT(*)
                FROM team_calendar
                WHERE date BETWEEN %s AND %s
                  AND ({member_conditions})
                  AND day NOT IN ('Saturday', 'Sunday');
            """
        cursor.execute(query, (start_date, end_date))
        result = cursor.fetchone()[0]
        return result
    finally:
        cursor.close()
        conn.close()

def purge_member_column(db_config, member):
    """
    Purge the given member column from the team_calendar table and update active_members.
    """
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Remove the member from active_members
        cursor.execute("DELETE FROM active_members WHERE member_name = %s;", (member,))
        conn.commit()

        # Drop the column from team_calendar
        cursor.execute(f"ALTER TABLE team_calendar DROP COLUMN {member};")
        conn.commit()

        print(f"Column {member} purged and removed from active_members.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

def print_report(db_config, start_date, end_date):
    """
    Print a full report with total working and non-working days for all active members.
    """
    try:
        working_days = get_total_working_days(db_config, start_date, end_date)
        non_working_days_incl_weekends = get_total_non_working_days(db_config, start_date, end_date, include_weekends=True)
        non_working_days_excl_weekends = get_total_non_working_days(db_config, start_date, end_date, include_weekends=False)

        print("Report:")
        print(f"Total working days in range ({start_date} to {end_date}): {working_days}")
        print(f"Total non-working days (including weekends): {non_working_days_incl_weekends}")
        print(f"Total non-working days (excluding weekends): {non_working_days_excl_weekends}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Team Calendar Utility")
    parser.add_argument("--start_date", type=str, help="Start date in YYYYMMDD format.")
    parser.add_argument("--end_date", type=str, help="End date in YYYYMMDD format.")
    parser.add_argument("--member", type=str, help="Specify a member to query (e.g., 'member1').")
    parser.add_argument("--purge_member", type=str, help="Specify a member to purge (e.g., 'member2').")
    parser.add_argument("--print_report", action="store_true", help="Print a full report.")

    args = parser.parse_args()

    # PostgreSQL connection configuration
    db_config = {
        "dbname": "holidays_db",   # Replace with your database name
        "user": "postgres",        # Replace with your username
        "password": "password",    # Replace with your password
        "host": "localhost",       # Replace with your host
        "port": "5432"             # Replace with your port
    }

    if args.purge_member:
        purge_member_column(db_config, args.purge_member)
    elif args.print_report:
        if not args.start_date or not args.end_date:
            print("Error: Both start_date and end_date must be provided for the report.")
        else:
            print_report(db_config, args.start_date, args.end_date)
    elif args.member:
        if not args.start_date or not args.end_date:
            print("Error: Both start_date and end_date must be provided to query a member.")
        else:
            working_days = get_total_working_days(db_config, args.start_date, args.end_date, args.member)
            print(f"Total working days for {args.member} from {args.start_date} to {args.end_date}: {working_days}")
    else:
        if not args.start_date or not args.end_date:
            print("Error: Both start_date and end_date must be provided.")
        else:
            working_days = get_total_working_days(db_config, args.start_date, args.end_date)
            print(f"Total working days from {args.start_date} to {args.end_date}: {working_days}")

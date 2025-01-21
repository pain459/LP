import psycopg2

def setup_active_members_table(db_config):
    """
    Create the active_members table and populate it with initial members.
    """
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Create the active_members table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS active_members (
                member_name VARCHAR(50) PRIMARY KEY
            );
        """)
        conn.commit()
        print("Table 'active_members' is ready.")

        # Populate with default members if empty
        cursor.execute("SELECT COUNT(*) FROM active_members;")
        if cursor.fetchone()[0] == 0:
            members = ["member1", "member2", "member3"]
            cursor.executemany("INSERT INTO active_members (member_name) VALUES (%s);", [(m,) for m in members])
            conn.commit()
            print("Default members added to 'active_members'.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    db_config = {
        "dbname": "holidays_db",   # Replace with your database name
        "user": "postgres",        # Replace with your username
        "password": "password",    # Replace with your password
        "host": "localhost",       # Replace with your host
        "port": "5432"             # Replace with your port
    }

    setup_active_members_table(db_config)

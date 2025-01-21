import psycopg2
import pandas as pd

def populate_fixed_holidays(db_config, holiday_data):
    """
    Populate the fixed_holidays table in PostgreSQL with the given holiday data.

    Args:
    - db_config (dict): Dictionary with database connection parameters.
    - holiday_data (list of dict): List of holiday data with 'holiday_date' and 'holiday_name'.
    """
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
        
        # Create the fixed_holidays table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fixed_holidays (
                holiday_date DATE PRIMARY KEY,
                holiday_name VARCHAR(255) NOT NULL
            );
        """)
        conn.commit()
        print("Table 'fixed_holidays' is ready.")
        
        # Insert holiday data into the table
        for holiday in holiday_data:
            cursor.execute("""
                INSERT INTO fixed_holidays (holiday_date, holiday_name)
                VALUES (%s, %s)
                ON CONFLICT (holiday_date) DO NOTHING;
            """, (holiday["holiday_date"], holiday["holiday_name"]))
        
        conn.commit()
        print("Holiday data has been inserted successfully.")
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
    
    # Holiday data (example)
    holiday_data = [
        {"holiday_date": "20250101", "holiday_name": "New Year's Day"},
        {"holiday_date": "20250126", "holiday_name": "Republic Day"},
        {"holiday_date": "20250317", "holiday_name": "Holi"},
        {"holiday_date": "20250815", "holiday_name": "Independence Day"},
        {"holiday_date": "20251225", "holiday_name": "Christmas"}
    ]
    
    # Populate the fixed_holidays table
    populate_fixed_holidays(db_config, holiday_data)

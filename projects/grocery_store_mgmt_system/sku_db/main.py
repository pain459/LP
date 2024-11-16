import sqlite3
import time

DB_PATH = "/data/sku.db"

def create_table():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sku (
            SKU_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Item_Name TEXT NOT NULL,
            Category TEXT,
            Price REAL NOT NULL,
            Stock_Quantity INTEGER NOT NULL,
            Description TEXT
        )
        """)
        print("SKU Table created successfully.")

def add_item(item_name, category, price, stock_quantity, description):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO sku (Item_Name, Category, Price, Stock_Quantity, Description)
        VALUES (?, ?, ?, ?, ?)
        """, (item_name, category, price, stock_quantity, description))
        conn.commit()
        print(f"Item '{item_name}' added successfully.")

if __name__ == "__main__":
    create_table()
    # Example usage: Add an item
    add_item("Apple", "Fruit", 2.5, 100, "Fresh red apples")
    
    # Keep the script running to prevent container from exiting
    print("Container is running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting container...")

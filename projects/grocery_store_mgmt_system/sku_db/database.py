import sqlite3
import csv

DB_PATH = "/data/sku.db"
CSV_PATH = "/sku_db/sku_list.csv"

def create_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sku_transactions (
            Transaction_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SKU_ID INTEGER NOT NULL,
            Item_Name TEXT NOT NULL,
            Quantity INTEGER NOT NULL,
            Price REAL NOT NULL,
            Transaction_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_report (
            SKU_ID INTEGER PRIMARY KEY,
            Item_Name TEXT NOT NULL,
            Total_Quantity INTEGER DEFAULT 0
        )
        """)
        conn.commit()

def add_sku_entry(sku_id, quantity, price=None):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Load data from CSV
        with open(CSV_PATH, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["SKU_ID"]) == sku_id:
                    item_name = row["Item_Name"]
                    default_price = float(row["Default_Price"])
                    break
            else:
                return {"error": f"SKU_ID {sku_id} not found."}

        # Insert into transactions
        final_price = price if price else default_price
        cursor.execute("""
        INSERT INTO sku_transactions (SKU_ID, Item_Name, Quantity, Price)
        VALUES (?, ?, ?, ?)
        """, (sku_id, item_name, quantity, final_price))

        # Update stock report
        cursor.execute("""
        INSERT INTO stock_report (SKU_ID, Item_Name, Total_Quantity)
        VALUES (?, ?, ?)
        ON CONFLICT(SKU_ID) DO UPDATE SET Total_Quantity = Total_Quantity + ?
        """, (sku_id, item_name, quantity, quantity))

        conn.commit()
        return {"message": "SKU added successfully."}

def get_stock_report():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stock_report")
        return cursor.fetchall()
    
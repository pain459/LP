import sqlite3
import csv
import os
from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import print_formatted_text, prompt

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
        print_formatted_text("Tables created successfully.")

def load_csv_data(sku_id):
    with open(CSV_PATH, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["SKU_ID"]) == sku_id:
                return row
    return None

def add_sku_entry(sku_id, quantity, override_price=None):
    sku_data = load_csv_data(sku_id)
    if not sku_data:
        print_formatted_text(f"SKU ID {sku_id} not found in CSV.")
        return

    item_name = sku_data["Item_Name"]
    default_price = float(sku_data["Default_Price"])
    price = override_price if override_price else default_price

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO sku_transactions (SKU_ID, Item_Name, Quantity, Price)
        VALUES (?, ?, ?, ?)
        """, (sku_id, item_name, quantity, price))

        cursor.execute("""
        INSERT INTO stock_report (SKU_ID, Item_Name, Total_Quantity)
        VALUES (?, ?, ?)
        ON CONFLICT(SKU_ID) DO UPDATE SET Total_Quantity = Total_Quantity + ?
        """, (sku_id, item_name, quantity, quantity))

        conn.commit()
        print_formatted_text(f"SKU ID {sku_id} ({item_name}) updated: Quantity {quantity}, Price {price}.")

def display_stock_report():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stock_report")
        rows = cursor.fetchall()
        print_formatted_text("\nStock Report:")
        print_formatted_text(f"{'SKU_ID':<10} {'Item_Name':<20} {'Total_Quantity':<15}")
        for row in rows:
            print_formatted_text(f"{row[0]:<10} {row[1]:<20} {row[2]:<15}")

def main_menu():
    session = PromptSession()
    while True:
        print_formatted_text("\n--- SKU Management System ---")
        print_formatted_text("1. Add SKU Entry")
        print_formatted_text("2. View Stock Report")
        print_formatted_text("3. Exit")
        choice = session.prompt("Enter your choice: ")

        if choice == '1':
            try:
                sku_id = int(session.prompt("Enter SKU ID: "))
                quantity = int(session.prompt("Enter Quantity: "))
                override_price = session.prompt("Enter Price (leave blank to use default): ", default="")
                override_price = float(override_price) if override_price else None
                add_sku_entry(sku_id, quantity, override_price)
            except ValueError:
                print_formatted_text("Invalid input. Please try again.")
        elif choice == '2':
            display_stock_report()
        elif choice == '3':
            print_formatted_text("Exiting SKU Management System. Goodbye!")
            break
        else:
            print_formatted_text("Invalid choice. Please try again.")

if __name__ == "__main__":
    create_tables()
    main_menu()

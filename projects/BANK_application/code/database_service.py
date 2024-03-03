import sqlite3


class DatabaseService:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Create tables if they don't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                account_type TEXT,
                balance REAL
            )
        """)
        self.connection.commit()

    def add_account(self, user_id, account_type, initial_balance):
        # Add a new account to the database
        self.cursor.execute("""
            INSERT INTO accounts (user_id, account_type, balance)
            VALUES (?, ?, ?)
        """, (user_id, account_type, initial_balance))
        self.connection.commit()

    def get_accounts(self, user_id):
        # Get accounts associated with the specified user_id
        self.cursor.execute("""
               SELECT * FROM accounts WHERE user_id = ?
           """, (user_id,))
        accounts = self.cursor.fetchall()
        account_details = []
        for account in accounts:
            account_dict = {
                "id": account[0],
                "user_id": account[1],
                "account_type": account[2],
                "balance": account[3]
            }
            account_details.append(account_dict)
        return account_details

    def update_balance(self, account_id, new_balance):
        # Update the balance of an account
        self.cursor.execute("""
            UPDATE accounts SET balance = ? WHERE id = ?
        """, (new_balance, account_id))
        self.connection.commit()


# Usage example:
# db_service = DatabaseService("bank.db")
# db_service.create_tables()
# db_service.add_account(1, "Savings", 1000.0)
# accounts = db_service.get_accounts(1)
# print(accounts)


db_service = DatabaseService("bank.db")
db_service.create_tables()
# db_service.add_account(1, "Savings", 1000.0)
# db_service.add_account(2, "Savings", 10000000.0)
# db_service.add_account(1, "Savings1", 1000.0)
# accounts = db_service.get_accounts(1)
# accounts = db_service.get_accounts(2)
# print(accounts)

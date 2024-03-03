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

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                account_id INTEGER,
                amount REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES accounts(id)
            )
        """)
        self.connection.commit()

    def add_account(self, user_id, account_type, initial_balance):
        self.cursor.execute("""
            INSERT INTO accounts (user_id, account_type, balance)
            VALUES (?, ?, ?)
        """, (user_id, account_type, initial_balance))

        account_id = self.cursor.lastrowid
        # Add initial transaction record for opening balance
        self.cursor.execute("""
            INSERT INTO transactions (account_id, amount)
            VALUES (?, ?)
        """, (account_id, initial_balance))

        self.connection.commit()

    def get_accounts(self, user_id=None):
        if user_id is not None:
            self.cursor.execute("""
                SELECT * FROM accounts WHERE user_id = ?
            """, (user_id,))
        else:
            self.cursor.execute("""
                SELECT * FROM accounts
            """)
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

    def get_account_transactions(self, account_id):
        self.cursor.execute("""
            SELECT * FROM transactions WHERE account_id = ?
        """, (account_id,))
        return self.cursor.fetchall()

    def update_balance(self, account_id, new_balance):
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

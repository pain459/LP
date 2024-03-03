# account_service.py
from database_service import DatabaseService

class AccountService:
    def __init__(self, db_name):
        self.db_service = DatabaseService(db_name)

    def create_account(self, user_id, account_type, initial_balance):
        # Check if the user already has an account of the same type
        user_accounts = self.db_service.get_accounts(user_id)
        for account in user_accounts:
            if account["account_type"] == account_type:
                raise ValueError("Account of type '{}' already exists for user {}".format(account_type, user_id))

        # If no duplicate account found, create a new account
        self.db_service.add_account(user_id, account_type, initial_balance)

    def get_user_accounts(self, user_id):
        return self.db_service.get_accounts(user_id)


# Usage example:
# account_service = AccountService("bank.db")
# account_service.create_account(1, "Savings", 1000.0)
# user_accounts = account_service.get_user_accounts(1)
# print(user_accounts)

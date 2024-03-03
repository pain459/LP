from database_service import DatabaseService

class AccountService:
    def __init__(self, db_name):
        self.db_service = DatabaseService(db_name)

    def create_account(self, user_id, account_type, initial_balance):
        try:
            # Check if the user already has an account of the same type
            user_accounts = self.db_service.get_accounts(user_id)
            for account in user_accounts:
                if account[2] == account_type:
                    raise ValueError("Account of type '{}' already exists for user {}".format(account_type, user_id))

            # If no duplicate account found, create a new account
            self.db_service.add_account(user_id, account_type, initial_balance)
            return "Account created successfully."
        except Exception as e:
            return str(e)  # Return the error message

    def get_user_accounts(self, user_id):
        user_accounts = self.db_service.get_accounts(user_id)
        return user_accounts

# Usage example:
account_service = AccountService("bank.db")
# result = account_service.create_account(1, "Savings", 1000.0)
# if isinstance(result, str):
#     print("Error:", result)
# else:
#     print(result)

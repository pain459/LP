from database_service import DatabaseService


class TransactionService:
    def __init__(self, db_name):
        self.db_service = DatabaseService(db_name)

    def transfer_funds(self, sender_account_id, receiver_account_id, amount):
        sender_account = self.get_account_by_id(sender_account_id)
        receiver_account = self.get_account_by_id(receiver_account_id)

        if sender_account and receiver_account:
            if sender_account["balance"] >= amount:
                sender_new_balance = sender_account["balance"] - amount
                receiver_new_balance = receiver_account["balance"] + amount

                self.db_service.update_balance(sender_account_id, sender_new_balance)
                self.db_service.update_balance(receiver_account_id, receiver_new_balance)
                return True, "Funds transferred successfully."
            else:
                return False, "Insufficient funds in sender account."
        else:
            return False, "One or both accounts not found."

    def get_account_by_id(self, account_id):
        # Helper function to get account details by ID
        accounts = self.db_service.get_accounts(account_id)
        if accounts:
            return accounts[0]
        else:
            return None

# Usage example:
# transaction_service = TransactionService("bank.db")
# success, message = transaction_service.transfer_funds(1, 2, 500.0)
# print(success, message)


# Usage example:
transaction_service = TransactionService("bank.db")
success, message = transaction_service.transfer_funds(2, 1, 500.0)
print(success, message)
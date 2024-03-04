# Example usage:
from account_service import AccountService

# Create an instance of AccountService
account_service = AccountService("bank.db")

# Specify the account_id for which you want to see the transaction history
account_id = 1  # Replace 123 with the actual account ID

# Fetch the transaction history for the specified account_id
transactions = account_service.db_service.get_account_transactions(account_id)

# Print the transaction history
if transactions:
    print("Transaction History for Account ID", account_id)
    for transaction in transactions:
        print("Transaction ID:", transaction['id'])
        print("Amount:", transaction['amount'])
        print("Timestamp:", transaction['timestamp'])
        print()
else:
    print("No transactions found for Account ID", account_id)

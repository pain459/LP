# Example usage:
from account_service import AccountService

# Create an instance of AccountService
account_service = AccountService("bank.db")

# Specify the account_id for which you want to see the transaction history
account_id = 2  # Replace 123 with the actual account ID

# Fetch the transaction history for the specified account_id
transactions = account_service.db_service.get_account_transactions(account_id)

# Print the transaction history
if transactions:
    print("Transaction History for Account ID", account_id)
    for transaction in transactions:
        print("ID:", transaction[0])
        print("User ID:", transaction[1])
        print("Amount:", transaction[2])
        print("Timestamp:", transaction[3])
        print()
else:
    print("No transactions found for Account ID", account_id)

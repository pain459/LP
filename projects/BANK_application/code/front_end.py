# frontend.py
from account_service import AccountService
from authentication_service import AuthenticationService

# Global variable to store the current session token
current_session_token = None


def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    result = auth_service.register_user(username, password)
    print(result)


def login():
    global current_session_token
    if current_session_token:
        print("Another user is already logged in. Please logout first.")
        return None
    else:
        username = input("Enter username: ")
        password = input("Enter password: ")
        session_token = auth_service.login_user(username, password)
        if session_token:
            print("Login successful. Session token:", session_token)
            current_session_token = session_token
            return session_token
        else:
            print("Invalid username or password.")
            return None


def logout():
    global current_session_token
    if current_session_token:
        auth_service.logout_user(current_session_token)
        print("Logged out successfully.")
        current_session_token = None
    else:
        print("No user is currently logged in.")


def view_account_details():
    global current_session_token
    if current_session_token:
        # Fetch and print account details for the authenticated user
        accounts = account_service.get_user_accounts(current_session_token)
        if accounts:
            print("Your Accounts:")
            for account in accounts:
                print("Account ID:", account['id'])
                print("Account Type:", account['account_type'])
                print("Balance:", account['balance'])
                print()

            # Prompt user to enter the account ID to fetch details
            account_id = input("Enter the Account ID you want to fetch details for: ")
            # Fetch account details directly from the database
            account_details = account_service.db_service.get_account(account_id)
            if account_details and account_details['user_id'] == current_session_token:
                print("Account Details:")
                print("Account ID:", account_details['id'])
                print("Account Type:", account_details['account_type'])
                print("Balance:", account_details['balance'])
            else:
                print("Account not found or you don't have access to this account.")
        else:
            print("No accounts found for this user.")
    else:
        print("Please login first.")


if __name__ == "__main__":
    db_name = "bank.db"
    auth_service = AuthenticationService(db_name)
    account_service = AccountService(db_name)

    while True:
        print("1. Register")
        print("2. Login")
        print("3. View Account Details")
        print("4. Logout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login()
        elif choice == "3":
            view_account_details()
        elif choice == "4":
            logout()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

from account_service import AccountService
from authentication_service import AuthenticationService

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    result = auth_service.register_user(username, password)
    print(result)

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    session_token = auth_service.login_user(username, password)
    if session_token:
        print("Login successful. Session token:", session_token)
        return session_token
    else:
        print("Invalid username or password.")
        return None

def logout(session_token):
    auth_service.logout_user(session_token)
    print("Logged out successfully.")

def view_account_details(session_token):
    if session_token:
        # Fetch and print account details for the authenticated user
        accounts = account_service.get_user_accounts(session_token)
        if accounts:
            print("Account details:")
            for account in accounts:
                print("Account ID:", account['id'])
                print("Account Type:", account['account_type'])
                print("Balance:", account['balance'])
                print()
        else:
            print("No accounts found for this user.")
    else:
        print("Please login first.")

if __name__ == "__main__":
    db_name = "bank.db"
    auth_service = AuthenticationService(db_name)
    account_service = AccountService(db_name)

    session_token = None
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
            session_token = login()
        elif choice == "3":
            view_account_details(session_token)
        elif choice == "4":
            if session_token:
                logout(session_token)
                session_token = None
            else:
                print("Please login first.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

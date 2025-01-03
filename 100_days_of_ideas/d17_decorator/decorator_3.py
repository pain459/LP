# Simulating user authentication
current_user = {"is_logged_in": False}


# Define authorization decorator
def authorize(func):
    def wrapper(*args, **kwargs):
        if current_user.get("is_logged_in"):
            print("User is authenticated!")
            return func(*args, **kwargs)
        else:
            print("Unauthorized access! Please log in.")
            return None
        
    return wrapper

# Apply the decorator to a function
@authorize
def view_profile(user_id):
    print(f"Fetching profile for user ID: {user_id}")
    return {"user_id": user_id, "name": "Doe", "age": 30}

# Call the decorated function
print(view_profile(101))  # simulation
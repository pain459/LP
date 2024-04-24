import requests

# Authenticate and get token
def login(username, password):
    try:
        response = requests.post('http://127.0.0.1:5000/login', auth=(username, password))
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data.get('token'), data.get('expiration_time')
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None, None

# Access protected endpoint
def access_protected(token):
    headers = {'token': token}
    try:
        response = requests.get('http://127.0.0.1:5000/protected', headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    token, expiration_time = login(username, password)
    
    if token:
        print("Token:", token)
        print("Token expiration time:", expiration_time)
        access_protected(token)

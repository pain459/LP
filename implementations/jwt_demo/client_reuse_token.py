import requests

# Enter your username and password
username = 'username'
password = 'password'

# Initialize token variable
token = None

def login():
    global token
    response = requests.post('http://127.0.0.1:5000/login', auth=(username, password))
    if response.status_code == 200:
        data = response.json()
        token = data['token']
        expiration_time = data['expiration_time']
        print("Token:", token)
        print("Token expiration time:", expiration_time)
    else:
        print("Failed to obtain JWT token. Status code:", response.status_code)

def access_protected():
    global token
    if token:
        headers = {'token': token}
        protected_response = requests.get('http://127.0.0.1:5000/protected', headers=headers)
        print("Protected endpoint response:", protected_response.text)
    else:
        print("No token available. Please login first.")

# Authenticate and get JWT token
login()

# Reuse the token to access the protected endpoint
access_protected()

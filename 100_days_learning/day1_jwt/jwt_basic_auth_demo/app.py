from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

# Secret key for encoding and decoding JWT
SECRET_KEY = 'your-secret-key'

# Dummy user data for demonstration
users = {
    "example_user": "password123"
}

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        # Create JWT
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401

# Route for accessing protected resource
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization').split()[1]

    try:
        # Decode the JWT
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({"message": f"Welcome {decoded_payload['username']}!"})
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(debug=True)

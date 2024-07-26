from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Secret key for encoding and decoding JWT
SECRET_KEY = 'your-secret-key'

# Dummy user data for demonstration
users = {
    "example_user": {"password": "password123", "role": "user"},
    "admin_user": {"password": "adminpass", "role": "admin"}
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = users.get(data['username'])
            if current_user is None:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated(current_user, *args, **kwargs):
            if current_user['role'] != role:
                return jsonify({'message': 'You do not have access to this resource!'}), 403
            return f(current_user, *args, **kwargs)
        return decorated
    return decorator

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')

    if username in users:
        return jsonify({'message': 'User already exists!'}), 400

    users[username] = {'password': password, 'role': role}
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username]['password'] == password:
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/refresh', methods=['POST'])
@token_required
def refresh(current_user):
    payload = {
        'username': current_user['username'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return jsonify({"token": token})

@app.route('/protected', methods=['GET'])
@token_required
def protected(current_user):
    return jsonify({"message": f"Welcome {current_user['username']}!"})

@app.route('/admin', methods=['GET'])
@token_required
@role_required('admin')
def admin(current_user):
    return jsonify({"message": f"Welcome admin {current_user['username']}!"})

if __name__ == '__main__':
    app.run(debug=True)

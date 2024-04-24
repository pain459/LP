import jwt
import datetime
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Dummy user data
users = {
    'username': 'password'
}

# Token expiration time (minutes)
TOKEN_EXPIRATION_TIME_MINUTES = 30

# Token verification decorator
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('token')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return f(*args, **kwargs)

    return decorated_function

# Authentication endpoint
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    if auth.username in users and users[auth.username] == auth.password:
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRATION_TIME_MINUTES)
        token = jwt.encode({'user': auth.username, 'exp': expiration_time}, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token, 'expiration_time': expiration_time.strftime('%Y-%m-%d %H:%M:%S')})

    return jsonify({'message': 'Invalid username or password'}), 401

# Protected endpoint
@app.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'Access granted for protected resource'})

if __name__ == '__main__':
    app.run(debug=True)

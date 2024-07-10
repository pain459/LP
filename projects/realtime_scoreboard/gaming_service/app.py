from flask import Flask, request, jsonify
import mysql.connector
import redis
import os

app = Flask(__name__)

# MySQL configuration
db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME')
}

# Redis configuration
redis_host = os.getenv('REDIS_HOST')
redis_client = redis.StrictRedis(host=redis_host, port=6379, db=0, decode_responses=True)

# Create User
@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.json['username']
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
        conn.commit()
        user_id = cursor.lastrowid
        return jsonify({'user_id': user_id, 'username': username}), 201
    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Submit Score
@app.route('/submit_score', methods=['POST'])
def submit_score():
    user_id = request.json['user_id']
    score = request.json['score']
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scores (user_id, score) VALUES (%s, %s)", (user_id, score))
        conn.commit()

        # Update leaderboard
        redis_client.zadd('leaderboard', {user_id: score})

        return jsonify({'status': 'success'}), 200
    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Get Leaderboard
@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    top_scores = redis_client.zrevrange('leaderboard', 0, 9, withscores=True)
    return jsonify(top_scores), 200

# Get User Information
@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        return jsonify(user), 200
    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Get User Scores
@app.route('/get_user_scores/<int:user_id>', methods=['GET'])
def get_user_scores(user_id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM scores WHERE user_id = %s ORDER BY created_at DESC", (user_id,))
        scores = cursor.fetchall()
        return jsonify(scores), 200
    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Update User Information
@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    username = request.json['username']
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET username = %s WHERE id = %s", (username, user_id))
        conn.commit()
        return jsonify({'status': 'success'}), 200
    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Delete User
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        redis_client.zrem('leaderboard', user_id)
        return jsonify({'status': 'success'}), 200
    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

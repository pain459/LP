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

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    top_scores = redis_client.zrevrange('leaderboard', 0, 9, withscores=True)
    return jsonify(top_scores), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify
import time
import redis

app = Flask(__name__)

# Connect to Redis (assuming Redis is running on localhost:6379)
r = redis.StrictRedis(host='redis', port=6379, db=0)

RATE_LIMIT = 5  # requests
WINDOW_SIZE = 60  # seconds

@app.route('/api', methods=['GET'])
def api():
    client_ip = request.remote_addr
    current_time = int(time.time())
    window_start = current_time - WINDOW_SIZE

    # Remove outdated requests
    r.zremrangebyscore(client_ip, 0, window_start)

    # Count requests in the current window
    request_count = r.zcount(client_ip, window_start, current_time)

    if request_count >= RATE_LIMIT:
        return jsonify({"error": "Rate limit exceeded"}), 429
    else:
        # Record the new request
        r.zadd(client_ip, {current_time: current_time})
        return jsonify({
            "time": current_time,
            "server": request.host
        }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

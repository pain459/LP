from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/publish', methods=['POST'])
def publish_message():
    data = request.json
    channel = data.get('channel')
    message = data.get('message')

    if not channel or not message:
        return jsonify({'error': 'Channel and message are required'}), 400

    r.publish(channel, message)
    return jsonify({'status': 'Message sent'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

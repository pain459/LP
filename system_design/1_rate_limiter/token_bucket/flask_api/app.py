from flask import Flask, jsonify
import time
import socket

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    # time.sleep(4)  # Simulate a delay
    response = {
        "time": int(time.time()),  # Current time in epoch UTC format
        "server": socket.gethostname()  # Server name
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

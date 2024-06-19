from flask import Flask
import time

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    time.sleep(4)  # Simulate a delay
    return "Success", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

import requests
import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_weather', methods=['GET'])
def get_weather():
    # Implement API call for weather
    return jsonify({"description": "sunny"})

@app.route('/tell_time', methods=['GET'])
def tell_time():
    current_time = time.strftime("%H:%M:%S")
    return jsonify({"time": current_time})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

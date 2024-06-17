from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Route to render the dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Route to fetch authenticated sessions
@app.route('/fetch_sessions')
def fetch_sessions():
    response = requests.get('http://localhost:5000/authenticated_sessions')
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"status": "error", "message": "Failed to fetch sessions"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

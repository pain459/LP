import pandas as pd
import os
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load voting center IDs from file
voting_centers_file = 'voting_centers.csv'
if os.path.exists(voting_centers_file):
    voting_centers_df = pd.read_csv(voting_centers_file)
else:
    print("Voting centers file not found.")
    exit()

# Create a set of valid center IDs for quick lookup
valid_center_ids = set(voting_centers_df['CenterID'].values)

# Dictionary to track authenticated sessions and their last seen times
authenticated_sessions = {}

# Route to validate center ID
@app.route('/validate_center_id', methods=['GET'])
def validate_center_id():
    center_id = request.args.get('center_id')
    if center_id in valid_center_ids:
        authenticated_sessions[center_id] = time.time()
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "Invalid center ID."}), 400

# Route to handle heartbeat updates
@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.json
    center_id = data.get('center_id')
    if center_id in authenticated_sessions:
        authenticated_sessions[center_id] = time.time()
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "Invalid center ID."}), 400

# Route to get authenticated sessions and last seen times
@app.route('/authenticated_sessions', methods=['GET'])
def get_authenticated_sessions():
    sessions = [
        {"center_id": center_id, "last_seen": time.ctime(last_seen)}
        for center_id, last_seen in authenticated_sessions.items()
    ]
    return jsonify({"status": "success", "sessions": sessions}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

import pandas as pd
import os
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

# Route to validate center ID
@app.route('/validate_center_id', methods=['GET'])
def validate_center_id():
    center_id = request.args.get('center_id')
    if center_id in valid_center_ids:
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "Invalid center ID."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

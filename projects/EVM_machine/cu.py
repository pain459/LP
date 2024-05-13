from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate_voter():
    voter_id = request.json['voter_id']
    conn = sqlite3.connect('voters.db')
    c = conn.cursor()
    c.execute("SELECT * FROM voters WHERE voter_id_number = ? AND voted = 0", (voter_id,))
    voter = c.fetchone()
    if voter:
        # Unlock the voting unit somehow, e.g., by sending a signal or message
        return jsonify({"access": "granted", "polling_booth_id": voter[3]})
    return jsonify({"access": "denied"})

@app.route('/cast_vote', methods=['POST'])
def cast_vote():
    voter_id = request.json['voter_id']
    conn = sqlite3.connect('voters.db')
    c = conn.cursor()
    # Mark the voter as having voted
    c.execute("UPDATE voters SET voted = 1 WHERE voter_id_number = ?", (voter_id,))
    conn.commit()
    return jsonify({"status": "vote registered"})

if __name__ == '__main__':
    app.run(port=5000)

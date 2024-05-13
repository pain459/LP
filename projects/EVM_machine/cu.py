# CONTROL UNIT

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate_voter():
    voter_id = request.json['voter_id']
    # Here, add logic to check voter ID
    return jsonify({"access": "granted" if voter_id == "valid_id" else "denied"})

if __name__ == '__main__':
    app.run(port=5000)

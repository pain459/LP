from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to hold vote counts
votes = {}

# Greek letter names as candidates
candidates = [chr(913+i) for i in range(20)]  # Greek capital letters Alpha to Tau
votes = {candidate: 0 for candidate in candidates}

@app.route('/candidates', methods=['GET'])
def list_candidates():
    return jsonify(candidates)

@app.route('/vote', methods=['POST'])
def cast_vote():
    candidate = request.json['candidate']
    if candidate in votes:
        votes[candidate] += 1
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed", "reason": "Invalid candidate"}), 400

if __name__ == '__main__':
    app.run(port=5001)

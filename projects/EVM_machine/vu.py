# VOTING UNIT

from flask import Flask, request, jsonify
app = Flask(__name__)
votes = {}

@app.route('/vote', methods=['POST'])
def vote():
    candidate = request.json['candidate']
    votes[candidate] = votes.get(candidate, 0) + 1
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5001)

from flask import Flask, jsonify
app = Flask(__name__)

votes = {}

@app.route('/vote', methods=['POST'])
def vote():
    candidate = request.form['candidate']
    votes[candidate] = votes.get(candidate, 0) + 1
    return jsonify({"status": "success"})

@app.route('/results', methods=['GET'])
def results():
    return jsonify(votes)

if __name__ == '__main__':
    app.run(port=5002)

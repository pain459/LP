# COUNTING MACHINE

from flask import Flask, jsonify
app = Flask(__name__)
from voting_unit import votes

@app.route('/results', methods=['GET'])
def results():
    return jsonify(votes)

if __name__ == '__main__':
    app.run(port=5002)

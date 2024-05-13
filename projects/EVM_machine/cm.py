from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Import the votes dictionary from the Voting Unit
# This is just a placeholder; in a real application, you'd need a secure and reliable way to share this data.
from voting_unit import votes

@app.route('/results', methods=['GET'])
def results():
    return jsonify(votes)

@app.route('/download_results', methods=['GET'])
def download_results():
    results = "Candidate,Votes\n" + "\n".join(f"{candidate},{count}" for candidate, count in votes.items())
    response = make_response(results)
    response.headers["Content-Disposition"] = "attachment; filename=vote_results.csv"
    response.headers["Content-Type"] = "text/csv"
    return response

if __name__ == '__main__':
    app.run(port=5002)

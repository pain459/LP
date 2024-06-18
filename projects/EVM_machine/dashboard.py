import pandas as pd
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Load the user list from CSV
user_list_df = pd.read_csv('user_list.csv')

# Function to load voting data
def load_voting_data():
    if os.path.exists('voting_data.csv'):
        return pd.read_csv('voting_data.csv')
    else:
        return pd.DataFrame(columns=["UniqueID", "Voted", "VotedToSymbol"])

# Route to serve the dashboard page
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Route to get voting data
@app.route('/data')
def get_data():
    voting_df = load_voting_data()
    total_voters = len(user_list_df)
    total_votes = voting_df['UniqueID'].nunique()
    voting_percentage = (total_votes / total_voters) * 100 if total_voters > 0 else 0

    votes_per_symbol = voting_df['VotedToSymbol'].value_counts().sort_index()
    party_symbols = {
        1: 'α (Alpha)',
        2: 'β (Beta)',
        3: 'γ (Gamma)',
        4: 'δ (Delta)',
        5: 'ε (Epsilon)',
        6: 'ζ (Zeta)',
        7: 'η (Eta)',
        8: 'θ (Theta)',
        9: 'ι (Iota)',
        10: 'κ (Kappa)'
    }
    votes_per_symbol.index = votes_per_symbol.index.map(party_symbols)

    if not votes_per_symbol.empty:
        leading_party = votes_per_symbol.idxmax()
        leading_votes = votes_per_symbol.max()
        leading_by = leading_votes - votes_per_symbol.nlargest(2).iloc[-1]
    else:
        leading_party = "None"
        leading_votes = 0
        leading_by = 0

    data = {
        'voting_percentage': float(voting_percentage),
        'votes_per_symbol': votes_per_symbol.to_dict(),
        'total_votes': int(total_votes),
        'total_voters': int(total_voters),
        'leading_party': leading_party,
        'leading_by': int(leading_by)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

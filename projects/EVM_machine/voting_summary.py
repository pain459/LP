import pandas as pd
import os

# Load the user list and voting data from CSV
user_list_csv = 'user_list.csv'
voting_csv = 'voting_data.csv'

if os.path.exists(user_list_csv) and os.path.exists(voting_csv):
    user_list_df = pd.read_csv(user_list_csv)
    voting_df = pd.read_csv(voting_csv)
else:
    print("Required CSV files are missing. Make sure 'user_list.csv' and 'voting_data.csv' exist in the directory.")
    exit()

# Greek numerals as party symbols
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

# Calculate voting percentage
total_users = len(user_list_df)
voted_users = voting_df['UniqueID'].nunique()
voting_percentage = (voted_users / total_users) * 100

# Calculate votes per symbol
votes_per_symbol = voting_df['VotedToSymbol'].value_counts().sort_index()

# Display the voting summary
print(f"Voting Percentage: {voting_percentage:.2f}%")
print("\nVotes per Symbol:")
for symbol, count in votes_per_symbol.items():
    print(f"{party_symbols[symbol]}: {count} votes")

if votes_per_symbol.empty:
    print("No votes have been cast yet.")

# Save the summary to a file
summary_file = 'voting_summary.txt'
with open(summary_file, 'w') as f:
    f.write(f"Voting Percentage: {voting_percentage:.2f}%\n\n")
    f.write("Votes per Symbol:\n")
    for symbol, count in votes_per_symbol.items():
        f.write(f"{party_symbols[symbol]}: {count} votes\n")
    if votes_per_symbol.empty:
        f.write("No votes have been cast yet.\n")

print(f"Voting summary saved to {summary_file}.")

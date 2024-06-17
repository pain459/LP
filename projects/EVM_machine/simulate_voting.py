import pandas as pd
import os

# Load the user list from CSV
user_list_df = pd.read_csv('user_list.csv')

# Create a blank CSV to store voting information if it doesn't already exist
voting_csv = 'voting_data.csv'
if not os.path.exists(voting_csv):
    voting_df = pd.DataFrame(columns=["UniqueID", "Voted", "VotedToSymbol"])
    voting_df.to_csv(voting_csv, index=False)
else:
    voting_df = pd.read_csv(voting_csv)

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

# Function to display party symbols
def display_party_symbols():
    print("Please cast your vote by selecting one of the following symbols:")
    for key, value in party_symbols.items():
        print(f"{key}. {value}")

# Function to validate unique ID
def validate_unique_id(unique_id):
    return unique_id in user_list_df['UniqueID'].values

# Function to check if user has already voted
def has_already_voted(unique_id):
    if unique_id in voting_df['UniqueID'].values:
        return voting_df[voting_df['UniqueID'] == unique_id]['Voted'].values[0] == 1
    return False

# Main voting loop
while True:
    unique_id = input("Please enter your unique ID: ").strip()
    
    if validate_unique_id(unique_id):
        if has_already_voted(unique_id):
            print("You have already voted. Thank you!")
        else:
            display_party_symbols()
            try:
                vote = int(input("Enter the number corresponding to your chosen symbol: ").strip())
                if vote in party_symbols:
                    new_vote = pd.DataFrame([[unique_id, 1, vote]], columns=["UniqueID", "Voted", "VotedToSymbol"])
                    voting_df = pd.concat([voting_df, new_vote], ignore_index=True)
                    voting_df.to_csv(voting_csv, index=False)
                    print("Thank you for voting!")
                else:
                    print("Invalid symbol selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number corresponding to the symbols.")
    else:
        print("Invalid unique ID. Please try again.")

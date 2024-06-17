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

# Function to validate unique ID
def validate_unique_id(unique_id):
    return unique_id in user_list_df['UniqueID'].values

# Function to check if user has already voted
def has_already_voted(unique_id):
    if unique_id in voting_df['UniqueID'].values:
        return voting_df[voting_df['UniqueID'] == unique_id]['Voted'].values[0] == 1
    return False

# Function to unblock user for voting
def unblock_user_for_voting(unique_id):
    if not validate_unique_id(unique_id):
        print("Invalid unique ID. Please try again.")
        return False
    if has_already_voted(unique_id):
        print("User has already voted. Cannot unblock.")
        return False
    with open('unblock.txt', 'w') as f:
        f.write(unique_id)
    print("User unblocked for voting.")
    return True

# Main admin loop
while True:
    admin_unique_id = input("Admin: Enter the unique ID to unblock for voting: ").strip()
    unblock_user_for_voting(admin_unique_id)

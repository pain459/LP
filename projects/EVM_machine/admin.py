import pandas as pd
import os
import requests
import time
from threading import Thread, Lock
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Suppress Flask logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Load the user list from CSV
user_list_df = pd.read_csv('user_list.csv')

# Create a blank CSV to store voting information if it doesn't already exist
voting_csv = 'voting_data.csv'
if not os.path.exists(voting_csv):
    voting_df = pd.DataFrame(columns=["UniqueID", "Voted", "VotedToSymbol"])
    voting_df.to_csv(voting_csv, index=False)
else:
    voting_df = pd.read_csv(voting_csv)

# Track registered user consoles
user_consoles = []
current_console_index = 0
vote_in_progress = False
lock = Lock()

# Function to validate polling center ID
def validate_center_id(center_id):
    while True:
        try:
            response = requests.get(f'http://localhost:5000/validate_center_id?center_id={center_id}')
            if response.status_code == 200 and response.json().get('status') == 'success':
                return True
            elif response.status_code == 400:
                print(response.json().get('message'))
                return False
        except requests.exceptions.RequestException as e:
            print(f"Failed to validate center ID: {e}. Retrying in 5 seconds...")
            time.sleep(5)

# Function to send heartbeat updates
def send_heartbeat(center_id):
    while True:
        try:
            response = requests.post('http://localhost:5000/heartbeat', json={"center_id": center_id})
            if response.status_code != 200:
                print("Failed to send heartbeat update.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send heartbeat: {e}. Retrying in 30 seconds...")
        time.sleep(30)  # Send heartbeat every 30 seconds

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
    global current_console_index, vote_in_progress
    if not validate_unique_id(unique_id):
        return False, "Invalid unique ID."
    if has_already_voted(unique_id):
        return False, "User has already voted."
    with lock:
        if vote_in_progress:
            return False, "All consoles are currently busy."
        vote_in_progress = True

    if user_consoles:
        user_console = user_consoles[current_console_index]
        current_console_index = (current_console_index + 1) % len(user_consoles)
        with open(f'unblock_{user_console["name"]}.txt', 'w') as f:
            f.write(unique_id)
        return True, f"User unblocked for console {user_console['name']}."
    return False, "No user consoles available."

# Function to mark the completion of a vote
@app.route('/vote_completed', methods=['POST'])
def vote_completed():
    global vote_in_progress
    with lock:
        vote_in_progress = False
    return jsonify({"status": "success"}), 200

# Function to check if client is up
def is_client_up(user_console):
    try:
        response = requests.get(f'http://localhost:{user_console["port"]}/client_status')
        if response.status_code == 200 and response.json().get('status') == 'up':
            return True
    except requests.exceptions.RequestException as e:
        print(f"Client {user_console['name']} is not up: {e}.")
    return False

# Route to validate and unblock user
@app.route('/unblock', methods=['POST'])
def unblock():
    data = request.json
    unique_id = data.get('unique_id')
    if not unique_id:
        return jsonify({"status": "error", "message": "Unique ID is required"}), 400
    success, result = unblock_user_for_voting(unique_id)
    if success:
        return jsonify({"status": "success", "message": result}), 200
    return jsonify({"status": "error", "message": result}), 400

# Function to add a new user console
def add_user_console():
    while True:
        user_console_id = input("Admin: Enter the user console identity to register (or 'done' to finish): ").strip()
        if user_console_id.lower() == 'done':
            break
        if any(console['name'] == user_console_id for console in user_consoles):
            print(f"User console {user_console_id} is already registered.")
            continue
        port = input(f"Enter the port for {user_console_id}: ").strip()
        user_console = {"name": user_console_id, "port": port}
        if is_client_up(user_console):
            user_consoles.append(user_console)
            print(f"User console {user_console_id} registered on port {port}.")
        else:
            print(f"User console {user_console_id} is not up on port {port}.")

# Function to list registered user consoles
def list_user_consoles():
    if not user_consoles:
        print("No user consoles registered.")
    else:
        print("Registered user consoles:")
        for console in user_consoles:
            print(f"Name: {console['name']}, Port: {console['port']}")

# Function to flush all allocated unique IDs
def flush_allocations():
    global vote_in_progress
    with lock:
        for console in user_consoles:
            unblock_file = f'unblock_{console["name"]}.txt'
            if os.path.exists(unblock_file):
                os.remove(unblock_file)
        vote_in_progress = False
    print("All allocations have been flushed.")

# Main admin loop
def main():
    while True:
        admin_center_id = input("Admin: Enter the polling center ID to validate: ").strip()
        if validate_center_id(admin_center_id):
            print("Polling center ID is valid. Starting to serve requests locally...")
            
            # Start the heartbeat thread
            heartbeat_thread = Thread(target=send_heartbeat, args=(admin_center_id,))
            heartbeat_thread.daemon = True
            heartbeat_thread.start()

            # Register initial user consoles
            add_user_console()

            if not user_consoles:
                print("No user consoles registered. Exiting...")
                return

            while True:
                print("\nAdmin Menu:")
                print("1. Add new console")
                print("2. Enter the unique ID to unblock for voting")
                print("3. List registered consoles")
                print("4. Flush allocations")
                print("5. Exit")
                choice = input("Select an option: ").strip()

                if choice == '1':
                    add_user_console()
                elif choice == '2':
                    admin_unique_id = input("Admin: Enter the unique ID to unblock for voting: ").strip()
                    success, result = unblock_user_for_voting(admin_unique_id)
                    if success:
                        print(f"{result}")
                    else:
                        print(result)
                elif choice == '3':
                    list_user_consoles()
                elif choice == '4':
                    flush_allocations()
                elif choice == '5':
                    print("Exiting...")
                    return
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid polling center ID. Please try again.")

if __name__ == '__main__':
    flask_thread = Thread(target=lambda: app.run(host='0.0.0.0', port=5002))
    flask_thread.daemon = True
    flask_thread.start()
    main()

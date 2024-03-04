import datetime
import subprocess
import logging

# Configure logging
logging.basicConfig(filename='execution_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def execute_command(start_date):
    # Calculate the end date which is 180 days less than the start date
    end_date = start_date - datetime.timedelta(days=180)

    # Example command to execute - Replace this with your actual command
    command = f"echo 'From Date: {start_date.strftime('%Y-%m-%d')}, To Date: {end_date.strftime('%Y-%m-%d')}'"

    # Execute the command
    subprocess.run(command, shell=True)

    # Log the executed command with timestamp
    logging.info(f"Command executed: {command}")


# Get current date
current_date = datetime.date.today()

while True:
    # Get input date from user
    input_date_str = input("Enter a date (YYYY-MM-DD format) or 'quit' to exit: ")

    # Check if user wants to quit
    if input_date_str.lower() == 'quit':
        print("Exiting the script.")
        break

    try:
        # Convert input string to date object
        input_date = datetime.datetime.strptime(input_date_str, "%Y-%m-%d").date()

        # Execute command from input date to current date
        while input_date < current_date:
            execute_command(input_date)
            input_date += datetime.timedelta(days=1)

        print("All commands executed.")
        break

    except ValueError:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")

import pandas as pd
import requests

# Function to post DataFrame to Slack as a table
def post_df_to_slack(webhook_url, dataframe):
    # Convert DataFrame to Markdown table
    table = dataframe.to_markdown(index=False)

    # Format the message with Markdown code block
    message = f"```\n{table}\n```"

    # Prepare payload for Slack
    payload = {'text': message}

    # Post message to Slack
    response = requests.post(webhook_url, json=payload)

    # Check if message was posted successfully
    if response.status_code == 200:
        print("DataFrame posted successfully to Slack!")
    else:
        print(f"Failed to post DataFrame to Slack. Error: {response.text}")


def main():
    # JSON-like data (dictionary)
    json_data = {
        "id": [101, 102, 103, 104],
        "name": ["John", "Alice", "Bob", "Emily"],
        "age": [30, 25, 35, 28],
        "city": ["New York", "Los Angeles", "Chicago", "Houston"],
        "gender": ["Male", "Female", "Male", "Female"]
    }

    # Create DataFrame from JSON data
    df = pd.DataFrame.from_dict(json_data)

    webhook_url = 'YOUR_WEBHOOK_URL'
    # webhook_url = 'https://hooks.slack.com/services/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'

    # Post DataFrame to Slack
    post_df_to_slack(webhook_url, df[['id', 'name', 'age', 'city', 'gender']])


if __name__ == "__main__":
    main()

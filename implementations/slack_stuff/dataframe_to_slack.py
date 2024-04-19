import requests
import pandas as pd

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

# Assuming df is your DataFrame with columns 'id', 'title', and 'category'
# You can replace it with your actual DataFrame
df = pd.DataFrame({
    'id': [1, 2, 3],
    'title': ['Product A', 'Product B', 'Product C'],
    'category': ['Category X', 'Category Y', 'Category Z']
})

# Replace 'YOUR_WEBHOOK_URL' with your actual webhook URL obtained from Slack
webhook_url = 'YOUR_WEBHOOK_URL'

# Post DataFrame to Slack
post_df_to_slack(webhook_url, df[['id', 'title', 'category']])

import requests
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/albums'
webhook_url = 'https://hooks.slack.com/services/XXXXX'

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

response = requests.get(url)

if response.status_code == 200:
    # parse json data
    json_data = response.json()

    # Convert JSON data to dataframe
    df = pd.DataFrame.from_dict(json_data)
    # print(df.head())
    post_df_to_slack(webhook_url, df[['id', 'title']])

else:
    print(f'Error!!!')
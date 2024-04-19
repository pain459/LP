import requests
import json

def post_to_slack(webhook_url, data_dict):
    # Convert dictionary to Markdown table format
    table = "\n".join([f"| {key} | {', '.join(str(val) for val in value)} |" for key, value in data_dict.items()])
    message = f"```\n{table}\n```"  # Enclose the table in triple backticks for code block in Slack
    payload = {'text': message}
    response = requests.post(webhook_url, data=json.dumps(payload))
    if response.status_code == 200:
        print("Message posted successfully to Slack!")
    else:
        print(f"Failed to post message to Slack. Error: {response.text}")

if __name__ == "__main__":
    # Replace 'YOUR_WEBHOOK_URL' with the actual webhook URL obtained from Slack
    webhook_url = 'YOUR_WEBHOOK_URL'
    data_dict = {'Fruits': ['apple', 'orange', 'pine']}
    post_to_slack(webhook_url, data_dict)

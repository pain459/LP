import requests
import json

def post_to_slack(webhook_url, message):
    payload = {'text': message}
    response = requests.post(webhook_url, data=json.dumps(payload))
    if response.status_code == 200:
        print("Message posted successfully to Slack!")
    else:
        print(f"Failed to post message to Slack. Error: {response.text}")

if __name__ == "__main__":
    # Replace 'YOUR_WEBHOOK_URL' with the actual webhook URL obtained from Slack
    webhook_url = 'YOUR_WEBHOOK_URL'
    # message = "This is firstline.\nThis is second line."
    # message = "This is not blocked text\n>This is blocked\nTHis is not blocked\n>This is blocked."
    message = ":rotating_light:"
    post_to_slack(webhook_url, message)

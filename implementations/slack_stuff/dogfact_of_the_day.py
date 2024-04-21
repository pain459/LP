import requests
import random
from datetime import date


dog_facts_api = 'https://dog-api.kinduff.com/api/facts?number=100'
webhook_url = "https://hooks.slack.com/services/XXXXXX"

def get_facts(url):
    response = requests.get(url)

    if response.status_code == 200:
        # print('Facts fetched!')
        return response
    else:
        return f'Error!!! {response.status_code}'

def parse_facts(result):
    response_json = result.json()
    return response_json

def select_random_fact(facts_data):
    a = random.choice(list(facts_data))
    return a

def post_to_slack(data, webhook_url):
    today = date.today()
    d1 = today.strftime("%B %d, %Y")
    message = f"Random dog fact for {d1} \n```{data}```"
    payload = {'text': message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print('Successfully posted to slack.')
    else:
        print(f'Error occurrec!!! {response.status_code}')


def main():
    facts = get_facts(url=dog_facts_api)
    results = parse_facts(facts)
    random_fact = select_random_fact(results['facts'])
    post_to_slack(data=random_fact, webhook_url=webhook_url)



if __name__ == "__main__":
    main()
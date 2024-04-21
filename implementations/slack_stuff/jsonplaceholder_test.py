import requests
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/albums'
response = requests.get(url)

if response.status_code == 200:
    # parse json data
    json_data = response.json()

    # Convert JSON data to dataframe
    df = pd.DataFrame.from_dict(json_data)
    print(df.head())

else:
    print(f'Failed to reetrive response {response.status_code}')
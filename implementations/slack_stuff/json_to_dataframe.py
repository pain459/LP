import requests
import pandas as pd

# Fetch JSON data from the API
url = 'https://dummyjson.com/products/1'
response = requests.get(url)

if response.status_code == 200:
    # Parse JSON data
    json_data = response.json()

    # Convert JSON data to DataFrame
    df = pd.DataFrame.from_dict(json_data, orient='index').transpose()
    print("DataFrame:")
    print(df)
else:
    print(f"Failed to fetch JSON data. Status code: {response.status_code}")


print(df[['id', 'title', 'category']])
import requests

url = 'https://jsonplaceholder.typicode.com/albums'
r = requests.get(url)

# print(r.status_code)

if r.status_code == 200:
    print('response received.')
else:
    print('error')

# print(r.json())
import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/pain459"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})

print(profile_picture)
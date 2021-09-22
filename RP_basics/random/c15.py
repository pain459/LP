# interacting with the web.
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")
print(html_text)

# Using beautiful soup to scrape HTML data.

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())

# Interacting with HTML forms
import mechanicalsoup
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)

print(page.soup)

# automating data fill with mechanicalsoup

import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)

profiles_page.url
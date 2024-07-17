import requests
from bs4 import BeautifulSoup
import re
import time
import csv

class SimpleWebCrawler:
    def __init__(self, base_url, max_pages=10, output_file="crawled_data.csv"):
        self.base_url = base_url
        self.max_pages = max_pages
        self.visited_urls = set()
        self.to_visit_urls = [base_url]
        self.output_file = output_file

    def fetch_content(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_links(self, content, base_url):
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all('a', href=True)
        full_links = [self.full_url(base_url, link['href']) for link in links]
        return full_links

    def full_url(self, base_url, link):
        if link.startswith("http"):
            return link
        else:
            return re.match(r'^(https?://)?(www\.)?([A-Za-z_0-9.-]+)+([/?].*)?$', base_url).group() + link

    def crawl(self):
        with open(self.output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Title"])
            
            while self.to_visit_urls and len(self.visited_urls) < self.max_pages:
                current_url = self.to_visit_urls.pop(0)
                if current_url in self.visited_urls:
                    continue
                print(f"Visiting: {current_url}")
                content = self.fetch_content(current_url)
                if content:
                    self.visited_urls.add(current_url)
                    title = self.extract_title(content)
                    writer.writerow([current_url, title])
                    links = self.parse_links(content, self.base_url)
                    for link in links:
                        if link not in self.visited_urls and link not in self.to_visit_urls:
                            self.to_visit_urls.append(link)
                time.sleep(1)  # Be polite, avoid hitting the server too hard

    def extract_title(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        return soup.title.string if soup.title else 'No Title'

if __name__ == "__main__":
    crawler = SimpleWebCrawler(base_url="https://en.wikipedia.org/wiki/Telugu_language", max_pages=50)
    crawler.crawl()

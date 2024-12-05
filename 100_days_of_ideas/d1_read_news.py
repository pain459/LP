import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import argparse

# Load the .env file
load_dotenv()

# Fetch the API key from the .env file
api_key = os.getenv('NEWS_API_KEY')

if not api_key:
    print("Error: NEWS_API_KEY is missing in the .env file.")
    exit(1)

# Initialize the NewsApiClient
newsapi = NewsApiClient(api_key=api_key)

# List of valid ISO 3166-1 alpha-2 country codes
VALID_COUNTRIES = ['ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 
                   'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 
                   'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 
                   'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 
                   'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 
                   'ua', 'us', 've', 'za']

# Function to fetch and display news articles
def fetch_news(country, topic, top_n):
    try:
        # Fetch top headlines
        if topic:
            response = newsapi.get_top_headlines(q=topic, country=country, language='en')
        else:
            response = newsapi.get_top_headlines(country=country, language='en')

        articles = response.get('articles', [])

        if not articles:
            print(f"No news articles found for {'topic: ' + topic if topic else 'country: ' + country}.")
            return

        # Limit articles to top_n if specified
        articles = articles[:top_n]

        print(f"\nTop {len(articles)} news articles for {'topic: ' + topic if topic else 'country: ' + country.upper()}:\n")
        for i, article in enumerate(articles, start=1):
            print(f"Article {i}:")
            print(f"Title: {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"Published At: {article['publishedAt']}")
            print(f"URL: {article['url']}\n")
    except Exception as e:
        print(f"Error fetching news: {e}")

# Main function
if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Fetch the latest news by country and topic.")
    parser.add_argument('country', type=str, help="Two-letter country code (e.g., 'in' for India, 'us' for USA)")
    parser.add_argument('--top', type=int, default=10, help="Number of top articles to display (default: 10)")
    args = parser.parse_args()

    # Validate country code
    if args.country.lower() not in VALID_COUNTRIES:
        print("Invalid country code. Please use a valid ISO 3166-1 alpha-2 country code.")
        exit(1)

    # Prompt user for the topic
    topic = input("Enter the topic you want to search for (leave blank to fetch all news for the country): ").strip()

    # Fetch and display news
    fetch_news(args.country.lower(), topic, args.top)


# sample
# python news_fetcher.py in --top 3
# Enter the topic you want to search for (leave blank to fetch all news for the country): technology

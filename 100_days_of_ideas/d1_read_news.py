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

# Function to fetch the latest news articles
def get_latest_news_by_country_and_topic(country, topic):
    try:
        # Fetch top headlines for the given country and topic
        top_headlines = newsapi.get_top_headlines(q=topic, country=country.lower(), language='en')

        # Check if articles are found
        if top_headlines['articles']:
            print(f"Top news for '{topic}' in {country.capitalize()}:\n")
            for article in top_headlines['articles']:
                print(f"Title: {article['title']}")
                print(f"Source: {article['source']['name']}")
                print(f"Published At: {article['publishedAt']}")
                print(f"URL: {article['url']}\n")
        else:
            print(f"No news articles found for topic '{topic}' in {country.capitalize()}.")
    except Exception as e:
        print(f"Error fetching news: {e}")

# Main function
if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Fetch the latest news by country and topic.")
    parser.add_argument('country', type=str, help="Two-letter country code (e.g., 'in' for India, 'us' for USA)")
    args = parser.parse_args()

    # Prompt user for the topic
    topic = input("Enter the topic you want to search for: ")

    # Fetch and display news
    get_latest_news_by_country_and_topic(args.country, topic)


# Test run
# python script.py in
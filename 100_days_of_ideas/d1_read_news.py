import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

# Load the .env file
load_dotenv()

# Fetch the API key from the .env file
api_key = os.getenv('NEWS_API_KEY')

# Initialize the NewsApiClient
if not api_key:
    print("Error: NEWS_API_KEY is missing in the .env file.")
else:
    newsapi = NewsApiClient(api_key=api_key)

    # Function to fetch the latest news articles about a given topic
    def get_latest_news(topic):
        try:
            # Fetch top headlines related to the topic
            top_headlines = newsapi.get_top_headlines(q=topic, language='en')

            # Check if articles are found
            if top_headlines['articles']:
                for article in top_headlines['articles']:
                    print(f"Title: {article['title']}")
                    print(f"Source: {article['source']['name']}")
                    print(f"Published At: {article['publishedAt']}")
                    print(f"URL: {article['url']}\n")
            else:
                print(f"No news articles found for the topic: {topic}")
        except Exception as e:
            print(f"Error fetching news: {e}")

    # Example usage
    if __name__ == "__main__":
        topic = input("Enter the topic you want to search for: ")
        get_latest_news(topic)

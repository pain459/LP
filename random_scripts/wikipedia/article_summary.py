import wikipediaapi
from transformers import pipeline

def get_wikipedia_summary(article_title):
    # Initialize Wikipedia API
    wiki_wiki = wikipediaapi.Wikipedia('en')
    
    # Set the user agent
    wiki_wiki.requests_wrapper.session.headers.update({
        'User-Agent': 'MyApp/1.0 (pain@gmail.com)'
    })
    
    page = wiki_wiki.page(article_title)
    
    # Check if the page exists
    if not page.exists():
        return "Article not found."

    # Fetch the article content
    content = page.text

    # Initialize the summarization pipeline
    summarizer = pipeline("summarization")

    # Summarize the content
    summary = summarizer(content, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    article_title = input("Enter the Wikipedia article title: ")
    summary = get_wikipedia_summary(article_title)
    print("\nSummary:\n", summary)

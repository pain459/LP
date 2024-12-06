import argparse
import sys
import spacy
import requests
from transformers import pipeline
from bs4 import BeautifulSoup

"""
Librarires:

pip install spacy requests beautifulsoup4 transformers
python -m spacy download en_core_web_sm

"""

def fetch_external_content(url):
    # Fetch HTML content from the external URL
    response = requests.get(url)
    response.raise_for_status()
    html_content = response.text

    # Parse HTML and extract main content
    soup = BeautifulSoup(html_content, 'html.parser')

    # For Wikipedia pages, main content is usually in <div id="mw-content-text">
    content_div = soup.find('div', id='mw-content-text')
    if content_div:
        content = content_div.get_text(separator=' ')
    else:
        # If not found, fall back to entire page text
        content = soup.get_text(separator=' ')
    return content

def load_and_summarize(content, chunk_size=3000):
    # Load SpaCy model
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(content)
    sentences = [sent.text for sent in doc.sents]

    # Join all sentences into one big text
    full_text = " ".join(sentences)

    # Load summarization pipeline (using a transformer model)
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Chunk the text if it's too large
    # Transformers typically handle ~1024 tokens; you might find a suitable chunk_size by trial
    chunks = []
    start = 0
    while start < len(full_text):
        end = start + chunk_size
        # ensure we split at a space if possible
        if end < len(full_text):
            end = full_text.rfind(' ', start, end)  # find space before chunk_size
            if end == -1:
                end = start + chunk_size
        chunks.append(full_text[start:end])
        start = end

    # Summarize each chunk individually
    chunk_summaries = []
    for c in chunks:
        # Make sure that c is not empty or too short
        if c.strip():
            # Adjust max_length and min_length depending on desired summary size
            summary_chunk = summarizer(c, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
            chunk_summaries.append(summary_chunk)

    # Combine the summaries of each chunk into a final summary
    combined_text = " ".join(chunk_summaries)

    # Optionally run summarizer again on the combined summary if it's still long
    if len(combined_text) > chunk_size:
        final_summary = summarizer(combined_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    else:
        final_summary = combined_text

    return final_summary


def main():
    parser = argparse.ArgumentParser(description="Summarize text from a local file or an external URL.")
    parser.add_argument('--local', type=str, help='Path to the local text file')
    parser.add_argument('--external', type=str, help='URL of the external webpage (e.g., Wikipedia link)')

    args = parser.parse_args()

    # Validate input source
    if args.local and args.external:
        print("Error: Please provide only one source (either --local or --external).", file=sys.stderr)
        sys.exit(1)
    elif not args.local and not args.external:
        print("Error: Please provide a source with --local or --external.", file=sys.stderr)
        sys.exit(1)

    # Read content from the specified source
    if args.local:
        with open(args.local, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        # Fetch from external URL
        content = fetch_external_content(args.external)

    # Summarize the content
    summary = load_and_summarize(content)

    # Print the summary
    print("Summary:")
    print(summary)

if __name__ == "__main__":
    main()

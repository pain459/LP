import spacy
from transformers import pipeline

# Load a SpaCy model (e.g., English Core Web)
nlp = spacy.load("en_core_web_sm")

# Read your input file
with open("input.txt", "r") as f:
    text = f.read()

# Process the text with SpaCy
doc = nlp(text)

# Extract sentences for summarization
sentences = [sent.text for sent in doc.sents]

# Load a summarization pipeline (using a transformer model)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Summarize (note: you may need to handle long text in chunks)
summary = summarizer(" ".join(sentences), max_length=150, min_length=50, do_sample=False)[0]['summary_text']

print("Summary:")
print(summary)

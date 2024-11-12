# Loading the summarization model
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

import re

def preprocess_subtitles(file_path):
    """
    Clean up and prepare subtitle text by removing timestamps, line numbers, and non-dialogue cues.
    
    Parameters:
    - file_path (str): Path to the subtitle (.srt) file.

    Returns:
    - str: Cleaned subtitle text.
    """
    # Read the subtitle file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove BOM (Byte Order Mark) if present at the start of the file
    content = content.lstrip("\ufeff")
    
    # Remove timestamps (format: 00:00:35,202 --> 00:00:37,538)
    content = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', content)
    
    # Remove line numbers (appear as standalone numbers in the text)
    content = re.sub(r'\n\d+\n', '\n', content)
    
    # Remove non-dialogue cues such as (MUSIC PLAYING) or <i>italic text</i>
    content = re.sub(r'\(.*?\)', '', content)  # Remove text within parentheses
    content = re.sub(r'<.*?>', '', content)    # Remove HTML-like tags within <>

    # Replace multiple newlines with a single space for better readability
    content = re.sub(r'\n+', ' ', content)
    content = content.strip()  # Remove any leading or trailing whitespace
    
    return content


def chunk_text(text, max_length=500):
    """
    Split cleaned text into manageable chunks for summarization.
    
    Parameters:
    - text (str): The cleaned subtitle text.
    - max_length (int): Maximum number of words per chunk.

    Returns:
    - list: List of text chunks.
    """
    words = text.split()
    chunks = []
    
    # Create chunks of specified max length
    for i in range(0, len(words), max_length):
        chunk = " ".join(words[i:i + max_length])
        chunks.append(chunk)
    
    return chunks


def load_summarizer():
    """
    Load the Hugging Face summarization pipeline using the BART model.

    Returns:
    - Pipeline: Hugging Face summarization pipeline.
    """
    return pipeline("summarization", model="facebook/bart-large-cnn")


def summarize_chunks(chunks, summarizer):
    """
    Summarize each chunk individually and combine results.
    
    Parameters:
    - chunks (list): List of text chunks.
    - summarizer (Pipeline): Loaded summarization pipeline.

    Returns:
    - str: Combined summary of all chunks.
    """
    chunk_summaries = []
    for chunk in chunks:
        # Summarize each chunk and append to results list
        summary = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
        chunk_summaries.append(summary[0]['summary_text'])
    
    # Combine all chunk summaries into one large text
    return " ".join(chunk_summaries)


def final_summary(text, summarizer, section_length=400, max_input_length=1024):
    """
    Create a final summary by breaking down the combined summary into smaller sections if necessary.
    
    Parameters:
    - text (str): Combined summary text from all chunks.
    - summarizer (Pipeline): Loaded summarization pipeline.
    - section_length (int): Word length of each section for further summarization.
    - max_input_length (int): Maximum length of input text tokens for the final summary.

    Returns:
    - str: Final summarized text.
    """
    # Split combined text into smaller sections
    words = text.split()
    sections = []
    for i in range(0, len(words), section_length):
        section = " ".join(words[i:i + section_length])
        sections.append(section)
    
    # Summarize each section separately
    section_summaries = []
    for section in sections:
        summary = summarizer(section, max_length=120, min_length=40, do_sample=False)
        section_summaries.append(summary[0]['summary_text'])
    
    # Combine section summaries into a single text
    combined_summary = " ".join(section_summaries)
    
    # If still large, truncate to max_input_length for one final summarization pass
    if len(combined_summary.split()) > max_input_length:
        combined_summary = " ".join(combined_summary.split()[:max_input_length])
    
    # Summarize the combined text to get the final movie summary
    final_summary = summarizer(combined_summary, max_length=150, min_length=50, do_sample=False)
    return final_summary[0]['summary_text']


def generate_movie_summary(file_path):
    """
    Generate a movie summary from subtitles by processing and summarizing in stages.
    
    Parameters:
    - file_path (str): Path to the subtitle file.

    Returns:
    - str: Final summarized text representing the movie plot.
    """
    # Step 1: Preprocess the subtitle file to clean the text
    cleaned_text = preprocess_subtitles(file_path)
    
    # Step 2: Split cleaned text into manageable chunks
    chunks = chunk_text(cleaned_text, max_length=500)
    
    # Step 3: Load the summarization model
    summarizer = load_summarizer()
    
    # Step 4: Summarize each chunk and combine the summaries
    combined_summary = summarize_chunks(chunks, summarizer)
    print("Combined summary length (in words):", len(combined_summary.split()))  # Debugging line
    
    # Step 5: Generate a final summary from the combined chunk summaries
    movie_summary = final_summary(combined_summary, summarizer)
    return movie_summary


# file_path = 'D:\\src_git\\LP\\LP\\projects\\video_subtitle_summary\\subtitle_summary\\avatar_twow.srt'
file_path = 'D:\\src_git\\LP\\LP\\projects\\video_subtitle_summary\\subtitle_summary\\John.Wick.1.srt'


summary = generate_movie_summary(file_path)
print("Movie Summary:\n", summary)
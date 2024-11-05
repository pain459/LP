import os
import re
from transformers import pipeline
from concurrent.futures import ThreadPoolExecutor

input_dir = '/app/input'
output_dir = '/app/output'

def clean_subtitles(text):
    """ Remove timestamps and empty lines from the subtitle text. """
    # Remove timestamps using regex
    cleaned_text = re.sub(r"\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", "", text)
    # Remove extra whitespace and newlines
    cleaned_text = re.sub(r"\n\s*\n", "\n", cleaned_text).strip()
    return cleaned_text

def summarize_subtitles(subtitle_file):
    # Load the summarization pipeline with GPU support
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0)
    
    # Read the subtitle file and clean text
    subtitle_path = os.path.join(input_dir, subtitle_file)
    with open(subtitle_path, 'r') as f:
        raw_text = f.read()
    dialogue = clean_subtitles(raw_text)
    
    # Generate summary
    summary_text = summarizer(dialogue, max_length=100, min_length=50, do_sample=False)[0]['summary_text']
    
    # Save summary to output file
    summary_file = os.path.join(output_dir, os.path.splitext(subtitle_file)[0] + "_summary.txt")
    with open(summary_file, 'w') as f:
        f.write(summary_text)
    
    print(f"Generated summary for {subtitle_file}")

def main():
    with ThreadPoolExecutor() as executor:
        for file in os.listdir(input_dir):
            if file.endswith(".srt"):
                executor.submit(summarize_subtitles, file)

if __name__ == "__main__":
    main()

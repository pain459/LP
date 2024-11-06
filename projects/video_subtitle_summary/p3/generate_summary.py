import os
import re
import torch
from transformers import pipeline, BartTokenizer, BartForConditionalGeneration

input_dir = '/app/input'
output_dir = '/app/output'

os.environ["CUDA_LAUNCH_BLOCKING"] = "1"  # Ensure errors are reported accurately
os.environ["TORCH_USE_CUDA_DSA"] = "1"    # Enable device-side assertions

def clean_subtitles(text):
    """Remove timestamps and empty lines from the subtitle text."""
    cleaned_text = re.sub(r"\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", "", text)
    cleaned_text = re.sub(r"\n\s*\n", "\n", cleaned_text).strip()
    return cleaned_text

def validate_input(dialogue, tokenizer):
    """Tokenize input and filter out invalid sequences."""
    tokens = tokenizer(dialogue, return_tensors="pt", truncation=True, max_length=1024)
    if tokens["input_ids"].size(1) == 0:
        print("Warning: Empty input after tokenization.")
        return None
    return tokens

def summarize_subtitles(subtitle_file):
    # Initialize tokenizer and model
    device = 0 if torch.cuda.is_available() else -1
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name).to(device)
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=device)
    
    # Read and clean the subtitle file
    subtitle_path = os.path.join(input_dir, subtitle_file)
    with open(subtitle_path, 'r') as f:
        raw_text = f.read()
    dialogue = clean_subtitles(raw_text)

    # Validate tokenized input
    tokens = validate_input(dialogue, tokenizer)
    if tokens is None:
        print(f"Skipping invalid subtitle file: {subtitle_file}")
        return

    # Generate summary
    summary_text = summarizer(dialogue, max_length=100, min_length=80, do_sample=False)[0]['summary_text']
    
    # Save the summary
    summary_file = os.path.join(output_dir, os.path.splitext(subtitle_file)[0] + "_summary.txt")
    with open(summary_file, 'w') as f:
        f.write(summary_text)
    
    print(f"Generated summary for {subtitle_file}")

def main():
    for file in os.listdir(input_dir):
        if file.endswith(".srt"):
            summarize_subtitles(file)

if __name__ == "__main__":
    main()

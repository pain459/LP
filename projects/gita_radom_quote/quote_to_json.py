import json
import re

def extract_quotes(file_path):
    gita_quotes = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    pattern = re.compile(r'Bg\.\s*(\d+)\.(\d+)\s+.*?Translation\s+(.*?)(?=\n*Purport)', re.DOTALL)
    matches = pattern.findall(text)

    for match in matches:
        chapter = match[0]
        verse = match[1]
        translation = match[2].strip().replace('\n', ' ')  # Clean up the translation text

        if chapter not in gita_quotes:
            gita_quotes[chapter] = {}
        gita_quotes[chapter][verse] = translation

    return gita_quotes

def save_quotes_to_json(gita_quotes, output_file_path):
    # Convert dictionary to JSON and write to file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(gita_quotes, file, ensure_ascii=False, indent=4)  # Pretty print the JSON

# File paths
input_file_path = '/home/ravik/src_git/LP/projects/gita_radom_quote/extracted_text.txt'
output_file_path = 'gita_quotes.json'

# Extract quotes and store them in JSON format
gita_quotes_json = extract_quotes(input_file_path)

# Save the JSON data to a file
save_quotes_to_json(gita_quotes_json, output_file_path)

print(f"JSON data has been saved to {output_file_path}.")

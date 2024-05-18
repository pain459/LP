import pandas as pd
import random

# Function to load the Bhagavad Gita verses from an Excel file
def load_gita_verses(filepath):
    # Load the data using pandas, focusing on the relevant columns
    data = pd.read_excel(filepath, usecols=['Chapter', 'Verse', 'Title', 'Enlgish Translation'])
    # Filter out rows where the 'Enlgish Translation' column is empty, assuming this column contains Krishna's speeches
    filtered_data = data[data['Enlgish Translation'].notna()]
    return filtered_data

# Function to get a random verse from the data
def get_random_verse(data):
    # Randomly pick a row from the filtered DataFrame
    random_row = data.sample(n=1).iloc[0]
    chapter = random_row['Chapter']
    verse = random_row['Verse']
    title = random_row['Title']
    text = random_row['Enlgish Translation']
    return chapter, verse, title, text

# Example usage of the functions
if __name__ == "__main__":
    # Specify the path to your Excel file
    filepath = '/home/ravik/src_git/LP/projects/gita_radom_quote/gita.xlsx'
    
    # Load the Bhagavad Gita verses
    gita_data = load_gita_verses(filepath)
    
    # Get a random verse spoken by Krishna
    random_chapter, random_verse, chapter_title, krishna_speech = get_random_verse(gita_data)
    
    # Print the output
    print(f"Chapter: {random_chapter}, Verse: {random_verse}, Title: {chapter_title}")
    print(f"Krishna's Speech: {krishna_speech}")

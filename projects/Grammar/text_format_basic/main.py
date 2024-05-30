import nltk
import spacy
from textblob import TextBlob
import textstat
import language_tool_python

# Load Spacy model
nlp = spacy.load('en_core_web_sm')
tool = language_tool_python.LanguageTool('en-US')

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def correct_indentation(line):
    # Implement indentation correction logic
    return line

def check_grammar(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.correct(text, matches)
    return corrected_text, len(matches)

def suggest_alternatives(text):
    doc = nlp(text)
    suggestions = {}
    for token in doc:
        if token.pos_ in ['NOUN', 'VERB', 'ADJ', 'ADV']:
            synonyms = get_synonyms(token.text)
            if synonyms:
                suggestions[token.text] = synonyms
    return suggestions

def get_synonyms(word):
    synonyms = set()
    for syn in nltk.corpus.wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def evaluate_text(text):
    readability = textstat.flesch_reading_ease(text)
    delivery = textstat.gunning_fog(text)
    clarity = textstat.coleman_liau_index(text)
    return readability, delivery, clarity

def process_file(input_path, output_path):
    lines = read_file(input_path)
    corrected_lines = []
    total_grammar_issues = 0

    for line in lines:
        corrected_line = correct_indentation(line)
        corrected_text, grammar_issues = check_grammar(corrected_line)
        total_grammar_issues += grammar_issues
        corrected_lines.append(corrected_text)

    write_file(output_path, corrected_lines)
    
    full_text = ' '.join(corrected_lines)
    readability, delivery, clarity = evaluate_text(full_text)
    
    suggestions = suggest_alternatives(full_text)

    return total_grammar_issues, readability, delivery, clarity, suggestions

if __name__ == "__main__":
    input_file = '/home/ravik/src_git/LP/projects/Grammar/text_format_basic/sample.txt'
    output_file = '/home/ravik/src_git/LP/projects/Grammar/text_format_basic/output.txt'
    total_grammar_issues, readability, delivery, clarity, suggestions = process_file(input_file, output_file)
    
    print(f"Total Grammar Issues: {total_grammar_issues}")
    print(f"Readability Score: {readability}")
    print(f"Delivery Score: {delivery}")
    print(f"Clarity Score: {clarity}")
    print("Suggestions for Improvement:")
    for word, synonyms in suggestions.items():
        print(f"{word}: {', '.join(synonyms)}")

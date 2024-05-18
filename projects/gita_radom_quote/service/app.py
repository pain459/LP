from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

# Load the quotes from the JSON file
with open('/home/ravik/src_git/LP/projects/gita_radom_quote/service/gita_quotes.json', 'r', encoding='utf-8') as file:
    quotes = json.load(file)

# # Remove quotes from chapters 1, 2, and 7
# quotes.pop('1', None)
# quotes.pop('2', None)
# quotes.pop('7', None)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-quote')
def random_quote():
    # Select a random chapter
    chapter = random.choice(list(quotes.keys()))
    # Select a random verse from the selected chapter
    verse = random.choice(list(quotes[chapter].keys()))
    # Return the quote
    quote = quotes[chapter][verse]
    return jsonify(chapter=chapter, verse=verse, quote=quote)

if __name__ == '__main__':
    app.run(debug=True)

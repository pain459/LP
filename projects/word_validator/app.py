from flask import Flask, render_template, request
from main import load_wordnet, validate_word

app = Flask(__name__)
wordnet_dict = load_wordnet()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    word = request.form['word']
    is_valid, word_info = validate_word(word, wordnet_dict)
    if is_valid:
        description, classification = word_info
        result = f"The word '{word}' is valid! Description: {description}, Classification: {classification}"
    else:
        result = f"Sorry, '{word}' is not a valid word."
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

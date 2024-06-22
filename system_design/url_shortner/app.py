from flask import Flask, request, render_template, redirect, url_for
from tinydb import TinyDB, Query
import string
import random
import os

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'url_mappings.json')
db = TinyDB(db_path)

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    short_code = generate_short_code()
    db.insert({'original_url': original_url, 'short_code': short_code})
    short_url = request.host_url + short_code
    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    Url = Query()
    result = db.search(Url.short_code == short_code)
    if result:
        return redirect(result[0]['original_url'])
    return 'URL not found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

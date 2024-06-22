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
    urls = db.all()
    return render_template('index.html', urls=urls)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    custom_shortname = request.form['shortname']
    Url = Query()

    if custom_shortname:
        short_code = custom_shortname
        if db.search(Url.short_code == short_code):
            return render_template('index.html', error="Custom short name already exists!", urls=db.all())
    else:
        result = db.search(Url.original_url == original_url)
        if result:
            short_code = result[0]['short_code']
        else:
            short_code = generate_short_code()
            while db.search(Url.short_code == short_code):
                short_code = generate_short_code()

    if not db.search(Url.original_url == original_url):
        db.insert({'original_url': original_url, 'short_code': short_code, 'hits': 0})

    short_url = request.host_url + short_code
    return render_template('index.html', short_url=short_url, urls=db.all())

@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    Url = Query()
    result = db.search(Url.short_code == short_code)
    if result:
        db.update({'hits': result[0]['hits'] + 1}, Url.short_code == short_code)
        return redirect(result[0]['original_url'])
    return 'URL not found', 404

@app.route('/delete', methods=['POST'])
def delete_url():
    short_code = request.form['short_code']
    Url = Query()
    db.remove(Url.short_code == short_code)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

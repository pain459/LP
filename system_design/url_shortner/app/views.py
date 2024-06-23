from flask import request, jsonify, render_template, redirect, url_for
from app import app, db
from app.models import URL
from app.utils import generate_hash

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('original_url')
        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url:
            return redirect(url_for('index'))

        url_hash = generate_hash(original_url)
        shortened_url = f"http://short.url/{url_hash}"

        new_url = URL(original_url=original_url, shortened_url=shortened_url, url_hash=url_hash)
        db.session.add(new_url)
        db.session.commit()

        return redirect(url_for('index'))

    urls = URL.query.all()
    return render_template('index.html', urls=urls)

@app.route('/delete/<int:url_id>', methods=['POST'])
def delete_url(url_id):
    url = URL.query.get(url_id)
    if url:
        db.session.delete(url)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:url_id>', methods=['POST'])
def update_url(url_id):
    new_original_url = request.form.get('new_original_url')
    url = URL.query.get(url_id)
    if url:
        new_hash = generate_hash(new_original_url)
        new_shortened_url = f"http://short.url/{new_hash}"

        url.original_url = new_original_url
        url.url_hash = new_hash
        url.shortened_url = new_shortened_url

        db.session.commit()
    return redirect(url_for('index'))

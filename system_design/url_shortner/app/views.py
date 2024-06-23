from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from app.models import URL
from app.utils import generate_short_url

@app.route('/')
def index():
    urls = URL.query.all()
    return render_template('index.html', urls=urls)

@app.route('/', methods=['POST'])
def shorten_url():
    original_url = request.form['original_url']
    short_name = request.form.get('short_name', None)

    existing_url = URL.query.filter_by(original_url=original_url).first()
    if existing_url:
        return jsonify({
            'message': 'URL is already shortened',
            'shortened_url': existing_url.shortened_url,
            'short_name': existing_url.short_name
        }), 200

    if short_name:
        if URL.query.filter_by(short_name=short_name).first():
            return jsonify({'message': 'Short name already exists'}), 400

    url_hash = generate_short_url(original_url)
    shortened_url = url_for('redirect_to_original', url_hash=url_hash, _external=True)
    new_url = URL(original_url=original_url, shortened_url=shortened_url, url_hash=url_hash, short_name=short_name)
    db.session.add(new_url)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/<url_hash>')
def redirect_to_original(url_hash):
    url = URL.query.filter_by(url_hash=url_hash).first_or_404()
    return redirect(url.original_url)

@app.route('/s/<short_name>')
def redirect_to_short_name(short_name):
    url = URL.query.filter_by(short_name=short_name).first_or_404()
    return redirect(url.original_url)

@app.route('/delete/<int:url_id>', methods=['POST'])
def delete_url(url_id):
    url = URL.query.get_or_404(url_id)
    db.session.delete(url)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:url_id>', methods=['POST'])
def update_url(url_id):
    new_original_url = request.form['new_original_url']
    short_name = request.form.get('short_name', None)

    url = URL.query.get_or_404(url_id)
    url.original_url = new_original_url
    url.url_hash = generate_short_url(new_original_url)
    url.shortened_url = url_for('redirect_to_original', url_hash=url.url_hash, _external=True)
    url.short_name = short_name
    db.session.commit()
    return redirect(url_for('index'))

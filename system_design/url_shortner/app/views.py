from flask import Flask, render_template, request, redirect, url_for
from app import app, db
from app.models import URL
from app.utils import generate_short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_name = request.form['short_name']
        url_hash = generate_short_url(original_url)
        shortened_url = request.host_url + 's/' + (short_name if short_name else url_hash)
        
        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url:
            return render_template('index.html', urls=URL.query.all(), message=f"URL is already shortened: {existing_url.shortened_url}")
        
        new_url = URL(original_url=original_url, shortened_url=shortened_url, url_hash=url_hash, short_name=short_name)
        db.session.add(new_url)
        db.session.commit()
        return redirect(url_for('index'))
    
    urls = URL.query.all()
    return render_template('index.html', urls=urls)

@app.route('/s/<identifier>')
def redirect_to_url(identifier):
    url = URL.query.filter((URL.url_hash == identifier) | (URL.short_name == identifier)).first_or_404()
    url.hit_count += 1
    db.session.commit()
    return redirect(url.original_url)

@app.route('/update/<int:url_id>', methods=['POST'])
def update_url(url_id):
    new_original_url = request.form['new_original_url']
    new_short_name = request.form['short_name']
    url = URL.query.get_or_404(url_id)
    url.original_url = new_original_url
    url.short_name = new_short_name
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:url_id>', methods=['POST'])
def delete_url(url_id):
    url = URL.query.get_or_404(url_id)
    db.session.delete(url)
    db.session.commit()
    return redirect(url_for('index'))

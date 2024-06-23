from flask import request, jsonify
from app import app, db
from app.models import URL
from app.utils import generate_hash

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('original_url')
    
    existing_url = URL.query.filter_by(original_url=original_url).first()
    if existing_url:
        return jsonify({
            'message': 'URL is already shortened',
            'shortened_url': existing_url.shortened_url
        }), 200

    url_hash = generate_hash(original_url)
    shortened_url = f"http://short.url/{url_hash}"

    new_url = URL(original_url=original_url, shortened_url=shortened_url, url_hash=url_hash)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        'original_url': original_url,
        'shortened_url': shortened_url
    }), 201

@app.route('/<url_hash>', methods=['GET'])
def retrieve_url(url_hash):
    url = URL.query.filter_by(url_hash=url_hash).first()
    if url:
        return jsonify({'original_url': url.original_url}), 200
    return jsonify({'message': 'URL not found'}), 404

@app.route('/update', methods=['PUT'])
def update_url():
    original_url = request.json.get('original_url')
    new_original_url = request.json.get('new_original_url')
    
    url_hash = generate_hash(original_url)
    url = URL.query.filter_by(url_hash=url_hash).first()
    if not url:
        return jsonify({'message': 'URL not found'}), 404

    new_hash = generate_hash(new_original_url)
    new_shortened_url = f"http://short.url/{new_hash}"

    url.original_url = new_original_url
    url.url_hash = new_hash
    url.shortened_url = new_shortened_url

    db.session.commit()

    return jsonify({
        'message': 'URL updated successfully',
        'original_url': url.original_url,
        'shortened_url': url.shortened_url
    }), 200

@app.route('/delete', methods=['DELETE'])
def delete_url():
    original_url = request.json.get('original_url')
    url_hash = generate_hash(original_url)
    
    url = URL.query.filter_by(url_hash=url_hash).first()
    if not url:
        return jsonify({'message': 'URL not found'}), 404

    db.session.delete(url)
    db.session.commit()

    return jsonify({'message': 'URL deleted successfully'}), 200

from app import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), unique=True, nullable=False)
    shortened_url = db.Column(db.String(10), unique=True, nullable=False)
    url_hash = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, original_url, shortened_url, url_hash):
        self.original_url = original_url
        self.shortened_url = shortened_url
        self.url_hash = url_hash

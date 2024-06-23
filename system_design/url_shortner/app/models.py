from app import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    shortened_url = db.Column(db.String(100), nullable=False, unique=True)
    url_hash = db.Column(db.String(10), nullable=False, unique=True)
    short_name = db.Column(db.String(50), nullable=True, unique=True)

    def __init__(self, original_url, shortened_url, url_hash, short_name=None):
        self.original_url = original_url
        self.shortened_url = shortened_url
        self.url_hash = url_hash
        self.short_name = short_name

from app import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    shortened_url = db.Column(db.String(2048), nullable=False, unique=True)
    url_hash = db.Column(db.String(10), nullable=False, unique=True)
    short_name = db.Column(db.String(50), nullable=True, unique=True)
    hit_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<URL {self.shortened_url}>'

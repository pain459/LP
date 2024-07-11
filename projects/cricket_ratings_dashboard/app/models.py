from . import db

class CountryRanking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String(10), unique=True, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'unique_id': self.unique_id,
            'country': self.country,
            'points': self.points
        }

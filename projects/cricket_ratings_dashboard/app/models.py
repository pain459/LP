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

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String(16), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    country_unique_id = db.Column(db.String(10), db.ForeignKey('country_ranking.unique_id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'unique_id': self.unique_id,
            'name': self.name,
            'country_unique_id': self.country_unique_id
        }

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@db:5432/country_rankings'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

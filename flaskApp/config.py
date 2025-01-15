import os


class Config:
    DEBUG = os.environ.get('DEBUG', True)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','sqlite:///steel_price.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
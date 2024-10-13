import os


class Config:
    def __init__(self):
        project_root = os.path.dirname(os.path.abspath(__file__))
        self.DEBUG = True
        self.SQLALCHEMY_DATABASE_URI = f'sqlite:///data.db'
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.JWT_SECRET_KEY = 'my-secret'

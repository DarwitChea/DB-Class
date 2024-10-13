from flask import Flask
from model import *

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:mysql12345@localhost:5432/AdminDB"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return 'Hello World'


if __name__ == '__main__':  # Corrected to use "name" and double underscores
    app.run()

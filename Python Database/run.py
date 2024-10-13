from flask import Flask
from models import *
from seed import *

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'SECRET'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:Rupp2357.!@localhost:5432/AdminDB"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    
    if Gender.query.count()==0:
        seed_gender()
    
    if Student.query.count() ==0:
        seed_student()

@app.route('/')
def home():
    return 'Hello World'
5
if __name__ == '__main__': 
    app.run()
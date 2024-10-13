from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Student(db.Model):
    # __tablename__='student'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)

    def __repr__(self):
        return f'Student ({self.id},{self.first_name},{self.last_name},{self.email},{self.age})'

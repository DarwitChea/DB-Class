from flask import Flask, request, json
from flask_restx import Api, Resource, fields, reqparse
from models import db, Student

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# with app.app_context():
# db.create_all()


api = Api(app)
api_ns = api.namespace('Api', path='/', description='API Student CRUD')


student_fields = api.model('Student', {
    'first_name': fields.String,
    'last_name': fields.String,
    'gender': fields.String,
    'email': fields.String,
    'age': fields.Integer
}
)

student_parser = reqparse.RequestParser()
student_parser.add_argument('first_name', type=str, required=False)
student_parser.add_argument('last_name', type=str, required=False)
student_parser.add_argument('gender', type=str, required=False)
student_parser.add_argument('email', type=str, required=False)
student_parser.add_argument('age', type=int, required=False)


@api_ns.route('/student')
class ManageStudent(Resource):
    def get(self):
        students = Student.query.filter(Student.last_name.like('%ra%')).all()

        students_list = [{'id': student.id,
                          'first_name': student.first_name,
                          'last_name': student.last_name,
                          'gender': student.gender,
                          'email': student.email,
                          'age': student.age, }
                         for student in students]
        return students_list

    @api_ns.expect(student_fields)
    @api_ns.marshal_with(student_fields)
    def post(self):
        args = api.payload
        print(args)
        item = Student(
            first_name=args['first_name'],
            last_name=args['last_name'],
            gender=args['gender'],
            email=args['email'],
            age=args['age']
        )
        db.session.add(item)
        db.session.commit()
        return item


@api_ns.route('/student/<int:id>')
class ManageStudent(Resource):
    @api_ns.marshal_with(student_fields)
    def get(self, id):
        student = Student.query.get(id)
        if student:
            return student
        api.abort(404, f"Student {id} is not found")

    @api_ns.expect(student_fields)
    @api_ns.marshal_with(student_fields)
    def put(self, id):
        student = Student.query.get(id)
        if student:
            args = api.payload
            student.first_name = args['first_name']
            student.last_name = args['last_name']
            student.gender = args['gender']
            student.email = args['email']
            student.age = args['age']
            db.session.commit()
            return student

    def delete(self, id):
        student = Student.query.get(id)
        if student:
            db.session.delete(student)
            db.session.commit()
            return {"message": f"Item {id} has been deleted"}, 204
        api.abort(404, f"Item {id} not found")


if __name__ == '__main__':
    app.run()

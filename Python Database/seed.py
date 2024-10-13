from models import db,Gender,Student

def seed_gender():
    g1=Gender()
    g1.name_latin = "Male"
    g1.acronym = "M"
    db.session.add(g1)
    db.session.commit()
    
    g2 = Gender(name_latin = "Female",acronym= "F")
    db.session.add(g2)
    db.session.commit()
    
    
def seed_student(): 
    data =[
    {'first_name':'Dara1','last_name':'Sok','gender_id':1,'email':'sok.dara@rupp.edu.kh','age':35},
    {'first_name':'Dara2','last_name':'Sok','gender_id':1,'email':'sok.dara2@rupp.edu.kh','age':40}]
    db.session.bulk_insert_mappings(Student,data)
    db.session.commit()
    
    students = [Student(first_name='Sok1',last_name='Pisey',gender_id=2,email='sok1@rupp.edu.kh',age=24),
    Student(first_name='Sok2',last_name='Pisey',gender_id=2,email='sok2@rupp.edu.kh',age=25)]
    db.session.add_all(students)
    db.session.commit()
    
def update_data():
    s = Student.query.get(1)
    s.name_latin = "Kanha123"
    db.session.commit()


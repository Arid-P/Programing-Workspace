from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DB_PATH = r'Python +SQL\Practice databases\orm_demo.db'
engine = create_engine(f'sqlite:///{DB_PATH}', echo=True)
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer)
    grade = Column(String)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', grade='{self.grade}')>"

#Making the teacher class for the table
class Teacher (Base) :
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = Column(String)
    phone = Column(Integer, unique=True)

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', subject='{self.subject}')>"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#Inserting 2 teachers
teacher1 = Teacher(name="Rahul Cu", subject="Bakchodi", phone=1324793782)
teacher2 = Teacher(name="Mohit", subject="Physics", phone=4874873447)

session.add(teacher1)
session.add(teacher2)
session.commit()

#Reading the conditional data
read_students: List[Student] = session.query(Student).filter_by(grade="10-A").all()
print(read_students)

#Updating the data
update_student: Student = session.query(Student).filter_by(id=1).first()
update_student.grade = "11-A"  #type: ignore
session.commit()

#Deleting the students
students_to_delete = session.query(Student).filter_by(grade="9-A").all()
for student in students_to_delete:
    session.delete(student)
    session.commit()
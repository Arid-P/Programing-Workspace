# ----------------------------------------------------
# LESSON 10 NOTES: SQLAlchemy ORM (Beginner)
# ----------------------------------------------------
# ORM = Object Relational Mapper
# Instead of SQL, you interact using Python Classes.
# SQLAlchemy handles table creation, insertion, querying.
#
# Steps:
# 1. Create engine (connect to SQLite)
# 2. Create Base class
# 3. Create Model classes (Student)
# 4. Create session
# 5. Insert / Query using ORM style

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DB_PATH = r"Python +SQL\Practice databases\orm_demo.db"

# 1. Create Engine (connection to SQLite)
engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)  
# echo=True shows SQL logs (useful for learning)

# 2. Base class
Base = declarative_base()

# 3. Model Class
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer)
    grade = Column(String)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', grade='{self.grade}')>"

# 4. Create tables
Base.metadata.create_all(engine)

# 5. Create Session class
Session = sessionmaker(bind=engine)
session = Session()

# 6. INSERT data using ORM
student1 = Student(name="Aarav", number=9876543210, grade="9-A")
student2 = Student(name="Riya", number=9823001122, grade="10-B")

session.add(student1)
session.add(student2)
session.commit()

# 7. SELECT using ORM
all_students = session.query(Student).all()
print(all_students)

one_student = session.query(Student).filter_by(grade="9-A").all()
print(one_student)

# 8. UPDATE using ORM
student_to_update = session.query(Student).filter_by(name="Aarav").first()
student_to_update.grade = "10-A" # type: ignore
session.commit()

# 9. DELETE using ORM
student_to_delete = session.query(Student).filter_by(name="Riya").first()
session.delete(student_to_delete)
session.commit()


print(end="\n\n\n")
print(all_students)
print(one_student)
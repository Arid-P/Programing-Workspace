from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Students(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(15), unique=True, nullable=False)
    grade = Column(String(5), nullable=False)

    __table_args__ = (
        CheckConstraint("name GLOB '*[^0-9]* *[^0-9]*'"),
        CheckConstraint("CAST(phone_number as INTEGER) BETWEEN 1000000000 AND 9999999999"),
        CheckConstraint("grade GLOB '[1-9]-[A-D]' OR grade GLOB '1[0-2]-[A-D]'"),
    )


class Teachers(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(15), unique=True, nullable=False)
    subject = Column(String(15), nullable=False)

    __table_args__ = (
        CheckConstraint("name GLOB '*[^0-9]* *[^0-9]*'"),
        CheckConstraint("subject GLOB '*[^0-9]* *[^0-9]*'"),
        CheckConstraint("CAST(phone_number as INTEGER) BETWEEN 1000000000 AND 9999999999"),
    )

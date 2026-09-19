from typing import List
import logging

logger = logging.getLogger("school.student")

from sqlalchemy.exc import IntegrityError
from .tables import Students
from . import get_session


def add_student(name: str, phone_number: str, grade: str) -> bool:
    """Add the student record in the database"""
    student = Students(name=name, phone_number=phone_number, grade=grade)
    with get_session() as session:
        try:
            session.add(student)
            session.commit()
            logger.info(f"Added student | name={name}, number={phone_number}, grade={grade}")
        except IntegrityError:
            session.rollback()
            logger.error(f"IntegrityError while adding student | number={phone_number}", exc_info=True)
            return False
    return True


def view_students(grade: None | str = None) -> List[Students]:
    """Returns the list of all the students in the database"""
    with get_session() as session:
        if grade:
            students = session.query(Students).filter_by(grade=grade).all()
            logger.info(f"Students fetched for grade={grade} | count={len(students)}")
        else:
            students = session.query(Students).all()
            logger.info(f"Fetched all students | count={len(students)}")
    return students


def update_student(id_: int, field_num: int, field_value: str) -> bool:
    """Updates the student's records based on its id"""
    logger.info(f"Update requested | id={id_}, field={field_num}, value={field_value}")

    with get_session() as session:
        student: Students = session.query(Students).filter_by(id=id_).first()
        if not student:
            print(f"No student with id {id_} exists.")
            logger.warning(f"Update failed | no student found with id={id_}")
            return False
        
        if field_num == 1:
            student.name = field_value  #type: ignore
        elif field_num == 2:
            student.phone_number = field_value  #type: ignore
        elif field_num == 3:
            student.grade = field_value  #type: ignore
        
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            logger.error(f"IntegrityError while updating student | field={field_num}, value={field_value}", exc_info=True)
            return False

        logger.info(f"Student updated successfully | id={id_}")
    return True


def delete_student(id_: int) -> bool:
    """Deletes the student record based on the id"""
    logger.info(f"Delete requested | id={id_}")

    with get_session() as session:
        student: Students = session.query(Students).filter_by(id=id_).first()
        if not student:
            print(f"No student with id {id_} exists.")
            logger.warning(f"Delete failed | no student found with id={id_}")
            return False
        
        session.delete(student)
        session.commit()
        logger.info(f"Student deleted successfully | id={id_}")

    return True


if __name__ == "__main__":
    print("Go run main.py, not student.py")
    logger.warning("Executed wrong file")

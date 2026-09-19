from typing import List
import logging

logger = logging.getLogger("school.teacher")

from sqlalchemy.exc import IntegrityError
from .tables import Teachers
from . import get_session


def add_teacher(name: str, phone_number: str, subject: str) -> bool:
    """Add the teacher record in the database"""
    teacher = Teachers(name=name, phone_number=phone_number, subject=subject)
    
    with get_session() as session:
        try:
            session.add(teacher)
            session.commit()
            logger.info(f"Added teacher | name={name}, number={phone_number}, subject={subject}")
        except IntegrityError:
            session.rollback()
            logger.error(f"IntegrityError while adding teacher | phone_number={phone_number}", exc_info=True)
            return False
    return True


def view_teacher(subject: None | str = None) -> List[Teachers]:
    """Returns the list of all the teachers in the database"""
    with get_session() as session:
        if subject:
            teachers = session.query(Teachers).filter_by(subject=subject).all()
            logger.info(f"Teachers fetched for subject={subject} | count={len(teachers)}")
        else:
            teachers = session.query(Teachers).all()
            logger.info(f"Fetched all teachers | count={len(teachers)}")
    return teachers


def update_teacher(id_: int, field_num: int, field_value: str) -> bool:
    """Updates the teacher's records based on its id"""
    logger.info(f"Update requested | id={id_}, field={field_num}, value={field_value}")

    with get_session() as session:
        teacher: Teachers = session.query(Teachers).filter_by(id=id_).first()
        if not teacher:
            print(f"No teacher with id {id_} exists.")
            logger.warning(f"Update failed | no teacher found with id={id_}")
            return False
        
        if field_num == 1:
            teacher.name = field_value # type: ignore
        elif field_num == 2:
            teacher.phone_number = field_value# type: ignore
        elif field_num == 3:
            teacher.subject = field_value# type: ignore
        
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            logger.error(f"IntegrityError while updating teacher | field={field_num}, value={field_value}", exc_info=True)
            return False

        logger.info(f"Teacher updated successfully | id={id_}")
    return True


def delete_teacher(id_: int) -> bool:
    """Deletes the teacher record based on the id"""
    logger.info(f"Delete requested | id={id_}")

    with get_session() as session:
        teacher: Teachers = session.query(Teachers).filter_by(id=id_).first()
        if not teacher:
            print(f"No teacher with id {id_} exists.")
            logger.warning(f"Delete failed | no teacher found with id={id_}")
            return False
        
        session.delete(teacher)
        session.commit()
        logger.info(f"Teacher deleted successfully | id={id_}")

    return True


if __name__ == "__main__":
    print("Go run main.py, not teacher.py")
    logger.warning("Executed wrong file")

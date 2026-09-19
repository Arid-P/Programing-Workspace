from gui.logger import get_logger
from school_models import student, teacher  # existing backend

logger = get_logger("backend_adapter")


class BackendAdapter:
    def __init__(self):
        logger.info("BackendAdapter initialized")

    # Students
    def add_student(self, name: str, phone_number: str, grade: str):
        logger.info(f"Calling backend.add_student(name={name}, phone_number={phone_number}, grade={grade})")
        return student.add_student(name, phone_number, grade)

    def view_students(self, grade: str | None = None):
        logger.info(f"Calling backend.view_students(grade={grade})")
        return student.view_students(grade)

    def update_student(self, id_: int, field_num: int, field_value: str):
        logger.info(f"Calling backend.update_student(id={id_}, field={field_num}, value={field_value})")
        return student.update_student(id_, field_num, field_value)

    def delete_student(self, id_: int):
        logger.info(f"Calling backend.delete_student(id={id_})")
        return student.delete_student(id_)

    # Teachers
    def add_teacher(self, name: str, phone_number: str, subject: str):
        logger.info(f"Calling backend.add_teacher(name={name}, phone_number={phone_number}, subject={subject})")
        return teacher.add_teacher(name, phone_number, subject)

    def view_teachers(self, subject: str | None = None):
        logger.info(f"Calling backend.view_teacher(subject={subject})")
        return teacher.view_teacher(subject)

    def update_teacher(self, id_: int, field_num: int, field_value: str):
        logger.info(f"Calling backend.update_teacher(id={id_}, field={field_num}, value={field_value})")
        return teacher.update_teacher(id_, field_num, field_value)

    def delete_teacher(self, id_: int):
        logger.info(f"Calling backend.delete_teacher(id={id_})")
        return teacher.delete_teacher(id_)

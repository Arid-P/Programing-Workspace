from gui.logger import get_logger
from gui.adapters.backend_adapter import BackendAdapter

logger = get_logger("student_controller")


class StudentController:
    def __init__(self):
        logger.info("StudentController initialized")
        self.backend = BackendAdapter()

    def add_student(self, name: str, phone_number: str, grade: str):
        logger.info(f"UI request → Add student | name={name}, phone_number={phone_number}, grade={grade}")
        try:
            success = self.backend.add_student(name, phone_number, grade)
            if success:
                logger.info("Student added successfully via backend")
            return success
        except Exception as e:
            logger.error(f"Backend rejected add_student: {e}")
            return False

    def view_students(self, grade: str | None  = None):
        logger.info(f"UI request → View students | grade={grade}")
        try:
            return self.backend.view_students(grade)
        except Exception as e:
            logger.error(f"Backend rejected view_students: {e}")
            return []

    def update_student(self, id_: int, field_num: int, field_value: str):
        logger.info(f"UI request → Update student | id={id_}, field={field_num}, value={field_value}")
        try:
            return self.backend.update_student(id_, field_num, field_value)
        except Exception as e:
            logger.error(f"Backend rejected update_student: {e}")
            return False

    def delete_student(self, id_: int):
        logger.info(f"UI request → Delete student | id={id_}")
        try:
            return self.backend.delete_student(id_)
        except Exception as e:
            logger.error(f"Backend rejected delete_student: {e}")
            return False

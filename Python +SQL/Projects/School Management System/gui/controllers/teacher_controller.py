from gui.logger import get_logger
from gui.adapters.backend_adapter import BackendAdapter

logger = get_logger("teacher_controller")


class TeacherController:
    def __init__(self):
        logger.info("TeacherController initialized")
        self.backend = BackendAdapter()

    def add_teacher(self, name: str, phone_number: str, subject: str):
        logger.info(f"UI request → Add teacher | name={name}, phone_number={phone_number}, subject={subject}")
        try:
            success = self.backend.add_teacher(name, phone_number, subject)
            if success:
                logger.info("Teacher added successfully via backend")
            return success
        except Exception as e:
            logger.error(f"Backend rejected add_teacher: {e}")
            return False

    def view_teachers(self, subject: str | None  = None):
        logger.info(f"UI request → View teachers | subject={subject}")
        try:
            return self.backend.view_teachers(subject)
        except Exception as e:
            logger.error(f"Backend rejected view_teachers: {e}")
            return []

    def update_teacher(self, id_: int, field_num: int, field_value: str):
        logger.info(f"UI request → Update teacher | id={id_}, field={field_num}, value={field_value}")
        try:
            return self.backend.update_teacher(id_, field_num, field_value)
        except Exception as e:
            logger.error(f"Backend rejected update_teacher: {e}")
            return False

    def delete_teacher(self, id_: int):
        logger.info(f"UI request → Delete teacher | id={id_}")
        try:
            return self.backend.delete_teacher(id_)
        except Exception as e:
            logger.error(f"Backend rejected delete_teacher: {e}")
            return False

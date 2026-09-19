from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s",
    filename="Python +SQL/Projects/School Management System3/Logging/management_system.log",      # The file where logs will be saved
    filemode="a"             
)

logger = logging.getLogger("school.main")
logger.info(f"\n\n{'-'*100}\n")
logger.info( 'Next run')

from school_models import student, teacher, validity_checking as vc

logger = logging.getLogger("school.main")
logger.setLevel(logging.DEBUG)

def log_call(func):
    def inner(*args, **kwargs):
        logger.info(f"{func.__name__} called")
        return func(*args, **kwargs)
    return inner


class CRUDFunction(ABC):
    def __init__(self, model_type: str) -> None:
        if not model_type:
            raise ValueError("model_type must be provided")
        self.model_type = model_type
        self.validity_handler = vc.ValidityHandle(model_type)

    @abstractmethod
    def get_extra_fields(self) -> dict[str, str]:
        pass

    @abstractmethod
    def _add_to_db(self, name: str, phone_number: str, extra_data: dict[str, str]) -> bool:
        pass

    @abstractmethod
    def view_all_which(self, extra: dict[str, str]) -> list:
        pass
    
    @abstractmethod
    def _print_records(self, records: list, extra: dict[str, str]):
        pass
    
    @abstractmethod
    def _update_to_db(self, id_: int, field_selected_num: int, field_value) -> bool:
        pass

    @abstractmethod
    def _delete_to_db(self, id_: int) -> bool:
        pass

    @log_call
    def add(self):
        print(f"To add a new {self.model_type} record, kindly enter the following details:")
        name = self.validity_handler.name_validity()
        phone_number = self.validity_handler.phone_number_validity()
        extra_data = self.get_extra_fields()
        check = self._add_to_db(name, phone_number, extra_data)

        if check:
            print(f"New {self.model_type} record has been added.")
            logger.info(f"New {self.model_type} added | name={name}")
        else:
            print(f"Record was not added; phone number already exists.")
            logger.info(f"{self.model_type} record not added | duplicate phone number={phone_number}")

    @log_call
    def view_all(self):
        extra_data = {'grade': None, 'subject': None}
        records = self.view_all_which(extra_data) #type: ignore
        self._print_records(records, extra_data) #type: ignore

    @log_call
    def view_by_criteria(self):
        extra_data = self.get_extra_fields()
        records = self.view_all_which(extra_data)
        self._print_records(records, extra_data)

    @log_call
    def update(self):
        id_ = self.validity_handler.id_validity()
        fields = ['Name', 'Phone Number', 'Grade/Subject']

        print("Select the field to update:")
        for idx, field in enumerate(fields, start=1):
            print(f"{idx}. {field}")

        field_selected_num = self.validity_handler.option_validity(1, len(fields))

        if field_selected_num == 1:
            field_value = self.validity_handler.name_validity()
        elif field_selected_num == 2:
            field_value = self.validity_handler.phone_number_validity()
        else:
            extra_data = self.get_extra_fields()
            field_value = extra_data[list(extra_data.keys())[0]]

        updated = self._update_to_db(id_, field_selected_num, field_value)
        
        if updated:
            print("Record successfully updated.")
            logger.info(f"Record updated | id={id_}")
        else:
            print("Record was not updated. Check ID or input value.")
            logger.info(f"Update failed | id={id_}")

    @log_call
    def delete(self):
        id_ = self.validity_handler.id_validity()
        confirm = input(f"Do you really want to delete the record with id {id_}? Type 'yes' to confirm: ")
        if confirm.lower() != 'yes':
            print("Record not deleted.")
            logger.info(f"Deletion cancelled | id={id_}")
            return

        deleted = self._delete_to_db(id_)
        if deleted:
            print("Record successfully deleted.")
            logger.info(f"Record deleted | id={id_}")
        else:
            print("Record not found or could not be deleted.")
            logger.info(f"Deletion failed | id={id_}")


class StudentFunction(CRUDFunction):
    def __init__(self):
        super().__init__("student")

    @log_call
    def get_extra_fields(self):
        return {"grade": self.validity_handler.grade_validity()}

    @log_call
    def _add_to_db(self, name, phone_number, extra):
        return student.add_student(name, phone_number, extra["grade"])

    @log_call
    def view_all_which(self, extra) -> list[student.Students]:
        return student.view_students(extra.get('grade'))

    @log_call
    def _print_records(self, records, extra):
        if not records:
            print("No students found.")
            logger.info("No students in database")
            return
        print(f"{'ID':<6}{'Name':<25}{'Number':<12}{'Grade':<5}")
        print("-"*50)
        for s in records:
            print(f"{s.id:<6}{s.name:<25}{s.phone_number:<12}{s.grade:<5}")
        logger.info(f"Displayed students | extra_data={extra}")

    @log_call
    def _update_to_db(self, id_, field_selected_num, field_value):
        return student.update_student(id_, field_selected_num, field_value)

    @log_call
    def _delete_to_db(self, id_):
        return student.delete_student(id_)

class TeacherFunction(CRUDFunction):
    def __init__(self):
        super().__init__("teacher")

    @log_call
    def get_extra_fields(self):
        return {"subject": self.validity_handler.subject_validity()}

    @log_call
    def _add_to_db(self, name, phone_number, extra):
        return teacher.add_teacher(name, phone_number, extra["subject"])

    @log_call
    def view_all_which(self, extra) -> list[teacher.Teachers]:
        return teacher.view_teacher(extra.get('subject'))

    @log_call
    def _print_records(self, records, extra):
        if not records:
            print("No teachers found.")
            logger.info("No teachers in database")
            return
        print(f"{'ID':<6}{'Name':<25}{'Number':<12}{'Subject':<10}")
        print("-"*55)
        for t in records:
            print(f"{t.id:<6}{t.name:<25}{t.phone_number:<12}{t.subject:<10}")
        logger.info(f"Displayed teachers | extra_data={extra}")

    @log_call
    def _update_to_db(self, id_, field_selected_num, field_value):
        return teacher.update_teacher(id_, field_selected_num, field_value)

    @log_call
    def _delete_to_db(self, id_):
        return teacher.delete_teacher(id_)


# ----------------------
# Convenience methods to match previous main.py design
# ----------------------

# Student wrappers
class StudentActions(StudentFunction):
    @log_call
    def add_student(self):
        super().add()

    @log_call
    def view_all_students(self):
        super().view_all()

    @log_call
    def view_students_by_grade(self):
        super().view_by_criteria()

    @log_call
    def update_student(self):
        super().update()

    @log_call
    def delete_student(self):
        super().delete()


# Teacher wrappers
class TeacherActions(TeacherFunction):
    @log_call
    def add_teacher(self):
        super().add()

    @log_call
    def view_all_teachers(self):
        super().view_all()

    @log_call
    def view_teachers_by_subject(self):
        super().view_by_criteria()

    @log_call
    def update_teacher(self):
        super().update()

    @log_call
    def delete_teacher(self):
        super().delete()

def main() -> None:
    """Starting function for the School Management System"""
    logger.info("Management system has been started")

    # Initialize the action classes
    student_actions = StudentActions()
    teacher_actions = TeacherActions()

    # Menu mapping
    menu_options_func = {
        "Add New Student Record": student_actions.add_student,
        "Add New Teacher Record": teacher_actions.add_teacher,
        "View All Students": student_actions.view_all_students,
        "View All Teachers": teacher_actions.view_all_teachers,
        "View Students by Grade": student_actions.view_students_by_grade,
        "View Teachers by Subject": teacher_actions.view_teachers_by_subject,
        "Update a Student Record": student_actions.update_student,
        "Update a Teacher Record": teacher_actions.update_teacher,
        "Delete a Student Record": student_actions.delete_student,
        "Delete a Teacher Record": teacher_actions.delete_teacher,
        "Exit the Management System": exit
    }

    menu_options = list(menu_options_func.keys())

    while True:
        logger.info("Menu loop started")

        print("Select an option by typing the number in front of it:")
        for idx, menu in enumerate(menu_options):
            print(f"{idx+1}. {menu}")
        print()

        # Valid input from user
        validity_handler = vc.ValidityHandle("main")
        command_selected_num = validity_handler.option_validity(1, len(menu_options))

        # Execute the corresponding function
        method = menu_options_func[menu_options[command_selected_num - 1]]

        if method != exit:
            logger.info(f"Option selected: {menu_options[command_selected_num-1]} | Function: {method.__name__}")
        else:
            logger.info("Option selected: Exit the Management System")
            logger.info(f"Function called: exit")
        method()
        print()


if __name__ == "__main__":
    print()
    main()

import logging

logger = logging.getLogger("school.validity_checking")


# Custom exceptions
class EmptyValueError(Exception):
    """Raised when input is empty."""
    pass


class InvalidCharacterError(Exception):
    """Raised when input contains invalid characters."""
    pass


class ValueOutOfRangeError(Exception):
    """Raised when input is outside allowed range."""
    pass


class ValidityHandle:
    def __init__(self, model_type: str) -> None:
        self.model_type = model_type

    def option_validity(self, lower_limit: int, upper_limit: int) -> int:
        while True:
            users_input = input("Enter the option number: ")
            try:
                value = int(users_input)
                if not (lower_limit <= value <= upper_limit):
                    raise ValueOutOfRangeError
                return value
            except ValueError:
                print("Please enter an integer value like 1, 2, 3.")
                logger.warning(f"Invalid input for option: {users_input}")
            except ValueOutOfRangeError:
                print(f"Please enter an option between {lower_limit} and {upper_limit}.")
                logger.warning(f"Option out of range: {users_input}")

    def id_validity(self) -> int:
        while True:
            users_input = input(f"Enter the id of the {self.model_type}: ")
            try:
                value = int(users_input)
                if not (1 <= value <= 99999):
                    raise ValueOutOfRangeError
                return value
            except ValueError:
                print("Please enter a valid integer ID.")
                logger.warning(f"Invalid ID input: {users_input}")
            except ValueOutOfRangeError:
                print("ID must be between 1 and 99999.")
                logger.warning(f"ID out of range: {users_input}")

    def name_validity(self) -> str:
        while True:
            name = input(f"Enter the name of the {self.model_type}: ").strip()
            try:
                if not name:
                    raise EmptyValueError
                if any(not c.isalpha() and c != " " for c in name):
                    raise InvalidCharacterError
                return name
            except EmptyValueError:
                print("Name cannot be empty.")
                logger.warning("Empty name submitted")
            except InvalidCharacterError:
                print("Name must contain only alphabets and spaces.")
                logger.warning(f"Invalid characters in name: {name}")

    def phone_number_validity(self) -> str:
        while True:
            users_input = input(f"Enter the number of the {self.model_type}: ").strip()
            try:
                if len(users_input) != 10 or not users_input.isdigit():
                    raise ValueOutOfRangeError
                return users_input
            except ValueOutOfRangeError:
                print("Phone number must have exactly 10 digits and contain only numbers.")
                logger.warning(f"Invalid phone number: {users_input}")

    def grade_validity(self) -> str:
        while True:
            users_input = input("Enter the grade of the student (like 10 A): ").strip()
            try:
                parts = users_input.split()
                if len(parts) != 2:
                    raise ValueError
                class_no = int(parts[0])
                section = parts[1].upper()
                if class_no < 1 or class_no > 12:
                    raise ValueOutOfRangeError
                if section not in {"A", "B", "C", "D"}:
                    raise InvalidCharacterError
                return f"{class_no}-{section}"
            except ValueError:
                print("Enter a valid grade format like '10 A'.")
                logger.warning(f"Invalid grade format: {users_input}")
            except InvalidCharacterError:
                print("Section must be one of A, B, C, D.")
                logger.warning(f"Invalid section: {users_input}")
            except ValueOutOfRangeError:
                print("Class number must be between 1 and 12.")
                logger.warning(f"Class number out of range: {users_input}")

    def subject_validity(self) -> str:
        while True:
            subject = input(f"Enter the subject of the {self.model_type}: ").strip()
            try:
                if not subject:
                    raise EmptyValueError
                if any(not c.isalpha() and c != " " for c in subject):
                    raise InvalidCharacterError
                return subject
            except EmptyValueError:
                print("Subject cannot be empty.")
                logger.warning("Empty subject submitted")
            except InvalidCharacterError:
                print("Subject must contain only alphabets and spaces.")
                logger.warning(f"Invalid characters in subject: {subject}")

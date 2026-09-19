from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel
from gui.logger import get_logger

logger = get_logger("forms")

class SimpleForm(QWidget):
    def __init__(self, fields: dict[str, str]):
        super().__init__()
        logger.info(f"Initializing SimpleForm with fields: {fields}")

        # Correct initialization
        form_layout = QFormLayout()
        self.inputs = {}

        for field_name, placeholder in fields.items():
            label = QLabel(field_name)
            line_edit = QLineEdit()
            line_edit.setPlaceholderText(placeholder)
            form_layout.addRow(label, line_edit)  # addRow is a method of QFormLayout
            self.inputs[field_name] = line_edit

        self.setLayout(form_layout)  # set the layout for the widget

    def get_values(self) -> dict[str, str]:
        values = {k: v.text() for k, v in self.inputs.items()}
        logger.info(f"Form values retrieved: {values}")
        return values

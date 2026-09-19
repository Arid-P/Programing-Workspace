from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem, QHBoxLayout
)
from PySide6.QtCore import Qt

from gui.logger import get_logger
from gui.controllers.student_controller import StudentController

logger = get_logger("student_view")


class StudentView(QWidget):
    def __init__(self):
        super().__init__()
        logger.info("Initializing StudentView")

        self.controller = StudentController()

        self.setWindowTitle("Student Management")
        self.setMinimumSize(600, 400)

        layout = QVBoxLayout(self)

        title = QLabel("Student Management")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(title)

        # Add Student Form
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Phone Number")
        self.grade_input = QLineEdit()
        self.grade_input.setPlaceholderText("Grade (e.g., 10-A)")

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(self.grade_input)

        layout.addLayout(form_layout)

        add_btn = QPushButton("Add Student")
        add_btn.clicked.connect(self.on_add_student)
        layout.addWidget(add_btn)

        # Student Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Grade"])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.refresh_table()

    def on_add_student(self):
        logger.info("Add Student button clicked")
        name = self.name_input.text()
        phone = self.phone_input.text()
        grade = self.grade_input.text()

        if self.controller.add_student(name, phone, grade):
            logger.info("Student added, refreshing table")
            self.refresh_table()
        else:
            logger.error("Failed to add student")

    def refresh_table(self):
        students = self.controller.view_students()
        self.table.setRowCount(len(students))
        for i, s in enumerate(students):
            self.table.setItem(i, 0, QTableWidgetItem(str(s.id)))  #type: ignore
            self.table.setItem(i, 1, QTableWidgetItem(s.name))  #type: ignore
            self.table.setItem(i, 2, QTableWidgetItem(s.phone_number))  #type: ignore
            self.table.setItem(i, 3, QTableWidgetItem(s.grade))  #type: ignore

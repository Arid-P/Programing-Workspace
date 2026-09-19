from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout
)
from PySide6.QtCore import Qt

from gui.logger import get_logger
from gui.controllers.teacher_controller import TeacherController

logger = get_logger("teacher_view")


class TeacherView(QWidget):
    def __init__(self):
        super().__init__()
        logger.info("Initializing TeacherView")

        self.controller = TeacherController()

        self.setWindowTitle("Teacher Management")
        self.setMinimumSize(600, 400)

        layout = QVBoxLayout(self)

        title = QLabel("Teacher Management")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(title)

        # Add Teacher Form
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Phone Number")
        self.subject_input = QLineEdit()
        self.subject_input.setPlaceholderText("Subject")

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(self.subject_input)

        layout.addLayout(form_layout)

        add_btn = QPushButton("Add Teacher")
        add_btn.clicked.connect(self.on_add_teacher)
        layout.addWidget(add_btn)

        # Teacher Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Subject"])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.refresh_table()

    def on_add_teacher(self):
        logger.info("Add Teacher button clicked")
        name = self.name_input.text()
        phone = self.phone_input.text()
        subject = self.subject_input.text()

        if self.controller.add_teacher(name, phone, subject):
            logger.info("Teacher added, refreshing table")
            self.refresh_table()
        else:
            logger.error("Failed to add teacher")

    def refresh_table(self):
        teachers = self.controller.view_teachers()
        self.table.setRowCount(len(teachers))
        for i, t in enumerate(teachers):
            self.table.setItem(i, 0, QTableWidgetItem(str(t.id)))  #type: ignore
            self.table.setItem(i, 1, QTableWidgetItem(t.name))  #type: ignore
            self.table.setItem(i, 2, QTableWidgetItem(t.phone_number))  #type: ignore
            self.table.setItem(i, 3, QTableWidgetItem(t.subject))  #type: ignore

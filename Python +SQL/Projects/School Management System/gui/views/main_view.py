from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from gui.logger import get_logger
from gui.views.student_view import StudentView
from gui.views.teacher_view import TeacherView

logger = get_logger("main_view")

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        logger.info("Initializing MainView")

        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()

        # Add tabs
        self.tabs.addTab(StudentView(), "Students")
        self.tabs.addTab(TeacherView(), "Teachers")

        layout.addWidget(self.tabs)

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from gui.theme import DARK_THEME
from gui.views.student_view import StudentView
from gui.views.teacher_view import TeacherView
from gui.logger import get_logger

logger = get_logger("app")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("School Management System")
        self.setMinimumSize(1000, 650)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        tabs = QTabWidget()
        tabs.addTab(StudentView(), "Students")
        tabs.addTab(TeacherView(), "Teachers")

        layout.addWidget(tabs)


def main():
    logger.info("Starting GUI application")
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_THEME)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

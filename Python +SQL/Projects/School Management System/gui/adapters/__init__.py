# gui/app.py

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
    QTabWidget,
)

from gui.theme import DARK_THEME


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("School Management System")
        self.setMinimumSize(1000, 650)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        # Tabs (Students / Teachers)
        tabs = QTabWidget()

        # Temporary placeholders
        tabs.addTab(self._placeholder("Students Module UI Coming Next"), "Students")
        tabs.addTab(self._placeholder("Teachers Module UI Coming Next"), "Teachers")

        layout.addWidget(tabs)

    def _placeholder(self, text: str) -> QWidget:
        w = QWidget()
        l = QVBoxLayout(w)
        lbl = QLabel(text)
        lbl.setStyleSheet("font-size: 18px; padding: 20px;")
        l.addWidget(lbl)
        l.addStretch()
        return w


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_THEME)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

# DARK_THEME stylesheet for PySide6
# Applied via app.setStyleSheet(DARK_THEME)

DARK_THEME = """
QWidget {
    background-color: #2E2E2E;
    color: #F0F0F0;
    font-family: "Segoe UI", sans-serif;
    font-size: 14px;
}

QLabel {
    color: #F0F0F0;
    font-weight: bold;
}

QPushButton {
    background-color: #4A90E2;
    color: #FFFFFF;
    border-radius: 5px;
    padding: 6px 12px;
}

QPushButton:hover {
    background-color: #6BA8FF;
}

QPushButton:pressed {
    background-color: #3B78D8;
}

QLineEdit, QSpinBox, QComboBox, QTextEdit {
    background-color: #3C3C3C;
    color: #F0F0F0;
    border: 1px solid #555555;
    border-radius: 4px;
    padding: 4px;
}

QTabWidget::pane {
    border: 1px solid #555555;
    top: -1px;
}

QTabBar::tab {
    background: #3C3C3C;
    color: #F0F0F0;
    padding: 6px 12px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    margin-right: 2px;
}

QTabBar::tab:selected {
    background: #4A90E2;
}

QTableWidget {
    background-color: #3C3C3C;
    gridline-color: #555555;
}

QHeaderView::section {
    background-color: #4A4A4A;
    color: #F0F0F0;
    padding: 4px;
    border: 1px solid #555555;
}
"""

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

def populate_table(table: QTableWidget, data: list, columns: list):
    table.setColumnCount(len(columns))
    table.setHorizontalHeaderLabels(columns)
    table.setRowCount(len(data))
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            table.setItem(i, j, QTableWidgetItem(str(val)))

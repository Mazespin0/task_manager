import sys
import os
import PySide6
from math import sqrt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from mainwindow import Ui_MainWindow

import sqlite3

def _init_sql():
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute("SELECT NAME FROM projects;")
    global one_result
    one_result = cur.fetchall()

    n = "1"
    d = "2"



    sqlite_insert_query = """INSERT INTO projects
                          (name, deadline)
                          VALUES
                          ('{n}', '{d}');"""
    count = cur.execute(sqlite_insert_query)
    conn.commit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загрузка интерфейса из файла .ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Использование project_list
        for el in range (0, len(one_result)):
            self.ui.project_list.addItem(one_result[el][0])
        


if __name__ == "__main__":

    _init_sql()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

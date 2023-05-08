import sys
import os
import PySide6
from math import sqrt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QTableWidget, QTableWidgetItem
from PyQt5 import QtWidgets, uic
from mainwindow import Ui_MainWindow
from dialog import Ui_Dialog

import sqlite3

def _init_sql():
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute("SELECT NAME FROM projects;")
    global one_result
    one_result = cur.fetchall()

    conn.commit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        _init_sql()
        # Загрузка интерфейса из файла .ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # обработчики кнопок
        self.ui.addButton.clicked.connect(self.addButton_clicked)
        self.ui.delButton.clicked.connect(self.delButton_clicked)
        self.ui.editButton.clicked.connect(self.editButton_clicked)

        # привязка таблицы
        self.tableWidget = self.ui.tableWidget
        self.tableWidget.setRowCount(9) 
        self.tableWidget.setColumnCount(3)

        print(one_result)

        # вытаскиваем данные из таблицы
        if len(one_result) > 0:
            for i in range(0, len(one_result)):
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(one_result[i][0]))
        

        
    #функция добавления нового проекта    
    def addButton_clicked(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Dialog')
        dialog.exec()
        print("Добавить")
    #Функция удаления 
    def delButton_clicked(self):
        print("Удалить")
    #Функция Измеенения уже добавленого проекта
    def editButton_clicked(self):
        print("Изменить")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())







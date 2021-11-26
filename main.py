import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem


class Programm(QWidget):
    def __init__(self):
        super(Programm, self).__init__()
        uic.loadUI('main.ui', self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('SELECT * FROM coffee').fetchall()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                              'Описание вкуса', 'Цена', 'Объем упаковки'])
        self.table.setRowCount(0)
        for i, row in enumerate(result):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(elem)))



import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QApplication


class Programm(QWidget):
    def __init__(self):
        super(Programm, self).__init__()
        uic.loadUi('main.ui', self)
        global self_programm
        self_programm = self
        self.btn.clicked.connect(self.open_window)
        self.btn_restart.clicked.connect(self.restart)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        result = self.cur.execute('SELECT * FROM coffee').fetchall()
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

    def open_window(self):
        self.form = Window()
        self.form.show()

    def restart(self):
        result = self.cur.execute('SELECT * FROM coffee').fetchall()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                              'Описание вкуса', 'Цена', 'Объем порции'])
        self.table.setRowCount(0)
        for i, row in enumerate(result):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(elem)))


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.btn_change.clicked.connect(self.change)
        self.btn_add.clicked.connect(self.add)

    def change(self):
        id = self.id_input.text()
        type = self.type_input.text()
        roast_degree = self.roast_degree_input.text()
        consistency = self.consistency_input.text()
        taste = self.taste_input.toPlainText()
        price = self.price_input.text()
        volume = self.volume_input.text()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        if type != '':
            cur.execute(f'''UPDATE coffee
SET type = "{type}"
WHERE id = "{id}"''')
        if roast_degree != '':
            cur.execute(f'''UPDATE coffee
SET roast_degree = "{roast_degree}"
WHERE id = "{id}"''')
        if consistency != '':
            cur.execute(f'''UPDATE coffee
SET consistency = "{consistency}"
WHERE id = "{id}"''')
        if taste != '':
            cur.execute(f'''UPDATE coffee
SET taste = "{taste}"
WHERE id = "{id}"''')
        if price != '':
            cur.execute(f'''UPDATE coffee
SET price = "{price}"
WHERE id = "{id}"''')
        if volume != '':
            cur.execute(f'''UPDATE coffee
SET volume = "{volume}"
WHERE id = "{id}"''')
        con.commit()
        self_programm.form.close()
        self_programm.restart()

    def add(self):
        id = self.id_input.text()
        type = self.type_input.text()
        roast_degree = self.roast_degree_input.text()
        consistency = self.consistency_input.text()
        taste = self.taste_input.toPlainText()
        price = self.price_input.text()
        volume = self.volume_input.text()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute(f"INSERT INTO coffee VALUES ('{id}', '{type}', '{roast_degree}',"
                    f" '{consistency}', '{taste}', '{price}', '{volume}')")
        con.commit()
        self_programm.form.close()
        self_programm.restart()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Programm()
    ex.show()
    sys.exit(app.exec())

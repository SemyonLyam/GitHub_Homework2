from PyQt5.QtWidgets import QWidget, QPushButton


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Git и случайные окружности')
        self.btn = QPushButton('Пуск', self)
        self.btn.move(2, 2)
        self.btn.resize(45, 25)
        self.btn.clicked.connect(self.drawf)

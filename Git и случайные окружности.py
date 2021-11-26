import sys
from random import randint
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication
from UI import UI


class Programm(UI):
    def __init__(self):
        super(Programm, self).__init__()
        self.qp = QPainter()
        self.flag = False

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        x = randint(1, 600)
        y = randint(1, 600)
        radius = randint(1, 300)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.qp.setBrush(QColor(r, g, b))
        self.qp.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Programm()
    ex.show()
    sys.exit(app.exec())

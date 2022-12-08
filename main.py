import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from random import randint as rnd


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.push)
        self.c = []

    def push(self):
        self.c.append((rnd(0, 600), rnd(0, 300), rnd(5, 30)))
        self.repaint()

    def paintEvent(self, event=None):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        for circle in self.c:
            qp.drawEllipse(circle[0], circle[1], circle[2], circle[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

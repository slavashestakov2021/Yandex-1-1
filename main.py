import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from random import randint as rnd
from ui import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.push)
        self.c = []

    def push(self):
        color = QColor(rnd(0, 255), rnd(0, 255), rnd(0, 255))
        self.c.append((rnd(0, 600), rnd(0, 300), rnd(5, 30), color))
        self.repaint()

    def paintEvent(self, event=None):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        for circle in self.c:
            qp.setPen(QPen(circle[-1], 5, Qt.SolidLine))
            qp.setBrush(QBrush(circle[-1], Qt.SolidPattern))
            qp.drawEllipse(circle[0], circle[1], circle[2], circle[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

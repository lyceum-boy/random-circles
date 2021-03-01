import sys
import random


from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QWidget, QApplication

from UI import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.qp = QPainter()

        self.flag = False
        self.coordinates = None

        self.pushButton.clicked.connect(self.draw_flag)

    def draw(self):
        for _ in range(random.randint(10, 100)):
            x = random.randint(1, self.width())
            y = random.randint(1, self.height())
            size = random.randint(1, min([self.width(), self.height()]) // 4)
            self.qp.setBrush(QColor(random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255)))
            self.qp.drawEllipse(x - size // 2, y - size // 2, size, size)

    def draw_flag(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()


def excepthook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

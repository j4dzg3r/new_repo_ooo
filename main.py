from PyQt6 import QtGui, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
import random

from ui import Ui_MainWindow

class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.load_ui.loadUi("UI.ui", self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.button.clicked.connect(self.createCircle)
        self.do_paint = True

    def paintEvent(self, event):
        if self.do_paint:
            painter = QtGui.QPainter()
            painter.begin(self)
            painter.setBrush(QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            x, y = random.randint(0, 800), random.randint(0, 600)
            width = random.randint(0, 500)
            painter.drawEllipse(x, y, width, width)
            painter.end()
        self.do_paint = False

    def createCircle(self):
        self.do_paint = True
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())

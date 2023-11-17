from PyQt6 import QtGui, uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import random

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.load_ui.loadUi("UI.ui", self)
        self.initUI()

    def initUI(self):
        self.button = self.findChild(QPushButton, 'button')
        self.button.clicked.connect(self.createCircle)
        self.do_paint = True

    def paintEvent(self, event):
        if self.do_paint:
            painter = QtGui.QPainter()
            painter.begin(self)
            painter.setBrush(QtCore.Qt.GlobalColor.yellow)
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

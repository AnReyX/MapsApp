import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class Error_Window(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('Error_Window.ui', self)

        self.Understand_btn.clicked.connect(self.Dest)

    def Dest(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Error_Window()
    ex.show()
    sys.exit(app.exec())
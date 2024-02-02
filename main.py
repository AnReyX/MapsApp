import sys
import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView, QMainWindow


class MapsAPI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Map_API.ui', self)
        self.request = "https://static-maps.yandex.ru/1.x/?ll=139.295036%2C-24.682020&spn=0.016457,20.91619&l=sat"
        self.response = requests.get(self.request)
        self.map_file = 'map.png'
        with open(self.map_file, 'wb') as f:
            f.write(self.response.content)
        self.pixmap = QPixmap(self.map_file)
        self.Result_picture_label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapsAPI()
    ex.show()
    sys.exit(app.exec())

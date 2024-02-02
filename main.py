import sys
import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MapsAPI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Map_API.ui', self)
        self.map_file = 'map.png'

        self.pushButton.clicked.connect(self.updateMap)

    def updateMap(self):
        x_position = self.X_Pos_line.text()
        y_position = self.Y_Pos_line.text()
        zoom = self.Zoom_line.text()

        self.request = f"https://static-maps.yandex.ru/1.x/?ll={x_position},{y_position}&z={zoom}&l=sat"
        response = requests.get(self.request)

        # Обновляем карту
        with open(self.map_file, 'wb') as f:
            f.write(response.content)
        pixmap = QPixmap(self.map_file)
        self.Result_picture_label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapsAPI()
    ex.show()
    sys.exit(app.exec())

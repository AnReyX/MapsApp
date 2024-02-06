import sys
import requests
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MapsAPI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.map_type = "sat"
        uic.loadUi('Map_API.ui', self)
        self.map_file = 'map.png'

        self.Search_btn.clicked.connect(self.updateMap)
        self.Hybrid_btn.clicked.connect(self.Hybrid_Map)
        self.Satellite_btn.clicked.connect(self.Satelite_Map)
        self.Scheme_btn.clicked.connect(self.Scheme_Map)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_PageUp, Qt.Key_PageDown):
            try:
                n = float(self.Zoom_line.text())
                self.Zoom_line.setText(str(round(n + (0.1 if event.key() == Qt.Key_PageUp else -0.1), 1)))
                self.updateMap()
            except ValueError:
                self.Zoom_line.setText('0')
        if event.key() in (Qt.Key_Down, Qt.Key_Up):
            try:
                n = float(self.Y_Pos_line.text())
                self.Y_Pos_line.setText(str(round(n + (0.1 if event.key() == Qt.Key_Up else -0.1), 1)))
                self.updateMap()
            except ValueError:
                self.Y_Pos_line.setText('0')
        event.accept()
        if event.key() in (Qt.Key_Right, Qt.Key_Left):
            try:
                n = float(self.X_Pos_line.text())
                self.X_Pos_line.setText(str(round(n - (0.1 if event.key() == Qt.Key_Right else -0.1), 1)))
                self.updateMap()
            except ValueError:
                self.X_Pos_line.setText('0')
        event.accept()

    def Satelite_Map(self):
        self.map_type = "sat"
        self.updateMap()

    def Scheme_Map(self):
        self.map_type = "map"
        self.updateMap()

    def Hybrid_Map(self):
        self.map_type = "skl"
        self.updateMap()

    def updateMap(self):
        try:
            x = float(self.X_Pos_line.text())
            if not 0 <= x < 180:
                raise ValueError
        except ValueError:
            self.X_Pos_line.setText('0')
            x = 0
        try:
            y = float(self.Y_Pos_line.text())
            if not 0 <= y < 85:
                raise ValueError
        except ValueError:
            self.Y_Pos_line.setText('0')
            y = 0
        try:
            spn = float(self.Zoom_line.text())
            if not 0 <= spn <= 90:
                self.Zoom_line.setText('0' if 0 > spn else '90')
                spn = 0 if 0 > spn else 90
        except ValueError:
            self.Zoom_line.setText('0')
            spn = 0
        response = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={x},{y}&spn={spn},{spn}&size=650,400&l={self.map_type}")
        with open(self.map_file, 'wb') as f:
            f.write(response.content)
        pixmap = QPixmap(self.map_file)
        self.Result_picture_label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapsAPI()
    ex.show()
    sys.exit(app.exec())

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window")
        self.setWindowIcon(QIcon("qt.png"))
        #self.setFixedHeight(200)
        #self.setFixedWidth(200)
        self.setGeometry(500,500,500,500)
        self.setStyleSheet("background-color:red")


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())

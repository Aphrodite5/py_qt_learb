from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(1300, 800, 1300, 800)

    def create_stuff(self):
        btn = QPushButton("start", self)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
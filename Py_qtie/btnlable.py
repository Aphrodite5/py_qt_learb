from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(1300, 800, 1300, 800)

class

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
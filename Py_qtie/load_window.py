from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("py.des.ui", self)

app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
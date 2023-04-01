from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Layouts")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500, 200, 500, 400)

        vbox = QVBoxLayout()
        btn = QPushButton("start")
        vbox.addWidget(btn)
        self.setLayout(vbox)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Layouts")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500, 200, 500, 400)

        grid = QGridLayout()
        btn0 = QPushButton("start")
        btn1 = QPushButton("stop")
        btn2 = QPushButton("resume")
        btn3 = QPushButton("pause")
        grid.addWidget(btn0, 0, 0)
        grid.addWidget(btn1, 0, 2)
        grid.addWidget(btn2, 1, 2)
        grid.addWidget(btn3, 0, 3)
        self.setLayout(grid)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500, 500, 500, 500)
        self.create_stuff()
    def create_stuff(self):
        btn = QPushButton("start", self)
        btn.setGeometry(100, 100, 100, 100)
        btn.setStyleSheet("background-color: red")
        btn.setIcon(QIcon("football.png"))
        btn.setFont(QFont("Time New Roman", 15))

        lable = QLabel("button", self)
        lable.move(100, 200)
        lable.setStyleSheet("color.green")
        lable.setFont(QFont("console",15))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(600, 600, 600, 600)
        self.create_stuff()

    def create_stuff(self):
        btn = QPushButton("start", self)
        btn.setGeometry(100, 100, 100, 100)
        btn.setStyleSheet("background-color: red")
        btn.setIcon(QIcon("football.png"))
        btn.setFont(QFont("Time New Roman", 15))
        btn.clicked.connect(self.clicked_btn)

        self.lable = QLabel("button", self)
        self.lable.setGeometry(200, 320, 300, 200)
        self.lable.setStyleSheet("color.green")
        self.lable.setFont(QFont("console", 15))

    def clicked_btn(self):
        self.lable.setText("The text has been changed")
        self.lable.setStyleSheet("background-color: white")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

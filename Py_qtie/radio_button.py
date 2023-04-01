from PyQt5.QtWidgets import  QApplication, QWidget, QVBoxLayout, QGroupBox
from PyQt5.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RadioButton")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500, 200, 500, 400)

        self.radio_btn()
        vbox = QVBoxLayout()
        vbox.addWidget(self.grpbox)

        self.setLayout(vbox)


    def radio_btn(self):
        self.grpbox = QGroupBox("Choose programming language")
        self.grpbox.setFont(QFont("Time New Roman", 15))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import sys
import numpy as np


class Graphs(FigureCanvasQTAgg):
    def __init__(self, width, height, dpi) -> None:
        self.Fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.Fig.add_subplot(111)
        super().__init__(self.Fig)

    def clear(self) -> None:
        self.ax.clear()

    def set(self, xmin, xmax, ymin, ymax) -> None:
        self.ax.set_xlim(xmin, xmax)
        self.ax.set_ylim(ymin, ymax)

    def tocenter(self) -> None:
        self.ax.spines['right'].set_color('none')
        self.ax.spines['left'].set_position('center')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['bottom'].set_position('center')

    def toside(self) -> None:
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')

    def plot(self, func, *args):
        func(self.ax, *args)
        self.Fig.canvas.draw()
        self.Fig.canvas.flush_events()


class QtGraphs(Graphs):
    def __init__(self, root, width, height, dpi):
        super().__init__(width, height, dpi)
        self.root = root

    def place(self):
        self.root.addWidget(self)


class QtBase:
    def unpack(self, keys, func, *args):
        check = True
        result = []
        for arg in args:
            if arg in keys:
                result.append(keys[arg])
                keys.pop(arg)
            else:
                check = False
                break
        if (check):
            func(*result)

    def setsize(self, x, y, w, h):
        self.setGeometry(QtCore.QRect(x, y, w, h))

    def setfsize(self, size):
        self.setFont(QtGui.QFont('', size))

    def place(self, **keys):
        if 'parent' in keys:
            self.setParent(keys['parent'])
            return
        if 'label' in keys:
            self.setLayout(keys['label'])
            return
        print('place:invalid args ', keys)

    def catch(self, keys):
        if len(keys) != 0:
            print('catch:invalid args ', keys)


class vLayout(QtWidgets.QVBoxLayout, QtBase):
    def __init__(self, *arg, **keys):
        super().__init__(*arg)
        self.unpack(keys, self.setsize, 'x', 'y', 'w', 'h')
        self.unpack(keys, self.setSpacing, 'spacing')
        self.catch(keys)

    def place(self, **keys):
        if 'parent' in keys:
            self.setParent(keys['parent'])
            return
        if 'label' in keys:
            self.addLayout(keys['label'])
            return
        if 'widget' in keys:
            self.addWidget(keys['widget'])
            return
        print('place:invalid args ', keys)


class ScrollArea(QtWidgets.QScrollArea, QtBase):
    def __init__(self, *arg, **keys):
        super().__init__(*arg)
        self.unpack(keys, self.setsize, 'x', 'y', 'w', 'h')
        self.catch(keys)

    def place(self, **keys):
        if 'parent' in keys:
            self.setParent(keys['parent'])
            return
        if 'label' in keys:
            self.setLayout(keys['label'])
            return
        if 'widget' in keys:
            self.setWidget(keys['widget'])
            return
        print('place:invalid args ', keys)


class Frame(QtWidgets.QFrame, QtBase):
    def __init__(self, *arg, **keys):
        super().__init__(*arg)
        self.unpack(keys, self.setsize, 'x', 'y', 'w', 'h')
        self.catch(keys)


class Button(QtWidgets.QPushButton, QtBase):
    def __init__(self, *arg, **keys):
        super().__init__(*arg)
        self.unpack(keys, self.setsize, 'x', 'y', 'w', 'h')
        self.unpack(keys, self.setText, 'text')
        self.unpack(keys, self.setfsize, 'font')
        self.unpack(keys, self.clicked.connect, 'cmd')
        self.catch(keys)


class Groupbox(QtWidgets.QGroupBox, QtBase):
    def __init__(self, *arg, **keys):
        super().__init__(*arg)
        self.unpack(keys, self.setsize, 'x', 'y', 'w', 'h')
        self.unpack(keys, self.setTitle, 'text')
        self.catch(keys)


class Entry(QtWidgets.QLineEdit, QtBase):
    def __init__(self, *arg, **keys):
        super().__init__(*arg)
        self.unpack(keys, self.setsize, 'x', 'y', 'w', 'h')
        self.unpack(keys, self.setText, 'text')
        self.unpack(keys, self.setfsize, 'font')
        self.unpack(keys, self.setValidator, 'validate')
        self.unpack(keys, self.editingFinished.connect, 'cmd')
        self.catch(keys)


class Widget(QtWidgets.QWidget, QtBase):
    def __init__(self, *arg, **keys):
        super().__init__(*arg)
        self.unpack(keys, self.setsize, 'x', 'y', 'w', 'h')
        self.catch(keys)


def func():
    print('pressed')


app = QtWidgets.QApplication(sys.argv)
root = QtWidgets.QMainWindow()
root.resize(700, 600)
window = QtWidgets.QWidget()

frame1 = Frame(x=0, y=0, w=372, h=10 + 10 * 211)
frame1.place(parent=window)

for i in range(10):
    frame2 = Frame(x=0, y=10 + i * 211, w=383, h=201)
    frame2.place(parent=frame1)
    frame2.setStyleSheet('background-color:red')
    frame3 = Frame(x=0, y=0, w=201, h=201)
    frame3.place(parent=frame2)
    frame3.setStyleSheet('background-color:blue')

frame2.deleteLater()
frame1.setGeometry(0, 0, 372, 10 + 9 * 211)

scroll = ScrollArea(x=10, y=10, w=391, h=432)

scroll.place(parent=window)

scroll.place(widget=frame1)

root.setCentralWidget(window)
root.show()

sys.exit(app.exec_())

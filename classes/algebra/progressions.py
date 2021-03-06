from modules import *
from classes.algebra.progressions__.arithmetic import Arithmetic
from classes.algebra.progressions__.geometric import Geometric

class Progressions(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Прогрессии")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        button = QPushButton("Сумма арифметической прогрессии", self)
        button.setGeometry(QRect(250, 120, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Arithmetic))

        button = QPushButton("Сумма геометрической прогрессии", self)
        button.setGeometry(QRect(250, 220, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Geometric))

    def open_parent_window(self):
        self.parent_window.show()
        self.close()

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()
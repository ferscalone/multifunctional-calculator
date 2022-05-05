from modules import *
from classes.algebra.average_values__.quadr import Quadr
from classes.algebra.average_values__.arithm import Arithm
from classes.algebra.average_values__.geom import Geom
from classes.algebra.average_values__.harmon import Harmon

class Average_Values(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Средние величины")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        button = QPushButton("Среднее квадратическое", self)
        button.setGeometry(QRect(250, 120, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Quadr))

        button = QPushButton("Среднее арифметическое", self)
        button.setGeometry(QRect(250, 220, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Arithm))

        button = QPushButton("Среднее геометрическое", self)
        button.setGeometry(QRect(250, 320, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Geom))

        button = QPushButton("Среднее гармоническое", self)
        button.setGeometry(QRect(250, 420, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Harmon))

    def open_parent_window(self):
        self.parent_window.show()
        self.close()

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()
from modules import *
from classes.algebra.average_values import Average_Values
from classes.algebra.arithmetic import Arithmetic
from classes.algebra.equations import Equations
from classes.algebra.progressions import Progressions
from classes.algebra.combinatorics import Combinatorics
from classes.algebra.calculus import Calculus
from classes.algebra.graphic import Graphic

class Algebra(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Алгебра")
        self.resize(910, 850)

        menu_button = QPushButton("Меню", self)
        menu_button.setGeometry(QRect(250, 20, 280, 100))
        menu_button.clicked.connect(self.open_parent_window)

        average_values_button = QPushButton("Средние величины", self)
        average_values_button.setGeometry(QRect(250, 120, 280, 100))
        average_values_button.clicked.connect(lambda: self.open_sub_window(Average_Values))

        arithmetic_button = QPushButton("Арифметика", self)
        arithmetic_button.setGeometry(QRect(250, 220, 280, 100))
        arithmetic_button.clicked.connect(lambda: self.open_sub_window(Arithmetic))

        equations_button = QPushButton("Уравнения и неравенства", self)
        equations_button.setGeometry(QRect(250, 320, 280, 100))
        equations_button.clicked.connect(lambda: self.open_sub_window(Equations))

        progressions_button = QPushButton("Прогрессии", self)
        progressions_button.setGeometry(QRect(250, 420, 280, 100))
        progressions_button.clicked.connect(lambda: self.open_sub_window(Progressions))

        combinatorics_button = QPushButton("Комбинаторика", self)
        combinatorics_button.setGeometry(QRect(250, 520, 280, 100))
        combinatorics_button.clicked.connect(lambda: self.open_sub_window(Combinatorics))

        """calculus_button = QPushButton("Немного из матанализа", self)
        calculus_button.setGeometry(QRect(530, 120, 280, 100))
        calculus_button.clicked.connect(lambda: self.open_sub_window(Calculus))

        graphic_button = QPushButton("Построение графика функции", self)
        graphic_button.setGeometry(QRect(530, 220, 280, 100))
        graphic_button.clicked.connect(lambda: self.open_sub_window(Graphic))"""

    def open_parent_window(self):
        self.parent_window.show()
        self.close()

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()
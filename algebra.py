from modules import *
from functions.algebra.quadratic_equations import Quadratic_Equations

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

        quadratic_equations_button = QPushButton("Квадратные уравнения", self)
        quadratic_equations_button.setGeometry(QRect(250, 120, 280, 100))
        quadratic_equations_button.clicked.connect(lambda: self.open_sub_window(Quadratic_Equations))

        quadratic_equations_button = QPushButton("Средние величины", self)
        quadratic_equations_button.setGeometry(QRect(250, 120, 280, 100))
        quadratic_equations_button.clicked.connect(lambda: self.open_sub_window(Average_Values))

        quadratic_equations_button = QPushButton("Арифметика", self)
        quadratic_equations_button.setGeometry(QRect(250, 120, 280, 100))
        quadratic_equations_button.clicked.connect(lambda: self.open_sub_window(Arithmetic))

        quadratic_equations_button = QPushButton("Уравнения", self)
        quadratic_equations_button.setGeometry(QRect(250, 120, 280, 100))
        quadratic_equations_button.clicked.connect(lambda: self.open_sub_window(Equations))

        quadratic_equations_button = QPushButton("Прогрессии", self)
        quadratic_equations_button.setGeometry(QRect(250, 120, 280, 100))
        quadratic_equations_button.clicked.connect(lambda: self.open_sub_window(Progressions))

        quadratic_equations_button = QPushButton("Комбинаторика", self)
        quadratic_equations_button.setGeometry(QRect(250, 120, 280, 100))
        quadratic_equations_button.clicked.connect(lambda: self.open_sub_window(Combinatorics))

    def open_parent_window(self):
        self.parent_window.show()
        self.close()

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()
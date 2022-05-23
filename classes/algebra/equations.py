from modules import *
from classes.algebra.equations__.quadratic_equations import Quadratic_Equations
from classes.algebra.equations__.biquadratic import Biquadratic
from classes.algebra.equations__.linear_equation import Linear
from classes.algebra.equations__.cubic_equation import Cubic_Equation
from classes.algebra.equations__.system_of_linear_equations import System
from classes.algebra.equations__.inequalities import Inequalities

class Equations(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Уравнения")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        quadratic_equations_button = QPushButton("Квадратные уравнения", self)
        quadratic_equations_button.setGeometry(QRect(250, 120, 280, 100))
        quadratic_equations_button.clicked.connect(lambda: self.open_sub_window(Quadratic_Equations))

        button = QPushButton("Биквадратные уравнения", self)
        button.setGeometry(QRect(250, 220, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Biquadratic))

        button = QPushButton("Линейные уравнения", self)
        button.setGeometry(QRect(250, 320, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Linear))

        button = QPushButton("Кубические уравнения", self)
        button.setGeometry(QRect(250, 420, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Cubic_Equation))

        """button = QPushButton("Система линейных уравнений", self)
        button.setGeometry(QRect(250, 520, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(System))

        button = QPushButton("Неравенства", self)
        button.setGeometry(QRect(530, 120, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Inequalities))"""

    def open_parent_window(self):
        self.parent_window.show()
        self.close()

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()
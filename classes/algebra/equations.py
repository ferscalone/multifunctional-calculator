from modules import *
from classes.algebra.equations__.quadratic_equations import Quadratic_Equations

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

    def open_parent_window(self):
        self.parent_window.show()
        self.close()

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()
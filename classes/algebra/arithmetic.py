from modules import *
from classes.algebra.arithmetic__.gcd_and_lmn import GCD_and_LMN
from classes.algebra.arithmetic__.simplicity_and_factorization import Simplicity_And_Factorization
from classes.algebra.arithmetic__.exponentiation import Exponentiation
from classes.algebra.arithmetic__.root_extraction import Root_Extraction

class Arithmetic(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Арифметика")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        button = QPushButton("НОД и НОК", self)
        button.setGeometry(QRect(250, 120, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(GCD_and_LMN))

        button = QPushButton("Проверка числа на простоту и его факторизация", self)
        button.setGeometry(QRect(250, 220, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Simplicity_And_Factorization))

        button = QPushButton("Возведение в степень", self)
        button.setGeometry(QRect(250, 320, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Exponentiation))

        button = QPushButton("Извлечение корня", self)
        button.setGeometry(QRect(250, 420, 280, 100))
        button.clicked.connect(lambda: self.open_sub_window(Root_Extraction))

    def open_parent_window(self):
        self.parent_window.show()
        self.close()

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()
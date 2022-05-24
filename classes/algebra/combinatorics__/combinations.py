import math

from modules import *


class Combinations(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Сочетания")
        self.resize(910, 850)

        x_2_pixmap = QPixmap("./images/soch.jpg")
        x_pixmap = QPixmap("./images/sochet.jpg")

        x_2 = QLabel(self)
        x = QLabel(self)
        plus1 = QLabel(self)
        plus2 = QLabel(self)

        x_2.setGeometry(QRect(50, 190, 1000, 500))
        x.setGeometry(QRect(400, 100, 500, 200))
        plus1.setGeometry(QRect(70, 190, 50, 50))
        plus2.setGeometry(QRect(150, 190, 50, 50))

        x_2.setPixmap(x_2_pixmap)
        x.setPixmap(x_pixmap)
        plus1.setText("n: ")
        plus2.setText("k: ")

        display_solution_button = QPushButton("Показать количество сочетаний из n элементов по k", self)
        display_solution_button.setGeometry(QRect(530, 20, 280, 100))
        display_solution_button.clicked.connect(self.display_solution)

        self.b_argument = QLineEdit(self)
        self.b_argument.setGeometry(QRect(90, 190, 50, 50))
        self.b_argument.setValidator(QIntValidator(1, 1000000000, self))

        self.c_argument = QLineEdit(self)
        self.c_argument.setGeometry(QRect(170, 190, 50, 50))
        self.c_argument.setValidator(QIntValidator(1, 1000000000, self))

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        self.svg = QSvgWidget(self)
        self.svg.setGeometry(QRect(10, 10, 100, 50))

    def display_solution(self):
        if self.b_argument.text() != '' and int(self.b_argument.text()) != 0 and self.c_argument.text() != '':
            n = int(self.b_argument.text())
            k = int(self.c_argument.text())
            self.svg.load(tex2svg(latex(math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))))
            self.svg.show()

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
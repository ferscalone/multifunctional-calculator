from modules import *


class Arithmetic(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Cумма n первых членов арифметической прогрессии")
        self.resize(910, 850)

        self.a_argument = QLineEdit(self)
        self.a_argument.setGeometry(QRect(0, 190, 50, 50))
        self.a_argument.setValidator(QIntValidator(-1000000000, 1000000000, self))

        self.b_argument = QLineEdit(self)
        self.b_argument.setGeometry(QRect(90, 190, 50, 50))
        self.b_argument.setValidator(QIntValidator(-1000000000, 1000000000, self))

        self.c_argument = QLineEdit(self)
        self.c_argument.setGeometry(QRect(170, 190, 50, 50))
        self.c_argument.setValidator(QIntValidator(-1000000000, 1000000000, self))

        self.svg_1 = QSvgWidget(self)
        self.svg_1.setGeometry(QRect(10, 10, 200, 100))

        a_label = QLabel("a1", self)
        a_label.setGeometry(QRect(10, 130, 50, 100))

        b_label = QLabel("d", self)
        b_label.setGeometry(QRect(100, 130, 50, 100))

        c_label = QLabel("n", self)
        c_label.setGeometry(QRect(180, 130, 50, 100))

        display_solution_button = QPushButton("Показать сумму", self)
        display_solution_button.setGeometry(QRect(250, 130, 280, 100))
        display_solution_button.clicked.connect(self.display_solution)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

    def display_solution(self):
        if self.a_argument.text() != '' and self.b_argument.text() != '' and self.c_argument.text() != '':
            a1 = int(self.a_argument.text())
            d = int(self.b_argument.text())
            n = int(self.c_argument.text())
            self.svg_1.load(tex2svg(latex(a1*n + (d*n*(n-1))/2)))
            self.svg_1.show()

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
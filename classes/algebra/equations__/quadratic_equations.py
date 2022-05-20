from modules import *


class Quadratic_Equations(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Квадратные уравнения")
        self.resize(910, 850)

        x_2_pixmap = QPixmap("./images/x^2.svg")
        x_2 = QLabel(self)
        x_2.setGeometry(QRect(0, 190, 50, 50))
        x_2.setPixmap(x_2_pixmap)

        display_solution_button = QPushButton("Показать решение", self)
        display_solution_button.setGeometry(QRect(250, 130, 280, 100))
        display_solution_button.clicked.connect(self.display_solution)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        a_label = QLabel("a", self)
        a_label.setGeometry(QRect(50, 130, 50, 100))

        b_label = QLabel("b", self)
        b_label.setGeometry(QRect(100, 130, 50, 100))

        c_label = QLabel("c", self)
        c_label.setGeometry(QRect(150, 130, 50, 100))

        self.solution_label = QLabel(self)
        self.solution_label.setGeometry(QRect(50, 50, 500, 100))

        self.a_argument = QLineEdit(self)
        self.a_argument.setGeometry(QRect(25, 190, 50, 50))
        self.a_argument.setValidator(QIntValidator(1, 1000000000, self))

        self.b_argument = QLineEdit(self)
        self.b_argument.setGeometry(QRect(75, 190, 50, 50))
        self.b_argument.setValidator(QIntValidator(1, 1000000000, self))

        self.c_argument = QLineEdit(self) 
        self.c_argument.setGeometry(QRect(125, 190, 50, 50))
        self.c_argument.setValidator(QIntValidator(1, 1000000000, self))
        
        self.svg_1 = QSvgWidget(self)
        self.svg_1.setGeometry(QRect(10, 10, 100, 50))

        self.svg_2 = QSvgWidget(self)
        self.svg_2.setGeometry(QRect(10, 110, 100, 50))

    def display_solution(self):
        if self.a_argument.text() != '' and self.b_argument.text() != '' and self.c_argument.text() != '':
            a = int(self.a_argument.text())
            b = int(self.b_argument.text())
            c = int(self.c_argument.text())

            D = b ** 2 - 4 * a * c
            if D < 0:
                self.svg_1.close()
                self.svg_2.close()
                self.solution_label.setText("РЕШЕНИЙ НЕТ")
                self.solution_label.show()

            elif D == 0:
                solution = sympy.simplify(-b / (2 * a))
                self.svg_2.close()
                self.solution_label.close()
                self.svg_1.load(tex2svg(latex(solution)))
                self.svg_1.show()

            else:
                solution_1 = sympy.simplify((-b + sympy.sqrt(D)) / (2 * a))
                solution_2 = sympy.simplify((-b - sympy.sqrt(D)) / (2 * a))
                self.solution_label.close()
                self.svg_1.load(tex2svg(latex(solution_1)))
                self.svg_1.show()
                self.svg_2.load(tex2svg(latex(solution_2)))
                self.svg_2.show()

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
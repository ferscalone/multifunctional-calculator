from modules import *

class Biquadratic(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Биквадратные уравнения")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        display_solution_button = QPushButton("Показать решение", self)
        display_solution_button.setGeometry(QRect(250, 130, 280, 100))
        display_solution_button.clicked.connect(self.display_solution)

        self.solution_label = QLabel(self)
        self.solution_label.setGeometry(QRect(50, 50, 500, 100))

        self.a_argument = QLineEdit(self)
        self.a_argument.setGeometry(QRect(25, 190, 50, 50))
        self.a_argument.setValidator(QIntValidator(-1000000000, 1000000000, self))

        self.b_argument = QLineEdit(self)
        self.b_argument.setGeometry(QRect(75, 190, 50, 50))
        self.b_argument.setValidator(QIntValidator(-1000000000, 1000000000, self))

        self.c_argument = QLineEdit(self)
        self.c_argument.setGeometry(QRect(125, 190, 50, 50))
        self.c_argument.setValidator(QIntValidator(-1000000000, 1000000000, self))

        self.svg_1 = QSvgWidget(self)
        self.svg_1.setGeometry(QRect(10, 10, 100, 50))

        self.svg_2 = QSvgWidget(self)
        self.svg_2.setGeometry(QRect(10, 60, 100, 50))

        self.svg_3 = QSvgWidget(self)
        self.svg_3.setGeometry(QRect(110, 10, 100, 50))

        self.svg_4 = QSvgWidget(self)
        self.svg_4.setGeometry(QRect(110, 60, 100, 50))

    def display_solution(self):
        if self.a_argument.text() != '' and self.a_argument.text() != '0' and self.b_argument.text() != '' and self.c_argument.text() != '':
            a = int(self.a_argument.text())
            b = int(self.b_argument.text())
            c = int(self.c_argument.text())

            D = b ** 2 - 4 * a * c
            if D < 0:
                self.svg_1.close()
                self.svg_2.close()
                self.svg_3.close()
                self.svg_4.close()
                self.solution_label.setText("РЕШЕНИЙ НЕТ")
                self.solution_label.show()

            elif D == 0:
                """solution = sympy.simplify(-b / (2 * a))"""
                t = -b/(2*a)
                self.svg_3.close()
                self.svg_4.close()
                if t >= 0:
                    x1 = -sympy.sqrt(t)
                    x2 = sympy.sqrt(t)
                    self.solution_label.close()
                    self.svg_1.load(tex2svg(latex(x1)))
                    self.svg_2.load(tex2svg(latex(x2)))
                    self.svg_1.show()
                    self.svg_2.show()
                else:
                    self.svg_1.close()
                    self.svg_2.close()
                    self.solution_label.setText("РЕШЕНИЙ НЕТ")
                    self.solution_label.show()

            else:
                t_11 = sympy.simplify((-b + sympy.sqrt(D)) / (2 * a))
                t_22 = sympy.simplify((-b - sympy.sqrt(D)) / (2 * a))
                """t_11 = (-b + math.sqrt(D)) / (2 * a)
                t_22 = (-b - math.sqrt(D)) / (2 * a)"""

                if t_11 >= 0 and t_22 >= 0:
                    x1 = -sympy.sqrt(t_11)
                    x2 = sympy.sqrt(t_11)
                    x3 = -sympy.sqrt(t_22)
                    x4 = sympy.sqrt(t_22)
                    self.solution_label.close()
                    self.svg_1.load(tex2svg(latex(x1)))
                    self.svg_2.load(tex2svg(latex(x2)))
                    self.svg_3.load(tex2svg(latex(x3)))
                    self.svg_4.load(tex2svg(latex(x4)))
                    self.svg_1.show()
                    self.svg_2.show()
                    self.svg_3.show()
                    self.svg_4.show()

                if t_22 >= 0 and t_11 < 0:
                    x1 = -sympy.sqrt(t_22)
                    x2 = sympy.sqrt(t_22)
                    self.solution_label.close()
                    self.svg_1.load(tex2svg(latex(x1)))
                    self.svg_2.load(tex2svg(latex(x2)))
                    self.svg_3.close()
                    self.svg_4.close()
                    self.svg_1.show()
                    self.svg_2.show()

                if t_11 >= 0 and t_22 < 0:
                    x1 = -sympy.sqrt(t_11)
                    x2 = sympy.sqrt(t_11)
                    self.solution_label.close()
                    self.svg_1.load(tex2svg(latex(x1)))
                    self.svg_2.load(tex2svg(latex(x2)))
                    self.svg_3.close()
                    self.svg_4.close()
                    self.svg_1.show()
                    self.svg_2.show()

                if t_22 < 0 and t_11 < 0:
                    self.svg_1.close()
                    self.svg_2.close()
                    self.svg_3.close()
                    self.svg_4.close()
                    self.solution_label.setText("РЕШЕНИЙ НЕТ")
                    self.solution_label.show()

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
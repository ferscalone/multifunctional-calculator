from modules import *

class Linear(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Линейные уравнения")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        x_pixmap = QPixmap("./images/x.svg")
        plus_pixmap = QPixmap("./images/plus.svg")
        eq_pixmap = QPixmap("./images/eq.svg")

        x = QLabel(self)
        plus = QLabel(self)
        eq = QLabel(self)

        x.setGeometry(QRect(50, 190, 50, 50))
        eq.setGeometry(QRect(140, 190, 50, 50))
        plus.setGeometry(QRect(70, 190, 50, 50))

        x.setPixmap(x_pixmap)
        plus.setPixmap(plus_pixmap)
        eq.setPixmap(eq_pixmap)

        display_solution_button = QPushButton("Показать решение", self)
        display_solution_button.setGeometry(QRect(250, 130, 280, 100))
        display_solution_button.clicked.connect(self.display_solution)

        self.solution_label = QLabel(self)
        self.solution_label.setGeometry(QRect(50, 50, 500, 100))

        self.a_argument = QLineEdit(self)
        self.a_argument.setGeometry(QRect(0, 190, 50, 50))
        self.a_argument.setValidator(QIntValidator(-1000000000, 1000000000, self))

        self.b_argument = QLineEdit(self)
        self.b_argument.setGeometry(QRect(90, 190, 50, 50))
        self.b_argument.setValidator(QIntValidator(-1000000000, 1000000000, self))

        self.c_argument = QLineEdit(self)
        self.c_argument.setGeometry(QRect(170, 190, 50, 50))
        self.c_argument.setValidator(QIntValidator(-1000000000, 1000000000, self))

        self.svg = QSvgWidget(self)
        self.svg.setGeometry(QRect(10, 10, 100, 50))

    def display_solution(self):
        if self.a_argument.text() != '' and int(self.a_argument.text()) != 0 and self.b_argument.text() != '' and self.c_argument.text() != '':
            a = int(self.a_argument.text())
            b = int(self.b_argument.text())
            c = int(self.c_argument.text())
            self.svg.load(tex2svg(latex((c-b)/a)))
            self.svg.show()

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
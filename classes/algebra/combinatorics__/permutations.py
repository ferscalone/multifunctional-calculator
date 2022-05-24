from modules import *


class Permutations(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Перестановки")
        self.resize(910, 850)

        plus1 = QLabel(self)
        plus1.setGeometry(QRect(70, 190, 50, 50))
        plus1.setText("n: ")

        x_2_pixmap = QPixmap("./images/perest.jpg")
        x_2 = QLabel(self)
        x_2.setGeometry(QRect(50, 190, 1000, 500))
        x_2.setPixmap(x_2_pixmap)

        display_solution_button = QPushButton("Показать количество перестановок из n элементов", self)
        display_solution_button.setGeometry(QRect(530, 20, 280, 100))
        display_solution_button.clicked.connect(self.display_solution)

        self.b_argument = QLineEdit(self)
        self.b_argument.setGeometry(QRect(90, 190, 50, 50))
        self.b_argument.setValidator(QIntValidator(1, 1000000000, self))

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        self.svg = QSvgWidget(self)
        self.svg.setGeometry(QRect(10, 10, 200, 100))

    def display_solution(self):
        if self.b_argument.text() != '':
            n = int(self.b_argument.text())
            self.svg.load(tex2svg(latex(math.factorial(n))))
            self.svg.show()

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
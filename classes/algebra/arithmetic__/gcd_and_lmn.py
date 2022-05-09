from modules import *


class GCD_and_LMN(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("НОД и НОК")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        self.a_argument = QLineEdit(self)
        self.a_argument.setGeometry(QRect(25, 190, 50, 50))
        self.a_argument.setValidator(QIntValidator(1, 1000000000, self))

        self.b_argument = QLineEdit(self)
        self.b_argument.setGeometry(QRect(75, 190, 50, 50))
        self.b_argument.setValidator(QIntValidator(1, 1000000000, self))

        gcd_button = QPushButton("НОД", self)
        gcd_button.setGeometry(QRect(250, 130, 280, 100))
        gcd_button.clicked.connect(self.gcd)

        lmn_button = QPushButton("НОК", self)
        lmn_button.setGeometry(QRect(250, 230, 280, 100))
        lmn_button.clicked.connect(self.lmn)

        self.svg_gcd = QSvgWidget(self)
        self.svg_gcd.setGeometry(QRect(530, 150, 100, 50))

        self.svg_lmn = QSvgWidget(self)
        self.svg_lmn.setGeometry(QRect(530, 250, 100, 50))

    def gcd(self):
        if self.a_argument.text() != '' and self.b_argument.text() != '':
            a = int(self.a_argument.text())
            b = int(self.b_argument.text())
            self.svg_gcd.load(tex2svg(latex(sympy.gcd(a, b))))
    def lmn(self):
        if self.a_argument.text() != '' and self.b_argument.text() != '':
            a = int(self.a_argument.text())
            b = int(self.b_argument.text())
            self.svg_lmn.load(tex2svg(latex(a*b/sympy.gcd(a, b))))

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
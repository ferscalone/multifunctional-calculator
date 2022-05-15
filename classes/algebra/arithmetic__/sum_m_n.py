from modules import *


class Sum_M_N(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Сумма натуральных чисел от m до n")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        self.m = QLineEdit(self)
        self.m.setGeometry(QRect(25, 190, 50, 50))
        self.m.setValidator(QIntValidator(1, 1000000000))

        self.n = QLineEdit(self)
        self.n.setGeometry(QRect(75, 190, 50, 50))
        self.n.setValidator(QIntValidator(1, 1000000000))

        root_button = QPushButton("Сумма чисел от m до n", self)
        root_button.setGeometry(QRect(250, 130, 280, 100))
        root_button.clicked.connect(self.root)

        self.svg_root = QSvgWidget(self)
        self.svg_root.setGeometry(QRect(530, 150, 100, 20))

    def root(self):
        if self.m.text() != '' and self.n.text() != '':
            m = int(self.m.text())
            n = int(self.n.text())
            if m <= n:
                self.svg_root.load(tex2svg(latex(int((m+n)*(n-m+1)/2))))
            else:
                self.svg_root.load(tex2svg(latex(int((m + n) * (m - n + 1) / 2))))

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
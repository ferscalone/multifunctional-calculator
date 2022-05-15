from modules import *


class Exponentiation(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Возведение в степень")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        self.a = QLineEdit(self)
        self.a.setGeometry(QRect(25, 190, 50, 50))
        self.a.setValidator(QDoubleValidator(0.0, 1000000000.0, 6))

        self.b = QLineEdit(self)
        self.b.setGeometry(QRect(75, 190, 50, 50))
        self.b.setValidator(QDoubleValidator(0.0, 1000000000.0, 6))

        root_button = QPushButton("Показать степень (сначала возводимое число, потом степень)", self)
        root_button.setGeometry(QRect(250, 130, 280, 100))
        root_button.clicked.connect(self.root)

        self.svg_root = QSvgWidget(self)
        self.svg_root.setGeometry(QRect(530, 150, 100, 20))

    def root(self):
        if self.a.text() != '' and self.b.text() != '':
            a = self.a.text()
            b = self.b.text()
            a = a.replace(",", ".")
            b = b.replace(",", ".")
            a = float(a)
            b = float(b)
            self.svg_root.load(tex2svg(latex(a**b)))

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
from modules import *

class Informatics(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Информатика")
        self.resize(910, 850)

        menu_button = QPushButton("В меню", self)
        menu_button.setGeometry(QRect(250, 20, 280, 100))
        menu_button.clicked.connect(self.open_parent_window)

        binary_calculator_button = QPushButton("Двоичный калькулятор", self)
        binary_calculator_button.setGeometry(QRect(250, 120, 280, 100))
        binary_calculator_button.clicked.connect(lambda: self.open_sub_window(Binary_Calculator))

        translation_of_number_systems_button = QPushButton("Перевод систем счисления", self)
        translation_of_number_systems_button.setGeometry(QRect(250, 220, 280, 100))
        translation_of_number_systems_button.clicked.connect(lambda: self.open_sub_window(Translation_Of_Number_Systems))

    def open_parent_window(self):
        self.parent_window.show()
        self.close()

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()


class Binary_Calculator(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Двоичный калькулятор")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

    def open_parent_window(self):
        self.parent_window.show()
        self.close()


class Translation_Of_Number_Systems(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Перевод систем счисления")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
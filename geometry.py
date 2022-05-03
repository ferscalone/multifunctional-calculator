from modules import *

class Geometry(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Геометрия")
        self.resize(910, 850)

        menu_button = QPushButton("В меню", self)
        menu_button.setGeometry(QRect(250, 20, 280, 100))
        menu_button.clicked.connect(self.open_parent_window)

        squares_of_figures_button = QPushButton("Площади фигур", self)
        squares_of_figures_button.setGeometry(QRect(250, 130, 280, 100))
        squares_of_figures_button.clicked.connect(lambda: self.open_sub_window(Squares_Of_Figures))

    def open_parent_window(self):
        self.parent_window.show()
        self.close()

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()


class Squares_Of_Figures(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Площади фигур")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
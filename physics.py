from modules import *

class Physics(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Физика")
        self.resize(910, 850)

        menu_button = QPushButton("В меню", self)
        menu_button.setGeometry(QRect(250, 20, 280, 100))
        menu_button.clicked.connect(self.open_parent_window)

    def open_parent_window(self):
        self.parent_window.show()
        self.close()

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()
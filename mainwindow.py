from modules import *
from algebra import Algebra
from geometry import Geometry
from trigonometry import Trigonometry
from informatics import Informatics
from physics import Physics

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("The решатор")
        self.resize(910, 850)

        algebra_button = QPushButton("Алгебра", self)
        algebra_button.setGeometry(QRect(250, 130, 280, 100))
        algebra_button.clicked.connect(lambda: self.open_sub_window(Algebra))

        geometry_button = QPushButton("Геометрия", self)
        geometry_button.setGeometry(QRect(250, 230, 280, 100))
        geometry_button.clicked.connect(lambda: self.open_sub_window(Geometry))

        trigonometry_button = QPushButton("Тригонометрические функции", self)
        trigonometry_button.setGeometry(QRect(250, 330, 280, 100))
        trigonometry_button.clicked.connect(lambda: self.open_sub_window(Trigonometry))

        informatics_button = QPushButton("Информатика", self)
        informatics_button.setGeometry(QRect(250, 430, 280, 100))
        informatics_button.clicked.connect(lambda: self.open_sub_window(Informatics))

        physics_button = QPushButton("Физика", self)
        physics_button.setGeometry(QRect(250, 530, 280, 100))
        physics_button.clicked.connect(lambda: self.open_sub_window(Physics))

        menu_label = QLabel("Меню", self)
        menu_label.setGeometry(QRect(250, 60, 50, 100))

        font = QFont()
        font.setPointSize(13)
        self.setFont(font)

    def open_sub_window(self, window_type):
        self.sub_window = window_type(self)
        self.sub_window.show()
        self.close()
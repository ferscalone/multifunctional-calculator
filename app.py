from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sympy
from PyQt5.QtSvg import QSvgWidget
from sympy.printing.latex import latex
from tex2svg import tex2svg

#I. Главное окно
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("The решатор")
        self.resize(910, 850)
        #self.move(300, 300)

        font = QFont()
        font.setPointSize(13)

        self.btn = QPushButton("Квадратные уравнения", self)
        self.btn.setGeometry(QRect(250, 130, 280, 100))
        self.btn.clicked.connect(self.open_quadratic_equation)

        self.btn = QPushButton("Тригонометрия", self)
        self.btn.setGeometry(QRect(250, 230, 280, 100))
        self.btn.clicked.connect(self.open_trigonometric)

        self.btn = QPushButton("Информатика", self)
        self.btn.setGeometry(QRect(250, 330, 280, 100))
        self.btn.clicked.connect(self.open_informatika)

        self.btn = QPushButton("Геометрия", self)
        self.btn.setGeometry(QRect(250, 430, 280, 100))
        self.btn.clicked.connect(self.open_geometry)

        self.btn = QPushButton("Комбинаторика", self)
        self.btn.setGeometry(QRect(250, 530, 280, 100))
        self.btn.clicked.connect(self.open_informatika)

        self.menu = QLabel("Меню", self)
        self.menu.setGeometry(QRect(250, 60, 50, 100))
        self.setFont(font)

    def open_quadratic_equation(self):
        self.qu_eq = QuadraticEquation()
        self.qu_eq.show()
        self.hide()

    def open_trigonometric(self):
        self.qu_eq = Trigonometric()
        self.qu_eq.show()
        self.hide()

    def open_informatika(self):
        self.qu_eq = Informatika()
        self.qu_eq.show()
        self.hide()

    def open_geometry(self):
        self.qu_eq = Geometry()
        self.qu_eq.show()
        self.hide()

#II. Наборы функций по темам (прописать остававшиеся большие темы с переходами)
class Geometry(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Геометрия")
        self.resize(910, 850)
        #self.move(300, 300)
        
        self.menu = QPushButton("В меню", self)
        self.menu.setGeometry(QRect(250, 20, 280, 100))
        self.menu.clicked.connect(self.go_mainwindow)

        self.btn = QPushButton("Площади фигур", self)
        self.btn.setGeometry(QRect(250, 130, 280, 100))
        self.btn.clicked.connect(self.open_informatika)

        self.btn = QPushButton("Объёмы фигур", self)
        self.btn.setGeometry(QRect(250, 230, 280, 100))
        self.btn.clicked.connect(self.open_informatika)

        self.btn = QPushButton("Элементы фигур", self)
        self.btn.setGeometry(QRect(250, 330, 280, 100))
        self.btn.clicked.connect(self.open_informatika)

        self.btn = QPushButton("Периметры фигур", self)
        self.btn.setGeometry(QRect(250, 430, 280, 100))
        self.btn.clicked.connect(self.open_informatika)

        self.btn = QPushButton("Теоремы", self)
        self.btn.setGeometry(QRect(250, 530, 280, 100))
        self.btn.clicked.connect(self.open_informatika)

    def go_mainwindow(self):
        self.mw = MainWindow()
        self.mw.show()
        self.hide()

    def open_informatika():
        pass

class Trigonometric(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Тригонометрические функции")
        self.resize(910, 850)
        #self.move(300, 300)

        self.menu = QPushButton("В меню", self)
        self.menu.setGeometry(QRect(250, 20, 280, 100))
        self.menu.clicked.connect(self.go_mainwindow)

    def go_mainwindow(self):
        self.mw = MainWindow()
        self.mw.show()
        self.hide()

class Informatika(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Информатика")
        self.resize(910, 850)
        #self.move(300, 300)
        
        self.menu = QPushButton("В меню", self)
        self.menu.setGeometry(QRect(250, 20, 280, 100))
        self.menu.clicked.connect(self.go_mainwindow)

        self.menu = QPushButton("Двоичный калькулятор", self)
        self.menu.setGeometry(QRect(250, 120, 280, 100))
        self.menu.clicked.connect(self.go_dvoich)

        self.menu = QPushButton("Перевод систем счисления", self)
        self.menu.setGeometry(QRect(250, 220, 280, 100))
        self.menu.clicked.connect(self.go_perevod)

    def go_mainwindow(self):
        self.mw = MainWindow()
        self.mw.show()
        self.hide()

    def go_dvoich(self):
        self.mw = Dvoich()
        self.mw.show()
        self.hide()

    def go_perevod(self):
        self.mw = Perevod()
        self.mw.show()
        self.hide()

#III. Реализуемые базовые функции (возможно некоторые будут включать ещё подклассы)

##Алгебра
class QuadraticEquation(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Квадратное уравнение")
        self.resize(910, 850)
        #self.move(300, 300)

        '''self.image = QLabel(self)
        self.image.setGeometry(QRect(0, 50, 50, 50))
        self.pixmap = QPixmap("images/download.svg")
        self.image.setPixmap(self.pixmap)'''

        self.btn = QPushButton("Отобразить решение", self)
        self.btn.setGeometry(QRect(250, 130, 280, 100))
        self.btn.clicked.connect(self.display)

        self.menu = QPushButton("В меню", self)
        self.menu.setGeometry(QRect(250, 20, 280, 100))
        self.menu.clicked.connect(self.go_mainwindow)

        self.label = QLabel(self)
        self.label.setGeometry(QRect(50, 50, 500, 100))

        self.a = QLabel("a", self)
        self.a.setGeometry(QRect(50, 130, 50, 100))

        self.b = QLabel("b", self)
        self.b.setGeometry(QRect(100, 130, 50, 100))

        self.c = QLabel("c", self)
        self.c.setGeometry(QRect(150, 130, 50, 100))

        self.a = QLineEdit(self)
        self.b = QLineEdit(self)
        self.c = QLineEdit(self)

        self.a.setGeometry(QRect(25, 190, 50, 50))
        self.b.setGeometry(QRect(75, 190, 50, 50))
        self.c.setGeometry(QRect(125, 190, 50, 50))

        self.a.setValidator(QIntValidator(1, 1000000000, self))
        self.b.setValidator(QIntValidator(1, 1000000000, self))
        self.c.setValidator(QIntValidator(1, 1000000000, self))

    def display(self):
        if self.a.text() != '' and self.b.text() != '' and self.c.text() != '':
            a = int(self.a.text())
            b = int(self.b.text())
            c = int(self.c.text())
            D = b**2 - 4*a*c
            if D < 0:      
                self.label.setText("Решений нет!")
            elif D == 0:
                resh = sympy.simplify(-b/(2*a))
                self.svg = QSvgWidget(self)
                self.svg.load(tex2svg(latex(resh)))
                self.svg.setGeometry(QRect(0, 50, 100, 100))
                self.svg.show()
            else:
                D = sympy.sqrt(D)
                resh1 = sympy.simplify((-b + D)/(2*a))
                resh2 = sympy.simplify((-b - D)/(2*a))

                #обращай внимание на self, если с self, то надо очищать QLabel, например True
                self.svg1 = QSvgWidget()              
                self.svg1.load(tex2svg(latex(resh1)))               
                self.svg1.setGeometry(QRect(0, 50, 50, 30))
                self.svg1.show()

                self.svg2 = QSvgWidget()
                self.svg2.load(tex2svg(latex(resh2)))
                self.svg2.setGeometry(QRect(0, 150, 50, 30))
                self.svg2.show()

    def go_mainwindow(self):
        self.mw = MainWindow()
        self.mw.show()
        self.hide()

##Информатика
class Dvoich(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Двоичный калькулятор")
        self.resize(910, 850)
        #self.move(300, 300)
        
        self.menu = QPushButton("В меню", self)
        self.menu.setGeometry(QRect(250, 20, 280, 100))
        self.menu.clicked.connect(self.go_info)

    def go_info(self):
        self.mw = Informatika()
        self.mw.show()
        self.hide()

class Perevod(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Перевод систем счисления")
        self.resize(910, 850)
        #self.move(300, 300)
        
        self.menu = QPushButton("В меню", self)
        self.menu.setGeometry(QRect(250, 20, 280, 100))
        self.menu.clicked.connect(self.go_info)

    def go_info(self):
        self.mw = Informatika()
        self.mw.show()
        self.hide()

##Геометрия
class SquaresOfFigures(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass

### SquaresOfFigures
class FlatShapes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass
class ThreeDimensionalFigures(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass
#### FlatShapes
class Triangle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass

##Комбинаторика
##Тригонометрия
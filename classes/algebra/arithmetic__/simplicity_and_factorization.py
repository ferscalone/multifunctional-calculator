from modules import *
from sympy import expand, symbols, factor

"""a = int(input())
k = Factor(a) Ans
l = set(k) 
s = ''
for i in l:
    s += str(factor(expand(symbols(str(i))**(k.count(i)))))
    s += " "
print(s)"""

class Simplicity_And_Factorization(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.initUI()
        self.parent_window = parent_window

    def initUI(self):
        self.setWindowTitle("Проверка числа на простоту и его факторизация")
        self.resize(910, 850)

        back_button = QPushButton("Назад", self)
        back_button.setGeometry(QRect(250, 20, 280, 100))
        back_button.clicked.connect(self.open_parent_window)

        self.number = QLineEdit(self)
        self.number.setGeometry(QRect(25, 190, 50, 50))
        self.number.setValidator(QIntValidator(1, 1000000000, self))

        prime_btn = QPushButton("Число простое?", self)
        prime_btn.setGeometry(QRect(250, 130, 280, 100))
        prime_btn.clicked.connect(self.IsPrime)

        fact_btn = QPushButton("Факторизация числа", self)
        fact_btn.setGeometry(QRect(250, 230, 280, 100))
        fact_btn.clicked.connect(self.Factor)

        self.svg_fact = QSvgWidget(self)
        self.svg_fact.setGeometry(QRect(530, 270, 100, 50))

        self.prime_label = QLabel(self)
        self.prime_label.setGeometry(QRect(530, 150, 100, 50))

    def Factor(self):
        if self.number.text() != "":
            n = int(self.number.text())
            Ans = []
            d = 2
            while d * d <= n:
                if n % d == 0:
                    Ans.append(d)
                    n //= d
                else:
                    d += 1
            if n > 1:
                Ans.append(n)

            listik = set(Ans)
            s = []
            for i in listik:
                s.append(latex(factor(expand(symbols(str(i)) ** (Ans.count(i))))))
            self.svg_fact.load(tex2svg("\cdot".join(s)))

    def IsPrime(self):
        if self.number.text() != "":
            n = int(self.number.text())
            d = 2
            while d * d <= n and n % d != 0:
                d += 1
            if d * d > n:
                self.prime_label.setText(" ДА")
            else:
                self.prime_label.setText(" Нет, оно составное")


    def open_parent_window(self):
        self.parent_window.show()
        self.close()
from modules import *

from sympy import expand, symbols, factor
def Factor(n):
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
    s = ""
    for i in listik:
        s += str(factor(expand(symbols(str(i)) ** (k.count(i)))))
        s += " "
    """s = "+".join(listik)"""
    return s

def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

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

    def open_parent_window(self):
        self.parent_window.show()
        self.close()
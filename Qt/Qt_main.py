import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from Qt.Qt_profile import Profile
from Qt.Qt_entrance import Entrance
from Qt.Qt_regestratione import Regestration
from Qt.Qt_deposit_money import Deposit_money

widget_wallet = None


class Widget_wallet(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files\\main_window.ui', self)
        self.UiComponents()
        print("Запуск")
        self.setWindowTitle('Крипто кошелёк (Лиза Ш.)')

    def UiComponents(self):
        self.regestratione.clicked.connect(self.reg)
        self.entrance.clicked.connect(self.ent)

        # Загрузка изображения и установка его в QLabel
        pixmap = QPixmap('image\\bitloin.png')
        self.label.setPixmap(pixmap)
        # self.label.setScaledContents(True)

    def ent(self):
        self.w2 = Entrance(self)
        self.w2.show()

    def reg(self):
        self.w2 = Regestration(self)
        self.w2.show()

    def start_profile(self, id):
        self.w2 = Profile(id, self)
        self.w2.show()

    def start_deposit_money(self, id):
        self.money = Deposit_money(id)
        self.money.show()


def startMain():
    app = QApplication(sys.argv)
    widget_wallet = Widget_wallet()
    widget_wallet.show()
    sys.exit(app.exec())

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton

from BD.DataBase import CryptoWalletDatabase


class Deposit(QMainWindow):
    def __init__(self, id):
        super().__init__()
        uic.loadUi('ui_files\\deposit_q.ui', self)
        self.id = id
        self.db = CryptoWalletDatabase("BD\\DataBase")
        self.setWindowTitle('Пополнение')
        self.db.connect()
        self.Ui_comp()
        self.index = None
        self.waluta = None

    def Ui_comp(self):
        self.back.clicked.connect(self.close_entr)
        self.dtposit_btn.clicked.connect(self.deposit_m)
        self.comboBox_deposit.activated.connect(self.activated)
        self.comboBox_deposit.currentTextChanged.connect(self.text_changed)
        self.comboBox_deposit.currentIndexChanged.connect(self.index_changed)
        self.No_deposit_btn.clicked.connect(self.close_entr)

    def close_entr(self):
        self.close()

    def deposit_m(self):
        result = list(self.db.all_maney(self.id)[0])[self.index]

        self.db.deposit_money(self.id, self.waluta, float(self.lineEdit_deposit.text()) + float(result))

    def activated(self, index):
        self.index = index
        print("Activated index:", index)

    def text_changed(self, s):
        self.waluta = s
        print("Text changed:", s)

    def index_changed(self, index):
        print("Index changed", index)

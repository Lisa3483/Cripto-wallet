from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton
from BD.DataBase import CryptoWalletDatabase


class Bringout(QMainWindow):
    def __init__(self, id):
        super().__init__()
        uic.loadUi('ui_files\\bringout_q.ui', self)
        self.id = id
        self.db = CryptoWalletDatabase("BD\\DataBase")
        self.setWindowTitle('Вывод средств')
        self.db.connect()
        self.Ui_comp()

    def Ui_comp(self):
        self.bringout_btn.clicked.connect(self.brigout_m)
        self.comboBox_bringout.activated.connect(self.activated)
        self.comboBox_bringout.currentTextChanged.connect(self.text_changed)
        self.comboBox_bringout.currentIndexChanged.connect(self.index_changed)
        self.No_bringout_btn.clicked.connect(self.close_entr)

    def brigout_m(self):
        result = list(self.db.all_maney(self.id)[0])[self.index]

        self.db.deposit_money(self.id, self.waluta,   float(result) - float(self.lineEdit_bringout.text()))

    def close_entr(self):
        self.close()

    def activated(self, index):
        self.index = index
        print("Activated index:", index)

    def text_changed(self, s):
        self.waluta = s
        print("Text changed:", s)

    def index_changed(self, index):
        print("Index changed", index)

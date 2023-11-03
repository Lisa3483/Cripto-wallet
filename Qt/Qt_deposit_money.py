from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

from BD.DataBase import CryptoWalletDatabase


class Deposit_money(QDialog):
    def __init__(self, id):
        super().__init__()
        uic.loadUi('ui_files\\deposit_money.ui', self)
        self.id = id
        self.db = CryptoWalletDatabase("BD\\DataBase")
        self.db.connect()
